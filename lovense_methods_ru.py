# -*- coding: utf-8 -*-
LOVENSE_METHODS_RU = {
    "heading": "Настройка Lovense в SplitCam — 3 шага",
    "lead": "Это в точности повторяет фирменную настройку Lovense из трёх шагов. "
            "<strong>Cam Extension</strong> считывает чаевые с вашего кам-сайта, "
            "<strong>Lovense Connect</strong> — это Bluetooth-мост к вашей игрушке, а "
            "<strong>SplitCam Toolset</strong> добавляет оверлей Lovense прямо в SplitCam, "
            "который вещает по RTMP. Всё бесплатно, а кнопки загрузки сами определяют вашу систему.",
    "stage_word": "Шаг",
    "get_label": "Скачать",
    "do_label": "Дальше",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Считывает чаевые с вашего кам-сайта — ставится в Chrome или Edge.",
            "get": ["camext"],
            "steps": [
                "Скачайте Cam Extension и распакуйте архив.",
                "Откройте <strong>chrome://extensions</strong> (или <strong>edge://extensions</strong>), "
                "включите <strong>Developer mode</strong> в правом верхнем углу, нажмите "
                "<strong>Load unpacked</strong> и выберите распакованную папку <em>lovense_cam</em>.",
                "Нажмите на иконку Lovense на панели и войдите в свой аккаунт Lovense.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Мост, который общается с вашей игрушкой по Bluetooth.",
            "get": ["connect"],
            "steps": [
                "На компьютере: установите Lovense Connect (лучше с USB Bluetooth-адаптером Lovense). "
                "На телефоне: скачайте приложение Lovense Connect из Google Play или App Store.",
                "Включите игрушку и подключите её в Connect — дождитесь статуса «подключено». "
                "В приложении на телефоне отсканируйте QR-код с экрана компьютера, чтобы связать их.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Показывает оверлей Lovense в SplitCam и вещает вашу трансляцию.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Установите SplitCam, затем поставьте Lovense SplitCam Toolset — плагин, который "
                "добавляет оверлей Lovense в SplitCam.",
                "В Cam Extension нажмите <strong>+</strong>, добавьте свой кам-сайт (Chaturbate, "
                "Stripchat, …) и настройте меню чаевых, затем откройте вкладку "
                "<strong>Video Feedback</strong> и выберите <strong>SplitCam</strong> из списка "
                "(OBS / SplitCam / Streamster).",
                "В SplitCam добавьте источник <strong>Lovense</strong>, который зарегистрировал "
                "Toolset — на сцене появится оверлей с меню чаевых и статусом игрушки. Держите его "
                "поверх остальных слоёв.",
                "Добавьте камеру, вставьте RTMP-ключ вашего кам-сайта в <strong>Stream Settings</strong> "
                "SplitCam и нажмите <strong>Go Live</strong> — оверлей и игрушка реагируют на чаевые.",
            ],
        },
    ],
}
