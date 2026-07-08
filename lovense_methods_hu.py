# -*- coding: utf-8 -*-
LOVENSE_METHODS_HU = {
    "heading": "A Lovense beállítása SplitCammel — 3 lépés",
    "lead": "Ez a Lovense saját, háromlépéses beállítását követi. A <strong>Cam Extension</strong> "
            "olvassa be a borravalókat a kamerás oldaladról, a <strong>Lovense Connect</strong> a "
            "Bluetooth-híd a játékodhoz, a <strong>SplitCam Toolset</strong> pedig a Lovense overlayt "
            "teszi a SplitCambe, amely RTMP-n keresztül sugároz. Minden ingyenes; a letöltőgombok "
            "automatikusan a rendszeredhez igazodnak.",
    "stage_word": "Lépés",
    "get_label": "Letöltés",
    "do_label": "Utána",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Beolvassa a borravalókat a kamerás oldaladról — Chrome vagy Edge alá települ.",
            "get": ["camext"],
            "steps": [
                "Töltsd le a Cam Extensiont, és csomagold ki.",
                "Nyisd meg a <strong>chrome://extensions</strong> (vagy <strong>edge://extensions</strong>) "
                "oldalt, kapcsold be a jobb felül lévő <strong>Developer mode</strong> kapcsolót, kattints a "
                "<strong>Load unpacked</strong> gombra, és válaszd ki a kicsomagolt <em>lovense_cam</em> mappát.",
                "Kattints a Lovense ikonra az eszköztárban, és jelentkezz be a Lovense-fiókoddal.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "A híd, amely Bluetooth-on keresztül kommunikál a játékoddal.",
            "get": ["connect"],
            "steps": [
                "Számítógépen: telepítsd a Lovense Connectet (ajánlott egy Lovense USB Bluetooth-adapter). "
                "Telefonon: töltsd le a Lovense Connect appot a Google Playről vagy az App Store-ból.",
                "Kapcsold be a játékodat, és párosítsd a Connectben, amíg csatlakoztatott állapotot nem mutat. "
                "A telefonos appban olvasd be a számítógépen megjelenő QR-kódot az összekapcsoláshoz.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Megjeleníti a Lovense overlayt a SplitCamben, és sugározza az adásodat.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Telepítsd a SplitCamet, majd a Lovense SplitCam Toolsetet — ez a bővítmény adja hozzá a "
                "Lovense overlayt a SplitCamhez.",
                "A Cam Extensionben kattints a <strong>+</strong> gombra a kamerás oldalad (Chaturbate, "
                "Stripchat, …) hozzáadásához, állítsd be a borravaló-menüt, majd nyisd meg a "
                "<strong>Video Feedback</strong> fület, és válaszd a <strong>SplitCam</strong> lehetőséget a "
                "listából (OBS / SplitCam / Streamster).",
                "A SplitCamben add hozzá a Toolset által regisztrált <strong>Lovense</strong> forrást — a "
                "borravaló-menü / játékállapot overlay megjelenik a jeleneteden. Tartsd a többi réteged felett.",
                "Add hozzá a kamerádat, illeszd be a kamerás oldalad RTMP-kulcsát a SplitCam <strong>Stream "
                "Settings</strong> menüjébe, és kattints a <strong>Go Live</strong> gombra — az overlay és a "
                "játék reagál a borravalókra.",
            ],
        },
    ],
}
