# -*- coding: utf-8 -*-
LOVENSE_METHODS_BG = {
    "heading": "Настройка на Lovense в SplitCam — 3 стъпки",
    "lead": "Това повтаря собствената тристъпкова настройка на Lovense. <strong>Cam Extension</strong> отчита бакшишите от твоя кам сайт, <strong>Lovense Connect</strong> е Bluetooth мостът към играчката ти, а <strong>SplitCam Toolset</strong> добавя Lovense overlay-а вътре в SplitCam, който излъчва по RTMP. Всичко е безплатно; бутоните за изтегляне се напасват автоматично към твоята система.",
    "stage_word": "Стъпка",
    "get_label": "Изтегли",
    "do_label": "После",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Отчита бакшишите от твоя кам сайт — инсталира се в Chrome или Edge.",
            "get": ["camext"],
            "steps": [
                "Изтегли Cam Extension и разархивирай папката.",
                "Отвори <strong>chrome://extensions</strong> (или <strong>edge://extensions</strong>), включи <strong>Developer mode</strong> горе вдясно, натисни <strong>Load unpacked</strong> и избери разархивираната папка <em>lovense_cam</em>.",
                "Натисни иконата на Lovense в лентата с инструменти и влез с твоя Lovense акаунт."
            ]
        },
        {
            "title": "Lovense Connect",
            "role": "Мостът, който комуникира с играчката ти по Bluetooth.",
            "get": ["connect"],
            "steps": [
                "На компютър: инсталирай Lovense Connect (препоръчва се USB Bluetooth адаптер на Lovense). На телефон: свали приложението Lovense Connect от Google Play или App Store.",
                "Включи играчката и я сдвои в Connect, докато покаже, че е свързана. В приложението на телефона сканирай QR кода, показан на компютъра, за да ги свържеш."
            ]
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Показва Lovense overlay-а в SplitCam и излъчва твоя стрийм.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Инсталирай SplitCam, след това инсталирай Lovense SplitCam Toolset — плъгина, който добавя Lovense overlay-а към SplitCam.",
                "В Cam Extension натисни <strong>+</strong>, за да добавиш своя кам сайт (Chaturbate, Stripchat, …) и настрой tip меню-то, после отвори раздела <strong>Video Feedback</strong> и избери <strong>SplitCam</strong> от списъка (OBS / SplitCam / Streamster).",
                "В SplitCam добави източника <strong>Lovense</strong>, който Toolset регистрира — overlay-ът с tip меню-то / статуса на играчката се появява в сцената ти. Дръж го над останалите слоеве.",
                "Добави камерата си, постави RTMP ключа на твоя кам сайт в <strong>Stream Settings</strong> на SplitCam и натисни <strong>Go Live</strong> — overlay-ът и играчката реагират на бакшишите."
            ]
        }
    ]
}
