# -*- coding: utf-8 -*-
LOVENSE_METHODS_CS = {
    "heading": "Nastavení Lovense ve SplitCamu — 3 kroky",
    "lead": "Přesně kopíruje oficiální třífázové nastavení od Lovense. <strong>Cam Extension</strong> "
            "načítá dýška z tvého cam webu, <strong>Lovense Connect</strong> je Bluetooth můstek k tvé "
            "hračce a <strong>SplitCam Toolset</strong> vloží překryv Lovense přímo do SplitCamu, který "
            "vysílá přes RTMP. Všechno je zdarma; tlačítka ke stažení se automaticky přizpůsobí tvému "
            "systému.",
    "stage_word": "Krok",
    "get_label": "Stáhnout",
    "do_label": "Potom",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Načítá dýška z tvého cam webu — instaluje se do Chromu nebo Edge.",
            "get": ["camext"],
            "steps": [
                "Stáhni Cam Extension a rozbal ho.",
                "Otevři <strong>chrome://extensions</strong> (nebo <strong>edge://extensions</strong>), "
                "vpravo nahoře zapni <strong>Developer mode</strong>, klikni na <strong>Load unpacked</strong> "
                "a vyber rozbalenou složku <em>lovense_cam</em>.",
                "Klikni na ikonu Lovense na liště a přihlas se svým účtem Lovense.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Můstek, který komunikuje s tvou hračkou přes Bluetooth.",
            "get": ["connect"],
            "steps": [
                "Na počítači: nainstaluj Lovense Connect (doporučujeme USB Bluetooth adaptér od Lovense). "
                "Na telefonu: stáhni aplikaci Lovense Connect z Google Play nebo App Store.",
                "Zapni hračku a spáruj ji v Connectu, dokud se nezobrazí jako připojená. V mobilní "
                "aplikaci naskenuj QR kód zobrazený na počítači a propoj je.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Zobrazí překryv Lovense ve SplitCamu a vysílá tvůj stream.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Nainstaluj SplitCam a pak nainstaluj Lovense SplitCam Toolset — plugin, který přidá "
                "překryv Lovense do SplitCamu.",
                "V Cam Extension klikni na <strong>+</strong>, přidej svůj cam web (Chaturbate, "
                "Stripchat, …) a nastav si tip menu, pak otevři záložku <strong>Video Feedback</strong> "
                "a ze seznamu vyber <strong>SplitCam</strong> (OBS / SplitCam / Streamster).",
                "Ve SplitCamu přidej zdroj <strong>Lovense</strong>, který Toolset zaregistroval — na "
                "scéně se objeví překryv s tip menu / stavem hračky. Nech ho nad ostatními vrstvami.",
                "Přidej kameru, vlož RTMP klíč svého cam webu do <strong>Stream Settings</strong> ve "
                "SplitCamu a klikni na <strong>Go Live</strong> — překryv i hračka reagují na dýška.",
            ],
        },
    ],
}
