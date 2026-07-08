# -*- coding: utf-8 -*-
LOVENSE_METHODS_SK = {
    "heading": "Nastavte Lovense v SplitCam — 3 kroky",
    "lead": "Toto kopíruje vlastné trojkrokové nastavenie od Lovense. <strong>Cam Extension</strong> "
            "číta prepitné z tvojej cam stránky, <strong>Lovense Connect</strong> je Bluetooth mostík k "
            "tvojej hračke a <strong>SplitCam Toolset</strong> vloží Lovense prekrytie priamo do "
            "SplitCam, ktorý vysiela cez RTMP. Všetko je zadarmo; tlačidlá na stiahnutie sa "
            "automaticky prispôsobia tvojmu systému.",
    "stage_word": "Krok",
    "get_label": "Stiahnuť",
    "do_label": "Potom",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Číta prepitné z tvojej cam stránky — inštaluje sa do Chrome alebo Edge.",
            "get": ["camext"],
            "steps": [
                "Stiahni Cam Extension a rozbaľ ho.",
                "Otvor <strong>chrome://extensions</strong> (alebo <strong>edge://extensions</strong>), "
                "vpravo hore zapni <strong>Developer mode</strong>, klikni na <strong>Load unpacked</strong> "
                "a vyber rozbalený priečinok <em>lovense_cam</em>.",
                "Klikni na ikonu Lovense na paneli nástrojov a prihlás sa svojím Lovense účtom.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Mostík, ktorý komunikuje s tvojou hračkou cez Bluetooth.",
            "get": ["connect"],
            "steps": [
                "Na počítači: nainštaluj Lovense Connect (odporúča sa USB Bluetooth adaptér od Lovense). "
                "Na telefóne: stiahni aplikáciu Lovense Connect z Google Play alebo App Store.",
                "Zapni hračku a spáruj ju v Connect, kým sa nezobrazí ako pripojená. V aplikácii na "
                "telefóne naskenuj QR kód zobrazený na počítači, aby si ich prepojil.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Zobrazuje Lovense prekrytie v SplitCam a vysiela tvoj stream.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Nainštaluj SplitCam, potom nainštaluj Lovense SplitCam Toolset — plugin, ktorý pridá "
                "Lovense prekrytie do SplitCam.",
                "V Cam Extension klikni na <strong>+</strong>, pridaj svoju cam stránku (Chaturbate, "
                "Stripchat, …) a nastav si menu prepitných, potom otvor kartu <strong>Video Feedback</strong> "
                "a zo zoznamu vyber <strong>SplitCam</strong> (OBS / SplitCam / Streamster).",
                "V SplitCam pridaj zdroj <strong>Lovense</strong>, ktorý Toolset zaregistroval — prekrytie "
                "s menu prepitných a stavom hračky sa objaví na tvojej scéne. Nechaj ho nad ostatnými vrstvami.",
                "Pridaj svoju kameru, vlož RTMP kľúč svojej cam stránky v <strong>Stream Settings</strong> "
                "v SplitCam a klikni na <strong>Go Live</strong> — prekrytie aj hračka reagujú na prepitné.",
            ],
        },
    ],
}
