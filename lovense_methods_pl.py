# -*- coding: utf-8 -*-
LOVENSE_METHODS_PL = {
    "heading": "Skonfiguruj Lovense w SplitCam — 3 kroki",
    "lead": "To odzwierciedla oficjalną trzykrokową konfigurację Lovense. <strong>Cam Extension</strong> "
            "odczytuje napiwki z Twojej strony kamerkowej, <strong>Lovense Connect</strong> to most "
            "Bluetooth do Twojej zabawki, a <strong>SplitCam Toolset</strong> umieszcza nakładkę Lovense "
            "wewnątrz SplitCam, który nadaje przez RTMP. Wszystko jest darmowe, a przyciski pobierania "
            "automatycznie dopasowują się do Twojego systemu.",
    "stage_word": "Krok",
    "get_label": "Pobierz",
    "do_label": "Następnie",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Odczytuje napiwki z Twojej strony kamerkowej — instaluje się w Chrome lub Edge.",
            "get": ["camext"],
            "steps": [
                "Pobierz Cam Extension i rozpakuj archiwum.",
                "Otwórz <strong>chrome://extensions</strong> (lub <strong>edge://extensions</strong>), "
                "włącz <strong>Developer mode</strong> w prawym górnym rogu, kliknij <strong>Load unpacked</strong> "
                "i wybierz rozpakowany folder <em>lovense_cam</em>.",
                "Kliknij ikonę Lovense na pasku narzędzi i zaloguj się na swoje konto Lovense.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Most, który komunikuje się z Twoją zabawką przez Bluetooth.",
            "get": ["connect"],
            "steps": [
                "Na komputerze: zainstaluj Lovense Connect (zalecany jest adapter Bluetooth USB Lovense). "
                "Na telefonie: pobierz aplikację Lovense Connect z Google Play lub App Store.",
                "Włącz zabawkę i sparuj ją w Connect, aż pokaże się jako połączona. W aplikacji na telefonie "
                "zeskanuj kod QR wyświetlony na komputerze, aby je powiązać.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Wyświetla nakładkę Lovense w SplitCam i nadaje Twój stream.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Zainstaluj SplitCam, a następnie zainstaluj Lovense SplitCam Toolset — wtyczkę, która "
                "dodaje nakładkę Lovense do SplitCam.",
                "W Cam Extension kliknij <strong>+</strong>, aby dodać swoją stronę kamerkową (Chaturbate, "
                "Stripchat, …) i ustaw menu napiwków, następnie otwórz zakładkę <strong>Video Feedback</strong> "
                "i wybierz z listy <strong>SplitCam</strong> (OBS / SplitCam / Streamster).",
                "W SplitCam dodaj źródło <strong>Lovense</strong>, które zarejestrował Toolset — nakładka "
                "z menu napiwków / statusem zabawki pojawi się na Twojej scenie. Trzymaj ją nad pozostałymi warstwami.",
                "Dodaj swoją kamerę, wklej klucz RTMP swojej strony kamerkowej w <strong>Stream Settings</strong> "
                "w SplitCam i kliknij <strong>Go Live</strong> — nakładka i zabawka reagują na napiwki.",
            ],
        },
    ],
}
