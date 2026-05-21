# -*- coding: utf-8 -*-
"""Russian content for cam-streaming-guides. Genuinely per-platform, FAQ-enriched."""

_T_ETH = ("Проводное подключение", "Ethernet надёжнее Wi-Fi для долгого эфира — обрыв кадра это "
          "потерянный токен. Протяните кабель к стрим-ПК.")
_T_TEST = ("Сначала приватный тест", "Короткая тестовая трансляция проверит камеру, звук, "
           "кадрирование и накладки до открытия комнаты.")

PLATFORMS_RU = [
    {
        "slug": "chaturbate", "name": "Chaturbate",
        "title": "Как вести трансляцию на Chaturbate через SplitCam — токен и RTMP",
        "desc": "Вещание на Chaturbate через бесплатный SplitCam. Возьмите broadcast-токен в "
                "Broadcast Yourself, направьте внешний кодировщик через SplitCam — сцены, "
                "накладки, без водяного знака.",
        "kw": "как вести трансляцию на chaturbate, chaturbate broadcast token, chaturbate rtmp obs, "
              "chaturbate внешний кодировщик",
        "h1html": 'Как вести трансляцию на <span class="accent">Chaturbate</span> через SplitCam',
        "h1short": "Трансляция на Chaturbate",
        "card": "Настройка через токен и внешний кодировщик Chaturbate.",
        "intro": "Chaturbate — одна из крупнейших кам-платформ с токен-экономикой. Её браузерный "
                 "вещатель — одна простая камера; маршрут через "
                 "<strong style='color:var(--text)'>внешний кодировщик</strong> с бесплатным "
                 "<strong style='color:var(--text)'>SplitCam</strong> открывает сцены с "
                 "несколькими камерами, накладки и фильтры на том же токен-потоке.",
        "quick": "Вещание на Chaturbate через SplitCam: установите SplitCam, соберите сцену, "
                 "откройте <em>Broadcast Yourself → My Broadcast</em>, скопируйте broadcast-токен, "
                 "вставьте в SplitCam, нажмите Go Live."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Скопируйте broadcast-токен Chaturbate.</li><li>Вставьте в SplitCam.</li>"
                 "<li>Нажмите Go Live.</li></ol>",
        "key_how": "На Chaturbate нажмите <strong>Broadcast Yourself</strong> — откроется "
                   "страница <strong>My Broadcast</strong>, затем <strong>View RTMP/OBS broadcast "
                   "information and stream key</strong>. Ключ показан как ваш "
                   "<strong>broadcast-токен</strong> — скопируйте его. Работает как пароль, "
                   "публично не выкладывайте.",
        "tips": [
            ("Токен — это ключ", "Chaturbate использует broadcast-токен вместо обычного ключа "
             "трансляции. Берегите как пароль, сбросьте если утёк."),
            ("Большой запас по качеству", "RTMP-приём Chaturbate принимает до 4K, 60 fps и очень "
             "высокий битрейт — качество ограничивает ваш аплоад, а не платформа. Интервал "
             "ключевых кадров — 2 секунды."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Chaturbate разрешает OBS / внешние кодировщики?", "Да — Chaturbate официально "
             "поддерживает внешние кодировщики и имеет свою статью «How do I set up OBS?». "
             "Включается через «Use External Encoder to Broadcast» в настройках вещания."),
            ("Где ключ трансляции Chaturbate?", "Broadcast Yourself → My Broadcast → View "
             "RTMP/OBS broadcast information and stream key. Ключ — это broadcast-токен."),
            ("Какое разрешение и fps поддерживает Chaturbate?", "RTMP-приём Chaturbate принимает "
             "до 3840×2160 (4K) и 60 fps с 2-секундным интервалом ключевых кадров — куда больше "
             "запаса, чем у большинства кам-платформ."),
            ("Какой битрейт для Chaturbate?", "3500–6000 Кбит/с для 1080p достаточно. Потолок "
             "Chaturbate очень высокий, так что реальный предел — ваш аплоад; проверьте его "
             "тестом скорости SplitCam."),
        ],
    },
    {
        "slug": "cam4", "name": "CAM4",
        "title": "Как вести трансляцию на CAM4 через SplitCam — внешний кодировщик",
        "desc": "Вещание на CAM4 через бесплатный SplitCam. Откройте Broadcast & Earn Money, "
                "External Encoder, Get Stream Key, гео-настройки — сцены и накладки.",
        "kw": "как вести трансляцию на cam4, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
        "h1html": 'Как вести трансляцию на <span class="accent">CAM4</span> через SplitCam',
        "h1short": "Трансляция на CAM4",
        "card": "External Encoder CAM4 + гео-настройки.",
        "intro": "CAM4 — глобальная кам-платформа со встроенными гео-настройками: можно скрыть "
                 "эфир в выбранных странах. Маршрут через бесплатный "
                 "<strong style='color:var(--text)'>SplitCam</strong> как внешний кодировщик "
                 "даёт переключение сцен и накладки, которых нет у базового вещателя.",
        "quick": "Вещание на CAM4 через SplitCam: установите SplitCam, соберите сцену, на CAM4 "
                 "откройте <em>Broadcast &amp; Earn Money → Start Broadcast → External "
                 "Encoder</em>, Get Stream Key, вставьте в SplitCam, Go Live."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Получите ключ CAM4.</li><li>Вставьте в SplitCam.</li>"
                 "<li>Нажмите Go Live.</li></ol>",
        "key_how": "На CAM4 нажмите <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn "
                   "Money</strong> → <strong>Start Broadcast</strong>, затем "
                   "<strong>External Encoder</strong> сверху. Заполните дату рождения, пол и "
                   "страну, нажмите <strong>Get Stream Key</strong> и скопируйте ключ. Зелёный "
                   "слайдер в Stream Settings SplitCam подтверждает подключение.",
        "tips": [
            ("Настройте гео-ограничения", "CAM4 позволяет скрыть эфир в конкретных странах и "
             "регионах — задайте это на стороне CAM4 до выхода в эфир, если нужно."),
            ("Следите за зелёным слайдером", "При настройке CAM4 в Stream Settings SplitCam "
             "появляется зелёный слайдер при принятом ключе — красный значит проверьте ключ."),
            ("Битрейт ниже обычного", "Приём CAM4 ограничивает видеобитрейт примерно 3000 "
             "Кбит/с — ниже, чем у большинства кам-сайтов. Не задирайте выше."),
            _T_ETH,
        ],
        "faq": [
            ("CAM4 официально поддерживает OBS / внешние кодировщики?", "Да — у CAM4 есть "
             "официальный OBS Guide на сайте поддержки, и платформа рекомендует опцию External "
             "Encoder. SplitCam использует тот же RTMP-путь."),
            ("Можно ли гео-блокировать эфир на CAM4?", "Да — у CAM4 есть встроенное гео-"
             "ограничение, чтобы скрыть эфир в некоторых странах. Настраивается на CAM4."),
            ("Где ключ трансляции CAM4?", "Broadcast → Broadcast & Earn Money → Start Broadcast "
             "→ External Encoder → Get Stream Key."),
            ("Какой битрейт для CAM4?", "Ниже, чем у большинства: приём CAM4 ограничивает "
             "видеобитрейт ~3000 Кбит/с при 30 fps и 1-секундном интервале ключевых кадров. В "
             "официальном OBS Guide CAM4 есть таблица по тесту скорости — выше ~3000 не нужно."),
        ],
    },
    {
        "slug": "bongacams", "name": "BongaCams",
        "title": "Как вести трансляцию на BongaCams через SplitCam — внешний кодировщик",
        "desc": "Вещание на BongaCams через бесплатный SplitCam. Broadcast settings → Select "
                "Encoder → External Encoder. Если кнопки нет — её включает поддержка.",
        "kw": "как вести трансляцию на bongacams, bongacams external encoder, bongacams rtmp obs",
        "h1html": 'Как вести трансляцию на <span class="accent">BongaCams</span> через SplitCam',
        "h1short": "Трансляция на BongaCams",
        "card": "External Encoder BongaCams.",
        "intro": "BongaCams — глобальная кам-платформа. Вещание через внешний кодировщик там "
                 "включено не всегда по умолчанию — после включения бесплатный "
                 "<strong style='color:var(--text)'>SplitCam</strong> ведёт эфир со сценами, "
                 "накладками и AI-фоном.",
        "quick": "Вещание на BongaCams через SplitCam: установите SplitCam, соберите сцену, на "
                 "BongaCams откройте <em>Options → Broadcast settings → Select Encoder → External "
                 "Encoder</em>, скопируйте URL и ключ, вставьте в SplitCam, Go Live."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Получите URL и ключ BongaCams.</li><li>Вставьте в SplitCam.</li>"
                 "<li>Нажмите Go Live.</li></ol>",
        "key_how": "На BongaCams откройте <strong>Options</strong> → <strong>Broadcast "
                   "settings</strong> → <strong>Select Encoder</strong> → <strong>External "
                   "Encoder</strong> и скопируйте показанные URL сервера и ключ. "
                   "<strong>Если кнопки External Encoder нет</strong> — напишите в поддержку "
                   "BongaCams и попросите включить внешнее кодирование для вашего аккаунта.",
        "tips": [
            ("Нет кнопки External Encoder? Поддержка", "BongaCams гейтит внешнее кодирование — "
             "если опции нет в Broadcast settings, её включает поддержка."),
            ("Совпадение разрешения", "BongaCams рекомендует, чтобы разрешение веб-камеры и "
             "трансляции совпадали — например, оба 1280×720."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Почему нет кнопки External Encoder на BongaCams?", "Внешнее кодирование включено "
             "не для каждого аккаунта — напишите в поддержку BongaCams, и кнопка появится в "
             "Broadcast settings."),
            ("Нужна ли верификация аккаунта на BongaCams?", "Да — для вещания нужно быть 18+, "
             "иметь действующий гос. документ для проверки возраста и пройти одобрение аккаунта "
             "до выхода в эфир."),
            ("Какой битрейт для BongaCams?", "RTMP-приём BongaCams ограничивает видеобитрейт "
             "примерно 6000 Кбит/с при 2-секундном интервале ключевых кадров — 3500–6000 для "
             "1080p оптимально; сначала проверьте аплоад."),
            ("SplitCam бесплатен для BongaCams?", "Да — бесплатно, без водяного знака, без "
             "лимитов."),
        ],
    },
    {
        "slug": "stripchat", "name": "Stripchat",
        "title": "Как вести трансляцию на Stripchat через SplitCam — внешний софт",
        "desc": "Вещание на Stripchat через бесплатный SplitCam. Switch to external software, "
                "скопируйте ключ-токен, ведите сцены и накладки. Без водяного знака.",
        "kw": "как вести трансляцию на stripchat, stripchat external software, stripchat ключ, "
              "stripchat rtmp obs",
        "h1html": 'Как вести трансляцию на <span class="accent">Stripchat</span> через SplitCam',
        "h1short": "Трансляция на Stripchat",
        "card": "Настройка внешнего софта для Stripchat.",
        "intro": "Stripchat — крупная кам-платформа с упором на интерактив. Режим <em>external "
                 "software</em> выдаёт ключ-токен — передайте его бесплатному "
                 "<strong style='color:var(--text)'>SplitCam</strong>, чтобы вещать со сценами, "
                 "накладками и фильтрами вместо одной плоской камеры.",
        "quick": "Вещание на Stripchat через SplitCam: установите SplitCam, соберите сцену, на "
                 "Stripchat выберите <em>Switch to external software</em>, скопируйте ключ, "
                 "вставьте в SplitCam, Go Live."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Получите ключ Stripchat.</li><li>Вставьте в SplitCam.</li>"
                 "<li>Нажмите Go Live.</li></ol>",
        "key_how": "На Stripchat выберите <strong>Switch to external software</strong>, затем "
                   "откройте <strong>Show external software settings for the stream</strong>. "
                   "Скопируйте ключ трансляции — Stripchat показывает его как токен. Держите в "
                   "секрете.",
        "tips": [
            ("Точно совпадайте по разрешению", "FAQ Stripchat предупреждает: разрешение в вашей "
             "программе должно точно совпадать с разрешением на сайте, иначе картинка "
             "пикселит. Ставьте одинаковое."),
            ("Помните про порог 2 Мбит/с", "Stripchat указывает 2 Мбит/с аплоада как минимум — "
             "и явно отмечает, что этого НЕ хватит для вещания через OBS или одновременной "
             "мультитрансляции. Берите с большим запасом."),
            ("Ключ — это токен", "Ключ трансляции Stripchat это токен — копируйте точно, не "
             "делитесь, сбросьте при утечке."),
            _T_ETH,
        ],
        "faq": [
            ("Stripchat рекомендует OBS / внешний софт?", "Да — собственный FAQ Stripchat "
             "советует внешние программы вроде OBS «для лучшего качества видео и звука». "
             "SplitCam работает так же."),
            ("Как переключить Stripchat на внешний софт?", "В Broadcast Center выберите Switch "
             "to External Broadcast Software (OBS), затем откройте настройки внешнего софта — "
             "там будет ключ (токен)."),
            ("Какой битрейт для Stripchat?", "RTMP-приём принимает до ~6000 Кбит/с при "
             "2-секундном интервале ключевых кадров. 3500–6000 для 1080p оптимально — но нужен "
             "запас сильно выше минимума 2 Мбит/с, особенно при вещании через OBS."),
            ("SplitCam бесплатен для Stripchat?", "Да — бесплатно, без водяного знака, без "
             "лимитов."),
        ],
    },
    {
        "slug": "onlyfans", "name": "OnlyFans",
        "title": "Как выйти в эфир на OnlyFans через SplitCam — авторизация или ключ",
        "desc": "Прямой эфир на OnlyFans через бесплатный SplitCam. Подключение через "
                "авторизацию (вошёл один раз — ключ синхронизируется сам) или вручную через "
                "OBS Key — сцены, накладки, без водяного знака.",
        "kw": "как выйти в эфир на onlyfans, onlyfans авторизация splitcam, onlyfans obs key, "
              "onlyfans прямой эфир, onlyfans программа трансляции",
        "h1html": 'Как выйти в эфир на <span class="accent">OnlyFans</span> через SplitCam',
        "h1short": "Эфир на OnlyFans",
        "card": "Авторизуйтесь один раз или вставьте ключ — эфир на OnlyFans.",
        "intro": "Прямой эфир OnlyFans идёт для ваших подписчиков. SplitCam подключается "
                 "<strong style='color:var(--text)'>двумя способами</strong> — войдите один "
                 "раз под своим логином OnlyFans, и SplitCam сам заберёт ключ трансляции и "
                 "будет держать его синхронизированным, либо вставьте OBS Key вручную. В любом "
                 "случае вы вещаете со сценами, накладками и фильтрами.",
        "quick": "Эфир на OnlyFans через SplitCam: установите SplitCam, соберите сцену, "
                 "откройте Stream Settings &rarr; Add Channel &rarr; OnlyFans и выберите "
                 "<em>Авторизацию</em> — войдите под логином OnlyFans, и SplitCam сам подтянет "
                 "ключ трансляции — затем нажмите Go Live. Аккаунт подключён, поэтому настройки "
                 "OnlyFans можно менять прямо в SplitCam, не заходя на сайт OnlyFans.",
        "steps": [
            ("Скачайте и установите SplitCam",
             "SplitCam — бесплатная программа для трансляций на Windows и macOS — без "
             "регистрации, без карты, без водяного знака. Именно она отправляет видео на "
             "OnlyFans."),
            ("Настройте камеру и сцену",
             "Откройте SplitCam и добавьте веб-камеру. Соберите сцену, которую увидят зрители "
             "— накладки, текст, вторая камера, бьюти-фильтры или AI-фон, применяются вживую."),
            ("Подключение — Способ 1: Авторизация (рекомендуется)",
             "В SplitCam откройте <strong>Stream Settings</strong> &rarr; <strong>Add "
             "Channel</strong> &rarr; <strong>OnlyFans</strong> и выберите "
             "<strong>Авторизацию</strong>. Войдите под email и паролем OnlyFans. SplitCam "
             "подключается к вашему аккаунту, сам забирает ключ трансляции и держит его "
             "синхронизированным — и позволяет управлять настройками эфира OnlyFans прямо в "
             "SplitCam, меняя их во время стрима или после, не заходя на сайт OnlyFans."),
            ("Подключение — Способ 2: Stream Key (вручную)",
             "Не хотите входить в аккаунт? Используйте ключ. На OnlyFans откройте "
             "<strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; раздел "
             "<strong>Other</strong> и скопируйте <strong>OBS Key</strong>. В SplitCam: Add "
             "Channel &rarr; OnlyFans, вставьте его в поле ключа. Этот ключ статичный — чтобы "
             "поменять настройки потом, придётся снова зайти на сайт OnlyFans."),
            ("Нажмите Go Live",
             "Каким бы способом ни подключились, нажмите <strong>Go Live</strong> в SplitCam. "
             "Со Способом 1 настройки OnlyFans можно продолжать менять из SplitCam на ходу; со "
             "Способом 2 ключ остаётся ровно таким, как задан."),
        ],
        "tips": [
            ("Авторизация против Stream Key", "Два способа подключения: "
             "<strong>Авторизация</strong> (вошёл один раз — ключ забирается и держится "
             "синхронизированным, проще всего) или <strong>Stream Key</strong> (скопировать "
             "OBS Key в OnlyFans → Profile → Settings → Other и вставить). Авторизация не "
             "требует ручного копирования."),
            ("Меняйте настройки не выходя из SplitCam", "При авторизации аккаунт остаётся "
             "подключённым, поэтому настройки эфира OnlyFans можно менять прямо в SplitCam "
             "посреди стрима или после — без захода на сайт OnlyFans."),
            ("Битрейт держите низким", "RTMP-приём OnlyFans ограничивает видеобитрейт примерно "
             "2500 Кбит/с — строже большинства кам-сайтов. Цельтесь в 720p–1080p при "
             "~2000–2500."),
            _T_ETH,
        ],
        "faq": [
            ("Как подключить OnlyFans к SplitCam?", "Двумя способами. "
             "<strong>Авторизация</strong> — Stream Settings → Add Channel → OnlyFans → войти "
             "под логином OnlyFans, и SplitCam сам заберёт ключ трансляции. Либо <strong>Stream "
             "Key</strong> — скопировать OBS Key в OnlyFans → Profile → Settings → Other и "
             "вставить."),
            ("Можно менять настройки эфира OnlyFans не заходя на сайт?", "Да — при способе "
             "Авторизация SplitCam остаётся подключённым к вашему аккаунту OnlyFans, и ключ с "
             "настройками синхронизируются автоматически. Их можно менять прямо в SplitCam во "
             "время стрима или после него, не заходя на onlyfans.com."),
            ("Какой битрейт для OnlyFans?", "Держите скромным — RTMP-приём OnlyFans "
             "ограничивает видеобитрейт примерно 2500 Кбит/с, куда строже большинства кам-"
             "платформ. Цельтесь в 720p–1080p при ~2000–2500 Кбит/с."),
            ("SplitCam бесплатен для эфиров OnlyFans?", "Да — бесплатно, без водяного знака, "
             "без лимита."),
        ],
    },
    {
        "slug": "camplace", "name": "CamPlace",
        "title": "Как вести трансляцию на CamPlace через SplitCam — гайд",
        "desc": "Вещание на CamPlace через бесплатный SplitCam — внешний кодировщик, сцены с "
                "камерами, накладки и фильтры. Пошагово, без водяного знака.",
        "kw": "как вести трансляцию на camplace, camplace программа трансляции, camplace rtmp",
        "h1html": 'Как вести трансляцию на <span class="accent">CamPlace</span> через SplitCam',
        "h1short": "Трансляция на CamPlace",
        "card": "Настройка внешнего кодировщика для CamPlace.",
        "intro": "CamPlace — кам-платформа. Публичной статьи про OBS у неё нет, поэтому "
                 "<strong style='color:var(--text)'>видео-гайд выше</strong> — основной "
                 "ориентир. Бесплатный <strong style='color:var(--text)'>SplitCam</strong> "
                 "подключается по стандартному RTMP и добавляет сцены, накладки и AI-фон, "
                 "которых нет у базовой камеры.",
        "quick": "Вещание на CamPlace через SplitCam: установите SplitCam, соберите сцену, "
                 "включите внешнее/RTMP-вещание в CamPlace, скопируйте URL сервера и ключ, "
                 "вставьте в SplitCam, Go Live. Следуйте видео-гайду выше для актуального пути."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Получите RTMP-ключ CamPlace.</li><li>Вставьте в SplitCam.</li>"
                 "<li>Нажмите Go Live.</li></ol>",
        "key_how": "Войдите в CamPlace и откройте настройки вещания. Переключитесь на внешний "
                   "кодировщик / RTMP / OBS, чтобы увидеть <strong>URL сервера</strong> и "
                   "<strong>ключ трансляции</strong>, скопируйте оба. Официальной документации "
                   "по OBS у CamPlace нет, поэтому <strong>видео-гайд выше</strong> — самый "
                   "надёжный разбор текущего интерфейса.",
        "tips": [
            ("Нет официального OBS-гайда — смотрите видео", "У CamPlace нет публичной статьи "
             "поддержки про внешние кодировщики; видео-гайд выше — ориентир по актуальному "
             "пути."),
            ("Стандартный RTMP работает", "Даже без документации CamPlace принимает стандартный "
             "URL RTMP-сервера и ключ — SplitCam подключается обычной пользовательской "
             "RTMP-площадкой."),
            ("Накладки в SplitCam", "Цели по токенам, ник и соцсети как слои сцены — базовая "
             "камера CamPlace так не умеет."),
            _T_ETH,
        ],
        "faq": [
            ("Есть ли у CamPlace официальный OBS-гайд?", "Публичной статьи поддержки про "
             "внешние кодировщики не найдено. CamPlace принимает стандартный URL RTMP и ключ, "
             "так что SplitCam работает — следуйте видео-гайду выше для актуального пути."),
            ("CamPlace поддерживает внешние кодировщики?", "Да — принимает стандартный RTMP-"
             "ключ, так что SplitCam подключается пользовательской RTMP-площадкой."),
            ("SplitCam бесплатен для CamPlace?", "Да — бесплатно, без водяного знака, без лимита."),
            ("Какой битрейт для CamPlace?", "3500–6000 Кбит/с для 1080p; проверьте аплоад."),
        ],
    },
    {
        "slug": "camsoda", "name": "CamSoda",
        "title": "Как вести трансляцию на CamSoda через SplitCam — гайд",
        "desc": "Вещание на CamSoda через бесплатный SplitCam. Кнопка Use OBS Broadcaster, "
                "официальный OBS-гайд в вики, региональные серверы. Без водяного знака.",
        "kw": "как вести трансляцию на camsoda, camsoda live, camsoda obs broadcaster, "
              "camsoda rtmp",
        "h1html": 'Как вести трансляцию на <span class="accent">CamSoda</span> через SplitCam',
        "h1short": "Трансляция на CamSoda",
        "card": "Настройка через Use OBS Broadcaster на CamSoda.",
        "intro": "CamSoda — американская кам-платформа, известная необычными интерактивными "
                 "форматами шоу. Она официально поддерживает вещание через OBS — на странице "
                 "Go Live есть кнопка <strong style='color:var(--text)'>Use OBS Broadcaster</strong> "
                 "и официальный OBS-гайд в вики CamSoda. Бесплатный "
                 "<strong style='color:var(--text)'>SplitCam</strong> работает так же.",
        "quick": "Вещание на CamSoda через SplitCam: установите SplitCam, соберите сцену, "
                 "нажмите Use OBS Broadcaster на странице Go Live CamSoda, скопируйте URL "
                 "сервера и ключ, вставьте в SplitCam, Go Live."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Нажмите Use OBS Broadcaster на CamSoda.</li>"
                 "<li>Вставьте URL и ключ в SplitCam.</li><li>Нажмите Go Live.</li></ol>",
        "key_how": "На странице <strong>Go Live</strong> CamSoda нажмите <strong>Use OBS "
                   "Broadcaster</strong>. CamSoda покажет URL RTMP-сервера и ключ — скопируйте "
                   "оба. Выберите ближайший региональный сервер (Северная Америка, Европа, "
                   "Азия и т.д.). В вики CamSoda есть полный OBS-гайд, если нужны детали.",
        "tips": [
            ("Пройдите верификацию для чаевых", "На CamSoda вещать может кто угодно, но чтобы "
             "получать чаевые, нужно пройти заявку на верификацию CamSoda."),
            ("Берите ближайший региональный сервер", "CamSoda даёт региональные серверы приёма "
             "— ближайший (СА / Европа / Азия / Южная Америка / Океания) снижает задержку и "
             "дропы кадров."),
            ("Потолок 1080p / 30 fps", "Приём CamSoda — примерно до 1080p, 30 fps и ~6000 "
             "Кбит/с — выше задирать не нужно."),
            _T_ETH,
        ],
        "faq": [
            ("CamSoda поддерживает OBS / внешние кодировщики?", "Да — официально. На странице "
             "Go Live есть кнопка Use OBS Broadcaster и OBS-гайд в вики CamSoda, так что "
             "SplitCam работает."),
            ("Нужна ли верификация на CamSoda?", "Чтобы вещать — нет. Чтобы получать чаевые — "
             "да: CamSoda требует сначала пройти заявку на верификацию."),
            ("Какое разрешение поддерживает CamSoda?", "До 1920×1080 при 30 fps, примерно "
             "6000 Кбит/с максимум на RTMP-приёме."),
            ("SplitCam бесплатен для CamSoda?", "Да — бесплатно, без водяного знака, без лимита."),
        ],
    },
    {
        "slug": "streamate", "name": "Streamate",
        "title": "Как вести трансляцию на Streamate через SplitCam — встроенный канал",
        "desc": "Вещание на Streamate через бесплатный SplitCam. Streamate — встроенный канал в "
                "SplitCam: SM Connect, скопируйте ключ, Add Channel → Streamate.",
        "kw": "как вести трансляцию на streamate, streamate sm connect, streamate rtmp, "
              "streamate программа трансляции",
        "h1html": 'Как вести трансляцию на <span class="accent">Streamate</span> через SplitCam',
        "h1short": "Трансляция на Streamate",
        "card": "Streamate — встроенный канал SplitCam, быстрая настройка.",
        "intro": "Streamate — устоявшаяся кам-платформа, и это одна из площадок, "
                 "<strong style='color:var(--text)'>предустановленных в SplitCam</strong> в "
                 "списке каналов — настройка быстрее ручного ввода RTMP: выбрал Streamate, "
                 "вставил ключ, готово.",
        "quick": "Вещание на Streamate через SplitCam: установите SplitCam, соберите сцену, на "
                 "Streamate через <em>SM Connect → Start Show</em> скопируйте ключ, затем в "
                 "SplitCam откройте <em>Stream Settings → Add Channel → Streamate</em> и вставьте."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Получите ключ Streamate через SM Connect.</li>"
                 "<li>Add Channel → Streamate в SplitCam.</li><li>Нажмите Go Live.</li></ol>",
        "key_how": "На Streamate откройте <strong>SM Connect</strong>, примите условия, нажмите "
                   "<strong>Start Show</strong> слева и закройте открывшееся окно — затем "
                   "скопируйте ключ трансляции. В SplitCam откройте <strong>Stream "
                   "Settings</strong> → <strong>Add Channel</strong>, выберите "
                   "<strong>Streamate</strong> из списка и вставьте ключ. Зелёный слайдер "
                   "подтверждает подключение.",
        "tips": [
            ("Streamate — встроенный канал", "Ручной RTMP-URL не нужен — Streamate есть в списке "
             "Add Channel SplitCam, просто выберите его и вставьте ключ."),
            ("Закройте окно SM Connect", "После Start Show Streamate открывает окно — закройте "
             "его; оно нужно было только чтобы показать ключ."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Streamate встроен в SplitCam?", "Да — Streamate есть в списке Add Channel SplitCam, "
             "вы выбираете его вместо ручного ввода RTMP-URL."),
            ("Где ключ трансляции Streamate?", "SM Connect → принять условия → Start Show → "
             "закрыть окно → скопировать ключ."),
            ("SplitCam бесплатен для Streamate?", "Да — бесплатно, без водяного знака, без лимита."),
            ("Какой битрейт для Streamate?", "3500–6000 Кбит/с для 1080p; проверьте аплоад."),
        ],
    },
    {
        "slug": "streamray", "name": "StreamRay",
        "title": "Как вести трансляцию на StreamRay через SplitCam — URL из чата",
        "desc": "Вещание на StreamRay через бесплатный SplitCam. StreamRay даёт URL потока в окне "
                "чата и не использует ключ — SplitCam справляется с этим.",
        "kw": "как вести трансляцию на streamray, streamray obs broadcaster, streamray cam, "
              "streamray rtmp",
        "h1html": 'Как вести трансляцию на <span class="accent">StreamRay</span> через SplitCam',
        "h1short": "Трансляция на StreamRay",
        "card": "Настройка StreamRay — URL берётся из чата.",
        "intro": "У StreamRay необычная настройка внешнего кодировщика — он выдаёт URL потока "
                 "<strong style='color:var(--text)'>прямо в окне чата</strong> трансляции и не "
                 "использует отдельный ключ. Бесплатный "
                 "<strong style='color:var(--text)'>SplitCam</strong> справляется с таким "
                 "режимом «только URL».",
        "quick": "Вещание на StreamRay через SplitCam: установите SplitCam, соберите сцену, на "
                 "StreamRay включите OBS Broadcaster, скопируйте URL потока из окна чата, "
                 "вставьте в SplitCam (поле ключа оставьте пустым), Go Live."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Скопируйте URL StreamRay из чата.</li>"
                 "<li>Вставьте URL в SplitCam.</li><li>Нажмите Go Live.</li></ol>",
        "key_how": "На StreamRay дважды нажмите <strong>Broadcast Now</strong>, откройте меню "
                   "<strong>Other</strong>, выберите <strong>OBS Broadcaster</strong> и "
                   "<strong>Save and Close</strong>. После этого StreamRay выкладывает "
                   "<strong>URL потока в окно чата</strong> — скопируйте его оттуда. Поле ключа "
                   "в SplitCam оставьте <strong>пустым</strong>; StreamRay авторизует по URL.",
        "tips": [
            ("URL — в чате", "StreamRay не показывает URL потока в окне настроек — он выкладывает "
             "его в окно чата трансляции. Копируйте оттуда."),
            ("Поле ключа оставьте пустым", "StreamRay не использует отдельный ключ — только URL. "
             "Не заполняйте поле ключа в SplitCam."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Где URL потока StreamRay?", "После включения OBS Broadcaster StreamRay выкладывает "
             "URL потока в окно чата — копируйте из чата."),
            ("Почему у StreamRay нет ключа трансляции?", "StreamRay авторизует только по URL — "
             "поле ключа в SplitCam оставьте пустым."),
            ("SplitCam бесплатен для StreamRay?", "Да — бесплатно, без водяного знака, без лимита."),
            ("Какой битрейт для StreamRay?", "3500–6000 Кбит/с для 1080p; проверьте аплоад."),
        ],
    },
    {
        "slug": "xlovecam", "name": "XLoveCam",
        "title": "Как вести трансляцию на XLoveCam через SplitCam — RTMP-ссылка и ключ",
        "desc": "Вещание на XLoveCam через бесплатный SplitCam. RTMP-ссылка и ключ в My Account "
                "→ settings, региональные серверы. Без водяного знака.",
        "kw": "как вести трансляцию на xlovecam, xlovecam rtmp, xlovecam ключ, x love cam",
        "h1html": 'Как вести трансляцию на <span class="accent">XLoveCam</span> через SplitCam',
        "h1short": "Трансляция на XLoveCam",
        "card": "RTMP-ссылка и ключ для XLoveCam.",
        "intro": "XLoveCam — европейская многоязычная кам-платформа. В настройках аккаунта есть "
                 "и <strong style='color:var(--text)'>RTMP-ссылка</strong>, и "
                 "<strong style='color:var(--text)'>ключ трансляции</strong> — бесплатный "
                 "<strong style='color:var(--text)'>SplitCam</strong> берёт оба и вещает со "
                 "сценами и накладками.",
        "quick": "Вещание на XLoveCam через SplitCam: установите SplitCam, соберите сцену, на "
                 "XLoveCam откройте <em>My Account → settings</em>, скопируйте RTMP-ссылку и "
                 "ключ, вставьте оба в SplitCam, начните шоу."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Скопируйте RTMP-ссылку и ключ XLoveCam.</li><li>Вставьте оба в SplitCam.</li>"
                 "<li>Нажмите Go Live.</li></ol>",
        "key_how": "На XLoveCam откройте <strong>My Account</strong> → <strong>settings</strong>. "
                   "В настройках есть и <strong>RTMP-ссылка</strong>, и <strong>ключ "
                   "трансляции</strong> — скопируйте оба в поля URL сервера и ключа SplitCam, "
                   "затем нажмите <strong>Start your show</strong> на XLoveCam.",
        "tips": [
            ("Копируйте и ссылку, и ключ", "XLoveCam даёт RTMP-ссылку И отдельный ключ — нужны "
             "оба в SplitCam, не только что-то одно."),
            ("Берите ближайший сервер", "XLoveCam даёт региональные серверы приёма — Европа "
             "(Нидерланды, Румыния), Северная и Южная Америка, Азия. Ближайший снижает задержку."),
            ("Многоязычная аудитория", "XLoveCam европейская и многоязычная — понятная текстовая "
             "накладка на вашем языке помогает зрителям вас найти."),
            _T_ETH,
        ],
        "faq": [
            ("Где RTMP-данные XLoveCam?", "My Account → settings — показаны и RTMP-ссылка, и ключ."),
            ("XLoveCam поддерживает внешние кодировщики?", "Да — XLoveCam даёт официальный режим "
             "вещания через OBS с RTMP-ссылкой и ключом, так что SplitCam работает."),
            ("SplitCam бесплатен для XLoveCam?", "Да — бесплатно, без водяного знака, без лимита."),
            ("Какой битрейт для XLoveCam?", "3500–6000 Кбит/с для 1080p; проверьте аплоад."),
        ],
    },
    {
        "slug": "soulcams", "name": "SoulCams",
        "title": "Как вести трансляцию на SoulCams через SplitCam — настройки OBS",
        "desc": "Вещание на SoulCams через бесплатный SplitCam. Go Online → Settings → OBS "
                "показывает RTMP-сервер и ключ вместе. Сцены, накладки.",
        "kw": "как вести трансляцию на soulcams, soulcams obs, soul cams, soulcams rtmp",
        "h1html": 'Как вести трансляцию на <span class="accent">SoulCams</span> через SplitCam',
        "h1short": "Трансляция на SoulCams",
        "card": "Настройка SoulCams через OBS-настройки.",
        "intro": "SoulCams — кам-платформа, чьи OBS-настройки показывают "
                 "<strong style='color:var(--text)'>RTMP-сервер и ключ вместе</strong> в одном "
                 "окне. Вставьте оба в бесплатный "
                 "<strong style='color:var(--text)'>SplitCam</strong>, чтобы вещать со сценами "
                 "и накладками.",
        "quick": "Вещание на SoulCams через SplitCam: установите SplitCam, соберите сцену, на "
                 "SoulCams нажмите Go Online → Settings → OBS, скопируйте сервер и ключ, "
                 "вставьте оба в SplitCam, Go Live."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Откройте SoulCams Settings → OBS.</li>"
                 "<li>Вставьте сервер и ключ в SplitCam.</li><li>Нажмите Go Live.</li></ol>",
        "key_how": "На SoulCams войдите и нажмите <strong>Go Online</strong>, затем откройте "
                   "<strong>Settings</strong> → <strong>OBS</strong>. Окно OBS показывает "
                   "<strong>RTMP-сервер</strong> и <strong>ключ</strong> вместе — скопируйте оба "
                   "в SplitCam.",
        "tips": [
            ("Сервер и ключ рядом", "SoulCams показывает RTMP-сервер и ключ в одном окне OBS — "
             "берите оба сразу."),
            ("Сначала Go Online", "Настройки OBS появляются только после нажатия Go Online на "
             "SoulCams — сделайте это до поиска данных кодировщика."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Где OBS-настройки SoulCams?", "Войдите, нажмите Go Online, затем Settings → OBS — "
             "RTMP-сервер и ключ показаны вместе."),
            ("SoulCams поддерживает внешние кодировщики?", "Да — его OBS-настройки дают "
             "RTMP-сервер и ключ, так что SplitCam работает."),
            ("SplitCam бесплатен для SoulCams?", "Да — бесплатно, без водяного знака, без лимита."),
            ("Какой битрейт для SoulCams?", "3500–6000 Кбит/с для 1080p; проверьте аплоад."),
        ],
    },
    {
        "slug": "imlive", "name": "ImLive",
        "title": "Как использовать SplitCam на ImLive — виртуальная камера",
        "desc": "ImLive использует веб-камеру напрямую — без RTMP. Подключите SplitCam как "
                "виртуальную камеру, чтобы сцены, накладки и фильтры были в видеочате ImLive.",
        "kw": "как вести трансляцию на imlive, imlive splitcam, imlive виртуальная камера, "
              "imlive веб-камера",
        "h1html": 'Как использовать <span class="accent">ImLive</span> со SplitCam',
        "h1short": "SplitCam на ImLive",
        "card": "Виртуальная камера для ImLive — RTMP не нужен.",
        "intro": "ImLive использует веб-камеру напрямую в браузере — "
                 "<strong style='color:var(--text)'>RTMP и ключа трансляции нет</strong>. "
                 "Бесплатный <strong style='color:var(--text)'>SplitCam</strong> подключается "
                 "как <strong style='color:var(--text)'>виртуальная камера</strong>: соберите "
                 "сцену в SplitCam, затем выберите SplitCam камерой в ImLive.",
        "quick": "SplitCam на ImLive: установите SplitCam, соберите сцену с медиа-слоями, "
                 "откройте ImLive и начните видеочат, в настройках ImLive выберите SplitCam "
                 "камерой и микрофоном."
                 "<ol><li>Установите SplitCam.</li><li>Соберите сцену в SplitCam.</li>"
                 "<li>Начните видеочат на ImLive.</li>"
                 "<li>Выберите SplitCam камерой ImLive.</li><li>Начните чат.</li></ol>",
        "steps": [
            ("Установите SplitCam",
             "SplitCam — бесплатная программа для Windows и macOS. Установите её — без водяного "
             "знака и регистрации. На ImLive она работает как <strong>виртуальная "
             "камера</strong>, а не RTMP-кодировщик."),
            ("Соберите сцену в SplitCam",
             "Откройте SplitCam и через <strong>Media Layers +</strong> добавьте веб-камеру и "
             "любые накладки, текст, фильтры или AI-фон. Эта собранная сцена и будет камерой "
             "для ImLive."),
            ("Начните видеочат на ImLive",
             "Зайдите на сайт ImLive, нажмите <strong>Start Video Chat</strong>, затем откройте "
             "<strong>Go To Settings</strong> для доступа к настройкам камеры и микрофона."),
            ("Выберите SplitCam камерой",
             "В настройках ImLive выберите <strong>SplitCam</strong> и как веб-камеру, и как "
             "микрофон. ImLive покажет вашу полную сцену SplitCam вместо обычной камеры."),
            ("Начните Free Live Chat",
             "Нажмите <strong>Free Live Chat</strong> на ImLive, чтобы выйти в эфир. Чтобы "
             "поменять вид по ходу — редактируйте сцену в SplitCam, ImLive обновится сразу."),
        ],
        "tips": [
            ("Ключ трансляции не нужен", "У ImLive нет RTMP — не ищите URL сервера или ключ. "
             "SplitCam просто выбирается устройством камеры."),
            ("SplitCam и микрофоном", "Выберите SplitCam и микрофоном тоже — чтобы ваш аудиомикс "
             "и шумоподавление шли в эфир."),
            ("Соберите сцену до эфира", "ImLive показывает то, что выдаёт SplitCam — расставьте "
             "слои до начала чата."),
            _T_TEST,
        ],
        "faq": [
            ("ImLive использует RTMP или ключ?", "Нет — ImLive использует веб-камеру напрямую "
             "через браузер, официальной OBS-документации у него нет. SplitCam подключается "
             "виртуальной камерой, копировать ключ не нужно."),
            ("Как выбрать SplitCam на ImLive?", "Start Video Chat → Go To Settings → выберите "
             "SplitCam веб-камерой и микрофоном."),
            ("SplitCam бесплатен для ImLive?", "Да — бесплатно, без водяного знака, без лимита."),
            ("Можно ли накладки на ImLive?", "Да — соберите их в сцене SplitCam; ImLive покажет "
             "собранный результат."),
        ],
    },
    {
        "slug": "vxlive", "name": "VXLive",
        "title": "Как вести трансляцию на VXLive через SplitCam — официальная поддержка",
        "desc": "VXLive (VXModels) официально поддерживает SplitCam: есть статья помощи и "
                "пресет VISIT-X. Stream with third-party software, сервер + ключ.",
        "kw": "как вести трансляцию на vxlive, vxlive splitcam, vxmodels splitcam, visit-x splitcam",
        "h1html": 'Как вести трансляцию на <span class="accent">VXLive</span> через SplitCam',
        "h1short": "Трансляция на VXLive",
        "card": "VXLive официально поддерживает SplitCam (пресет VISIT-X).",
        "intro": "VXLive (VXModels / VISIT-X) — кам-платформа немецкого рынка и одна из немногих, "
                 "кто <strong style='color:var(--text)'>официально поддерживает SplitCam по "
                 "имени</strong>. У VXModels есть отдельная статья помощи по подключению "
                 "<strong style='color:var(--text)'>SplitCam</strong> к VXLive, а в SplitCam "
                 "есть готовый пресет канала VISIT-X.",
        "quick": "Вещание на VXLive через SplitCam: установите SplitCam, соберите сцену, в "
                 "VXLive выберите «Stream with third-party software», скопируйте URL сервера и "
                 "ключ, в SplitCam выберите пресет VISIT-X и вставьте их, Go Live в SplitCam, "
                 "затем GO ONLINE в VXLive."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Получите URL сервера и ключ VXLive.</li>"
                 "<li>Выберите пресет VISIT-X в SplitCam, вставьте.</li>"
                 "<li>Go Live, затем GO ONLINE в VXLive.</li></ol>",
        "key_how": "В VXLive выберите <strong>Stream with third-party software</strong> и опцию "
                   "для <strong>OBS, SplitCam или XSplit</strong>. VXLive выдаёт <strong>URL "
                   "сервера</strong> и <strong>ключ трансляции</strong>. В SplitCam выберите "
                   "<strong>VISIT-X</strong> как платформу, вставьте оба, нажмите <strong>Go "
                   "Live</strong> в SplitCam, затем <strong>GO ONLINE</strong> в VXLive.",
        "tips": [
            ("VISIT-X — встроенный пресет", "Сырой RTMP-URL вводить не надо — VISIT-X есть в "
             "списке платформ SplitCam, выберите его и просто вставьте URL сервера и ключ."),
            ("Выход в эфир в два шага", "На VXLive сначала жмёте Go Live в SplitCam, затем GO "
             "ONLINE в VXLive — оба, именно в таком порядке."),
            ("Платформа немецкого рынка", "Аудитория VXLive в основном немецкоязычная — немецкая "
             "текстовая накладка или заголовок помогут сблизиться со зрителями."),
            _T_ETH,
        ],
        "faq": [
            ("VXLive официально поддерживает SplitCam?", "Да — у VXModels (VXLive) есть отдельная "
             "официальная статья помощи по настройке SplitCam, и SplitCam указан наряду с OBS и "
             "XSplit как поддерживаемая программа вещания."),
            ("Как подключить SplitCam к VXLive?", "В VXLive выберите «Stream with third-party "
             "software», затем в SplitCam выберите пресет VISIT-X и вставьте URL сервера и ключ "
             "от VXLive."),
            ("Где жать «в эфир» — в SplitCam или VXLive?", "В обоих — сначала Go Live в "
             "SplitCam, затем GO ONLINE в VXLive."),
            ("SplitCam бесплатен для VXLive?", "Да — бесплатно, без водяного знака, без лимита."),
        ],
    },
    {
        "slug": "virtwish", "name": "VirtWish",
        "title": "Как вести трансляцию на VirtWish через SplitCam — URL потока и ключ",
        "desc": "Вещание на VirtWish через бесплатный SplitCam. Profile → Start Broadcast → "
                "раздел OBS даёт URL потока и ключ. Сцены, накладки, без водяного знака.",
        "kw": "как вести трансляцию на virtwish, virtwish программа трансляции, virtwish rtmp, "
              "virtwish obs",
        "h1html": 'Как вести трансляцию на <span class="accent">VirtWish</span> через SplitCam',
        "h1short": "Трансляция на VirtWish",
        "card": "URL потока и ключ для VirtWish.",
        "intro": "VirtWish — интерактивная кам-платформа. Её настройки вещания дают "
                 "<strong style='color:var(--text)'>URL потока и отдельный ключ</strong> в "
                 "разделе OBS — бесплатный <strong style='color:var(--text)'>SplitCam</strong> "
                 "берёт оба и ведёт шоу со сценами и накладками.",
        "quick": "Вещание на VirtWish через SplitCam: установите SplitCam, соберите сцену, на "
                 "VirtWish откройте <em>Profile → Start Broadcast</em> до раздела OBS, "
                 "скопируйте ссылку и ключ, вставьте оба в SplitCam, Go Live."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Получите URL и ключ VirtWish.</li><li>Вставьте оба в SplitCam.</li>"
                 "<li>Нажмите Go Live.</li></ol>",
        "key_how": "На VirtWish нажмите иконку справа вверху → <strong>Profile</strong> → "
                   "<strong>Start Broadcast</strong>, затем <strong>Start Broadcast</strong> "
                   "ещё раз, чтобы дойти до раздела OBS. <strong>Скопируйте ссылку из первой "
                   "строки</strong> в поле Stream URL SplitCam, а <strong>Stream Key</strong> "
                   "скопируйте отдельно в поле ключа.",
        "tips": [
            ("Ссылка — в первой строке", "Раздел OBS VirtWish помещает URL потока в первую "
             "строку — скопируйте её в Stream URL SplitCam, затем ключ отдельно."),
            ("Start Broadcast дважды", "Start Broadcast на VirtWish нажимается дважды, чтобы "
             "дойти до раздела OBS — это нормально, не сбой."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Где RTMP-данные VirtWish?", "Иконка справа вверху → Profile → Start Broadcast "
             "дважды → раздел OBS показывает ссылку и ключ."),
            ("VirtWish поддерживает внешние кодировщики?", "Да — его раздел OBS даёт URL потока "
             "и ключ, так что SplitCam работает."),
            ("SplitCam бесплатен для VirtWish?", "Да — бесплатно, без водяного знака, без лимита."),
            ("Какой битрейт для VirtWish?", "3500–6000 Кбит/с для 1080p; проверьте аплоад."),
        ],
    },
    {
        "slug": "xmodels", "name": "XModels",
        "title": "Как вести трансляцию на XModels через SplitCam — гайд",
        "desc": "Вещание на XModels через бесплатный SplitCam. Опция внешнего кодировщика в "
                "настройках модельного аккаунта. Сцены, накладки, без водяного знака.",
        "kw": "как вести трансляцию на xmodels, xmodels программа трансляции, xmodels rtmp",
        "h1html": 'Как вести трансляцию на <span class="accent">XModels</span> через SplitCam',
        "h1short": "Трансляция на XModels",
        "card": "Опция внешнего кодировщика в аккаунте XModels.",
        "intro": "XModels — кам-платформа со встроенной "
                 "<strong style='color:var(--text)'>опцией внешнего кодировщика</strong> в "
                 "настройках модельного аккаунта. Бесплатный "
                 "<strong style='color:var(--text)'>SplitCam</strong> вещает на неё со сценами, "
                 "накладками и фильтрами вместо одной плоской камеры.",
        "quick": "Вещание на XModels через SplitCam: установите SplitCam, соберите сцену, в "
                 "модельном аккаунте XModels включите опцию внешнего кодировщика, скопируйте "
                 "URL сервера и ключ, вставьте в SplitCam, Go Live."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Включите внешний кодировщик в настройках аккаунта XModels.</li>"
                 "<li>Вставьте URL и ключ в SplitCam.</li><li>Нажмите Go Live.</li></ol>",
        "key_how": "В <strong>настройках модельного аккаунта</strong> XModels включите опцию "
                   "<strong>вещания через внешний кодировщик</strong>. XModels выдаёт "
                   "<strong>ключ трансляции</strong> — скопируйте его в SplitCam. Если опции "
                   "или пути нет где ожидаете, поддержка XModels работает через FAQ-чат на "
                   "сайте и <strong>info@xmodels.com</strong>; видео-гайд выше тоже показывает.",
        "tips": [
            ("Опция в настройках аккаунта", "XModels помещает опцию внешнего кодировщика внутрь "
             "настроек модельного аккаунта, а не на отдельный экран вещания."),
            ("Поддержка — чат и email", "Большого публичного хелп-центра у XModels нет — FAQ-чат "
             "на сайте и info@xmodels.com это официальные каналы поддержки."),
            ("Накладки в SplitCam", "Цели по токенам, ник и соцсети как слои сцены — базовая "
             "камера XModels так не умеет."),
            _T_ETH,
        ],
        "faq": [
            ("XModels поддерживает внешние кодировщики?", "Да — в настройках модельного аккаунта "
             "есть опция вещания через внешний кодировщик с выдачей ключа, так что SplitCam "
             "работает."),
            ("Где получить помощь по XModels?", "Поддержка XModels — через FAQ-чат на сайте и "
             "email info@xmodels.com; большого публичного хелп-центра нет."),
            ("SplitCam бесплатен для XModels?", "Да — бесплатно, без водяного знака, без лимита."),
            ("Какой битрейт для XModels?", "3500–6000 Кбит/с для 1080p; проверьте аплоад."),
        ],
    },
    {
        "slug": "flirt4free", "name": "Flirt4Free",
        "title": "Как вести трансляцию на Flirt4Free через SplitCam — External Broadcast Form",
        "desc": "Вещание на Flirt4Free через бесплатный SplitCam. External Broadcast Form даёт "
                "RTMP URL и Stream Name + поля разрешения/битрейта. Без водяного знака.",
        "kw": "как вести трансляцию на flirt4free, flirt4free external broadcast, flirt4free rtmp",
        "h1html": 'Как вести трансляцию на <span class="accent">Flirt4Free</span> через SplitCam',
        "h1short": "Трансляция на Flirt4Free",
        "card": "Настройка через External Broadcast Form Flirt4Free.",
        "intro": "Flirt4Free — одна из старейших кам-платформ, в сети с 1990-х. Она официально "
                 "поддерживает внешнее вещание через "
                 "<strong style='color:var(--text)'>External Broadcast Form</strong> — "
                 "бесплатный <strong style='color:var(--text)'>SplitCam</strong> отправляет "
                 "поток, а форма задаёт разрешение и битрейт.",
        "quick": "Вещание на Flirt4Free через SplitCam: установите SplitCam, соберите сцену, "
                 "откройте External Broadcast Form Flirt4Free, скопируйте RTMP URL и Stream Name "
                 "и задайте разрешение/битрейт, вставьте в SplitCam, Go Live."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Откройте External Broadcast Form Flirt4Free.</li>"
                 "<li>Вставьте RTMP URL + Stream Name в SplitCam.</li><li>Нажмите Go Live.</li></ol>",
        "key_how": "В модельной зоне Flirt4Free откройте <strong>External Broadcast Form</strong>. "
                   "В отличие от большинства кам-сайтов, Flirt4Free даёт <strong>RTMP URL</strong> "
                   "и <strong>Stream Name</strong> (а не «ключ»), плюс поля разрешения и "
                   "битрейта, которые заполняются прямо в форме. Скопируйте URL и Stream Name в "
                   "поля сервера и ключа SplitCam.",
        "tips": [
            ("Это Stream Name, не ключ", "Flirt4Free называет учётные данные Stream Name. "
             "Вставьте его в поле ключа SplitCam — роль та же."),
            ("Задайте разрешение/битрейт в форме", "У External Broadcast Form Flirt4Free свои "
             "поля разрешения и битрейта — сделайте их совпадающими с настройками SplitCam, "
             "чтобы картинку не масштабировало."),
            ("Устоявшаяся платформа", "Flirt4Free работает с 1990-х — модельные инструменты "
             "зрелые, и External Broadcast Form это их документированная часть."),
            _T_ETH,
        ],
        "faq": [
            ("Flirt4Free поддерживает внешние кодировщики?", "Да — официально, через External "
             "Broadcast Form, которая даёт RTMP URL и Stream Name. SplitCam работает как "
             "кодировщик."),
            ("Где взять RTMP-данные Flirt4Free?", "Из External Broadcast Form в модельной зоне "
             "— там показаны RTMP URL, Stream Name и поля разрешения/битрейта."),
            ("SplitCam бесплатен для Flirt4Free?", "Да — бесплатно, без водяного знака, без "
             "лимита."),
            ("Какой битрейт для Flirt4Free?", "3500–6000 Кбит/с для 1080p — задайте одно и то "
             "же значение в External Broadcast Form и в SplitCam."),
        ],
    },
    {
        "slug": "mfc-alerts", "name": "MFC Alerts",
        "title": "Как добавить MFC Alerts на трансляцию через SplitCam",
        "desc": "Показывайте анимированные алерты о токенах на трансляции MyFreeCams. Добавьте "
                "ваш URL с mfcalerts.com слоем Browser в SplitCam — выше веб-камеры.",
        "kw": "mfc alerts, как добавить mfc alerts, myfreecams алерты токенов, mfcalerts splitcam",
        "h1html": 'Как добавить <span class="accent">MFC Alerts</span> на трансляцию',
        "h1short": "Добавить MFC Alerts",
        "card": "Анимированные алерты о токенах на трансляции MyFreeCams.",
        "intro": "MFC Alerts показывает анимированные эффекты на вашей трансляции MyFreeCams "
                 "когда зритель присылает токены. Работает как "
                 "<strong style='color:var(--text)'>слой Browser</strong> внутри бесплатного "
                 "<strong style='color:var(--text)'>SplitCam</strong> — настроил один раз, и "
                 "токены вызывают реакции на экране вживую.",
        "quick": "Добавить MFC Alerts через SplitCam: установите SplitCam, добавьте веб-камеру, "
                 "откройте вкладку Browser и загрузите mfcalerts.com, скопируйте ваш URL "
                 "алертов, добавьте слоем Browser выше веб-камеры, проверьте тестовым токеном."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте веб-камеру.</li>"
                 "<li>Возьмите URL на mfcalerts.com.</li>"
                 "<li>Добавьте его слоем Browser выше камеры.</li>"
                 "<li>Отправьте тестовый токен.</li></ol>",
        "steps": [
            ("Установите SplitCam и добавьте веб-камеру",
             "Установите бесплатный SplitCam для Windows или macOS, затем добавьте "
             "<strong>веб-камеру</strong> источником. MFC Alerts ляжет слоем поверх этой камеры."),
            ("Откройте вкладку Browser и зайдите на mfcalerts.com",
             "В SplitCam откройте вкладку <strong>Browser</strong> и зайдите на "
             "<strong>www.mfcalerts.com</strong>. Войдите или зарегистрируйтесь, если аккаунта "
             "на mfcalerts.com ещё нет."),
            ("Скопируйте ваш URL алертов",
             "На mfcalerts.com нажмите <strong>Copy to clipboard</strong>, чтобы скопировать "
             "ваш персональный URL алертов — это страница, которая рисует анимации токенов."),
            ("Добавьте URL слоем Browser — выше веб-камеры",
             "Вставьте URL в окно Browser SplitCam и нажмите <strong>Add</strong>. Затем "
             "переставьте список источников так, чтобы <strong>MFC Alerts был выше веб-"
             "камеры</strong> (меню из 3 точек → Move Up). Если ниже камеры — эффекты не видны."),
            ("Проверьте тестовым токеном",
             "Откройте <strong>Settings → Send test tip</strong> и убедитесь, что эффект "
             "появляется поверх камеры. Затем вещайте на MyFreeCams как обычно — реальные "
             "токены теперь вызывают анимации."),
        ],
        "tips": [
            ("MFC Alerts должен быть выше камеры", "Самая частая ошибка: если слой MFC Alerts "
             "ниже веб-камеры в списке источников, эффекты скрыты. Поднимите его выше."),
            ("Нужен аккаунт на mfcalerts.com", "URL алертов персональный — сначала "
             "зарегистрируйтесь на mfcalerts.com, если аккаунта нет."),
            ("Тестовый токен до эфира", "Через Settings → Send test tip проверьте, что накладка "
             "работает — не узнавайте о поломке посреди шоу."),
            _T_ETH,
        ],
        "faq": [
            ("Что такое MFC Alerts?", "Система уведомлений для MyFreeCams, показывающая видео-"
             "эффекты на трансляции при отправке токенов — добавляется накладкой Browser в "
             "SplitCam."),
            ("Почему мои MFC Alerts не видны?", "Почти всегда порядок слоёв — слой Browser с "
             "MFC Alerts должен быть выше веб-камеры в списке источников SplitCam."),
            ("А как вещать на сам MyFreeCams?", "MyFreeCams официально поддерживает вещание "
             "через OBS (свой плагин Sidekick прекращён — вики советует «используйте OBS»). "
             "Рекомендованно: 720p, 30 fps, ~2500 Кбит/с — SplitCam подключается так же."),
            ("SplitCam для этого бесплатен?", "Да — SplitCam бесплатен, без водяного знака, без "
             "лимитов."),
        ],
    },
    {
        "slug": "lovense", "name": "Lovense",
        "title": "Как подключить игрушку Lovense к трансляции через SplitCam",
        "desc": "Подключите интерактивную игрушку Lovense к кам-трансляции через бесплатный "
                "SplitCam. У Lovense есть официальный Lovense SplitCam Toolset.",
        "kw": "как подключить lovense к трансляции, lovense splitcam toolset, lovense кам, "
              "интерактивная игрушка lovense стрим",
        "h1html": 'Как подключить <span class="accent">игрушку Lovense</span> к трансляции',
        "h1short": "Игрушка Lovense",
        "card": "Подключение интерактивной игрушки Lovense к эфиру.",
        "intro": "Ведите кам-трансляцию через бесплатный <strong style='color:var(--text)'>"
                 "SplitCam</strong> и подключите интерактивную игрушку "
                 "<strong style='color:var(--text)'>Lovense</strong>, чтобы она реагировала на "
                 "токены. У Lovense есть официальный "
                 "<strong style='color:var(--text)'>Lovense SplitCam Toolset</strong>, а в "
                 "SplitCam есть официальный плагин Lovense — интеграция поддержана с обеих "
                 "сторон.",
        "quick": "Чтобы подключить Lovense к трансляции: установите SplitCam и софт Lovense, "
                 "подключите игрушку, привяжите Lovense к кам-платформе, добавьте статус Lovense "
                 "как слой Browser в SplitCam и вещайте как обычно."
                 "<ol><li>Установите SplitCam.</li><li>Установите и подключите софт Lovense.</li>"
                 "<li>Привяжите Lovense к кам-сайту.</li>"
                 "<li>Добавьте накладку Lovense в SplitCam.</li><li>Нажмите Go Live.</li></ol>",
        "steps": [
            ("Установите SplitCam",
             "SplitCam — бесплатная программа для трансляций на Windows и macOS, кодировщик, "
             "который отправляет видео на кам-платформу. Установите её; без водяного знака."),
            ("Установите и подключите софт Lovense",
             "Установите официальное приложение Lovense Connect / Lovense Stream. Включите "
             "игрушку и подключите по Bluetooth — приложение покажет её подключённой."),
            ("Привяжите Lovense к кам-платформе",
             "В приложении Lovense подключите аккаунт кам-сайта, чтобы игрушка реагировала на "
             "токены и чаевые зрителей. Lovense поддерживает большинство крупных кам-платформ."),
            ("Добавьте накладку Lovense в SplitCam",
             "Lovense даёт URL виджета / накладки. Добавьте его слоем "
             "<strong>Browser</strong> в сцену SplitCam — зрители увидят статус игрушки и "
             "недавние чаевые на экране."),
            ("Соберите сцену и выходите в эфир",
             "Добавьте камеру и другие накладки, вставьте RTMP-ключ кам-платформы в SplitCam и "
             "нажмите <strong>Go Live</strong>. Игрушка реагирует на токены в реальном времени."),
        ],
        "tips": [
            ("Используйте официальный Lovense SplitCam Toolset", "Lovense выпускает отдельный "
             "тулсет под SplitCam со своим гайдом установки — он добавляет накладку активности "
             "игрушки и алертов о токенах, сделанную для SplitCam."),
            ("Обновите Lovense Cam Extension", "Тулсету нужен свежий Lovense Cam Extension "
             "(30.1.4 или новее) — обновите его до эфира."),
            ("Заряжайте игрушку", "Севшая посреди эфира батарея убивает интерактив — заряжайте "
             "полностью перед эфиром."),
            ("Проверьте реакцию", "Отправьте небольшой тестовый токен, чтобы убедиться, что "
             "игрушка реагирует, до открытия комнаты."),
        ],
        "faq": [
            ("Lovense официально поддерживает SplitCam?", "Да — у Lovense есть официальный "
             "«Lovense SplitCam Toolset» со своим гайдом установки, а в SplitCam есть "
             "официальный плагин Lovense. Интеграция поддержана с обеих сторон."),
            ("Игрушка подключается прямо к SplitCam?", "Нет — игрушка подключается к приложению "
             "Lovense; SplitCam показывает накладку Lovense и вещает камеру."),
            ("Какие кам-сайты поддерживают Lovense?", "Cam Extension Lovense официально "
             "поддерживает Chaturbate, Stripchat, BongaCams, MyFreeCams и CamSoda, с разной "
             "поддержкой прочих — актуальный список в приложении Lovense."),
            ("Можно показывать недавние чаевые на экране?", "Да — добавьте URL виджета Lovense "
             "слоем Browser в SplitCam."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Несколько кам-сайтов",
        "title": "Как вещать на несколько кам-сайтов одновременно через SplitCam",
        "desc": "Трансляция на MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat и другие "
                "одновременно через бесплатную мультитрансляцию SplitCam. Без водяного знака.",
        "kw": "вещание на несколько кам-сайтов, мультитрансляция кам, трансляция на chaturbate и "
              "bongacams одновременно",
        "h1html": 'Как вещать на <span class="accent">несколько кам-сайтов</span> одновременно',
        "h1short": "Мультитрансляция кам",
        "card": "Вещание на несколько кам-сайтов одновременно.",
        "intro": "Бесплатный <strong style='color:var(--text)'>SplitCam</strong> может вещать "
                 "один поток на <strong style='color:var(--text)'>несколько кам-сайтов "
                 "одновременно</strong> — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat и "
                 "другие. Без водяного знака, в один клик.",
        "quick": "Чтобы вещать на несколько кам-сайтов сразу: установите SplitCam, соберите "
                 "сцену, получите URL RTMP-сервера и ключ от каждого кам-сайта, добавьте их все "
                 "в настройках мультитрансляции SplitCam, нажмите Go Live один раз."
                 "<ol><li>Установите SplitCam.</li><li>Добавьте камеру и сцену.</li>"
                 "<li>Получите RTMP-ключ от каждого кам-сайта.</li>"
                 "<li>Добавьте все ключи в мультитрансляцию.</li>"
                 "<li>Нажмите Go Live один раз.</li></ol>",
        "steps": [
            ("Установите SplitCam",
             "SplitCam — бесплатная программа для трансляций на Windows и macOS со встроенной "
             "мультитрансляцией. Установите — без водяного знака и регистрации."),
            ("Настройте камеру и сцену",
             "Откройте SplitCam, добавьте веб-камеру и соберите сцену с накладками и фильтрами. "
             "Одна сцена идёт на все площадки."),
            ("Получите RTMP-ключ от каждого кам-сайта",
             "На каждой кам-платформе включите внешнее / RTMP-вещание и скопируйте её "
             "<strong>URL сервера</strong> и <strong>ключ</strong>. Повторите для каждого "
             "сайта — точные пути в отдельных гайдах по платформам."),
            ("Добавьте все площадки в SplitCam",
             "Откройте <strong>Stream Settings</strong> и добавьте каждый кам-сайт "
             "пользовательской RTMP-площадкой — вставьте URL сервера и ключ. Отметьте нужные."),
            ("Нажмите Go Live один раз",
             "Нажмите <strong>Go Live</strong>. SplitCam отправит поток на все выбранные кам-"
             "сайты одновременно, peer-to-peer, из одного кодирования — без доплат."),
        ],
        "tips": [
            ("Следите за аплоадом", "Мультитрансляция умножает нагрузку на исходящий канал. "
             "Каждой площадке нужен свой битрейт — убедитесь, что канал тянет сумму."),
            ("Проверьте правила площадок", "Некоторые кам-сайты запрещают одновременное вещание "
             "в другом месте — уточните до мультитрансляции."),
            _T_ETH,
            ("Монитор состояния", "SplitCam показывает статус по каждой площадке — отключите "
             "сайт, если аплоад не тянет."),
        ],
        "faq": [
            ("Мультитрансляция в SplitCam бесплатна?", "Да — мультитрансляция встроена и "
             "бесплатна, без платы за площадку и без водяного знака."),
            ("На сколько кам-сайтов можно вещать сразу?", "Насколько хватает исходящего "
             "канала — каждая площадка потребляет свой битрейт."),
            ("Используется ли облачный ретранслятор?", "Нет — SplitCam отправляет потоки "
             "peer-to-peer напрямую с вашего ПК на сервер каждой платформы."),
            ("Мультитрансляция замедлит ПК?", "Кодирование делается один раз и "
             "переиспользуется; аппаратное кодирование держит нагрузку на CPU низкой."),
        ],
    },
]
