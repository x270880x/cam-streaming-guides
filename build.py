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
OG_LOCALE = {"en": "en_US", "ru": "ru_RU", "es": "es_ES"}
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


LANG_LABEL = {"en": "EN", "ru": "RU", "es": "ES"}
LANG_PATH = {"en": "", "ru": "ru/", "es": "es/"}


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
VIDEO_H = {"en": "Video guide", "ru": "Видео-гайд", "es": "Guía en vídeo"}
COLLAB_LABEL = {"en": "Setup guide", "ru": "Гайд по настройке", "es": "Guía de configuración"}

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
    for L in ("en", "ru", "es"):
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
        for L in ("en", "ru", "es")
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
        for L in ("en", "ru", "es")
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
        for L in ("en", "ru", "es")
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
    from platforms_en import PLATFORMS_EN
    langs_data = {"en": PLATFORMS_EN}
    try:
        from platforms_ru import PLATFORMS_RU
        langs_data["ru"] = PLATFORMS_RU
    except ImportError:
        pass
    try:
        from platforms_es import PLATFORMS_ES
        langs_data["es"] = PLATFORMS_ES
    except ImportError:
        pass

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
