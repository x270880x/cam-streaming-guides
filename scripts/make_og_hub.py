# -*- coding: utf-8 -*-
"""Generate rich hub OG banners (1200x630) for every language — "poster" style.

Design:
  - diagonal dark gradient + soft accent radial glow
  - "● LIVE" pill (top-left), SplitCam logo + wordmark (top-right)
  - heavy auto-fit headline: line 1 white, line 2 on an accent "marker" highlight
  - subtitle line
  - strip of REAL round platform logos along the bottom (proof of breadth)
  - brand wordmark (bottom-right)

Messaging pitches the SOFTWARE (free, multistream, beauty effects) AND the
guides (setup guides for 19 platforms). Per-language text in HUB_OG below.

Arabic is reshaped + bidi-ordered (pure-python arabic_reshaper + python-bidi)
and right-aligned. CJK/Thai use script-capable fonts.

Run:  python3 scripts/make_og_hub.py            # all languages
      python3 scripts/make_og_hub.py ko en ar   # only these
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "og")
ROUND = os.path.join(ROOT, "logos", "round")
SPLITCAM_LOGO = os.path.join(ROOT, "assets", "splitcam.png")

W, H = 1200, 630
ACCENT = (217, 70, 239)
WHITE = (255, 255, 255)
SUB = (203, 213, 225)
BRAND = "camstreamguide.com"
MARGIN = 80
MAXW = W - 2 * MARGIN

STRIP = ["chaturbate", "stripchat", "bongacams", "cam4", "onlyfans",
         "camsoda", "streamate", "flirt4free", "imlive"]

SF = "/System/Library/Fonts/Supplemental/"
SYS = "/System/Library/Fonts/"

# (path, ttc_index) candidates per script; first that loads wins.
FONTS = {
    "latin": [(SF + "Arial Black.ttf", 0), (SYS + "HelveticaNeue.ttc", 0), (SF + "Arial Bold.ttf", 0)],
    "latin_bold": [(SF + "Arial Bold.ttf", 0), (SYS + "HelveticaNeue.ttc", 0)],
    # Vietnamese + Cyrillic + Greek: Arial Black lacks full coverage → use Arial Bold (broad coverage)
    "wide": [(SF + "Arial Bold.ttf", 0), (SYS + "HelveticaNeue.ttc", 0), ("/Library/Fonts/Arial Unicode.ttf", 0)],
    "ko": [(SYS + "AppleSDGothicNeo.ttc", 1), (SYS + "AppleSDGothicNeo.ttc", 0)],
    "zh": [(SYS + "Hiragino Sans GB.ttc", 1), (SYS + "Hiragino Sans GB.ttc", 0), ("/Library/Fonts/Arial Unicode.ttf", 0)],
    "ja": [(SYS + "Hiragino Sans GB.ttc", 1), (SYS + "Hiragino Sans GB.ttc", 0), ("/Library/Fonts/Arial Unicode.ttf", 0)],
    "th": [(SF + "Silom.ttf", 0), ("/Library/Fonts/Arial Unicode.ttf", 0)],
    "ar": [("/Library/Fonts/Arial Unicode.ttf", 0), (SF + "Arial Unicode.ttf", 0)],
}
SCRIPT_LANG = {"ko": "ko", "zh": "zh", "ja": "ja", "th": "th", "ar": "ar"}
# Latin-script langs whose glyphs Arial Black does not fully cover → use the "wide" bold font
WIDE_LANG = {"vi", "ru", "bg", "sr", "el"}
RTL = {"ar"}


def _load(key, size):
    for path, idx in FONTS[key]:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size, index=idx)
            except Exception:
                try:
                    return ImageFont.truetype(path, size)
                except Exception:
                    continue
    return ImageFont.load_default()


def disp_font(lang, size):
    if lang in SCRIPT_LANG:
        return _load(SCRIPT_LANG[lang], size)
    if lang in WIDE_LANG:
        return _load("wide", size)
    return _load("latin", size)


def sub_font(lang, size):
    key = SCRIPT_LANG.get(lang)
    return _load(key, size) if key else _load("latin_bold", size)


def shape(lang, s):
    if lang in RTL:
        import arabic_reshaper
        from bidi.algorithm import get_display
        return get_display(arabic_reshaper.reshape(s))
    return s


def gradient_bg():
    img = Image.new("RGB", (W, H))
    px = img.load()
    c1, c2, c3 = (12, 18, 38), (40, 38, 110), (95, 30, 140)
    for y in range(H):
        t = y / H
        if t < 0.5:
            tt = t / 0.5
            col = tuple(int(c1[i] + (c2[i] - c1[i]) * tt) for i in range(3))
        else:
            tt = (t - 0.5) / 0.5
            col = tuple(int(c2[i] + (c3[i] - c2[i]) * tt) for i in range(3))
        for x in range(W):
            px[x, y] = col
    return img


def add_glow(img, cx, cy, radius, color, strength=95):
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    ImageDraw.Draw(glow).ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=color)
    glow = glow.filter(ImageFilter.GaussianBlur(radius // 2))
    base, gl = img.load(), glow.load()
    f = strength / 255.0
    for y in range(H):
        for x in range(W):
            b, g = base[x, y], gl[x, y]
            base[x, y] = tuple(min(255, int(b[i] + g[i] * f)) for i in range(3))
    return img


def tw(d, s, f):
    bb = d.textbbox((0, 0), s, font=f)
    return bb[2] - bb[0]


def fit(d, s, lang, start, mins):
    sz = start
    while sz > mins:
        f = disp_font(lang, sz)
        if tw(d, s, f) <= MAXW:
            return f
        sz -= 2
    return disp_font(lang, mins)


def make_banner(lang, line1, line2, sub):
    rtl = lang in RTL
    l1, l2, subt = shape(lang, line1), shape(lang, line2), shape(lang, sub)

    img = gradient_bg()
    img = add_glow(img, 600, 300, 420, (140, 40, 180), 95)
    img = add_glow(img, 1000, 120, 240, (90, 70, 200), 60)
    d = ImageDraw.Draw(img, "RGBA")

    # LIVE pill (top-left, always LTR)
    f_live = _load("latin", 24)
    txt = "LIVE"
    pad, dot, ph = 22, 8, 48
    lw = tw(d, txt, f_live)
    pw = pad + dot * 2 + 14 + lw + pad
    x0, y0 = MARGIN, 70
    d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=ph // 2, fill=(255, 255, 255, 28))
    d.ellipse([x0 + pad, y0 + ph // 2 - dot, x0 + pad + dot * 2, y0 + ph // 2 + dot], fill=(244, 63, 94))
    d.text((x0 + pad + dot * 2 + 14, y0 + ph // 2), txt, font=f_live, fill=WHITE, anchor="lm")

    # SplitCam logo + wordmark (top-right)
    try:
        logo = Image.open(SPLITCAM_LOGO).convert("RGBA").resize((60, 60), Image.LANCZOS)
        f_wm = _load("latin_bold", 28)
        wm = "SplitCam"
        ww = tw(d, wm, f_wm)
        rx = W - MARGIN - (60 + 12 + ww)
        img.paste(logo, (rx, 66), logo)
        d.text((rx + 60 + 12, 66 + 30), wm, font=f_wm, fill=WHITE, anchor="lm")
    except Exception:
        pass

    # Headline (two lines, auto-fit)
    ax = (W - MARGIN) if rtl else MARGIN
    anc = "ra" if rtl else "la"
    f1 = fit(d, l1, lang, 84, 50)
    y = 178
    d.text((ax, y), l1, font=f1, fill=WHITE, anchor=anc)
    bb = d.textbbox((ax, y), l1, font=f1, anchor=anc)
    f2 = fit(d, l2, lang, 84, 50)
    y2 = bb[3] + 12
    bb2 = d.textbbox((ax, y2), l2, font=f2, anchor=anc)
    p = 16
    d.rounded_rectangle([bb2[0] - p, y2 + 6, bb2[2] + p, bb2[3] + 12], radius=12, fill=(217, 70, 239, 235))
    d.text((ax, y2), l2, font=f2, fill=WHITE, anchor=anc)

    # Subtitle
    fs = fit(d, subt, lang, 32, 22) if tw(d, subt, sub_font(lang, 32)) > MAXW else sub_font(lang, 32)
    ys = bb2[3] + 40
    d.text((ax, ys), subt, font=fs, fill=SUB, anchor=anc)

    # Platform logo strip (bottom)
    size = 72
    gap = 16
    sy = H - 56 - size
    for i, slug in enumerate(STRIP):
        p = os.path.join(ROUND, slug + ".png")
        if not os.path.exists(p):
            continue
        lg = Image.open(p).convert("RGBA").resize((size, size), Image.LANCZOS)
        img.paste(lg, (MARGIN + i * (size + gap), sy), lg)

    # Brand (bottom-right)
    d = ImageDraw.Draw(img, "RGBA")
    f_brand = _load("latin_bold", 26)
    bw = tw(d, BRAND, f_brand)
    d.text((W - MARGIN - bw, H - 50), BRAND, font=f_brand, fill=(226, 232, 240))

    img.save(os.path.join(OUT, f"hub-{lang}.png"), "PNG", optimize=True)
    return f"hub-{lang}.png"


# (line1 white, line2 accent/marker, subtitle) — software pitch + guides
HUB_OG = {
    "en": ("Free cam streaming software", "Multistream · beauty effects", "Setup guides for 19 platforms · no watermark"),
    "ru": ("Бесплатный софт для cam-стриминга", "Мультистрим · бьюти-эффекты", "Гайды по 19 платформам · без водяного знака"),
    "es": ("Software gratis de cam streaming", "Multistream · efectos beauty", "Guías para 19 plataformas · sin marca de agua"),
    "de": ("Kostenlose Cam-Streaming-Software", "Multistream · Beauty-Effekte", "Anleitungen für 19 Plattformen · ohne Wasserzeichen"),
    "fr": ("Logiciel de cam streaming gratuit", "Multistream · effets beauté", "Guides pour 19 plateformes · sans filigrane"),
    "it": ("Software gratis di cam streaming", "Multistream · effetti beauty", "Guide per 19 piattaforme · senza watermark"),
    "pt": ("Software grátis de cam streaming", "Multistream · efeitos beauty", "Guias para 19 plataformas · sem marca d'água"),
    "nl": ("Gratis cam-streaming-software", "Multistream · beauty-effecten", "Gidsen voor 19 platforms · geen watermerk"),
    "ro": ("Software gratuit de cam streaming", "Multistream · efecte beauty", "Ghiduri pentru 19 platforme · fără watermark"),
    "bg": ("Безплатен софтуер за cam стрийминг", "Мултистрийм · бюти ефекти", "Ръководства за 19 платформи · без воден знак"),
    "hu": ("Ingyenes cam streaming szoftver", "Multistream · beauty effektek", "Útmutatók 19 platformhoz · vízjel nélkül"),
    "el": ("Δωρεάν λογισμικό cam streaming", "Multistream · εφέ beauty", "Οδηγοί για 19 πλατφόρμες · χωρίς υδατογράφημα"),
    "fi": ("Ilmainen cam-striimausohjelmisto", "Multistream · beauty-efektit", "Oppaat 19 alustalle · ei vesileimaa"),
    "da": ("Gratis cam-streaming-software", "Multistream · beauty-effekter", "Guides til 19 platforme · uden vandmærke"),
    "no": ("Gratis cam-streaming-programvare", "Multistream · beauty-effekter", "Guider for 19 plattformer · uten vannmerke"),
    "sr": ("Besplatan softver za cam striming", "Multistrim · beauty efekti", "Vodiči za 19 platformi · bez vodenog žiga"),
    "hr": ("Besplatan softver za cam streaming", "Multistream · beauty efekti", "Vodiči za 19 platformi · bez vodenog žiga"),
    "zh": ("免费直播推流软件", "多平台同步推流 · 美颜特效", "19 个平台设置指南 · 无水印"),
    "ja": ("無料カム配信ソフト", "マルチ配信 · 美顔エフェクト", "19 プラットフォームの設定ガイド · 透かしなし"),
    "ar": ("برنامج بث كام مجاني", "بث متعدد · مؤثرات تجميل", "أدلة إعداد لـ 19 منصة · بلا علامة مائية"),
    "th": ("ซอฟต์แวร์สตรีมแคมฟรี", "มัลติสตรีม · เอฟเฟกต์บิวตี้", "คู่มือตั้งค่า 19 แพลตฟอร์ม · ไม่มีลายน้ำ"),
    "fil": ("Libreng cam streaming software", "Multistream · beauty effects", "Mga gabay para sa 19 platform · walang watermark"),
    "tr": ("Ücretsiz cam yayın yazılımı", "Çoklu yayın · güzellik efektleri", "19 platform için kurulum rehberi · filigran yok"),
    "id": ("Software cam streaming gratis", "Multistream · efek kecantikan", "Panduan setup 19 platform · tanpa watermark"),
    "vi": ("Phần mềm phát cam miễn phí", "Đa nền tảng · hiệu ứng làm đẹp", "Hướng dẫn cho 19 nền tảng · không watermark"),
    "pl": ("Darmowy program do cam streamingu", "Multistream · efekty beauty", "Poradniki dla 19 platform · bez znaku wodnego"),
    "ko": ("무료 캠 스트리밍 소프트웨어", "멀티스트리밍 · 뷰티 효과", "19개 플랫폼 설정 가이드 · 워터마크 없음"),
}


if __name__ == "__main__":
    only = sys.argv[1:] or None
    done = []
    for lang, (l1, l2, sub) in HUB_OG.items():
        if only and lang not in only:
            continue
        done.append(make_banner(lang, l1, l2, sub))
    print("Wrote", len(done), "banners:", ", ".join(done))
