# -*- coding: utf-8 -*-
LOVENSE_METHODS_SR = {
    "heading": "Подеси Lovense у SplitCam-у — 3 корака",
    "lead": "Ово прати Lovense-ово сопствено подешавање у три корака. <strong>Cam Extension</strong> чита напојнице са твог кам-сајта, <strong>Lovense Connect</strong> је Bluetooth мост до твоје играчке, а <strong>SplitCam Toolset</strong> убацује Lovense оверлеј у SplitCam, који емитује преко RTMP-а. Све је бесплатно; дугмад за преузимање се аутоматски прилагођавају твом систему.",
    "stage_word": "Корак",
    "get_label": "Преузми",
    "do_label": "Затим",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Чита напојнице са твог кам-сајта — инсталира се у Chrome или Edge.",
            "get": [
                "camext"
            ],
            "steps": [
                "Преузми Cam Extension и распакуј га.",
                "Отвори <strong>chrome://extensions</strong> (или <strong>edge://extensions</strong>), укључи <strong>Developer mode</strong> горе десно, кликни <strong>Load unpacked</strong> и изабери распаковани <em>lovense_cam</em> фолдер.",
                "Кликни на Lovense иконицу у траци са алаткама и пријави се својим Lovense налогом."
            ]
        },
        {
            "title": "Lovense Connect",
            "role": "Мост који комуницира са твојом играчком преко Bluetooth-а.",
            "get": [
                "connect"
            ],
            "steps": [
                "На рачунару: инсталирај Lovense Connect (препоручује се Lovense USB Bluetooth адаптер). На телефону: преузми Lovense Connect апликацију са Google Play-а или App Store-а.",
                "Укључи играчку и упари је у Connect-у док не покаже да је повезана. У апликацији на телефону скенирај QR код приказан на рачунару да их повежеш."
            ]
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Приказује Lovense оверлеј у SplitCam-у и емитује твој стрим.",
            "get": [
                "splitcam",
                "toolset"
            ],
            "steps": [
                "Инсталирај SplitCam, затим инсталирај Lovense SplitCam Toolset — додатак који убацује Lovense оверлеј у SplitCam.",
                "У Cam Extension-у кликни <strong>+</strong> да додаш свој кам-сајт (Chaturbate, Stripchat, …) и подеси мени напојница, затим отвори картицу <strong>Video Feedback</strong> и изабери <strong>SplitCam</strong> са листе (OBS / SplitCam / Streamster).",
                "У SplitCam-у додај <strong>Lovense</strong> извор који је Toolset регистровао — оверлеј са менијем напојница / статусом играчке појављује се на твојој сцени. Држи га изнад осталих слојева.",
                "Додај своју камеру, налепи RTMP кључ свог кам-сајта у SplitCam-ове <strong>Stream Settings</strong> и кликни <strong>Go Live</strong> — оверлеј и играчка реагују на напојнице."
            ]
        }
    ]
}
