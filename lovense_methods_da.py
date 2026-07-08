# -*- coding: utf-8 -*-
LOVENSE_METHODS_DA = {
    "heading": "Sæt Lovense op på SplitCam — 3 trin",
    "lead": "Dette følger Lovenses egen opsætning i tre trin. <strong>Cam Extension</strong> aflæser drikkepenge fra dit camsite, <strong>Lovense Connect</strong> er Bluetooth-broen til dit legetøj, og <strong>SplitCam Toolset</strong> lægger Lovense-overlayet ind i SplitCam, som sender via RTMP. Alt er gratis, og downloadknapperne matcher automatisk dit system.",
    "stage_word": "Trin",
    "get_label": "Download",
    "do_label": "Derefter",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Aflæser drikkepengene fra dit camsite — installeres i Chrome eller Edge.",
            "get": [
                "camext"
            ],
            "steps": [
                "Download Cam Extension og pak den ud.",
                "Åbn <strong>chrome://extensions</strong> (eller <strong>edge://extensions</strong>), slå <strong>Developer mode</strong> til øverst til højre, klik på <strong>Load unpacked</strong> og vælg den udpakkede <em>lovense_cam</em>-mappe.",
                "Klik på Lovense-ikonet i værktøjslinjen og log ind med din Lovense-konto."
            ]
        },
        {
            "title": "Lovense Connect",
            "role": "Broen, der taler med dit legetøj over Bluetooth.",
            "get": [
                "connect"
            ],
            "steps": [
                "På en computer: installer Lovense Connect (en Lovense USB Bluetooth-adapter anbefales). På en telefon: hent Lovense Connect-appen fra Google Play eller App Store.",
                "Tænd dit legetøj og par det i Connect, indtil det viser forbundet. I telefonappen scanner du QR-koden, der vises på din computer, for at forbinde dem."
            ]
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Viser Lovense-overlayet i SplitCam og sender dit stream.",
            "get": [
                "splitcam",
                "toolset"
            ],
            "steps": [
                "Installer SplitCam, og installer derefter Lovense SplitCam Toolset — pluginnet, der tilføjer Lovense-overlayet til SplitCam.",
                "I Cam Extension klikker du på <strong>+</strong> for at tilføje dit camsite (Chaturbate, Stripchat, …) og opsætte din tip-menu, åbn derefter fanen <strong>Video Feedback</strong> og vælg <strong>SplitCam</strong> fra listen (OBS / SplitCam / Streamster).",
                "I SplitCam tilføjer du <strong>Lovense</strong>-kilden, som Toolset registrerede — overlayet med tip-menu og legetøjsstatus vises på din scene. Hold det over dine øvrige lag.",
                "Tilføj dit kamera, indsæt dit camsites RTMP-nøgle under SplitCams <strong>Stream Settings</strong>, og klik på <strong>Go Live</strong> — overlayet og legetøjet reagerer på drikkepenge."
            ]
        }
    ]
}
