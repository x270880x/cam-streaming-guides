# -*- coding: utf-8 -*-
LOVENSE_METHODS_RO = {
    "heading": "Configurează Lovense pe SplitCam — 3 pași",
    "lead": "Aceasta reproduce configurarea oficială Lovense în trei pași. <strong>Cam Extension</strong> "
            "citește bacșișurile de pe site-ul tău de cameră, <strong>Lovense Connect</strong> este puntea "
            "Bluetooth către jucăria ta, iar <strong>SplitCam Toolset</strong> aduce overlay-ul Lovense în "
            "SplitCam, care transmite prin RTMP. Totul este gratuit, iar butoanele de descărcare se "
            "potrivesc automat cu sistemul tău.",
    "stage_word": "Pasul",
    "get_label": "Descarcă",
    "do_label": "Apoi",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Citește bacșișurile de pe site-ul tău de cameră — se instalează în Chrome sau Edge.",
            "get": ["camext"],
            "steps": [
                "Descarcă Cam Extension și dezarhivează fișierul.",
                "Deschide <strong>chrome://extensions</strong> (sau <strong>edge://extensions</strong>), "
                "activează <strong>Developer mode</strong> în dreapta sus, apasă <strong>Load unpacked</strong> "
                "și selectează folderul dezarhivat <em>lovense_cam</em>.",
                "Apasă pictograma Lovense din bara de instrumente și autentifică-te cu contul tău Lovense.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Puntea care comunică cu jucăria ta prin Bluetooth.",
            "get": ["connect"],
            "steps": [
                "Pe computer: instalează Lovense Connect (se recomandă un adaptor USB Bluetooth Lovense). "
                "Pe telefon: descarcă aplicația Lovense Connect din Google Play sau App Store.",
                "Pornește jucăria și asociaz-o în Connect până apare ca fiind conectată. În aplicația de pe "
                "telefon, scanează codul QR afișat pe computer pentru a le lega.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Afișează overlay-ul Lovense în SplitCam și transmite streamul tău.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Instalează SplitCam, apoi instalează Lovense SplitCam Toolset — plugin-ul care adaugă "
                "overlay-ul Lovense în SplitCam.",
                "În Cam Extension, apasă <strong>+</strong> pentru a adăuga site-ul tău de cameră (Chaturbate, "
                "Stripchat, …) și configurează meniul de bacșișuri, apoi deschide fila <strong>Video Feedback</strong> "
                "și alege <strong>SplitCam</strong> din listă (OBS / SplitCam / Streamster).",
                "În SplitCam, adaugă sursa <strong>Lovense</strong> înregistrată de Toolset — overlay-ul cu "
                "meniul de bacșișuri și statusul jucăriei apare pe scena ta. Ține-l deasupra celorlalte straturi.",
                "Adaugă camera, lipește cheia RTMP a site-ului tău în <strong>Stream Settings</strong> din "
                "SplitCam și apasă <strong>Go Live</strong> — overlay-ul și jucăria reacționează la bacșișuri.",
            ],
        },
    ],
}
