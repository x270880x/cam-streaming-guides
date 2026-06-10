# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_HR = {
    "common": [
        (
            "Koliko modeli mogu zaraditi na {name}?",
            "Zarada na {name} ovisi o veličini publike, satima streamanja i napojnicama. "
            "Aktivni broadcasteri obično zarade 200–3.000 USD mjesečno; najbolji izvođači dosežu "
            "10.000+ USD. Vaš udio u prihodu prati strukturu provizije platforme {name} — provjerite "
            "ugovor s modelom prije nego što krenete uživo."
        ),
        (
            "Je li {name} siguran za broadcastere?",
            "{name} zahtijeva provjeru dobi i identiteta prije isplate, što štiti modele od "
            "prijevara. Koristite umjetničko ime, nikada ne dijelite osobne podatke pred kamerom, "
            "uključite geo-blokade kako biste sakrili stream od svoje regije i tretirajte svaki "
            "zahtjev gledatelja kao transakciju. SplitCam overlayi i AI pozadina također mogu "
            "sakriti ili zamijeniti vaše stvarno okruženje."
        ),
        (
            "Koji su mi dokumenti potrebni da postanem model na {name}?",
            "{name} obično zahtijeva državnu osobnu ispravu s fotografijom (putovnica, vozačka "
            "dozvola ili osobna iskaznica), selfie s tom ispravom u ruci i porezni/isplatni "
            "obrazac (W-9 za SAD, W-8BEN za ostale). Odobrenje obično traje 24–72 sata; nakon "
            "odobrenja možete krenuti uživo isti dan."
        ),
        (
            "Mogu li streamati na {name} s mobitela?",
            "{name} obično nudi mobilnu aplikaciju za broadcastere ili mobile-web broadcaster, ali "
            "iskustvo je ograničeno — bez overlaya, bez druge kamere, bez AI pozadine. Za punu "
            "produkcijsku kvalitetu emitirajte s računala koristeći SplitCam, a mobitel iskoristite "
            "kao drugu kameru (SplitCam prihvaća ulaz IP-kamere s mobitela)."
        ),
    ],
    "stream": (
        "Podržava li {name} OBS ili vanjski enkoder?",
        "Da — {name} u broadcaster panelu nudi RTMP server URL i stream ključ. "
        "Zalijepite oboje u SplitCam <strong>Stream Settings → Custom RTMP</strong>, postavite "
        "1920×1080 pri 30 fps s bitrateom 4.000–5.000 Kbps i kliknite <strong>Go Live</strong>. "
        "Ruta Custom RTMP daje vam punu kompoziciju scene u SplitCamu (više kamera, overlayi, filteri)."
    ),
    "vcam": (
        "Mogu li koristiti SplitCam kao virtualnu kameru na {name}?",
        "Da — {name} uživo radi u pregledniku, pa se SplitCam registrira kao webcam pod nazivom "
        "<strong>\"SplitCam Video Driver\"</strong>. Otvorite {name} broadcaster, kliknite selektor "
        "kamere u pregledniku i odaberite SplitCam. Vaša komponirana scena (overlayi, druga kamera, "
        "filteri, AI pozadina) dolazi do gledatelja kao jedan webcam feed."
    ),
}
