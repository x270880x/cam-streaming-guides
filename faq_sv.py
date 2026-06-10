# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_SV = {
    "common": [
        (
            "Hur mycket kan modeller tjäna på {name}?",
            "Inkomsten på {name} beror på publikstorlek, antal sändningstimmar och tipsbeteende. "
            "Aktiva sändare tjänar vanligtvis 200–3 000 USD per månad; toppmodeller når "
            "10 000 USD+. Din intäktsandel följer {name}:s provisionsstruktur — läs modellavtalet "
            "innan du går live."
        ),
        (
            "Är {name} säkert för sändare?",
            "{name} kräver ålders- och ID-verifiering före utbetalning, vilket skyddar modeller från "
            "bedrägeri. Använd ett artistnamn, dela aldrig personuppgifter framför kameran, aktivera "
            "geo-blockering för att dölja din sändning från din hemregion och behandla varje "
            "tittarförfrågan som en transaktion. SplitCams overlays och AI-bakgrund kan också dölja "
            "eller ersätta din verkliga omgivning."
        ),
        (
            "Vilka dokument behöver jag för att bli modell på {name}?",
            "{name} kräver vanligtvis ett statligt utfärdat foto-ID (pass, körkort eller ID-kort), "
            "en selfie där du håller upp ID-handlingen och ett skatte-/utbetalningsformulär (W-9 för "
            "USA, W-8BEN för icke-USA). Godkännandet tar oftast 24–72 timmar; när du godkänts kan du "
            "gå live samma dag."
        ),
        (
            "Kan jag sända på {name} från min telefon?",
            "{name} erbjuder vanligtvis en mobil sändarapp eller en mobilwebb-sändare, men "
            "upplevelsen är begränsad — inga overlays, ingen andra kamera, ingen AI-bakgrund. För "
            "full produktionskvalitet, sänd från en dator med SplitCam och använd telefonen som en "
            "andra kamera (SplitCam accepterar IP-kamerainmatning från telefoner)."
        ),
    ],
    "stream": (
        "Stöder {name} OBS eller en extern encoder?",
        "Ja — {name} tillhandahåller en RTMP-server-URL och en stream key i sändarpanelen. "
        "Klistra in båda i SplitCams <strong>Stream Settings → Custom RTMP</strong>, ställ in "
        "1920×1080 vid 30 fps med en bitrate på 4 000–5 000 Kbps och klicka på <strong>Go Live</strong>. "
        "Custom RTMP-vägen ger dig full scenkomposition i SplitCam (flera kameror, overlays, filter)."
    ),
    "vcam": (
        "Kan jag använda SplitCam som en virtuell kamera på {name}?",
        "Ja — {name}:s live körs i webbläsaren, så SplitCam registreras som en webbkamera vid namn "
        "<strong>\"SplitCam Video Driver\"</strong>. Öppna {name}-sändaren, klicka på "
        "kameraväljaren i webbläsaren och välj SplitCam. Din komponerade scen (overlays, andra "
        "kamera, filter, AI-bakgrund) når tittarna som en enda webbkameraström."
    ),
}
