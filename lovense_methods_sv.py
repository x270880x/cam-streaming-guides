# -*- coding: utf-8 -*-
LOVENSE_METHODS_SV = {
    "heading": "Ställ in Lovense på SplitCam — 3 steg",
        "lead": "Det här följer Lovenses egen trestegsuppsättning. <strong>Cam Extension</strong> läser "
                "dricksen från din camsajt, <strong>Lovense Connect</strong> är Bluetooth-bryggan till "
                "din leksak, och <strong>SplitCam Toolset</strong> lägger Lovense-overlayen inuti "
                "SplitCam, som sänder över RTMP. Allt är gratis; nedladdningsknapparna anpassar sig "
                "automatiskt efter ditt system.",
        "stage_word": "Steg",
        "get_label": "Ladda ner",
        "do_label": "Sedan",
        "stages": [
            {
                "title": "Lovense Cam Extension",
                "role": "Läser dricksen från din camsajt — installeras i Chrome eller Edge.",
                "get": ["camext"],
                "steps": [
                    "Ladda ner Cam Extension och packa upp den.",
                    "Öppna <strong>chrome://extensions</strong> (eller <strong>edge://extensions</strong>), "
                    "slå på <strong>Developer mode</strong> uppe till höger, klicka på <strong>Load unpacked</strong> "
                    "och välj den uppackade mappen <em>lovense_cam</em>.",
                    "Klicka på Lovense-ikonen i verktygsfältet och logga in med ditt Lovense-konto.",
                ],
            },
            {
                "title": "Lovense Connect",
                "role": "Bryggan som pratar med din leksak över Bluetooth.",
                "get": ["connect"],
                "steps": [
                    "På en dator: installera Lovense Connect (en Lovense USB Bluetooth-adapter "
                    "rekommenderas). På en telefon: hämta appen Lovense Connect från Google Play eller App Store.",
                    "Slå på din leksak och para ihop den i Connect tills den visas som ansluten. I telefonappen, "
                    "skanna QR-koden som visas på din dator för att länka dem.",
                ],
            },
            {
                "title": "SplitCam + Toolset",
                "role": "Visar Lovense-overlayen i SplitCam och sänder din stream.",
                "get": ["splitcam", "toolset"],
                "steps": [
                    "Installera SplitCam, och installera sedan Lovense SplitCam Toolset — pluginet som lägger "
                    "till Lovense-overlayen i SplitCam.",
                    "I Cam Extension, klicka på <strong>+</strong> för att lägga till din camsajt (Chaturbate, "
                    "Stripchat, …) och ställ in din dricksmeny, öppna sedan fliken <strong>Video Feedback</strong> "
                    "och välj <strong>SplitCam</strong> i listan (OBS / SplitCam / Streamster).",
                    "I SplitCam, lägg till <strong>Lovense</strong>-källan som Toolset registrerade — "
                    "overlayen med dricksmeny / leksaksstatus dyker upp på din scen. Håll den ovanför dina andra lager.",
                    "Lägg till din kamera, klistra in din camsajts RTMP-nyckel i SplitCams <strong>Stream "
                    "Settings</strong>, och klicka på <strong>Go Live</strong> — overlayen och leksaken reagerar på dricks.",
                ],
            },
        ],
}
