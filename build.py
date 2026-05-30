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

ROOT = Path(__file__).parent
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
             "no": "nb_NO", "sr": "sr_RS", "hr": "hr_HR"}
LANGS_AVAIL = ["en", "ru", "es", "de", "fr", "it", "pt", "nl",
               "ro", "bg", "hu", "el", "fi", "da", "no", "sr", "hr"]  # set by main() to those with platforms_<lang>.py
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
.lang-switch{display:flex;border:1px solid var(--app-border2);border-radius:8px;overflow:hidden;flex-shrink:0}
.lang-switch a{padding:7px 11px;font-size:12px;font-weight:600;color:var(--text-sub);transition:all .15s}
.lang-switch a:hover{color:var(--text);background:rgba(255,255,255,.04)}
.lang-switch a.cur{background:var(--blue);color:#fff}
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


LANG_LABEL = {"en": "EN", "ru": "RU", "es": "ES", "de": "DE", "fr": "FR", "it": "IT",
              "pt": "PT", "nl": "NL", "ro": "RO", "bg": "BG", "hu": "HU",
              "el": "EL", "fi": "FI", "da": "DA", "no": "NO", "sr": "SR", "hr": "HR"}
LANG_PATH = {"en": "", "ru": "ru/", "es": "es/", "de": "de/", "fr": "fr/", "it": "it/",
             "pt": "pt/", "nl": "nl/", "ro": "ro/", "bg": "bg/", "hu": "hu/",
             "el": "el/", "fi": "fi/", "da": "da/", "no": "no/", "sr": "sr/", "hr": "hr/"}


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
           "no": "Videoguide", "sr": "Видео водич", "hr": "Video vodič"}
COLLAB_LABEL = {"en": "Setup guide", "ru": "Гайд по настройке", "es": "Guía de configuración",
                "de": "Setup-Anleitung", "fr": "Guide d'installation", "it": "Guida alla configurazione",
                "pt": "Guia de configuração", "nl": "Installatiegids",
                "ro": "Ghid de configurare", "bg": "Ръководство за настройка",
                "hu": "Beállítási útmutató", "el": "Οδηγός εγκατάστασης",
                "fi": "Asennusohje", "da": "Opsætningsguide", "no": "Oppsettsguide",
                "sr": "Водич за подешавање", "hr": "Vodič za postavljanje"}

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
    for L in LANGS_AVAIL:
        if slug:
            href = f"{depth}{LANG_PATH[L]}{slug}/"
        else:
            href = f"{depth}{LANG_PATH[L]}" or "./"
        cls = ' class="cur"' if L == cur else ""
        items.append(f'<a href="{href}"{cls}>{LANG_LABEL[L]}</a>')
    return '<div class="lang-switch">' + "".join(items) + "</div>"


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
                for q, a in d["faq"]]},
            {"@type": "SoftwareApplication", "name": "SplitCam",
             "applicationCategory": "MultimediaApplication",
             "operatingSystem": "Windows, macOS",
             "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
        ],
    }

    return f"""<!DOCTYPE html>
<html lang="{u['lang']}">
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
<section class="section">
  <h2 class="sec-h">{u['faq_h']}</h2>
  <div class="faq-list">{faq_html}</div>
</section>
<div class="section">
  <h3 style="font-size:17px;font-weight:700;margin-bottom:4px">{u['related']}</h3>
  <div class="related-grid">{related}</div>
</div>
<section class="cta-block">
  <h2>{u['cta_h']}</h2>
  <p>{u['cta_p']}</p>
  <a href="{e(DOWNLOAD_URL)}" class="btn-primary btn-lg" target="_blank" rel="nofollow noopener">⬇ {u['download']}</a>
</section>
<div class="section meta-line">
  <span class="age-tag">18+</span>
  <span>{u['updated']}: <time datetime="{MODIFIED_DATE}">{MODIFIED_DATE}</time></span>
</div>
<footer>
  <div class="footer-inner">
    <div>© 2026 {SITE_NAME} · <span class="age-tag-sm">18+</span></div>
    <div class="footer-links">
      <a href="{home}">{u['home']}</a>
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
<html lang="{u['lang']}">
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
  <p style="margin-top:32px;color:var(--text-sub);font-size:13px">
    <span class="age-tag">18+</span> &nbsp; {u['updated']}: <time datetime="{MODIFIED_DATE}">{MODIFIED_DATE}</time>
  </p>
</section>
<footer>
  <div class="footer-inner">
    <div>© 2026 {SITE_NAME} · <span class="age-tag-sm">18+</span></div>
    <div class="footer-links">
      <a href="{home}">{u['home']}</a>
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
        f'<img class="hub-card-icon" src="logos/round/{p["slug"]}.png" alt="">'
        f'<div class="hub-card-body"><h4>{e(p[lang]["h1short"])}</h4>'
        f'<p>{e(p[lang]["card"])}</p></div></a>' for p in ordered)
    canon = f'{SITE}/{u["path"]}'
    og_image = f'{SITE}/assets/og/hub-{lang}.png'
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
<html lang="{u['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(hb['title'])}</title>
<meta name="description" content="{e(hb['desc'])}">
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
      <a href="about/">{u['about']}</a>
      <a href="contact/">{u['contact']}</a>
      <a href="privacy/">{u['privacy']}</a>
      <a href="terms/">{u['terms']}</a>
    </div>
  </div>
</footer>
</body>
</html>
"""


def main():
    global LANGS_AVAIL
    from platforms_en import PLATFORMS_EN
    langs_data = {"en": PLATFORMS_EN}
    for code in ("ru", "es", "de", "fr", "it", "pt", "nl",
                 "ro", "bg", "hu", "el", "fi", "da", "no", "sr", "hr"):
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
