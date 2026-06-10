# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_PL = {
    "common": [
        (
            "Ile modelki mogą zarobić na {name}?",
            "Zarobki na {name} zależą od wielkości widowni, liczby godzin transmisji i hojności napiwków. "
            "Aktywni nadawcy zwykle zarabiają 200–3 000 USD miesięcznie; topowi performerzy osiągają "
            "10 000 USD i więcej. Twój udział w przychodach wynika ze struktury prowizji {name} — "
            "sprawdź umowę modelki przed wejściem na żywo."
        ),
        (
            "Czy {name} jest bezpieczne dla nadawców?",
            "{name} wymaga weryfikacji wieku i dokumentu tożsamości przed wypłatą, co chroni modelki przed "
            "oszustwami. Używaj pseudonimu scenicznego, nigdy nie udostępniaj danych osobowych przed kamerą, "
            "włącz geo-blokady, aby ukryć transmisję przed mieszkańcami swojego regionu, i traktuj każde "
            "życzenie widza jako transakcję. Nakładki i tło AI w SplitCam pomogą też ukryć lub zastąpić "
            "Twoje prawdziwe otoczenie."
        ),
        (
            "Jakie dokumenty są potrzebne, aby zostać modelką na {name}?",
            "{name} zwykle wymaga rządowego dokumentu tożsamości ze zdjęciem (paszport, prawo jazdy "
            "lub dowód osobisty), selfie z dokumentem w ręku oraz formularza podatkowego/wypłat "
            "(W-9 dla USA, W-8BEN poza USA). Akceptacja trwa zwykle 24–72 godziny; po zatwierdzeniu "
            "możesz wejść na żywo tego samego dnia."
        ),
        (
            "Czy mogę nadawać na {name} z telefonu?",
            "{name} zwykle oferuje mobilną aplikację dla nadawców lub mobilną wersję webową, ale "
            "doświadczenie jest ograniczone — bez nakładek, drugiej kamery i tła AI. Dla pełnej jakości "
            "produkcji nadawaj z komputera w SplitCam, a telefonu używaj jako drugiej kamery "
            "(SplitCam przyjmuje sygnał z telefonu jako IP-camera)."
        ),
    ],
    "stream": (
        "Czy {name} obsługuje OBS lub zewnętrzny enkoder?",
        "Tak — {name} udostępnia adres serwera RTMP i klucz transmisji w panelu nadawcy. "
        "Wklej oba do SplitCam w <strong>Stream Settings → Custom RTMP</strong>, ustaw "
        "1920×1080 przy 30 fps i bitrate 4 000–5 000 Kbps, a następnie kliknij <strong>Go Live</strong>. "
        "Ścieżka Custom RTMP daje pełną kompozycję sceny w SplitCam (multi-kamera, nakładki, filtry)."
    ),
    "vcam": (
        "Czy mogę używać SplitCam jako wirtualnej kamery na {name}?",
        "Tak — transmisja na {name} działa w przeglądarce, więc SplitCam pojawia się jako kamera "
        "<strong>\"SplitCam Video Driver\"</strong>. Otwórz panel nadawcy {name}, kliknij selektor "
        "kamery w przeglądarce i wybierz SplitCam. Twoja skomponowana scena (nakładki, druga kamera, "
        "filtry, tło AI) trafia do widzów jako pojedynczy sygnał kamery."
    ),
}
