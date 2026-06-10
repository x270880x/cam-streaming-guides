# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_DE = {
    "common": [
        (
            "Wie viel können Modelle auf {name} verdienen?",
            "Die Einnahmen auf {name} hängen von der Zuschauerzahl, den gestreamten Stunden und dem "
            "Trinkgeld-Verhalten ab. Aktive Broadcaster verdienen typischerweise 200–3.000 $ pro Monat; "
            "Top-Performer erreichen 10.000 $ und mehr. Dein Umsatzanteil richtet sich nach der "
            "Provisionsstruktur von {name} — prüfe den Modellvertrag, bevor du live gehst."
        ),
        (
            "Ist {name} sicher für Broadcaster?",
            "{name} verlangt vor der Auszahlung eine Alters- und Ausweisprüfung (Modell-Verifizierung), "
            "die Modelle vor Betrug schützt. Verwende einen Künstlernamen, gib niemals persönliche Daten "
            "vor der Kamera preis, aktiviere Geo-Sperren, um deinen Stream in deiner Heimatregion "
            "auszublenden, und behandle jede Zuschaueranfrage als geschäftlich. Die Overlays und der "
            "KI-Hintergrund von SplitCam können deine echte Umgebung zusätzlich verbergen oder ersetzen."
        ),
        (
            "Welche Dokumente brauche ich, um Modell auf {name} zu werden?",
            "{name} verlangt in der Regel einen amtlichen Lichtbildausweis (Reisepass, Führerschein "
            "oder Personalausweis), ein Selfie mit dem Ausweis in der Hand und ein Steuer-/Auszahlungs"
            "formular (W-9 für die USA, W-8BEN für Nicht-US-Modelle). Die Freigabe dauert üblicherweise "
            "24–72 Stunden; nach der Bestätigung kannst du noch am selben Tag live gehen."
        ),
        (
            "Kann ich auf {name} vom Handy aus streamen?",
            "{name} bietet meist eine mobile Broadcaster-App oder eine mobile Web-Variante an, doch "
            "der Funktionsumfang ist eingeschränkt — keine Overlays, keine zweite Kamera, kein "
            "KI-Hintergrund. Für volle Produktionsqualität sendest du vom Computer mit SplitCam und "
            "nutzt dein Handy als Zweitkamera (SplitCam akzeptiert IP-Kamera-Eingang vom Handy)."
        ),
    ],
    "stream": (
        "Unterstützt {name} OBS oder einen externen Encoder?",
        "Ja — {name} stellt im Broadcaster-Panel eine RTMP-Server-URL und einen Stream-Key bereit. "
        "Füge beide in SplitCam unter <strong>Stream-Einstellungen → Custom RTMP</strong> ein, stelle "
        "1920×1080 bei 30 fps mit einer Bitrate von 4.000–5.000 Kbps ein und klicke auf "
        "<strong>Go Live</strong>. Der Weg über Custom RTMP (externer Encoder) gibt dir die volle "
        "Szenenkomposition von SplitCam (Multikamera, Overlays, Filter)."
    ),
    "vcam": (
        "Kann ich SplitCam als virtuelle Kamera auf {name} verwenden?",
        "Ja — der Live-Modus von {name} läuft im Browser, daher meldet sich SplitCam als Webcam "
        "namens <strong>\"SplitCam Video Driver\"</strong> an. Öffne den Broadcaster von {name}, "
        "klicke im Browser auf die Kameraauswahl und wähle SplitCam. Deine komponierte Szene "
        "(Overlays, Zweitkamera, Filter, KI-Hintergrund, Premium-Inhalte) erreicht die Zuschauer "
        "als einzelner Webcam-Feed."
    ),
}
