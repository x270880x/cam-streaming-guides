#!/usr/bin/env python3
"""
Static page generator for cam-streaming-guides.

Generates one "how to stream on <platform>" guide per platform per language,
from a shared dark-theme template. Run:  python3 build.py

Output: <slug>/index.html (EN), ru/<slug>/index.html, es/<slug>/index.html
"""
import datetime
import html
import json
from pathlib import Path

from obs_content import OBS_VS
from model_content import MODEL_GUIDE, EARNINGS_FAQ

ROOT = Path(__file__).parent
OBS_SLUG = "obs-alternative"
MODEL_SLUG = "become-a-cam-model"
# Short localized footer label for the SplitCam-vs-OBS page (falls back to "SplitCam vs OBS").
OBS_NAV = {
    "en": "SplitCam vs OBS", "ru": "SplitCam vs OBS", "es": "SplitCam vs OBS",
    "de": "SplitCam vs OBS", "fr": "SplitCam vs OBS", "it": "SplitCam vs OBS",
    "pt": "SplitCam vs OBS", "nl": "SplitCam vs OBS", "ro": "SplitCam vs OBS",
    "bg": "SplitCam vs OBS", "hu": "SplitCam vs OBS", "el": "SplitCam vs OBS",
    "fi": "SplitCam vs OBS", "da": "SplitCam vs OBS", "no": "SplitCam vs OBS",
    "sr": "SplitCam vs OBS", "hr": "SplitCam vs OBS", "zh": "SplitCam vs OBS",
    "ja": "SplitCam vs OBS", "ar": "SplitCam مقابل OBS", "th": "SplitCam vs OBS",
    "fil": "SplitCam vs OBS", "tr": "SplitCam vs OBS", "id": "SplitCam vs OBS", "vi": "SplitCam vs OBS",
    "pl": "SplitCam vs OBS", "ko": "SplitCam vs OBS", "uk": "SplitCam проти OBS", "cs": "SplitCam vs OBS",
    "sk": "SplitCam vs OBS", "sv": "SplitCam vs OBS", "ms": "SplitCam vs OBS", "he": "SplitCam מול OBS", "fa": "SplitCam در مقابل OBS", "hi": "SplitCam बनाम OBS",
}
SITE = "https://camstreamguide.com"
DOWNLOAD_URL = "https://splitcam.com/download"   # software download (decision point — see README)
SITE_NAME = "Cam Stream Guide"


def nav_html(home, home_label, lang_sw=""):
    """Header nav: home/logo link (left) + site name top-right + lang switcher."""
    return (
        '<nav>'
        f'<a class="nav-home" href="{home}"><span class="dot"></span>'
        f'<span class="nav-home-t">{home_label}</span></a>'
        f'<div class="nav-right">{lang_sw}'
        f'<a class="nav-brand" href="{home}">{SITE_NAME}</a></div>'
        '</nav>'
    )
PUBLISHED_DATE = "2026-05-21"
MODIFIED_DATE = datetime.date.today().isoformat()
OG_LOCALE = {"en": "en_US", "ru": "ru_RU", "es": "es_ES",
             "de": "de_DE", "fr": "fr_FR", "it": "it_IT",
             "pt": "pt_BR", "nl": "nl_NL",
             "ro": "ro_RO", "bg": "bg_BG", "hu": "hu_HU",
             "el": "el_GR", "fi": "fi_FI", "da": "da_DK",
             "no": "nb_NO", "sr": "sr_RS", "hr": "hr_HR",
             "zh": "zh_CN", "ja": "ja_JP", "ar": "ar_AR",
             "th": "th_TH", "fil": "fil_PH", "tr": "tr_TR", "id": "id_ID", "vi": "vi_VN", "pl": "pl_PL",
             "ko": "ko_KR", "uk": "uk_UA", "cs": "cs_CZ", "sk": "sk_SK", "sv": "sv_SE", "ms": "ms_MY",
             "he": "he_IL", "fa": "fa_IR", "hi": "hi_IN"}
LANGS_AVAIL = ["en", "ru", "es", "de", "fr", "it", "pt", "nl",
               "ro", "bg", "hu", "el", "fi", "da", "no", "sr", "hr",
               "zh", "ja", "ar", "th", "fil", "tr", "id", "vi", "pl", "ko", "uk", "cs", "sk", "sv", "ms", "he", "fa", "hi"]  # set by main() to those with platforms_<lang>.py
RTL_LANGS = {"ar", "he", "fa"}  # languages that need dir="rtl" on <html>


# Inline JS that auto-redirects visitors to their browser-preferred language.
# - Honours a saved choice in localStorage (set when the user clicks the lang-switch)
# - Otherwise reads navigator.languages and redirects to the best matching locale
# - Hides <html> during the redirect to avoid a flash of the wrong language
LANG_REDIRECT_JS = """<script>
(function(){try{
var L=["en","ru","es","de","fr","it","pt","nl","ro","bg","hu","el","fi","da","no","sr","hr","zh","ja","ar","th","fil"];
var cur=document.documentElement.lang;
var path=location.pathname;
if(path.charAt(0)==="/")path=path.substring(1);
var parts=path.split("/");
if(L.indexOf(parts[0])>=0)parts.shift();
var slug=parts.join("/");
function go(lang){var p=lang==="en"?"/"+slug:"/"+lang+"/"+slug;if(p!==location.pathname){document.documentElement.style.visibility="hidden";location.replace(p+location.search+location.hash);}}
var stored;try{stored=localStorage.getItem("preferred_lang");}catch(e){}
if(stored&&L.indexOf(stored)>=0){if(stored!==cur)go(stored);}
else{var bl=navigator.languages||(navigator.language?[navigator.language]:[]);for(var i=0;i<bl.length;i++){var c=bl[i].toLowerCase().split("-")[0];if(c==="nb"||c==="nn")c="no";if(c==="tl")c="fil";if(L.indexOf(c)>=0){if(c!==cur)go(c);break;}}}
if(document.addEventListener){document.addEventListener("click",function(e){var t=e.target;while(t&&t!==document){if(t.tagName==="A"&&t.getAttribute&&t.getAttribute("data-lang")){try{localStorage.setItem("preferred_lang",t.getAttribute("data-lang"));}catch(e){}break;}t=t.parentNode;}},true);}
}catch(e){}})();
</script>"""

# Reveals the floating download button after the visitor scrolls past the hero,
# and hides it again while the footer download CTA is on screen (no double CTA).
STICKY_DL_JS = """<script>
(function(){var el=document.getElementById("stickyDl");if(!el)return;
var cta=document.querySelector(".cta-block"),ctaVis=false;
function upd(){var s=(window.scrollY||document.documentElement.scrollTop)>500;
if(s&&!ctaVis)el.classList.add("show");else el.classList.remove("show");}
if(window.IntersectionObserver&&cta){new IntersectionObserver(function(e){ctaVis=e[0].isIntersecting;upd();},{rootMargin:"0px 0px -10% 0px"}).observe(cta);}
window.addEventListener("scroll",upd,{passive:true});upd();})();
</script>"""
# Ahrefs Web Analytics (free, cookieless). Loaded async in every <head>.
AHREFS_JS = '<script src="https://analytics.ahrefs.com/analytics.js" data-key="xKzNuGcNdMMVQ1gW3UJZOw" async></script>'
PUBLISHER = {"@type": "Organization", "name": SITE_NAME, "url": f"{SITE}/"}

# ---------------------------------------------------------------- CSS (shared)
CSS = """
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{--app-base:#141420;--app-panel:#1c1c2e;--app-surface:#22223a;
--app-border:rgba(255,255,255,.08);--app-border2:rgba(255,255,255,.14);
--blue:#2878fc;--blue-hover:#4d8eff;--blue-dim:rgba(40,120,252,.13);
--purple:#9c5bff;--red:#ff5454;--green:#5ee572;
--text:#eeeeff;--text-sub:#9090bb;--text-dim:#50506a}
html{scroll-behavior:smooth;background:var(--app-base)}
body{font-family:'Geist',sans-serif;background:var(--app-base);color:var(--text);
line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
nav{position:fixed;top:0;left:0;right:0;z-index:100;height:60px;display:flex;
align-items:center;justify-content:space-between;padding:0 40px;
background:rgba(20,20,32,.85);backdrop-filter:blur(16px);
border-bottom:1px solid var(--app-border)}
.nav-home{display:flex;align-items:center;gap:9px;font-size:15px;font-weight:600;color:var(--text-sub);transition:color .15s}
.nav-home:hover{color:var(--text)}
.nav-home .dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;
background:linear-gradient(135deg,var(--blue),var(--purple))}
.nav-right{display:flex;align-items:center;gap:14px;min-width:0}
.nav-brand{font-size:19px;font-weight:800;letter-spacing:.2px;color:var(--text);white-space:nowrap}
.nav-brand:hover{color:var(--text)}
.nav-links{display:flex;gap:26px;list-style:none}
.nav-links a{font-size:14px;color:var(--text-sub);font-weight:500;transition:color .15s}
.nav-links a:hover{color:var(--text)}
.btn-primary{display:inline-flex;align-items:center;gap:7px;padding:10px 18px;
border-radius:8px;background:var(--blue);color:#fff;font-size:13px;font-weight:600;transition:background .15s}
.btn-primary:hover{background:var(--blue-hover)}
.btn-ghost{display:inline-flex;align-items:center;gap:7px;padding:10px 18px;border-radius:8px;
background:transparent;color:var(--text);border:1px solid var(--app-border2);
font-size:13px;font-weight:600;transition:all .15s}
.btn-lg{padding:13px 24px;font-size:14px;border-radius:10px}
.dl{position:relative;display:inline-block}
.dl>summary{list-style:none;cursor:pointer}
.dl>summary::-webkit-details-marker{display:none}
.dl>summary::marker{content:""}
.dl-caret{display:inline-block;font-size:11px;transition:transform .15s}
.dl[open] .dl-caret{transform:rotate(180deg)}
.dl-menu{position:absolute;top:calc(100% + 8px);left:0;min-width:220px;
background:var(--app-surface);border:1px solid var(--app-border2);border-radius:12px;
padding:6px;z-index:30;box-shadow:0 14px 36px rgba(0,0,0,.5)}
.dl-menu a{display:block;padding:11px 14px;border-radius:8px;font-size:14px;
font-weight:600;color:var(--text);transition:background .12s}
.dl-menu a:hover{background:var(--blue-dim)}
.lang-dl{position:relative;display:inline-block;flex-shrink:0}
.lang-dl>summary{list-style:none;cursor:pointer;padding:7px 11px;border:1px solid var(--app-border2);border-radius:8px;display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:600;color:var(--text);transition:background .15s;background:rgba(255,255,255,.02)}
.lang-dl>summary:hover{background:rgba(255,255,255,.06)}
.lang-dl>summary::-webkit-details-marker{display:none}
.lang-dl>summary::marker{content:""}
.lang-dl .lf{font-size:16px;line-height:1}
.lang-dl>summary .dl-caret{font-size:10px;color:var(--text-sub);margin-left:2px}
.lang-dl[open]>summary .dl-caret{transform:rotate(180deg)}
.lang-dl-menu{position:absolute;top:calc(100% + 8px);right:0;min-width:380px;max-height:75vh;overflow-y:auto;background:var(--app-surface);border:1px solid var(--app-border2);border-radius:12px;padding:6px;z-index:30;box-shadow:0 14px 36px rgba(0,0,0,.5);display:grid;grid-template-columns:1fr 1fr;gap:2px}
.lang-dl-menu a{display:flex;align-items:center;gap:8px;padding:9px 12px;border-radius:8px;font-size:13px;font-weight:600;color:var(--text);transition:background .12s}
.lang-dl-menu a:hover{background:var(--blue-dim)}
.lang-dl-menu a.cur{background:var(--blue);color:#fff}
.lang-dl-menu .ln{font-size:13px}
[dir="rtl"] .lang-dl-menu{right:auto;left:0}
@media (max-width:640px){.lang-dl-menu{min-width:280px;grid-template-columns:1fr;max-height:60vh}.lang-dl>summary .lc{display:none}}
.shot{margin:14px 0 2px;border:1px solid var(--app-border);border-radius:10px;overflow:hidden;background:var(--app-base)}
.shot img{display:block;width:100%;height:auto}
.shot figcaption{padding:9px 14px;font-size:12.5px;color:var(--text-sub);background:var(--app-surface);border-top:1px solid var(--app-border)}
.video-wrap{position:relative;width:100%;padding-bottom:56.25%;border-radius:14px;overflow:hidden;border:1px solid var(--app-border);background:#000}
.video-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.breadcrumbs{padding:80px 40px 0;max-width:900px;margin:0 auto;font-size:13px;color:var(--text-dim)}
.breadcrumbs a{color:var(--text-sub)}.breadcrumbs a:hover{color:var(--text)}
.breadcrumbs .sep{margin:0 8px}
.hero{padding:32px 40px 50px;max-width:900px;margin:0 auto;position:relative}
.hero-glow{position:absolute;top:-50px;right:-100px;width:480px;height:480px;
background:radial-gradient(circle,rgba(156,91,255,.15),transparent 70%);pointer-events:none;z-index:0}
.eyebrow{display:inline-block;padding:5px 12px;background:var(--blue-dim);color:var(--blue);
font-size:11.5px;font-weight:700;letter-spacing:.6px;text-transform:uppercase;
border-radius:99px;margin-bottom:18px;position:relative;z-index:1}
.h1{font-size:clamp(32px,4.4vw,48px);font-weight:800;line-height:1.07;letter-spacing:-1.4px;
margin-bottom:18px;max-width:760px;position:relative;z-index:1}
.h1 .accent{background:linear-gradient(135deg,var(--blue),var(--purple));
-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.sub{font-size:18px;color:var(--text-sub);max-width:660px;line-height:1.55;
margin-bottom:26px;position:relative;z-index:1}
.hero-cta{display:flex;gap:12px;flex-wrap:wrap;position:relative;z-index:1}
.hero-inner{display:grid;grid-template-columns:1fr 300px;gap:32px;align-items:center;position:relative;z-index:1}
.collab{background:linear-gradient(150deg,var(--app-panel),var(--app-surface));border:1px solid var(--app-border2);border-radius:18px;padding:28px 18px;display:flex;flex-direction:column;align-items:center;gap:14px;text-align:center}
.collab-flow{display:flex;align-items:center;justify-content:center}
.collab-pill{padding:11px 15px;border-radius:13px;font-weight:800;font-size:14px;color:#fff;box-shadow:0 10px 22px rgba(0,0,0,.4);white-space:nowrap;display:flex;align-items:center;gap:7px;line-height:1.1}
.collab-sc{background:linear-gradient(150deg,#26263f,#16161f);border:1px solid var(--app-border2)}
.collab-sc img{display:block;width:23px;height:23px}
.collab-sc span{font-size:15.5px;color:var(--text);font-weight:700}
.collab-logo{display:block;height:21px;width:auto;max-width:180px;
object-fit:contain;object-position:left center}
.collab-plat{padding:8px 15px}
.collab-plat img{height:24px;width:24px;border-radius:50%;object-fit:cover}
.collab-plat span{font-size:15.5px;color:var(--text);font-weight:700;white-space:nowrap}
.hub-card-icon{width:32px;height:32px;flex-shrink:0;border-radius:50%;
object-fit:cover;background:var(--app-surface)}
.hub-grid .related-card{display:flex;align-items:center;gap:14px;
padding:18px 20px}
.hub-grid .related-card .hub-card-body{flex:1;min-width:0}
.collab-wire{width:46px;height:4px;position:relative;flex-shrink:0;background:linear-gradient(90deg,rgba(255,255,255,.05),rgba(255,255,255,.16))}
.collab-dot{position:absolute;top:50%;width:12px;height:12px;border-radius:50%;background:var(--blue);box-shadow:0 0 13px 2px var(--blue);transform:translateY(-50%);animation:collabflow 1.7s cubic-bezier(.55,0,.45,1) infinite}
@keyframes collabflow{0%{left:-3px;opacity:0}14%{opacity:1}80%{opacity:1}100%{left:37px;opacity:0}}
.collab-plat{position:relative}
.collab-plat::after{content:"";position:absolute;inset:0;border-radius:13px;animation:collabrecv 1.7s ease-in-out infinite}
@keyframes collabrecv{0%,52%{box-shadow:0 0 0 0 rgba(255,255,255,0)}70%{box-shadow:0 0 0 5px rgba(255,255,255,.25)}100%{box-shadow:0 0 0 10px rgba(255,255,255,0)}}
.collab-label{font-size:11px;color:var(--text-sub);text-transform:uppercase;letter-spacing:.6px;font-weight:700}
.section{padding:40px 40px;max-width:900px;margin:0 auto}
.sec-h{font-size:30px;font-weight:700;letter-spacing:-.9px;line-height:1.15;margin-bottom:16px}
.sec-p{font-size:16px;color:var(--text-sub);line-height:1.7;margin-bottom:26px;max-width:680px}
.qa-box{padding:24px 28px;background:linear-gradient(135deg,rgba(40,120,252,.08),rgba(156,91,255,.05));
border:1px solid rgba(40,120,252,.25);border-radius:14px}
.qa-h{font-size:13px;font-weight:800;color:var(--blue);letter-spacing:.6px;
text-transform:uppercase;margin-bottom:12px}
.qa-text{font-size:15.5px;line-height:1.7;color:var(--text)}
.qa-text ol{margin:8px 0 0 22px}.qa-text li{margin-bottom:5px}
.steps{display:flex;flex-direction:column;gap:16px}
.step{display:flex;gap:22px;padding:22px 24px;background:var(--app-panel);
border:1px solid var(--app-border);border-radius:14px}
.step-num{flex:0 0 44px;height:44px;border-radius:11px;
background:linear-gradient(135deg,var(--blue),var(--purple));color:#fff;display:flex;
align-items:center;justify-content:center;font-weight:800;font-size:19px}
.step-body{flex:1}
.step-h{font-size:18px;font-weight:700;margin-bottom:7px;letter-spacing:-.3px}
.step-p{font-size:14.5px;color:var(--text-sub);line-height:1.65}
.step-p strong{color:var(--text)}
.tips-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.tip-card{padding:20px;background:var(--app-panel);border:1px solid var(--app-border);border-radius:12px}
.tip-card h3{font-size:15px;font-weight:700;margin-bottom:7px}
.tip-card p{font-size:13.5px;color:var(--text-sub);line-height:1.6}
.faq-list{display:flex;flex-direction:column;gap:10px}
.faq-item{padding:18px 22px;border:1px solid var(--app-border);border-radius:12px;
background:var(--app-panel)}
.faq-item summary{font-size:15.5px;font-weight:600;list-style:none;cursor:pointer;
display:flex;justify-content:space-between;gap:16px}
.faq-item summary::-webkit-details-marker{display:none}
.faq-item summary::after{content:"+";font-size:22px;color:var(--text-sub);font-weight:300}
.faq-item[open] summary::after{content:"\\2013"}
.faq-item p{margin-top:12px;color:var(--text-sub);font-size:14.5px;line-height:1.65}
.sp-block{padding:24px 26px;background:linear-gradient(135deg,rgba(40,120,252,.06),rgba(156,91,255,.04));border:1px solid var(--app-border2);border-radius:14px}
.sp-list{list-style:none;display:flex;flex-direction:column;gap:8px;margin:10px 0 16px}
.sp-row{display:flex;align-items:center;gap:12px;font-size:14.5px}
.sp-row .sp-icon{flex-shrink:0;font-size:17px;width:24px;text-align:center}
.sp-row a{color:var(--blue);word-break:break-all;font-weight:500}
.sp-row a:hover{color:var(--blue-hover);text-decoration:underline}
.sp-note{font-size:13px;color:var(--text-sub);line-height:1.55;margin-top:6px}
.cmp-wrap{overflow-x:auto;border:1px solid var(--app-border2);border-radius:14px;margin-top:8px}
.cmp{width:100%;border-collapse:collapse;font-size:14.5px;min-width:520px}
.cmp th,.cmp td{padding:13px 16px;text-align:left;border-bottom:1px solid var(--app-border)}
[dir="rtl"] .cmp th,[dir="rtl"] .cmp td{text-align:right}
.cmp thead th{background:var(--app-surface);font-weight:700;font-size:13.5px}
.cmp thead th:nth-child(2){color:var(--blue)}
.cmp tbody tr:last-child td{border-bottom:none}
.cmp td:first-child{color:var(--text-sub);font-weight:500}
.cmp td:nth-child(2){font-weight:600}
.cmp .ok{color:var(--green)}
.cmp-verdict{margin-top:22px;padding:22px 24px;background:linear-gradient(135deg,rgba(40,120,252,.08),rgba(156,91,255,.05));border:1px solid var(--app-border2);border-radius:14px;font-size:15px;line-height:1.65}
.sticky-dl{position:fixed;right:20px;bottom:20px;z-index:90;opacity:0;transform:translateY(14px);pointer-events:none;transition:opacity .25s ease,transform .25s ease}
.sticky-dl.show{opacity:1;transform:none;pointer-events:auto}
.sticky-dl a{display:inline-flex;align-items:center;gap:8px;padding:13px 22px;border-radius:999px;background:var(--blue);color:#fff;font-size:14px;font-weight:700;box-shadow:0 10px 30px rgba(40,120,252,.45);white-space:nowrap}
.sticky-dl a:hover{background:var(--blue-hover)}
[dir="rtl"] .sticky-dl{right:auto;left:20px}
@media (max-width:640px){.sticky-dl{right:12px;left:12px;bottom:12px}[dir="rtl"] .sticky-dl{right:12px;left:12px}.sticky-dl a{justify-content:center;width:100%}}
.related-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:16px}
.hub-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:16px}
.hub-grid .related-card{padding:20px 22px}
.hub-grid .related-card h4{font-size:16.5px}
.related-card{padding:16px 18px;background:var(--app-panel);border:1px solid var(--app-border);
border-radius:11px;transition:all .16s}
.related-card:hover{border-color:var(--blue);transform:translateY(-2px)}
.related-card h4{font-size:14.5px;font-weight:700}
.related-card p{font-size:12.5px;color:var(--text-sub);margin-top:3px}
.cta-block{padding:52px 40px;background:linear-gradient(135deg,var(--app-panel),var(--app-surface));
border-top:1px solid var(--app-border);border-bottom:1px solid var(--app-border);
text-align:center;margin-top:44px}
.cta-block h2{font-size:30px;font-weight:700;letter-spacing:-.8px;margin-bottom:12px}
.cta-block p{font-size:15.5px;color:var(--text-sub);max-width:520px;margin:0 auto 24px;line-height:1.6}
.meta-line{display:flex;align-items:center;gap:14px;padding:18px 20px 0;
font-size:13px;color:var(--text-sub)}
.age-tag{display:inline-flex;align-items:center;padding:3px 9px;border-radius:6px;
background:var(--red);color:#fff;font-size:11px;font-weight:800;letter-spacing:.5px}
.age-tag-sm{display:inline-block;padding:1px 6px;border-radius:4px;
background:var(--red);color:#fff;font-size:10px;font-weight:800;letter-spacing:.3px;
vertical-align:middle;margin-left:4px}
footer{padding:36px 40px;border-top:1px solid var(--app-border);background:var(--app-panel)}
.footer-inner{max-width:900px;margin:0 auto;display:flex;justify-content:space-between;
flex-wrap:wrap;gap:14px;font-size:13px;color:var(--text-dim)}
.footer-inner a{color:var(--text-sub)}.footer-inner a:hover{color:var(--text)}
.footer-links{display:flex;gap:22px;flex-wrap:wrap}
@media(max-width:900px){nav{padding:0 20px}.nav-links{display:none}
.breadcrumbs{padding:80px 20px 0}.hero,.section{padding-left:20px;padding-right:20px}
.cta-block{padding:44px 20px}.tips-grid,.related-grid,.hub-grid{grid-template-columns:1fr}
.step{flex-direction:column;gap:10px}footer{padding:30px 20px}
.footer-inner{flex-direction:column;text-align:center}
.hero-inner{grid-template-columns:1fr;gap:24px}
.collab{max-width:300px}}
@media(max-width:600px){nav{padding:0 16px}.nav-right{gap:10px}.nav-brand{font-size:16px}.nav-home-t{display:none}
.breadcrumbs{padding:78px 16px 0}.hero,.section{padding-left:16px;padding-right:16px}
.hero{padding-top:24px}.h1{font-size:clamp(25px,6.6vw,34px);letter-spacing:-.6px}
.sub{font-size:16px}.sec-h{font-size:23px;letter-spacing:-.4px}.cta-block h2{font-size:23px}
.eyebrow{font-size:12px}.cta-block{padding:38px 16px}footer{padding:28px 16px}}
@media(max-width:380px){.nav-brand{font-size:14px}.lang-dl>summary{padding:6px 8px}
.h1{font-size:23px}.sub{font-size:15px}.sec-h{font-size:20px}.btn-lg{padding:12px 18px;font-size:13px}}
"""

# ---------------------------------------------------------------- UI strings per language
UI = {
    "en": {"home": "All guides", "download": "Download SplitCam", "crumb_home": "Guides",
           "skip": "Skip to steps", "related": "Other platform guides",
           "quick": "Quick answer", "steps_h": "Step-by-step",
           "tips_h": "Pro tips", "faq_h": "FAQ", "cta_h": "Ready to go live?",
           "cta_p": "Free software. No watermark, no signup. Set up once, go live in one click.",
           "updated": "Last updated", "about": "About", "contact": "Contact",
           "privacy": "Privacy", "terms": "Terms",
           "path": "", "lang": "en"},
    "ru": {"home": "Все гайды", "download": "Скачать SplitCam", "crumb_home": "Гайды",
           "skip": "К шагам", "related": "Гайды по другим платформам",
           "quick": "Коротко", "steps_h": "Пошагово",
           "tips_h": "Советы", "faq_h": "Вопросы и ответы", "cta_h": "Готовы выйти в эфир?",
           "cta_p": "Бесплатная программа. Без водяного знака и регистрации. Настройка один раз — эфир в один клик.",
           "updated": "Обновлено", "about": "О проекте", "contact": "Контакты",
           "privacy": "Конфиденциальность", "terms": "Условия",
           "path": "ru/", "lang": "ru"},
    "es": {"home": "Todas las guías", "download": "Descargar SplitCam", "crumb_home": "Guías",
           "skip": "Ir a los pasos", "related": "Guías de otras plataformas",
           "quick": "Respuesta rápida", "steps_h": "Paso a paso",
           "tips_h": "Consejos", "faq_h": "Preguntas frecuentes", "cta_h": "¿Listo para emitir?",
           "cta_p": "Software gratuito. Sin marca de agua ni registro. Configúralo una vez y emite con un clic.",
           "updated": "Actualizado", "about": "Acerca de", "contact": "Contacto",
           "privacy": "Privacidad", "terms": "Términos",
           "path": "es/", "lang": "es"},
    "de": {"home": "Alle Anleitungen", "download": "SplitCam herunterladen", "crumb_home": "Anleitungen",
           "skip": "Zu den Schritten", "related": "Andere Plattform-Anleitungen",
           "quick": "Kurzantwort", "steps_h": "Schritt für Schritt",
           "tips_h": "Profi-Tipps", "faq_h": "FAQ", "cta_h": "Bereit für den Live-Stream?",
           "cta_p": "Kostenlose Software. Kein Wasserzeichen, keine Registrierung. Einmal einrichten, mit einem Klick live gehen.",
           "updated": "Zuletzt aktualisiert", "about": "Über uns", "contact": "Kontakt",
           "privacy": "Datenschutz", "terms": "Nutzungsbedingungen",
           "path": "de/", "lang": "de"},
    "fr": {"home": "Tous les guides", "download": "Télécharger SplitCam", "crumb_home": "Guides",
           "skip": "Aller aux étapes", "related": "Autres guides de plateforme",
           "quick": "En bref", "steps_h": "Pas à pas",
           "tips_h": "Astuces", "faq_h": "FAQ", "cta_h": "Prêt à passer en live ?",
           "cta_p": "Logiciel gratuit. Aucun filigrane, aucune inscription. Configurez une fois, lancez le direct en un clic.",
           "updated": "Mis à jour", "about": "À propos", "contact": "Contact",
           "privacy": "Confidentialité", "terms": "Conditions",
           "path": "fr/", "lang": "fr"},
    "it": {"home": "Tutte le guide", "download": "Scarica SplitCam", "crumb_home": "Guide",
           "skip": "Vai ai passaggi", "related": "Altre guide di piattaforma",
           "quick": "In breve", "steps_h": "Passo dopo passo",
           "tips_h": "Consigli", "faq_h": "FAQ", "cta_h": "Pronto a trasmettere in diretta?",
           "cta_p": "Software gratuito. Nessuna filigrana, nessuna registrazione. Configuralo una volta, vai live con un clic.",
           "updated": "Aggiornato", "about": "Chi siamo", "contact": "Contatti",
           "privacy": "Privacy", "terms": "Termini",
           "path": "it/", "lang": "it"},
    "pt": {"home": "Todos os guias", "download": "Baixar SplitCam", "crumb_home": "Guias",
           "skip": "Ir para os passos", "related": "Outros guias de plataforma",
           "quick": "Em resumo", "steps_h": "Passo a passo",
           "tips_h": "Dicas", "faq_h": "FAQ", "cta_h": "Pronto pra entrar ao vivo?",
           "cta_p": "Software grátis. Sem marca d'água, sem cadastro. Configure uma vez e entre ao vivo num clique.",
           "updated": "Atualizado", "about": "Sobre", "contact": "Contato",
           "privacy": "Privacidade", "terms": "Termos",
           "path": "pt/", "lang": "pt"},
    "nl": {"home": "Alle gidsen", "download": "SplitCam downloaden", "crumb_home": "Gidsen",
           "skip": "Naar de stappen", "related": "Andere platformgidsen",
           "quick": "Kort", "steps_h": "Stap voor stap",
           "tips_h": "Tips", "faq_h": "FAQ", "cta_h": "Klaar om live te gaan?",
           "cta_p": "Gratis software. Geen watermerk, geen account. Eenmaal instellen, met één klik live.",
           "updated": "Laatst bijgewerkt", "about": "Over", "contact": "Contact",
           "privacy": "Privacy", "terms": "Voorwaarden",
           "path": "nl/", "lang": "nl"},
    "ro": {"home": "Toate ghidurile", "download": "Descarcă SplitCam", "crumb_home": "Ghiduri",
           "skip": "La pași", "related": "Alte ghiduri de platforme",
           "quick": "Pe scurt", "steps_h": "Pas cu pas",
           "tips_h": "Sfaturi", "faq_h": "Întrebări frecvente", "cta_h": "Gata să intri live?",
           "cta_p": "Software gratuit. Fără filigran, fără cont. Configurezi o dată, intri live cu un clic.",
           "updated": "Actualizat", "about": "Despre", "contact": "Contact",
           "privacy": "Confidențialitate", "terms": "Termeni",
           "path": "ro/", "lang": "ro"},
    "bg": {"home": "Всички ръководства", "download": "Изтегли SplitCam", "crumb_home": "Ръководства",
           "skip": "Към стъпките", "related": "Други ръководства за платформи",
           "quick": "Накратко", "steps_h": "Стъпка по стъпка",
           "tips_h": "Съвети", "faq_h": "Често задавани въпроси", "cta_h": "Готов(а) ли си за ефир?",
           "cta_p": "Безплатен софтуер. Без воден знак, без регистрация. Настройваш веднъж, излизаш на живо с един клик.",
           "updated": "Обновено", "about": "За проекта", "contact": "Контакти",
           "privacy": "Поверителност", "terms": "Условия",
           "path": "bg/", "lang": "bg"},
    "hu": {"home": "Összes útmutató", "download": "SplitCam letöltése", "crumb_home": "Útmutatók",
           "skip": "Ugrás a lépésekhez", "related": "További platform-útmutatók",
           "quick": "Röviden", "steps_h": "Lépésről lépésre",
           "tips_h": "Tippek", "faq_h": "GYIK", "cta_h": "Készen állsz az élő adásra?",
           "cta_p": "Ingyenes szoftver. Vízjel nélkül, regisztráció nélkül. Egyszer beállítod, és egy kattintással élőben vagy.",
           "updated": "Frissítve", "about": "Rólunk", "contact": "Kapcsolat",
           "privacy": "Adatvédelem", "terms": "Feltételek",
           "path": "hu/", "lang": "hu"},
    "el": {"home": "Όλοι οι οδηγοί", "download": "Λήψη SplitCam", "crumb_home": "Οδηγοί",
           "skip": "Στα βήματα", "related": "Άλλοι οδηγοί πλατφορμών",
           "quick": "Σύντομη απάντηση", "steps_h": "Βήμα προς βήμα",
           "tips_h": "Συμβουλές", "faq_h": "Συχνές ερωτήσεις", "cta_h": "Έτοιμος για ζωντανή μετάδοση;",
           "cta_p": "Δωρεάν λογισμικό. Χωρίς υδατογράφημα, χωρίς εγγραφή. Στήσε μία φορά, βγες ζωντανά με ένα κλικ.",
           "updated": "Τελευταία ενημέρωση", "about": "Σχετικά", "contact": "Επικοινωνία",
           "privacy": "Απόρρητο", "terms": "Όροι",
           "path": "el/", "lang": "el"},
    "fi": {"home": "Kaikki oppaat", "download": "Lataa SplitCam", "crumb_home": "Oppaat",
           "skip": "Vaiheisiin", "related": "Muut alustaoppaat",
           "quick": "Lyhyesti", "steps_h": "Vaihe vaiheelta",
           "tips_h": "Vinkit", "faq_h": "UKK", "cta_h": "Valmis lähetykseen?",
           "cta_p": "Ilmainen ohjelmisto. Ei vesileimaa, ei rekisteröitymistä. Aseta kerran, mene livenä yhdellä klikkauksella.",
           "updated": "Päivitetty", "about": "Tietoja", "contact": "Yhteystiedot",
           "privacy": "Tietosuoja", "terms": "Ehdot",
           "path": "fi/", "lang": "fi"},
    "da": {"home": "Alle guides", "download": "Hent SplitCam", "crumb_home": "Guides",
           "skip": "Til trinene", "related": "Andre platformsguides",
           "quick": "Kort fortalt", "steps_h": "Trin for trin",
           "tips_h": "Tips", "faq_h": "FAQ", "cta_h": "Klar til at gå live?",
           "cta_p": "Gratis software. Intet vandmærke, ingen oprettelse. Sæt op én gang, gå live med ét klik.",
           "updated": "Senest opdateret", "about": "Om os", "contact": "Kontakt",
           "privacy": "Privatliv", "terms": "Vilkår",
           "path": "da/", "lang": "da"},
    "no": {"home": "Alle guider", "download": "Last ned SplitCam", "crumb_home": "Guider",
           "skip": "Til trinnene", "related": "Andre plattformguider",
           "quick": "Kort", "steps_h": "Steg for steg",
           "tips_h": "Tips", "faq_h": "FAQ", "cta_h": "Klar til å gå live?",
           "cta_p": "Gratis programvare. Uten vannmerke, uten konto. Sett opp én gang, gå live med ett klikk.",
           "updated": "Sist oppdatert", "about": "Om oss", "contact": "Kontakt",
           "privacy": "Personvern", "terms": "Vilkår",
           "path": "no/", "lang": "no"},
    "sr": {"home": "Сви водичи", "download": "Преузми SplitCam", "crumb_home": "Водичи",
           "skip": "На кораке", "related": "Други водичи за платформе",
           "quick": "Укратко", "steps_h": "Корак по корак",
           "tips_h": "Савети", "faq_h": "Честа питања", "cta_h": "Спреман(на) за пренос уживо?",
           "cta_p": "Бесплатан софтвер. Без водеяног жига, без регистрације. Подеси једном, иди уживо једним кликом.",
           "updated": "Ажурирано", "about": "О сајту", "contact": "Контакт",
           "privacy": "Приватност", "terms": "Услови",
           "path": "sr/", "lang": "sr"},
    "hr": {"home": "Svi vodiči", "download": "Preuzmi SplitCam", "crumb_home": "Vodiči",
           "skip": "Na korake", "related": "Drugi vodiči za platforme",
           "quick": "Ukratko", "steps_h": "Korak po korak",
           "tips_h": "Savjeti", "faq_h": "Česta pitanja", "cta_h": "Spreman(a) za prijenos uživo?",
           "cta_p": "Besplatan softver. Bez vodenog žiga, bez registracije. Postavi jednom, idi uživo jednim klikom.",
           "updated": "Ažurirano", "about": "O nama", "contact": "Kontakt",
           "privacy": "Privatnost", "terms": "Uvjeti",
           "path": "hr/", "lang": "hr"},
    "zh": {"home": "所有指南", "download": "下载 SplitCam", "crumb_home": "指南",
           "skip": "跳到步骤", "related": "其他平台指南",
           "quick": "快速回答", "steps_h": "分步指南",
           "tips_h": "专业提示", "faq_h": "常见问题", "cta_h": "准备开始直播了吗？",
           "cta_p": "免费软件。无水印，无需注册。一次设置，一键直播。",
           "updated": "最后更新", "about": "关于", "contact": "联系",
           "privacy": "隐私", "terms": "条款",
           "path": "zh/", "lang": "zh"},
    "ja": {"home": "すべてのガイド", "download": "SplitCamをダウンロード", "crumb_home": "ガイド",
           "skip": "手順へ", "related": "他のプラットフォームガイド",
           "quick": "簡単な答え", "steps_h": "ステップバイステップ",
           "tips_h": "プロのヒント", "faq_h": "よくある質問", "cta_h": "ライブ配信の準備はできましたか？",
           "cta_p": "無料ソフトウェア。透かしなし、登録不要。一度設定すれば、ワンクリックでライブ配信。",
           "updated": "最終更新", "about": "概要", "contact": "お問い合わせ",
           "privacy": "プライバシー", "terms": "利用規約",
           "path": "ja/", "lang": "ja"},
    "ar": {"home": "كل الأدلة", "download": "تحميل SplitCam", "crumb_home": "الأدلة",
           "skip": "الانتقال إلى الخطوات", "related": "أدلة منصات أخرى",
           "quick": "إجابة سريعة", "steps_h": "خطوة بخطوة",
           "tips_h": "نصائح احترافية", "faq_h": "الأسئلة الشائعة", "cta_h": "جاهز للبث المباشر؟",
           "cta_p": "برنامج مجاني. بدون علامة مائية، بدون تسجيل. إعداد لمرة واحدة، بث مباشر بنقرة واحدة.",
           "updated": "آخر تحديث", "about": "حول", "contact": "اتصل بنا",
           "privacy": "الخصوصية", "terms": "الشروط",
           "path": "ar/", "lang": "ar"},
    "th": {"home": "คู่มือทั้งหมด", "download": "ดาวน์โหลด SplitCam", "crumb_home": "คู่มือ",
           "skip": "ข้ามไปยังขั้นตอน", "related": "คู่มือแพลตฟอร์มอื่น",
           "quick": "คำตอบด่วน", "steps_h": "ทีละขั้นตอน",
           "tips_h": "เคล็ดลับ", "faq_h": "คำถามที่พบบ่อย", "cta_h": "พร้อมไลฟ์สดหรือยัง?",
           "cta_p": "ซอฟต์แวร์ฟรี ไม่มีลายน้ำ ไม่ต้องสมัคร ตั้งค่าครั้งเดียว ไลฟ์ได้ด้วยคลิกเดียว",
           "updated": "อัพเดทล่าสุด", "about": "เกี่ยวกับ", "contact": "ติดต่อ",
           "privacy": "ความเป็นส่วนตัว", "terms": "ข้อกำหนด",
           "path": "th/", "lang": "th"},
    "fil": {"home": "Lahat ng gabay", "download": "I-download ang SplitCam", "crumb_home": "Mga gabay",
            "skip": "Pumunta sa mga hakbang", "related": "Iba pang gabay sa platform",
            "quick": "Mabilis na sagot", "steps_h": "Hakbang-hakbang",
            "tips_h": "Mga tip", "faq_h": "FAQ", "cta_h": "Handa nang mag-live?",
            "cta_p": "Libreng software. Walang watermark, walang pagpaparehistro. Mag-set up minsan, mag-live sa isang click.",
            "updated": "Huling na-update", "about": "Tungkol sa", "contact": "Kontakin",
            "privacy": "Privacy", "terms": "Mga tuntunin",
            "path": "fil/", "lang": "fil"},
    "tr": {"home": "Tüm rehberler", "download": "SplitCam'i indir", "crumb_home": "Rehberler",
           "skip": "Adımlara geç", "related": "Diğer platform rehberleri",
           "quick": "Kısa cevap", "steps_h": "Adım adım",
           "tips_h": "Profesyonel ipuçları", "faq_h": "SSS", "cta_h": "Canlı yayına hazır mısın?",
           "cta_p": "Ücretsiz yazılım. Filigran yok, kayıt yok. Bir kez kur, tek tıkla canlıya geç.",
           "updated": "Son güncelleme", "about": "Hakkında", "contact": "İletişim",
           "privacy": "Gizlilik", "terms": "Koşullar",
           "path": "tr/", "lang": "tr"},
    "id": {"home": "Semua panduan", "download": "Unduh SplitCam", "crumb_home": "Panduan",
           "skip": "Lewat ke langkah", "related": "Panduan platform lain",
           "quick": "Jawaban singkat", "steps_h": "Langkah demi langkah",
           "tips_h": "Tips pro", "faq_h": "FAQ", "cta_h": "Siap untuk live?",
           "cta_p": "Software gratis. Tanpa watermark, tanpa daftar. Atur sekali, live dengan satu klik.",
           "updated": "Terakhir diperbarui", "about": "Tentang", "contact": "Kontak",
           "privacy": "Privasi", "terms": "Ketentuan",
           "path": "id/", "lang": "id"},
    "vi": {"home": "Tất cả hướng dẫn", "download": "Tải SplitCam", "crumb_home": "Hướng dẫn",
           "skip": "Tới các bước", "related": "Hướng dẫn nền tảng khác",
           "quick": "Trả lời nhanh", "steps_h": "Từng bước",
           "tips_h": "Mẹo chuyên nghiệp", "faq_h": "Câu hỏi thường gặp", "cta_h": "Sẵn sàng lên sóng?",
           "cta_p": "Phần mềm miễn phí. Không watermark, không đăng ký. Cài một lần, live bằng một cú nhấp.",
           "updated": "Cập nhật lần cuối", "about": "Giới thiệu", "contact": "Liên hệ",
           "privacy": "Quyền riêng tư", "terms": "Điều khoản",
           "path": "vi/", "lang": "vi"},
    "pl": {"home": "Wszystkie poradniki", "download": "Pobierz SplitCam", "crumb_home": "Poradniki",
           "skip": "Przejdź do kroków", "related": "Poradniki dla innych platform",
           "quick": "Szybka odpowiedź", "steps_h": "Krok po kroku",
           "tips_h": "Wskazówki dla profesjonalistów", "faq_h": "FAQ", "cta_h": "Gotowy, by wejść na żywo?",
           "cta_p": "Darmowe oprogramowanie. Bez znaku wodnego, bez rejestracji. Skonfiguruj raz, wejdź na żywo jednym kliknięciem.",
           "updated": "Ostatnia aktualizacja", "about": "O nas", "contact": "Kontakt",
           "privacy": "Prywatność", "terms": "Regulamin",
           "path": "pl/", "lang": "pl"},
    "ko": {"home": "모든 가이드", "download": "SplitCam 다운로드", "crumb_home": "가이드",
           "skip": "단계로 건너뛰기", "related": "다른 플랫폼 가이드",
           "quick": "빠른 답변", "steps_h": "단계별 안내",
           "tips_h": "프로 팁", "faq_h": "자주 묻는 질문", "cta_h": "라이브 방송 준비됐나요?",
           "cta_p": "무료 소프트웨어. 워터마크 없음, 가입 없음. 한 번 설정하고 한 번 클릭으로 라이브.",
           "updated": "마지막 업데이트", "about": "소개", "contact": "문의",
           "privacy": "개인정보", "terms": "이용약관",
           "path": "ko/", "lang": "ko"},
    "uk": {"home": "Усі посібники", "download": "Завантажити SplitCam", "crumb_home": "Посібники",
           "skip": "До кроків", "related": "Посібники для інших платформ",
           "quick": "Швидка відповідь", "steps_h": "Покроково",
           "tips_h": "Поради для профі", "faq_h": "Часті питання", "cta_h": "Готові вийти наживо?",
           "cta_p": "Безкоштовна програма. Без водяного знака, без реєстрації. Налаштуйте раз, вийдіть наживо одним кліком.",
           "updated": "Останнє оновлення", "about": "Про нас", "contact": "Контакти",
           "privacy": "Приватність", "terms": "Умови",
           "path": "uk/", "lang": "uk"},
    "cs": {"home": "Všechny návody", "download": "Stáhnout SplitCam", "crumb_home": "Návody",
           "skip": "Přejít na kroky", "related": "Návody pro jiné platformy",
           "quick": "Rychlá odpověď", "steps_h": "Krok za krokem",
           "tips_h": "Profi tipy", "faq_h": "Časté dotazy", "cta_h": "Připraveni jít živě?",
           "cta_p": "Software zdarma. Bez vodoznaku, bez registrace. Nastavte jednou, jděte živě jedním kliknutím.",
           "updated": "Naposledy aktualizováno", "about": "O nás", "contact": "Kontakt",
           "privacy": "Soukromí", "terms": "Podmínky",
           "path": "cs/", "lang": "cs"},
    "sk": {"home": "Všetky návody", "download": "Stiahnuť SplitCam", "crumb_home": "Návody",
           "skip": "Prejsť na kroky", "related": "Návody pre iné platformy",
           "quick": "Rýchla odpoveď", "steps_h": "Krok za krokom",
           "tips_h": "Profi tipy", "faq_h": "Časté otázky", "cta_h": "Pripravení ísť naživo?",
           "cta_p": "Softvér zadarmo. Bez vodoznaku, bez registrácie. Nastavte raz, choďte naživo jedným kliknutím.",
           "updated": "Naposledy aktualizované", "about": "O nás", "contact": "Kontakt",
           "privacy": "Súkromie", "terms": "Podmienky",
           "path": "sk/", "lang": "sk"},
    "sv": {"home": "Alla guider", "download": "Ladda ner SplitCam", "crumb_home": "Guider",
           "skip": "Hoppa till stegen", "related": "Guider för andra plattformar",
           "quick": "Snabbt svar", "steps_h": "Steg för steg",
           "tips_h": "Proffstips", "faq_h": "Vanliga frågor", "cta_h": "Redo att gå live?",
           "cta_p": "Gratis mjukvara. Ingen vattenstämpel, ingen registrering. Ställ in en gång, gå live med ett klick.",
           "updated": "Senast uppdaterad", "about": "Om oss", "contact": "Kontakt",
           "privacy": "Integritet", "terms": "Villkor",
           "path": "sv/", "lang": "sv"},
    "ms": {"home": "Semua panduan", "download": "Muat turun SplitCam", "crumb_home": "Panduan",
           "skip": "Langkau ke langkah", "related": "Panduan untuk platform lain",
           "quick": "Jawapan ringkas", "steps_h": "Langkah demi langkah",
           "tips_h": "Petua pro", "faq_h": "Soalan lazim", "cta_h": "Sedia untuk go live?",
           "cta_p": "Perisian percuma. Tiada tera air, tiada pendaftaran. Tetapkan sekali, go live dengan satu klik.",
           "updated": "Kemas kini terakhir", "about": "Tentang", "contact": "Hubungi",
           "privacy": "Privasi", "terms": "Terma",
           "path": "ms/", "lang": "ms"},
    "he": {"home": "כל המדריכים", "download": "הורדת SplitCam", "crumb_home": "מדריכים",
           "skip": "דלגו לשלבים", "related": "מדריכים לפלטפורמות אחרות",
           "quick": "תשובה מהירה", "steps_h": "שלב אחר שלב",
           "tips_h": "טיפים מקצועיים", "faq_h": "שאלות נפוצות", "cta_h": "מוכנים לעלות ללייב?",
           "cta_p": "תוכנה חינמית. ללא סימן מים, ללא הרשמה. הגדירו פעם אחת, עלו ללייב בלחיצה אחת.",
           "updated": "עודכן לאחרונה", "about": "אודות", "contact": "צור קשר",
           "privacy": "פרטיות", "terms": "תנאים",
           "path": "he/", "lang": "he"},
    "fa": {"home": "همه راهنماها", "download": "دانلود SplitCam", "crumb_home": "راهنماها",
           "skip": "رفتن به مراحل", "related": "راهنماهای پلتفرم‌های دیگر",
           "quick": "پاسخ سریع", "steps_h": "مرحله به مرحله",
           "tips_h": "نکات حرفه‌ای", "faq_h": "سؤالات متداول", "cta_h": "آماده پخش زنده هستید؟",
           "cta_p": "نرم‌افزار رایگان. بدون واترمارک، بدون ثبت‌نام. یک‌بار تنظیم کنید، با یک کلیک پخش کنید.",
           "updated": "آخرین به‌روزرسانی", "about": "درباره", "contact": "تماس با ما",
           "privacy": "حریم خصوصی", "terms": "شرایط",
           "path": "fa/", "lang": "fa"},
    "hi": {"home": "सभी गाइड", "download": "SplitCam डाउनलोड करें", "crumb_home": "गाइड",
           "skip": "चरणों पर जाएं", "related": "दूसरे प्लेटफ़ॉर्म के गाइड",
           "quick": "त्वरित उत्तर", "steps_h": "चरण दर चरण",
           "tips_h": "प्रो टिप्स", "faq_h": "अक्सर पूछे जाने वाले प्रश्न", "cta_h": "लाइव जाने के लिए तैयार हैं?",
           "cta_p": "मुफ़्त सॉफ़्टवेयर। कोई वॉटरमार्क नहीं, कोई रजिस्ट्रेशन नहीं। एक बार सेट करें, एक क्लिक में लाइव जाएं।",
           "updated": "अंतिम अपडेट", "about": "हमारे बारे में", "contact": "संपर्क",
           "privacy": "गोपनीयता", "terms": "शर्तें",
           "path": "hi/", "lang": "hi"},
}

def e(s):
    return html.escape(str(s), quote=True)


# Generic step templates. {name} = platform name, {key} = platform-specific instructions.
STEP_TMPL = {
    "en": [
        ("Download and install SplitCam",
         "SplitCam is free live-streaming software for Windows and macOS. Download it and run the "
         "installer — no signup, no card, no watermark, no time limit. It is the encoder that sends "
         "your video to {name}."),
        ("Set up your camera and scene",
         "Open SplitCam and add your webcam. Build your scene the way you want viewers to see it — "
         "add overlays, text, a second camera or your phone, beauty filters or an AI background. "
         "Everything is applied live before the stream leaves your PC."),
        ("Get your {name} stream key", "{key}"),
        ("Connect SplitCam to {name}",
         "In SplitCam open <strong>Stream Settings</strong>, paste the {name} server URL and stream "
         "key into the custom RTMP fields. Set the bitrate to 3,500–6,000&nbsp;Kbps for 1080p, "
         "2,000–4,000&nbsp;Kbps for 720p, and run the built-in speed test first."),
        ("Click Go Live",
         "Press <strong>Go Live</strong> in SplitCam, then start the broadcast on {name}. Within "
         "~10 seconds your camera feed is live. Subsequent streams are one click — open SplitCam, "
         "Go Live."),
    ],
    "ru": [
        ("Скачайте и установите SplitCam",
         "SplitCam — бесплатная программа для трансляций на Windows и macOS. Скачайте и запустите "
         "установщик — без регистрации, без водяного знака, без ограничения по времени. Именно "
         "SplitCam отправляет видео на {name}."),
        ("Настройте камеру и сцену",
         "Откройте SplitCam и добавьте веб-камеру. Соберите сцену как нужно — наложения, текст, "
         "вторая камера или телефон, бьюти-фильтры или AI-фон. Всё применяется в реальном времени "
         "до отправки потока."),
        ("Получите ключ трансляции {name}", "{key}"),
        ("Подключите SplitCam к {name}",
         "В SplitCam откройте <strong>Настройки трансляции</strong>, вставьте URL сервера и ключ "
         "{name} в поля custom RTMP. Битрейт: 3500–6000&nbsp;Кбит/с для 1080p, 2000–4000 для 720p. "
         "Сначала запустите встроенный тест скорости."),
        ("Нажмите Go Live",
         "Нажмите <strong>Go Live</strong> в SplitCam, затем запустите эфир на {name}. Через "
         "~10 секунд камера в эфире. Следующие трансляции — в один клик."),
    ],
    "es": [
        ("Descarga e instala SplitCam",
         "SplitCam es un software de streaming gratuito para Windows y macOS. Descárgalo y ejecuta "
         "el instalador — sin registro, sin marca de agua, sin límite de tiempo. SplitCam es el "
         "codificador que envía tu vídeo a {name}."),
        ("Configura tu cámara y escena",
         "Abre SplitCam y añade tu webcam. Monta la escena como quieras — superposiciones, texto, "
         "una segunda cámara o tu teléfono, filtros de belleza o un fondo con IA. Todo se aplica en "
         "directo antes de enviar el stream."),
        ("Consigue tu clave de stream de {name}", "{key}"),
        ("Conecta SplitCam a {name}",
         "En SplitCam abre <strong>Ajustes de stream</strong>, pega la URL del servidor y la clave "
         "de {name} en los campos RTMP personalizados. Bitrate: 3.500–6.000&nbsp;Kbps para 1080p. "
         "Ejecuta primero el test de velocidad."),
        ("Pulsa Go Live",
         "Pulsa <strong>Go Live</strong> en SplitCam y luego inicia la emisión en {name}. En unos "
         "~10 segundos tu cámara está en directo."),
    ],
    "de": [
        ("SplitCam herunterladen und installieren",
         "SplitCam ist eine kostenlose Streaming-Software für Windows und macOS. Lade sie herunter und führe den Installer aus — keine Registrierung, keine Kreditkarte, kein Wasserzeichen, kein Zeitlimit. SplitCam ist der Encoder, der dein Video an {name} sendet."),
        ("Kamera und Szene einrichten",
         "Öffne SplitCam und füge deine Webcam hinzu. Baue die Szene, wie deine Zuschauer sie sehen sollen — Overlays, Text, eine zweite Kamera oder dein Handy, Beauty-Filter oder KI-Hintergrund. Alles wird live angewendet, bevor der Stream deinen PC verlässt."),
        ("Hol dir deinen {name}-Stream-Key", "{key}"),
        ("SplitCam mit {name} verbinden",
         "Öffne in SplitCam <strong>Stream Settings</strong>, füge die {name}-Server-URL und den Stream-Key in die Custom-RTMP-Felder ein. Bitrate: 3.500–6.000&nbsp;Kbps für 1080p, 2.000–4.000&nbsp;Kbps für 720p. Starte zuerst den eingebauten Speedtest."),
        ("Auf Go Live klicken",
         "Drücke in SplitCam <strong>Go Live</strong> und starte dann die Übertragung auf {name}. In ~10 Sekunden ist deine Kamera live. Folgestreams sind ein Klick — SplitCam öffnen, Go Live."),
    ],
    "fr": [
        ("Téléchargez et installez SplitCam",
         "SplitCam est un logiciel de streaming gratuit pour Windows et macOS. Téléchargez-le et lancez l'installateur — pas d'inscription, pas de carte bancaire, pas de filigrane, pas de limite de temps. SplitCam est l'encodeur qui envoie votre vidéo vers {name}."),
        ("Configurez votre caméra et votre scène",
         "Ouvrez SplitCam et ajoutez votre webcam. Composez la scène telle que vous voulez que les spectateurs la voient — overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA. Tout s'applique en direct avant l'envoi du flux."),
        ("Récupérez votre clé de stream {name}", "{key}"),
        ("Connectez SplitCam à {name}",
         "Dans SplitCam, ouvrez <strong>Stream Settings</strong>, collez l'URL serveur et la clé de stream {name} dans les champs RTMP personnalisés. Débit : 3 500–6 000&nbsp;Kbps en 1080p, 2 000–4 000&nbsp;Kbps en 720p. Lancez d'abord le test de vitesse intégré."),
        ("Cliquez sur Go Live",
         "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis lancez la diffusion sur {name}. En ~10 secondes votre caméra est en direct. Les streams suivants se lancent en un clic — ouvrir SplitCam, Go Live."),
    ],
    "it": [
        ("Scarica e installa SplitCam",
         "SplitCam è un software di streaming gratuito per Windows e macOS. Scaricalo e avvia il programma di installazione — nessuna registrazione, nessuna carta, nessuna filigrana, nessun limite di tempo. SplitCam è l'encoder che invia il tuo video a {name}."),
        ("Configura la tua camera e la scena",
         "Apri SplitCam e aggiungi la webcam. Costruisci la scena come vuoi che i tuoi spettatori la vedano — sovrapposizioni, testo, una seconda camera o il telefono, filtri beauty o sfondo IA. Tutto si applica in diretta prima che lo stream lasci il PC."),
        ("Recupera la stream key di {name}", "{key}"),
        ("Connetti SplitCam a {name}",
         "In SplitCam apri <strong>Stream Settings</strong>, incolla l'URL del server e la stream key di {name} nei campi RTMP personalizzati. Bitrate: 3.500–6.000&nbsp;Kbps in 1080p, 2.000–4.000&nbsp;Kbps in 720p. Esegui prima lo speed test integrato."),
        ("Clicca su Go Live",
         "Premi <strong>Go Live</strong> in SplitCam, poi avvia la trasmissione su {name}. In ~10 secondi la tua camera è in diretta. Le trasmissioni successive partono con un clic — apri SplitCam, Go Live."),
    ],
    "pt": [
        ("Baixe e instale o SplitCam",
         "O SplitCam é um software de streaming grátis pra Windows e macOS. Baixe e rode o instalador — sem cadastro, sem cartão, sem marca d'água, sem limite de tempo. O SplitCam é o encoder que envia o seu vídeo pro {name}."),
        ("Configure sua câmera e a cena",
         "Abra o SplitCam e adicione a webcam. Monte a cena do jeito que quer que os espectadores vejam — sobreposições, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo com IA. Tudo é aplicado ao vivo antes do stream sair do PC."),
        ("Pegue sua stream key do {name}", "{key}"),
        ("Conecte o SplitCam ao {name}",
         "No SplitCam abra <strong>Stream Settings</strong>, cole a URL do servidor e a stream key do {name} nos campos RTMP personalizados. Bitrate: 3.500–6.000&nbsp;Kbps em 1080p, 2.000–4.000&nbsp;Kbps em 720p. Rode antes o teste de velocidade embutido."),
        ("Clique em Go Live",
         "Pressione <strong>Go Live</strong> no SplitCam e depois inicie a transmissão no {name}. Em ~10 segundos a câmera está ao vivo. As próximas transmissões saem com um clique — abrir SplitCam, Go Live."),
    ],
    "nl": [
        ("Download en installeer SplitCam",
         "SplitCam is gratis streamingsoftware voor Windows en macOS. Download en start het installatieprogramma — geen aanmelding, geen creditcard, geen watermerk, geen tijdslimiet. SplitCam is de encoder die je video naar {name} stuurt."),
        ("Stel je camera en scène in",
         "Open SplitCam en voeg je webcam toe. Bouw de scène zoals je kijkers hem moeten zien — overlays, tekst, een tweede camera of je telefoon, beautyfilters of een AI-achtergrond. Alles wordt live toegepast voordat de stream je pc verlaat."),
        ("Haal je stream key van {name}", "{key}"),
        ("Verbind SplitCam met {name}",
         "Open in SplitCam <strong>Stream Settings</strong>, plak de server-URL en de stream key van {name} in de aangepaste RTMP-velden. Bitrate: 3.500–6.000&nbsp;Kbps op 1080p, 2.000–4.000&nbsp;Kbps op 720p. Draai eerst de ingebouwde snelheidstest."),
        ("Klik op Go Live",
         "Druk in SplitCam op <strong>Go Live</strong> en start daarna de uitzending op {name}. Binnen ~10 seconden is je camera live. Volgende streams gaan met één klik — SplitCam openen, Go Live."),
    ],
    "ro": [
        ("Descarcă și instalează SplitCam",
         "SplitCam este software de streaming gratuit pentru Windows și macOS. Descarcă-l și rulează installerul — fără înregistrare, fără card, fără filigran, fără limită de timp. SplitCam este encoderul care îți trimite videoul către {name}."),
        ("Configurează camera și scena",
         "Deschide SplitCam și adaugă webcamul. Construiește scena așa cum vrei să o vadă spectatorii — suprapuneri, text, o a doua cameră sau telefonul, filtre beauty sau fundal AI. Totul se aplică live înainte ca streamul să plece din PC."),
        ("Obține cheia de stream {name}", "{key}"),
        ("Conectează SplitCam la {name}",
         "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului și cheia de stream {name} în câmpurile RTMP personalizate. Bitrate: 3.500–6.000&nbsp;Kbps la 1080p, 2.000–4.000&nbsp;Kbps la 720p. Rulează mai întâi testul de viteză integrat."),
        ("Apasă Go Live",
         "Apasă <strong>Go Live</strong> în SplitCam, apoi pornește transmisiunea pe {name}. În ~10 secunde camera ta este live. Următoarele streamuri se pornesc cu un singur clic — deschizi SplitCam, Go Live."),
    ],
    "bg": [
        ("Изтегли и инсталирай SplitCam",
         "SplitCam е безплатен софтуер за стрийминг за Windows и macOS. Изтегли го и пусни инсталатора — без регистрация, без карта, без воден знак, без времево ограничение. SplitCam е енкодерът, който изпраща видеото ти към {name}."),
        ("Настрой камера и сцена",
         "Отвори SplitCam и добави уебкамерата. Изгради сцената така, както искаш зрителите да я видят — наслагвания, текст, втора камера или телефонът, бюти филтри или AI фон. Всичко се прилага на живо, преди потокът да напусне компютъра."),
        ("Вземи стрийм ключа на {name}", "{key}"),
        ("Свържи SplitCam към {name}",
         "В SplitCam отвори <strong>Stream Settings</strong>, постави URL-а на сървъра и стрийм ключа на {name} в полетата за custom RTMP. Битрейт: 3500–6000&nbsp;Kbps за 1080p, 2000–4000&nbsp;Kbps за 720p. Първо пусни вградения тест за скорост."),
        ("Натисни Go Live",
         "Натисни <strong>Go Live</strong> в SplitCam, после стартирай излъчването на {name}. След ~10 секунди камерата е в ефир. Следващите трансляции тръгват с един клик — отваряш SplitCam, Go Live."),
    ],
    "hu": [
        ("Töltsd le és telepítsd a SplitCamet",
         "A SplitCam ingyenes streamelő szoftver Windowsra és macOS-re. Töltsd le és futtasd a telepítőt — regisztráció, kártya, vízjel és időkorlát nélkül. A SplitCam az enkóder, amely a videódat a {name} felé küldi."),
        ("Állítsd be a kamerát és a jelenetet",
         "Nyisd meg a SplitCamet és add hozzá a webkamerát. Építsd fel a jelenetet úgy, ahogy a nézők látni fogják — overlay-ek, szöveg, második kamera vagy a telefon, szépségszűrők vagy AI háttér. Minden élőben alkalmazódik, mielőtt a stream elhagyná a gépet."),
        ("Szerezd meg a {name} stream kulcsodat", "{key}"),
        ("Csatlakoztasd a SplitCamet a {name} platformhoz",
         "A SplitCamben nyisd meg a <strong>Stream Settings</strong> menüt, illeszd be a {name} szerver URL-t és a stream kulcsot a custom RTMP mezőkbe. Bitráta: 3500–6000&nbsp;Kbps 1080p-hez, 2000–4000&nbsp;Kbps 720p-hez. Először futtasd le a beépített sebességtesztet."),
        ("Kattints a Go Live gombra",
         "Nyomd meg a <strong>Go Live</strong> gombot a SplitCamben, majd indítsd el az adást a {name} oldalon. ~10 másodperc alatt élőben vagy. A következő streamek egy kattintással indulnak — megnyitod a SplitCamet, Go Live."),
    ],
    "el": [
        ("Κατέβασε και εγκατέστησε το SplitCam",
         "Το SplitCam είναι δωρεάν λογισμικό streaming για Windows και macOS. Κατέβασέ το και τρέξε τον installer — χωρίς εγγραφή, χωρίς κάρτα, χωρίς υδατογράφημα, χωρίς χρονικό όριο. Το SplitCam είναι ο encoder που στέλνει το βίντεό σου στο {name}."),
        ("Ρύθμισε κάμερα και σκηνή",
         "Άνοιξε το SplitCam και πρόσθεσε την webcam σου. Φτιάξε τη σκηνή όπως θέλεις να τη βλέπουν οι θεατές — overlays, κείμενο, δεύτερη κάμερα ή το κινητό, beauty φίλτρα ή AI φόντο. Όλα εφαρμόζονται ζωντανά πριν φύγει το stream από τον υπολογιστή."),
        ("Πάρε το stream key για {name}", "{key}"),
        ("Σύνδεσε το SplitCam στο {name}",
         "Στο SplitCam άνοιξε τα <strong>Stream Settings</strong>, επικόλλησε το server URL και το stream key του {name} στα πεδία custom RTMP. Bitrate: 3.500–6.000&nbsp;Kbps για 1080p, 2.000–4.000&nbsp;Kbps για 720p. Τρέξε πρώτα το ενσωματωμένο speed test."),
        ("Πάτησε Go Live",
         "Πάτησε <strong>Go Live</strong> στο SplitCam, μετά ξεκίνα την μετάδοση στο {name}. Σε ~10 δευτερόλεπτα η κάμερά σου είναι ζωντανή. Οι επόμενες μεταδόσεις ξεκινούν με ένα κλικ — ανοίγεις το SplitCam, Go Live."),
    ],
    "fi": [
        ("Lataa ja asenna SplitCam",
         "SplitCam on ilmainen suoratoisto-ohjelmisto Windowsille ja macOS:lle. Lataa se ja aja asennusohjelma — ei rekisteröitymistä, ei korttia, ei vesileimaa, ei aikarajaa. SplitCam on enkooderi, joka lähettää videosi alustalle {name}."),
        ("Aseta kamera ja näkymä",
         "Avaa SplitCam ja lisää webkamera. Rakenna näkymä sellaiseksi, kuin haluat katsojien näkevän — overlayt, teksti, toinen kamera tai puhelin, beauty-suodattimet tai AI-tausta. Kaikki sovelletaan livenä ennen kuin striimi lähtee koneelta."),
        ("Hanki {name}-striimiavain", "{key}"),
        ("Yhdistä SplitCam alustaan {name}",
         "Avaa SplitCamissa <strong>Stream Settings</strong>, liitä {name}-palvelimen URL ja striimiavain custom RTMP -kenttiin. Bitrate: 3 500–6 000&nbsp;Kbps 1080p:lle, 2 000–4 000&nbsp;Kbps 720p:lle. Aja ensin sisäänrakennettu nopeustesti."),
        ("Klikkaa Go Live",
         "Paina <strong>Go Live</strong> SplitCamissa, käynnistä sitten lähetys alustalla {name}. ~10 sekunnissa kamerasi on livenä. Seuraavat striimit lähtevät yhdellä klikkauksella."),
    ],
    "da": [
        ("Hent og installer SplitCam",
         "SplitCam er gratis streamingsoftware til Windows og macOS. Hent det og kør installationsprogrammet — ingen oprettelse, intet kort, intet vandmærke, ingen tidsbegrænsning. SplitCam er encoderen, der sender din video til {name}."),
        ("Sæt kamera og scene op",
         "Åbn SplitCam og tilføj webcammet. Byg scenen, som du ønsker seerne skal se den — overlays, tekst, et ekstra kamera eller telefonen, beauty-filtre eller AI-baggrund. Alt anvendes live, før streamen forlader din PC."),
        ("Hent din {name}-stream key", "{key}"),
        ("Forbind SplitCam til {name}",
         "I SplitCam åbn <strong>Stream Settings</strong>, indsæt {name}-server-URL og stream key i de tilpassede RTMP-felter. Bitrate: 3.500–6.000&nbsp;Kbps til 1080p, 2.000–4.000&nbsp;Kbps til 720p. Kør først den indbyggede hastighedstest."),
        ("Klik Go Live",
         "Tryk <strong>Go Live</strong> i SplitCam, og start derefter udsendelsen på {name}. På ~10 sekunder er dit kamera live. Næste streams starter med ét klik — åbn SplitCam, Go Live."),
    ],
    "no": [
        ("Last ned og installer SplitCam",
         "SplitCam er gratis strømmeprogramvare for Windows og macOS. Last ned og kjør installasjonsprogrammet — uten registrering, uten kort, uten vannmerke, uten tidsgrense. SplitCam er enkoderen som sender videoen din til {name}."),
        ("Sett opp kamera og scene",
         "Åpne SplitCam og legg til webkameraet. Bygg scenen slik du vil at seerne skal se den — overlays, tekst, et ekstra kamera eller telefonen, beauty-filtre eller AI-bakgrunn. Alt brukes live før strømmen forlater PC-en."),
        ("Hent {name}-strømnøkkelen din", "{key}"),
        ("Koble SplitCam til {name}",
         "I SplitCam åpne <strong>Stream Settings</strong>, lim inn {name}-server-URL og strømnøkkelen i custom RTMP-feltene. Bitrate: 3 500–6 000&nbsp;Kbps for 1080p, 2 000–4 000&nbsp;Kbps for 720p. Kjør først den innebygde hastighetstesten."),
        ("Klikk Go Live",
         "Trykk <strong>Go Live</strong> i SplitCam, og start så sendingen på {name}. På ~10 sekunder er kameraet ditt live. Neste strømmer starter med ett klikk — åpne SplitCam, Go Live."),
    ],
    "sr": [
        ("Преузми и инсталирај SplitCam",
         "SplitCam је бесплатан софтвер за стриминг за Windows и macOS. Преузми га и покрени инсталер — без регистрације, без картице, без воденог жига, без временског ограничења. SplitCam је енкодер који шаље твој видео ка {name}."),
        ("Подеси камеру и сцену",
         "Отвори SplitCam и додај веб камеру. Изгради сцену онако како желиш да је гледаоци виде — преклапања, текст, друга камера или телефон, бјути филтери или AI позадина. Све се примењује уживо пре него што стрим оде са рачунара."),
        ("Узми свој {name} стрим кључ", "{key}"),
        ("Повежи SplitCam са {name}",
         "У SplitCam-у отвори <strong>Stream Settings</strong>, налепи URL сервера и стрим кључ платформе {name} у custom RTMP поља. Bitrate: 3.500–6.000&nbsp;Kbps за 1080p, 2.000–4.000&nbsp;Kbps за 720p. Прво покрени уграђени тест брзине."),
        ("Кликни Go Live",
         "Притисни <strong>Go Live</strong> у SplitCam-у, затим покрени пренос на {name}. За ~10 секунди камера је уживо. Наредни стримови крећу једним кликом — отвориш SplitCam, Go Live."),
    ],
    "hr": [
        ("Preuzmi i instaliraj SplitCam",
         "SplitCam je besplatan softver za streaming za Windows i macOS. Preuzmi ga i pokreni instalacijski program — bez registracije, bez kartice, bez vodenog žiga, bez vremenskog ograničenja. SplitCam je enkoder koji šalje tvoj video prema {name}."),
        ("Postavi kameru i scenu",
         "Otvori SplitCam i dodaj web kameru. Izgradi scenu onako kako želiš da je gledatelji vide — preklapanja, tekst, druga kamera ili mobitel, beauty filtri ili AI pozadina. Sve se primjenjuje uživo prije nego stream napusti računalo."),
        ("Uzmi svoj {name} stream ključ", "{key}"),
        ("Spoji SplitCam s {name}",
         "U SplitCamu otvori <strong>Stream Settings</strong>, zalijepi URL servera i stream ključ platforme {name} u custom RTMP polja. Bitrate: 3.500–6.000&nbsp;Kbps za 1080p, 2.000–4.000&nbsp;Kbps za 720p. Prvo pokreni ugrađeni test brzine."),
        ("Klikni Go Live",
         "Pritisni <strong>Go Live</strong> u SplitCamu, zatim pokreni prijenos na {name}. Za ~10 sekundi kamera je uživo. Sljedeći streamovi kreću jednim klikom — otvoriš SplitCam, Go Live."),
    ],
    "zh": [
        ("下载并安装 SplitCam",
         "SplitCam 是适用于 Windows 和 macOS 的免费直播软件。下载并运行安装程序——无需注册、无需信用卡、无水印、无时间限制。SplitCam 是将您的视频发送到 {name} 的编码器。"),
        ("设置摄像头和场景",
         "打开 SplitCam 并添加网络摄像头。按照您希望观众看到的方式构建场景——叠加层、文本、第二个摄像头或手机、美颜滤镜或 AI 背景。所有内容都在直播流离开 PC 之前实时应用。"),
        ("获取您的 {name} 直播密钥", "{key}"),
        ("将 SplitCam 连接到 {name}",
         "在 SplitCam 中打开 <strong>Stream Settings</strong>，将 {name} 服务器 URL 和直播密钥粘贴到自定义 RTMP 字段中。比特率：1080p 为 3,500–6,000&nbsp;Kbps，720p 为 2,000–4,000&nbsp;Kbps。先运行内置的速度测试。"),
        ("点击 Go Live",
         "在 SplitCam 中按 <strong>Go Live</strong>，然后在 {name} 上开始直播。约 10 秒内您的摄像头就会上线。后续直播只需一键——打开 SplitCam，点击 Go Live。"),
    ],
    "ja": [
        ("SplitCamをダウンロードしてインストール",
         "SplitCamはWindowsとmacOS用の無料ライブ配信ソフトウェアです。ダウンロードしてインストーラーを実行してください — 登録不要、カード不要、透かしなし、時間制限なし。SplitCamは、あなたのビデオを{name}に送信するエンコーダーです。"),
        ("カメラとシーンをセットアップ",
         "SplitCamを開いてウェブカメラを追加します。視聴者に見せたいようにシーンを構築 — オーバーレイ、テキスト、2台目のカメラまたはスマートフォン、ビューティーフィルターやAI背景。すべてがストリームがPCを離れる前にライブで適用されます。"),
        ("{name}のストリームキーを取得", "{key}"),
        ("SplitCamを{name}に接続",
         "SplitCamで<strong>Stream Settings</strong>を開き、{name}のサーバーURLとストリームキーをカスタムRTMPフィールドに貼り付けます。ビットレート：1080pは3,500–6,000&nbsp;Kbps、720pは2,000–4,000&nbsp;Kbps。最初に内蔵の速度テストを実行してください。"),
        ("Go Liveをクリック",
         "SplitCamで<strong>Go Live</strong>を押してから、{name}で配信を開始。約10秒以内にカメラがライブになります。次回以降の配信はワンクリック — SplitCamを開いてGo Live。"),
    ],
    "ar": [
        ("قم بتنزيل وتثبيت SplitCam",
         "SplitCam هو برنامج بث مباشر مجاني لنظامي التشغيل Windows و macOS. قم بتنزيله وتشغيل المثبت — بدون تسجيل، بدون بطاقة، بدون علامة مائية، بدون حد زمني. SplitCam هو المُشفِّر الذي يرسل الفيديو الخاص بك إلى {name}."),
         ("إعداد الكاميرا والمشهد",
         "افتح SplitCam وأضف كاميرا الويب. ابنِ المشهد بالطريقة التي تريد أن يراه بها المشاهدون — التراكبات، النصوص، كاميرا ثانية أو هاتفك، مرشحات الجمال أو خلفية AI. يتم تطبيق كل شيء بشكل مباشر قبل أن يغادر البث جهازك."),
         ("احصل على مفتاح بث {name} الخاص بك", "{key}"),
         ("قم بتوصيل SplitCam بـ {name}",
         "في SplitCam، افتح <strong>Stream Settings</strong>، الصق عنوان URL لخادم {name} ومفتاح البث في حقول RTMP المخصصة. معدل البت: 3,500–6,000&nbsp;Kbps لـ 1080p، 2,000–4,000&nbsp;Kbps لـ 720p. شغّل اختبار السرعة المدمج أولاً."),
         ("انقر فوق Go Live",
         "اضغط على <strong>Go Live</strong> في SplitCam، ثم ابدأ البث على {name}. خلال ~10 ثوانٍ، تكون كاميرتك مباشرة. تبدأ عمليات البث اللاحقة بنقرة واحدة — افتح SplitCam، Go Live."),
    ],
    "th": [
        ("ดาวน์โหลดและติดตั้ง SplitCam",
         "SplitCam คือซอฟต์แวร์สตรีมมิ่งสดฟรีสำหรับ Windows และ macOS ดาวน์โหลดและรันตัวติดตั้ง — ไม่ต้องสมัคร ไม่ต้องใช้บัตร ไม่มีลายน้ำ ไม่มีขีดจำกัดเวลา SplitCam คือ encoder ที่ส่งวิดีโอของคุณไปยัง {name}"),
        ("ตั้งค่ากล้องและฉาก",
         "เปิด SplitCam และเพิ่มเว็บแคม สร้างฉากตามที่คุณต้องการให้ผู้ชมเห็น — โอเวอร์เลย์ ข้อความ กล้องที่สองหรือโทรศัพท์ ฟิลเตอร์ความงามหรือพื้นหลัง AI ทุกอย่างจะถูกนำมาใช้แบบสดก่อนที่สตรีมจะออกจากพีซีของคุณ"),
        ("รับสตรีมคีย์ {name} ของคุณ", "{key}"),
        ("เชื่อมต่อ SplitCam กับ {name}",
         "ใน SplitCam เปิด <strong>Stream Settings</strong> วาง URL เซิร์ฟเวอร์ {name} และสตรีมคีย์ในช่อง RTMP กำหนดเอง บิตเรต: 3,500–6,000&nbsp;Kbps สำหรับ 1080p, 2,000–4,000&nbsp;Kbps สำหรับ 720p เรียกใช้การทดสอบความเร็วในตัวก่อน"),
        ("คลิก Go Live",
         "กด <strong>Go Live</strong> ใน SplitCam จากนั้นเริ่มการถ่ายทอดสดบน {name} ภายในประมาณ 10 วินาที กล้องของคุณก็จะออนไลน์ การสตรีมครั้งต่อๆ ไปทำได้ด้วยคลิกเดียว — เปิด SplitCam, Go Live"),
    ],
    "fil": [
        ("I-download at i-install ang SplitCam",
         "Ang SplitCam ay libreng live-streaming software para sa Windows at macOS. I-download ito at patakbuhin ang installer — walang sign-up, walang card, walang watermark, walang time limit. Ito ang encoder na nagpapadala ng iyong video sa {name}."),
        ("I-set up ang iyong camera at scene",
         "Buksan ang SplitCam at idagdag ang iyong webcam. Buuin ang scene sa paraang gusto mong makita ng mga viewer — overlays, text, pangalawang camera o telepono, beauty filters o AI background. Ang lahat ay inilalapat nang live bago umalis ang stream sa iyong PC."),
        ("Kunin ang iyong {name} stream key", "{key}"),
        ("Ikonekta ang SplitCam sa {name}",
         "Sa SplitCam buksan ang <strong>Stream Settings</strong>, i-paste ang {name} server URL at stream key sa mga custom RTMP field. Bitrate: 3,500–6,000&nbsp;Kbps para sa 1080p, 2,000–4,000&nbsp;Kbps para sa 720p. Patakbuhin muna ang built-in speed test."),
        ("I-click ang Go Live",
         "Pindutin ang <strong>Go Live</strong> sa SplitCam, pagkatapos ay simulan ang broadcast sa {name}. Sa loob ng ~10 segundo, live na ang iyong camera. Ang mga susunod na stream ay isang click lang — buksan ang SplitCam, Go Live."),
    ],
    "tr": [
        ("SplitCam'i indir ve kur",
         "SplitCam, Windows ve macOS için ücretsiz bir canlı yayın yazılımıdır. İndir ve kurulumu çalıştır — kayıt yok, kart yok, filigran yok, süre sınırı yok. Videonu {name}'e gönderen kodlayıcıdır."),
        ("Kamera ve sahneni ayarla",
         "SplitCam'i aç ve web kameranı ekle. Sahneyi izleyicilerin görmesini istediğin gibi oluştur — katmanlar, metin, ikinci kamera veya telefonun, güzellik filtreleri veya AI arka plan. Hepsi yayın PC'den çıkmadan önce canlı uygulanır."),
        ("{name} yayın anahtarını al", "{key}"),
        ("SplitCam'i {name}'e bağla",
         "SplitCam'de <strong>Stream Settings</strong>'i aç, {name} sunucu URL'sini ve yayın anahtarını özel RTMP alanlarına yapıştır. Bitrate: 1080p için 3.500–6.000&nbsp;Kbps, 720p için 2.000–4.000&nbsp;Kbps. Önce yerleşik hız testini çalıştır."),
        ("Go Live'a tıkla",
         "SplitCam'de <strong>Go Live</strong>'a bas, sonra {name}'de yayını başlat. ~10 saniye içinde kameran canlıda. Sonraki yayınlar tek tık — SplitCam'i aç, Go Live."),
    ],
    "id": [
        ("Unduh dan pasang SplitCam",
         "SplitCam adalah software live-streaming gratis untuk Windows dan macOS. Unduh dan jalankan installer — tanpa daftar, tanpa kartu, tanpa watermark, tanpa batas waktu. Inilah encoder yang mengirim videomu ke {name}."),
        ("Atur kamera dan scene",
         "Buka SplitCam dan tambahkan webcam-mu. Susun scene seperti yang ingin dilihat penonton — overlay, teks, kamera kedua atau ponselmu, filter kecantikan atau latar AI. Semua diterapkan secara live sebelum stream meninggalkan PC-mu."),
        ("Ambil stream key {name}", "{key}"),
        ("Hubungkan SplitCam ke {name}",
         "Di SplitCam buka <strong>Stream Settings</strong>, tempel URL server dan stream key {name} ke kolom RTMP kustom. Atur bitrate ke 3.500–6.000&nbsp;Kbps untuk 1080p, 2.000–4.000&nbsp;Kbps untuk 720p, dan jalankan tes kecepatan bawaan dulu."),
        ("Klik Go Live",
         "Tekan <strong>Go Live</strong> di SplitCam, lalu mulai siaran di {name}. Dalam ~10 detik feed kameramu live. Siaran berikutnya cukup satu klik — buka SplitCam, Go Live."),
    ],
    "vi": [
        ("Tải và cài SplitCam",
         "SplitCam là phần mềm live-streaming miễn phí cho Windows và macOS. Tải và chạy trình cài đặt — không đăng ký, không thẻ, không watermark, không giới hạn thời gian. Đây là bộ mã hóa gửi video của bạn tới {name}."),
        ("Thiết lập camera và cảnh",
         "Mở SplitCam và thêm webcam. Dựng cảnh theo cách bạn muốn người xem thấy — overlay, chữ, camera thứ hai hoặc điện thoại, bộ lọc làm đẹp hoặc nền AI. Tất cả áp dụng trực tiếp trước khi luồng rời PC."),
        ("Lấy stream key {name}", "{key}"),
        ("Kết nối SplitCam với {name}",
         "Trong SplitCam mở <strong>Stream Settings</strong>, dán URL máy chủ và stream key của {name} vào ô RTMP tùy chỉnh. Đặt bitrate 3.500–6.000&nbsp;Kbps cho 1080p, 2.000–4.000&nbsp;Kbps cho 720p, và chạy bài test tốc độ tích hợp trước."),
        ("Nhấn Go Live",
         "Nhấn <strong>Go Live</strong> trong SplitCam, rồi bắt đầu phát trên {name}. Trong ~10 giây camera của bạn đã lên sóng. Những buổi sau chỉ một cú nhấp — mở SplitCam, Go Live."),
    ],
    "pl": [
        ("Pobierz i zainstaluj SplitCam",
         "SplitCam to darmowe oprogramowanie do transmisji na żywo dla Windows i macOS. Pobierz i uruchom instalator — bez rejestracji, bez karty, bez znaku wodnego, bez limitu czasu. To enkoder, który wysyła twoje wideo do {name}."),
        ("Skonfiguruj kamerę i scenę",
         "Otwórz SplitCam i dodaj kamerę. Zbuduj scenę tak, jak chcesz, by widzieli ją widzowie — nakładki, tekst, druga kamera lub telefon, filtry upiększające albo tło AI. Wszystko stosowane na żywo, zanim stream opuści twój komputer."),
        ("Pobierz klucz streamu {name}", "{key}"),
        ("Połącz SplitCam z {name}",
         "W SplitCam otwórz <strong>Stream Settings</strong>, wklej URL serwera i klucz streamu {name} w pola niestandardowego RTMP. Ustaw bitrate na 3500–6000&nbsp;Kbps dla 1080p, 2000–4000&nbsp;Kbps dla 720p i najpierw uruchom wbudowany test prędkości."),
        ("Kliknij Go Live",
         "Naciśnij <strong>Go Live</strong> w SplitCam, potem rozpocznij transmisję na {name}. W ~10 sekund twój obraz jest na żywo. Kolejne transmisje to jedno kliknięcie — otwórz SplitCam, Go Live."),
    ],
    "ko": [
        ("SplitCam 다운로드 및 설치",
         "SplitCam은 Windows와 macOS용 무료 라이브 방송 소프트웨어입니다. 다운로드하고 설치 프로그램을 실행하세요 — 가입 없음, 카드 없음, 워터마크 없음, 시간 제한 없음. 당신의 영상을 {name}로 보내는 인코더입니다."),
        ("카메라와 장면 설정",
         "SplitCam을 열고 웹캠을 추가하세요. 시청자가 볼 모습대로 장면을 구성하세요 — 오버레이, 텍스트, 두 번째 카메라나 휴대폰, 뷰티 필터나 AI 배경. 스트림이 PC를 떠나기 전에 모두 실시간 적용됩니다."),
        ("{name} 스트림 키 받기", "{key}"),
        ("SplitCam을 {name}에 연결",
         "SplitCam에서 <strong>Stream Settings</strong>를 열고 {name} 서버 URL과 스트림 키를 커스텀 RTMP 칸에 붙여넣으세요. 비트레이트는 1080p에 3,500–6,000&nbsp;Kbps, 720p에 2,000–4,000&nbsp;Kbps로 설정하고 먼저 내장 속도 테스트를 돌리세요."),
        ("Go Live 클릭",
         "SplitCam에서 <strong>Go Live</strong>를 누른 뒤 {name}에서 방송을 시작하세요. ~10초 안에 카메라가 라이브됩니다. 이후 방송은 한 번 클릭 — SplitCam 열고 Go Live."),
    ],
    "uk": [
        ("Завантажте та встановіть SplitCam",
         "SplitCam — безкоштовна програма для трансляцій на Windows і macOS. Завантажте й запустіть інсталятор — без реєстрації, без картки, без водяного знака, без обмеження часу. Це кодувальник, що надсилає ваше відео на {name}."),
        ("Налаштуйте камеру й сцену",
         "Відкрийте SplitCam і додайте вебкамеру. Зберіть сцену так, як хочете, щоб її бачили глядачі — оверлеї, текст, друга камера чи телефон, beauty-фільтри або AI-фон. Усе застосовується наживо, перш ніж стрим покине ваш ПК."),
        ("Отримайте ключ трансляції {name}", "{key}"),
        ("Під'єднайте SplitCam до {name}",
         "У SplitCam відкрийте <strong>Stream Settings</strong>, вставте URL сервера й ключ трансляції {name} у поля кастомного RTMP. Задайте бітрейт 3500–6000&nbsp;Кбіт/с для 1080p, 2000–4000&nbsp;Кбіт/с для 720p і спершу запустіть вбудований тест швидкості."),
        ("Натисніть Go Live",
         "Натисніть <strong>Go Live</strong> у SplitCam, далі почніть трансляцію на {name}. За ~10 секунд ваша камера наживо. Наступні трансляції — один клік: відкрийте SplitCam, Go Live."),
    ],
    "cs": [
        ("Stáhněte a nainstalujte SplitCam",
         "SplitCam je bezplatný software pro živé vysílání pro Windows a macOS. Stáhněte ho a spusťte instalátor — bez registrace, bez karty, bez vodoznaku, bez časového limitu. Je to kodér, který posílá vaše video na {name}."),
        ("Nastavte kameru a scénu",
         "Otevřete SplitCam a přidejte webkameru. Sestavte scénu tak, jak chcete, aby ji diváci viděli — překryvy, text, druhá kamera nebo telefon, beauty filtry nebo AI pozadí. Vše se aplikuje živě, než stream opustí váš PC."),
        ("Získejte stream key {name}", "{key}"),
        ("Připojte SplitCam k {name}",
         "Ve SplitCam otevřete <strong>Stream Settings</strong>, vložte URL serveru a stream key {name} do polí vlastního RTMP. Nastavte bitrate na 3500–6000&nbsp;Kbps pro 1080p, 2000–4000&nbsp;Kbps pro 720p a nejdřív spusťte vestavěný test rychlosti."),
        ("Klikněte na Go Live",
         "Stiskněte <strong>Go Live</strong> ve SplitCam, poté spusťte vysílání na {name}. Za ~10 sekund je vaše kamera živě. Další vysílání jsou na jedno kliknutí — otevřete SplitCam, Go Live."),
    ],
    "sk": [
        ("Stiahnite a nainštalujte SplitCam",
         "SplitCam je bezplatný softvér na živé vysielanie pre Windows a macOS. Stiahnite ho a spustite inštalátor — bez registrácie, bez karty, bez vodoznaku, bez časového limitu. Je to kodér, ktorý posiela vaše video na {name}."),
        ("Nastavte kameru a scénu",
         "Otvorte SplitCam a pridajte webkameru. Zostavte scénu tak, ako chcete, aby ju diváci videli — prekrytia, text, druhá kamera alebo telefón, beauty filtre alebo AI pozadie. Všetko sa aplikuje naživo, skôr než stream opustí váš PC."),
        ("Získajte stream key {name}", "{key}"),
        ("Pripojte SplitCam k {name}",
         "V SplitCam otvorte <strong>Stream Settings</strong>, vložte URL servera a stream key {name} do polí vlastného RTMP. Nastavte bitrate na 3500–6000&nbsp;Kbps pre 1080p, 2000–4000&nbsp;Kbps pre 720p a najprv spustite vstavaný test rýchlosti."),
        ("Kliknite na Go Live",
         "Stlačte <strong>Go Live</strong> v SplitCam, potom spustite vysielanie na {name}. Za ~10 sekúnd je vaša kamera naživo. Ďalšie vysielania sú na jedno kliknutie — otvorte SplitCam, Go Live."),
    ],
    "sv": [
        ("Ladda ner och installera SplitCam",
         "SplitCam är gratis livesändningsmjukvara för Windows och macOS. Ladda ner och kör installationsprogrammet — ingen registrering, inget kort, ingen vattenstämpel, ingen tidsgräns. Det är kodaren som skickar din video till {name}."),
        ("Ställ in kamera och scen",
         "Öppna SplitCam och lägg till din webbkamera. Bygg scenen som du vill att tittarna ska se den — overlays, text, andra kamera eller telefon, skönhetsfilter eller AI-bakgrund. Allt appliceras live innan streamen lämnar din dator."),
        ("Hämta streamnyckeln för {name}", "{key}"),
        ("Anslut SplitCam till {name}",
         "I SplitCam öppnar du <strong>Stream Settings</strong>, klistrar in {name} server-URL och streamnyckel i fälten för anpassad RTMP. Ställ in bitrate på 3500–6000&nbsp;Kbps för 1080p, 2000–4000&nbsp;Kbps för 720p och kör det inbyggda hastighetstestet först."),
        ("Klicka Go Live",
         "Tryck <strong>Go Live</strong> i SplitCam, starta sedan sändningen på {name}. Inom ~10 sekunder är din kamera live. Kommande sändningar är ett klick — öppna SplitCam, Go Live."),
    ],
    "ms": [
        ("Muat turun dan pasang SplitCam",
         "SplitCam ialah perisian penstriman langsung percuma untuk Windows dan macOS. Muat turun dan jalankan pemasang — tiada pendaftaran, tiada kad, tiada tera air, tiada had masa. Ia pengekod yang menghantar video anda ke {name}."),
        ("Tetapkan kamera dan adegan",
         "Buka SplitCam dan tambah kamera web. Bina adegan seperti yang anda mahu penonton lihat — tindihan, teks, kamera kedua atau telefon, penapis kecantikan atau latar AI. Semua dikenakan secara langsung sebelum strim meninggalkan PC anda."),
        ("Dapatkan kunci strim {name}", "{key}"),
        ("Sambung SplitCam ke {name}",
         "Dalam SplitCam buka <strong>Stream Settings</strong>, tampal URL pelayan dan kunci strim {name} ke medan RTMP tersuai. Tetapkan bitrate ke 3,500–6,000&nbsp;Kbps untuk 1080p, 2,000–4,000&nbsp;Kbps untuk 720p, dan jalankan ujian kelajuan terbina dahulu."),
        ("Klik Go Live",
         "Tekan <strong>Go Live</strong> dalam SplitCam, kemudian mula siaran di {name}. Dalam ~10 saat suapan kamera anda live. Siaran seterusnya hanya satu klik — buka SplitCam, Go Live."),
    ],
    "he": [
        ("הורידו והתקינו SplitCam",
         "‏SplitCam היא תוכנת שידור חי חינמית ל-Windows ו-macOS. הורידו והריצו את ההתקנה — ללא הרשמה, ללא כרטיס, ללא סימן מים, ללא הגבלת זמן. זה המקודד ששולח את הווידאו שלכם ל-{name}."),
        ("הגדירו מצלמה וסצנה",
         "פתחו SplitCam והוסיפו את המצלמה. בנו את הסצנה כפי שאתם רוצים שהצופים יראו — שכבות, טקסט, מצלמה שנייה או טלפון, מסנני יופי או רקע AI. הכול מוחל בזמן אמת לפני שהזרם עוזב את המחשב."),
        ("קבלו מפתח שידור של {name}", "{key}"),
        ("חברו את SplitCam ל-{name}",
         "ב-SplitCam פתחו <strong>Stream Settings</strong>, הדביקו את URL השרת ומפתח השידור של {name} בשדות ה-RTMP המותאם. הגדירו ביטרייט 3,500–6,000&nbsp;Kbps ל-1080p, 2,000–4,000&nbsp;Kbps ל-720p, והריצו קודם את בדיקת המהירות המובנית."),
        ("לחצו Go Live",
         "לחצו <strong>Go Live</strong> ב-SplitCam, ואז התחילו את השידור ב-{name}. תוך ~10 שניות המצלמה שלכם בלייב. השידורים הבאים בלחיצה אחת — פתחו SplitCam, Go Live."),
    ],
    "fa": [
        ("SplitCam را دانلود و نصب کنید",
         "SplitCam نرم‌افزار پخش زنده رایگان برای Windows و macOS است. آن را دانلود و نصب‌کننده را اجرا کنید — بدون ثبت‌نام، بدون کارت، بدون واترمارک، بدون محدودیت زمانی. این رمزگذاری است که ویدیوی شما را به {name} ارسال می‌کند."),
        ("دوربین و صحنه را تنظیم کنید",
         "SplitCam را باز کنید و وب‌کم خود را اضافه کنید. صحنه را همان‌طور که می‌خواهید بینندگان ببینند بسازید — پوشش‌ها، متن، دوربین دوم یا تلفن، فیلترهای زیبایی یا پس‌زمینه هوش مصنوعی. همه چیز قبل از ترک جریان از رایانه به صورت زنده اعمال می‌شود."),
        ("کلید جریان {name} را دریافت کنید", "{key}"),
        ("SplitCam را به {name} متصل کنید",
         "در SplitCam <strong>Stream Settings</strong> را باز کنید، URL سرور و کلید جریان {name} را در فیلدهای RTMP سفارشی جای‌گذاری کنید. بیت‌ریت را ۳۵۰۰–۶۰۰۰&nbsp;Kbps برای ۱۰۸۰p، ۲۰۰۰–۴۰۰۰&nbsp;Kbps برای ۷۲۰p تنظیم کنید و ابتدا تست سرعت داخلی را اجرا کنید."),
        ("Go Live را کلیک کنید",
         "در SplitCam <strong>Go Live</strong> را فشار دهید، سپس پخش را در {name} شروع کنید. ظرف ~۱۰ ثانیه دوربین شما زنده می‌شود. پخش‌های بعدی با یک کلیک — SplitCam را باز کنید، Go Live."),
    ],
    "hi": [
        ("SplitCam डाउनलोड और इंस्टॉल करें",
         "SplitCam Windows और macOS के लिए मुफ़्त लाइव स्ट्रीमिंग सॉफ़्टवेयर है। इसे डाउनलोड करें और इंस्टॉलर चलाएं — कोई रजिस्ट्रेशन नहीं, कोई कार्ड नहीं, कोई वॉटरमार्क नहीं, कोई समय सीमा नहीं। यह एन्कोडर है जो आपका वीडियो {name} को भेजता है।"),
        ("कैमरा और सीन सेट करें",
         "SplitCam खोलें और वेबकैम जोड़ें। सीन बनाएं जैसा आप चाहते हैं कि दर्शक देखें — ओवरले, टेक्स्ट, दूसरा कैमरा या फ़ोन, ब्यूटी फ़िल्टर या AI बैकग्राउंड। सब कुछ स्ट्रीम PC छोड़ने से पहले लाइव अप्लाई होता है।"),
        ("{name} की स्ट्रीम की प्राप्त करें", "{key}"),
        ("SplitCam को {name} से कनेक्ट करें",
         "SplitCam में <strong>Stream Settings</strong> खोलें, {name} का सर्वर URL और स्ट्रीम की कस्टम RTMP फ़ील्ड में पेस्ट करें। बिटरेट 1080p के लिए 3500–6000&nbsp;Kbps, 720p के लिए 2000–4000&nbsp;Kbps सेट करें और पहले बिल्ट-इन स्पीड टेस्ट चलाएं।"),
        ("Go Live क्लिक करें",
         "SplitCam में <strong>Go Live</strong> दबाएं, फिर {name} पर ब्रॉडकास्ट शुरू करें। ~10 सेकंड में आपका कैमरा लाइव है। अगली स्ट्रीम एक क्लिक में — SplitCam खोलें, Go Live।"),
    ],
}


def build_steps(p, lang):
    """Build the 5-step list for a platform.

    d['steps'] may override the shared template. It can be a full list of
    (head, body) tuples, or a list where some entries are None — a None entry
    falls back to the shared template, so a platform can customise only the
    steps that differ and keep generic ones (install, key) shared."""
    d = p[lang]
    custom = d.get("steps")
    name = p["name"]
    out = []
    for idx, (head, body) in enumerate(STEP_TMPL[lang]):
        if custom and idx < len(custom) and custom[idx]:
            out.append(custom[idx])
        else:
            out.append((head.replace("{name}", name),
                        body.replace("{name}", name).replace("{key}", d.get("key_how", ""))))
    return out


# Localized "Troubleshooting" heading per language.
TROUBLE_H = {
    "en": "Troubleshooting", "ru": "Решение проблем", "es": "Solución de problemas",
    "de": "Fehlerbehebung", "fr": "Dépannage", "it": "Risoluzione dei problemi",
    "pt": "Solução de problemas", "nl": "Problemen oplossen", "ro": "Depanare",
    "bg": "Решаване на проблеми", "hu": "Hibaelhárítás", "el": "Αντιμετώπιση προβλημάτων",
    "fi": "Vianmääritys", "da": "Fejlfinding", "no": "Feilsøking", "sr": "Решавање проблема",
    "hr": "Rješavanje problema", "zh": "故障排除", "ja": "トラブルシューティング",
    "ar": "استكشاف الأخطاء وإصلاحها", "th": "การแก้ไขปัญหา", "fil": "Pag-troubleshoot",
    "tr": "Sorun giderme",
    "id": "Pemecahan masalah",
    "vi": "Khắc phục sự cố",
    "pl": "Rozwiązywanie problemów",
    "ko": "문제 해결",
    "uk": "Усунення несправностей",
    "cs": "Řešení problémů",
    "sk": "Riešenie problémov",
    "sv": "Felsökning",
    "ms": "Penyelesaian masalah",
    "he": "פתרון בעיות",
    "fa": "عیب‌یابی",
    "hi": "समस्या निवारण",
}

# Common encoder-level streaming problems and fixes. {name} = platform name.
# Each entry is (problem, solution). Universal across platforms; the platform
# name is woven in so every page stays unique.
TROUBLE_TMPL = {
    "en": [
        ("Your {name} stream lags or buffers",
         "Almost always the bitrate is higher than your upload can sustain. Run SplitCam's built-in speed test, then set the bitrate to about 75% of your measured upload — 3,500–6,000&nbsp;Kbps for 1080p, lower for 720p. The lag clears once the encoder stops outrunning your connection."),
        ("Dropped frames during the {name} broadcast",
         "Dropped frames mean packets aren't reaching {name} in time — usually unstable Wi-Fi. Switch to a wired Ethernet connection, close bandwidth-heavy apps, and lower the bitrate a notch. One spike is fine; a steady climb means the connection can't keep up."),
        ("Black screen — viewers see no video on {name}",
         "Your camera isn't selected as the active source in SplitCam, or another app is holding it. Close Zoom, Skype or OBS, pick your webcam again in SplitCam's source list, and confirm the preview shows your feed before you press Go Live."),
        ("{name} rejects the stream key or won't connect",
         "Re-copy the stream key — a trailing space or an old, rotated key is the usual cause. Confirm the server URL matches the one {name} shows and that external-encoder broadcasting is enabled on your account. A green slider in SplitCam's Stream Settings confirms a valid key."),
        ("No audio or audio is out of sync on {name}",
         "Pick SplitCam as both the camera and the microphone, and select your real mic inside SplitCam's audio source. If audio drifts behind the video, lower the resolution one step — the encoder is overloaded and the audio is waiting on late frames."),
    ],
    "ru": [
        ("Трансляция на {name} лагает или буферизует",
         "Почти всегда битрейт выше, чем тянет ваш аплоад. Запустите встроенный тест скорости SplitCam и выставьте битрейт примерно на 75% от измеренного аплоада — 3500–6000&nbsp;Кбит/с для 1080p, ниже для 720p. Лаги уходят, как только энкодер перестаёт обгонять соединение."),
        ("Потеря кадров во время эфира на {name}",
         "Потеря кадров значит, что пакеты не доходят до {name} вовремя — обычно нестабильный Wi-Fi. Перейдите на проводной Ethernet, закройте программы, жрущие канал, и чуть снизьте битрейт. Единичный скачок — норма; устойчивый рост значит, что соединение не справляется."),
        ("Чёрный экран — зрители не видят видео на {name}",
         "Камера не выбрана активным источником в SplitCam, или её держит другая программа. Закройте Zoom, Skype или OBS, выберите веб-камеру заново в списке источников SplitCam и убедитесь, что превью показывает картинку до нажатия Go Live."),
        ("{name} не принимает ключ трансляции или не подключается",
         "Скопируйте ключ заново — обычно причина в лишнем пробеле или старом, уже сброшенном ключе. Проверьте, что URL сервера совпадает с показанным в {name} и что вещание через внешний энкодер включено на аккаунте. Зелёный слайдер в Настройках трансляции SplitCam подтверждает валидный ключ."),
        ("Нет звука или звук рассинхронизирован на {name}",
         "Выберите SplitCam и как камеру, и как микрофон, а внутри SplitCam укажите ваш реальный микрофон источником звука. Если звук отстаёт от видео, снизьте разрешение на ступень — энкодер перегружен и звук ждёт опаздывающие кадры."),
    ],
    "es": [
        ("Tu emisión en {name} va con lag o se entrecorta",
         "Casi siempre el bitrate es más alto de lo que aguanta tu subida. Ejecuta el test de velocidad de SplitCam y pon el bitrate en torno al 75% de tu subida medida — 3.500–6.000&nbsp;Kbps para 1080p, menos para 720p. El lag desaparece cuando el codificador deja de ir por delante de tu conexión."),
        ("Fotogramas perdidos durante la emisión en {name}",
         "Los fotogramas perdidos significan que los paquetes no llegan a tiempo a {name} — normalmente Wi-Fi inestable. Cambia a conexión por cable Ethernet, cierra apps que consuman ancho de banda y baja un poco el bitrate. Un pico puntual está bien; un aumento constante indica que la conexión no da abasto."),
        ("Pantalla negra — los espectadores no ven vídeo en {name}",
         "Tu cámara no está seleccionada como fuente activa en SplitCam, o la retiene otra app. Cierra Zoom, Skype u OBS, vuelve a elegir tu webcam en la lista de fuentes de SplitCam y confirma que la vista previa muestra tu imagen antes de pulsar Go Live."),
        ("{name} rechaza la clave de stream o no conecta",
         "Vuelve a copiar la clave — un espacio sobrante o una clave antigua ya rotada es la causa habitual. Confirma que la URL del servidor coincide con la que muestra {name} y que la emisión por codificador externo está activada en tu cuenta. Un slider verde en los Ajustes de stream de SplitCam confirma una clave válida."),
        ("Sin audio o audio desincronizado en {name}",
         "Elige SplitCam como cámara y como micrófono, y selecciona tu micro real dentro de la fuente de audio de SplitCam. Si el audio se atrasa respecto al vídeo, baja la resolución un paso — el codificador está sobrecargado y el audio espera fotogramas que llegan tarde."),
    ],
    "de": [
        ("Dein {name}-Stream ruckelt oder puffert",
         "Fast immer ist die Bitrate höher, als dein Upload verkraftet. Führe den eingebauten Speedtest von SplitCam aus und stell die Bitrate auf etwa 75% deines gemessenen Uploads — 3.500–6.000&nbsp;Kbps für 1080p, weniger für 720p. Das Ruckeln verschwindet, sobald der Encoder deine Verbindung nicht mehr überholt."),
        ("Dropped Frames während der {name}-Übertragung",
         "Dropped Frames bedeuten, dass Pakete {name} nicht rechtzeitig erreichen — meist instabiles WLAN. Wechsle zu einer kabelgebundenen Ethernet-Verbindung, schließe bandbreitenhungrige Apps und senke die Bitrate etwas. Ein einzelner Ausschlag ist okay; ein stetiger Anstieg heißt, die Verbindung kommt nicht mit."),
        ("Schwarzer Bildschirm — Zuschauer sehen kein Video auf {name}",
         "Deine Kamera ist nicht als aktive Quelle in SplitCam gewählt, oder eine andere App belegt sie. Schließe Zoom, Skype oder OBS, wähle deine Webcam erneut in der Quellenliste von SplitCam und prüfe, dass die Vorschau dein Bild zeigt, bevor du Go Live drückst."),
        ("{name} lehnt den Stream-Key ab oder verbindet nicht",
         "Kopiere den Stream-Key erneut — ein Leerzeichen am Ende oder ein alter, bereits zurückgesetzter Key ist die übliche Ursache. Prüfe, dass die Server-URL mit der von {name} angezeigten übereinstimmt und dass External-Encoder-Übertragung in deinem Konto aktiviert ist. Ein grüner Slider in den Stream Settings von SplitCam bestätigt einen gültigen Key."),
        ("Kein Ton oder Ton asynchron auf {name}",
         "Wähle SplitCam sowohl als Kamera als auch als Mikrofon, und stell dein echtes Mikro innerhalb der Audioquelle von SplitCam ein. Wenn der Ton hinter dem Video herhinkt, senke die Auflösung um eine Stufe — der Encoder ist überlastet und der Ton wartet auf verspätete Frames."),
    ],
    "fr": [
        ("Ton stream {name} rame ou met en mémoire tampon",
         "La cause est presque toujours un débit supérieur à ce que ton upload supporte. Lance le test de vitesse intégré de SplitCam, puis règle le débit à environ 75% de ton upload mesuré — 3 500–6 000&nbsp;Kbps en 1080p, moins en 720p. Le lag disparaît dès que l'encodeur cesse de dépasser ta connexion."),
        ("Images perdues pendant la diffusion sur {name}",
         "Les images perdues signifient que les paquets n'atteignent pas {name} à temps — souvent du Wi-Fi instable. Passe à une connexion Ethernet filaire, ferme les applis gourmandes en bande passante et baisse un peu le débit. Un pic isolé est normal ; une hausse continue veut dire que la connexion ne suit pas."),
        ("Écran noir — les spectateurs ne voient pas de vidéo sur {name}",
         "Ta caméra n'est pas sélectionnée comme source active dans SplitCam, ou une autre appli la retient. Ferme Zoom, Skype ou OBS, resélectionne ta webcam dans la liste des sources de SplitCam et vérifie que l'aperçu affiche ton flux avant d'appuyer sur Go Live."),
        ("{name} refuse la clé de stream ou ne se connecte pas",
         "Recopie la clé de stream — un espace en trop ou une ancienne clé déjà régénérée est la cause habituelle. Vérifie que l'URL du serveur correspond à celle affichée par {name} et que la diffusion par encodeur externe est activée sur ton compte. Un slider vert dans les Stream Settings de SplitCam confirme une clé valide."),
        ("Pas de son ou son désynchronisé sur {name}",
         "Choisis SplitCam comme caméra ET comme micro, et sélectionne ton vrai micro dans la source audio de SplitCam. Si le son traîne derrière la vidéo, baisse la résolution d'un cran — l'encodeur est surchargé et le son attend des images en retard."),
    ],
    "it": [
        ("Lo stream su {name} va a scatti o si blocca in buffering",
         "Quasi sempre il bitrate è più alto di quanto regge il tuo upload. Esegui lo speed test integrato di SplitCam e imposta il bitrate a circa il 75% dell'upload misurato — 3.500–6.000&nbsp;Kbps per 1080p, meno per 720p. Il lag sparisce appena l'encoder smette di superare la tua connessione."),
        ("Frame persi durante la trasmissione su {name}",
         "I frame persi significano che i pacchetti non arrivano a {name} in tempo — di solito Wi-Fi instabile. Passa a una connessione Ethernet via cavo, chiudi le app che consumano banda e abbassa un po' il bitrate. Un picco isolato va bene; una salita costante vuol dire che la connessione non tiene il passo."),
        ("Schermo nero — gli spettatori non vedono il video su {name}",
         "La camera non è selezionata come sorgente attiva in SplitCam, o un'altra app la sta usando. Chiudi Zoom, Skype o OBS, riseleziona la webcam nella lista sorgenti di SplitCam e verifica che l'anteprima mostri il tuo flusso prima di premere Go Live."),
        ("{name} rifiuta la stream key o non si connette",
         "Ricopia la stream key — uno spazio finale o una chiave vecchia già rigenerata è la causa più comune. Verifica che l'URL del server corrisponda a quello mostrato da {name} e che la trasmissione via encoder esterno sia attiva sul tuo account. Uno slider verde nelle Stream Settings di SplitCam conferma una chiave valida."),
        ("Niente audio o audio fuori sync su {name}",
         "Scegli SplitCam come camera e come microfono, e seleziona il tuo microfono reale dentro la sorgente audio di SplitCam. Se l'audio resta indietro rispetto al video, abbassa la risoluzione di un livello — l'encoder è sovraccarico e l'audio aspetta i frame in ritardo."),
    ],
    "pt": [
        ("Sua transmissão no {name} trava ou fica em buffer",
         "Quase sempre o bitrate está mais alto do que seu upload aguenta. Rode o teste de velocidade embutido do SplitCam e ajuste o bitrate pra cerca de 75% do upload medido — 3.500–6.000&nbsp;Kbps em 1080p, menos em 720p. O lag some assim que o encoder para de ultrapassar sua conexão."),
        ("Frames perdidos durante a transmissão no {name}",
         "Frames perdidos significam que os pacotes não chegam ao {name} a tempo — geralmente Wi-Fi instável. Mude pra conexão Ethernet com cabo, feche apps que consomem banda e baixe um pouco o bitrate. Um pico isolado é normal; uma subida constante quer dizer que a conexão não dá conta."),
        ("Tela preta — os espectadores não veem vídeo no {name}",
         "Sua câmera não está selecionada como fonte ativa no SplitCam, ou outro app está usando ela. Feche Zoom, Skype ou OBS, escolha a webcam de novo na lista de fontes do SplitCam e confirme que o preview mostra sua imagem antes de apertar Go Live."),
        ("{name} rejeita a stream key ou não conecta",
         "Copie a stream key de novo — um espaço sobrando ou uma chave antiga já resetada é a causa comum. Confirme que a URL do servidor bate com a mostrada pelo {name} e que a transmissão por encoder externo está ativada na sua conta. Um slider verde nas Stream Settings do SplitCam confirma uma chave válida."),
        ("Sem áudio ou áudio fora de sincronia no {name}",
         "Escolha o SplitCam como câmera e como microfone, e selecione seu microfone real dentro da fonte de áudio do SplitCam. Se o áudio atrasa em relação ao vídeo, baixe a resolução um nível — o encoder está sobrecarregado e o áudio espera frames atrasados."),
    ],
    "nl": [
        ("Je {name}-stream hapert of buffert",
         "Bijna altijd is de bitrate hoger dan je upload aankan. Draai de ingebouwde snelheidstest van SplitCam en zet de bitrate op ongeveer 75% van je gemeten upload — 3.500–6.000&nbsp;Kbps voor 1080p, lager voor 720p. De hapering verdwijnt zodra de encoder je verbinding niet meer voorbijstreeft."),
        ("Dropped frames tijdens de {name}-uitzending",
         "Dropped frames betekenen dat pakketten {name} niet op tijd bereiken — meestal instabiele wifi. Schakel over op een bekabelde Ethernet-verbinding, sluit bandbreedte-vretende apps en verlaag de bitrate iets. Eén piek is prima; een gestage stijging betekent dat de verbinding het niet bijhoudt."),
        ("Zwart scherm — kijkers zien geen video op {name}",
         "Je camera is niet als actieve bron in SplitCam gekozen, of een andere app houdt hem vast. Sluit Zoom, Skype of OBS, kies je webcam opnieuw in SplitCam's bronnenlijst en controleer dat de preview je beeld toont voor je op Go Live drukt."),
        ("{name} weigert de stream key of maakt geen verbinding",
         "Kopieer de stream key opnieuw — een spatie aan het eind of een oude, al vernieuwde key is de gebruikelijke oorzaak. Controleer dat de server-URL overeenkomt met die {name} toont en dat externe-encoder-uitzending op je account is ingeschakeld. Een groene slider in SplitCam's Stream Settings bevestigt een geldige key."),
        ("Geen geluid of geluid loopt niet synchroon op {name}",
         "Kies SplitCam als camera én als microfoon, en selecteer je echte mic binnen SplitCam's audiobron. Als het geluid achterloopt op de video, verlaag de resolutie een stap — de encoder is overbelast en het geluid wacht op te late frames."),
    ],
    "ro": [
        ("Stream-ul tău pe {name} are lag sau se blochează la buffering",
         "Aproape întotdeauna bitrate-ul e mai mare decât suportă uploadul tău. Rulează testul de viteză integrat din SplitCam și setează bitrate-ul la circa 75% din uploadul măsurat — 3.500–6.000&nbsp;Kbps la 1080p, mai puțin la 720p. Lagul dispare odată ce encoderul nu mai depășește conexiunea."),
        ("Frame-uri pierdute în timpul transmisiunii pe {name}",
         "Frame-urile pierdute înseamnă că pachetele nu ajung la {name} la timp — de obicei Wi-Fi instabil. Treci pe conexiune Ethernet prin cablu, închide aplicațiile care consumă lățime de bandă și scade puțin bitrate-ul. Un vârf izolat e ok; o creștere constantă înseamnă că conexiunea nu face față."),
        ("Ecran negru — spectatorii nu văd video pe {name}",
         "Camera nu e selectată ca sursă activă în SplitCam, sau o ține altă aplicație. Închide Zoom, Skype sau OBS, reselectează webcamul în lista de surse SplitCam și confirmă că previzualizarea îți arată imaginea înainte să apeși Go Live."),
        ("{name} respinge cheia de stream sau nu se conectează",
         "Recopiază cheia de stream — un spațiu la final sau o cheie veche, deja resetată, e cauza obișnuită. Confirmă că URL-ul serverului se potrivește cu cel afișat de {name} și că transmisiunea prin encoder extern e activată pe contul tău. Un slider verde în Stream Settings SplitCam confirmă o cheie validă."),
        ("Fără audio sau audio desincronizat pe {name}",
         "Alege SplitCam și ca cameră, și ca microfon, și selectează microfonul real în sursa audio SplitCam. Dacă audio rămâne în urma video-ului, scade rezoluția cu o treaptă — encoderul e supraîncărcat și audio așteaptă frame-uri întârziate."),
    ],
    "bg": [
        ("Излъчването на {name} лагва или буферира",
         "Почти винаги битрейтът е по-висок, отколкото издържа аплоудът ти. Пусни вградения тест за скорост на SplitCam и задай битрейта на около 75% от измерения аплоуд — 3500–6000&nbsp;Kbps за 1080p, по-малко за 720p. Лагът изчезва, щом енкодерът спре да изпреварва връзката."),
        ("Изпуснати кадри по време на излъчване на {name}",
         "Изпуснатите кадри значат, че пакетите не стигат до {name} навреме — обикновено нестабилен Wi-Fi. Премини на кабелна Ethernet връзка, затвори приложения, които ядат трафик, и намали малко битрейта. Единичен скок е нормален; постоянно покачване значи, че връзката не смогва."),
        ("Черен екран — зрителите не виждат видео на {name}",
         "Камерата не е избрана като активен източник в SplitCam, или друго приложение я държи. Затвори Zoom, Skype или OBS, избери уебкамерата отново в списъка с източници на SplitCam и потвърди, че прегледът показва картина, преди да натиснеш Go Live."),
        ("{name} отхвърля стрийм ключа или не се свързва",
         "Копирай стрийм ключа отново — излишен интервал или стар, вече нулиран ключ е честата причина. Потвърди, че URL-ът на сървъра съвпада с показания от {name} и че излъчването през външен енкодер е активирано на акаунта ти. Зелен слайдер в Stream Settings на SplitCam потвърждава валиден ключ."),
        ("Няма звук или звукът е разсинхронизиран на {name}",
         "Избери SplitCam и като камера, и като микрофон, и задай реалния си микрофон като аудио източник в SplitCam. Ако звукът изостава от видеото, намали резолюцията с едно ниво — енкодерът е претоварен и звукът чака закъснели кадри."),
    ],
    "hu": [
        ("A {name} streamed akadozik vagy pufferel",
         "Szinte mindig a bitráta magasabb, mint amit a feltöltésed elbír. Futtasd le a SplitCam beépített sebességtesztjét, majd állítsd a bitrátát a mért feltöltés kb. 75%-ára — 3500–6000&nbsp;Kbps 1080p-hez, kevesebb 720p-hez. Az akadozás megszűnik, amint az enkóder már nem előzi meg a kapcsolatodat."),
        ("Eldobott képkockák a {name} adás közben",
         "Az eldobott képkockák azt jelentik, hogy a csomagok nem érnek el időben a {name} platformhoz — általában instabil Wi-Fi. Válts vezetékes Ethernet kapcsolatra, zárd be a sávszélesség-zabáló appokat, és csökkentsd kicsit a bitrátát. Egy kiugrás rendben van; az állandó emelkedés azt jelenti, hogy a kapcsolat nem bírja."),
        ("Fekete képernyő — a nézők nem látnak videót a {name} platformon",
         "A kamerád nincs aktív forrásként kiválasztva a SplitCamben, vagy egy másik app foglalja. Zárd be a Zoomot, Skype-ot vagy OBS-t, válaszd ki újra a webkamerát a SplitCam forráslistájában, és ellenőrizd, hogy az előnézet mutatja a képet, mielőtt megnyomod a Go Live-ot."),
        ("A {name} elutasítja a stream kulcsot vagy nem csatlakozik",
         "Másold ki újra a stream kulcsot — egy záró szóköz vagy egy régi, már lecserélt kulcs a szokásos ok. Ellenőrizd, hogy a szerver URL megegyezik a {name} által mutatottal, és hogy a külső enkóderes adás engedélyezve van a fiókodon. Egy zöld csúszka a SplitCam Stream Settings menüjében érvényes kulcsot jelez."),
        ("Nincs hang vagy a hang nincs szinkronban a {name} platformon",
         "Válaszd a SplitCamet kameraként ÉS mikrofonként is, és állítsd be a valódi mikrofonodat a SplitCam audioforrásában. Ha a hang lemarad a videótól, csökkentsd a felbontást egy lépéssel — az enkóder túlterhelt, és a hang a késő képkockákra vár."),
    ],
    "el": [
        ("Το stream σου στο {name} κολλάει ή κάνει buffering",
         "Σχεδόν πάντα το bitrate είναι υψηλότερο απ' ό,τι αντέχει το upload σου. Τρέξε το ενσωματωμένο speed test του SplitCam και βάλε το bitrate στο περίπου 75% του μετρημένου upload — 3.500–6.000&nbsp;Kbps για 1080p, λιγότερο για 720p. Το lag φεύγει μόλις ο encoder σταματήσει να ξεπερνά τη σύνδεσή σου."),
        ("Χαμένα frames κατά τη μετάδοση στο {name}",
         "Τα χαμένα frames σημαίνουν ότι τα πακέτα δεν φτάνουν στο {name} εγκαίρως — συνήθως ασταθές Wi-Fi. Πέρνα σε ενσύρματη σύνδεση Ethernet, κλείσε εφαρμογές που τρώνε bandwidth και χαμήλωσε λίγο το bitrate. Μια μεμονωμένη κορύφωση είναι ok· μια σταθερή άνοδος σημαίνει ότι η σύνδεση δεν προλαβαίνει."),
        ("Μαύρη οθόνη — οι θεατές δεν βλέπουν βίντεο στο {name}",
         "Η κάμερά σου δεν είναι επιλεγμένη ως ενεργή πηγή στο SplitCam, ή την κρατά άλλη εφαρμογή. Κλείσε Zoom, Skype ή OBS, ξαναεπίλεξε την webcam στη λίστα πηγών του SplitCam και βεβαιώσου ότι η προεπισκόπηση δείχνει την εικόνα σου πριν πατήσεις Go Live."),
        ("Το {name} απορρίπτει το stream key ή δεν συνδέεται",
         "Ξαναντίγραψε το stream key — ένα κενό στο τέλος ή ένα παλιό, ήδη ανανεωμένο key είναι η συνηθισμένη αιτία. Επιβεβαίωσε ότι το server URL ταιριάζει με αυτό που δείχνει το {name} και ότι η μετάδοση μέσω εξωτερικού encoder είναι ενεργή στον λογαριασμό σου. Ένα πράσινο slider στις Stream Settings του SplitCam επιβεβαιώνει έγκυρο key."),
        ("Χωρίς ήχο ή ήχος εκτός συγχρονισμού στο {name}",
         "Επίλεξε το SplitCam ως κάμερα ΚΑΙ ως μικρόφωνο, και διάλεξε το πραγματικό σου μικρόφωνο μέσα στην πηγή ήχου του SplitCam. Αν ο ήχος καθυστερεί σε σχέση με το βίντεο, χαμήλωσε την ανάλυση ένα σκαλί — ο encoder είναι υπερφορτωμένος και ο ήχος περιμένει καθυστερημένα frames."),
    ],
    "fi": [
        ("{name}-striimisi pätkii tai puskuroi",
         "Lähes aina bitrate on korkeampi kuin uploadisi kestää. Aja SplitCamin sisäänrakennettu nopeustesti ja aseta bitrate noin 75 %:iin mitatusta uploadista — 3 500–6 000&nbsp;Kbps 1080p:lle, vähemmän 720p:lle. Pätkiminen loppuu, kun enkooderi lakkaa ohittamasta yhteyttäsi."),
        ("Pudonneita ruutuja {name}-lähetyksen aikana",
         "Pudonneet ruudut tarkoittavat, etteivät paketit ehdi alustalle {name} ajoissa — yleensä epävakaa Wi-Fi. Vaihda langalliseen Ethernet-yhteyteen, sulje kaistaa syövät sovellukset ja laske bitrateä hieman. Yksittäinen piikki on ok; tasainen nousu tarkoittaa, ettei yhteys pysy perässä."),
        ("Musta ruutu — katsojat eivät näe videota alustalla {name}",
         "Kameraasi ei ole valittu aktiiviseksi lähteeksi SplitCamissa, tai toinen sovellus pitää sitä. Sulje Zoom, Skype tai OBS, valitse webkamera uudelleen SplitCamin lähdelistasta ja varmista, että esikatselu näyttää kuvasi ennen kuin painat Go Live."),
        ("{name} hylkää striimiavaimen tai ei yhdistä",
         "Kopioi striimiavain uudelleen — loppuun jäänyt välilyönti tai vanha, jo vaihdettu avain on tavallinen syy. Varmista, että palvelimen URL vastaa alustan {name} näyttämää ja että ulkoisen enkooderin lähetys on käytössä tililläsi. Vihreä liukusäädin SplitCamin Stream Settingsissä vahvistaa kelvollisen avaimen."),
        ("Ei ääntä tai ääni ei ole synkassa alustalla {name}",
         "Valitse SplitCam sekä kameraksi että mikrofoniksi, ja valitse oikea mikrofonisi SplitCamin äänilähteeksi. Jos ääni jää videosta jälkeen, laske resoluutiota yksi pykälä — enkooderi on ylikuormittunut ja ääni odottaa myöhässä olevia ruutuja."),
    ],
    "da": [
        ("Dit {name}-stream hakker eller buffer",
         "Næsten altid er bitraten højere, end dit upload kan klare. Kør SplitCams indbyggede hastighedstest og sæt bitraten til omkring 75% af dit målte upload — 3.500–6.000&nbsp;Kbps til 1080p, lavere til 720p. Hakket forsvinder, så snart encoderen holder op med at overhale din forbindelse."),
        ("Tabte frames under {name}-udsendelsen",
         "Tabte frames betyder, at pakkerne ikke når frem til {name} i tide — som regel ustabilt Wi-Fi. Skift til en kabelforbundet Ethernet-forbindelse, luk båndbredde-tunge apps og sænk bitraten en smule. Et enkelt udsving er fint; en jævn stigning betyder, at forbindelsen ikke kan følge med."),
        ("Sort skærm — seerne ser ingen video på {name}",
         "Dit kamera er ikke valgt som aktiv kilde i SplitCam, eller en anden app holder på det. Luk Zoom, Skype eller OBS, vælg dit webcam igen i SplitCams kildeliste, og bekræft at forhåndsvisningen viser dit billede, før du trykker Go Live."),
        ("{name} afviser stream key eller vil ikke forbinde",
         "Kopiér stream key igen — et mellemrum til sidst eller en gammel, allerede skiftet nøgle er den sædvanlige årsag. Bekræft at server-URL matcher den, {name} viser, og at ekstern-encoder-udsendelse er aktiveret på din konto. En grøn slider i SplitCams Stream Settings bekræfter en gyldig nøgle."),
        ("Ingen lyd eller lyd ude af sync på {name}",
         "Vælg SplitCam som både kamera og mikrofon, og vælg din rigtige mikrofon inde i SplitCams lydkilde. Hvis lyden halter efter videoen, sænk opløsningen et trin — encoderen er overbelastet, og lyden venter på forsinkede frames."),
    ],
    "no": [
        ("{name}-strømmen din henger eller bufrer",
         "Nesten alltid er bitraten høyere enn opplastningen din takler. Kjør SplitCams innebygde hastighetstest og sett bitraten til omtrent 75% av målt opplastning — 3 500–6 000&nbsp;Kbps for 1080p, lavere for 720p. Hakkingen forsvinner så snart enkoderen slutter å overgå forbindelsen din."),
        ("Tapte frames under {name}-sendingen",
         "Tapte frames betyr at pakkene ikke når {name} i tide — som regel ustabilt Wi-Fi. Bytt til kablet Ethernet-tilkobling, lukk båndbredde-tunge apper og senk bitraten litt. Ett enkelt utslag er greit; en jevn økning betyr at forbindelsen ikke holder følge."),
        ("Svart skjerm — seerne ser ingen video på {name}",
         "Kameraet ditt er ikke valgt som aktiv kilde i SplitCam, eller en annen app holder på det. Lukk Zoom, Skype eller OBS, velg webkameraet på nytt i SplitCams kildeliste, og bekreft at forhåndsvisningen viser bildet ditt før du trykker Go Live."),
        ("{name} avviser strømnøkkelen eller kobler ikke til",
         "Kopier strømnøkkelen på nytt — et mellomrom til slutt eller en gammel, allerede byttet nøkkel er den vanlige årsaken. Bekreft at server-URL-en matcher den {name} viser, og at ekstern-enkoder-sending er aktivert på kontoen din. En grønn slider i SplitCams Stream Settings bekrefter en gyldig nøkkel."),
        ("Ingen lyd eller lyd ute av synk på {name}",
         "Velg SplitCam som både kamera og mikrofon, og velg den ekte mikrofonen din inne i SplitCams lydkilde. Hvis lyden henger etter videoen, senk oppløsningen ett hakk — enkoderen er overbelastet og lyden venter på forsinkede frames."),
    ],
    "sr": [
        ("Твој пренос на {name} лагује или баферује",
         "Готово увек је битрејт виши него што твој аплоуд издржава. Покрени уграђени тест брзине SplitCam-а и постави битрејт на око 75% измереног аплоуда — 3500–6000&nbsp;Kbps за 1080p, мање за 720p. Лаг нестаје чим енкодер престане да престиже твоју везу."),
        ("Изгубљени фрејмови током преноса на {name}",
         "Изгубљени фрејмови значе да пакети не стижу до {name} на време — обично нестабилан Wi-Fi. Пређи на кабловску Ethernet везу, затвори апликације које троше проток и мало смањи битрејт. Један скок је у реду; стални пораст значи да веза не може да испрати."),
        ("Црн екран — гледаоци не виде видео на {name}",
         "Камера није изабрана као активни извор у SplitCam-у, или је друга апликација држи. Затвори Zoom, Skype или OBS, поново изабери веб камеру у листи извора SplitCam-а и потврди да преглед приказује слику пре него притиснеш Go Live."),
        ("{name} одбија стрим кључ или се не повезује",
         "Поново копирај стрим кључ — сувишан размак или стар, већ ресетован кључ је честа узрок. Потврди да се URL сервера поклапа са оним који приказује {name} и да је пренос преко спољног енкодера укључен на налогу. Зелени слајдер у Stream Settings SplitCam-а потврђује важећи кључ."),
        ("Нема звука или звук није синхронизован на {name}",
         "Изабери SplitCam и као камеру и као микрофон, и постави свој прави микрофон као аудио извор у SplitCam-у. Ако звук касни за видеом, смањи резолуцију за једну степеницу — енкодер је преоптерећен и звук чека закаснеле фрејмове."),
    ],
    "hr": [
        ("Tvoj prijenos na {name} lagira ili buffera",
         "Gotovo uvijek je bitrate viši nego što tvoj upload izdrži. Pokreni ugrađeni test brzine SplitCama i postavi bitrate na oko 75% izmjerenog uploada — 3.500–6.000&nbsp;Kbps za 1080p, manje za 720p. Lag nestaje čim enkoder prestane prestizati tvoju vezu."),
        ("Izgubljeni frameovi tijekom prijenosa na {name}",
         "Izgubljeni frameovi znače da paketi ne stižu do {name} na vrijeme — obično nestabilan Wi-Fi. Prijeđi na kabelsku Ethernet vezu, zatvori aplikacije koje troše propusnost i malo smanji bitrate. Jedan skok je u redu; stalni porast znači da veza ne može pratiti."),
        ("Crni ekran — gledatelji ne vide video na {name}",
         "Kamera nije odabrana kao aktivni izvor u SplitCamu, ili je druga aplikacija drži. Zatvori Zoom, Skype ili OBS, ponovno odaberi web kameru u listi izvora SplitCama i potvrdi da pregled prikazuje sliku prije nego pritisneš Go Live."),
        ("{name} odbija stream ključ ili se ne povezuje",
         "Ponovno kopiraj stream ključ — suvišan razmak ili stari, već resetiran ključ je čest uzrok. Potvrdi da se URL servera podudara s onim koji prikazuje {name} i da je prijenos preko vanjskog enkodera uključen na tvom računu. Zeleni slider u Stream Settings SplitCama potvrđuje valjan ključ."),
        ("Nema zvuka ili zvuk nije sinkroniziran na {name}",
         "Odaberi SplitCam i kao kameru i kao mikrofon, i postavi svoj pravi mikrofon kao audio izvor u SplitCamu. Ako zvuk kasni za videom, smanji rezoluciju za jednu razinu — enkoder je preopterećen i zvuk čeka zakašnjele frameove."),
    ],
    "zh": [
        ("您的 {name} 直播卡顿或缓冲",
         "几乎总是比特率高于您的上传所能承受的。运行 SplitCam 内置的速度测试，然后将比特率设为测得上传的约 75% — 1080p 为 3,500–6,000&nbsp;Kbps，720p 更低。一旦编码器不再超出您的连接，卡顿就会消失。"),
        ("{name} 直播期间丢帧",
         "丢帧意味着数据包未能及时到达 {name} — 通常是 Wi-Fi 不稳定。改用有线以太网连接，关闭占用带宽的应用，并稍微降低比特率。单次峰值没问题；持续上升说明连接跟不上。"),
        ("黑屏 — 观众在 {name} 上看不到视频",
         "您的摄像头未在 SplitCam 中被选为活动源，或被另一个应用占用。关闭 Zoom、Skype 或 OBS，在 SplitCam 的源列表中重新选择摄像头，并在按 Go Live 前确认预览显示您的画面。"),
        ("{name} 拒绝直播密钥或无法连接",
         "重新复制直播密钥 — 末尾多余的空格或旧的、已轮换的密钥是常见原因。确认服务器 URL 与 {name} 显示的一致，并且您的账户已启用外部编码器直播。SplitCam Stream Settings 中的绿色滑块确认密钥有效。"),
        ("{name} 上没有声音或声音不同步",
         "将 SplitCam 同时选为摄像头和麦克风，并在 SplitCam 的音频源中选择您的真实麦克风。如果音频落后于视频，将分辨率降低一档 — 编码器过载，音频在等待迟到的帧。"),
    ],
    "ja": [
        ("{name} の配信がカクつく・バッファリングする",
         "ほぼ常にビットレートがアップロードの限界を超えています。SplitCam の内蔵速度テストを実行し、ビットレートを測定したアップロードの約75%に設定してください — 1080pで3,500–6,000&nbsp;Kbps、720pはそれ以下。エンコーダーが接続を追い越さなくなればカクつきは消えます。"),
        ("{name} 配信中のフレーム落ち",
         "フレーム落ちはパケットが {name} に間に合っていないこと — 通常は不安定なWi-Fiが原因です。有線Ethernet接続に切り替え、帯域を食うアプリを閉じ、ビットレートを少し下げてください。単発のスパイクは問題なし；継続的な増加は接続が追いつかないサインです。"),
        ("黒い画面 — {name} で視聴者に映像が映らない",
         "カメラが SplitCam でアクティブソースとして選択されていないか、別のアプリが使用中です。Zoom、Skype、OBS を閉じ、SplitCam のソースリストでウェブカメラを選び直し、Go Live を押す前にプレビューに映像が表示されることを確認してください。"),
        ("{name} がストリームキーを拒否する・接続しない",
         "ストリームキーをコピーし直してください — 末尾のスペースや古い、すでにローテートされたキーが通常の原因です。サーバーURLが {name} の表示と一致し、アカウントで外部エンコーダー配信が有効か確認してください。SplitCam の Stream Settings の緑のスライダーが有効なキーを確認します。"),
        ("{name} で音声がない・音ズレする",
         "SplitCam をカメラとマイクの両方に選び、SplitCam の音声ソースで実際のマイクを選択してください。音声が映像から遅れる場合は解像度を1段下げてください — エンコーダーが過負荷で、音声が遅れたフレームを待っています。"),
    ],
    "ar": [
        ("بث {name} لديك يتقطع أو يخزّن مؤقتاً",
         "في معظم الأحيان يكون معدل البت أعلى مما يتحمله الرفع لديك. شغّل اختبار السرعة المدمج في SplitCam، ثم اضبط معدل البت على نحو 75% من الرفع المقاس — 3,500–6,000&nbsp;Kbps لـ 1080p، أقل لـ 720p. يختفي التقطع بمجرد أن يتوقف المُشفِّر عن تجاوز اتصالك."),
        ("إطارات مفقودة أثناء البث على {name}",
         "الإطارات المفقودة تعني أن الحزم لا تصل إلى {name} في الوقت المناسب — عادةً Wi-Fi غير مستقر. انتقل إلى اتصال Ethernet سلكي، أغلق التطبيقات التي تستهلك النطاق الترددي، وخفّض معدل البت قليلاً. ارتفاع واحد عادي؛ الارتفاع المستمر يعني أن الاتصال لا يواكب."),
        ("شاشة سوداء — المشاهدون لا يرون فيديو على {name}",
         "الكاميرا غير محددة كمصدر نشط في SplitCam، أو يحتجزها تطبيق آخر. أغلق Zoom أو Skype أو OBS، اختر كاميرا الويب مرة أخرى في قائمة مصادر SplitCam، وتأكد من أن المعاينة تعرض صورتك قبل الضغط على Go Live."),
        ("{name} يرفض مفتاح البث أو لا يتصل",
         "انسخ مفتاح البث من جديد — مسافة زائدة في النهاية أو مفتاح قديم تم تدويره هو السبب المعتاد. تأكد من أن عنوان URL للخادم يطابق ما يعرضه {name} وأن البث عبر مُشفِّر خارجي مفعّل على حسابك. شريط أخضر في Stream Settings لـ SplitCam يؤكد مفتاحاً صالحاً."),
        ("لا يوجد صوت أو الصوت غير متزامن على {name}",
         "اختر SplitCam ككاميرا وميكروفون معاً، واختر ميكروفونك الحقيقي داخل مصدر الصوت في SplitCam. إذا تأخر الصوت عن الفيديو، خفّض الدقة درجة واحدة — المُشفِّر محمّل بشكل زائد والصوت ينتظر الإطارات المتأخرة."),
    ],
    "th": [
        ("สตรีม {name} ของคุณกระตุกหรือบัฟเฟอร์",
         "เกือบทุกครั้งบิตเรตสูงกว่าที่อัปโหลดของคุณรับไหว รันการทดสอบความเร็วในตัวของ SplitCam แล้วตั้งบิตเรตที่ประมาณ 75% ของอัปโหลดที่วัดได้ — 3,500–6,000&nbsp;Kbps สำหรับ 1080p ต่ำกว่าสำหรับ 720p อาการกระตุกจะหายไปเมื่อ encoder หยุดวิ่งแซงการเชื่อมต่อของคุณ"),
        ("เฟรมหลุดระหว่างการถ่ายทอดบน {name}",
         "เฟรมหลุดหมายความว่าแพ็กเก็ตไปไม่ถึง {name} ทันเวลา — มักเป็น Wi-Fi ไม่เสถียร เปลี่ยนเป็นการเชื่อมต่อ Ethernet แบบมีสาย ปิดแอปที่กินแบนด์วิดท์ และลดบิตเรตลงเล็กน้อย พีคครั้งเดียวไม่เป็นไร แต่การเพิ่มขึ้นต่อเนื่องหมายความว่าการเชื่อมต่อตามไม่ทัน"),
        ("จอดำ — ผู้ชมไม่เห็นวิดีโอบน {name}",
         "กล้องของคุณไม่ได้ถูกเลือกเป็นแหล่งที่ใช้งานใน SplitCam หรือมีแอปอื่นยึดไว้ ปิด Zoom, Skype หรือ OBS เลือกเว็บแคมใหม่ในรายการแหล่งของ SplitCam และยืนยันว่าตัวอย่างแสดงภาพของคุณก่อนกด Go Live"),
        ("{name} ปฏิเสธสตรีมคีย์หรือไม่เชื่อมต่อ",
         "คัดลอกสตรีมคีย์ใหม่ — ช่องว่างที่ท้ายหรือคีย์เก่าที่หมุนเปลี่ยนแล้วเป็นสาเหตุปกติ ยืนยันว่า URL เซิร์ฟเวอร์ตรงกับที่ {name} แสดง และเปิดใช้งานการถ่ายทอดผ่าน encoder ภายนอกในบัญชีของคุณแล้ว แถบเลื่อนสีเขียวใน Stream Settings ของ SplitCam ยืนยันว่าคีย์ถูกต้อง"),
        ("ไม่มีเสียงหรือเสียงไม่ตรงกับภาพบน {name}",
         "เลือก SplitCam เป็นทั้งกล้องและไมโครโฟน และเลือกไมโครโฟนจริงของคุณในแหล่งเสียงของ SplitCam หากเสียงตามหลังวิดีโอ ลดความละเอียดลงหนึ่งระดับ — encoder ทำงานหนักเกินไปและเสียงกำลังรอเฟรมที่มาช้า"),
    ],
    "fil": [
        ("Ang {name} stream mo ay nag-lalag o nag-bubuffer",
         "Halos palaging mas mataas ang bitrate kaysa kaya ng upload mo. Patakbuhin ang built-in speed test ng SplitCam, tapos i-set ang bitrate sa mga 75% ng nasukat mong upload — 3,500–6,000&nbsp;Kbps para sa 1080p, mas mababa para sa 720p. Nawawala ang lag kapag tumigil na ang encoder sa pag-unahan sa koneksyon mo."),
        ("Dropped frames habang nag-bo-broadcast sa {name}",
         "Ang dropped frames ay nangangahulugang hindi umaabot ang mga packet sa {name} sa tamang oras — kadalasan ay hindi stable na Wi-Fi. Lumipat sa wired Ethernet connection, isara ang mga app na kumakain ng bandwidth, at bahagyang ibaba ang bitrate. Ok lang ang isang spike; ang tuloy-tuloy na pagtaas ay nangangahulugang hindi kaya ng koneksyon."),
        ("Black screen — walang nakikitang video ang viewers sa {name}",
         "Hindi napili ang camera mo bilang active source sa SplitCam, o may ibang app na humahawak dito. Isara ang Zoom, Skype o OBS, piliin muli ang webcam sa source list ng SplitCam, at tiyakin na ipinapakita ng preview ang feed mo bago pindutin ang Go Live."),
        ("Tinatanggihan ng {name} ang stream key o ayaw kumonekta",
         "Kopyahin muli ang stream key — ang trailing space o luma nang key na na-rotate na ang karaniwang dahilan. Tiyakin na tumutugma ang server URL sa ipinapakita ng {name} at na naka-enable ang external-encoder broadcasting sa account mo. Isang green slider sa Stream Settings ng SplitCam ang nagkukumpirma ng valid na key."),
        ("Walang audio o hindi sync ang audio sa {name}",
         "Piliin ang SplitCam bilang camera AT microphone, at piliin ang totoong mic mo sa loob ng audio source ng SplitCam. Kung nahuhuli ang audio sa video, ibaba ang resolution ng isang hakbang — overloaded ang encoder at naghihintay ang audio sa mga late frame."),
    ],
    "tr": [
        ("{name} yayının takılıyor veya tamponluyor",
         "Neredeyse her zaman bitrate yüklemenin kaldırabileceğinden yüksektir. SplitCam'in yerleşik hız testini çalıştır, sonra bitrate'i ölçülen yüklemenin yaklaşık %75'ine ayarla — 1080p için 3.500–6.000&nbsp;Kbps, 720p için daha düşük. Kodlayıcı bağlantını geçmeyi bırakınca takılma geçer."),
        ("{name} yayını sırasında kare kaybı",
         "Kare kaybı, paketlerin {name}'e zamanında ulaşmadığı anlamına gelir — genelde kararsız Wi-Fi. Kablolu Ethernet bağlantısına geç, bant genişliği yiyen uygulamaları kapat ve bitrate'i biraz düşür. Tek bir sıçrama sorun değil; sürekli artış bağlantının yetişemediğini gösterir."),
        ("Siyah ekran — izleyiciler {name}'de video görmüyor",
         "Kameran SplitCam'de etkin kaynak olarak seçili değil ya da başka bir uygulama tutuyor. Zoom, Skype veya OBS'i kapat, web kameranı SplitCam kaynak listesinde tekrar seç ve Go Live'a basmadan önce önizlemenin görüntünü gösterdiğini doğrula."),
        ("{name} yayın anahtarını reddediyor veya bağlanmıyor",
         "Yayın anahtarını yeniden kopyala — sondaki boşluk ya da eski, değiştirilmiş anahtar her zamanki nedendir. Sunucu URL'sinin {name}'in gösterdiğiyle eşleştiğini ve hesabında harici kodlayıcı yayınının açık olduğunu doğrula. SplitCam'in Stream Settings'indeki yeşil kaydırıcı geçerli anahtarı onaylar."),
        ("{name}'de ses yok veya ses senkron dışı",
         "SplitCam'i hem kamera hem mikrofon olarak seç ve SplitCam'in ses kaynağında gerçek mikrofonunu seç. Ses videonun gerisinde kalıyorsa çözünürlüğü bir kademe düşür — kodlayıcı aşırı yüklenmiş ve ses geç kalan kareleri bekliyor."),
    ],
    "id": [
        ("Siaran {name} tersendat atau buffering",
         "Hampir selalu bitrate diatur lebih tinggi dari yang mampu ditanggung upload-mu. Jalankan tes kecepatan bawaan SplitCam, lalu setel bitrate ke sekitar 75% dari upload terukur — 3.500–6.000&nbsp;Kbps untuk 1080p, lebih rendah untuk 720p. Tersendat hilang begitu encoder berhenti melampaui koneksimu."),
        ("Frame hilang saat siaran {name}",
         "Frame hilang berarti paket tidak sampai ke {name} tepat waktu — biasanya Wi-Fi tidak stabil. Pindah ke Ethernet kabel, tutup aplikasi pemakan bandwidth, dan turunkan bitrate sedikit. Satu lonjakan tidak masalah; kenaikan terus-menerus berarti koneksi tidak mengejar."),
        ("Layar hitam — penonton tidak melihat video di {name}",
         "Kameramu tidak terpilih sebagai sumber aktif di SplitCam, atau aplikasi lain menahannya. Tutup Zoom, Skype, atau OBS, pilih ulang webcam di daftar sumber SplitCam, dan pastikan preview menampilkan gambarmu sebelum tekan Go Live."),
        ("{name} menolak stream key atau tidak terhubung",
         "Salin ulang stream key — spasi di akhir atau kunci lama yang sudah di-reset adalah penyebab paling umum. Pastikan URL server cocok dengan yang ditampilkan {name} dan bahwa siaran encoder eksternal aktif di akunmu. Slider hijau di Stream Settings SplitCam menandakan kunci valid."),
        ("Tidak ada audio atau audio tidak sinkron di {name}",
         "Pilih SplitCam sebagai kamera DAN mikrofon, dan pilih mikrofon aslimu di dalam sumber audio SplitCam. Jika audio tertinggal dari video, turunkan resolusi satu tingkat — encoder kelebihan beban dan audio menunggu frame yang terlambat."),
    ],
    "vi": [
        ("Buổi phát {name} giật hoặc buffering",
         "Hầu như luôn do bitrate đặt cao hơn mức đường upload gánh được. Chạy bài test tốc độ tích hợp của SplitCam, rồi đặt bitrate khoảng 75% upload đo được — 3.500–6.000&nbsp;Kbps cho 1080p, thấp hơn cho 720p. Giật sẽ hết khi bộ mã hóa thôi vượt quá kết nối của bạn."),
        ("Frame rơi khi phát {name}",
         "Frame rơi nghĩa là gói tin không tới {name} đúng lúc — thường là Wi-Fi không ổn định. Chuyển sang Ethernet có dây, đóng các ứng dụng ngốn băng thông và hạ bitrate một chút. Một lần nhảy thì không sao; tăng liên tục nghĩa là kết nối không theo kịp."),
        ("Màn hình đen — người xem không thấy video trên {name}",
         "Camera của bạn không được chọn làm nguồn hoạt động trong SplitCam, hoặc ứng dụng khác đang giữ nó. Đóng Zoom, Skype hoặc OBS, chọn lại webcam trong danh sách nguồn của SplitCam, và chắc chắn preview hiện hình bạn trước khi nhấn Go Live."),
        ("{name} từ chối stream key hoặc không kết nối",
         "Sao chép lại stream key — khoảng trắng ở cuối hoặc khóa cũ đã reset là nguyên nhân phổ biến nhất. Chắc chắn URL máy chủ khớp với cái {name} hiển thị và phát sóng bộ mã hóa ngoài đã bật trên tài khoản. Thanh trượt xanh trong Stream Settings của SplitCam xác nhận khóa hợp lệ."),
        ("Không có âm thanh hoặc âm thanh lệch trên {name}",
         "Chọn SplitCam làm cả camera VÀ micro, và chọn micro thật của bạn bên trong nguồn âm thanh của SplitCam. Nếu âm thanh trễ so với video, hạ độ phân giải một mức — bộ mã hóa quá tải và âm thanh đang chờ các frame trễ."),
    ],
    "pl": [
        ("Transmisja {name} się tnie lub buforuje",
         "Niemal zawsze bitrate jest ustawiony wyżej, niż udźwignie twój upload. Uruchom wbudowany test prędkości SplitCam, potem ustaw bitrate na około 75% zmierzonego uploadu — 3500–6000&nbsp;Kbps dla 1080p, niżej dla 720p. Cięcia znikają, gdy enkoder przestaje przekraczać twoje łącze."),
        ("Zgubione klatki podczas transmisji {name}",
         "Zgubione klatki oznaczają, że pakiety nie docierają do {name} na czas — zwykle niestabilne Wi-Fi. Przejdź na przewodowy Ethernet, zamknij aplikacje pożerające pasmo i nieco obniż bitrate. Pojedynczy skok to nic; ciągły wzrost oznacza, że łącze nie nadąża."),
        ("Czarny ekran — widzowie nie widzą wideo na {name}",
         "Twoja kamera nie jest wybrana jako aktywne źródło w SplitCam albo trzyma ją inna aplikacja. Zamknij Zoom, Skype lub OBS, wybierz ponownie kamerę na liście źródeł SplitCam i upewnij się, że podgląd pokazuje twój obraz, zanim naciśniesz Go Live."),
        ("{name} odrzuca klucz streamu lub się nie łączy",
         "Skopiuj klucz streamu ponownie — spacja na końcu albo stary, zresetowany klucz to najczęstsze przyczyny. Upewnij się, że URL serwera zgadza się z tym, co pokazuje {name}, a transmisja enkoderem zewnętrznym jest włączona na koncie. Zielony suwak w Stream Settings SplitCam potwierdza ważny klucz."),
        ("Brak dźwięku lub dźwięk niezsynchronizowany na {name}",
         "Wybierz SplitCam jako kamerę I mikrofon, a w źródle dźwięku SplitCam wybierz swój prawdziwy mikrofon. Jeśli dźwięk opóźnia się względem wideo, obniż rozdzielczość o jeden poziom — enkoder jest przeciążony i dźwięk czeka na spóźnione klatki."),
    ],
    "ko": [
        ("{name} 방송이 끊기거나 버퍼링됨",
         "거의 항상 비트레이트가 업로드가 감당할 수 있는 것보다 높게 설정된 경우입니다. SplitCam 내장 속도 테스트를 돌린 뒤 비트레이트를 측정된 업로드의 약 75%로 설정하세요 — 1080p에 3,500–6,000&nbsp;Kbps, 720p는 더 낮게. 인코더가 회선을 초과하지 않으면 끊김이 사라집니다."),
        ("{name} 방송 중 프레임 끊김",
         "프레임 끊김은 패킷이 {name}에 제때 도착하지 못한다는 뜻입니다 — 보통 불안정한 와이파이. 유선 이더넷으로 바꾸고 대역폭을 먹는 앱을 닫고 비트레이트를 약간 낮추세요. 한 번 튀는 건 괜찮지만 계속 늘면 회선이 못 따라가는 것입니다."),
        ("검은 화면 — 시청자가 {name}에서 영상을 못 봄",
         "카메라가 SplitCam에서 활성 소스로 선택되지 않았거나 다른 앱이 잡고 있습니다. Zoom, Skype, OBS를 닫고 SplitCam 소스 목록에서 웹캠을 다시 고르고 Go Live 전에 미리보기에 영상이 나오는지 확인하세요."),
        ("{name}이 스트림 키를 거부하거나 연결되지 않음",
         "스트림 키를 다시 복사하세요 — 끝의 공백이나 재설정된 오래된 키가 가장 흔한 원인입니다. 서버 URL이 {name}이 표시한 것과 일치하고 계정에 외부 인코더 방송이 켜져 있는지 확인하세요. SplitCam Stream Settings의 초록 슬라이더가 유효한 키를 확인해 줍니다."),
        ("{name}에서 소리가 없거나 음성이 어긋남",
         "SplitCam을 카메라 그리고 마이크로 모두 선택하고 SplitCam 오디오 소스 안에서 진짜 마이크를 고르세요. 오디오가 영상보다 뒤처지면 해상도를 한 단계 낮추세요 — 인코더가 과부하라 오디오가 늦은 프레임을 기다리는 것입니다."),
    ],
    "uk": [
        ("Трансляція {name} гальмує або буферизується",
         "Майже завжди бітрейт заданий вище, ніж витримає ваш аплоуд. Запустіть вбудований тест швидкості SplitCam, далі задайте бітрейт приблизно 75% від виміряного аплоуду — 3500–6000&nbsp;Кбіт/с для 1080p, нижче для 720p. Гальмування зникає, коли кодувальник перестає перевищувати ваш канал."),
        ("Втрата кадрів під час трансляції {name}",
         "Втрата кадрів означає, що пакети не доходять до {name} вчасно — зазвичай нестабільний Wi-Fi. Перейдіть на дротовий Ethernet, закрийте застосунки, що з'їдають канал, і трохи знизьте бітрейт. Один стрибок — це нічого; постійне зростання означає, що канал не встигає."),
        ("Чорний екран — глядачі не бачать відео на {name}",
         "Ваша камера не вибрана як активне джерело у SplitCam, або її тримає інший застосунок. Закрийте Zoom, Skype чи OBS, виберіть вебкамеру знову у списку джерел SplitCam і переконайтеся, що попередній перегляд показує ваше зображення, перш ніж натиснути Go Live."),
        ("{name} відхиляє ключ трансляції або не під'єднується",
         "Скопіюйте ключ трансляції знову — пробіл у кінці чи старий, скинутий ключ — найчастіші причини. Переконайтеся, що URL сервера збігається з тим, що показує {name}, і що трансляція зовнішнім кодувальником увімкнена на акаунті. Зелений повзунок у Stream Settings SplitCam підтверджує дійсний ключ."),
        ("Немає звуку або звук розсинхронізований на {name}",
         "Виберіть SplitCam камерою І мікрофоном, а в джерелі звуку SplitCam виберіть свій справжній мікрофон. Якщо звук відстає від відео, знизьте роздільну здатність на один рівень — кодувальник перевантажений, і звук чекає на запізнілі кадри."),
    ],
    "cs": [
        ("Vysílání {name} se seká nebo bufferuje",
         "Téměř vždy je bitrate nastavený výš, než unese váš upload. Spusťte vestavěný test rychlosti SplitCam, poté nastavte bitrate na zhruba 75 % naměřeného uploadu — 3500–6000&nbsp;Kbps pro 1080p, méně pro 720p. Sekání zmizí, jakmile kodér přestane překračovat vaši linku."),
        ("Ztráta snímků během vysílání {name}",
         "Ztráta snímků znamená, že pakety nedorazí na {name} včas — obvykle nestabilní Wi-Fi. Přejděte na drátový Ethernet, zavřete aplikace požírající pásmo a mírně snižte bitrate. Jeden výkyv nevadí; trvalý nárůst znamená, že linka nestíhá."),
        ("Černá obrazovka — diváci nevidí video na {name}",
         "Vaše kamera není vybraná jako aktivní zdroj ve SplitCam, nebo ji drží jiná aplikace. Zavřete Zoom, Skype nebo OBS, vyberte webkameru znovu v seznamu zdrojů SplitCam a ujistěte se, že náhled ukazuje váš obraz, než stisknete Go Live."),
        ("{name} odmítá stream key nebo se nepřipojuje",
         "Zkopírujte stream key znovu — mezera na konci nebo starý, resetovaný klíč jsou nejčastější příčiny. Ujistěte se, že URL serveru odpovídá tomu, co {name} zobrazuje, a že vysílání externím kodérem je na účtu zapnuté. Zelený posuvník v Stream Settings SplitCam potvrzuje platný klíč."),
        ("Žádný zvuk nebo zvuk nesynchronní na {name}",
         "Vyberte SplitCam jako kameru I mikrofon a ve zdroji zvuku SplitCam vyberte svůj skutečný mikrofon. Pokud zvuk zaostává za videem, snižte rozlišení o úroveň — kodér je přetížený a zvuk čeká na opožděné snímky."),
    ],
    "sk": [
        ("Vysielanie {name} sa seká alebo bufferuje",
         "Takmer vždy je bitrate nastavený vyššie, než unesie váš upload. Spustite vstavaný test rýchlosti SplitCam, potom nastavte bitrate na zhruba 75 % nameraného uploadu — 3500–6000&nbsp;Kbps pre 1080p, menej pre 720p. Sekanie zmizne, keď kodér prestane prekračovať vašu linku."),
        ("Strata snímok počas vysielania {name}",
         "Strata snímok znamená, že pakety nedôjdu na {name} včas — zvyčajne nestabilné Wi-Fi. Prejdite na drôtový Ethernet, zatvorte aplikácie požierajúce pásmo a mierne znížte bitrate. Jeden výkyv nevadí; trvalý nárast znamená, že linka nestíha."),
        ("Čierna obrazovka — diváci nevidia video na {name}",
         "Vaša kamera nie je vybraná ako aktívny zdroj v SplitCam, alebo ju drží iná aplikácia. Zatvorte Zoom, Skype alebo OBS, vyberte webkameru znovu v zozname zdrojov SplitCam a uistite sa, že náhľad ukazuje váš obraz, skôr než stlačíte Go Live."),
        ("{name} odmieta stream key alebo sa nepripája",
         "Skopírujte stream key znovu — medzera na konci alebo starý, resetovaný kľúč sú najčastejšie príčiny. Uistite sa, že URL servera zodpovedá tomu, čo {name} zobrazuje, a že vysielanie externým kodérom je na účte zapnuté. Zelený posuvník v Stream Settings SplitCam potvrdzuje platný kľúč."),
        ("Žiadny zvuk alebo zvuk nesynchronný na {name}",
         "Vyberte SplitCam ako kameru AJ mikrofón a v zdroji zvuku SplitCam vyberte svoj skutočný mikrofón. Ak zvuk zaostáva za videom, znížte rozlíšenie o úroveň — kodér je preťažený a zvuk čaká na oneskorené snímky."),
    ],
    "sv": [
        ("{name}-sändningen hackar eller buffrar",
         "Nästan alltid är bitraten satt högre än din uppladdning klarar. Kör SplitCams inbyggda hastighetstest, ställ sedan in bitrate på runt 75 % av uppmätt uppladdning — 3500–6000&nbsp;Kbps för 1080p, lägre för 720p. Hackandet försvinner när kodaren slutar överstiga din linje."),
        ("Tappade bildrutor under {name}-sändning",
         "Tappade bildrutor betyder att paket inte når {name} i tid — oftast ostabilt Wi-Fi. Byt till kabelansluten Ethernet, stäng appar som äter bandbredd och sänk bitraten något. En enstaka topp gör inget; en stadig ökning betyder att linjen inte hänger med."),
        ("Svart skärm — tittarna ser ingen video på {name}",
         "Din kamera är inte vald som aktiv källa i SplitCam, eller så håller en annan app den. Stäng Zoom, Skype eller OBS, välj webbkameran igen i SplitCams källista och säkerställ att förhandsvisningen visar din bild innan du trycker Go Live."),
        ("{name} avvisar streamnyckeln eller ansluter inte",
         "Kopiera streamnyckeln igen — ett blanksteg i slutet eller en gammal, återställd nyckel är de vanligaste orsakerna. Säkerställ att server-URL:en matchar den {name} visar och att extern kodare-sändning är påslagen på kontot. Det gröna reglaget i SplitCams Stream Settings bekräftar en giltig nyckel."),
        ("Inget ljud eller osynkat ljud på {name}",
         "Välj SplitCam som både kamera OCH mikrofon, och välj din riktiga mikrofon inuti SplitCams ljudkälla. Om ljudet släpar efter videon, sänk upplösningen ett steg — kodaren är överbelastad och ljudet väntar på sena bildrutor."),
    ],
    "ms": [
        ("Siaran {name} tersekat atau menimbal",
         "Hampir sentiasa bitrate ditetapkan lebih tinggi daripada yang mampu ditanggung muat naik anda. Jalankan ujian kelajuan terbina SplitCam, kemudian tetapkan bitrate kira-kira 75% daripada muat naik diukur — 3,500–6,000&nbsp;Kbps untuk 1080p, lebih rendah untuk 720p. Tersekat hilang sebaik pengekod berhenti melebihi talian anda."),
        ("Bingkai hilang semasa siaran {name}",
         "Bingkai hilang bermakna paket tidak sampai ke {name} tepat masa — biasanya Wi-Fi tidak stabil. Beralih ke Ethernet berwayar, tutup apl yang memakan lebar jalur dan turunkan bitrate sedikit. Satu lonjakan tak mengapa; peningkatan berterusan bermakna talian tidak mengejar."),
        ("Skrin hitam — penonton tidak nampak video di {name}",
         "Kamera anda tidak dipilih sebagai sumber aktif dalam SplitCam, atau apl lain menahannya. Tutup Zoom, Skype atau OBS, pilih semula kamera web dalam senarai sumber SplitCam dan pastikan pratonton menunjukkan imej anda sebelum tekan Go Live."),
        ("{name} menolak kunci strim atau tidak menyambung",
         "Salin semula kunci strim — ruang di hujung atau kunci lama yang telah diset semula ialah punca paling biasa. Pastikan URL pelayan sepadan dengan yang {name} paparkan dan siaran pengekod luaran dihidupkan pada akaun anda. Peluncur hijau dalam Stream Settings SplitCam mengesahkan kunci sah."),
        ("Tiada audio atau audio tak segerak di {name}",
         "Pilih SplitCam sebagai kamera DAN mikrofon, dan pilih mikrofon sebenar anda dalam sumber audio SplitCam. Jika audio ketinggalan daripada video, turunkan resolusi satu peringkat — pengekod terlebih beban dan audio menunggu bingkai yang lewat."),
    ],
    "he": [
        ("השידור ב-{name} נתקע או באפרינג",
         "כמעט תמיד הביטרייט מוגדר גבוה ממה שההעלאה שלכם נושאת. הריצו את בדיקת המהירות המובנית של SplitCam, ואז הגדירו ביטרייט לכ-75% מההעלאה הנמדדת — 3,500–6,000&nbsp;Kbps ל-1080p, נמוך יותר ל-720p. התקיעות נעלמת ברגע שהמקודד מפסיק לחרוג מהקו שלכם."),
        ("פריימים שאבדו במהלך שידור {name}",
         "פריימים שאבדו פירושם שחבילות לא מגיעות ל-{name} בזמן — בדרך כלל Wi-Fi לא יציב. עברו ל-Ethernet קווי, סגרו אפליקציות שאוכלות רוחב פס והורידו מעט את הביטרייט. קפיצה בודדת לא נורא; עלייה מתמשכת פירושה שהקו לא עומד בקצב."),
        ("מסך שחור — הצופים לא רואים וידאו ב-{name}",
         "המצלמה שלכם לא נבחרה כמקור פעיל ב-SplitCam, או שאפליקציה אחרת מחזיקה אותה. סגרו Zoom, Skype או OBS, בחרו שוב את המצלמה ברשימת המקורות של SplitCam וודאו שהתצוגה המקדימה מציגה את התמונה לפני לחיצה על Go Live."),
        ("{name} דוחה את מפתח השידור או לא מתחבר",
         "העתיקו שוב את מפתח השידור — רווח בסוף או מפתח ישן שאופס הם הסיבות הנפוצות. ודאו ש-URL השרת תואם למה ש-{name} מציג וששידור במקודד חיצוני מופעל בחשבון. המחוון הירוק ב-Stream Settings של SplitCam מאשר מפתח תקף."),
        ("אין אודיו או אודיו לא מסונכרן ב-{name}",
         "בחרו SplitCam גם כמצלמה וגם כמיקרופון, ובחרו את המיקרופון האמיתי שלכם בתוך מקור האודיו של SplitCam. אם האודיו מפגר אחרי הווידאו, הורידו את הרזולוציה ברמה אחת — המקודד עמוס מדי והאודיו מחכה לפריימים מאוחרים."),
    ],
    "fa": [
        ("پخش {name} متوقف می‌شود یا بافر می‌کند",
         "تقریباً همیشه بیت‌ریت بالاتر از آن تنظیم شده که آپلود شما تحمل کند. تست سرعت داخلی SplitCam را اجرا کنید، سپس بیت‌ریت را به حدود ۷۵٪ آپلود اندازه‌گیری شده تنظیم کنید — ۳۵۰۰–۶۰۰۰&nbsp;Kbps برای ۱۰۸۰p."),
        ("فریم‌های از دست رفته حین پخش {name}",
         "فریم‌های از دست رفته به این معناست که بسته‌ها به {name} به موقع نمی‌رسند — معمولاً Wi-Fi ناپایدار. به Ethernet سیمی تغییر دهید، برنامه‌هایی که پهنای باند می‌خورند را ببندید و بیت‌ریت را کمی کاهش دهید."),
        ("صفحه سیاه — بینندگان ویدیو را در {name} نمی‌بینند",
         "دوربین شما به عنوان منبع فعال در SplitCam انتخاب نشده، یا برنامه دیگری آن را نگه داشته. Zoom، Skype یا OBS را ببندید، وب‌کم را دوباره در لیست منابع SplitCam انتخاب کنید."),
        ("{name} کلید جریان را رد می‌کند یا متصل نمی‌شود",
         "کلید جریان را دوباره کپی کنید — فاصله در انتها یا کلید قدیمی بازنشانی شده رایج‌ترین دلایل هستند. مطمئن شوید URL سرور با آنچه {name} نشان می‌دهد مطابقت دارد."),
        ("صدا وجود ندارد یا صدا در {name} ناهمزمان است",
         "SplitCam را هم به عنوان دوربین و هم میکروفون انتخاب کنید، و میکروفون واقعی خود را در منبع صدای SplitCam انتخاب کنید. اگر صدا از ویدیو عقب می‌ماند، رزولوشن را یک سطح پایین بیاورید."),
    ],
    "hi": [
        ("{name} स्ट्रीम रुक-रुक रही है या बफ़र हो रही है",
         "लगभग हमेशा बिटरेट आपके अपलोड से ज़्यादा सेट होता है। SplitCam का बिल्ट-इन स्पीड टेस्ट चलाएं, फिर बिटरेट मापे गए अपलोड का ~75% सेट करें — 1080p के लिए 3500–6000&nbsp;Kbps। जब एन्कोडर आपकी लाइन से ज़्यादा नहीं जाता तो रुकना बंद हो जाता है।"),
        ("{name} स्ट्रीम के दौरान फ्रेम खो रहे हैं",
         "खोए फ्रेम का मतलब है पैकेट समय पर {name} नहीं पहुंचते — आमतौर पर अस्थिर Wi-Fi। वायर्ड Ethernet पर स्विच करें, बैंडविड्थ खाने वाले ऐप बंद करें और बिटरेट थोड़ा कम करें।"),
        ("ब्लैक स्क्रीन — दर्शक {name} पर वीडियो नहीं देख सकते",
         "आपका कैमरा SplitCam में एक्टिव सोर्स नहीं चुना गया, या कोई दूसरा ऐप इसे रोक रहा है। Zoom, Skype या OBS बंद करें, SplitCam में वेबकैम दोबारा चुनें।"),
        ("{name} स्ट्रीम की रिजेक्ट कर रहा है या कनेक्ट नहीं हो रहा",
         "स्ट्रीम की दोबारा कॉपी करें — अंत में स्पेस या पुरानी रीसेट की सबसे आम कारण हैं। सुनिश्चित करें सर्वर URL वही है जो {name} दिखाता है।"),
        ("{name} पर कोई ऑडियो नहीं या ऑडियो सिंक नहीं है",
         "SplitCam को कैमरा और माइक्रोफ़ोन दोनों के रूप में चुनें, और SplitCam के ऑडियो सोर्स में अपना असली माइक्रोफ़ोन चुनें। अगर ऑडियो वीडियो से पीछे है, रेज़ॉल्यूशन एक स्तर कम करें।"),
    ],
}


def render_trouble(slug, name, lang):
    """Render the troubleshooting section for a platform page."""
    rows = TROUBLE_TMPL.get(lang) or TROUBLE_TMPL["en"]
    items = "".join(
        f'<details class="faq-item"><summary>{e(prob.replace("{name}", name))}</summary>'
        f'<p>{sol.replace("{name}", name)}</p></details>'
        for prob, sol in rows)
    heading = TROUBLE_H.get(lang, TROUBLE_H["en"])
    return (f'<section class="section"><h2 class="sec-h">{heading}</h2>'
            f'<div class="faq-list">{items}</div></section>')


LANG_LABEL = {"en": "EN", "ru": "RU", "es": "ES", "de": "DE", "fr": "FR", "it": "IT",
              "pt": "PT", "nl": "NL", "ro": "RO", "bg": "BG", "hu": "HU",
              "el": "EL", "fi": "FI", "da": "DA", "no": "NO", "sr": "SR", "hr": "HR",
              "zh": "中", "ja": "日", "ar": "ع", "th": "ไทย", "fil": "FIL", "tr": "TR", "id": "ID", "vi": "VI", "pl": "PL", "ko": "KO", "uk": "UK", "cs": "CS", "sk": "SK", "sv": "SV", "ms": "MS", "he": "עב", "fa": "فا", "hi": "हि"}
LANG_FLAG = {"en": "🇬🇧", "ru": "🇷🇺", "es": "🇪🇸", "de": "🇩🇪", "fr": "🇫🇷", "it": "🇮🇹",
             "pt": "🇧🇷", "nl": "🇳🇱", "ro": "🇷🇴", "bg": "🇧🇬", "hu": "🇭🇺",
             "el": "🇬🇷", "fi": "🇫🇮", "da": "🇩🇰", "no": "🇳🇴", "sr": "🇷🇸", "hr": "🇭🇷",
             "zh": "🇨🇳", "ja": "🇯🇵", "ar": "🇸🇦", "th": "🇹🇭", "fil": "🇵🇭", "tr": "🇹🇷", "id": "🇮🇩", "vi": "🇻🇳", "pl": "🇵🇱", "ko": "🇰🇷", "uk": "🇺🇦", "cs": "🇨🇿", "sk": "🇸🇰", "sv": "🇸🇪", "ms": "🇲🇾", "he": "🇮🇱", "fa": "🇮🇷", "hi": "🇮🇳"}
LANG_NATIVE = {"en": "English", "ru": "Русский", "es": "Español", "de": "Deutsch",
               "fr": "Français", "it": "Italiano", "pt": "Português", "nl": "Nederlands",
               "ro": "Română", "bg": "Български", "hu": "Magyar", "el": "Ελληνικά",
               "fi": "Suomi", "da": "Dansk", "no": "Norsk", "sr": "Српски", "hr": "Hrvatski",
               "zh": "中文", "ja": "日本語", "ar": "العربية", "th": "ไทย", "fil": "Filipino",
               "tr": "Türkçe", "id": "Bahasa Indonesia", "vi": "Tiếng Việt", "pl": "Polski", "ko": "한국어",
               "uk": "Українська", "cs": "Čeština", "sk": "Slovenčina", "sv": "Svenska",
               "ms": "Bahasa Melayu", "he": "עברית",
               "fa": "فارسی",
               "hi": "हिन्दी"}
LANG_PATH = {"en": "", "ru": "ru/", "es": "es/", "de": "de/", "fr": "fr/", "it": "it/",
             "pt": "pt/", "nl": "nl/", "ro": "ro/", "bg": "bg/", "hu": "hu/",
             "el": "el/", "fi": "fi/", "da": "da/", "no": "no/", "sr": "sr/", "hr": "hr/",
             "zh": "zh/", "ja": "ja/", "ar": "ar/", "th": "th/", "fil": "fil/", "tr": "tr/", "id": "id/", "vi": "vi/", "pl": "pl/", "ko": "ko/", "uk": "uk/", "cs": "cs/", "sk": "sk/", "sv": "sv/", "ms": "ms/", "he": "he/", "fa": "fa/", "hi": "hi/"}


# YouTube video IDs per platform (one tutorial video each, language-agnostic).
VIDEOS = {
    "bongacams": "QJPwJHVbYio", "cam4": "40F6C_cvXyQ", "camplace": "1smUXVUzyAo",
    "camsoda": "mCUrXWoTYXM", "chaturbate": "ynClBb7wbg0", "flirt4free": "1fX20UU6w6Q",
    "imlive": "qMWOaNZMGgc", "lovense": "JK7xSVCqjsA", "mfc-alerts": "Ps5--obPRvw",
    "multistream-cams": "MWLSQKDQCY0", "onlyfans": "pNw0yJ-bGXQ", "soulcams": "iyzOi9tKOJ4",
    "streamate": "tEFVec3b-MU", "streamray": "i0CN1q-yLK4", "stripchat": "i_Nbv2wAKTg",
    "virtwish": "mJGi9-Ffp74", "vxlive": "7A0wuhtqkAw", "xlovecam": "myrur7zCHak",
    "xmodels": "v-QUSgra5v8",
}
VIDEO_H = {"en": "Video guide", "ru": "Видео-гайд", "es": "Guía en vídeo",
           "de": "Video-Anleitung", "fr": "Guide vidéo", "it": "Guida video",
           "pt": "Guia em vídeo", "nl": "Videogids",
           "ro": "Ghid video", "bg": "Видео ръководство", "hu": "Videós útmutató",
           "el": "Οδηγός βίντεο", "fi": "Video-opas", "da": "Videoguide",
           "no": "Videoguide", "sr": "Видео водич", "hr": "Video vodič",
           "zh": "视频指南", "ja": "ビデオガイド", "ar": "دليل الفيديو",
           "th": "คู่มือวิดีโอ", "fil": "Gabay sa video", "tr": "Video rehberi", "id": "Panduan video",
           "vi": "Video hướng dẫn", "pl": "Poradnik wideo", "ko": "영상 가이드", "uk": "Відеопосібник",
           "cs": "Videonávod", "sk": "Videonávod", "sv": "Videoguide", "ms": "Panduan video",
           "he": "מדריך וידאו", "fa": "راهنمای ویدیو", "hi": "वीडियो गाइड"}
COLLAB_LABEL = {"en": "Setup guide", "ru": "Гайд по настройке", "es": "Guía de configuración",
                "de": "Setup-Anleitung", "fr": "Guide d'installation", "it": "Guida alla configurazione",
                "pt": "Guia de configuração", "nl": "Installatiegids",
                "ro": "Ghid de configurare", "bg": "Ръководство за настройка",
                "hu": "Beállítási útmutató", "el": "Οδηγός εγκατάστασης",
                "fi": "Asennusohje", "da": "Opsætningsguide", "no": "Oppsettsguide",
                "sr": "Водич за подешавање", "hr": "Vodič za postavljanje",
                "zh": "设置指南", "ja": "セットアップガイド", "ar": "دليل الإعداد",
                "th": "คู่มือการตั้งค่า", "fil": "Gabay sa setup", "tr": "Kurulum rehberi", "id": "Panduan setup",
                "vi": "Hướng dẫn thiết lập", "pl": "Poradnik konfiguracji", "ko": "설정 가이드", "uk": "Посібник з налаштування",
                "cs": "Návod k nastavení", "sk": "Návod na nastavenie", "sv": "Installationsguide", "ms": "Panduan persediaan",
                "he": "מדריך הגדרה", "fa": "راهنمای تنظیم", "hi": "सेटअप गाइड"}

# Brand-ish accent colour per platform — used for the hero collab badge.
BRAND = {
    "chaturbate": "#f5871f", "cam4": "#ff5a3c", "bongacams": "#e6325f",
    "stripchat": "#e8a200", "onlyfans": "#00aff0", "camplace": "#6d5bd0",
    "camsoda": "#16b8be", "streamate": "#3f7fd6", "streamray": "#b03636",
    "xlovecam": "#d6307a", "soulcams": "#8455d6", "imlive": "#e0644a",
    "vxlive": "#e5006d", "virtwish": "#7b56e0", "xmodels": "#c44d96",
    "flirt4free": "#d63d6a", "mfc-alerts": "#1e9e57", "lovense": "#00b3b6",
    "multistream-cams": "#2878fc",
}
SHOT_EXTS = ("png", "jpg", "jpeg", "webp")


# Official support contacts per platform. Verified from each platform's own
# help / contact pages. Omit a key when the platform doesn't publish one.
PLATFORM_SUPPORT = {
    "chaturbate":  {"email": "support@chaturbate.com",       "url": "https://support.chaturbate.com/hc/en-us"},
    "cam4":        {"email": "support@cam4.biz",             "url": "https://www.cam4support.com/"},
    "bongacams":   {"email": "support@bongacams.com",        "url": "https://bongacams.com/contacts"},
    "stripchat":   {"email": "help@stripchat.com",           "url": "https://support.stripchat.com/hc/en-us"},
    "onlyfans":    {"email": "support@onlyfans.com",         "url": "https://onlyfans.com/help"},
    "camplace":    {                                          "url": "https://www.camplace.com/contact"},
    "camsoda":     {"email": "modelsupport@camsoda.com",     "url": "https://www.camsoda.com/support"},
    "streamate":   {"email": "smsupport@streamatemodels.com","url": "https://www.streamatemodels.com/"},
    "streamray":   {                                          "url": "https://streamray.com/"},
    "xlovecam":    {                                          "url": "https://www.xlovecam.com/en/contact"},
    "soulcams":    {                                          "url": "https://soulcams.com/"},
    "imlive":      {                                          "url": "https://imlive.com/help/CsCenter.aspx"},
    "vxlive":      {                                          "url": "https://helpcenter.vxmodels.com/", "ticket": "https://support.vxmodels.com/"},
    "virtwish":    {                                          "url": "https://t.me/vwsupport", "chat": "https://t.me/vwsupport"},
    "xmodels":     {"email": "info@xmodels.com",             "url": "https://www.xmodels.com/contact"},
    "flirt4free":  {"email": "customerservice@flirt4free.com","url": "https://www.flirt4free.com/help"},
    "mfc-alerts":  {"email": "mfcalerts@myfreecamsmail.com", "url": "https://mfcalerts.com/"},
    "lovense":     {"email": "support@lovense.com",          "url": "https://support.lovense.com/"},
    "multistream-cams": {"email": "hello@splitcam.com",      "url": "https://splitcam.com/support"},
}

# Localized heading + disclaimer for the platform support block.
# (heading, note)
SUPPORT_LABELS = {
    "en":  ("Official support", "We are an independent guide. For account, payment or technical issues contact the platform's official support directly."),
    "ru":  ("Официальная поддержка платформы", "Мы независимый ресурс. По вопросам аккаунта, выплат или техподдержки обращайтесь в официальный саппорт платформы напрямую."),
    "es":  ("Soporte oficial", "Somos una guía independiente. Para problemas de cuenta, pagos o técnicos contacta directamente con el soporte oficial de la plataforma."),
    "de":  ("Offizieller Support", "Wir sind ein unabhängiger Guide. Bei Konto-, Zahlungs- oder technischen Problemen wende dich direkt an den offiziellen Support der Plattform."),
    "fr":  ("Support officiel", "Nous sommes un guide indépendant. Pour les problèmes de compte, de paiement ou techniques, contactez directement le support officiel de la plateforme."),
    "it":  ("Supporto ufficiale", "Siamo una guida indipendente. Per problemi di account, pagamenti o tecnici contatta direttamente il supporto ufficiale della piattaforma."),
    "pt":  ("Suporte oficial", "Somos um guia independente. Pra questões de conta, pagamentos ou problemas técnicos, fale direto com o suporte oficial da plataforma."),
    "nl":  ("Officiële support", "We zijn een onafhankelijke gids. Voor account-, betaal- of technische problemen neem direct contact op met de officiële support van het platform."),
    "ro":  ("Suport oficial", "Suntem un ghid independent. Pentru probleme de cont, plată sau tehnice, contactează direct suportul oficial al platformei."),
    "bg":  ("Официална поддръжка", "Ние сме независим ресурс. За въпроси по акаунт, плащания или технически проблеми се свържи директно с официалната поддръжка на платформата."),
    "hu":  ("Hivatalos támogatás", "Független útmutató vagyunk. Fiók-, fizetési vagy technikai problémák esetén lépj kapcsolatba közvetlenül a platform hivatalos támogatásával."),
    "el":  ("Επίσημη υποστήριξη", "Είμαστε ανεξάρτητος οδηγός. Για ζητήματα λογαριασμού, πληρωμών ή τεχνικά προβλήματα επικοινωνήστε απευθείας με την επίσημη υποστήριξη της πλατφόρμας."),
    "fi":  ("Virallinen tuki", "Olemme riippumaton opas. Tili-, maksu- tai teknisten ongelmien yhteydessä ota suoraan yhteyttä alustan viralliseen tukeen."),
    "da":  ("Officiel support", "Vi er en uafhængig guide. Ved konto-, betalings- eller tekniske problemer kontakt platformens officielle support direkte."),
    "no":  ("Offisiell støtte", "Vi er en uavhengig guide. For konto-, betalings- eller tekniske problemer kontakt plattformens offisielle støtte direkte."),
    "sr":  ("Званична подршка", "Ми смо независан водич. За питања налога, плаћања или техничке проблеме обратите се директно званичној подршци платформе."),
    "hr":  ("Službena podrška", "Mi smo neovisan vodič. Za pitanja računa, plaćanja ili tehničke probleme obratite se izravno službenoj podršci platforme."),
    "zh":  ("官方支持", "我们是独立的指南。如有账户、付款或技术问题，请直接联系平台的官方支持。"),
    "ja":  ("公式サポート", "私たちは独立したガイドです。アカウント、支払い、技術的な問題については、プラットフォームの公式サポートに直接お問い合わせください。"),
    "ar":  ("الدعم الرسمي", "نحن دليل مستقل. لمشاكل الحساب أو الدفع أو الفنية، تواصل مباشرة مع الدعم الرسمي للمنصة."),
    "th":  ("ฝ่ายสนับสนุนอย่างเป็นทางการ", "เราคือคู่มืออิสระ สำหรับปัญหาเกี่ยวกับบัญชี การชำระเงิน หรือปัญหาทางเทคนิค โปรดติดต่อฝ่ายสนับสนุนอย่างเป็นทางการของแพลตฟอร์มโดยตรง"),
    "fil": ("Opisyal na suporta", "Kami ay isang independyenteng gabay. Para sa mga isyu sa account, bayad o teknikal, direktang kontakin ang opisyal na suporta ng platform."),
    "tr": ("Resmi destek", "Biz bağımsız bir rehberiz. Hesap, ödeme veya teknik sorunlar için doğrudan platformun resmi desteğiyle iletişime geç."),
    "id": ("Dukungan resmi", "Kami panduan independen. Untuk masalah akun, pembayaran, atau teknis, hubungi langsung dukungan resmi platform."),
    "vi": ("Hỗ trợ chính thức", "Chúng tôi là hướng dẫn độc lập. Với vấn đề tài khoản, thanh toán hoặc kỹ thuật, hãy liên hệ trực tiếp hỗ trợ chính thức của nền tảng."),
    "pl": ("Oficjalne wsparcie", "Jesteśmy niezależnym poradnikiem. W sprawach konta, płatności lub problemów technicznych skontaktuj się bezpośrednio z oficjalnym wsparciem platformy."),
    "ko": ("공식 지원", "저희는 독립 가이드입니다. 계정, 결제, 기술 문제는 플랫폼의 공식 지원에 직접 문의하세요."),
    "uk": ("Офіційна підтримка", "Ми незалежний посібник. З питань акаунта, платежів чи технічних проблем звертайтеся напряму до офіційної підтримки платформи."),
    "cs": ("Oficiální podpora", "Jsme nezávislý průvodce. S problémy s účtem, platbami nebo technikou se obraťte přímo na oficiální podporu platformy."),
    "sk": ("Oficiálna podpora", "Sme nezávislý sprievodca. S problémami s účtom, platbami alebo technikou sa obráťte priamo na oficiálnu podporu platformy."),
    "sv": ("Officiell support", "Vi är en oberoende guide. För konto-, betalnings- eller tekniska problem, kontakta plattformens officiella support direkt."),
    "ms": ("Sokongan rasmi", "Kami panduan bebas. Untuk isu akaun, pembayaran atau teknikal, hubungi sokongan rasmi platform secara terus."),
    "he": ("תמיכה רשמית", "אנחנו מדריך עצמאי. לבעיות חשבון, תשלום או טכניות, פנו ישירות לתמיכה הרשמית של הפלטפורמה."),
    "fa": ("پشتیبانی رسمی", "ما یک راهنمای مستقل هستیم. برای مشکلات حساب، پرداخت یا فنی، مستقیماً با پشتیبانی رسمی پلتفرم تماس بگیرید."),
    "hi": ("आधिकारिक सहायता", "हम एक स्वतंत्र गाइड हैं। अकाउंट, भुगतान या तकनीकी समस्याओं के लिए सीधे प्लेटफ़ॉर्म की आधिकारिक सहायता से संपर्क करें।"),
}


def render_support(slug, name, lang):
    """Render the official-platform-support block for a platform page, or '' if no contacts known."""
    sup = PLATFORM_SUPPORT.get(slug)
    if not sup:
        return ""
    heading, note = SUPPORT_LABELS.get(lang, SUPPORT_LABELS["en"])
    items = []
    if sup.get("email"):
        items.append(
            f'<li class="sp-row"><span class="sp-icon" aria-hidden="true">✉️</span>'
            f'<a href="mailto:{sup["email"]}">{sup["email"]}</a></li>'
        )
    if sup.get("url"):
        items.append(
            f'<li class="sp-row"><span class="sp-icon" aria-hidden="true">🌐</span>'
            f'<a href="{sup["url"]}" rel="nofollow noopener" target="_blank">{sup["url"]}</a></li>'
        )
    if sup.get("ticket"):
        items.append(
            f'<li class="sp-row"><span class="sp-icon" aria-hidden="true">🎫</span>'
            f'<a href="{sup["ticket"]}" rel="nofollow noopener" target="_blank">{sup["ticket"]}</a></li>'
        )
    if sup.get("chat") and sup.get("chat") != sup.get("url"):
        items.append(
            f'<li class="sp-row"><span class="sp-icon" aria-hidden="true">💬</span>'
            f'<a href="{sup["chat"]}" rel="nofollow noopener" target="_blank">{sup["chat"]}</a></li>'
        )
    if not items:
        return ""
    return (
        f'<section class="section sp-block"><h2 class="sec-h">{heading} — {e(name)}</h2>'
        f'<ul class="sp-list">{"".join(items)}</ul>'
        f'<p class="sp-note">{note}</p></section>'
    )


def shot_for(slug, n, depth, caption):
    """Return a figure block if a screenshot file exists for this step, else ''.
    Convention: shots/<slug>-<n>.<ext> — e.g. shots/onlyfans-3.png for step 3."""
    for ext in SHOT_EXTS:
        if (ROOT / "shots" / f"{slug}-{n}.{ext}").exists():
            return (f'<figure class="shot"><img src="{depth}shots/{slug}-{n}.{ext}" '
                    f'alt="{e(caption)}" loading="lazy">'
                    f'<figcaption>{e(caption)}</figcaption></figure>')
    return ""


LOGO_EXTS = ("svg", "png", "webp")


def platform_logo(slug, depth, name):
    """Official platform logo if dropped in logos/<slug>.<ext>, else the name as text.
    Drop a logo file and it replaces the wordmark automatically on rebuild."""
    for ext in LOGO_EXTS:
        if (ROOT / "logos" / f"{slug}.{ext}").exists():
            return f'<img class="collab-logo" src="{depth}logos/{slug}.{ext}" alt="{e(name)}">'
    return e(name)


def lang_switch(cur, depth, slug=None):
    """Language switcher. slug set -> platform pages; slug None -> hub pages."""
    items = []
    # Sort alphabetically by native language name (Latin → Cyrillic → Greek → Arabic → Thai → CJK).
    for L in sorted(LANGS_AVAIL, key=lambda x: LANG_NATIVE[x]):
        if slug:
            href = f"{depth}{LANG_PATH[L]}{slug}/"
        else:
            href = f"{depth}{LANG_PATH[L]}" or "./"
        cls = ' class="cur"' if L == cur else ""
        items.append(
            f'<a href="{href}" data-lang="{L}"{cls}>'
            f'<span class="lf">{LANG_FLAG[L]}</span>'
            f'<span class="ln">{LANG_NATIVE[L]}</span></a>'
        )
    return (
        '<details class="lang-dl">'
        f'<summary aria-label="Language"><span class="lf">{LANG_FLAG[cur]}</span>'
        f'<span class="lc">{LANG_LABEL[cur]}</span>'
        '<span class="dl-caret">▾</span></summary>'
        f'<div class="lang-dl-menu">{"".join(items)}</div>'
        '</details>'
    )


def render(p, lang, all_platforms):
    """Render one platform guide page."""
    u = UI[lang]
    d = p[lang]
    depth = "../../" if u["path"] else "../"   # from <path><slug>/index.html back to repo root
    home = depth                                # site root for this language section
    name = p["name"]

    # related: 3 other platforms
    others = [x for x in all_platforms if x["slug"] != p["slug"] and lang in x][:3]
    related = "".join(
        f'<a class="related-card" href="../{x["slug"]}/"><h4>{e(x[lang]["h1short"])}</h4>'
        f'<p>{e(x[lang]["card"])}</p></a>' for x in others)

    steps = build_steps(p, lang)
    steps_html = "".join(
        f'<div class="step"><div class="step-num">{i+1}</div><div class="step-body">'
        f'<div class="step-h">{e(s[0])}</div><p class="step-p">{s[1]}</p>'
        f'{shot_for(p["slug"], i+1, depth, s[0])}</div></div>'
        for i, s in enumerate(steps))

    brand = BRAND.get(p["slug"], "#2878fc")
    vid = VIDEOS.get(p["slug"])
    video_section = ""
    if vid:
        video_section = (
            f'<section class="section"><h2 class="sec-h">{VIDEO_H[lang]}</h2>'
            f'<div class="video-wrap"><iframe src="https://www.youtube-nocookie.com/embed/{vid}" '
            f'title="{e(_strip(d["h1html"]))}" loading="lazy" '
            f'allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div></section>')

    tips_html = "".join(
        f'<div class="tip-card"><h3>{e(t[0])}</h3><p>{t[1]}</p></div>'
        for t in d["tips"])

    faq_html = "".join(
        f'<details class="faq-item"><summary>{e(q)}</summary><p>{a}</p></details>'
        for q, a in d["faq"])

    support_html = render_support(p["slug"], name, lang)
    trouble_html = render_trouble(p["slug"], name, lang)
    trouble_rows = TROUBLE_TMPL.get(lang) or TROUBLE_TMPL["en"]

    canon = f'{SITE}/{u["path"]}{p["slug"]}/'
    og_image = f'{SITE}/assets/og/{p["slug"]}.png'
    hreflang_html = "\n".join(
        f'<link rel="alternate" hreflang="{L}" href="{SITE}/{LANG_PATH[L]}{p["slug"]}/">'
        for L in LANGS_AVAIL
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/{p["slug"]}/">'
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": u["crumb_home"],
                 "item": f'{SITE}/{u["path"]}'},
                {"@type": "ListItem", "position": 2, "name": name, "item": canon}]},
            {"@type": "HowTo", "name": _strip(d["h1html"]), "description": d["desc"],
             "totalTime": "PT5M", "inLanguage": lang,
             "datePublished": PUBLISHED_DATE, "dateModified": MODIFIED_DATE,
             "publisher": PUBLISHER, "image": og_image,
             "step": [{"@type": "HowToStep", "position": i+1, "name": s[0],
                       "text": html.unescape(_strip(s[1]))}
                      for i, s in enumerate(steps)]},
            {"@type": "FAQPage", "inLanguage": lang, "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": html.unescape(_strip(a))}}
                for q, a in d["faq"]] + [
                {"@type": "Question", "name": prob.replace("{name}", name),
                 "acceptedAnswer": {"@type": "Answer",
                                    "text": html.unescape(_strip(sol.replace("{name}", name)))}}
                for prob, sol in trouble_rows]},
            {"@type": "SoftwareApplication", "name": "SplitCam",
             "applicationCategory": "MultimediaApplication",
             "operatingSystem": "Windows, macOS",
             "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
        ],
    }

    return f"""<!DOCTYPE html>
<html lang="{u['lang']}"{" dir=\"rtl\"" if u['lang'] in RTL_LANGS else ""}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(d['title'])}</title>
<meta name="description" content="{e(d['desc'])}">
<meta name="keywords" content="{e(d['kw'])}">
<link rel="canonical" href="{canon}">
{hreflang_html}
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/svg+xml" href="{depth}favicon.svg">
<link rel="icon" type="image/x-icon" href="{depth}favicon.ico">
<link rel="apple-touch-icon" href="{depth}apple-touch-icon.png">
<!-- <meta name="google-site-verification" content="YOUR-GSC-TOKEN"> -->
<!-- <meta name="msvalidate.01" content="YOUR-BING-TOKEN"> -->
<!-- <meta name="yandex-verification" content="YOUR-YANDEX-TOKEN"> -->
<meta property="og:type" content="article">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{e(d['title'])}">
<meta property="og:description" content="{e(d['desc'])}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(d['title'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(d['title'])}">
<meta name="twitter:description" content="{e(d['desc'])}">
<meta name="twitter:image" content="{og_image}">
<meta name="theme-color" content="#141420">
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=1)}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
{LANG_REDIRECT_JS}
{AHREFS_JS}
</head>
<body>
{nav_html(home, u['home'], lang_switch(lang, depth, p['slug']))}
<div class="breadcrumbs">
  <a href="{home}">{u['crumb_home']}</a><span class="sep">/</span><span>{e(name)}</span>
</div>
<section class="hero">
  <div class="hero-glow"></div>
  <div class="hero-inner">
    <div class="hero-text">
      <span class="eyebrow">{e(name)}</span>
      <h1 class="h1">{d['h1html']}</h1>
      <p class="sub">{d['intro']}</p>
      <div class="hero-cta">
        <details class="dl">
          <summary class="btn-primary btn-lg">⬇ {u['download']} <span class="dl-caret">▾</span></summary>
          <div class="dl-menu">
            <a href="{e(DOWNLOAD_URL)}" target="_blank" rel="nofollow noopener">Windows</a>
            <a href="{e(DOWNLOAD_URL)}" target="_blank" rel="nofollow noopener">macOS</a>
            <a href="{e(DOWNLOAD_URL)}" target="_blank" rel="nofollow noopener">Android</a>
            <a href="{e(DOWNLOAD_URL)}" target="_blank" rel="nofollow noopener">iOS</a>
          </div>
        </details>
        <a href="#steps" class="btn-ghost btn-lg">{u['skip']} ↓</a>
      </div>
    </div>
    <div class="collab" aria-hidden="true">
      <div class="collab-flow">
        <div class="collab-pill collab-sc"><img src="{depth}assets/splitcam.png" alt=""><span>splitcam</span></div>
        <div class="collab-wire"><div class="collab-dot"></div></div>
        <div class="collab-pill collab-plat collab-plat-{p["slug"]}" style="background:{brand}"><img src="{depth}logos/round/{p["slug"]}.png" alt=""><span>{e(name)}</span></div>
      </div>
      <div class="collab-label">{COLLAB_LABEL[lang]}</div>
    </div>
  </div>
</section>
<div class="section">
  <div class="qa-box">
    <div class="qa-h">{u['quick']}</div>
    <div class="qa-text">{d['quick'].split('<ol>')[0]}</div>
  </div>
</div>
{video_section}
<section class="section" id="steps">
  <h2 class="sec-h">{u['steps_h']}</h2>
  <div class="steps">{steps_html}</div>
</section>
<section class="section">
  <h2 class="sec-h">{u['tips_h']}</h2>
  <div class="tips-grid">{tips_html}</div>
</section>
{trouble_html}
<section class="section">
  <h2 class="sec-h">{u['faq_h']}</h2>
  <div class="faq-list">{faq_html}</div>
</section>
{support_html}
<div class="section">
  <h3 style="font-size:17px;font-weight:700;margin-bottom:4px">{u['related']}</h3>
  <div class="related-grid">{related}</div>
</div>
<section class="cta-block">
  <h2>{u['cta_h']}</h2>
  <p>{u['cta_p']}</p>
  <a href="{e(DOWNLOAD_URL)}" class="btn-primary btn-lg" target="_blank" rel="nofollow noopener">⬇ {u['download']}</a>
</section>
<footer>
  <div class="footer-inner">
    <div>© 2026 {SITE_NAME} · <span class="age-tag-sm">18+</span></div>
    <div class="footer-links">
      <a href="{home}">{u['home']}</a>
      <a href="{depth}{MODEL_SLUG}/">{e(MODEL_GUIDE.get(lang, MODEL_GUIDE["en"])["h1short"])}</a>
      <a href="{depth}{OBS_SLUG}/">{OBS_NAV.get(lang, "SplitCam vs OBS")}</a>
      <a href="{depth}about/">{u['about']}</a>
      <a href="{depth}contact/">{u['contact']}</a>
      <a href="{depth}privacy/">{u['privacy']}</a>
      <a href="{depth}terms/">{u['terms']}</a>
    </div>
  </div>
</footer>
<div class="sticky-dl" id="stickyDl"><a href="{e(DOWNLOAD_URL)}" target="_blank" rel="nofollow noopener">⬇ {u['download']}</a></div>
{STICKY_DL_JS}
</body>
</html>
"""


def _strip(s):
    """Remove HTML tags for use in JSON-LD plain text."""
    import re
    return re.sub(r"<[^>]+>", "", s)


HUB = {
    "en": {"title": "Streaming Guides — Free Cam Broadcasting Setup Guides",
           "desc": "Free step-by-step guides to broadcast on any cam platform with SplitCam.",
           "h1": 'Free cam <span class="accent">broadcasting guides</span>',
           "sub": "Step-by-step setup for streaming to any cam platform with free SplitCam — "
                  "external encoder, scenes, overlays, no watermark.",
           "pick": "Pick your platform"},
    "ru": {"title": "Гайды по трансляциям — настройка вещания на кам-платформы",
           "desc": "Бесплатные пошаговые гайды по вещанию на кам-платформы через SplitCam.",
           "h1": 'Гайды по <span class="accent">вещанию на камах</span>',
           "sub": "Пошаговая настройка трансляций на любую кам-платформу через бесплатный "
                  "SplitCam — внешний кодировщик, сцены, наложения, без водяного знака.",
           "pick": "Выберите платформу"},
    "es": {"title": "Guías de streaming — configuración de emisión en plataformas cam",
           "desc": "Guías gratuitas paso a paso para emitir en plataformas cam con SplitCam.",
           "h1": 'Guías de <span class="accent">emisión cam</span>',
           "sub": "Configuración paso a paso para emitir en cualquier plataforma cam con SplitCam "
                  "gratis — codificador externo, escenas, superposiciones, sin marca de agua.",
           "pick": "Elige tu plataforma"},
    "de": {"title": "Streaming-Anleitungen — Cam-Übertragungen mit SplitCam einrichten",
           "desc": "Kostenlose Schritt-für-Schritt-Anleitungen zum Senden auf Cam-Plattformen mit SplitCam.",
           "h1": 'Kostenlose <span class="accent">Cam-Stream-Anleitungen</span>',
           "sub": "Schritt-für-Schritt-Setup für Übertragungen auf jeder Cam-Plattform mit dem "
                  "kostenlosen SplitCam — externer Encoder, Szenen, Overlays, kein Wasserzeichen.",
           "pick": "Wähle deine Plattform"},
    "fr": {"title": "Guides de streaming — diffusion sur les plateformes cam avec SplitCam",
           "desc": "Guides gratuits, pas à pas, pour diffuser sur les plateformes cam avec SplitCam.",
           "h1": 'Guides gratuits de <span class="accent">streaming cam</span>',
           "sub": "Configuration pas à pas pour diffuser sur toutes les plateformes cam avec "
                  "SplitCam gratuit — encodeur externe, scènes, overlays, sans filigrane.",
           "pick": "Choisis ta plateforme"},
    "it": {"title": "Guide allo streaming — trasmissioni cam con SplitCam",
           "desc": "Guide gratuite passo dopo passo per trasmettere sulle piattaforme cam con SplitCam.",
           "h1": 'Guide gratuite allo <span class="accent">streaming cam</span>',
           "sub": "Configurazione passo dopo passo per trasmettere su qualsiasi piattaforma cam "
                  "con SplitCam gratuito — encoder esterno, scene, sovrapposizioni, senza filigrana.",
           "pick": "Scegli la tua piattaforma"},
    "pt": {"title": "Guias de streaming — transmissões cam com SplitCam",
           "desc": "Guias grátis passo a passo pra transmitir nas plataformas cam com SplitCam.",
           "h1": 'Guias grátis de <span class="accent">streaming cam</span>',
           "sub": "Configuração passo a passo pra transmitir em qualquer plataforma cam com "
                  "o SplitCam grátis — encoder externo, cenas, sobreposições, sem marca d'água.",
           "pick": "Escolha sua plataforma"},
    "nl": {"title": "Streaminggidsen — cam-uitzendingen met SplitCam",
           "desc": "Gratis stap-voor-stap gidsen voor uitzenden op camplatforms met SplitCam.",
           "h1": 'Gratis <span class="accent">cam-stream-gidsen</span>',
           "sub": "Stap-voor-stap setup voor uitzenden op elk camplatform met gratis "
                  "SplitCam — externe encoder, scènes, overlays, geen watermerk.",
           "pick": "Kies je platform"},
    "ro": {"title": "Ghiduri de streaming — transmisiuni cam cu SplitCam",
           "desc": "Ghiduri gratuite pas cu pas pentru transmisiuni pe platforme cam cu SplitCam.",
           "h1": 'Ghiduri gratuite de <span class="accent">streaming cam</span>',
           "sub": "Configurare pas cu pas pentru transmisiuni pe orice platformă cam cu "
                  "SplitCam gratuit — encoder extern, scene, suprapuneri, fără filigran.",
           "pick": "Alege-ți platforma"},
    "bg": {"title": "Ръководства за стрийминг — кам излъчвания със SplitCam",
           "desc": "Безплатни стъпка по стъпка ръководства за излъчване на кам платформи със SplitCam.",
           "h1": 'Безплатни ръководства за <span class="accent">кам стрийминг</span>',
           "sub": "Стъпка по стъпка настройка за излъчване на всяка кам платформа с "
                  "безплатния SplitCam — външен енкодер, сцени, наслагвания, без воден знак.",
           "pick": "Избери своята платформа"},
    "hu": {"title": "Streaming útmutatók — cam adások SplitCammel",
           "desc": "Ingyenes lépésről lépésre útmutatók cam platformokon való adáshoz SplitCammel.",
           "h1": 'Ingyenes <span class="accent">cam streaming útmutatók</span>',
           "sub": "Lépésről lépésre beállítás bármely cam platformra az ingyenes SplitCammel — "
                  "külső enkóder, jelenetek, overlay-ek, vízjel nélkül.",
           "pick": "Válaszd ki a platformodat"},
    "el": {"title": "Οδηγοί streaming — μεταδόσεις cam με SplitCam",
           "desc": "Δωρεάν οδηγοί βήμα προς βήμα για μεταδόσεις σε cam πλατφόρμες με SplitCam.",
           "h1": 'Δωρεάν οδηγοί <span class="accent">cam streaming</span>',
           "sub": "Εγκατάσταση βήμα προς βήμα για μετάδοση σε οποιαδήποτε cam πλατφόρμα με "
                  "το δωρεάν SplitCam — εξωτερικός encoder, σκηνές, overlays, χωρίς υδατογράφημα.",
           "pick": "Επίλεξε την πλατφόρμα σου"},
    "fi": {"title": "Suoratoisto-oppaat — cam-lähetykset SplitCamilla",
           "desc": "Ilmaiset vaihe vaiheelta oppaat cam-alustojen lähetyksiin SplitCamilla.",
           "h1": 'Ilmaiset <span class="accent">cam-striimioppaat</span>',
           "sub": "Vaihe vaiheelta asennus mille tahansa cam-alustalle ilmaisella SplitCamilla — "
                  "ulkoinen enkooderi, näkymät, overlayt, ei vesileimaa.",
           "pick": "Valitse alustasi"},
    "da": {"title": "Streaming-guides — cam-udsendelser med SplitCam",
           "desc": "Gratis trin-for-trin guides til udsendelse på cam-platforme med SplitCam.",
           "h1": 'Gratis <span class="accent">cam-streaming-guides</span>',
           "sub": "Trin-for-trin opsætning til udsendelse på enhver cam-platform med gratis "
                  "SplitCam — ekstern encoder, scener, overlays, intet vandmærke.",
           "pick": "Vælg din platform"},
    "no": {"title": "Strømmingsguider — cam-sendinger med SplitCam",
           "desc": "Gratis trinn-for-trinn guider for sendinger på cam-plattformer med SplitCam.",
           "h1": 'Gratis <span class="accent">cam-strømmingsguider</span>',
           "sub": "Trinn-for-trinn oppsett for sending på enhver cam-plattform med gratis "
                  "SplitCam — ekstern enkoder, scener, overlays, uten vannmerke.",
           "pick": "Velg plattformen din"},
    "sr": {"title": "Водичи за стриминг — кам преноси са SplitCam-ом",
           "desc": "Бесплатни водичи корак по корак за преносе на кам платформама са SplitCam-ом.",
           "h1": 'Бесплатни водичи за <span class="accent">кам стриминг</span>',
           "sub": "Подешавање корак по корак за пренос на било којој кам платформи са "
                  "бесплатним SplitCam-ом — спољни енкодер, сцене, преклапања, без воденог жига.",
           "pick": "Изабери своју платформу"},
    "hr": {"title": "Vodiči za streaming — cam prijenosi sa SplitCamom",
           "desc": "Besplatni vodiči korak po korak za prijenose na cam platformama sa SplitCamom.",
           "h1": 'Besplatni vodiči za <span class="accent">cam streaming</span>',
           "sub": "Postavljanje korak po korak za prijenos na bilo kojoj cam platformi sa "
                  "besplatnim SplitCamom — vanjski enkoder, scene, preklapanja, bez vodenog žiga.",
           "pick": "Odaberi svoju platformu"},
    "zh": {"title": "直播指南 — 使用 SplitCam 进行 cam 平台直播",
           "desc": "使用 SplitCam 在任何 cam 平台直播的免费分步指南。",
           "h1": '免费 <span class="accent">cam 直播指南</span>',
           "sub": "使用免费 SplitCam 在任何 cam 平台直播的分步设置 — 外部编码器、场景、叠加层、无水印。",
           "pick": "选择您的平台"},
    "ja": {"title": "ストリーミングガイド — SplitCamでcam配信",
           "desc": "SplitCamを使用してcamプラットフォームで配信するための無料ステップバイステップガイド。",
           "h1": '無料の<span class="accent">camストリーミングガイド</span>',
           "sub": "無料SplitCamで任意のcamプラットフォームに配信するためのステップバイステップ設定 — "
                  "外部エンコーダー、シーン、オーバーレイ、透かしなし。",
           "pick": "プラットフォームを選択"},
    "ar": {"title": "أدلة البث — بث cam مع SplitCam",
           "desc": "أدلة مجانية خطوة بخطوة للبث على أي منصة cam مع SplitCam.",
           "h1": 'أدلة <span class="accent">بث cam</span> مجانية',
           "sub": "إعداد خطوة بخطوة للبث على أي منصة cam مع SplitCam المجاني — "
                  "مُشفِّر خارجي، مشاهد، تراكبات، بدون علامة مائية.",
           "pick": "اختر منصتك"},
    "th": {"title": "คู่มือสตรีมมิ่ง — การถ่ายทอด cam ด้วย SplitCam",
           "desc": "คู่มือฟรีทีละขั้นตอนสำหรับการถ่ายทอดบนแพลตฟอร์ม cam ใดๆ ด้วย SplitCam",
           "h1": 'คู่มือ<span class="accent">การสตรีม cam</span>ฟรี',
           "sub": "การตั้งค่าทีละขั้นตอนสำหรับการถ่ายทอดบนแพลตฟอร์ม cam ใดๆ ด้วย SplitCam ฟรี — "
                  "encoder ภายนอก, ฉาก, โอเวอร์เลย์, ไม่มีลายน้ำ",
           "pick": "เลือกแพลตฟอร์มของคุณ"},
    "fil": {"title": "Mga gabay sa streaming — cam broadcast sa SplitCam",
            "desc": "Libreng hakbang-hakbang na gabay para mag-broadcast sa anumang cam platform gamit ang SplitCam.",
            "h1": 'Libreng mga gabay sa <span class="accent">cam streaming</span>',
            "sub": "Hakbang-hakbang na setup para mag-broadcast sa anumang cam platform gamit ang libreng "
                   "SplitCam — external encoder, scenes, overlays, walang watermark.",
            "pick": "Piliin ang iyong platform"},
    "tr": {"title": "Yayın rehberleri — SplitCam ile cam yayınları",
           "desc": "SplitCam ile herhangi bir cam platformunda yayın yapmak için ücretsiz adım adım rehberler.",
           "h1": 'Ücretsiz <span class="accent">cam yayın rehberleri</span>',
           "sub": "Ücretsiz SplitCam ile herhangi bir cam platformunda yayın için adım adım kurulum — "
                  "harici kodlayıcı, sahneler, katmanlar, filigran yok.",
           "pick": "Platformunu seç"},
    "id": {"title": "Panduan streaming — siaran cam dengan SplitCam",
           "desc": "Panduan gratis langkah demi langkah untuk siaran di platform cam mana pun dengan SplitCam.",
           "h1": 'Panduan <span class="accent">cam streaming</span> gratis',
           "sub": "Setup langkah demi langkah untuk siaran di platform cam mana pun dengan SplitCam "
                  "gratis — encoder eksternal, scene, overlay, tanpa watermark.",
           "pick": "Pilih platform-mu"},
    "vi": {"title": "Hướng dẫn phát sóng — phát cam với SplitCam",
           "desc": "Hướng dẫn miễn phí từng bước để phát sóng trên mọi nền tảng cam với SplitCam.",
           "h1": 'Hướng dẫn <span class="accent">phát sóng cam</span> miễn phí',
           "sub": "Thiết lập từng bước để phát sóng trên mọi nền tảng cam với SplitCam miễn phí — "
                  "bộ mã hóa ngoài, cảnh, overlay, không watermark.",
           "pick": "Chọn nền tảng của bạn"},
    "pl": {"title": "Poradniki transmisji — nadawanie cam z SplitCam",
           "desc": "Darmowe poradniki krok po kroku do nadawania na dowolnej platformie cam z SplitCam.",
           "h1": 'Darmowe poradniki <span class="accent">transmisji cam</span>',
           "sub": "Konfiguracja krok po kroku do nadawania na dowolnej platformie cam z darmowym "
                  "SplitCam — enkoder zewnętrzny, sceny, nakładki, bez znaku wodnego.",
           "pick": "Wybierz swoją platformę"},
    "ko": {"title": "방송 가이드 — SplitCam으로 캠 방송하기",
           "desc": "SplitCam으로 어떤 캠 플랫폼에서든 방송하는 무료 단계별 가이드.",
           "h1": '무료 <span class="accent">캠 방송 가이드</span>',
           "sub": "무료 SplitCam으로 어떤 캠 플랫폼에서든 방송하는 단계별 설정 — "
                  "외부 인코더, 장면, 오버레이, 워터마크 없음.",
           "pick": "플랫폼을 고르세요"},
    "uk": {"title": "Посібники з трансляцій — кам-ефір зі SplitCam",
           "desc": "Безкоштовні покрокові посібники для трансляцій на будь-якій кам-платформі зі SplitCam.",
           "h1": 'Безкоштовні посібники з <span class="accent">кам-трансляцій</span>',
           "sub": "Покрокове налаштування для трансляцій на будь-якій кам-платформі з безкоштовним "
                  "SplitCam — зовнішній кодувальник, сцени, оверлеї, без водяного знака.",
           "pick": "Виберіть свою платформу"},
    "cs": {"title": "Návody na vysílání — cam vysílání se SplitCam",
           "desc": "Bezplatné návody krok za krokem pro vysílání na jakékoli cam platformě se SplitCam.",
           "h1": 'Bezplatné návody na <span class="accent">cam vysílání</span>',
           "sub": "Nastavení krok za krokem pro vysílání na jakékoli cam platformě se SplitCam "
                  "zdarma — externí kodér, scény, překryvy, bez vodoznaku.",
           "pick": "Vyberte svou platformu"},
    "sk": {"title": "Návody na vysielanie — cam vysielanie so SplitCam",
           "desc": "Bezplatné návody krok za krokom na vysielanie na akejkoľvek cam platforme so SplitCam.",
           "h1": 'Bezplatné návody na <span class="accent">cam vysielanie</span>',
           "sub": "Nastavenie krok za krokom na vysielanie na akejkoľvek cam platforme so SplitCam "
                  "zadarmo — externý kodér, scény, prekrytia, bez vodoznaku.",
           "pick": "Vyberte svoju platformu"},
    "sv": {"title": "Sändningsguider — cam-sändning med SplitCam",
           "desc": "Gratis steg-för-steg-guider för att sända på vilken cam-plattform som helst med SplitCam.",
           "h1": 'Gratis guider för <span class="accent">cam-sändning</span>',
           "sub": "Steg-för-steg-uppsättning för att sända på vilken cam-plattform som helst med gratis "
                  "SplitCam — extern kodare, scener, overlays, ingen vattenstämpel.",
           "pick": "Välj din plattform"},
    "ms": {"title": "Panduan siaran — siaran cam dengan SplitCam",
           "desc": "Panduan percuma langkah demi langkah untuk menyiar di mana-mana platform cam dengan SplitCam.",
           "h1": 'Panduan <span class="accent">siaran cam</span> percuma',
           "sub": "Persediaan langkah demi langkah untuk menyiar di mana-mana platform cam dengan SplitCam "
                  "percuma — pengekod luaran, adegan, tindihan, tiada tera air.",
           "pick": "Pilih platform anda"},
    "he": {"title": "מדריכי שידור — שידור קאם עם SplitCam",
           "desc": "מדריכים חינמיים שלב אחר שלב לשידור בכל פלטפורמת קאם עם SplitCam.",
           "h1": 'מדריכי <span class="accent">שידור קאם</span> חינמיים',
           "sub": "הגדרה שלב אחר שלב לשידור בכל פלטפורמת קאם עם SplitCam "
                  "החינמי — מקודד חיצוני, סצנות, שכבות, ללא סימן מים.",
           "pick": "בחרו את הפלטפורמה שלכם"},
    "fa": {"title": "راهنماهای پخش — پخش کم با SplitCam",
           "desc": "راهنماهای رایگان گام‌به‌گام برای پخش در هر پلتفرم کم با SplitCam.",
           "h1": 'راهنماهای <span class="accent">پخش کم</span> رایگان',
           "sub": "تنظیم گام‌به‌گام برای پخش در هر پلتفرم کم با SplitCam "
                  "رایگان — رمزگذار خارجی، صحنه‌ها، پوشش‌ها، بدون واترمارک.",
           "pick": "پلتفرم خود را انتخاب کنید"},
    "hi": {"title": "स्ट्रीमिंग गाइड — SplitCam के साथ कैम स्ट्रीमिंग",
           "desc": "किसी भी कैम प्लेटफ़ॉर्म पर SplitCam के साथ स्ट्रीम करने के लिए मुफ़्त चरण-दर-चरण गाइड।",
           "h1": 'मुफ़्त <span class="accent">कैम स्ट्रीमिंग गाइड</span>',
           "sub": "मुफ़्त SplitCam के साथ किसी भी कैम प्लेटफ़ॉर्म पर स्ट्रीम करने के लिए "
                  "चरण-दर-चरण सेटअप — एक्सटर्नल एन्कोडर, सीन, ओवरले, कोई वॉटरमार्क नहीं।",
           "pick": "अपना प्लेटफ़ॉर्म चुनें"},
}


LEGAL = {
    "about": {
        "en": ("About — Streaming Guides", "About this site", "About — Streaming Guides",
               "<p>Streaming Guides is a free, independent resource for setting up live broadcasts on adult cam platforms using <strong>SplitCam</strong> — free, no-watermark streaming software for Windows and macOS.</p>"
               "<p>We cover 19 platforms with step-by-step guides, troubleshooting tips and current technical details — from finding your stream key on each site to picking the right bitrate.</p>"
               "<p>This site is not affiliated with any of the platforms listed. Every brand name and logo belongs to its respective owner.</p>"),
        "ru": ("О проекте — Streaming Guides", "О проекте", "О сайте Streaming Guides",
               "<p>Streaming Guides — бесплатный независимый ресурс по настройке прямых трансляций на adult-кам платформах через <strong>SplitCam</strong>, бесплатную программу для стриминга на Windows и macOS, без водяного знака.</p>"
               "<p>Мы покрываем 19 платформ пошаговыми гайдами, советами по решению проблем и актуальными техническими деталями — от поиска ключа трансляции до выбора битрейта.</p>"
               "<p>Сайт не аффилирован ни с одной из перечисленных платформ. Все упомянутые торговые знаки и логотипы принадлежат их правообладателям.</p>"),
        "es": ("Acerca de — Streaming Guides", "Acerca de", "Acerca de Streaming Guides",
               "<p>Streaming Guides es un recurso gratuito e independiente para configurar emisiones en directo en plataformas cam para adultos usando <strong>SplitCam</strong> — software de streaming gratuito y sin marca de agua para Windows y macOS.</p>"
               "<p>Cubrimos 19 plataformas con guías paso a paso, consejos de resolución de problemas y detalles técnicos actuales — desde encontrar tu clave de stream hasta elegir el bitrate adecuado.</p>"
               "<p>Este sitio no está afiliado a ninguna de las plataformas listadas. Todos los nombres comerciales y logotipos pertenecen a sus respectivos propietarios.</p>"),
        "de": ("Über uns — Streaming Guides", "Über uns", "Über Streaming Guides",
               "<p>Streaming Guides ist eine kostenlose, unabhängige Ressource für die Einrichtung von Live-Übertragungen auf Erwachsenen-Cam-Plattformen mit <strong>SplitCam</strong> — kostenloser Streaming-Software ohne Wasserzeichen für Windows und macOS.</p>"
               "<p>Wir decken 19 Plattformen mit Schritt-für-Schritt-Anleitungen, Tipps zur Fehlerbehebung und aktuellen technischen Details ab — vom Finden deines Stream-Keys auf jeder Seite bis zur Wahl der richtigen Bitrate.</p>"
               "<p>Diese Seite steht in keiner Verbindung zu einer der gelisteten Plattformen. Alle Markennamen und Logos gehören den jeweiligen Eigentümern.</p>"),
        "fr": ("À propos — Streaming Guides", "À propos", "À propos de Streaming Guides",
               "<p>Streaming Guides est une ressource gratuite et indépendante pour configurer des diffusions en direct sur les plateformes cam pour adultes avec <strong>SplitCam</strong> — un logiciel de streaming gratuit, sans filigrane, pour Windows et macOS.</p>"
               "<p>Nous couvrons 19 plateformes avec des guides pas à pas, des astuces de dépannage et les détails techniques à jour — de la recherche de votre clé de stream sur chaque site au choix du bon débit.</p>"
               "<p>Ce site n'est affilié à aucune des plateformes mentionnées. Tous les noms commerciaux et logos appartiennent à leurs propriétaires respectifs.</p>"),
        "it": ("Chi siamo — Streaming Guides", "Chi siamo", "Chi siamo di Streaming Guides",
               "<p>Streaming Guides è una risorsa gratuita e indipendente per configurare trasmissioni in diretta su piattaforme cam per adulti usando <strong>SplitCam</strong> — software di streaming gratuito, senza filigrana, per Windows e macOS.</p>"
               "<p>Copriamo 19 piattaforme con guide passo dopo passo, consigli per risolvere i problemi e dettagli tecnici aggiornati — da dove trovare la tua stream key su ogni sito alla scelta del bitrate giusto.</p>"
               "<p>Questo sito non è affiliato a nessuna delle piattaforme elencate. Tutti i marchi e i loghi appartengono ai rispettivi proprietari.</p>"),
        "pt": ("Sobre — Streaming Guides", "Sobre", "Sobre o Streaming Guides",
               "<p>O Streaming Guides é um recurso gratuito e independente pra configurar transmissões ao vivo em plataformas cam adultas usando o <strong>SplitCam</strong> — software de streaming grátis, sem marca d'água, pra Windows e macOS.</p>"
               "<p>Cobrimos 19 plataformas com guias passo a passo, dicas pra resolver problemas e detalhes técnicos atualizados — de onde achar sua stream key em cada site até escolher o bitrate certo.</p>"
               "<p>Este site não é afiliado a nenhuma das plataformas listadas. Todas as marcas e logos pertencem aos seus respectivos donos.</p>"),
        "nl": ("Over — Streaming Guides", "Over", "Over Streaming Guides",
               "<p>Streaming Guides is een gratis, onafhankelijke bron voor het opzetten van live-uitzendingen op cam-platforms voor volwassenen met <strong>SplitCam</strong> — gratis streamingsoftware zonder watermerk voor Windows en macOS.</p>"
               "<p>We behandelen 19 platforms met stap-voor-stap gidsen, oplossingen voor veelvoorkomende problemen en actuele technische details — van het vinden van je stream key op elk platform tot het kiezen van de juiste bitrate.</p>"
               "<p>Deze site is niet gelieerd aan een van de genoemde platforms. Alle merknamen en logo's zijn eigendom van hun respectieve eigenaars.</p>"),
        "ro": ("Despre — Streaming Guides", "Despre", "Despre Streaming Guides",
               "<p>Streaming Guides este o resursă gratuită și independentă pentru configurarea transmisiunilor live pe platformele cam pentru adulți folosind <strong>SplitCam</strong> — software de streaming gratuit, fără filigran, pentru Windows și macOS.</p>"
               "<p>Acoperim 19 platforme cu ghiduri pas cu pas, sfaturi pentru rezolvarea problemelor și detalii tehnice actuale — de la găsirea cheii de stream pe fiecare site până la alegerea bitrate-ului potrivit.</p>"
               "<p>Acest site nu este afiliat cu niciuna dintre platformele enumerate. Toate numele de marcă și logourile aparțin proprietarilor respectivi.</p>"),
        "bg": ("За проекта — Streaming Guides", "За проекта", "За Streaming Guides",
               "<p>Streaming Guides е безплатен, независим ресурс за настройка на излъчвания на живо на кам платформи за възрастни чрез <strong>SplitCam</strong> — безплатен софтуер за стрийминг без воден знак за Windows и macOS.</p>"
               "<p>Покриваме 19 платформи с ръководства стъпка по стъпка, съвети за отстраняване на проблеми и актуални технически детайли — от това къде да намериш стрийм ключа на всеки сайт до избора на правилния битрейт.</p>"
               "<p>Този сайт не е свързан с никоя от изброените платформи. Всички марки и логота принадлежат на съответните им собственици.</p>"),
        "hu": ("Rólunk — Streaming Guides", "Rólunk", "A Streaming Guidesról",
               "<p>A Streaming Guides egy ingyenes, független erőforrás élő közvetítések beállításához felnőtt cam platformokon a <strong>SplitCam</strong> segítségével — ingyenes, vízjel nélküli streamelő szoftver Windowsra és macOS-re.</p>"
               "<p>19 platformot tárgyalunk lépésről lépésre útmutatókkal, hibaelhárítási tippekkel és aktuális technikai részletekkel — az egyes oldalak stream kulcsának megtalálásától a megfelelő bitráta kiválasztásáig.</p>"
               "<p>Ez az oldal nem áll kapcsolatban a felsorolt platformok egyikével sem. Minden márkanév és logó a megfelelő tulajdonosé.</p>"),
        "el": ("Σχετικά — Streaming Guides", "Σχετικά", "Σχετικά με το Streaming Guides",
               "<p>Το Streaming Guides είναι μια δωρεάν, ανεξάρτητη πηγή για την εγκατάσταση ζωντανών μεταδόσεων σε cam πλατφόρμες για ενήλικες με χρήση του <strong>SplitCam</strong> — δωρεάν λογισμικό streaming χωρίς υδατογράφημα για Windows και macOS.</p>"
               "<p>Καλύπτουμε 19 πλατφόρμες με οδηγούς βήμα προς βήμα, συμβουλές αντιμετώπισης προβλημάτων και επίκαιρες τεχνικές λεπτομέρειες — από την εύρεση του stream key σε κάθε site έως την επιλογή του σωστού bitrate.</p>"
               "<p>Αυτό το site δεν συνδέεται με καμία από τις πλατφόρμες που αναφέρονται. Όλα τα ονόματα μάρκας και τα λογότυπα ανήκουν στους αντίστοιχους κατόχους τους.</p>"),
        "fi": ("Tietoja — Streaming Guides", "Tietoja", "Tietoja Streaming Guidesista",
               "<p>Streaming Guides on ilmainen, riippumaton resurssi suorien lähetysten asentamiseen aikuisille suunnatuilla cam-alustoilla käyttäen <strong>SplitCamia</strong> — ilmainen, vesileimaton streaming-ohjelmisto Windowsille ja macOS:lle.</p>"
               "<p>Käsittelemme 19 alustaa vaihe vaiheelta -oppailla, vianmääritysvinkeillä ja ajantasaisilla teknisillä yksityiskohdilla — striimiavaimen löytämisestä jokaisella sivulla oikean bitraten valintaan.</p>"
               "<p>Tämä sivusto ei ole sidoksissa mihinkään luetelluista alustoista. Kaikki brändinimet ja logot kuuluvat omistajilleen.</p>"),
        "da": ("Om os — Streaming Guides", "Om os", "Om Streaming Guides",
               "<p>Streaming Guides er en gratis, uafhængig ressource til opsætning af live-udsendelser på voksen-cam-platforme med <strong>SplitCam</strong> — gratis streamingsoftware uden vandmærke til Windows og macOS.</p>"
               "<p>Vi dækker 19 platforme med trin-for-trin guides, fejlfindingstips og aktuelle tekniske detaljer — fra at finde din stream key på hver side til at vælge den rigtige bitrate.</p>"
               "<p>Denne side er ikke tilknyttet nogen af de listede platforme. Alle varemærker og logoer tilhører deres respektive ejere.</p>"),
        "no": ("Om oss — Streaming Guides", "Om oss", "Om Streaming Guides",
               "<p>Streaming Guides er en gratis, uavhengig ressurs for å sette opp direktesendinger på voksen-cam-plattformer med <strong>SplitCam</strong> — gratis strømmeprogramvare uten vannmerke for Windows og macOS.</p>"
               "<p>Vi dekker 19 plattformer med trinn-for-trinn guider, feilsøkingstips og oppdaterte tekniske detaljer — fra å finne strømnøkkelen på hvert nettsted til å velge riktig bitrate.</p>"
               "<p>Denne siden er ikke tilknyttet noen av de oppførte plattformene. Alle varemerker og logoer tilhører sine respektive eiere.</p>"),
        "sr": ("О сајту — Streaming Guides", "О сајту", "О Streaming Guides",
               "<p>Streaming Guides је бесплатан, независан ресурс за подешавање преноса уживо на кам платформама за одрасле користећи <strong>SplitCam</strong> — бесплатан софтвер за стриминг без воденог жига за Windows и macOS.</p>"
               "<p>Покривамо 19 платформи водичима корак по корак, саветима за решавање проблема и актуелним техничким детаљима — од проналажења стрим кључа на сваком сајту до избора правог битрејта.</p>"
               "<p>Овај сајт није повезан ни са једном од наведених платформи. Сви називи марки и логотипи припадају својим власницима.</p>"),
        "hr": ("O nama — Streaming Guides", "O nama", "O Streaming Guidesu",
               "<p>Streaming Guides je besplatan, neovisan resurs za postavljanje prijenosa uživo na cam platformama za odrasle koristeći <strong>SplitCam</strong> — besplatan softver za streaming bez vodenog žiga za Windows i macOS.</p>"
               "<p>Pokrivamo 19 platformi vodičima korak po korak, savjetima za rješavanje problema i aktualnim tehničkim detaljima — od pronalaska stream ključa na svakoj stranici do odabira ispravnog bitrate-a.</p>"
               "<p>Ova stranica nije povezana ni s jednom od navedenih platformi. Sva imena marki i logotipi pripadaju svojim vlasnicima.</p>"),
        "zh": ("关于 — Streaming Guides", "关于", "关于 Streaming Guides",
               "<p>Streaming Guides 是一个免费的独立资源，用于使用 <strong>SplitCam</strong> 设置成人 cam 平台的直播 — 适用于 Windows 和 macOS 的免费无水印直播软件。</p>"
               "<p>我们涵盖 19 个平台，提供分步指南、故障排除提示和当前技术细节 — 从在每个网站上找到您的直播密钥到选择正确的比特率。</p>"
               "<p>本网站与任何列出的平台均无关联。所有品牌名称和徽标均归各自所有者所有。</p>"),
        "ja": ("概要 — Streaming Guides", "概要", "Streaming Guides について",
               "<p>Streaming Guides は、<strong>SplitCam</strong>（Windows と macOS 用の無料・透かしなしのストリーミングソフトウェア）を使用して、成人向け cam プラットフォームでライブ配信を設定するための、無料の独立したリソースです。</p>"
               "<p>19のプラットフォームを、ステップバイステップガイド、トラブルシューティングのヒント、最新の技術的詳細でカバー — 各サイトでのストリームキーの見つけ方から、適切なビットレートの選択まで。</p>"
               "<p>このサイトは、リストされているプラットフォームのいずれとも提携していません。すべてのブランド名とロゴは、それぞれの所有者に帰属します。</p>"),
        "ar": ("حول — Streaming Guides", "حول", "حول Streaming Guides",
               "<p>Streaming Guides هو مصدر مجاني ومستقل لإعداد عمليات البث المباشر على منصات cam للبالغين باستخدام <strong>SplitCam</strong> — برنامج بث مجاني بدون علامة مائية لنظامي التشغيل Windows و macOS.</p>"
               "<p>نغطي 19 منصة بأدلة خطوة بخطوة، ونصائح لاستكشاف الأخطاء وإصلاحها، وتفاصيل تقنية حالية — من العثور على مفتاح البث الخاص بك على كل موقع إلى اختيار معدل البت الصحيح.</p>"
               "<p>هذا الموقع غير منتسب لأي من المنصات المدرجة. تنتمي جميع أسماء العلامات التجارية والشعارات إلى أصحابها المعنيين.</p>"),
        "th": ("เกี่ยวกับ — Streaming Guides", "เกี่ยวกับ", "เกี่ยวกับ Streaming Guides",
               "<p>Streaming Guides คือแหล่งข้อมูลฟรีและเป็นอิสระสำหรับการตั้งค่าการถ่ายทอดสดบนแพลตฟอร์ม cam ผู้ใหญ่โดยใช้ <strong>SplitCam</strong> — ซอฟต์แวร์สตรีมมิ่งฟรีไม่มีลายน้ำสำหรับ Windows และ macOS</p>"
               "<p>เราครอบคลุม 19 แพลตฟอร์มด้วยคู่มือทีละขั้นตอน เคล็ดลับการแก้ปัญหา และรายละเอียดทางเทคนิคที่เป็นปัจจุบัน — ตั้งแต่การหาสตรีมคีย์ของคุณบนแต่ละไซต์ไปจนถึงการเลือกบิตเรตที่เหมาะสม</p>"
               "<p>เว็บไซต์นี้ไม่มีส่วนเกี่ยวข้องกับแพลตฟอร์มใดๆ ที่ระบุไว้ ชื่อแบรนด์และโลโก้ทั้งหมดเป็นของเจ้าของที่เกี่ยวข้อง</p>"),
        "fil": ("Tungkol sa — Streaming Guides", "Tungkol sa", "Tungkol sa Streaming Guides",
                "<p>Ang Streaming Guides ay isang libreng, malayang pinagkukunan para sa pag-set up ng live broadcasts sa adult cam platforms gamit ang <strong>SplitCam</strong> — libreng, walang-watermark na streaming software para sa Windows at macOS.</p>"
                "<p>Sinasaklaw namin ang 19 platforms na may hakbang-hakbang na gabay, mga tip sa troubleshooting at kasalukuyang mga teknikal na detalye — mula sa paghahanap ng iyong stream key sa bawat site hanggang sa pagpili ng tamang bitrate.</p>"
                "<p>Ang site na ito ay hindi kaakibat sa anumang nakalistang platform. Ang lahat ng brand name at logo ay pag-aari ng kani-kanilang may-ari.</p>"),
        "tr": ("Hakkında — Streaming Guides", "Hakkında", "Streaming Guides Hakkında",
               "<p>Streaming Guides, yetişkin cam platformlarında <strong>SplitCam</strong> — Windows ve macOS için ücretsiz, filigransız yayın yazılımı — kullanarak canlı yayın kurmak için ücretsiz ve bağımsız bir kaynaktır.</p>"
               "<p>19 platformu adım adım rehberler, sorun giderme ipuçları ve güncel teknik detaylarla kapsıyoruz — her sitede yayın anahtarını bulmaktan doğru bitrate'i seçmeye kadar.</p>"
               "<p>Bu site, listelenen platformların hiçbiriyle bağlantılı değildir. Tüm marka adları ve logolar ilgili sahiplerine aittir.</p>"),
        "id": ("Tentang — Streaming Guides", "Tentang", "Tentang Streaming Guides",
               "<p>Streaming Guides adalah sumber gratis dan independen untuk menyiapkan siaran langsung di platform cam dewasa dengan <strong>SplitCam</strong> — software streaming gratis tanpa watermark untuk Windows dan macOS.</p>"
               "<p>Kami mencakup 19 platform dengan panduan langkah demi langkah, tips pemecahan masalah, dan detail teknis terkini — dari menemukan stream key-mu di tiap situs hingga memilih bitrate yang tepat.</p>"
               "<p>Situs ini tidak berafiliasi dengan platform mana pun yang tercantum. Semua nama merek dan logo adalah milik pemiliknya masing-masing.</p>"),
        "vi": ("Giới thiệu — Streaming Guides", "Giới thiệu", "Giới thiệu Streaming Guides",
               "<p>Streaming Guides là nguồn miễn phí, độc lập để thiết lập phát sóng trực tiếp trên các nền tảng cam người lớn với <strong>SplitCam</strong> — phần mềm phát sóng miễn phí không watermark cho Windows và macOS.</p>"
               "<p>Chúng tôi bao quát 19 nền tảng với hướng dẫn từng bước, mẹo khắc phục sự cố và chi tiết kỹ thuật cập nhật — từ tìm stream key ở mỗi site đến chọn bitrate phù hợp.</p>"
               "<p>Trang này không liên kết với bất kỳ nền tảng nào được liệt kê. Mọi tên thương hiệu và logo thuộc về chủ sở hữu tương ứng.</p>"),
        "pl": ("O nas — Streaming Guides", "O nas", "O Streaming Guides",
               "<p>Streaming Guides to darmowe, niezależne źródło wiedzy o konfiguracji transmisji na żywo na platformach cam dla dorosłych z <strong>SplitCam</strong> — darmowym oprogramowaniem do streamingu bez znaku wodnego dla Windows i macOS.</p>"
               "<p>Obejmujemy 19 platform poradnikami krok po kroku, wskazówkami rozwiązywania problemów i aktualnymi szczegółami technicznymi — od znalezienia klucza streamu w każdym serwisie po wybór odpowiedniego bitrate.</p>"
               "<p>Ta strona nie jest powiązana z żadną z wymienionych platform. Wszystkie nazwy marek i logo należą do ich właścicieli.</p>"),
        "ko": ("소개 — Streaming Guides", "소개", "Streaming Guides 소개",
               "<p>Streaming Guides는 <strong>SplitCam</strong> — Windows와 macOS용 무료, 워터마크 없는 방송 소프트웨어 — 으로 성인 캠 플랫폼에서 라이브 방송을 설정하기 위한 무료·독립 자료입니다.</p>"
               "<p>저희는 19개 플랫폼을 단계별 가이드, 문제 해결 팁, 최신 기술 세부사항으로 다룹니다 — 각 사이트에서 스트림 키 찾기부터 적절한 비트레이트 고르기까지.</p>"
               "<p>이 사이트는 나열된 어떤 플랫폼과도 제휴하지 않습니다. 모든 브랜드명과 로고는 각 소유자의 자산입니다.</p>"),
        "uk": ("Про нас — Streaming Guides", "Про нас", "Про Streaming Guides",
               "<p>Streaming Guides — безкоштовний незалежний ресурс про налаштування трансляцій наживо на дорослих кам-платформах зі <strong>SplitCam</strong> — безкоштовною програмою для стримінгу без водяного знака для Windows і macOS.</p>"
               "<p>Ми охоплюємо 19 платформ покроковими посібниками, порадами з усунення несправностей та актуальними технічними деталями — від пошуку ключа трансляції на кожному сайті до вибору правильного бітрейту.</p>"
               "<p>Цей сайт не пов'язаний із жодною з перелічених платформ. Усі назви брендів і логотипи належать їхнім власникам.</p>"),
        "cs": ("O nás — Streaming Guides", "O nás", "O Streaming Guides",
               "<p>Streaming Guides je bezplatný, nezávislý zdroj o nastavení živého vysílání na dospělých cam platformách se <strong>SplitCam</strong> — bezplatným streamovacím softwarem bez vodoznaku pro Windows a macOS.</p>"
               "<p>Pokrýváme 19 platforem návody krok za krokem, tipy na řešení problémů a aktuálními technickými detaily — od nalezení stream key na každé stránce po výběr správného bitrate.</p>"
               "<p>Tento web není spojen s žádnou z uvedených platforem. Všechny názvy značek a loga patří jejich vlastníkům.</p>"),
        "sk": ("O nás — Streaming Guides", "O nás", "O Streaming Guides",
               "<p>Streaming Guides je bezplatný, nezávislý zdroj o nastavení živého vysielania na dospelých cam platformách so <strong>SplitCam</strong> — bezplatným streamovacím softvérom bez vodoznaku pre Windows a macOS.</p>"
               "<p>Pokrývame 19 platforiem návodmi krok za krokom, tipmi na riešenie problémov a aktuálnymi technickými detailmi — od nájdenia stream key na každej stránke po výber správneho bitrate.</p>"
               "<p>Tento web nie je spojený so žiadnou z uvedených platforiem. Všetky názvy značiek a logá patria ich vlastníkom.</p>"),
        "sv": ("Om oss — Streaming Guides", "Om oss", "Om Streaming Guides",
               "<p>Streaming Guides är en gratis, oberoende resurs om hur du sätter upp livesändningar på cam-plattformar för vuxna med <strong>SplitCam</strong> — gratis sändningsmjukvara utan vattenstämpel för Windows och macOS.</p>"
               "<p>Vi täcker 19 plattformar med steg-för-steg-guider, felsökningstips och aktuella tekniska detaljer — från att hitta din streamnyckel på varje sajt till att välja rätt bitrate.</p>"
               "<p>Den här sajten är inte ansluten till någon av de listade plattformarna. Alla varumärkesnamn och logotyper tillhör sina respektive ägare.</p>"),
        "ms": ("Tentang — Streaming Guides", "Tentang", "Tentang Streaming Guides",
               "<p>Streaming Guides ialah sumber percuma dan bebas tentang cara menyediakan siaran langsung di platform cam dewasa dengan <strong>SplitCam</strong> — perisian penstriman percuma tanpa tera air untuk Windows dan macOS.</p>"
               "<p>Kami merangkumi 19 platform dengan panduan langkah demi langkah, petua penyelesaian masalah dan butiran teknikal terkini — daripada mencari kunci strim anda di setiap tapak hingga memilih bitrate yang betul.</p>"
               "<p>Tapak ini tidak bergabung dengan mana-mana platform yang disenaraikan. Semua nama jenama dan logo milik pemilik masing-masing.</p>"),
        "he": ("אודות — Streaming Guides", "אודות", "אודות Streaming Guides",
               "<p>Streaming Guides הוא מקור חינמי ועצמאי על הגדרת שידורים חיים בפלטפורמות קאם למבוגרים עם <strong>SplitCam</strong> — תוכנת שידור חינמית ללא סימן מים ל-Windows ו-macOS.</p>"
               "<p>אנחנו מכסים 19 פלטפורמות במדריכים שלב אחר שלב, טיפים לפתרון בעיות ופרטים טכניים עדכניים — ממציאת מפתח השידור בכל אתר ועד בחירת הביטרייט הנכון.</p>"
               "<p>אתר זה אינו מסונף לאף אחת מהפלטפורמות המופיעות. כל שמות המותגים והלוגואים שייכים לבעליהם.</p>"),
        "hi": ("हमारे बारे में — Streaming Guides", "हमारे बारे में", "Streaming Guides के बारे में",
               "<p>Streaming Guides, <strong>SplitCam</strong> — Windows और macOS के लिए मुफ़्त, वॉटरमार्क-रहित स्ट्रीमिंग सॉफ़्टवेयर — के साथ वयस्क कैम प्लेटफ़ॉर्म पर लाइव स्ट्रीम सेटअप करने का मुफ़्त, स्वतंत्र संसाधन है।</p>"
               "<p>हम 19 प्लेटफ़ॉर्म को चरण-दर-चरण गाइड, समस्या निवारण टिप्स और अद्यतन तकनीकी विवरण के साथ कवर करते हैं।</p>"
               "<p>यह साइट किसी भी सूचीबद्ध प्लेटफ़ॉर्म से संबद्ध नहीं है।</p>"),
        "fa": ("درباره — Streaming Guides", "درباره", "درباره Streaming Guides",
               "<p>Streaming Guides یک منبع رایگان و مستقل درباره تنظیم پخش زنده در پلتفرم‌های کم بزرگسالان با <strong>SplitCam</strong> — نرم‌افزار پخش رایگان بدون واترمارک برای Windows و macOS است.</p>"
               "<p>ما ۱۹ پلتفرم را با راهنماهای گام‌به‌گام، نکات عیب‌یابی و جزئیات فنی به‌روز پوشش می‌دهیم — از یافتن کلید جریان در هر سایت تا انتخاب بیت‌ریت مناسب.</p>"
               "<p>این سایت با هیچ‌یک از پلتفرم‌های فهرست‌شده وابستگی ندارد. تمام نام‌های تجاری و لوگوها متعلق به صاحبانشان هستند.</p>"),
    },
    "privacy": {
        "en": ("Privacy Policy — Streaming Guides", "Privacy Policy", "Privacy Policy",
               "<h2>What we collect</h2><p>Streaming Guides is a static website. We don't run cookies, accounts, forms or analytics that identify you personally. We don't run ads or affiliate trackers.</p>"
               "<h2>Third-party services</h2><p>Pages embed YouTube videos (via the privacy-enhanced youtube-nocookie.com domain) and load Google Fonts. These services may set their own cookies and log IP addresses according to their own privacy policies.</p>"
               "<h2>Server logs</h2><p>Standard web server logs may record your IP address and the page requested, retained for security purposes. We don't link these logs to any personal identity.</p>"
               "<h2>Your rights</h2><p>If you're in the EU/UK, you have rights under GDPR/UK GDPR. Since we hold no personal data tied to you, there's generally nothing to access, correct or delete. Contact us via the Contact page for any questions.</p>"
               "<h2>Changes</h2><p>This page may change. The latest version is always at this URL.</p>"),
        "ru": ("Конфиденциальность — Streaming Guides", "Конфиденциальность", "Политика конфиденциальности",
               "<h2>Что мы собираем</h2><p>Streaming Guides — статический сайт. Мы не используем cookies, не ведём аккаунты, не запускаем форм и не подключаем аналитику, которая идентифицирует пользователя лично. Рекламы и аффилиатных трекеров на сайте нет.</p>"
               "<h2>Сторонние сервисы</h2><p>На страницах встроены YouTube-видео (через домен повышенной приватности youtube-nocookie.com) и загружаются Google Fonts. Эти сервисы могут устанавливать собственные cookies и записывать IP-адреса согласно своим политикам конфиденциальности.</p>"
               "<h2>Логи сервера</h2><p>Стандартные веб-логи могут содержать IP-адрес и адрес запрошенной страницы; хранятся в целях безопасности. Мы не связываем эти логи с личностью пользователя.</p>"
               "<h2>Ваши права</h2><p>Если вы в ЕС/Великобритании, у вас есть права по GDPR/UK GDPR. Поскольку личных данных, связанных с вами, у нас нет, доступа, исправления или удаления, как правило, не требуется. Вопросы — через страницу «Контакты».</p>"
               "<h2>Изменения</h2><p>Содержимое страницы может меняться. Актуальная версия всегда по этому URL.</p>"),
        "es": ("Privacidad — Streaming Guides", "Privacidad", "Política de privacidad",
               "<h2>Qué recopilamos</h2><p>Streaming Guides es un sitio estático. No usamos cookies, cuentas, formularios ni analíticas que te identifiquen personalmente. No tenemos publicidad ni rastreadores de afiliados.</p>"
               "<h2>Servicios de terceros</h2><p>Las páginas incrustan vídeos de YouTube (a través del dominio de privacidad mejorada youtube-nocookie.com) y cargan Google Fonts. Estos servicios pueden establecer sus propias cookies y registrar direcciones IP según sus propias políticas de privacidad.</p>"
               "<h2>Registros del servidor</h2><p>Los registros estándar del servidor pueden contener tu dirección IP y la página solicitada, conservados con fines de seguridad. No vinculamos estos registros con ninguna identidad personal.</p>"
               "<h2>Tus derechos</h2><p>Si estás en la UE/Reino Unido, tienes derechos bajo el RGPD. Como no conservamos datos personales vinculados a ti, generalmente no hay nada que acceder, corregir o eliminar. Para cualquier consulta, contáctanos a través de la página Contacto.</p>"
               "<h2>Cambios</h2><p>Esta página puede cambiar. La versión más reciente está siempre en esta URL.</p>"),
        "de": ("Datenschutz — Streaming Guides", "Datenschutz", "Datenschutzerklärung",
               "<h2>Was wir erfassen</h2><p>Streaming Guides ist eine statische Website. Wir verwenden keine Cookies, Konten, Formulare oder Analytics, die dich persönlich identifizieren. Wir schalten keine Werbung und setzen keine Affiliate-Tracker ein.</p>"
               "<h2>Drittanbieter-Dienste</h2><p>Seiten betten YouTube-Videos ein (über die datenschutzfreundliche Domain youtube-nocookie.com) und laden Google Fonts. Diese Dienste können eigene Cookies setzen und IP-Adressen gemäß ihren eigenen Datenschutzrichtlinien protokollieren.</p>"
               "<h2>Server-Logs</h2><p>Standard-Webserver-Logs können deine IP-Adresse und die angeforderte Seite zu Sicherheitszwecken speichern. Wir verknüpfen diese Logs nicht mit einer persönlichen Identität.</p>"
               "<h2>Deine Rechte</h2><p>In der EU/Großbritannien hast du Rechte nach DSGVO/UK GDPR. Da wir keine personenbezogenen Daten zu dir speichern, gibt es in der Regel nichts zu beauskunften, korrigieren oder löschen. Bei Fragen erreichst du uns über die Kontaktseite.</p>"
               "<h2>Änderungen</h2><p>Diese Seite kann sich ändern. Die aktuelle Version steht immer unter dieser URL.</p>"),
        "fr": ("Confidentialité — Streaming Guides", "Confidentialité", "Politique de confidentialité",
               "<h2>Ce que nous collectons</h2><p>Streaming Guides est un site statique. Nous n'utilisons ni cookies, ni comptes, ni formulaires, ni outils d'analyse qui vous identifient personnellement. Nous ne diffusons pas de publicités et n'employons pas de trackers d'affiliation.</p>"
               "<h2>Services tiers</h2><p>Les pages intègrent des vidéos YouTube (via le domaine renforcé pour la confidentialité youtube-nocookie.com) et chargent Google Fonts. Ces services peuvent déposer leurs propres cookies et enregistrer des adresses IP selon leurs propres politiques de confidentialité.</p>"
               "<h2>Journaux serveur</h2><p>Les journaux standard du serveur peuvent enregistrer votre adresse IP et la page demandée, à des fins de sécurité. Nous ne lions pas ces journaux à une identité personnelle.</p>"
               "<h2>Vos droits</h2><p>Dans l'UE/au Royaume-Uni, vous bénéficiez de droits au titre du RGPD/UK GDPR. Comme nous ne conservons aucune donnée personnelle vous concernant, il n'y a généralement rien à consulter, corriger ou supprimer. Pour toute question, contactez-nous via la page Contact.</p>"
               "<h2>Modifications</h2><p>Cette page peut évoluer. La version la plus récente est toujours disponible à cette URL.</p>"),
        "it": ("Privacy — Streaming Guides", "Privacy", "Informativa sulla privacy",
               "<h2>Cosa raccogliamo</h2><p>Streaming Guides è un sito statico. Non usiamo cookie, account, moduli o strumenti di analisi che ti identifichino personalmente. Non pubblichiamo pubblicità né tracker di affiliazione.</p>"
               "<h2>Servizi di terze parti</h2><p>Le pagine incorporano video YouTube (tramite il dominio a privacy migliorata youtube-nocookie.com) e caricano Google Fonts. Questi servizi possono impostare cookie propri e registrare indirizzi IP secondo le loro politiche.</p>"
               "<h2>Log del server</h2><p>I log standard del server possono registrare il tuo indirizzo IP e la pagina richiesta, conservati a fini di sicurezza. Non colleghiamo questi log a un'identità personale.</p>"
               "<h2>I tuoi diritti</h2><p>Se sei nell'UE/Regno Unito, hai diritti ai sensi del GDPR/UK GDPR. Poiché non conserviamo dati personali collegati a te, in genere non c'è nulla da accedere, correggere o cancellare. Per qualsiasi domanda contattaci tramite la pagina Contatti.</p>"
               "<h2>Modifiche</h2><p>Questa pagina può cambiare. La versione più recente è sempre a questo URL.</p>"),
        "pt": ("Privacidade — Streaming Guides", "Privacidade", "Política de privacidade",
               "<h2>O que coletamos</h2><p>O Streaming Guides é um site estático. Não usamos cookies, contas, formulários nem analytics que te identifiquem pessoalmente. Não rodamos anúncios nem trackers de afiliados.</p>"
               "<h2>Serviços de terceiros</h2><p>As páginas embedam vídeos do YouTube (pelo domínio com privacidade melhorada youtube-nocookie.com) e carregam Google Fonts. Esses serviços podem definir cookies próprios e registrar endereços IP conforme as políticas deles.</p>"
               "<h2>Logs do servidor</h2><p>Logs padrão do servidor podem registrar seu IP e a página solicitada, mantidos por motivos de segurança. Não vinculamos esses logs a nenhuma identidade pessoal.</p>"
               "<h2>Seus direitos</h2><p>Se você está na UE/Reino Unido, tem direitos sob o GDPR/UK GDPR. Como não guardamos dados pessoais ligados a você, em geral não há nada a acessar, corrigir ou apagar. Para qualquer dúvida, fale conosco pela página Contato.</p>"
               "<h2>Alterações</h2><p>Esta página pode mudar. A versão mais recente está sempre nesta URL.</p>"),
        "nl": ("Privacy — Streaming Guides", "Privacy", "Privacybeleid",
               "<h2>Wat we verzamelen</h2><p>Streaming Guides is een statische website. We gebruiken geen cookies, accounts, formulieren of analytics die je persoonlijk identificeren. We tonen geen advertenties en gebruiken geen affiliate-trackers.</p>"
               "<h2>Externe diensten</h2><p>Pagina's embedden YouTube-video's (via het privacyvriendelijke domein youtube-nocookie.com) en laden Google Fonts. Deze diensten kunnen eigen cookies plaatsen en IP-adressen loggen volgens hun eigen privacybeleid.</p>"
               "<h2>Serverlogs</h2><p>Standaard serverlogs kunnen je IP-adres en de opgevraagde pagina registreren, bewaard om veiligheidsredenen. We koppelen deze logs niet aan een persoonlijke identiteit.</p>"
               "<h2>Jouw rechten</h2><p>Ben je in de EU/het VK, dan heb je rechten onder de AVG/UK GDPR. Omdat we geen persoonsgegevens van jou bewaren, valt er meestal niets in te zien, te corrigeren of te wissen. Voor vragen kun je ons bereiken via de Contact-pagina.</p>"
               "<h2>Wijzigingen</h2><p>Deze pagina kan veranderen. De meest recente versie staat altijd op deze URL.</p>"),
        "ro": ("Confidențialitate — Streaming Guides", "Confidențialitate", "Politică de confidențialitate",
               "<h2>Ce colectăm</h2><p>Streaming Guides este un site static. Nu folosim cookie-uri, conturi, formulare sau analytics care te identifică personal. Nu rulăm reclame sau trackere de afiliere.</p>"
               "<h2>Servicii terțe</h2><p>Paginile încorporează videoclipuri YouTube (prin domeniul cu confidențialitate îmbunătățită youtube-nocookie.com) și încarcă Google Fonts. Aceste servicii pot seta cookie-uri proprii și înregistra adrese IP conform politicilor lor de confidențialitate.</p>"
               "<h2>Loguri server</h2><p>Logurile standard ale serverului pot înregistra adresa ta IP și pagina solicitată, păstrate în scopuri de securitate. Nu legăm aceste loguri de nicio identitate personală.</p>"
               "<h2>Drepturile tale</h2><p>Dacă ești în UE/Marea Britanie, ai drepturi conform GDPR. Deoarece nu deținem date personale legate de tine, în general nu există nimic de accesat, corectat sau șters. Pentru întrebări, contactează-ne prin pagina Contact.</p>"
               "<h2>Modificări</h2><p>Această pagină se poate schimba. Cea mai recentă versiune este întotdeauna la acest URL.</p>"),
        "bg": ("Поверителност — Streaming Guides", "Поверителност", "Политика за поверителност",
               "<h2>Какво събираме</h2><p>Streaming Guides е статичен сайт. Не използваме бисквитки, акаунти, формуляри или аналитика, която те идентифицира лично. Не пускаме реклами или affiliate тракери.</p>"
               "<h2>Услуги от трети страни</h2><p>Страниците вграждат YouTube видеа (чрез домейна с подобрена поверителност youtube-nocookie.com) и зареждат Google Fonts. Тези услуги могат да задават собствени бисквитки и да записват IP адреси според собствените си политики за поверителност.</p>"
               "<h2>Сървърни логове</h2><p>Стандартните уеб логове може да записват твоя IP адрес и заявената страница, съхранявани с цел сигурност. Не свързваме тези логове с лична самоличност.</p>"
               "<h2>Твоите права</h2><p>Ако си в ЕС/Великобритания, имаш права по GDPR. Тъй като не съхраняваме лични данни, свързани с теб, обикновено няма какво да достъпиш, поправиш или изтриеш. За въпроси се свържи с нас чрез страницата Контакти.</p>"
               "<h2>Промени</h2><p>Тази страница може да се промени. Най-новата версия винаги е на този URL.</p>"),
        "hu": ("Adatvédelem — Streaming Guides", "Adatvédelem", "Adatvédelmi szabályzat",
               "<h2>Mit gyűjtünk</h2><p>A Streaming Guides statikus weboldal. Nem használunk sütiket, fiókokat, űrlapokat vagy téged személyesen azonosító analitikát. Nem futtatunk hirdetéseket vagy affiliate trackereket.</p>"
               "<h2>Harmadik féltől származó szolgáltatások</h2><p>Az oldalak YouTube-videókat ágyaznak be (a fokozott adatvédelmű youtube-nocookie.com domainen keresztül) és Google Fontsot töltenek be. Ezek a szolgáltatások saját sütiket állíthatnak be és IP-címeket naplózhatnak saját adatvédelmi szabályzatuk szerint.</p>"
               "<h2>Szerver naplók</h2><p>A szabványos webszerver naplók rögzíthetik az IP-címedet és a kért oldalt, biztonsági okokból megőrizve. Nem kapcsoljuk össze ezeket a naplókat semmilyen személyes azonosítóval.</p>"
               "<h2>Jogaid</h2><p>Ha az EU-ban/Egyesült Királyságban vagy, jogokat élvezel a GDPR alapján. Mivel nem tárolunk hozzád kötött személyes adatokat, általában nincs mit hozzáférned, javítanod vagy törölnöd. Kérdésekért keress minket a Kapcsolat oldalon.</p>"
               "<h2>Változások</h2><p>Ez az oldal változhat. A legújabb verzió mindig ezen a URL-en található.</p>"),
        "el": ("Απόρρητο — Streaming Guides", "Απόρρητο", "Πολιτική απορρήτου",
               "<h2>Τι συλλέγουμε</h2><p>Το Streaming Guides είναι ένα στατικό website. Δεν χρησιμοποιούμε cookies, λογαριασμούς, φόρμες ή analytics που σας ταυτοποιούν προσωπικά. Δεν τρέχουμε διαφημίσεις ή affiliate trackers.</p>"
               "<h2>Υπηρεσίες τρίτων</h2><p>Οι σελίδες ενσωματώνουν βίντεο YouTube (μέσω του domain ενισχυμένης ιδιωτικότητας youtube-nocookie.com) και φορτώνουν Google Fonts. Αυτές οι υπηρεσίες μπορεί να ορίζουν δικά τους cookies και να καταγράφουν διευθύνσεις IP σύμφωνα με τις δικές τους πολιτικές απορρήτου.</p>"
               "<h2>Logs διακομιστή</h2><p>Τα τυπικά logs διακομιστή μπορεί να καταγράφουν τη διεύθυνση IP σας και τη σελίδα που ζητήθηκε, για λόγους ασφαλείας. Δεν συνδέουμε αυτά τα logs με καμία προσωπική ταυτότητα.</p>"
               "<h2>Τα δικαιώματά σας</h2><p>Αν είστε στην ΕΕ/ΗΒ, έχετε δικαιώματα βάσει του GDPR. Καθώς δεν διατηρούμε προσωπικά δεδομένα συνδεδεμένα με εσάς, γενικά δεν υπάρχει τίποτα να αποκτήσετε πρόσβαση, να διορθώσετε ή να διαγράψετε. Για ερωτήσεις, επικοινωνήστε μαζί μας μέσω της σελίδας Επικοινωνία.</p>"
               "<h2>Αλλαγές</h2><p>Αυτή η σελίδα μπορεί να αλλάξει. Η τελευταία έκδοση είναι πάντα σε αυτό το URL.</p>"),
        "fi": ("Tietosuoja — Streaming Guides", "Tietosuoja", "Tietosuojakäytäntö",
               "<h2>Mitä keräämme</h2><p>Streaming Guides on staattinen sivusto. Emme käytä evästeitä, tilejä, lomakkeita tai sinut henkilökohtaisesti tunnistavaa analytiikkaa. Emme näytä mainoksia tai käytä affiliate-seurainta.</p>"
               "<h2>Kolmannen osapuolen palvelut</h2><p>Sivut upottavat YouTube-videoita (parannetun yksityisyyden youtube-nocookie.com-domainin kautta) ja lataavat Google Fontsia. Nämä palvelut voivat asettaa omia evästeitään ja kirjata IP-osoitteita omien tietosuojakäytäntöjensä mukaan.</p>"
               "<h2>Palvelimen lokit</h2><p>Vakio-verkkopalvelimen lokit voivat tallentaa IP-osoitteesi ja pyydetyn sivun, säilytettynä turvallisuussyistä. Emme yhdistä näitä lokeja mihinkään henkilökohtaiseen identiteettiin.</p>"
               "<h2>Oikeutesi</h2><p>Jos olet EU:ssa/Iso-Britanniassa, sinulla on oikeudet GDPR:n mukaisesti. Koska emme säilytä sinuun liittyviä henkilötietoja, yleensä mitään ei ole tarkasteltavaksi, korjattavaksi tai poistettavaksi. Yhteydenotot Yhteystiedot-sivun kautta.</p>"
               "<h2>Muutokset</h2><p>Tämä sivu voi muuttua. Uusin versio on aina tässä URL-osoitteessa.</p>"),
        "da": ("Privatliv — Streaming Guides", "Privatliv", "Privatlivspolitik",
               "<h2>Hvad vi indsamler</h2><p>Streaming Guides er en statisk hjemmeside. Vi bruger ikke cookies, konti, formularer eller analyser, der identificerer dig personligt. Vi viser ikke reklamer eller bruger affiliate-trackere.</p>"
               "<h2>Tredjepartstjenester</h2><p>Sider indlejrer YouTube-videoer (via det privatlivsforbedrede domæne youtube-nocookie.com) og indlæser Google Fonts. Disse tjenester kan sætte egne cookies og logge IP-adresser i henhold til deres egne privatlivspolitikker.</p>"
               "<h2>Serverlogs</h2><p>Standard webserverlogs kan registrere din IP-adresse og den anmodede side, opbevaret af sikkerhedshensyn. Vi forbinder ikke disse logs med nogen personlig identitet.</p>"
               "<h2>Dine rettigheder</h2><p>Hvis du er i EU/UK, har du rettigheder under GDPR. Da vi ikke opbevarer personlige data knyttet til dig, er der generelt intet at få adgang til, rette eller slette. Kontakt os via Kontakt-siden for spørgsmål.</p>"
               "<h2>Ændringer</h2><p>Denne side kan ændre sig. Den nyeste version er altid på denne URL.</p>"),
        "no": ("Personvern — Streaming Guides", "Personvern", "Personvernerklæring",
               "<h2>Hva vi samler inn</h2><p>Streaming Guides er en statisk nettside. Vi bruker ikke informasjonskapsler, kontoer, skjemaer eller analyser som identifiserer deg personlig. Vi viser ikke annonser og bruker ikke affiliate-sporere.</p>"
               "<h2>Tredjepartstjenester</h2><p>Sider bygger inn YouTube-videoer (via det personvernforbedrede domenet youtube-nocookie.com) og laster Google Fonts. Disse tjenestene kan sette egne informasjonskapsler og logge IP-adresser i henhold til sine egne personvernerklæringer.</p>"
               "<h2>Serverlogger</h2><p>Standard webserverlogger kan registrere IP-adressen din og den forespurte siden, oppbevart av sikkerhetsgrunner. Vi knytter ikke disse loggene til noen personlig identitet.</p>"
               "<h2>Dine rettigheter</h2><p>Hvis du er i EU/Storbritannia, har du rettigheter under GDPR. Siden vi ikke har personopplysninger knyttet til deg, er det generelt ingenting å få tilgang til, korrigere eller slette. Kontakt oss via Kontakt-siden for spørsmål.</p>"
               "<h2>Endringer</h2><p>Denne siden kan endres. Den nyeste versjonen er alltid på denne URL-en.</p>"),
        "sr": ("Приватност — Streaming Guides", "Приватност", "Политика приватности",
               "<h2>Шта прикупљамо</h2><p>Streaming Guides је статички сајт. Не користимо колачиће, налоге, формуларе или аналитику која те идентификује лично. Не приказујемо рекламе нити користимо affiliate трекере.</p>"
               "<h2>Услуге трећих страна</h2><p>Странице уграђују YouTube видео-снимке (преко домена са побољшаном приватношћу youtube-nocookie.com) и учитавају Google Fonts. Ове услуге могу постављати сопствене колачиће и бележити IP адресе у складу са сопственим политикама приватности.</p>"
               "<h2>Логови сервера</h2><p>Стандардни логови веб сервера могу бележити твоју IP адресу и тражену страницу, чувано из безбедносних разлога. Ове логове не повезујемо ни са једним личним идентитетом.</p>"
               "<h2>Твоја права</h2><p>Ако си у ЕУ/Великој Британији, имаш права по GDPR-у. Пошто не чувамо личне податке везане за тебе, обично нема ничега за приступ, исправљање или брисање. За питања нас контактирај преко странице Контакт.</p>"
               "<h2>Промене</h2><p>Ова страница се може мењати. Најновија верзија је увек на овом URL-у.</p>"),
        "hr": ("Privatnost — Streaming Guides", "Privatnost", "Politika privatnosti",
               "<h2>Što prikupljamo</h2><p>Streaming Guides je statična web stranica. Ne koristimo kolačiće, račune, obrasce ili analitiku koja te osobno identificira. Ne pokazujemo oglase i ne koristimo affiliate trackere.</p>"
               "<h2>Usluge trećih strana</h2><p>Stranice ugrađuju YouTube videozapise (preko domene s pojačanom privatnošću youtube-nocookie.com) i učitavaju Google Fonts. Ove usluge mogu postavljati vlastite kolačiće i bilježiti IP adrese sukladno svojim politikama privatnosti.</p>"
               "<h2>Zapisnici poslužitelja</h2><p>Standardni zapisnici web poslužitelja mogu bilježiti tvoju IP adresu i traženu stranicu, pohranjeno iz sigurnosnih razloga. Ove zapisnike ne povezujemo ni s jednim osobnim identitetom.</p>"
               "<h2>Tvoja prava</h2><p>Ako si u EU/Velikoj Britaniji, imaš prava prema GDPR-u. Budući da ne čuvamo osobne podatke vezane uz tebe, općenito nema ničega za pristup, ispravak ili brisanje. Za pitanja nas kontaktiraj preko stranice Kontakt.</p>"
               "<h2>Promjene</h2><p>Ova stranica se može promijeniti. Najnovija verzija je uvijek na ovom URL-u.</p>"),
        "zh": ("隐私 — Streaming Guides", "隐私", "隐私政策",
               "<h2>我们收集什么</h2><p>Streaming Guides 是一个静态网站。我们不使用 cookie、账户、表单或可识别您个人身份的分析。我们不投放广告或附属跟踪器。</p>"
               "<h2>第三方服务</h2><p>页面嵌入 YouTube 视频（通过隐私增强的 youtube-nocookie.com 域名）并加载 Google Fonts。这些服务可能根据其自己的隐私政策设置自己的 cookie 并记录 IP 地址。</p>"
               "<h2>服务器日志</h2><p>标准网络服务器日志可能会出于安全目的记录您的 IP 地址和请求的页面。我们不会将这些日志与任何个人身份关联。</p>"
               "<h2>您的权利</h2><p>如果您在欧盟/英国，您享有 GDPR 下的权利。由于我们不保留与您相关的个人数据，通常无需访问、更正或删除任何内容。如有问题，请通过联系页面与我们联系。</p>"
               "<h2>变更</h2><p>此页面可能会更改。最新版本始终在此 URL 上。</p>"),
        "ja": ("プライバシー — Streaming Guides", "プライバシー", "プライバシーポリシー",
               "<h2>収集する情報</h2><p>Streaming Guides は静的なウェブサイトです。Cookie、アカウント、フォーム、または個人を識別する分析を使用していません。広告やアフィリエイトトラッカーも実行していません。</p>"
               "<h2>第三者サービス</h2><p>ページは（プライバシー強化された youtube-nocookie.com ドメインを介して）YouTube ビデオを埋め込み、Google Fonts を読み込みます。これらのサービスは、それぞれのプライバシーポリシーに従って独自の Cookie を設定し、IP アドレスをログに記録する場合があります。</p>"
               "<h2>サーバーログ</h2><p>標準的なウェブサーバーログは、セキュリティ目的のためにあなたの IP アドレスと要求されたページを記録する場合があります。これらのログを個人の身元と結び付けることはありません。</p>"
               "<h2>あなたの権利</h2><p>EU/英国にお住まいの場合、GDPR の下での権利があります。あなたに関連する個人データを保持していないため、通常、アクセス、修正、削除するものはありません。ご質問はお問い合わせページから。</p>"
               "<h2>変更</h2><p>このページは変更される可能性があります。最新バージョンは常にこの URL にあります。</p>"),
        "ar": ("الخصوصية — Streaming Guides", "الخصوصية", "سياسة الخصوصية",
               "<h2>ما نجمعه</h2><p>Streaming Guides هو موقع ويب ثابت. لا نستخدم ملفات تعريف الارتباط أو الحسابات أو النماذج أو التحليلات التي تعرفك شخصيًا. لا نقوم بتشغيل إعلانات أو متعقبات تابعة.</p>"
               "<h2>خدمات الطرف الثالث</h2><p>تضمن الصفحات مقاطع فيديو YouTube (عبر نطاق youtube-nocookie.com المعزز للخصوصية) وتحمل Google Fonts. قد تضبط هذه الخدمات ملفات تعريف الارتباط الخاصة بها وتسجل عناوين IP وفقًا لسياسات الخصوصية الخاصة بها.</p>"
               "<h2>سجلات الخادم</h2><p>قد تسجل سجلات خادم الويب القياسية عنوان IP الخاص بك والصفحة المطلوبة، يتم الاحتفاظ بها لأغراض أمنية. لا نربط هذه السجلات بأي هوية شخصية.</p>"
               "<h2>حقوقك</h2><p>إذا كنت في الاتحاد الأوروبي/المملكة المتحدة، فلديك حقوق بموجب GDPR. نظرًا لأننا لا نحتفظ ببيانات شخصية مرتبطة بك، فعمومًا لا يوجد شيء للوصول إليه أو تصحيحه أو حذفه. اتصل بنا عبر صفحة الاتصال لأي أسئلة.</p>"
               "<h2>التغييرات</h2><p>قد تتغير هذه الصفحة. أحدث إصدار موجود دائمًا في هذا الرابط.</p>"),
        "th": ("ความเป็นส่วนตัว — Streaming Guides", "ความเป็นส่วนตัว", "นโยบายความเป็นส่วนตัว",
               "<h2>เราเก็บอะไรบ้าง</h2><p>Streaming Guides เป็นเว็บไซต์แบบสแตติก เราไม่ใช้คุกกี้ บัญชี แบบฟอร์ม หรือการวิเคราะห์ที่ระบุตัวคุณเป็นการส่วนตัว เราไม่แสดงโฆษณาหรือใช้ตัวติดตาม affiliate</p>"
               "<h2>บริการของบุคคลที่สาม</h2><p>หน้าเพจฝังวิดีโอ YouTube (ผ่านโดเมนความเป็นส่วนตัวเพิ่ม youtube-nocookie.com) และโหลด Google Fonts บริการเหล่านี้อาจตั้งคุกกี้ของตัวเองและบันทึกที่อยู่ IP ตามนโยบายความเป็นส่วนตัวของตัวเอง</p>"
               "<h2>บันทึกเซิร์ฟเวอร์</h2><p>บันทึกเว็บเซิร์ฟเวอร์มาตรฐานอาจบันทึกที่อยู่ IP และหน้าที่ขอเพื่อวัตถุประสงค์ด้านความปลอดภัย เราไม่เชื่อมโยงบันทึกเหล่านี้กับตัวตนส่วนบุคคลใดๆ</p>"
               "<h2>สิทธิ์ของคุณ</h2><p>หากคุณอยู่ใน EU/UK คุณมีสิทธิ์ภายใต้ GDPR เนื่องจากเราไม่เก็บข้อมูลส่วนตัวที่เชื่อมโยงกับคุณ โดยทั่วไปจึงไม่มีอะไรให้เข้าถึง แก้ไข หรือลบ ติดต่อเราผ่านหน้าติดต่อสำหรับคำถาม</p>"
               "<h2>การเปลี่ยนแปลง</h2><p>หน้านี้อาจมีการเปลี่ยนแปลง เวอร์ชันล่าสุดอยู่ที่ URL นี้เสมอ</p>"),
        "fil": ("Privacy — Streaming Guides", "Privacy", "Patakaran sa privacy",
                "<h2>Ano ang kinokolekta namin</h2><p>Ang Streaming Guides ay isang static na website. Hindi kami gumagamit ng cookies, accounts, forms, o analytics na nagpapakilala sa iyo nang personal. Hindi kami nagpapatakbo ng mga ad o affiliate tracker.</p>"
                "<h2>Mga serbisyo ng third-party</h2><p>Ang mga pahina ay nag-eembed ng mga YouTube video (sa pamamagitan ng privacy-enhanced youtube-nocookie.com domain) at nag-load ng Google Fonts. Maaaring magtakda ang mga serbisyong ito ng kanilang sariling cookies at mag-log ng IP addresses ayon sa kanilang sariling mga patakaran sa privacy.</p>"
                "<h2>Mga server log</h2><p>Maaaring i-record ng mga standard web server log ang iyong IP address at ang hiniling na pahina, pinananatili para sa mga layuning pang-seguridad. Hindi namin ini-link ang mga log na ito sa anumang personal na pagkakakilanlan.</p>"
                "<h2>Ang iyong mga karapatan</h2><p>Kung ikaw ay nasa EU/UK, may mga karapatan ka sa ilalim ng GDPR. Dahil hindi kami humahawak ng personal na data na nakatali sa iyo, sa pangkalahatan ay walang ma-access, itama, o tanggalin. Makipag-ugnayan sa amin sa pamamagitan ng pahina ng Kontak para sa anumang mga tanong.</p>"
                "<h2>Mga pagbabago</h2><p>Ang pahinang ito ay maaaring magbago. Ang pinakabagong bersyon ay palaging nasa URL na ito.</p>"),
        "tr": ("Gizlilik — Streaming Guides", "Gizlilik", "Gizlilik Politikası",
               "<h2>Ne topluyoruz</h2><p>Streaming Guides statik bir web sitesidir. Seni kişisel olarak tanımlayan çerez, hesap, form veya analiz kullanmıyoruz. Reklam veya ortaklık izleyicisi çalıştırmıyoruz.</p>"
               "<h2>Üçüncü taraf hizmetleri</h2><p>Sayfalar YouTube videoları gömer (gizliliği artırılmış youtube-nocookie.com alan adı üzerinden) ve Google Fonts yükler. Bu hizmetler kendi gizlilik politikalarına göre kendi çerezlerini ayarlayabilir ve IP adreslerini kaydedebilir.</p>"
               "<h2>Sunucu günlükleri</h2><p>Standart web sunucusu günlükleri güvenlik amacıyla IP adresini ve istenen sayfayı kaydedebilir. Bu günlükleri herhangi bir kişisel kimlikle ilişkilendirmiyoruz.</p>"
               "<h2>Haklarınız</h2><p>AB/Birleşik Krallık'taysan GDPR kapsamında haklara sahipsin. Sana bağlı kişisel veri tutmadığımız için genellikle erişilecek, düzeltilecek veya silinecek bir şey yoktur. Sorular için İletişim sayfasından bize ulaş.</p>"
               "<h2>Değişiklikler</h2><p>Bu sayfa değişebilir. En güncel sürüm her zaman bu URL'dedir.</p>"),
        "id": ("Privasi — Streaming Guides", "Privasi", "Kebijakan Privasi",
               "<h2>Apa yang kami kumpulkan</h2><p>Streaming Guides adalah situs web statis. Kami tidak memakai cookie, akun, formulir, atau analitik yang mengidentifikasimu secara pribadi. Kami tidak menjalankan iklan atau pelacak afiliasi.</p>"
               "<h2>Layanan pihak ketiga</h2><p>Halaman menyematkan video YouTube (lewat domain youtube-nocookie.com yang menjaga privasi) dan memuat Google Fonts. Layanan ini dapat menetapkan cookie sendiri dan mencatat alamat IP sesuai kebijakan privasi mereka.</p>"
               "<h2>Log server</h2><p>Log server web standar dapat mencatat alamat IP dan halaman yang diminta, disimpan untuk tujuan keamanan. Kami tidak mengaitkan log ini dengan identitas pribadi apa pun.</p>"
               "<h2>Hak Anda</h2><p>Jika kamu di UE/Inggris, kamu punya hak berdasarkan GDPR. Karena kami tidak menyimpan data pribadi yang terkait denganmu, umumnya tidak ada yang perlu diakses, dikoreksi, atau dihapus. Hubungi kami lewat halaman Kontak untuk pertanyaan apa pun.</p>"
               "<h2>Perubahan</h2><p>Halaman ini dapat berubah. Versi terbaru selalu ada di URL ini.</p>"),
        "vi": ("Quyền riêng tư — Streaming Guides", "Quyền riêng tư", "Chính sách quyền riêng tư",
               "<h2>Chúng tôi thu thập gì</h2><p>Streaming Guides là website tĩnh. Chúng tôi không dùng cookie, tài khoản, biểu mẫu hay phân tích nhận dạng bạn cá nhân. Chúng tôi không chạy quảng cáo hay trình theo dõi liên kết.</p>"
               "<h2>Dịch vụ bên thứ ba</h2><p>Các trang nhúng video YouTube (qua tên miền youtube-nocookie.com tăng cường quyền riêng tư) và tải Google Fonts. Các dịch vụ này có thể đặt cookie riêng và ghi địa chỉ IP theo chính sách riêng của họ.</p>"
               "<h2>Nhật ký máy chủ</h2><p>Nhật ký máy chủ web tiêu chuẩn có thể ghi địa chỉ IP và trang được yêu cầu, lưu vì mục đích an ninh. Chúng tôi không liên kết các nhật ký này với bất kỳ danh tính cá nhân nào.</p>"
               "<h2>Quyền của bạn</h2><p>Nếu bạn ở EU/Anh, bạn có các quyền theo GDPR. Vì chúng tôi không lưu dữ liệu cá nhân gắn với bạn, thường không có gì để truy cập, sửa hay xóa. Liên hệ chúng tôi qua trang Liên hệ cho mọi thắc mắc.</p>"
               "<h2>Thay đổi</h2><p>Trang này có thể thay đổi. Phiên bản mới nhất luôn ở URL này.</p>"),
        "pl": ("Prywatność — Streaming Guides", "Prywatność", "Polityka prywatności",
               "<h2>Co zbieramy</h2><p>Streaming Guides to statyczna strona internetowa. Nie używamy plików cookie, kont, formularzy ani analityki, która identyfikuje cię osobiście. Nie prowadzimy reklam ani trackerów afiliacyjnych.</p>"
               "<h2>Usługi zewnętrzne</h2><p>Strony osadzają filmy YouTube (przez domenę youtube-nocookie.com zwiększającą prywatność) i ładują Google Fonts. Usługi te mogą ustawiać własne pliki cookie i rejestrować adresy IP zgodnie z własnymi politykami prywatności.</p>"
               "<h2>Logi serwera</h2><p>Standardowe logi serwera mogą rejestrować adres IP i żądaną stronę, przechowywane w celach bezpieczeństwa. Nie łączymy tych logów z żadną osobistą tożsamością.</p>"
               "<h2>Twoje prawa</h2><p>Jeśli jesteś w UE/Wielkiej Brytanii, masz prawa wynikające z RODO. Ponieważ nie przechowujemy danych osobowych powiązanych z tobą, zwykle nie ma czego udostępniać, poprawiać ani usuwać. Skontaktuj się z nami przez stronę Kontakt w razie pytań.</p>"
               "<h2>Zmiany</h2><p>Ta strona może się zmieniać. Najnowsza wersja jest zawsze pod tym adresem URL.</p>"),
        "ko": ("개인정보 — Streaming Guides", "개인정보", "개인정보 처리방침",
               "<h2>수집하는 정보</h2><p>Streaming Guides는 정적 웹사이트입니다. 당신을 개인적으로 식별하는 쿠키, 계정, 양식, 분석을 사용하지 않습니다. 광고나 제휴 추적기를 운영하지 않습니다.</p>"
               "<h2>제3자 서비스</h2><p>페이지는 YouTube 영상을 임베드하고(개인정보 강화 youtube-nocookie.com 도메인 경유) Google Fonts를 로드합니다. 이 서비스들은 각자의 개인정보 방침에 따라 자체 쿠키를 설정하고 IP 주소를 기록할 수 있습니다.</p>"
               "<h2>서버 로그</h2><p>표준 웹 서버 로그는 보안 목적으로 IP 주소와 요청된 페이지를 기록할 수 있습니다. 저희는 이 로그를 어떤 개인 신원과도 연결하지 않습니다.</p>"
               "<h2>귀하의 권리</h2><p>EU/영국에 거주한다면 GDPR에 따른 권리가 있습니다. 저희는 당신과 연결된 개인정보를 보유하지 않으므로 일반적으로 접근·정정·삭제할 것이 없습니다. 문의는 문의 페이지로 연락하세요.</p>"
               "<h2>변경</h2><p>이 페이지는 변경될 수 있습니다. 최신 버전은 항상 이 URL에 있습니다.</p>"),
        "uk": ("Приватність — Streaming Guides", "Приватність", "Політика приватності",
               "<h2>Що ми збираємо</h2><p>Streaming Guides — статичний вебсайт. Ми не використовуємо файли cookie, акаунти, форми чи аналітику, що ідентифікує вас особисто. Ми не показуємо рекламу й не використовуємо афілійовані трекери.</p>"
               "<h2>Сторонні сервіси</h2><p>Сторінки вбудовують відео YouTube (через домен youtube-nocookie.com, що посилює приватність) і завантажують Google Fonts. Ці сервіси можуть встановлювати власні cookie й записувати IP-адреси згідно з власними політиками приватності.</p>"
               "<h2>Логи сервера</h2><p>Стандартні логи вебсервера можуть записувати IP-адресу й запитану сторінку, що зберігаються з міркувань безпеки. Ми не пов'язуємо ці логи з жодною особистою ідентичністю.</p>"
               "<h2>Ваші права</h2><p>Якщо ви в ЄС/Великій Британії, ви маєте права за GDPR. Оскільки ми не зберігаємо персональних даних, пов'язаних з вами, зазвичай немає чого надавати, виправляти чи видаляти. Звертайтеся через сторінку Контакти з будь-якими питаннями.</p>"
               "<h2>Зміни</h2><p>Ця сторінка може змінюватися. Найновіша версія завжди за цим URL.</p>"),
        "cs": ("Soukromí — Streaming Guides", "Soukromí", "Zásady ochrany soukromí",
               "<h2>Co shromažďujeme</h2><p>Streaming Guides je statický web. Nepoužíváme cookies, účty, formuláře ani analytiku, která vás osobně identifikuje. Neprovozujeme reklamy ani affiliate trackery.</p>"
               "<h2>Služby třetích stran</h2><p>Stránky vkládají videa YouTube (přes doménu youtube-nocookie.com posilující soukromí) a načítají Google Fonts. Tyto služby mohou nastavovat vlastní cookies a zaznamenávat IP adresy podle svých vlastních zásad ochrany soukromí.</p>"
               "<h2>Logy serveru</h2><p>Standardní logy webového serveru mohou zaznamenávat IP adresu a požadovanou stránku, uchovávané z bezpečnostních důvodů. Tyto logy nespojujeme s žádnou osobní identitou.</p>"
               "<h2>Vaše práva</h2><p>Pokud jste v EU/UK, máte práva podle GDPR. Protože neuchováváme osobní údaje spojené s vámi, obvykle není co zpřístupnit, opravit nebo smazat. S jakýmikoli dotazy nás kontaktujte přes stránku Kontakt.</p>"
               "<h2>Změny</h2><p>Tato stránka se může měnit. Nejnovější verze je vždy na této URL.</p>"),
        "sk": ("Súkromie — Streaming Guides", "Súkromie", "Zásady ochrany súkromia",
               "<h2>Čo zhromažďujeme</h2><p>Streaming Guides je statický web. Nepoužívame cookies, účty, formuláre ani analytiku, ktorá vás osobne identifikuje. Neprevádzkujeme reklamy ani affiliate trackery.</p>"
               "<h2>Služby tretích strán</h2><p>Stránky vkladajú videá YouTube (cez doménu youtube-nocookie.com posilňujúcu súkromie) a načítavajú Google Fonts. Tieto služby môžu nastavovať vlastné cookies a zaznamenávať IP adresy podľa svojich vlastných zásad ochrany súkromia.</p>"
               "<h2>Logy servera</h2><p>Štandardné logy webového servera môžu zaznamenávať IP adresu a požadovanú stránku, uchovávané z bezpečnostných dôvodov. Tieto logy nespájame so žiadnou osobnou identitou.</p>"
               "<h2>Vaše práva</h2><p>Ak ste v EÚ/UK, máte práva podľa GDPR. Keďže neuchovávame osobné údaje spojené s vami, zvyčajne nie je čo sprístupniť, opraviť alebo zmazať. S akýmikoľvek otázkami nás kontaktujte cez stránku Kontakt.</p>"
               "<h2>Zmeny</h2><p>Táto stránka sa môže meniť. Najnovšia verzia je vždy na tejto URL.</p>"),
        "sv": ("Integritet — Streaming Guides", "Integritet", "Integritetspolicy",
               "<h2>Vad vi samlar in</h2><p>Streaming Guides är en statisk webbplats. Vi använder inga cookies, konton, formulär eller analys som identifierar dig personligen. Vi kör inga annonser eller affiliate-spårare.</p>"
               "<h2>Tredjepartstjänster</h2><p>Sidorna bäddar in YouTube-videor (via den integritetsstärkta domänen youtube-nocookie.com) och laddar Google Fonts. Dessa tjänster kan sätta egna cookies och logga IP-adresser enligt sina egna integritetspolicyer.</p>"
               "<h2>Serverloggar</h2><p>Vanliga webbserverloggar kan registrera din IP-adress och den begärda sidan, sparade i säkerhetssyfte. Vi kopplar inte dessa loggar till någon personlig identitet.</p>"
               "<h2>Dina rättigheter</h2><p>Om du är i EU/Storbritannien har du rättigheter enligt GDPR. Eftersom vi inte lagrar personuppgifter kopplade till dig finns det vanligtvis inget att få tillgång till, rätta eller radera. Kontakta oss via Kontakt-sidan med eventuella frågor.</p>"
               "<h2>Ändringar</h2><p>Den här sidan kan ändras. Den senaste versionen finns alltid på denna URL.</p>"),
        "ms": ("Privasi — Streaming Guides", "Privasi", "Dasar Privasi",
               "<h2>Apa yang kami kumpul</h2><p>Streaming Guides ialah laman web statik. Kami tidak menggunakan kuki, akaun, borang atau analitik yang mengenal pasti anda secara peribadi. Kami tidak menjalankan iklan atau penjejak gabungan.</p>"
               "<h2>Perkhidmatan pihak ketiga</h2><p>Halaman membenamkan video YouTube (melalui domain youtube-nocookie.com yang memperkukuh privasi) dan memuatkan Google Fonts. Perkhidmatan ini boleh menetapkan kuki sendiri dan merekod alamat IP mengikut dasar privasi mereka sendiri.</p>"
               "<h2>Log pelayan</h2><p>Log pelayan web standard mungkin merekod alamat IP dan halaman yang diminta, disimpan untuk tujuan keselamatan. Kami tidak mengaitkan log ini dengan sebarang identiti peribadi.</p>"
               "<h2>Hak anda</h2><p>Jika anda di EU/UK, anda mempunyai hak di bawah GDPR. Kerana kami tidak menyimpan data peribadi yang dikaitkan dengan anda, biasanya tiada apa-apa untuk diakses, dibetulkan atau dipadam. Hubungi kami melalui halaman Hubungi untuk sebarang pertanyaan.</p>"
               "<h2>Perubahan</h2><p>Halaman ini boleh berubah. Versi terkini sentiasa di URL ini.</p>"),
        "he": ("פרטיות — Streaming Guides", "פרטיות", "מדיניות פרטיות",
               "<h2>מה אנחנו אוספים</h2><p>Streaming Guides הוא אתר סטטי. איננו משתמשים בעוגיות, חשבונות, טפסים או אנליטיקה שמזהים אתכם אישית. איננו מפעילים פרסומות או עוקבי שותפים.</p>"
               "<h2>שירותי צד שלישי</h2><p>הדפים מטמיעים סרטוני YouTube (דרך הדומיין youtube-nocookie.com משפר הפרטיות) וטוענים Google Fonts. שירותים אלה עשויים להגדיר עוגיות משלהם ולתעד כתובות IP לפי מדיניות הפרטיות שלהם.</p>"
               "<h2>יומני שרת</h2><p>יומני שרת אינטרנט סטנדרטיים עשויים לתעד את כתובת ה-IP ואת הדף המבוקש, נשמרים למטרות אבטחה. איננו מקשרים יומנים אלה לשום זהות אישית.</p>"
               "<h2>הזכויות שלכם</h2><p>אם אתם באיחוד האירופי/בריטניה, יש לכם זכויות לפי GDPR. מכיוון שאיננו שומרים נתונים אישיים הקשורים אליכם, בדרך כלל אין מה לגשת אליו, לתקן או למחוק. צרו קשר דרך עמוד צור קשר לכל שאלה.</p>"
               "<h2>שינויים</h2><p>דף זה עשוי להשתנות. הגרסה העדכנית ביותר תמיד בכתובת זו.</p>"),
        "hi": ("गोपनीयता — Streaming Guides", "गोपनीयता", "गोपनीयता नीति",
               "<h2>हम क्या एकत्र करते हैं</h2><p>Streaming Guides एक स्टैटिक वेबसाइट है। हम कोई कुकी, अकाउंट, फ़ॉर्म या एनालिटिक्स उपयोग नहीं करते जो आपको व्यक्तिगत रूप से पहचाने। हम विज्ञापन या एफ़िलिएट ट्रैकर नहीं चलाते।</p>"
               "<h2>तृतीय-पक्ष सेवाएं</h2><p>पेज YouTube वीडियो एम्बेड करते हैं और Google Fonts लोड करते हैं।</p>"
               "<h2>सर्वर लॉग</h2><p>मानक वेब सर्वर लॉग IP पता रिकॉर्ड कर सकते हैं।</p>"
               "<h2>आपके अधिकार</h2><p>EU/UK में हैं तो GDPR के तहत अधिकार हैं। संपर्क पेज पर प्रश्नों के लिए संपर्क करें।</p>"
               "<h2>परिवर्तन</h2><p>यह पेज बदल सकता है। नवीनतम संस्करण हमेशा इस URL पर है।</p>"),
        "fa": ("حریم خصوصی — Streaming Guides", "حریم خصوصی", "سیاست حریم خصوصی",
               "<h2>چه چیزی جمع‌آوری می‌کنیم</h2><p>Streaming Guides یک وب‌سایت ایستا است. ما از کوکی، حساب، فرم یا تجزیه‌وتحلیلی که شما را شخصاً شناسایی کند استفاده نمی‌کنیم. ما تبلیغات یا ردیاب‌های وابسته اجرا نمی‌کنیم.</p>"
               "<h2>خدمات شخص ثالث</h2><p>صفحات ویدیوهای YouTube را جاسازی می‌کنند (از طریق دامنه youtube-nocookie.com) و Google Fonts را بارگذاری می‌کنند. این خدمات ممکن است کوکی‌های خود را تنظیم کرده و آدرس‌های IP را ثبت کنند.</p>"
               "<h2>گزارش‌های سرور</h2><p>گزارش‌های استاندارد وب‌سرور ممکن است آدرس IP و صفحه درخواست‌شده را ثبت کنند. این گزارش‌ها را با هیچ هویت شخصی مرتبط نمی‌کنیم.</p>"
               "<h2>حقوق شما</h2><p>اگر در اتحادیه اروپا/بریتانیا هستید، حقوقی تحت GDPR دارید. با هر سؤالی از طریق صفحه تماس با ما در تماس باشید.</p>"
               "<h2>تغییرات</h2><p>این صفحه ممکن است تغییر کند. آخرین نسخه همیشه در این URL موجود است.</p>"),
    },
    "terms": {
        "en": ("Terms of Use — Streaming Guides", "Terms of Use", "Terms of Use",
               "<h2>Audience</h2><p><strong>This site is intended for adults (18+).</strong> The guides cover broadcasting on adult cam platforms. By using this site you confirm you are of legal age in your jurisdiction.</p>"
               "<h2>Information only</h2><p>The guides are provided for informational purposes. We can't guarantee accuracy at all times — platforms change interfaces, settings and policies. Verify steps on the platform's own help center before relying on them.</p>"
               "<h2>No affiliation</h2><p>This site isn't affiliated with, endorsed by or sponsored by any of the cam platforms referenced. All trademarks belong to their respective owners and are used here only for identification.</p>"
               "<h2>SplitCam</h2><p>SplitCam is a separate product. Download it only from the official <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a> website.</p>"
               "<h2>No warranty</h2><p>This site is provided 'as is' without warranty of any kind. We're not liable for any loss arising from use of the information here.</p>"),
        "ru": ("Условия использования — Streaming Guides", "Условия использования", "Условия использования",
               "<h2>Аудитория</h2><p><strong>Сайт предназначен для совершеннолетних (18+).</strong> Гайды посвящены вещанию на adult-кам платформах. Используя сайт, вы подтверждаете, что достигли совершеннолетия по законам вашей юрисдикции.</p>"
               "<h2>Только информация</h2><p>Гайды предоставляются в информационных целях. Мы не можем гарантировать актуальность 100% времени — платформы меняют интерфейсы, настройки и правила. Перед действиями сверяйтесь с официальным хелп-центром платформы.</p>"
               "<h2>Без аффилированности</h2><p>Сайт не аффилирован, не одобрен и не спонсируется ни одной из упомянутых кам-платформ. Все торговые знаки принадлежат их правообладателям и используются здесь только для идентификации.</p>"
               "<h2>SplitCam</h2><p>SplitCam — отдельный продукт. Скачивайте его только с официального сайта <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Без гарантий</h2><p>Сайт предоставляется «как есть», без каких-либо гарантий. Мы не несём ответственности за убытки, возникшие из использования информации с этого сайта.</p>"),
        "es": ("Términos de uso — Streaming Guides", "Términos de uso", "Términos de uso",
               "<h2>Audiencia</h2><p><strong>Este sitio está destinado a adultos (18+).</strong> Las guías cubren la emisión en plataformas cam para adultos. Al usar este sitio confirmas que tienes la mayoría de edad legal en tu jurisdicción.</p>"
               "<h2>Solo información</h2><p>Las guías se proporcionan con fines informativos. No podemos garantizar la exactitud en todo momento — las plataformas cambian interfaces, ajustes y políticas. Verifica los pasos en el centro de ayuda de cada plataforma antes de actuar.</p>"
               "<h2>Sin afiliación</h2><p>Este sitio no está afiliado, respaldado ni patrocinado por ninguna de las plataformas cam mencionadas. Todas las marcas comerciales pertenecen a sus respectivos propietarios y se usan aquí solo para identificación.</p>"
               "<h2>SplitCam</h2><p>SplitCam es un producto independiente. Descárgalo únicamente del sitio oficial <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Sin garantía</h2><p>Este sitio se proporciona «tal cual» sin garantía de ningún tipo. No somos responsables de ninguna pérdida derivada del uso de la información aquí publicada.</p>"),
        "de": ("Nutzungsbedingungen — Streaming Guides", "Nutzungsbedingungen", "Nutzungsbedingungen",
               "<h2>Zielgruppe</h2><p><strong>Diese Seite richtet sich an Erwachsene (18+).</strong> Die Anleitungen behandeln das Senden auf Erwachsenen-Cam-Plattformen. Mit der Nutzung dieser Seite bestätigst du, dass du in deiner Rechtsordnung volljährig bist.</p>"
               "<h2>Nur Informationen</h2><p>Die Anleitungen dienen nur zu Informationszwecken. Wir können keine durchgängige Richtigkeit garantieren — Plattformen ändern Oberflächen, Einstellungen und Richtlinien. Prüfe Schritte im offiziellen Hilfecenter der Plattform, bevor du dich darauf verlässt.</p>"
               "<h2>Keine Verbindung</h2><p>Diese Seite ist nicht mit den genannten Cam-Plattformen verbunden, von ihnen empfohlen oder gesponsert. Alle Marken gehören den jeweiligen Inhabern und werden hier nur zur Identifizierung verwendet.</p>"
               "<h2>SplitCam</h2><p>SplitCam ist ein eigenständiges Produkt. Lade es ausschließlich von der offiziellen Website <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a> herunter.</p>"
               "<h2>Keine Gewährleistung</h2><p>Diese Seite wird ohne jegliche Gewährleistung „wie besehen“ bereitgestellt. Wir haften nicht für Verluste, die sich aus der Nutzung der hier veröffentlichten Informationen ergeben.</p>"),
        "fr": ("Conditions d'utilisation — Streaming Guides", "Conditions d'utilisation", "Conditions d'utilisation",
               "<h2>Public</h2><p><strong>Ce site est destiné aux adultes (18+).</strong> Les guides couvrent la diffusion sur les plateformes cam pour adultes. En utilisant ce site, vous confirmez que vous êtes majeur·e dans votre juridiction.</p>"
               "<h2>Informations uniquement</h2><p>Les guides sont fournis à titre informatif. Nous ne pouvons garantir l'exactitude à tout moment — les plateformes modifient interfaces, paramètres et politiques. Vérifiez les étapes dans le centre d'aide officiel de la plateforme avant de vous y fier.</p>"
               "<h2>Aucune affiliation</h2><p>Ce site n'est ni affilié, ni recommandé, ni sponsorisé par les plateformes cam mentionnées. Toutes les marques appartiennent à leurs propriétaires respectifs et ne sont utilisées ici qu'à des fins d'identification.</p>"
               "<h2>SplitCam</h2><p>SplitCam est un produit distinct. Téléchargez-le uniquement depuis le site officiel <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Aucune garantie</h2><p>Ce site est fourni « en l'état » sans garantie d'aucune sorte. Nous ne sommes pas responsables des pertes résultant de l'utilisation des informations publiées ici.</p>"),
        "it": ("Termini di utilizzo — Streaming Guides", "Termini di utilizzo", "Termini di utilizzo",
               "<h2>Pubblico</h2><p><strong>Questo sito è destinato ad adulti (18+).</strong> Le guide trattano la trasmissione su piattaforme cam per adulti. Usando questo sito confermi di essere maggiorenne nella tua giurisdizione.</p>"
               "<h2>Solo informazione</h2><p>Le guide sono fornite a scopo informativo. Non possiamo garantire l'accuratezza in ogni momento — le piattaforme cambiano interfacce, impostazioni e politiche. Verifica i passaggi nel centro assistenza ufficiale della piattaforma prima di fare affidamento.</p>"
               "<h2>Nessuna affiliazione</h2><p>Questo sito non è affiliato, supportato né sponsorizzato da nessuna delle piattaforme cam menzionate. Tutti i marchi appartengono ai rispettivi proprietari e sono usati qui solo per identificazione.</p>"
               "<h2>SplitCam</h2><p>SplitCam è un prodotto separato. Scaricalo solo dal sito ufficiale <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Nessuna garanzia</h2><p>Questo sito è fornito «così com'è» senza garanzie di alcun tipo. Non siamo responsabili per perdite derivanti dall'uso delle informazioni qui pubblicate.</p>"),
        "pt": ("Termos de uso — Streaming Guides", "Termos de uso", "Termos de uso",
               "<h2>Público</h2><p><strong>Este site é destinado a adultos (18+).</strong> Os guias tratam de transmissão em plataformas cam adultas. Ao usar este site você confirma ser maior de idade na sua jurisdição.</p>"
               "<h2>Apenas informação</h2><p>Os guias são fornecidos pra fins informativos. Não podemos garantir precisão o tempo todo — as plataformas mudam interfaces, configurações e políticas. Confira os passos na central de ajuda oficial da plataforma antes de confiar neles.</p>"
               "<h2>Sem afiliação</h2><p>Este site não é afiliado, endossado nem patrocinado por nenhuma das plataformas cam mencionadas. Todas as marcas pertencem aos seus respectivos donos e são usadas aqui apenas pra identificação.</p>"
               "<h2>SplitCam</h2><p>O SplitCam é um produto separado. Baixe-o apenas do site oficial <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Sem garantia</h2><p>Este site é fornecido «no estado em que se encontra», sem garantia de nenhum tipo. Não somos responsáveis por perdas decorrentes do uso das informações aqui publicadas.</p>"),
        "nl": ("Voorwaarden — Streaming Guides", "Gebruiksvoorwaarden", "Gebruiksvoorwaarden",
               "<h2>Doelgroep</h2><p><strong>Deze site is bedoeld voor volwassenen (18+).</strong> De gidsen behandelen het uitzenden op cam-platforms voor volwassenen. Door deze site te gebruiken bevestig je dat je meerderjarig bent in jouw rechtsgebied.</p>"
               "<h2>Alleen informatief</h2><p>De gidsen zijn ter informatie. We kunnen de juistheid niet op elk moment garanderen — platforms wijzigen interfaces, instellingen en beleid. Controleer de stappen in het officiële helpcentrum van het platform voor je erop vertrouwt.</p>"
               "<h2>Geen affiliatie</h2><p>Deze site is niet gelieerd aan, onderschreven door of gesponsord door een van de genoemde cam-platforms. Alle handelsmerken zijn eigendom van hun respectieve eigenaars en worden hier uitsluitend ter identificatie gebruikt.</p>"
               "<h2>SplitCam</h2><p>SplitCam is een apart product. Download het uitsluitend van de officiële website <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Geen garantie</h2><p>Deze site wordt geleverd «zoals deze is», zonder enige garantie. We zijn niet aansprakelijk voor verlies dat voortvloeit uit het gebruik van de hier gepubliceerde informatie.</p>"),
        "ro": ("Termeni de utilizare — Streaming Guides", "Termeni de utilizare", "Termeni de utilizare",
               "<h2>Public</h2><p><strong>Acest site este destinat adulților (18+).</strong> Ghidurile acoperă transmisiuni pe platforme cam pentru adulți. Prin utilizarea acestui site confirmi că ești major în jurisdicția ta.</p>"
               "<h2>Doar informare</h2><p>Ghidurile sunt furnizate cu scop informativ. Nu putem garanta acuratețea în orice moment — platformele își modifică interfețele, setările și politicile. Verifică pașii în centrul oficial de asistență al platformei înainte de a te baza pe ei.</p>"
               "<h2>Fără afiliere</h2><p>Acest site nu este afiliat, susținut sau sponsorizat de niciuna dintre platformele cam menționate. Toate mărcile aparțin proprietarilor lor și sunt folosite aici doar pentru identificare.</p>"
               "<h2>SplitCam</h2><p>SplitCam este un produs separat. Descarcă-l doar de pe site-ul oficial <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Fără garanție</h2><p>Acest site este furnizat «așa cum este», fără nicio garanție. Nu suntem responsabili pentru pierderile rezultate din utilizarea informațiilor publicate aici.</p>"),
        "bg": ("Условия за ползване — Streaming Guides", "Условия за ползване", "Условия за ползване",
               "<h2>Аудитория</h2><p><strong>Този сайт е предназначен за възрастни (18+).</strong> Ръководствата покриват излъчване на кам платформи за възрастни. Използвайки този сайт, потвърждаваш, че си пълнолетен(на) в твоята юрисдикция.</p>"
               "<h2>Само информация</h2><p>Ръководствата се предоставят с информативна цел. Не можем да гарантираме точност през цялото време — платформите променят интерфейси, настройки и политики. Провери стъпките в официалния център за помощ на платформата, преди да разчиташ на тях.</p>"
               "<h2>Без афилиация</h2><p>Този сайт не е свързан, одобрен или спонсориран от никоя от споменатите кам платформи. Всички търговски марки принадлежат на съответните им собственици и се използват тук само за идентификация.</p>"
               "<h2>SplitCam</h2><p>SplitCam е отделен продукт. Изтегляй го само от официалния сайт <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Без гаранция</h2><p>Този сайт се предоставя «както е», без каквато и да е гаранция. Не носим отговорност за загуби, произтичащи от използването на публикуваната тук информация.</p>"),
        "hu": ("Felhasználási feltételek — Streaming Guides", "Felhasználási feltételek", "Felhasználási feltételek",
               "<h2>Célközönség</h2><p><strong>Ez az oldal felnőtteknek (18+) készült.</strong> Az útmutatók felnőtt cam platformokon való adást ismertetnek. A site használatával megerősíted, hogy nagykorú vagy a saját joghatóságodban.</p>"
               "<h2>Csak információ</h2><p>Az útmutatók tájékoztató jellegűek. Nem tudjuk minden időpontban garantálni a pontosságot — a platformok változtatják felületeiket, beállításaikat és szabályzataikat. Mielőtt rájuk hagyatkoznál, ellenőrizd a lépéseket a platform hivatalos súgóközpontjában.</p>"
               "<h2>Nincs kapcsolat</h2><p>Ez az oldal nincs kapcsolatban, nincs jóváhagyva és nincs szponzorálva az említett cam platformok egyikével sem. Minden védjegy a megfelelő tulajdonosé, és itt kizárólag azonosítás céljából használjuk.</p>"
               "<h2>SplitCam</h2><p>A SplitCam külön termék. Csak a hivatalos <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a> oldalról töltsd le.</p>"
               "<h2>Nincs garancia</h2><p>Ezt az oldalt «adott állapotban» biztosítjuk, mindenféle garancia nélkül. Nem vagyunk felelősek az itt közzétett információk használatából eredő veszteségekért.</p>"),
        "el": ("Όροι χρήσης — Streaming Guides", "Όροι χρήσης", "Όροι χρήσης",
               "<h2>Κοινό</h2><p><strong>Αυτό το site προορίζεται για ενήλικες (18+).</strong> Οι οδηγοί καλύπτουν μετάδοση σε cam πλατφόρμες για ενήλικες. Χρησιμοποιώντας αυτό το site, επιβεβαιώνετε ότι έχετε ενηλικιωθεί στη δικαιοδοσία σας.</p>"
               "<h2>Μόνο πληροφορίες</h2><p>Οι οδηγοί παρέχονται για ενημερωτικούς σκοπούς. Δεν μπορούμε να εγγυηθούμε την ακρίβεια ανά πάσα στιγμή — οι πλατφόρμες αλλάζουν διεπαφές, ρυθμίσεις και πολιτικές. Επαληθεύστε τα βήματα στο επίσημο κέντρο βοήθειας της πλατφόρμας πριν τα εμπιστευτείτε.</p>"
               "<h2>Καμία σύνδεση</h2><p>Αυτό το site δεν σχετίζεται, δεν εγκρίνεται ούτε χρηματοδοτείται από καμία από τις cam πλατφόρμες που αναφέρονται. Όλα τα εμπορικά σήματα ανήκουν στους αντίστοιχους κατόχους τους και χρησιμοποιούνται εδώ μόνο για αναγνώριση.</p>"
               "<h2>SplitCam</h2><p>Το SplitCam είναι ξεχωριστό προϊόν. Κατεβάστε το μόνο από την επίσημη ιστοσελίδα <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Καμία εγγύηση</h2><p>Αυτό το site παρέχεται «ως έχει» χωρίς καμία εγγύηση. Δεν είμαστε υπεύθυνοι για απώλειες που προκύπτουν από τη χρήση των πληροφοριών που δημοσιεύονται εδώ.</p>"),
        "fi": ("Käyttöehdot — Streaming Guides", "Käyttöehdot", "Käyttöehdot",
               "<h2>Yleisö</h2><p><strong>Tämä sivusto on tarkoitettu aikuisille (18+).</strong> Oppaat kattavat lähetykset aikuisille tarkoitetuilla cam-alustoilla. Käyttämällä tätä sivustoa vahvistat, että olet täysi-ikäinen lainkäyttöalueellasi.</p>"
               "<h2>Vain tiedoksi</h2><p>Oppaat tarjotaan tiedonantotarkoituksessa. Emme voi taata oikeellisuutta jokaisena hetkenä — alustat muuttavat käyttöliittymiä, asetuksia ja käytäntöjä. Tarkista vaiheet alustan virallisesta tukikeskuksesta ennen kuin luotat niihin.</p>"
               "<h2>Ei kytköstä</h2><p>Tämä sivusto ei ole sidoksissa, tukema tai sponsoroima minkään mainitun cam-alustan toimesta. Kaikki tavaramerkit kuuluvat omistajilleen ja niitä käytetään täällä vain tunnistamistarkoituksessa.</p>"
               "<h2>SplitCam</h2><p>SplitCam on erillinen tuote. Lataa se vain viralliselta sivustolta <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Ei takuuta</h2><p>Tämä sivusto tarjotaan «sellaisenaan» ilman minkäänlaista takuuta. Emme ole vastuussa täällä julkaistujen tietojen käytöstä aiheutuvista menetyksistä.</p>"),
        "da": ("Vilkår — Streaming Guides", "Vilkår", "Vilkår for brug",
               "<h2>Målgruppe</h2><p><strong>Denne side er tiltænkt voksne (18+).</strong> Guidesne dækker udsendelse på voksen-cam-platforme. Ved at bruge denne side bekræfter du, at du er myndig i din jurisdiktion.</p>"
               "<h2>Kun information</h2><p>Guidesne leveres til informationsformål. Vi kan ikke garantere nøjagtighed til enhver tid — platformene ændrer grænseflader, indstillinger og politikker. Verificer trinene i platformens officielle hjælpecenter, før du stoler på dem.</p>"
               "<h2>Ingen tilknytning</h2><p>Denne side er ikke tilknyttet, godkendt eller sponsoreret af nogen af de nævnte cam-platforme. Alle varemærker tilhører deres respektive ejere og bruges her udelukkende til identifikation.</p>"
               "<h2>SplitCam</h2><p>SplitCam er et separat produkt. Hent det kun fra det officielle <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Ingen garanti</h2><p>Denne side leveres «som den er», uden nogen form for garanti. Vi er ikke ansvarlige for tab, der opstår ved brug af informationen, der offentliggøres her.</p>"),
        "no": ("Vilkår — Streaming Guides", "Vilkår", "Vilkår for bruk",
               "<h2>Målgruppe</h2><p><strong>Denne siden er ment for voksne (18+).</strong> Guidene dekker sending på voksen-cam-plattformer. Ved å bruke denne siden bekrefter du at du er myndig i din jurisdiksjon.</p>"
               "<h2>Kun informasjon</h2><p>Guidene tilbys for informasjonsformål. Vi kan ikke garantere nøyaktighet til enhver tid — plattformene endrer grensesnitt, innstillinger og retningslinjer. Verifiser trinnene i plattformens offisielle hjelpesenter før du stoler på dem.</p>"
               "<h2>Ingen tilknytning</h2><p>Denne siden er ikke tilknyttet, anbefalt eller sponset av noen av de nevnte cam-plattformene. Alle varemerker tilhører sine respektive eiere og brukes her kun for identifisering.</p>"
               "<h2>SplitCam</h2><p>SplitCam er et separat produkt. Last det ned kun fra den offisielle <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>-siden.</p>"
               "<h2>Ingen garanti</h2><p>Denne siden leveres «som den er», uten noen form for garanti. Vi er ikke ansvarlige for tap som oppstår ved bruk av informasjonen som er publisert her.</p>"),
        "sr": ("Услови коришћења — Streaming Guides", "Услови коришћења", "Услови коришћења",
               "<h2>Публика</h2><p><strong>Овај сајт је намењен одраслима (18+).</strong> Водичи покривају преносе на кам платформама за одрасле. Коришћењем овог сајта потврђујеш да си пунолетан(а) у својој јурисдикцији.</p>"
               "<h2>Само информације</h2><p>Водичи се пружају у информативне сврхе. Не можемо гарантовати тачност у сваком тренутку — платформе мењају интерфејсе, подешавања и политике. Провери кораке у званичном центру за помоћ платформе пре него што се ослониш на њих.</p>"
               "<h2>Без повезаности</h2><p>Овај сајт није повезан, подржан нити спонзорисан од стране било које наведене кам платформе. Сви заштитни знаци припадају својим власницима и овде се користе само за идентификацију.</p>"
               "<h2>SplitCam</h2><p>SplitCam је засебан производ. Преузми га само са званичног сајта <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Без гаранције</h2><p>Овај сајт се пружа «такав какав је», без икакве гаранције. Нисмо одговорни за губитке настале коришћењем информација објављених овде.</p>"),
        "hr": ("Uvjeti korištenja — Streaming Guides", "Uvjeti korištenja", "Uvjeti korištenja",
               "<h2>Publika</h2><p><strong>Ova stranica je namijenjena odraslima (18+).</strong> Vodiči pokrivaju prijenose na cam platformama za odrasle. Korištenjem ove stranice potvrđuješ da si punoljetan(a) u svojoj jurisdikciji.</p>"
               "<h2>Samo informacije</h2><p>Vodiči se pružaju u informativne svrhe. Ne možemo jamčiti točnost u svakom trenutku — platforme mijenjaju sučelja, postavke i pravila. Provjeri korake u službenom centru za pomoć platforme prije nego što se osloniš na njih.</p>"
               "<h2>Bez povezanosti</h2><p>Ova stranica nije povezana, podržana niti sponzorirana od strane bilo koje navedene cam platforme. Svi zaštitni znakovi pripadaju svojim vlasnicima i ovdje se koriste samo za identifikaciju.</p>"
               "<h2>SplitCam</h2><p>SplitCam je zaseban proizvod. Preuzmi ga samo sa službene stranice <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Bez jamstva</h2><p>Ova stranica se pruža «takva kakva jest», bez ikakvog jamstva. Nismo odgovorni za gubitke nastale korištenjem informacija objavljenih ovdje.</p>"),
        "zh": ("使用条款 — Streaming Guides", "使用条款", "使用条款",
               "<h2>受众</h2><p><strong>本网站面向成年人（18+）。</strong>指南涵盖成人 cam 平台的直播。使用本网站即表示您确认您在司法管辖区内已达到法定年龄。</p>"
               "<h2>仅供参考</h2><p>这些指南仅供参考。我们无法保证信息始终准确——平台会更改界面、设置和政策。在依赖之前，请在平台的官方帮助中心验证步骤。</p>"
               "<h2>无关联</h2><p>本网站与任何 cam 平台均无关联、未获其认可或赞助。所有商标归各自所有者所有，此处仅用于识别。</p>"
               "<h2>SplitCam</h2><p>SplitCam 是独立产品。请仅从官方网站 <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a> 下载。</p>"
               "<h2>无担保</h2><p>本网站按「现状」提供，不附带任何形式的担保。我们不对因使用此处发布的信息而产生的任何损失负责。</p>"),
        "ja": ("利用規約 — Streaming Guides", "利用規約", "利用規約",
               "<h2>対象者</h2><p><strong>このサイトは成人（18歳以上）向けです。</strong>ガイドは成人 cam プラットフォームでの配信をカバーしています。このサイトを使用することで、あなたは管轄区域で法定年齢に達していることを確認します。</p>"
               "<h2>情報のみ</h2><p>ガイドは情報提供のみを目的としています。常に正確性を保証することはできません — プラットフォームはインターフェース、設定、ポリシーを変更します。依拠する前に、プラットフォーム独自のヘルプセンターで手順を確認してください。</p>"
               "<h2>非提携</h2><p>このサイトは、参照されている cam プラットフォームのいずれとも提携、推奨、後援されていません。すべての商標はそれぞれの所有者に属し、ここでは識別目的でのみ使用されています。</p>"
               "<h2>SplitCam</h2><p>SplitCam は別個の製品です。公式の <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a> ウェブサイトからのみダウンロードしてください。</p>"
               "<h2>保証なし</h2><p>このサイトは「現状のまま」提供され、いかなる種類の保証もありません。ここでの情報の使用に起因する損失について、当社は責任を負いません。</p>"),
        "ar": ("شروط الاستخدام — Streaming Guides", "شروط الاستخدام", "شروط الاستخدام",
               "<h2>الجمهور</h2><p><strong>هذا الموقع مخصص للبالغين (18+).</strong> تغطي الأدلة البث على منصات cam للبالغين. باستخدام هذا الموقع، فإنك تؤكد أنك بلغت السن القانونية في ولايتك القضائية.</p>"
               "<h2>للمعلومات فقط</h2><p>يتم توفير الأدلة لأغراض إعلامية. لا يمكننا ضمان الدقة في جميع الأوقات — تقوم المنصات بتغيير الواجهات والإعدادات والسياسات. تحقق من الخطوات في مركز المساعدة الرسمي للمنصة قبل الاعتماد عليها.</p>"
               "<h2>لا توجد علاقة</h2><p>هذا الموقع ليس تابعًا أو معتمدًا أو مدعومًا من قبل أي من منصات cam المشار إليها. تنتمي جميع العلامات التجارية إلى أصحابها المعنيين وتستخدم هنا للتحديد فقط.</p>"
               "<h2>SplitCam</h2><p>SplitCam هو منتج منفصل. قم بتنزيله فقط من الموقع الرسمي <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>بدون ضمان</h2><p>يتم توفير هذا الموقع «كما هو» بدون ضمان من أي نوع. نحن لسنا مسؤولين عن أي خسارة ناجمة عن استخدام المعلومات المنشورة هنا.</p>"),
        "th": ("ข้อกำหนดการใช้งาน — Streaming Guides", "ข้อกำหนดการใช้งาน", "ข้อกำหนดการใช้งาน",
               "<h2>กลุ่มเป้าหมาย</h2><p><strong>เว็บไซต์นี้มีไว้สำหรับผู้ใหญ่ (18+)</strong> คู่มือครอบคลุมการถ่ายทอดบนแพลตฟอร์ม cam ผู้ใหญ่ การใช้เว็บไซต์นี้แสดงว่าคุณยืนยันว่าคุณมีอายุตามกฎหมายในเขตอำนาจศาลของคุณ</p>"
               "<h2>ข้อมูลเท่านั้น</h2><p>คู่มือนี้จัดทำขึ้นเพื่อวัตถุประสงค์ในการให้ข้อมูล เราไม่สามารถรับประกันความถูกต้องตลอดเวลาได้ — แพลตฟอร์มเปลี่ยนแปลงอินเตอร์เฟส การตั้งค่า และนโยบาย ตรวจสอบขั้นตอนที่ศูนย์ช่วยเหลือของแพลตฟอร์มก่อนพึ่งพา</p>"
               "<h2>ไม่มีความเกี่ยวข้อง</h2><p>เว็บไซต์นี้ไม่ได้สังกัด รับรอง หรือสนับสนุนโดยแพลตฟอร์ม cam ใดๆ ที่อ้างถึง เครื่องหมายการค้าทั้งหมดเป็นของเจ้าของที่เกี่ยวข้องและใช้ที่นี่เพื่อระบุเท่านั้น</p>"
               "<h2>SplitCam</h2><p>SplitCam เป็นผลิตภัณฑ์แยกต่างหาก ดาวน์โหลดจากเว็บไซต์ทางการเท่านั้น <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a></p>"
               "<h2>ไม่มีการรับประกัน</h2><p>เว็บไซต์นี้ให้บริการ «ตามที่เป็น» โดยไม่มีการรับประกันใดๆ เราไม่รับผิดชอบต่อความสูญเสียที่เกิดจากการใช้ข้อมูลที่เผยแพร่ที่นี่</p>"),
        "fil": ("Mga tuntunin — Streaming Guides", "Mga tuntunin", "Mga tuntunin ng paggamit",
                "<h2>Madla</h2><p><strong>Ang site na ito ay para sa mga adulto (18+).</strong> Sinasaklaw ng mga gabay ang pag-broadcast sa adult cam platforms. Sa paggamit ng site na ito, kinukumpirma mong nasa legal na edad ka sa iyong hurisdiksyon.</p>"
                "<h2>Impormasyon lamang</h2><p>Ang mga gabay ay ibinibigay para sa mga layuning impormasyon. Hindi namin masisigurado ang kawastuhan sa lahat ng oras — ang mga platform ay nagbabago ng mga interface, setting, at patakaran. I-verify ang mga hakbang sa opisyal na help center ng platform bago umasa sa mga ito.</p>"
                "<h2>Walang kaakibatan</h2><p>Ang site na ito ay hindi kaakibat, hindi inendorso, at hindi sponsor ng anumang sinangguni na cam platform. Ang lahat ng trademark ay pag-aari ng kani-kanilang may-ari at ginagamit dito para lamang sa pagkakakilanlan.</p>"
                "<h2>SplitCam</h2><p>Ang SplitCam ay isang hiwalay na produkto. I-download lamang ito mula sa opisyal na website na <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
                "<h2>Walang warranty</h2><p>Ang site na ito ay ibinibigay «as is» nang walang anumang warranty. Hindi kami mananagot sa anumang pagkalugi na dulot ng paggamit ng impormasyong inilathala dito.</p>"),
        "tr": ("Kullanım Koşulları — Streaming Guides", "Kullanım Koşulları", "Kullanım Koşulları",
               "<h2>Kitle</h2><p><strong>Bu site yetişkinler (18+) içindir.</strong> Rehberler yetişkin cam platformlarında yayın yapmayı kapsar. Bu siteyi kullanarak kendi yargı bölgende reşit olduğunu onaylarsın.</p>"
               "<h2>Yalnızca bilgi</h2><p>Rehberler bilgilendirme amaçlıdır. Her zaman doğruluğu garanti edemeyiz — platformlar arayüzlerini, ayarlarını ve politikalarını değiştirir. Güvenmeden önce adımları platformun resmi yardım merkezinde doğrula.</p>"
               "<h2>Bağlantı yok</h2><p>Bu site, atıfta bulunulan cam platformlarının hiçbiriyle bağlantılı, onaylı veya sponsorlu değildir. Tüm ticari markalar ilgili sahiplerine aittir ve burada yalnızca tanımlama için kullanılır.</p>"
               "<h2>SplitCam</h2><p>SplitCam ayrı bir üründür. Yalnızca resmi <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a> sitesinden indir.</p>"
               "<h2>Garanti yok</h2><p>Bu site herhangi bir garanti olmadan «olduğu gibi» sunulur. Burada yayınlanan bilgilerin kullanımından doğan kayıplardan sorumlu değiliz.</p>"),
        "id": ("Ketentuan — Streaming Guides", "Ketentuan", "Ketentuan Penggunaan",
               "<h2>Audiens</h2><p><strong>Situs ini untuk dewasa (18+).</strong> Panduan mencakup siaran di platform cam dewasa. Dengan memakai situs ini, kamu mengonfirmasi bahwa kamu telah cukup umur secara hukum di wilayahmu.</p>"
               "<h2>Hanya informasi</h2><p>Panduan disediakan untuk tujuan informasi. Kami tidak bisa menjamin keakuratan setiap saat — platform mengubah antarmuka, pengaturan, dan kebijakan. Verifikasi langkah di pusat bantuan resmi platform sebelum mengandalkannya.</p>"
               "<h2>Tanpa afiliasi</h2><p>Situs ini tidak berafiliasi, didukung, atau disponsori oleh platform cam mana pun yang dirujuk. Semua merek dagang adalah milik pemiliknya masing-masing dan dipakai di sini hanya untuk identifikasi.</p>"
               "<h2>SplitCam</h2><p>SplitCam adalah produk terpisah. Unduh hanya dari situs resmi <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Tanpa jaminan</h2><p>Situs ini disediakan «apa adanya» tanpa jaminan apa pun. Kami tidak bertanggung jawab atas kerugian apa pun akibat penggunaan informasi yang dipublikasikan di sini.</p>"),
        "vi": ("Điều khoản — Streaming Guides", "Điều khoản", "Điều khoản sử dụng",
               "<h2>Đối tượng</h2><p><strong>Trang này dành cho người lớn (18+).</strong> Hướng dẫn bao quát việc phát sóng trên các nền tảng cam người lớn. Khi dùng trang này, bạn xác nhận đã đủ tuổi hợp pháp tại khu vực của mình.</p>"
               "<h2>Chỉ để tham khảo</h2><p>Hướng dẫn được cung cấp nhằm mục đích thông tin. Chúng tôi không thể đảm bảo độ chính xác mọi lúc — các nền tảng thay đổi giao diện, cài đặt và chính sách. Hãy xác minh các bước tại trung tâm trợ giúp chính thức của nền tảng trước khi dựa vào chúng.</p>"
               "<h2>Không liên kết</h2><p>Trang này không liên kết, không được chứng thực hay tài trợ bởi bất kỳ nền tảng cam nào được nhắc tới. Mọi nhãn hiệu thuộc về chủ sở hữu tương ứng và được dùng ở đây chỉ để nhận dạng.</p>"
               "<h2>SplitCam</h2><p>SplitCam là sản phẩm riêng biệt. Chỉ tải từ site chính thức <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Không bảo hành</h2><p>Trang này được cung cấp «nguyên trạng» không kèm bảo hành nào. Chúng tôi không chịu trách nhiệm cho mọi tổn thất phát sinh từ việc dùng thông tin đăng tại đây.</p>"),
        "pl": ("Regulamin — Streaming Guides", "Regulamin", "Regulamin korzystania",
               "<h2>Odbiorcy</h2><p><strong>Ta strona jest dla dorosłych (18+).</strong> Poradniki obejmują nadawanie na platformach cam dla dorosłych. Korzystając z tej strony, potwierdzasz, że jesteś pełnoletni w swojej jurysdykcji.</p>"
               "<h2>Tylko informacyjnie</h2><p>Poradniki służą celom informacyjnym. Nie możemy gwarantować dokładności przez cały czas — platformy zmieniają interfejsy, ustawienia i zasady. Zweryfikuj kroki w oficjalnym centrum pomocy platformy, zanim na nich polegniesz.</p>"
               "<h2>Brak powiązań</h2><p>Ta strona nie jest powiązana, wspierana ani sponsorowana przez żadną z przywołanych platform cam. Wszystkie znaki towarowe należą do ich właścicieli i są tu używane wyłącznie do identyfikacji.</p>"
               "<h2>SplitCam</h2><p>SplitCam to osobny produkt. Pobieraj go wyłącznie z oficjalnej strony <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Brak gwarancji</h2><p>Ta strona jest udostępniana «tak jak jest» bez jakiejkolwiek gwarancji. Nie ponosimy odpowiedzialności za jakiekolwiek straty wynikłe z korzystania z opublikowanych tu informacji.</p>"),
        "ko": ("이용약관 — Streaming Guides", "이용약관", "이용약관",
               "<h2>대상</h2><p><strong>이 사이트는 성인(18세 이상)용입니다.</strong> 가이드는 성인 캠 플랫폼에서의 방송을 다룹니다. 이 사이트를 이용함으로써 귀하가 거주 관할권에서 법적 성인임을 확인합니다.</p>"
               "<h2>정보 제공 목적</h2><p>가이드는 정보 제공 목적으로 제공됩니다. 항상 정확성을 보장할 수 없습니다 — 플랫폼은 인터페이스, 설정, 정책을 바꿉니다. 의존하기 전에 플랫폼 공식 고객센터에서 단계를 확인하세요.</p>"
               "<h2>제휴 없음</h2><p>이 사이트는 언급된 어떤 캠 플랫폼과도 제휴·보증·후원 관계가 없습니다. 모든 상표는 각 소유자의 자산이며 여기서는 식별 목적으로만 사용됩니다.</p>"
               "<h2>SplitCam</h2><p>SplitCam은 별개의 제품입니다. 공식 사이트 <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>에서만 다운로드하세요.</p>"
               "<h2>보증 없음</h2><p>이 사이트는 어떤 보증도 없이 «있는 그대로» 제공됩니다. 여기 게시된 정보의 사용으로 인한 손실에 대해 책임지지 않습니다.</p>"),
        "uk": ("Умови — Streaming Guides", "Умови", "Умови використання",
               "<h2>Аудиторія</h2><p><strong>Цей сайт для дорослих (18+).</strong> Посібники охоплюють трансляції на дорослих кам-платформах. Користуючись цим сайтом, ви підтверджуєте, що досягли повноліття у своїй юрисдикції.</p>"
               "<h2>Лише інформація</h2><p>Посібники надаються в інформаційних цілях. Ми не можемо гарантувати точність повсякчас — платформи змінюють інтерфейси, налаштування й політики. Перевіряйте кроки в офіційному центрі допомоги платформи, перш ніж покладатися на них.</p>"
               "<h2>Без зв'язків</h2><p>Цей сайт не пов'язаний, не схвалений і не спонсорований жодною зі згаданих кам-платформ. Усі торгові марки належать їхнім власникам і використовуються тут лише для ідентифікації.</p>"
               "<h2>SplitCam</h2><p>SplitCam — окремий продукт. Завантажуйте його лише з офіційного сайту <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Без гарантій</h2><p>Цей сайт надається «як є» без жодних гарантій. Ми не несемо відповідальності за будь-які збитки, спричинені використанням опублікованої тут інформації.</p>"),
        "cs": ("Podmínky — Streaming Guides", "Podmínky", "Podmínky použití",
               "<h2>Publikum</h2><p><strong>Tento web je pro dospělé (18+).</strong> Návody pokrývají vysílání na dospělých cam platformách. Používáním tohoto webu potvrzujete, že jste plnoletí ve své jurisdikci.</p>"
               "<h2>Jen informace</h2><p>Návody jsou poskytovány pro informační účely. Nemůžeme zaručit přesnost po celou dobu — platformy mění rozhraní, nastavení a zásady. Ověřte si kroky v oficiálním centru nápovědy platformy, než se na ně spolehnete.</p>"
               "<h2>Bez vazeb</h2><p>Tento web není spojen, schválen ani sponzorován žádnou z uvedených cam platforem. Všechny ochranné známky patří jejich vlastníkům a používají se zde jen pro identifikaci.</p>"
               "<h2>SplitCam</h2><p>SplitCam je samostatný produkt. Stahujte ho pouze z oficiálního webu <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Bez záruky</h2><p>Tento web je poskytován «tak jak je» bez jakékoli záruky. Neneseme odpovědnost za žádné ztráty způsobené použitím zde zveřejněných informací.</p>"),
        "sk": ("Podmienky — Streaming Guides", "Podmienky", "Podmienky používania",
               "<h2>Publikum</h2><p><strong>Tento web je pre dospelých (18+).</strong> Návody pokrývajú vysielanie na dospelých cam platformách. Používaním tohto webu potvrdzujete, že ste plnoletí vo svojej jurisdikcii.</p>"
               "<h2>Len informácie</h2><p>Návody sú poskytované na informačné účely. Nemôžeme zaručiť presnosť po celý čas — platformy menia rozhrania, nastavenia a zásady. Overte si kroky v oficiálnom centre pomoci platformy, než sa na ne spoľahnete.</p>"
               "<h2>Bez väzieb</h2><p>Tento web nie je spojený, schválený ani sponzorovaný žiadnou z uvedených cam platforiem. Všetky ochranné známky patria ich vlastníkom a používajú sa tu len na identifikáciu.</p>"
               "<h2>SplitCam</h2><p>SplitCam je samostatný produkt. Sťahujte ho len z oficiálneho webu <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Bez záruky</h2><p>Tento web je poskytovaný «tak ako je» bez akejkoľvek záruky. Nenesieme zodpovednosť za žiadne straty spôsobené použitím tu zverejnených informácií.</p>"),
        "sv": ("Villkor — Streaming Guides", "Villkor", "Användarvillkor",
               "<h2>Publik</h2><p><strong>Den här sajten är för vuxna (18+).</strong> Guiderna täcker sändning på cam-plattformar för vuxna. Genom att använda sajten bekräftar du att du är myndig i din jurisdiktion.</p>"
               "<h2>Endast information</h2><p>Guiderna tillhandahålls i informationssyfte. Vi kan inte garantera korrekthet hela tiden — plattformar ändrar gränssnitt, inställningar och regler. Verifiera stegen i plattformens officiella hjälpcenter innan du litar på dem.</p>"
               "<h2>Inga kopplingar</h2><p>Den här sajten är inte ansluten till, godkänd av eller sponsrad av någon av de nämnda cam-plattformarna. Alla varumärken tillhör sina ägare och används här endast för identifiering.</p>"
               "<h2>SplitCam</h2><p>SplitCam är en separat produkt. Ladda bara ner den från den officiella sajten <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Ingen garanti</h2><p>Den här sajten tillhandahålls «i befintligt skick» utan någon garanti. Vi ansvarar inte för några förluster orsakade av användning av informationen som publiceras här.</p>"),
        "ms": ("Terma — Streaming Guides", "Terma", "Terma Penggunaan",
               "<h2>Audiens</h2><p><strong>Tapak ini untuk dewasa (18+).</strong> Panduan merangkumi siaran di platform cam dewasa. Dengan menggunakan tapak ini, anda mengesahkan bahawa anda telah cukup umur secara sah di bidang kuasa anda.</p>"
               "<h2>Maklumat sahaja</h2><p>Panduan disediakan untuk tujuan maklumat. Kami tidak dapat menjamin ketepatan setiap masa — platform mengubah antara muka, tetapan dan dasar. Sahkan langkah di pusat bantuan rasmi platform sebelum bergantung padanya.</p>"
               "<h2>Tiada gabungan</h2><p>Tapak ini tidak bergabung, disokong atau ditaja oleh mana-mana platform cam yang dirujuk. Semua tanda dagangan milik pemilik masing-masing dan digunakan di sini hanya untuk pengenalan.</p>"
               "<h2>SplitCam</h2><p>SplitCam ialah produk berasingan. Muat turun hanya dari tapak rasmi <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>Tiada jaminan</h2><p>Tapak ini disediakan «sebagaimana adanya» tanpa sebarang jaminan. Kami tidak bertanggungjawab atas sebarang kerugian akibat penggunaan maklumat yang diterbitkan di sini.</p>"),
        "he": ("תנאים — Streaming Guides", "תנאים", "תנאי שימוש",
               "<h2>קהל</h2><p><strong>אתר זה מיועד למבוגרים (18+).</strong> המדריכים מכסים שידור בפלטפורמות קאם למבוגרים. בשימוש באתר זה אתם מאשרים שאתם בגיל חוקי בתחום השיפוט שלכם.</p>"
               "<h2>מידע בלבד</h2><p>המדריכים מסופקים למטרות מידע. איננו יכולים להבטיח דיוק בכל עת — הפלטפורמות משנות ממשקים, הגדרות ומדיניות. אמתו את השלבים במרכז העזרה הרשמי של הפלטפורמה לפני שתסתמכו עליהם.</p>"
               "<h2>ללא קשרים</h2><p>אתר זה אינו מסונף, מאושר או ממומן על ידי אף אחת מפלטפורמות הקאם המוזכרות. כל הסימנים המסחריים שייכים לבעליהם ומשמשים כאן לזיהוי בלבד.</p>"
               "<h2>SplitCam</h2><p>SplitCam הוא מוצר נפרד. הורידו אותו רק מהאתר הרשמי <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a>.</p>"
               "<h2>ללא אחריות</h2><p>אתר זה מסופק «כפי שהוא» ללא כל אחריות. איננו אחראים לכל אובדן שנגרם משימוש במידע המתפרסם כאן.</p>"),
        "hi": ("शर्तें — Streaming Guides", "शर्तें", "उपयोग की शर्तें",
               "<h2>दर्शक</h2><p><strong>यह साइट वयस्कों (18+) के लिए है।</strong> गाइड वयस्क कैम प्लेटफ़ॉर्म पर ब्रॉडकास्टिंग कवर करते हैं।</p>"
               "<h2>केवल जानकारी</h2><p>गाइड जानकारी उद्देश्यों के लिए हैं। हम सटीकता की गारंटी नहीं दे सकते।</p>"
               "<h2>कोई संबद्धता नहीं</h2><p>यह साइट किसी कैम प्लेटफ़ॉर्म से संबद्ध, समर्थित या प्रायोजित नहीं है।</p>"
               "<h2>SplitCam</h2><p>SplitCam एक अलग उत्पाद है। केवल आधिकारिक साइट <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a> से डाउनलोड करें।</p>"
               "<h2>कोई वारंटी नहीं</h2><p>यह साइट «जैसी है» बिना किसी वारंटी के प्रदान की जाती है।</p>"),
        "fa": ("شرایط — Streaming Guides", "شرایط", "شرایط استفاده",
               "<h2>مخاطبان</h2><p><strong>این سایت برای بزرگسالان (۱۸+) است.</strong> راهنماها پخش در پلتفرم‌های کم بزرگسالان را پوشش می‌دهند. با استفاده از این سایت تأیید می‌کنید که در حوزه قضایی خود سن قانونی دارید.</p>"
               "<h2>فقط اطلاعات</h2><p>راهنماها برای اهداف اطلاعاتی ارائه می‌شوند. نمی‌توانیم دقت را در همه اوقات تضمین کنیم — پلتفرم‌ها رابط‌ها، تنظیمات و سیاست‌ها را تغییر می‌دهند.</p>"
               "<h2>بدون وابستگی</h2><p>این سایت با هیچ‌یک از پلتفرم‌های کم ذکرشده وابستگی، تأیید یا حمایت ندارد. تمام علائم تجاری متعلق به صاحبانشان هستند.</p>"
               "<h2>SplitCam</h2><p>SplitCam یک محصول جداگانه است. فقط از سایت رسمی <a href='https://splitcam.com/' rel='nofollow'>splitcam.com</a> دانلود کنید.</p>"
               "<h2>بدون ضمانت</h2><p>این سایت «همان‌طور که هست» بدون هیچ ضمانتی ارائه می‌شود.</p>"),
    },
    "contact": {
        "en": ("Contact — Streaming Guides", "Contact", "Contact",
               "<p>For questions, corrections or feedback about the guides, write to <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>We don't handle account or technical support for the cam platforms themselves — contact each platform's official support for that.</p>"
               "<p>For SplitCam software support, see <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "ru": ("Контакты — Streaming Guides", "Контакты", "Контакты",
               "<p>Вопросы, правки и предложения по гайдам — на <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Поддержку аккаунтов и техподдержку самих кам-платформ мы не оказываем — пишите в официальную поддержку каждой платформы.</p>"
               "<p>По поддержке программы SplitCam — <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "es": ("Contacto — Streaming Guides", "Contacto", "Contacto",
               "<p>Para consultas, correcciones o comentarios sobre las guías, escribe a <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>No gestionamos soporte de cuenta ni soporte técnico de las propias plataformas cam — contacta con el soporte oficial de cada plataforma para eso.</p>"
               "<p>Para soporte del software SplitCam, consulta <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "de": ("Kontakt — Streaming Guides", "Kontakt", "Kontakt",
               "<p>Für Fragen, Korrekturen oder Feedback zu den Anleitungen schreib uns an <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Konto- oder technischen Support für die Cam-Plattformen selbst leisten wir nicht — wende dich dafür an den offiziellen Support der jeweiligen Plattform.</p>"
               "<p>Für Support zur SplitCam-Software siehe <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "fr": ("Contact — Streaming Guides", "Contact", "Contact",
               "<p>Pour toute question, correction ou retour sur les guides, écrivez à <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Nous ne gérons pas le support de compte ni le support technique des plateformes cam elles-mêmes — adressez-vous au support officiel de chaque plateforme.</p>"
               "<p>Pour le support du logiciel SplitCam, voir <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "it": ("Contatti — Streaming Guides", "Contatti", "Contatti",
               "<p>Per domande, correzioni o feedback sulle guide, scrivici a <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Non gestiamo supporto account o tecnico per le piattaforme cam in sé — contatta il supporto ufficiale di ciascuna piattaforma per quello.</p>"
               "<p>Per il supporto del software SplitCam, vedi <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "pt": ("Contato — Streaming Guides", "Contato", "Contato",
               "<p>Pra dúvidas, correções ou feedback sobre os guias, escreva pra <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Não damos suporte de conta nem técnico das próprias plataformas cam — fale com o suporte oficial de cada plataforma pra isso.</p>"
               "<p>Pra suporte do software SplitCam, veja <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "nl": ("Contact — Streaming Guides", "Contact", "Contact",
               "<p>Voor vragen, correcties of feedback over de gidsen, mail naar <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>We bieden geen account- of technische ondersteuning voor de cam-platforms zelf — neem voor zulke vragen contact op met de officiële support van het betreffende platform.</p>"
               "<p>Voor SplitCam-softwaresupport, zie <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "ro": ("Contact — Streaming Guides", "Contact", "Contact",
               "<p>Pentru întrebări, corecții sau feedback despre ghiduri, scrie la <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Nu oferim asistență pentru conturi sau asistență tehnică pentru platformele cam în sine — contactează asistența oficială a fiecărei platforme pentru asta.</p>"
               "<p>Pentru asistența software SplitCam, vezi <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "bg": ("Контакти — Streaming Guides", "Контакти", "Контакти",
               "<p>За въпроси, корекции или обратна връзка относно ръководствата, пиши на <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Не предоставяме поддръжка за акаунти или техническа поддръжка за самите кам платформи — обърни се към официалната поддръжка на всяка платформа за това.</p>"
               "<p>За поддръжка на софтуера SplitCam, виж <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "hu": ("Kapcsolat — Streaming Guides", "Kapcsolat", "Kapcsolat",
               "<p>Az útmutatókkal kapcsolatos kérdésekért, javításokért vagy visszajelzésért írj a <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a> címre.</p>"
               "<p>Nem nyújtunk fiók- vagy technikai támogatást maguknak a cam platformoknak — ehhez fordulj az egyes platformok hivatalos támogatásához.</p>"
               "<p>SplitCam szoftvertámogatáshoz lásd: <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "el": ("Επικοινωνία — Streaming Guides", "Επικοινωνία", "Επικοινωνία",
               "<p>Για ερωτήσεις, διορθώσεις ή σχόλια σχετικά με τους οδηγούς, γράψτε στο <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Δεν παρέχουμε υποστήριξη λογαριασμού ή τεχνική υποστήριξη για τις ίδιες τις cam πλατφόρμες — επικοινωνήστε με την επίσημη υποστήριξη κάθε πλατφόρμας για αυτό.</p>"
               "<p>Για υποστήριξη του λογισμικού SplitCam, δείτε <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "fi": ("Yhteystiedot — Streaming Guides", "Yhteystiedot", "Yhteystiedot",
               "<p>Kysymyksiä, korjauksia tai palautetta oppaista voi lähettää osoitteeseen <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Emme tarjoa tili- tai teknistä tukea itse cam-alustoille — ota yhteyttä kunkin alustan viralliseen tukeen sitä varten.</p>"
               "<p>SplitCam-ohjelmiston tukea varten katso <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "da": ("Kontakt — Streaming Guides", "Kontakt", "Kontakt",
               "<p>For spørgsmål, rettelser eller feedback om guidesne, skriv til <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Vi yder ikke konto- eller teknisk support for selve cam-platformene — kontakt den enkelte platforms officielle support for det.</p>"
               "<p>For SplitCam-softwaresupport, se <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "no": ("Kontakt — Streaming Guides", "Kontakt", "Kontakt",
               "<p>For spørsmål, rettelser eller tilbakemeldinger om guidene, skriv til <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Vi gir ikke konto- eller teknisk støtte for selve cam-plattformene — kontakt hver plattforms offisielle støtte for det.</p>"
               "<p>For SplitCam-programvarestøtte, se <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "sr": ("Контакт — Streaming Guides", "Контакт", "Контакт",
               "<p>За питања, исправке или повратне информације о водичима, пиши на <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Не пружамо подршку за налоге или техничку подршку за саме кам платформе — обрати се званичној подршци сваке платформе за то.</p>"
               "<p>За подршку за софтвер SplitCam, погледај <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "hr": ("Kontakt — Streaming Guides", "Kontakt", "Kontakt",
               "<p>Za pitanja, ispravke ili povratne informacije o vodičima, piši na <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Ne pružamo podršku za račune ni tehničku podršku za same cam platforme — obrati se službenoj podršci svake platforme za to.</p>"
               "<p>Za podršku za softver SplitCam, pogledaj <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "zh": ("联系 — Streaming Guides", "联系", "联系",
               "<p>有关指南的问题、更正或反馈，请发送电子邮件至 <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>。</p>"
               "<p>我们不处理 cam 平台本身的账户或技术支持 — 请联系每个平台的官方支持。</p>"
               "<p>有关 SplitCam 软件支持，请参阅 <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>。</p>"),
        "ja": ("お問い合わせ — Streaming Guides", "お問い合わせ", "お問い合わせ",
               "<p>ガイドに関するご質問、修正、フィードバックは <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a> までご連絡ください。</p>"
               "<p>cam プラットフォーム自体のアカウントまたは技術サポートは取り扱っておりません — 各プラットフォームの公式サポートにお問い合わせください。</p>"
               "<p>SplitCam ソフトウェアサポートについては、<a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a> をご覧ください。</p>"),
        "ar": ("اتصل بنا — Streaming Guides", "اتصل بنا", "اتصل بنا",
               "<p>للأسئلة أو التصحيحات أو التعليقات حول الأدلة، اكتب إلى <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>نحن لا نتعامل مع دعم الحساب أو الدعم الفني لمنصات cam نفسها — اتصل بالدعم الرسمي لكل منصة لذلك.</p>"
               "<p>للحصول على دعم برنامج SplitCam، راجع <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "th": ("ติดต่อ — Streaming Guides", "ติดต่อ", "ติดต่อ",
               "<p>สำหรับคำถาม การแก้ไข หรือข้อเสนอแนะเกี่ยวกับคู่มือ เขียนถึง <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a></p>"
               "<p>เราไม่จัดการกับการสนับสนุนบัญชีหรือการสนับสนุนทางเทคนิคสำหรับแพลตฟอร์ม cam เอง — ติดต่อฝ่ายสนับสนุนทางการของแต่ละแพลตฟอร์มสำหรับสิ่งนั้น</p>"
               "<p>สำหรับการสนับสนุนซอฟต์แวร์ SplitCam ดูที่ <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a></p>"),
        "fil": ("Kontakin — Streaming Guides", "Kontakin", "Kontakin",
                "<p>Para sa mga tanong, pagwawasto, o feedback tungkol sa mga gabay, sumulat sa <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
                "<p>Hindi kami humahawak ng suporta sa account o teknikal na suporta para sa mga cam platform mismo — kontakin ang opisyal na suporta ng bawat platform para diyan.</p>"
                "<p>Para sa suporta sa software ng SplitCam, tingnan ang <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "tr": ("İletişim — Streaming Guides", "İletişim", "İletişim",
               "<p>Rehberlerle ilgili sorular, düzeltmeler veya geri bildirim için <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a> adresine yaz.</p>"
               "<p>Cam platformlarının kendileri için hesap veya teknik destek sağlamıyoruz — bunun için her platformun resmi desteğine başvur.</p>"
               "<p>SplitCam yazılım desteği için <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>'a bak.</p>"),
        "id": ("Kontak — Streaming Guides", "Kontak", "Kontak",
               "<p>Untuk pertanyaan, koreksi, atau masukan tentang panduan, tulis ke <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Kami tidak menangani dukungan akun atau teknis untuk platform cam itu sendiri — hubungi dukungan resmi tiap platform untuk itu.</p>"
               "<p>Untuk dukungan software SplitCam, lihat <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "vi": ("Liên hệ — Streaming Guides", "Liên hệ", "Liên hệ",
               "<p>Với câu hỏi, đính chính hoặc góp ý về các hướng dẫn, hãy viết tới <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Chúng tôi không xử lý hỗ trợ tài khoản hay kỹ thuật cho chính các nền tảng cam — hãy liên hệ hỗ trợ chính thức của từng nền tảng cho việc đó.</p>"
               "<p>Để được hỗ trợ phần mềm SplitCam, xem <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "pl": ("Kontakt — Streaming Guides", "Kontakt", "Kontakt",
               "<p>W sprawie pytań, poprawek lub opinii o poradnikach pisz na <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Nie zajmujemy się wsparciem konta ani technicznym dla samych platform cam — w tej sprawie skontaktuj się z oficjalnym wsparciem każdej platformy.</p>"
               "<p>W sprawie wsparcia oprogramowania SplitCam zobacz <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "ko": ("문의 — Streaming Guides", "문의", "문의",
               "<p>가이드에 대한 질문, 정정, 의견은 <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>으로 보내주세요.</p>"
               "<p>저희는 캠 플랫폼 자체의 계정·기술 지원을 처리하지 않습니다 — 그건 각 플랫폼의 공식 지원에 문의하세요.</p>"
               "<p>SplitCam 소프트웨어 지원은 <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>를 참고하세요.</p>"),
        "uk": ("Контакти — Streaming Guides", "Контакти", "Контакти",
               "<p>З питань, виправлень чи відгуків про посібники пишіть на <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Ми не займаємося підтримкою акаунтів чи технічною підтримкою самих кам-платформ — з цим звертайтеся до офіційної підтримки кожної платформи.</p>"
               "<p>Щодо підтримки програми SplitCam дивіться <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "cs": ("Kontakt — Streaming Guides", "Kontakt", "Kontakt",
               "<p>S dotazy, opravami nebo zpětnou vazbou k návodům pište na <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Nezajišťujeme podporu účtů ani technickou podporu samotných cam platforem — s tím se obraťte na oficiální podporu každé platformy.</p>"
               "<p>Pro podporu softwaru SplitCam viz <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "sk": ("Kontakt — Streaming Guides", "Kontakt", "Kontakt",
               "<p>S otázkami, opravami alebo spätnou väzbou k návodom píšte na <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Nezabezpečujeme podporu účtov ani technickú podporu samotných cam platforiem — s tým sa obráťte na oficiálnu podporu každej platformy.</p>"
               "<p>Pre podporu softvéru SplitCam pozri <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "sv": ("Kontakt — Streaming Guides", "Kontakt", "Kontakt",
               "<p>För frågor, rättelser eller feedback om guiderna, skriv till <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Vi hanterar inte konto- eller teknisk support för själva cam-plattformarna — kontakta varje plattforms officiella support för det.</p>"
               "<p>För support för SplitCam-mjukvaran, se <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "ms": ("Hubungi — Streaming Guides", "Hubungi", "Hubungi",
               "<p>Untuk pertanyaan, pembetulan atau maklum balas tentang panduan, tulis ke <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>Kami tidak mengendalikan sokongan akaun atau teknikal untuk platform cam itu sendiri — hubungi sokongan rasmi setiap platform untuk itu.</p>"
               "<p>Untuk sokongan perisian SplitCam, lihat <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "he": ("צור קשר — Streaming Guides", "צור קשר", "צור קשר",
               "<p>לשאלות, תיקונים או משוב על המדריכים, כתבו ל-<a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a>.</p>"
               "<p>איננו מטפלים בתמיכת חשבון או תמיכה טכנית לפלטפורמות הקאם עצמן — פנו לתמיכה הרשמית של כל פלטפורמה לשם כך.</p>"
               "<p>לתמיכה בתוכנת SplitCam, ראו <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a>.</p>"),
        "hi": ("संपर्क — Streaming Guides", "संपर्क", "संपर्क",
               "<p>गाइड के बारे में प्रश्नों, सुधारों या फ़ीडबैक के लिए <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a> पर लिखें।</p>"
               "<p>हम कैम प्लेटफ़ॉर्म के लिए अकाउंट या तकनीकी सहायता नहीं संभालते।</p>"
               "<p>SplitCam सॉफ़्टवेयर सहायता के लिए <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a> देखें।</p>"),
        "fa": ("تماس با ما — Streaming Guides", "تماس با ما", "تماس با ما",
               "<p>برای سؤالات، تصحیحات یا بازخورد درباره راهنماها به <a href=\"mailto:hello@camstreamguide.com\">hello@camstreamguide.com</a> بنویسید.</p>"
               "<p>ما پشتیبانی حساب یا فنی برای پلتفرم‌های کم خود را انجام نمی‌دهیم — برای این کار با پشتیبانی رسمی هر پلتفرم تماس بگیرید.</p>"
               "<p>برای پشتیبانی نرم‌افزار SplitCam به <a href=\"https://splitcam.com/support\" rel=\"nofollow\">splitcam.com/support</a> مراجعه کنید.</p>"),
    },
}


def render_legal(slug, lang):
    u = UI[lang]
    title, h1, crumb, body = LEGAL[slug][lang]
    depth = "../" if u["path"] else ""
    home = depth or "./"
    canon = f'{SITE}/{u["path"]}{slug}/'
    hreflang_html = "\n".join(
        f'<link rel="alternate" hreflang="{L}" href="{SITE}/{LANG_PATH[L]}{slug}/">'
        for L in LANGS_AVAIL
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/{slug}/">'
    og_image = f'{SITE}/assets/og/hub-{lang}.png'
    return f"""<!DOCTYPE html>
<html lang="{u['lang']}"{" dir=\"rtl\"" if u['lang'] in RTL_LANGS else ""}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)}</title>
<meta name="description" content="{e(title)}">
<link rel="canonical" href="{canon}">
{hreflang_html}
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/svg+xml" href="{depth}favicon.svg">
<link rel="icon" type="image/x-icon" href="{depth}favicon.ico">
<link rel="apple-touch-icon" href="{depth}apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{e(title)}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta property="og:image" content="{og_image}">
<meta name="theme-color" content="#141420">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
{LANG_REDIRECT_JS}
{AHREFS_JS}
</head>
<body>
{nav_html(home, u['home'], lang_switch(lang, depth))}
<div class="breadcrumbs">
  <a href="{home}">{u['crumb_home']}</a><span class="sep">/</span><span>{e(crumb)}</span>
</div>
<section class="section" style="max-width:760px;margin:0 auto;padding-top:24px">
  <h1 class="h1">{e(h1)}</h1>
  <div class="legal-body">{body}</div>
</section>
<footer>
  <div class="footer-inner">
    <div>© 2026 {SITE_NAME} · <span class="age-tag-sm">18+</span></div>
    <div class="footer-links">
      <a href="{home}">{u['home']}</a>
      <a href="{depth}{MODEL_SLUG}/">{e(MODEL_GUIDE.get(lang, MODEL_GUIDE["en"])["h1short"])}</a>
      <a href="{depth}{OBS_SLUG}/">{OBS_NAV.get(lang, "SplitCam vs OBS")}</a>
      <a href="{depth}about/">{u['about']}</a>
      <a href="{depth}contact/">{u['contact']}</a>
      <a href="{depth}privacy/">{u['privacy']}</a>
      <a href="{depth}terms/">{u['terms']}</a>
    </div>
  </div>
</footer>
</body>
</html>
"""


def render_model_guide(lang):
    """Render the 'how to become a cam model' top-funnel page (indexable SEO target)."""
    u = UI[lang]
    c = MODEL_GUIDE.get(lang) or MODEL_GUIDE["en"]
    # Append the earnings FAQ (low-KD "how much do cam models make" cluster).
    faq = list(c["faq"])
    if lang in EARNINGS_FAQ:
        faq.append(EARNINGS_FAQ[lang])
    depth = "../" if u["path"] else ""
    home = depth or "./"
    canon = f'{SITE}/{u["path"]}{MODEL_SLUG}/'
    og_image = f'{SITE}/assets/og/hub-{lang}.png'
    kw = (f"{c['h1short']}, cam model, webcam model, camgirl, "
          "how to become a cam model, cam model for beginners, splitcam")
    hreflang_html = "\n".join(
        f'<link rel="alternate" hreflang="{L}" href="{SITE}/{LANG_PATH[L]}{MODEL_SLUG}/">'
        for L in LANGS_AVAIL
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/{MODEL_SLUG}/">'

    steps_html = "".join(
        f'<div class="step"><div class="step-num">{i+1}</div><div class="step-body">'
        f'<div class="step-h">{e(head)}</div><p class="step-p">{body}</p></div></div>'
        for i, (head, body) in enumerate(c["steps"]))
    faq_html = "".join(
        f'<details class="faq-item"><summary>{e(q)}</summary><p>{a}</p></details>'
        for q, a in faq)

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": u["crumb_home"],
                 "item": f'{SITE}/{u["path"]}'},
                {"@type": "ListItem", "position": 2, "name": c["h1short"], "item": canon}]},
            {"@type": "HowTo", "name": _strip(c["h1html"]), "description": c["desc"],
             "inLanguage": lang, "datePublished": PUBLISHED_DATE, "dateModified": MODIFIED_DATE,
             "publisher": PUBLISHER,
             "step": [{"@type": "HowToStep", "position": i+1, "name": head,
                       "text": html.unescape(_strip(body))}
                      for i, (head, body) in enumerate(c["steps"])]},
            {"@type": "FAQPage", "inLanguage": lang, "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": html.unescape(_strip(a))}}
                for q, a in faq]},
        ],
    }
    return f"""<!DOCTYPE html>
<html lang="{u['lang']}"{" dir=\"rtl\"" if u['lang'] in RTL_LANGS else ""}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(c['title'])}</title>
<meta name="description" content="{e(c['desc'])}">
<meta name="keywords" content="{e(kw)}">
<link rel="canonical" href="{canon}">
{hreflang_html}
<link rel="icon" type="image/svg+xml" href="{depth}favicon.svg">
<link rel="icon" type="image/x-icon" href="{depth}favicon.ico">
<link rel="apple-touch-icon" href="{depth}apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{e(c['title'])}">
<meta property="og:description" content="{e(c['desc'])}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#141420">
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=1)}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
{LANG_REDIRECT_JS}
{AHREFS_JS}
</head>
<body>
{nav_html(home, u['home'], lang_switch(lang, depth))}
<div class="breadcrumbs">
  <a href="{home}">{u['crumb_home']}</a><span class="sep">/</span><span>{e(c['h1short'])}</span>
</div>
<section class="hero" style="padding-top:24px">
  <div class="hero-glow"></div>
  <h1 class="h1">{c['h1html']}</h1>
  <p class="sub">{c['intro']}</p>
  <div class="hero-cta">
    <a href="{e(DOWNLOAD_URL)}" class="btn-primary btn-lg" target="_blank" rel="nofollow noopener">⬇ {u['download']}</a>
    <a href="{home}" class="btn-ghost btn-lg">{u['home']}</a>
  </div>
</section>
<section class="section" id="steps">
  <h2 class="sec-h">{e(c['steps_h'])}</h2>
  <div class="steps">{steps_html}</div>
</section>
<section class="section">
  <h2 class="sec-h">{u['faq_h']}</h2>
  <div class="faq-list">{faq_html}</div>
</section>
<section class="cta-block">
  <h2>{u['cta_h']}</h2>
  <p>{u['cta_p']}</p>
  <a href="{e(DOWNLOAD_URL)}" class="btn-primary btn-lg" target="_blank" rel="nofollow noopener">⬇ {u['download']}</a>
</section>
<footer>
  <div class="footer-inner">
    <div>© 2026 {SITE_NAME} · <span class="age-tag-sm">18+</span></div>
    <div class="footer-links">
      <a href="{home}">{u['home']}</a>
      <a href="{depth}{MODEL_SLUG}/">{e(c['h1short'])}</a>
      <a href="{depth}{OBS_SLUG}/">{OBS_NAV.get(lang, "SplitCam vs OBS")}</a>
      <a href="{depth}about/">{u['about']}</a>
      <a href="{depth}contact/">{u['contact']}</a>
      <a href="{depth}privacy/">{u['privacy']}</a>
      <a href="{depth}terms/">{u['terms']}</a>
    </div>
  </div>
</footer>
<div class="sticky-dl" id="stickyDl"><a href="{e(DOWNLOAD_URL)}" target="_blank" rel="nofollow noopener">⬇ {u['download']}</a></div>
{STICKY_DL_JS}
</body>
</html>
"""


def render_obs_vs(lang):
    """Render the SplitCam-vs-OBS / OBS-alternative comparison page (indexable, SEO target)."""
    u = UI[lang]
    c = OBS_VS.get(lang) or OBS_VS["en"]
    depth = "../" if u["path"] else ""
    home = depth or "./"
    canon = f'{SITE}/{u["path"]}{OBS_SLUG}/'
    og_image = f'{SITE}/assets/og/hub-{lang}.png'
    # Keywords grounded in Ahrefs data: "obs alternative" (2300 global) + brand cluster.
    obs_kw = (f"obs alternative, splitcam vs obs, free obs alternative, {c['h1short']}, "
              "splitcam, obs studio alternative, obs alternative for cam streaming, "
              "multistream software")
    hreflang_html = "\n".join(
        f'<link rel="alternate" hreflang="{L}" href="{SITE}/{LANG_PATH[L]}{OBS_SLUG}/">'
        for L in LANGS_AVAIL
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/{OBS_SLUG}/">'

    rows_html = "".join(
        f'<tr><td>{e(feat)}</td><td>{e(sc)}</td><td>{e(obs)}</td></tr>'
        for feat, sc, obs in c["rows"])
    faq_html = "".join(
        f'<details class="faq-item"><summary>{e(q)}</summary><p>{a}</p></details>'
        for q, a in c["faq"])

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": u["crumb_home"],
                 "item": f'{SITE}/{u["path"]}'},
                {"@type": "ListItem", "position": 2, "name": c["h1short"], "item": canon}]},
            {"@type": "FAQPage", "inLanguage": lang, "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": html.unescape(_strip(a))}}
                for q, a in c["faq"]]},
            {"@type": "WebPage", "name": c["title"], "description": c["desc"],
             "url": canon, "inLanguage": lang, "datePublished": PUBLISHED_DATE,
             "dateModified": MODIFIED_DATE, "publisher": PUBLISHER},
        ],
    }
    return f"""<!DOCTYPE html>
<html lang="{u['lang']}"{" dir=\"rtl\"" if u['lang'] in RTL_LANGS else ""}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(c['title'])}</title>
<meta name="description" content="{e(c['desc'])}">
<meta name="keywords" content="{e(obs_kw)}">
<link rel="canonical" href="{canon}">
{hreflang_html}
<link rel="icon" type="image/svg+xml" href="{depth}favicon.svg">
<link rel="icon" type="image/x-icon" href="{depth}favicon.ico">
<link rel="apple-touch-icon" href="{depth}apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{e(c['title'])}">
<meta property="og:description" content="{e(c['desc'])}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#141420">
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=1)}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
{LANG_REDIRECT_JS}
{AHREFS_JS}
</head>
<body>
{nav_html(home, u['home'], lang_switch(lang, depth))}
<div class="breadcrumbs">
  <a href="{home}">{u['crumb_home']}</a><span class="sep">/</span><span>{e(c['h1short'])}</span>
</div>
<section class="hero" style="padding-top:24px">
  <div class="hero-glow"></div>
  <h1 class="h1">{c['h1html']}</h1>
  <p class="sub">{c['intro']}</p>
  <div class="hero-cta">
    <a href="{e(DOWNLOAD_URL)}" class="btn-primary btn-lg" target="_blank" rel="nofollow noopener">⬇ {u['download']}</a>
    <a href="{home}" class="btn-ghost btn-lg">{u['home']}</a>
  </div>
</section>
<section class="section">
  <h2 class="sec-h">{e(c['table_h'])}</h2>
  <div class="cmp-wrap"><table class="cmp">
    <thead><tr><th></th><th>{e(c['col_sc'])}</th><th>{e(c['col_obs'])}</th></tr></thead>
    <tbody>{rows_html}</tbody>
  </table></div>
  <div class="cmp-verdict"><strong style="display:block;font-size:17px;margin-bottom:8px">{e(c['verdict_h'])}</strong>{c['verdict']}</div>
</section>
<section class="section">
  <h2 class="sec-h">{u['faq_h']}</h2>
  <div class="faq-list">{faq_html}</div>
</section>
<section class="cta-block">
  <h2>{u['cta_h']}</h2>
  <p>{u['cta_p']}</p>
  <a href="{e(DOWNLOAD_URL)}" class="btn-primary btn-lg" target="_blank" rel="nofollow noopener">⬇ {u['download']}</a>
</section>
<footer>
  <div class="footer-inner">
    <div>© 2026 {SITE_NAME} · <span class="age-tag-sm">18+</span></div>
    <div class="footer-links">
      <a href="{home}">{u['home']}</a>
      <a href="{depth}{MODEL_SLUG}/">{e(MODEL_GUIDE.get(lang, MODEL_GUIDE["en"])["h1short"])}</a>
      <a href="{depth}{OBS_SLUG}/">{OBS_NAV.get(lang, "SplitCam vs OBS")}</a>
      <a href="{depth}about/">{u['about']}</a>
      <a href="{depth}contact/">{u['contact']}</a>
      <a href="{depth}privacy/">{u['privacy']}</a>
      <a href="{depth}terms/">{u['terms']}</a>
    </div>
  </div>
</footer>
<div class="sticky-dl" id="stickyDl"><a href="{e(DOWNLOAD_URL)}" target="_blank" rel="nofollow noopener">⬇ {u['download']}</a></div>
{STICKY_DL_JS}
</body>
</html>
"""


def render_404():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>404 — Page Not Found · {SITE_NAME}</title>
<meta name="robots" content="noindex">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<meta name="theme-color" content="#141420">
<style>{CSS}
.err-wrap{{min-height:60vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:120px 20px 60px}}
.err-code{{font-size:120px;font-weight:900;background:linear-gradient(135deg,var(--blue),var(--purple));-webkit-background-clip:text;background-clip:text;color:transparent;line-height:1}}
.err-msg{{font-size:22px;color:var(--text);margin:18px 0 8px}}
.err-sub{{color:var(--text-sub);font-size:15px;max-width:480px;margin-bottom:28px}}
</style>
{AHREFS_JS}
</head>
<body>
<nav>
  <a class="nav-home" href="/"><span class="dot"></span><span class="nav-home-t">All guides</span></a>
  <div class="nav-right"><a class="nav-brand" href="/">{SITE_NAME}</a></div>
</nav>
<div class="err-wrap">
  <div class="err-code">404</div>
  <div class="err-msg">Page not found</div>
  <div class="err-sub">The page you're looking for doesn't exist or has moved. Head back to the guides hub and pick a platform.</div>
  <a href="/" class="btn-primary btn-lg">← All streaming guides</a>
</div>
<footer>
  <div class="footer-inner">
    <div>© 2026 {SITE_NAME} · <span class="age-tag-sm">18+</span></div>
    <div class="footer-links">
      <a href="/">Home</a>
      <a href="/about/">About</a>
      <a href="/contact/">Contact</a>
      <a href="/privacy/">Privacy</a>
      <a href="/terms/">Terms</a>
    </div>
  </div>
</footer>
</body>
</html>
"""


def render_hub(platforms, lang):
    u = UI[lang]
    hb = HUB[lang]
    hub_depth = "../" if u["path"] else ""
    avail = [p for p in platforms if lang in p]
    # hub display order: these first, then the rest in natural order
    first = ["multistream-cams", "onlyfans", "mfc-alerts", "lovense"]
    ordered = ([p for s in first for p in avail if p["slug"] == s]
               + [p for p in avail if p["slug"] not in first])
    cards = "".join(
        f'<a class="related-card" href="{p["slug"]}/">'
        f'<img class="hub-card-icon" src="{hub_depth}logos/round/{p["slug"]}.png" alt="" loading="lazy">'
        f'<div class="hub-card-body"><h4>{e(p[lang]["h1short"])}</h4>'
        f'<p>{e(p[lang]["card"])}</p></div></a>' for p in ordered)
    canon = f'{SITE}/{u["path"]}'
    og_image = f'{SITE}/assets/og/hub-{lang}.png'
    # Keywords: localized lead phrase (from H1) + universal brand/tech terms.
    hub_kw = (f"{_strip(hb['h1'])}, splitcam, obs alternative, "
              "chaturbate, onlyfans, stripchat, bongacams, cam4, streamate, "
              "myfreecams, cam streaming")
    hreflang_html = "\n".join(
        f'<link rel="alternate" hreflang="{L}" href="{SITE}/{LANG_PATH[L]}">'
        for L in LANGS_AVAIL
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/">'
    hub_schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebSite", "name": SITE_NAME, "url": f"{SITE}/",
             "inLanguage": lang, "publisher": PUBLISHER},
            {"@type": "CollectionPage", "name": hb["title"],
             "description": hb["desc"], "url": canon,
             "inLanguage": lang, "datePublished": PUBLISHED_DATE,
             "dateModified": MODIFIED_DATE, "publisher": PUBLISHER,
             "mainEntity": {"@type": "ItemList", "numberOfItems": len(ordered),
                            "itemListElement": [
                {"@type": "ListItem", "position": i+1,
                 "url": f"{canon}{p['slug']}/",
                 "name": p[lang]["h1short"]}
                for i, p in enumerate(ordered)]}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": u["crumb_home"],
                 "item": canon}]},
        ],
    }
    return f"""<!DOCTYPE html>
<html lang="{u['lang']}"{" dir=\"rtl\"" if u['lang'] in RTL_LANGS else ""}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(hb['title'])}</title>
<meta name="description" content="{e(hb['desc'])}">
<meta name="keywords" content="{e(hub_kw)}">
<link rel="canonical" href="{canon}">
{hreflang_html}
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/svg+xml" href="{hub_depth}favicon.svg">
<link rel="icon" type="image/x-icon" href="{hub_depth}favicon.ico">
<link rel="apple-touch-icon" href="{hub_depth}apple-touch-icon.png">
<!-- <meta name="google-site-verification" content="YOUR-GSC-TOKEN"> -->
<!-- <meta name="msvalidate.01" content="YOUR-BING-TOKEN"> -->
<!-- <meta name="yandex-verification" content="YOUR-YANDEX-TOKEN"> -->
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{e(hb['title'])}">
<meta property="og:description" content="{e(hb['desc'])}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(hb['title'])}">
<meta name="twitter:description" content="{e(hb['desc'])}">
<meta name="twitter:image" content="{og_image}">
<meta name="theme-color" content="#141420">
<script type="application/ld+json">
{json.dumps(hub_schema, ensure_ascii=False, indent=1)}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
{LANG_REDIRECT_JS}
{AHREFS_JS}
</head>
<body>
{nav_html("./", u['home'], lang_switch(lang, hub_depth))}
<section class="hero" style="padding-top:96px">
  <div class="hero-glow"></div>
  <h1 class="h1">{hb['h1']}</h1>
  <p class="sub">{e(hb['sub'])}</p>
</section>
<section class="section">
  <h2 class="sec-h">{e(hb['pick'])}</h2>
  <div class="hub-grid">{cards}</div>
</section>
<footer>
  <div class="footer-inner">
    <div>© 2026 {SITE_NAME} · <span class="age-tag-sm">18+</span></div>
    <div class="footer-links">
      <a href="./">{u['home']}</a>
      <a href="{MODEL_SLUG}/">{e(MODEL_GUIDE.get(lang, MODEL_GUIDE["en"])["h1short"])}</a>
      <a href="{OBS_SLUG}/">{OBS_NAV.get(lang, "SplitCam vs OBS")}</a>
      <a href="about/">{u['about']}</a>
      <a href="contact/">{u['contact']}</a>
      <a href="privacy/">{u['privacy']}</a>
      <a href="terms/">{u['terms']}</a>
    </div>
  </div>
</footer>
<div class="sticky-dl" id="stickyDl"><a href="{e(DOWNLOAD_URL)}" target="_blank" rel="nofollow noopener">⬇ {u['download']}</a></div>
{STICKY_DL_JS}
</body>
</html>
"""


def main():
    global LANGS_AVAIL
    from platforms_en import PLATFORMS_EN
    langs_data = {"en": PLATFORMS_EN}
    for code in ("ru", "es", "de", "fr", "it", "pt", "nl",
                 "ro", "bg", "hu", "el", "fi", "da", "no", "sr", "hr",
                 "zh", "ja", "ar", "th", "fil", "tr", "id", "vi", "pl", "ko", "uk", "cs", "sk", "sv", "ms", "he", "fa", "hi"):
        try:
            mod = __import__(f"platforms_{code}", fromlist=[f"PLATFORMS_{code.upper()}"])
            langs_data[code] = getattr(mod, f"PLATFORMS_{code.upper()}")
        except ImportError:
            pass
    LANGS_AVAIL = list(langs_data.keys())

    # merge into one list of platform dicts keyed by lang
    by_slug = {}
    for lang, plist in langs_data.items():
        for p in plist:
            slug = p["slug"]
            by_slug.setdefault(slug, {"slug": slug, "name": p["name"]})
            by_slug[slug][lang] = p
    platforms = list(by_slug.values())

    count = 0
    for lang in langs_data:
        avail = [p for p in platforms if lang in p]
        for p in avail:
            u = UI[lang]
            outdir = ROOT / u["path"] / p["slug"]
            outdir.mkdir(parents=True, exist_ok=True)
            (outdir / "index.html").write_text(render(p, lang, avail), encoding="utf-8")
            count += 1
        # hub page for this language
        u = UI[lang]
        hubdir = ROOT / u["path"] if u["path"] else ROOT
        hubdir.mkdir(parents=True, exist_ok=True)
        (hubdir / "index.html").write_text(render_hub(platforms, lang), encoding="utf-8")
        count += 1

        # legal pages for this language
        for slug in ("about", "privacy", "terms", "contact"):
            legaldir = ROOT / u["path"] / slug
            legaldir.mkdir(parents=True, exist_ok=True)
            (legaldir / "index.html").write_text(render_legal(slug, lang), encoding="utf-8")
            count += 1

        # OBS-alternative comparison page (indexable SEO target)
        obsdir = ROOT / u["path"] / OBS_SLUG
        obsdir.mkdir(parents=True, exist_ok=True)
        (obsdir / "index.html").write_text(render_obs_vs(lang), encoding="utf-8")
        count += 1

        # "How to become a cam model" top-funnel page (indexable SEO target)
        modeldir = ROOT / u["path"] / MODEL_SLUG
        modeldir.mkdir(parents=True, exist_ok=True)
        (modeldir / "index.html").write_text(render_model_guide(lang), encoding="utf-8")
        count += 1

    # 404 page (root)
    (ROOT / "404.html").write_text(render_404(), encoding="utf-8")

    # ---- sitemap.xml with hreflang alternates ----
    def alt_links(slug=None):
        out = []
        for L in langs_data:
            href = f'{SITE}/{LANG_PATH[L]}{slug + "/" if slug else ""}'
            out.append(f'    <xhtml:link rel="alternate" hreflang="{L}" href="{href}"/>')
        out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/{slug + "/" if slug else ""}"/>')
        return "\n".join(out)

    urls = []
    today = MODIFIED_DATE
    for lang in langs_data:
        # hub
        loc = f'{SITE}/{LANG_PATH[lang]}'
        urls.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n'
                    f'    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n'
                    f'{alt_links()}\n  </url>')
        for p in [p for p in platforms if lang in p]:
            loc = f'{SITE}/{LANG_PATH[lang]}{p["slug"]}/'
            urls.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n'
                        f'    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n'
                        f'{alt_links(p["slug"])}\n  </url>')
        for slug in ("about", "privacy", "terms", "contact"):
            loc = f'{SITE}/{LANG_PATH[lang]}{slug}/'
            urls.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n'
                        f'    <changefreq>yearly</changefreq>\n    <priority>0.3</priority>\n'
                        f'{alt_links(slug)}\n  </url>')
        # OBS-alternative comparison page
        loc = f'{SITE}/{LANG_PATH[lang]}{OBS_SLUG}/'
        urls.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n'
                    f'    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n'
                    f'{alt_links(OBS_SLUG)}\n  </url>')
        # become-a-cam-model top-funnel page
        loc = f'{SITE}/{LANG_PATH[lang]}{MODEL_SLUG}/'
        urls.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n'
                    f'    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n'
                    f'{alt_links(MODEL_SLUG)}\n  </url>')
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
               'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
               + "\n".join(urls) + "\n</urlset>\n")
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")

    # ---- robots.txt ----
    robots = ("User-agent: *\nAllow: /\n\n"
              f"Sitemap: {SITE}/sitemap.xml\n")
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")

    print(f"Generated {count} pages across {len(langs_data)} language(s); "
          f"sitemap.xml ({len(urls)} URLs) + robots.txt written.")


if __name__ == "__main__":
    main()
