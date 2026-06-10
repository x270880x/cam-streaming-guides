# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_RO = {
    "common": [
        (
            "Cât pot câștiga modelele pe {name}?",
            "Câștigurile pe {name} depind de mărimea audienței, orele de stream și obiceiul de "
            "tipping. Broadcasterii activi obțin de obicei între 200 și 3.000 $ pe lună, iar topul "
            "ajunge la 10.000 $+. Cota ta din venit urmează structura de comision a {name} — "
            "verifică acordul de model înainte să intri live."
        ),
        (
            "Este {name} sigur pentru broadcasteri?",
            "{name} cere verificare de vârstă și ID înainte de plată, ceea ce protejează modelele "
            "de fraudă. Folosește un nume de scenă, nu împărtăși niciodată date personale în "
            "cameră, activează geo-block-urile ca să ascunzi stream-ul de regiunea ta și tratează "
            "fiecare cerere a viewer-ilor ca o tranzacție. Overlay-urile și fundalul AI din "
            "SplitCam pot ascunde sau înlocui mediul tău real."
        ),
        (
            "Ce documente îmi trebuie ca să devin model pe {name}?",
            "{name} cere de obicei un act de identitate cu poză emis de stat (pașaport, permis de "
            "conducere sau carte de identitate), un selfie ținând actul în mână și un formular "
            "fiscal/de plată (W-9 pentru SUA, W-8BEN pentru non-SUA). Aprobarea durează de regulă "
            "24–72 de ore; odată aprobat, poți intra live în aceeași zi."
        ),
        (
            "Pot să dau stream pe {name} de pe telefon?",
            "{name} oferă de obicei o aplicație mobilă de broadcaster sau un broadcaster mobile-"
            "web, dar experiența este limitată — fără overlay-uri, fără a doua cameră, fără fundal "
            "AI. Pentru calitate de producție completă, transmite de pe un computer cu SplitCam și "
            "folosește telefonul ca a doua cameră (SplitCam acceptă input de tip IP-camera de pe "
            "telefoane)."
        ),
    ],
    "stream": (
        "{name} suportă OBS sau un encoder extern?",
        "Da — {name} furnizează un URL de server RTMP și o stream key în panoul de broadcaster. "
        "Lipește-le pe ambele în <strong>Stream Settings → Custom RTMP</strong> din SplitCam, "
        "setează 1920×1080 la 30 fps cu un bitrate de 4.000–5.000 Kbps și apasă "
        "<strong>Go Live</strong>. Ruta Custom RTMP îți oferă compoziția completă a scenei din "
        "SplitCam (multi-cameră, overlay-uri, filtre)."
    ),
    "vcam": (
        "Pot folosi SplitCam ca o cameră virtuală pe {name}?",
        "Da — live-ul de pe {name} rulează în browser, așa că SplitCam se înregistrează ca o "
        "cameră web numită <strong>\"SplitCam Video Driver\"</strong>. Deschide broadcaster-ul "
        "{name}, dă click pe selectorul de cameră din browser și alege SplitCam. Scena ta "
        "compusă (overlay-uri, a doua cameră, filtre, fundal AI) ajunge la viewer-i ca un "
        "singur feed de cameră web."
    ),
}
