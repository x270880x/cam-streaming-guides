# -*- coding: utf-8 -*-
LOVENSE_METHODS_NO = {
    "heading": "Sett opp Lovense på SplitCam — 3 steg",
    "lead": "Dette følger Lovense sitt eget oppsett i tre steg. <strong>Cam Extension</strong> leser "
            "tips fra cam-siden din, <strong>Lovense Connect</strong> er Bluetooth-broen til "
            "leketøyet ditt, og <strong>SplitCam Toolset</strong> legger Lovense-overlayet inn i "
            "SplitCam, som sender over RTMP. Alt er gratis, og nedlastingsknappene tilpasser seg "
            "systemet ditt automatisk.",
    "stage_word": "Steg",
    "get_label": "Last ned",
    "do_label": "Deretter",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Leser tipsene fra cam-siden din — installeres i Chrome eller Edge.",
            "get": ["camext"],
            "steps": [
                "Last ned Cam Extension og pakk den ut.",
                "Åpne <strong>chrome://extensions</strong> (eller <strong>edge://extensions</strong>), "
                "slå på <strong>Developer mode</strong> øverst til høyre, klikk <strong>Load unpacked</strong> "
                "og velg den utpakkede <em>lovense_cam</em>-mappen.",
                "Klikk på Lovense-ikonet i verktøylinjen og logg inn med Lovense-kontoen din.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Broen som snakker med leketøyet ditt over Bluetooth.",
            "get": ["connect"],
            "steps": [
                "På en datamaskin: installer Lovense Connect (en Lovense USB Bluetooth-adapter "
                "anbefales). På en telefon: hent Lovense Connect-appen fra Google Play eller App Store.",
                "Slå på leketøyet og par det i Connect til det viser tilkoblet. I telefonappen "
                "skanner du QR-koden som vises på datamaskinen for å koble dem sammen.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Viser Lovense-overlayet i SplitCam og sender strømmen din.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Installer SplitCam, og installer deretter Lovense SplitCam Toolset — plugin-en som legger "
                "Lovense-overlayet til SplitCam.",
                "I Cam Extension klikker du <strong>+</strong> for å legge til cam-siden din (Chaturbate, "
                "Stripchat, …) og setter opp tips-menyen, åpne så fanen <strong>Video Feedback</strong> "
                "og velg <strong>SplitCam</strong> fra listen (OBS / SplitCam / Streamster).",
                "I SplitCam legger du til <strong>Lovense</strong>-kilden som Toolset registrerte — "
                "overlayet med tips-meny / leketøy-status vises på scenen din. Hold det over de andre lagene dine.",
                "Legg til kameraet ditt, lim inn RTMP-nøkkelen fra cam-siden din i SplitCam sine <strong>Stream "
                "Settings</strong>, og klikk <strong>Go Live</strong> — overlayet og leketøyet reagerer på tips.",
            ],
        },
    ],
}
