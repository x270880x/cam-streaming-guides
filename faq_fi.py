# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_FI = {
    "common": [
        (
            "Kuinka paljon mallit voivat ansaita alustalla {name}?",
            "Ansiot alustalla {name} riippuvat yleisön koosta, lähetystunneista ja tippauskäyttäytymisestä. "
            "Aktiiviset lähettäjät tienaavat tyypillisesti 200–3 000 dollaria kuukaudessa; huippusuorittajat "
            "yltävät yli 10 000 dollariin. Tuottosi osuus noudattaa {name}-alustan palkkiorakennetta — "
            "tarkista mallisopimus ennen suoran lähetyksen aloittamista."
        ),
        (
            "Onko {name} turvallinen lähettäjille?",
            "{name} edellyttää iän ja henkilöllisyyden varmennusta ennen maksua, mikä suojaa malleja "
            "petoksilta. Käytä taiteilijanimeä, älä koskaan jaa henkilötietoja kameralla, ota käyttöön "
            "geo-estot piilottaaksesi lähetyksesi kotialueeltasi ja käsittele jokainen katsojan pyyntö "
            "kaupallisena. SplitCamin overlayt ja tekoälytausta voivat myös piilottaa tai korvata "
            "todellisen ympäristösi."
        ),
        (
            "Mitä dokumentteja tarvitsen tullakseni malliksi alustalle {name}?",
            "{name} vaatii tyypillisesti viranomaisen myöntämän valokuvallisen henkilöllisyystodistuksen "
            "(passi, ajokortti tai henkilökortti), selfien henkilöllisyystodistuksen kanssa sekä vero-/"
            "maksulomakkeen (W-9 Yhdysvalloissa, W-8BEN muille). Hyväksyntä kestää yleensä 24–72 tuntia; "
            "hyväksynnän jälkeen voit aloittaa suorat lähetykset samana päivänä."
        ),
        (
            "Voinko lähettää alustalle {name} puhelimestani?",
            "{name} tarjoaa yleensä mobiilisovelluksen lähettäjille tai mobiiliverkkolähettäjän, mutta "
            "kokemus on rajallinen — ei overlayta, ei toista kameraa, ei tekoälytaustaa. Täyden "
            "tuotantolaadun saavuttamiseksi lähetä tietokoneelta SplitCamilla ja käytä puhelinta toisena "
            "kamerana (SplitCam hyväksyy IP-kamerasyötteen puhelimista)."
        ),
    ],
    "stream": (
        "Tukeeko {name} OBS:ää tai ulkoista enkooderia?",
        "Kyllä — {name} tarjoaa RTMP-palvelimen URL-osoitteen ja stream key -avaimen lähettäjäpaneelissa. "
        "Liitä molemmat SplitCamin <strong>Stream Settings → Custom RTMP</strong> -kohtaan, aseta "
        "1920×1080 30 fps:llä ja 4 000–5 000 Kbps bittinopeudella, ja klikkaa <strong>Go Live</strong>. "
        "Custom RTMP -reitti antaa täyden SplitCam-näkymäkoostumuksen (monikamera, overlayt, suodattimet)."
    ),
    "vcam": (
        "Voinko käyttää SplitCamia virtuaalikamerana alustalla {name}?",
        "Kyllä — {name}-lähetys toimii selaimessa, joten SplitCam rekisteröityy verkkokamerana nimeltä "
        "<strong>\"SplitCam Video Driver\"</strong>. Avaa {name}-lähettäjäpaneeli, klikkaa selaimen "
        "kameravalitsinta ja valitse SplitCam. Koostettu näkymäsi (overlayt, toinen kamera, suodattimet, "
        "tekoälytausta) saavuttaa katsojat yhtenä verkkokamerasyötteenä."
    ),
}
