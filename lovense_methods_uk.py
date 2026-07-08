# -*- coding: utf-8 -*-
LOVENSE_METHODS_UK = {
    "heading": "Налаштуйте Lovense у SplitCam — 3 кроки",
    "lead": "Це повторює власне налаштування Lovense у три кроки. <strong>Cam Extension</strong> зчитує "
            "чайові з вашого кам-сайту, <strong>Lovense Connect</strong> — це Bluetooth-міст до "
            "вашої іграшки, а <strong>SplitCam Toolset</strong> додає оверлей Lovense усередину "
            "SplitCam, який транслює через RTMP. Усе безкоштовно; кнопки завантаження автоматично "
            "підбираються під вашу систему.",
    "stage_word": "Крок",
    "get_label": "Завантажити",
    "do_label": "Далі",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Зчитує чайові з вашого кам-сайту — встановлюється у Chrome або Edge.",
            "get": ["camext"],
            "steps": [
                "Завантажте Cam Extension і розпакуйте архів.",
                "Відкрийте <strong>chrome://extensions</strong> (або <strong>edge://extensions</strong>), "
                "увімкніть <strong>Developer mode</strong> угорі праворуч, натисніть <strong>Load unpacked</strong> "
                "і виберіть розпаковану теку <em>lovense_cam</em>.",
                "Натисніть іконку Lovense на панелі інструментів і увійдіть у свій акаунт Lovense.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Міст, що спілкується з вашою іграшкою через Bluetooth.",
            "get": ["connect"],
            "steps": [
                "На комп'ютері: встановіть Lovense Connect (рекомендуємо USB Bluetooth-адаптер Lovense). "
                "На телефоні: завантажте застосунок Lovense Connect із Google Play або App Store.",
                "Увімкніть іграшку та підключіть її у Connect, доки не з'явиться статус підключено. У застосунку "
                "на телефоні відскануйте QR-код, показаний на комп'ютері, щоб зв'язати їх.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Показує оверлей Lovense у SplitCam і транслює ваш стрім.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Встановіть SplitCam, а потім встановіть Lovense SplitCam Toolset — плагін, який додає "
                "оверлей Lovense у SplitCam.",
                "У Cam Extension натисніть <strong>+</strong>, щоб додати свій кам-сайт (Chaturbate, "
                "Stripchat, …) і налаштуйте меню чайових, потім відкрийте вкладку <strong>Video Feedback</strong> "
                "і виберіть <strong>SplitCam</strong> зі списку (OBS / SplitCam / Streamster).",
                "У SplitCam додайте джерело <strong>Lovense</strong>, яке зареєстрував Toolset — оверлей "
                "меню чайових / статусу іграшки з'явиться на вашій сцені. Тримайте його над іншими шарами.",
                "Додайте свою камеру, вставте RTMP-ключ вашого кам-сайту у <strong>Stream "
                "Settings</strong> у SplitCam і натисніть <strong>Go Live</strong> — оверлей та іграшка реагують на чайові.",
            ],
        },
    ],
}
