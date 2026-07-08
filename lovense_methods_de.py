# -*- coding: utf-8 -*-
LOVENSE_METHODS_DE = {
    "heading": "Lovense in SplitCam einrichten — 3 Schritte",
    "lead": "Das entspricht genau Lovenses eigener Einrichtung in drei Schritten. Die "
            "<strong>Cam Extension</strong> liest die Trinkgelder von deiner Cam-Seite aus, "
            "<strong>Lovense Connect</strong> ist die Bluetooth-Brücke zu deinem Toy, und das "
            "<strong>SplitCam Toolset</strong> blendet das Lovense-Overlay in SplitCam ein, das per "
            "RTMP sendet. Alles ist kostenlos; die Download-Buttons passen sich automatisch an dein "
            "System an.",
    "stage_word": "Schritt",
    "get_label": "Herunterladen",
    "do_label": "Danach",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Liest die Trinkgelder von deiner Cam-Seite aus — wird in Chrome oder Edge installiert.",
            "get": ["camext"],
            "steps": [
                "Lade die Cam Extension herunter und entpacke sie.",
                "Öffne <strong>chrome://extensions</strong> (oder <strong>edge://extensions</strong>), "
                "aktiviere oben rechts den <strong>Developer mode</strong>, klicke auf "
                "<strong>Load unpacked</strong> und wähle den entpackten Ordner <em>lovense_cam</em> aus.",
                "Klicke auf das Lovense-Symbol in der Symbolleiste und melde dich mit deinem Lovense-Konto an.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Die Brücke, die per Bluetooth mit deinem Toy kommuniziert.",
            "get": ["connect"],
            "steps": [
                "Auf einem Computer: Installiere Lovense Connect (ein Lovense-USB-Bluetooth-Adapter wird "
                "empfohlen). Auf einem Smartphone: Hol dir die Lovense-Connect-App bei Google Play oder im App Store.",
                "Schalte dein Toy ein und koppele es in Connect, bis es als verbunden angezeigt wird. Scanne in "
                "der Smartphone-App den QR-Code, der auf deinem Computer angezeigt wird, um beide zu verbinden.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Zeigt das Lovense-Overlay in SplitCam an und überträgt deinen Stream.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Installiere SplitCam und danach das Lovense SplitCam Toolset — das Plugin, das SplitCam das "
                "Lovense-Overlay hinzufügt.",
                "Klicke in der Cam Extension auf <strong>+</strong>, um deine Cam-Seite (Chaturbate, Stripchat, …) "
                "hinzuzufügen, richte dein Tip-Menü ein, öffne dann den Reiter <strong>Video Feedback</strong> und "
                "wähle in der Liste (OBS / SplitCam / Streamster) <strong>SplitCam</strong> aus.",
                "Füge in SplitCam die <strong>Lovense</strong>-Quelle hinzu, die das Toolset registriert hat — das "
                "Overlay mit Tip-Menü und Toy-Status erscheint in deiner Szene. Halte es über deinen anderen Ebenen.",
                "Füge deine Kamera hinzu, trage den RTMP-Schlüssel deiner Cam-Seite in den "
                "<strong>Stream Settings</strong> von SplitCam ein und klicke auf <strong>Go Live</strong> — das "
                "Overlay und das Toy reagieren auf Trinkgelder.",
            ],
        },
    ],
}
