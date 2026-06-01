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
    "fil": "SplitCam vs OBS", "tr": "SplitCam vs OBS", "id": "SplitCam vs OBS",
}
SITE = "https://camstreamguide.com"
DOWNLOAD_URL = "https://splitcam.com/download"   # software download (decision point — see README)
SITE_NAME = "Streaming Guides"
PUBLISHED_DATE = "2026-05-21"
MODIFIED_DATE = datetime.date.today().isoformat()
OG_LOCALE = {"en": "en_US", "ru": "ru_RU", "es": "es_ES",
             "de": "de_DE", "fr": "fr_FR", "it": "it_IT",
             "pt": "pt_BR", "nl": "nl_NL",
             "ro": "ro_RO", "bg": "bg_BG", "hu": "hu_HU",
             "el": "el_GR", "fi": "fi_FI", "da": "da_DK",
             "no": "nb_NO", "sr": "sr_RS", "hr": "hr_HR",
             "zh": "zh_CN", "ja": "ja_JP", "ar": "ar_AR",
             "th": "th_TH", "fil": "fil_PH", "tr": "tr_TR", "id": "id_ID"}
LANGS_AVAIL = ["en", "ru", "es", "de", "fr", "it", "pt", "nl",
               "ro", "bg", "hu", "el", "fi", "da", "no", "sr", "hr",
               "zh", "ja", "ar", "th", "fil", "tr", "id"]  # set by main() to those with platforms_<lang>.py
RTL_LANGS = {"ar"}  # languages that need dir="rtl" on <html>


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
.nav-logo{display:flex;align-items:center;gap:9px;font-size:20px;font-weight:700;letter-spacing:.3px}
.nav-logo .dot{width:11px;height:11px;border-radius:50%;
background:linear-gradient(135deg,var(--blue),var(--purple))}
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
              "zh": "中", "ja": "日", "ar": "ع", "th": "ไทย", "fil": "FIL", "tr": "TR", "id": "ID"}
LANG_FLAG = {"en": "🇬🇧", "ru": "🇷🇺", "es": "🇪🇸", "de": "🇩🇪", "fr": "🇫🇷", "it": "🇮🇹",
             "pt": "🇧🇷", "nl": "🇳🇱", "ro": "🇷🇴", "bg": "🇧🇬", "hu": "🇭🇺",
             "el": "🇬🇷", "fi": "🇫🇮", "da": "🇩🇰", "no": "🇳🇴", "sr": "🇷🇸", "hr": "🇭🇷",
             "zh": "🇨🇳", "ja": "🇯🇵", "ar": "🇸🇦", "th": "🇹🇭", "fil": "🇵🇭", "tr": "🇹🇷", "id": "🇮🇩"}
LANG_NATIVE = {"en": "English", "ru": "Русский", "es": "Español", "de": "Deutsch",
               "fr": "Français", "it": "Italiano", "pt": "Português", "nl": "Nederlands",
               "ro": "Română", "bg": "Български", "hu": "Magyar", "el": "Ελληνικά",
               "fi": "Suomi", "da": "Dansk", "no": "Norsk", "sr": "Српски", "hr": "Hrvatski",
               "zh": "中文", "ja": "日本語", "ar": "العربية", "th": "ไทย", "fil": "Filipino",
               "tr": "Türkçe", "id": "Bahasa Indonesia"}
LANG_PATH = {"en": "", "ru": "ru/", "es": "es/", "de": "de/", "fr": "fr/", "it": "it/",
             "pt": "pt/", "nl": "nl/", "ro": "ro/", "bg": "bg/", "hu": "hu/",
             "el": "el/", "fi": "fi/", "da": "da/", "no": "no/", "sr": "sr/", "hr": "hr/",
             "zh": "zh/", "ja": "ja/", "ar": "ar/", "th": "th/", "fil": "fil/", "tr": "tr/", "id": "id/"}


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
           "th": "คู่มือวิดีโอ", "fil": "Gabay sa video", "tr": "Video rehberi", "id": "Panduan video"}
COLLAB_LABEL = {"en": "Setup guide", "ru": "Гайд по настройке", "es": "Guía de configuración",
                "de": "Setup-Anleitung", "fr": "Guide d'installation", "it": "Guida alla configurazione",
                "pt": "Guia de configuração", "nl": "Installatiegids",
                "ro": "Ghid de configurare", "bg": "Ръководство за настройка",
                "hu": "Beállítási útmutató", "el": "Οδηγός εγκατάστασης",
                "fi": "Asennusohje", "da": "Opsætningsguide", "no": "Oppsettsguide",
                "sr": "Водич за подешавање", "hr": "Vodič za postavljanje",
                "zh": "设置指南", "ja": "セットアップガイド", "ar": "دليل الإعداد",
                "th": "คู่มือการตั้งค่า", "fil": "Gabay sa setup", "tr": "Kurulum rehberi", "id": "Panduan setup"}

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
<nav>
  <a class="nav-logo" href="{home}"><span class="dot"></span>{SITE_NAME}</a>
  <ul class="nav-links">
    <li><a href="{home}">{u['home']}</a></li>
  </ul>
  {lang_switch(lang, depth, p['slug'])}
</nav>
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
<nav>
  <a class="nav-logo" href="{home}"><span class="dot"></span>{SITE_NAME}</a>
  <ul class="nav-links"><li><a href="{home}">{u['home']}</a></li></ul>
  {lang_switch(lang, depth)}
</nav>
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
<nav>
  <a class="nav-logo" href="{home}"><span class="dot"></span>{SITE_NAME}</a>
  <ul class="nav-links"><li><a href="{home}">{u['home']}</a></li></ul>
  {lang_switch(lang, depth)}
</nav>
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
<nav>
  <a class="nav-logo" href="{home}"><span class="dot"></span>{SITE_NAME}</a>
  <ul class="nav-links"><li><a href="{home}">{u['home']}</a></li></ul>
  {lang_switch(lang, depth)}
</nav>
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
  <a class="nav-logo" href="/"><span class="dot"></span>{SITE_NAME}</a>
  <ul class="nav-links"><li><a href="/">All guides</a></li></ul>
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
<nav>
  <a class="nav-logo" href="./"><span class="dot"></span>{SITE_NAME}</a>
  <ul class="nav-links"><li><a href="./">{u['home']}</a></li></ul>
  {lang_switch(lang, hub_depth)}
</nav>
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
                 "zh", "ja", "ar", "th", "fil", "tr", "id"):
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
