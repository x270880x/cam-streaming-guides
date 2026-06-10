# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_IT = {
    "common": [
        (
            "Quanto possono guadagnare le modelle su {name}?",
            "I guadagni su {name} dipendono dalle dimensioni del pubblico, dalle ore di streaming "
            "e dai comportamenti di tipping. Le broadcaster attive portano a casa tipicamente "
            "200–3.000 $ al mese; i top performer raggiungono oltre 10.000 $. La tua quota di "
            "ricavi segue la struttura delle commissioni di {name} — controlla il contratto "
            "modella prima di andare in diretta."
        ),
        (
            "{name} è sicuro per le broadcaster?",
            "{name} richiede la verifica di età e identità prima del pagamento, il che protegge "
            "le modelle dalle frodi. Usa un nome d'arte, non condividere mai dati personali in "
            "camera, attiva i geo-block per nascondere lo stream dalla tua regione di residenza "
            "e tratta ogni richiesta degli spettatori come transazionale. Gli overlay e lo sfondo "
            "AI di SplitCam possono anche nascondere o sostituire l'ambiente reale."
        ),
        (
            "Quali documenti servono per diventare modella su {name}?",
            "{name} richiede tipicamente un documento d'identità con foto rilasciato dal governo "
            "(passaporto, patente o carta d'identità), un selfie con il documento in mano e un "
            "modulo fiscale/di pagamento (W-9 per gli USA, W-8BEN per non-USA). L'approvazione "
            "richiede di solito 24–72 ore; una volta approvata puoi andare in diretta lo stesso giorno."
        ),
        (
            "Posso trasmettere in streaming su {name} dal telefono?",
            "{name} di solito offre un'app broadcaster mobile o un broadcaster mobile-web, ma "
            "l'esperienza è limitata — niente overlay, niente seconda camera, niente sfondo AI. "
            "Per una qualità di produzione completa, trasmetti da un computer con SplitCam e usa "
            "il telefono come seconda camera (SplitCam accetta input da IP-camera dai telefoni)."
        ),
    ],
    "stream": (
        "{name} supporta OBS o un encoder esterno?",
        "Sì — {name} fornisce un URL del server RTMP e una chiave di streaming nel pannello "
        "broadcaster. Incollali entrambi nelle <strong>Stream Settings → Custom RTMP</strong> "
        "di SplitCam, imposta 1920×1080 a 30 fps con un bitrate di 4.000–5.000 Kbps e clicca "
        "<strong>Go Live</strong>. La via Custom RTMP ti dà la composizione completa delle "
        "scene di SplitCam (multi-camera, overlay, filtri)."
    ),
    "vcam": (
        "Posso usare SplitCam come camera virtuale su {name}?",
        "Sì — la live di {name} gira nel browser, quindi SplitCam si registra come una webcam "
        "chiamata <strong>\"SplitCam Video Driver\"</strong>. Apri il broadcaster di {name}, "
        "clicca sul selettore della camera nel browser e scegli SplitCam. La tua scena composta "
        "(overlay, seconda camera, filtri, sfondo AI) arriva agli spettatori come un singolo "
        "feed webcam."
    ),
}
