# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_DA = {
    "common": [
        (
            "Hvor meget kan modeller tjene på {name}?",
            "Indtjeningen på {name} afhænger af publikumsstørrelse, antal streamede timer og "
            "tipping-adfærd. Aktive broadcastere tager typisk $200–$3.000 hjem om måneden; "
            "topperformere når $10.000+. Din indtægtsandel følger {name}s kommissionsstruktur — "
            "tjek modelaftalen, før du går live."
        ),
        (
            "Er {name} sikkert for broadcastere?",
            "{name} kræver alders- og ID-verifikation før udbetaling, hvilket beskytter modeller "
            "mod svindel. Brug et kunstnernavn, del aldrig personlige data på kamera, aktivér "
            "geo-blokeringer for at skjule din stream fra dit hjemområde, og behandl enhver "
            "seerforespørgsel som transaktionel. SplitCams overlays og AI-baggrund kan også skjule "
            "eller erstatte dine reelle omgivelser."
        ),
        (
            "Hvilke dokumenter har jeg brug for at blive model på {name}?",
            "{name} kræver typisk et statsudstedt billed-ID (pas, kørekort eller ID-kort), en "
            "selfie hvor du holder ID'et, og en skatte-/udbetalingsformular (W-9 for USA, W-8BEN "
            "for ikke-USA). Godkendelse tager normalt 24–72 timer; når du er godkendt, kan du gå "
            "live samme dag."
        ),
        (
            "Kan jeg streame på {name} fra min telefon?",
            "{name} tilbyder normalt en mobil broadcaster-app eller en mobil-web broadcaster, men "
            "oplevelsen er begrænset — ingen overlays, intet andet kamera, ingen AI-baggrund. For "
            "fuld produktionskvalitet skal du sende fra en computer med SplitCam og bruge din "
            "telefon som et andet kamera (SplitCam accepterer IP-kamera-input fra telefoner)."
        ),
    ],
    "stream": (
        "Understøtter {name} OBS eller en ekstern encoder?",
        "Ja — {name} leverer en RTMP-server-URL og en stream-nøgle i broadcaster-panelet. "
        "Indsæt begge i SplitCams <strong>Stream Settings → Custom RTMP</strong>, sæt "
        "1920×1080 ved 30 fps med en bitrate på 4.000–5.000 Kbps, og klik <strong>Go Live</strong>. "
        "Custom RTMP-ruten giver dig fuld SplitCam-scenekomposition (multi-kamera, overlays, filtre)."
    ),
    "vcam": (
        "Kan jeg bruge SplitCam som et virtuelt kamera på {name}?",
        "Ja — {name}s live kører i browseren, så SplitCam registreres som et webcam kaldet "
        "<strong>\"SplitCam Video Driver\"</strong>. Åbn {name}-broadcasteren, klik på "
        "kameravælgeren i browseren, og vælg SplitCam. Din komponerede scene (overlays, andet "
        "kamera, filtre, AI-baggrund) når seerne som et enkelt webcam-feed."
    ),
}
