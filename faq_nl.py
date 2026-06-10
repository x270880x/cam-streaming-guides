# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_NL = {
    "common": [
        (
            "Hoeveel kunnen modellen verdienen op {name}?",
            "Inkomsten op {name} hangen af van de grootte van het publiek, het aantal streamuren en "
            "het foooigedrag. Actieve broadcasters verdienen doorgaans $200–$3.000 per maand; "
            "topperformers halen $10.000+. Jouw aandeel volgt de commissiestructuur van {name} — "
            "bekijk de modelovereenkomst voordat je live gaat."
        ),
        (
            "Is {name} veilig voor broadcasters?",
            "{name} vereist leeftijds- en ID-verificatie voordat er uitbetaald wordt, wat modellen "
            "beschermt tegen fraude. Gebruik een artiestennaam, deel nooit persoonlijke gegevens "
            "voor de camera, schakel geo-blokkades in om je stream te verbergen voor je eigen "
            "regio, en behandel elk kijkersverzoek als transactie. De overlays en AI-achtergrond "
            "van SplitCam kunnen je echte omgeving ook verbergen of vervangen."
        ),
        (
            "Welke documenten heb ik nodig om model te worden op {name}?",
            "{name} vraagt doorgaans om een door de overheid uitgegeven identiteitsbewijs met foto "
            "(paspoort, rijbewijs of ID-kaart), een selfie waarop je het ID vasthoudt, en een "
            "belasting-/uitbetalingsformulier (W-9 voor de VS, W-8BEN buiten de VS). Goedkeuring "
            "duurt meestal 24–72 uur; zodra je bent goedgekeurd, kun je dezelfde dag live gaan."
        ),
        (
            "Kan ik streamen op {name} vanaf mijn telefoon?",
            "{name} biedt meestal een mobiele broadcaster-app of een mobiele webbroadcaster, maar "
            "de ervaring is beperkt — geen overlays, geen tweede camera, geen AI-achtergrond. Voor "
            "volledige productiekwaliteit kun je beter uitzenden vanaf een computer met SplitCam "
            "en je telefoon gebruiken als tweede camera (SplitCam accepteert IP-camera-invoer van telefoons)."
        ),
    ],
    "stream": (
        "Ondersteunt {name} OBS of een externe encoder?",
        "Ja — {name} levert een RTMP-server-URL en een streamsleutel in het broadcasterpaneel. "
        "Plak beide in <strong>Stream Settings → Custom RTMP</strong> van SplitCam, stel "
        "1920×1080 op 30 fps in met een bitrate van 4.000–5.000 Kbps, en klik op <strong>Go Live</strong>. "
        "De Custom RTMP-route geeft je volledige SplitCam-scènesamenstelling (multi-camera, overlays, filters)."
    ),
    "vcam": (
        "Kan ik SplitCam gebruiken als virtuele camera op {name}?",
        "Ja — de live van {name} draait in de browser, dus SplitCam registreert zich als webcam met de naam "
        "<strong>\"SplitCam Video Driver\"</strong>. Open de {name}-broadcaster, klik op de "
        "cameraselector in de browser en kies SplitCam. Je samengestelde scène (overlays, tweede camera, "
        "filters, AI-achtergrond) bereikt de kijkers als één webcam-feed."
    ),
}
