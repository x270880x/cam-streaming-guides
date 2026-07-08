# -*- coding: utf-8 -*-
LOVENSE_METHODS_FI = {
    "heading": "Ota Lovense käyttöön SplitCamissa — 3 vaihetta",
    "lead": "Tämä noudattaa Lovensen omaa kolmivaiheista asennusta. <strong>Cam Extension</strong> lukee tipit cam-sivustoltasi, <strong>Lovense Connect</strong> on Bluetooth-silta leluusi, ja <strong>SplitCam Toolset</strong> tuo Lovense-overlayn SplitCamiin, joka lähettää RTMP:n kautta. Kaikki on ilmaista, ja latauspainikkeet tunnistavat järjestelmäsi automaattisesti.",
    "stage_word": "Vaihe",
    "get_label": "Lataa",
    "do_label": "Sitten",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Lukee tipit cam-sivustoltasi — asentuu Chromeen tai Edgeen.",
            "get": ["camext"],
            "steps": [
                "Lataa Cam Extension ja pura zip-tiedosto.",
                "Avaa <strong>chrome://extensions</strong> (tai <strong>edge://extensions</strong>), kytke oikeasta yläkulmasta <strong>Developer mode</strong> päälle, klikkaa <strong>Load unpacked</strong> ja valitse purettu <em>lovense_cam</em>-kansio.",
                "Klikkaa Lovense-kuvaketta työkalupalkissa ja kirjaudu sisään Lovense-tililläsi."
            ]
        },
        {
            "title": "Lovense Connect",
            "role": "Silta, joka keskustelee leluusi kanssa Bluetoothin kautta.",
            "get": ["connect"],
            "steps": [
                "Tietokoneella: asenna Lovense Connect (Lovensen USB-Bluetooth-sovitinta suositellaan). Puhelimella: hae Lovense Connect -sovellus Google Playstä tai App Storesta.",
                "Kytke lelu päälle ja paritä se Connectissa, kunnes se näkyy yhdistettynä. Skannaa puhelimen sovelluksessa tietokoneella näkyvä QR-koodi yhdistääksesi ne."
            ]
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Näyttää Lovense-overlayn SplitCamissa ja lähettää striimisi.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Asenna SplitCam ja sen jälkeen Lovense SplitCam Toolset — lisäosa, joka tuo Lovense-overlayn SplitCamiin.",
                "Klikkaa Cam Extensionissa <strong>+</strong> lisätäksesi cam-sivustosi (Chaturbate, Stripchat, …) ja määritä tippivalikkosi, avaa sitten <strong>Video Feedback</strong> -välilehti ja valitse listalta <strong>SplitCam</strong> (OBS / SplitCam / Streamster).",
                "Lisää SplitCamissa <strong>Lovense</strong>-lähde, jonka Toolset rekisteröi — tippivalikon / lelun tilan overlay ilmestyy näkymääsi. Pidä se muiden tasojen yläpuolella.",
                "Lisää kamerasi, liitä cam-sivustosi RTMP-avain SplitCamin <strong>Stream Settings</strong> -asetuksiin ja klikkaa <strong>Go Live</strong> — overlay ja lelu reagoivat tippeihin."
            ]
        }
    ]
}
