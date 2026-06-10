# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_NO = {
    "common": [
        (
            "Hvor mye kan modeller tjene på {name}?",
            "Inntektene på {name} avhenger av publikumsstørrelse, antall timer sendt og tipping-vaner. "
            "Aktive kringkastere tjener vanligvis $200–$3 000 i måneden; toppmodeller når "
            "$10 000+. Din andel av inntekten følger {name}s provisjonsstruktur — sjekk modellavtalen "
            "før du går live."
        ),
        (
            "Er {name} trygt for kringkastere?",
            "{name} krever alders- og ID-verifisering før utbetaling, noe som beskytter modeller mot "
            "svindel. Bruk et scenenavn, del aldri personlige data på kamera, aktiver geo-blokkering for "
            "å skjule strømmen fra hjemregionen din, og behandle hver seerforespørsel som "
            "en transaksjon. SplitCams overlegg og AI-bakgrunn kan også skjule eller erstatte "
            "de virkelige omgivelsene dine."
        ),
        (
            "Hvilke dokumenter trenger jeg for å bli modell på {name}?",
            "{name} krever vanligvis et offentlig utstedt foto-ID (pass, førerkort "
            "eller ID-kort), en selfie med ID-en i hånden, og et skatte-/utbetalingsskjema (W-9 for USA, W-8BEN for "
            "ikke-amerikanske). Godkjenning tar vanligvis 24–72 timer; når du er godkjent kan du gå live samme dag."
        ),
        (
            "Kan jeg strømme på {name} fra mobilen?",
            "{name} tilbyr vanligvis en mobil kringkasterapp eller en mobil-web-kringkaster, men "
            "opplevelsen er begrenset — ingen overlegg, ingen andre kamera, ingen AI-bakgrunn. For full "
            "produksjonskvalitet, send fra en datamaskin med SplitCam og bruk telefonen som "
            "andre kamera (SplitCam aksepterer IP-kamera-input fra telefoner)."
        ),
    ],
    "stream": (
        "Støtter {name} OBS eller en ekstern encoder?",
        "Ja — {name} oppgir en RTMP-server-URL og en strømnøkkel i kringkasterpanelet. "
        "Lim inn begge i SplitCams <strong>Stream Settings → Custom RTMP</strong>, sett "
        "1920×1080 ved 30 fps med 4 000–5 000 Kbps bitrate, og klikk <strong>Go Live</strong>. "
        "Custom RTMP-ruten gir deg full SplitCam-scenekomposisjon (flerkamera, overlegg, filtre)."
    ),
    "vcam": (
        "Kan jeg bruke SplitCam som virtuelt kamera på {name}?",
        "Ja — {name}s live kjører i nettleseren, så SplitCam registreres som et webkamera kalt "
        "<strong>\"SplitCam Video Driver\"</strong>. Åpne {name}-kringkasteren, klikk kameravelgeren "
        "i nettleseren, og velg SplitCam. Den komponerte scenen din (overlegg, andre kamera, "
        "filtre, AI-bakgrunn) når seerne som en enkelt webkamera-feed."
    ),
}
