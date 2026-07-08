# -*- coding: utf-8 -*-
LOVENSE_METHODS_HR = {
    "heading": "Postavi Lovense na SplitCam — 3 koraka",
    "lead": "Ovo prati Lovenseovo vlastito postavljanje u tri koraka. <strong>Cam Extension</strong> čita "
            "napojnice s tvoje cam stranice, <strong>Lovense Connect</strong> je Bluetooth most do "
            "tvoje igračke, a <strong>SplitCam Toolset</strong> stavlja Lovense overlay unutar "
            "SplitCama, koji emitira putem RTMP-a. Sve je besplatno; gumbi za preuzimanje automatski "
            "se prilagođavaju tvom sustavu.",
    "stage_word": "Korak",
    "get_label": "Preuzmi",
    "do_label": "Zatim",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Čita napojnice s tvoje cam stranice — instalira se u Chrome ili Edge.",
            "get": ["camext"],
            "steps": [
                "Preuzmi Cam Extension i raspakiraj ga.",
                "Otvori <strong>chrome://extensions</strong> (ili <strong>edge://extensions</strong>), "
                "uključi <strong>Developer mode</strong> u gornjem desnom kutu, klikni <strong>Load unpacked</strong> "
                "i odaberi raspakiranu <em>lovense_cam</em> mapu.",
                "Klikni ikonu Lovensea u alatnoj traci i prijavi se sa svojim Lovense računom.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Most koji komunicira s tvojom igračkom putem Bluetootha.",
            "get": ["connect"],
            "steps": [
                "Na računalu: instaliraj Lovense Connect (preporučuje se Lovense USB Bluetooth adapter). "
                "Na telefonu: nabavi aplikaciju Lovense Connect s Google Playa ili App Storea.",
                "Uključi igračku i upari je u Connectu dok ne pokaže da je povezana. U aplikaciji na telefonu "
                "skeniraj QR kôd prikazan na računalu da ih povežeš.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Prikazuje Lovense overlay u SplitCamu i emitira tvoj stream.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Instaliraj SplitCam, zatim instaliraj Lovense SplitCam Toolset — dodatak koji dodaje "
                "Lovense overlay u SplitCam.",
                "U Cam Extensionu klikni <strong>+</strong> da dodaš svoju cam stranicu (Chaturbate, "
                "Stripchat, …) i postavi izbornik napojnica, zatim otvori karticu <strong>Video Feedback</strong> "
                "i odaberi <strong>SplitCam</strong> s popisa (OBS / SplitCam / Streamster).",
                "U SplitCamu dodaj izvor <strong>Lovense</strong> koji je Toolset registrirao — overlay s "
                "izbornikom napojnica / statusom igračke pojavljuje se na tvojoj sceni. Drži ga iznad ostalih slojeva.",
                "Dodaj svoju kameru, zalijepi RTMP ključ svoje cam stranice u SplitCamove <strong>Stream "
                "Settings</strong> i klikni <strong>Go Live</strong> — overlay i igračka reagiraju na napojnice.",
            ],
        },
    ],
}
