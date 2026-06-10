# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_SK = {
    "common": [
        (
            "Koľko môžu modelky zarobiť na {name}?",
            "Zárobky na {name} závisia od veľkosti publika, odvysielaných hodín a štedrosti divákov "
            "v tipoch. Aktívni vysielatelia si bežne odnesú 200 – 3 000 $ mesačne; špička dosahuje "
            "10 000 $ a viac. Tvoj podiel z tržieb sa riadi províznou štruktúrou {name} — pred "
            "prvým live si prečítaj zmluvu pre modelky."
        ),
        (
            "Je {name} bezpečná platforma pre vysielateľky?",
            "{name} pred vyplatením vyžaduje overenie veku a totožnosti, čo modelky chráni pred "
            "podvodmi. Používaj umelecké meno, na kamere nikdy nezdieľaj osobné údaje, zapni "
            "geo-blokovanie, aby tvoj stream nevideli ľudia z tvojho regiónu, a každú požiadavku "
            "diváka ber ako transakciu. Overlaye a AI pozadie v SplitCame navyše dokážu skryť "
            "alebo nahradiť skutočné okolie."
        ),
        (
            "Aké doklady potrebujem, aby som sa stala modelkou na {name}?",
            "{name} typicky vyžaduje štátom vydaný doklad s fotkou (pas, vodičský preukaz alebo "
            "občiansky preukaz), selfie s dokladom v ruke a daňový/výplatný formulár (W-9 pre USA, "
            "W-8BEN pre ostatné krajiny). Schválenie zvyčajne trvá 24 – 72 hodín; po schválení "
            "môžeš ísť live ešte v ten istý deň."
        ),
        (
            "Môžem vysielať na {name} z mobilu?",
            "{name} obvykle ponúka mobilnú aplikáciu pre vysielateľov alebo mobilné webové "
            "rozhranie, no zážitok je obmedzený — žiadne overlaye, žiadna druhá kamera, žiadne "
            "AI pozadie. Pre plnú produkčnú kvalitu vysielaj z počítača cez SplitCam a telefón "
            "využi ako druhú kameru (SplitCam prijíma vstup IP kamery z telefónu)."
        ),
    ],
    "stream": (
        "Podporuje {name} OBS alebo externý encoder?",
        "Áno — {name} v paneli vysielateľa poskytuje RTMP URL servera a stream key. Vlož ich "
        "v SplitCame do <strong>Stream Settings → Custom RTMP</strong>, nastav 1920×1080 pri "
        "30 fps s bitrate 4 000 – 5 000 Kbps a klikni na <strong>Go Live</strong>. Cesta cez "
        "Custom RTMP ti dáva plnú kompozíciu scén v SplitCame (viac kamier, overlaye, filtre)."
    ),
    "vcam": (
        "Môžem použiť SplitCam ako virtuálnu kameru na {name}?",
        "Áno — live na {name} beží v prehliadači, takže sa SplitCam zaregistruje ako webkamera "
        "s názvom <strong>\"SplitCam Video Driver\"</strong>. Otvor panel vysielateľa na {name}, "
        "klikni v prehliadači na výber kamery a zvoľ SplitCam. Tvoja zložená scéna (overlaye, "
        "druhá kamera, filtre, AI pozadie) dorazí divákom ako jeden webcam feed."
    ),
}
