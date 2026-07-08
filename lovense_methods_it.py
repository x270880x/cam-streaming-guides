# -*- coding: utf-8 -*-
LOVENSE_METHODS_IT = {
    "heading": "Configura Lovense su SplitCam — 3 passaggi",
    "lead": "Segue la stessa configurazione in tre passaggi di Lovense. La <strong>Cam Extension</strong> "
            "legge le mance dal tuo sito cam, <strong>Lovense Connect</strong> è il ponte Bluetooth verso "
            "il tuo giocattolo e il <strong>SplitCam Toolset</strong> porta l'overlay Lovense dentro "
            "SplitCam, che trasmette via RTMP. È tutto gratuito e i pulsanti di download riconoscono "
            "automaticamente il tuo sistema.",
    "stage_word": "Passaggio",
    "get_label": "Scarica",
    "do_label": "Poi",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Legge le mance dal tuo sito cam — si installa su Chrome o Edge.",
            "get": ["camext"],
            "steps": [
                "Scarica la Cam Extension ed estrai il file zip.",
                "Apri <strong>chrome://extensions</strong> (oppure <strong>edge://extensions</strong>), "
                "attiva la <strong>Developer mode</strong> in alto a destra, clicca su <strong>Load unpacked</strong> "
                "e seleziona la cartella <em>lovense_cam</em> estratta.",
                "Clicca sull'icona Lovense nella barra degli strumenti e accedi con il tuo account Lovense.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Il ponte che comunica con il tuo giocattolo via Bluetooth.",
            "get": ["connect"],
            "steps": [
                "Su computer: installa Lovense Connect (è consigliato un adattatore Bluetooth USB Lovense). "
                "Su telefono: scarica l'app Lovense Connect da Google Play o dall'App Store.",
                "Accendi il giocattolo e abbinalo in Connect finché non risulta collegato. Sull'app del telefono, "
                "scansiona il codice QR mostrato sul computer per associarli.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Mostra l'overlay Lovense in SplitCam e trasmette il tuo stream.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Installa SplitCam, poi installa il Lovense SplitCam Toolset — il plugin che aggiunge "
                "l'overlay Lovense a SplitCam.",
                "Nella Cam Extension, clicca su <strong>+</strong> per aggiungere il tuo sito cam (Chaturbate, "
                "Stripchat, …) e imposta il tuo menu mance, poi apri la scheda <strong>Video Feedback</strong> "
                "e scegli <strong>SplitCam</strong> dalla lista (OBS / SplitCam / Streamster).",
                "In SplitCam, aggiungi la sorgente <strong>Lovense</strong> registrata dal Toolset — l'overlay "
                "del menu mance / stato del giocattolo appare nella tua scena. Tienilo sopra gli altri livelli.",
                "Aggiungi la tua camera, incolla la chiave RTMP del tuo sito cam nelle <strong>Stream "
                "Settings</strong> di SplitCam e clicca su <strong>Go Live</strong> — l'overlay e il giocattolo "
                "reagiscono alle mance.",
            ],
        },
    ],
}
