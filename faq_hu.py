# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_HU = {
    "common": [
        (
            "Mennyit kereshetnek a modellek a(z) {name} oldalon?",
            "A(z) {name} oldalon a kereset a nézőszámtól, az adásban töltött óráktól és a "
            "borravalózási szokásoktól függ. Az aktív műsorszórók általában havi 200–3 000 dollárt "
            "visznek haza; a legjobbak elérik a 10 000 dollárt is. A részesedésed a(z) {name} "
            "jutalékstruktúráját követi — élő adás előtt nézd át a modellszerződést."
        ),
        (
            "Biztonságos a(z) {name} a műsorszóróknak?",
            "A(z) {name} a kifizetés előtt életkor- és személyazonosság-igazolást kér, ami védi a "
            "modelleket a csalástól. Használj művésznevet, soha ne adj meg személyes adatot kamera "
            "előtt, kapcsold be a geo-blokkolást, hogy a lakóhelyed régiójában elrejtsd az adást, "
            "és minden nézői kérést kezelj tranzakcióként. A SplitCam overlay-jei és AI háttere "
            "szintén el tudják fedni vagy lecserélni a valódi környezetedet."
        ),
        (
            "Milyen dokumentumok kellenek ahhoz, hogy modell legyek a(z) {name} oldalon?",
            "A(z) {name} általában hatósági fényképes igazolványt (útlevél, jogosítvány vagy "
            "személyi igazolvány), egy szelfit, amelyen az igazolványt tartod, valamint adó- és "
            "kifizetési űrlapot (W-9 az USA-ban, W-8BEN az USA-n kívül) kér. A jóváhagyás általában "
            "24–72 órát vesz igénybe; az engedélyezés után még aznap élőben mehetsz."
        ),
        (
            "Streamelhetek a(z) {name} oldalra a telefonomról?",
            "A(z) {name} általában kínál mobil broadcaster appot vagy mobil-webes broadcastert, de "
            "az élmény korlátozott — nincs overlay, nincs második kamera, nincs AI háttér. A teljes "
            "produkciós minőséghez számítógépről közvetíts SplitCammel, és használd a telefonod "
            "második kameraként (a SplitCam fogad IP-kamera bemenetet telefonokról)."
        ),
    ],
    "stream": (
        "Támogatja a(z) {name} az OBS-t vagy külső enkódert?",
        "Igen — a(z) {name} a broadcaster panelben megad egy RTMP szerver URL-t és egy stream "
        "kulcsot. Illeszd be mindkettőt a SplitCam <strong>Stream Settings → Custom RTMP</strong> "
        "menüjébe, állíts be 1920×1080-at 30 fps-en 4 000–5 000 Kbps bitrátával, majd kattints a "
        "<strong>Go Live</strong> gombra. A Custom RTMP útvonal teljes SplitCam jelenet-"
        "kompozíciót ad (több kamera, overlay, szűrők)."
    ),
    "vcam": (
        "Használhatom a SplitCamet virtuális kameraként a(z) {name} oldalon?",
        "Igen — a(z) {name} élő adása böngészőben fut, így a SplitCam <strong>\"SplitCam Video "
        "Driver\"</strong> nevű webkameraként jelenik meg. Nyisd meg a(z) {name} broadcastert, "
        "kattints a kamera-választóra a böngészőben, és válaszd a SplitCamet. A komponált jeleneted "
        "(overlay, második kamera, szűrők, AI háttér) egyetlen webkamera-adásként jut el a nézőkhöz."
    ),
}
