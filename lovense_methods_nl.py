# -*- coding: utf-8 -*-
LOVENSE_METHODS_NL = {
    "heading": "Lovense instellen op SplitCam — 3 stappen",
    "lead": "Dit volgt Lovense's eigen driestapsinstallatie. De <strong>Cam Extension</strong> leest "
            "fooien uit van je camsite, <strong>Lovense Connect</strong> is de Bluetooth-brug naar "
            "je toy, en de <strong>SplitCam Toolset</strong> zet de Lovense-overlay in "
            "SplitCam, dat uitzendt via RTMP. Alles is gratis; de downloadknoppen passen zich "
            "automatisch aan je systeem aan.",
    "stage_word": "Stap",
    "get_label": "Downloaden",
    "do_label": "Daarna",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Leest de fooien uit van je camsite — installeert in Chrome of Edge.",
            "get": ["camext"],
            "steps": [
                "Download de Cam Extension en pak hem uit.",
                "Open <strong>chrome://extensions</strong> (of <strong>edge://extensions</strong>), "
                "zet <strong>Developer mode</strong> rechtsboven aan, klik op <strong>Load unpacked</strong> "
                "en selecteer de uitgepakte map <em>lovense_cam</em>.",
                "Klik op het Lovense-icoon in de werkbalk en log in met je Lovense-account.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "De brug die via Bluetooth met je toy praat.",
            "get": ["connect"],
            "steps": [
                "Op een computer: installeer Lovense Connect (een Lovense USB-Bluetooth-adapter wordt "
                "aanbevolen). Op een telefoon: haal de Lovense Connect-app uit Google Play of de App Store.",
                "Zet je toy aan en koppel hem in Connect totdat hij als verbonden wordt weergegeven. Scan in "
                "de telefoon-app de QR-code die op je computer wordt getoond om ze te koppelen.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Toont de Lovense-overlay in SplitCam en zendt je stream uit.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Installeer SplitCam en installeer daarna de Lovense SplitCam Toolset — de plug-in die "
                "de Lovense-overlay aan SplitCam toevoegt.",
                "Klik in de Cam Extension op <strong>+</strong> om je camsite (Chaturbate, "
                "Stripchat, …) toe te voegen en stel je tipmenu in, open dan het tabblad <strong>Video Feedback</strong> "
                "en kies <strong>SplitCam</strong> uit de lijst (OBS / SplitCam / Streamster).",
                "Voeg in SplitCam de <strong>Lovense</strong>-bron toe die de Toolset heeft geregistreerd — de "
                "overlay met tipmenu / toy-status verschijnt op je scène. Houd hem boven je andere lagen.",
                "Voeg je camera toe, plak de RTMP-sleutel van je camsite in de <strong>Stream "
                "Settings</strong> van SplitCam en klik op <strong>Go Live</strong> — de overlay en toy reageren op fooien.",
            ],
        },
    ],
}
