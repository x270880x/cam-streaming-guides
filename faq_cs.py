# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_CS = {
    "common": [
        (
            "Kolik si modelky můžou na {name} vydělat?",
            "Výdělky na {name} závisí na velikosti publika, počtu odvysílaných hodin a chování diváků při tipování. "
            "Aktivní vysílající si obvykle odnesou 200–3 000 $ měsíčně; špičkoví performeři dosahují "
            "i 10 000 $ a víc. Tvůj podíl na příjmech se řídí provizní strukturou {name} — před prvním vysíláním "
            "si projdi model agreement."
        ),
        (
            "Je {name} pro vysílající bezpečná?",
            "{name} před vyplacením vyžaduje ověření věku a totožnosti, což chrání modelky před "
            "podvody. Používej umělecké jméno, nikdy na kameře nesděluj osobní údaje, zapni geo-blocky, "
            "aby tvůj stream nešel vidět z domovského regionu, a každý požadavek diváka ber jako "
            "transakční. Overlaye a AI pozadí ve SplitCamu navíc dokážou skutečné okolí skrýt nebo "
            "nahradit."
        ),
        (
            "Jaké dokumenty potřebuju, abych se na {name} stala modelkou?",
            "{name} obvykle vyžaduje státem vydaný doklad s fotkou (pas, řidičák nebo občanku), "
            "selfie s tímto dokladem v ruce a daňový/výplatní formulář (W-9 pro USA, W-8BEN pro "
            "ostatní). Schválení trvá většinou 24–72 hodin; po schválení můžeš jít živě ještě ten samý den."
        ),
        (
            "Můžu na {name} vysílat z mobilu?",
            "{name} většinou nabízí mobilní broadcaster aplikaci nebo mobilní web pro vysílání, "
            "ale možnosti jsou omezené — žádné overlaye, žádná druhá kamera, žádné AI pozadí. "
            "Pro plnou produkční kvalitu vysílej z počítače se SplitCamem a mobil použij jako "
            "druhou kameru (SplitCam přijímá IP-camera vstup z telefonů)."
        ),
    ],
    "stream": (
        "Podporuje {name} OBS nebo externí enkodér?",
        "Ano — {name} ti v broadcaster panelu poskytne RTMP server URL a stream key. "
        "Vlož obojí do <strong>Stream Settings → Custom RTMP</strong> ve SplitCamu, nastav "
        "1920×1080 při 30 fps s bitrate 4 000–5 000 Kbps a klikni na <strong>Go Live</strong>. "
        "Cesta přes Custom RTMP ti dá plnou kompozici scény ve SplitCamu (více kamer, overlaye, filtry)."
    ),
    "vcam": (
        "Můžu SplitCam použít jako virtuální kameru na {name}?",
        "Ano — live na {name} běží v prohlížeči, takže SplitCam se zaregistruje jako webkamera s názvem "
        "<strong>\"SplitCam Video Driver\"</strong>. Otevři broadcaster {name}, klikni v prohlížeči na "
        "výběr kamery a zvol SplitCam. Tvoje složená scéna (overlaye, druhá kamera, "
        "filtry, AI pozadí) dorazí divákům jako jeden webkamerový stream."
    ),
}
