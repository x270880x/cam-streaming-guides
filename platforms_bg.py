# -*- coding: utf-8 -*-
"""Bulgarian (bg) content for cam-streaming-guides."""

_T_ETH = ("Използвай кабелна връзка", "Ethernet бие Wi-Fi в дълъг стрийм — загубен кадър е "
          "загубен тип. Прокарай кабел до стрийм компютъра.")
_T_TEST = ("Първо направи частен тест", "Пусни кратко тестово предаване за камера, звук, "
           "кадриране и наслагвания, преди да отвориш стаята за публика.")

PLATFORMS_BG = [
    {"slug": "chaturbate", "name": "Chaturbate",
     "title": "Излъчване в Chaturbate със SplitCam — Token & RTMP",
     "desc": "Излъчване в Chaturbate с безплатен SplitCam — broadcast token, RTMP, мулти-камера сцени и наслагвания. Без воден знак.",
     "kw": "излъчване chaturbate, chaturbate broadcast token, chaturbate rtmp obs, chaturbate external encoder, chaturbate live",
     "h1html": 'Как да излъчваш в <span class="accent">Chaturbate</span> със SplitCam',
     "h1short": "Излъчване Chaturbate",
     "card": "Token-базирано настройване с външен енкодер в Chaturbate.",
     "intro": "Chaturbate е една от най-големите кам платформи, изградена върху икономика на токени. Браузърният broadcaster е плоска един-камера програма — преминаването към <strong style='color:var(--text)'>външен енкодер</strong> с безплатния <strong style='color:var(--text)'>SplitCam</strong> отваря мулти-камера сцени, наслагвания и филтри върху същия токен-базиран стрийм.",
     "quick": "Излъчване в Chaturbate със SplitCam: инсталирай SplitCam, изгради сцената, в Chaturbate отвори <em>Broadcast Yourself → My Broadcast</em>, копирай broadcast token, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Копирай broadcast token от Chaturbate.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "В Chaturbate кликни <strong>Broadcast Yourself</strong> за страницата <strong>My Broadcast</strong>, после <strong>View RTMP/OBS broadcast information and stream key</strong>. Ключът се появява като <strong>broadcast token</strong> — копирай. Третирай го като парола; никога публично.",
     "tips": [
         ("Token е ключът", "Chaturbate използва broadcast token-а ти вместо обикновен stream key. Третирай го като парола и нулирай при изтичане."),
         ("Голям запас", "RTMP ingest на Chaturbate приема до 4K, 60 fps и висок битрейт — лимитът е твоят upload, не платформата. Keyframe на 2 секунди."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Позволява ли Chaturbate OBS / външни енкодери?", "Да — Chaturbate поддържа външни енкодери официално и има собствена статия «How do I set up OBS?». Активира се чрез «Use External Encoder to Broadcast» в настройките за излъчване."),
         ("Къде е моят Chaturbate stream key?", "Broadcast Yourself → My Broadcast → View RTMP/OBS broadcast information and stream key. Ключът е broadcast token-а."),
         ("Какъв битрейт за Chaturbate?", "3500–6000 Kbps на 1080p е достатъчно. Таванът на Chaturbate е висок — реалният лимит е твоят upload; пусни първо вградения тест за скорост на SplitCam."),
         ("SplitCam безплатен ли е за Chaturbate?", "Да — напълно безплатен, без воден знак и без времево ограничение: енкодерът не яде от твоите печалби в токени."),
     ]},
    {"slug": "cam4", "name": "CAM4",
     "title": "Излъчване в CAM4 със SplitCam — External Encoder",
     "desc": "Излъчване в CAM4 с безплатен SplitCam — External Encoder, stream key, гео-блокиране и наслагвания. Без воден знак.",
     "kw": "излъчване cam4, cam4.com, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
     "h1html": 'Как да излъчваш в <span class="accent">CAM4</span> със SplitCam',
     "h1short": "Излъчване CAM4",
     "card": "External Encoder в CAM4 с гео-контроли.",
     "intro": "CAM4 е глобална cam-and-earn платформа с вградени гео-контроли — можеш да скриеш излъчването в избрани страни. Излъчване чрез безплатен <strong style='color:var(--text)'>SplitCam</strong> като външен енкодер отваря смени на сцената и наслагвания, които базовият broadcaster не прави.",
     "quick": "Излъчване в CAM4 със SplitCam: инсталирай SplitCam, изгради сцената, в CAM4 отиди <em>Broadcast &amp; Earn Money → Start Broadcast → External Encoder</em>, Get Stream Key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи stream key от CAM4.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "В CAM4 кликни <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn Money</strong> → <strong>Start Broadcast</strong>, после <strong>External Encoder</strong> отгоре. Попълни рождена дата, пол и страна, използвай <strong>Get Stream Key</strong> и копирай. Зелен слайдер в Stream Settings на SplitCam потвърждава връзката.",
     "tips": [
         ("Настрой гео-ограниченията", "CAM4 позволява скриване на излъчването в конкретни страни и региони — настрой от CAM4 страната преди go-live."),
         ("Следи зеления слайдер", "Настройката на CAM4 показва зелен слайдер в Stream Settings на SplitCam, когато ключът е приет — червен означава: провери ключа."),
         ("По-нисък битрейт от обичайния", "Ingest-ът на CAM4 ограничава видео битрейта до около 3000 Kbps — по-нисък от повечето кам сайтове. Не натискай по-високо."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли CAM4 OBS / външни енкодери официално?", "Да — CAM4 има официален OBS Guide на сайта за поддръжка и препоръчва External Encoder за най-добро изживяване. SplitCam използва същия RTMP път."),
         ("Мога ли гео-блокирам стрийма в CAM4?", "Да — CAM4 има вградено гео-ограничение за скриване на излъчването в определени страни. Настрой в CAM4, не в SplitCam."),
         ("Къде е stream key на CAM4?", "Broadcast → Broadcast & Earn Money → Start Broadcast → External Encoder → Get Stream Key."),
         ("Какъв битрейт за CAM4?", "По-нисък от средния — ingest на CAM4 ограничава до ~3000 Kbps при 30 fps с 1-секунден keyframe. Официалната таблица препоръчва да не превишаваш ~3000."),
     ]},
    {"slug": "bongacams", "name": "BongaCams",
     "title": "Излъчване в BongaCams със SplitCam — External Encoder",
     "desc": "Излъчване в BongaCams с безплатен SplitCam — External Encoder, мулти-камера сцени, наслагвания и AI фон. Без воден знак.",
     "kw": "bongacams, bongcams, излъчване bongacams, bongacams external encoder, bongacams rtmp obs",
     "h1html": 'Как да излъчваш в <span class="accent">BongaCams</span> със SplitCam',
     "h1short": "Излъчване BongaCams",
     "card": "External Encoder настройка за BongaCams.",
     "intro": "BongaCams е глобална кам платформа. Излъчването чрез външен енкодер не идва винаги активирано — веднъж активирано, безплатният <strong style='color:var(--text)'>SplitCam</strong> води излъчването с мулти-камера сцени, наслагвания и AI фон.",
     "quick": "Излъчване в BongaCams със SplitCam: инсталирай SplitCam, изгради сцената, в BongaCams отиди <em>Options → Broadcast settings → Select Encoder → External Encoder</em>, копирай URL и ключ, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи URL и ключ от BongaCams.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "В BongaCams отвори <strong>Options</strong> → <strong>Broadcast settings</strong> → <strong>Select Encoder</strong> → <strong>External Encoder</strong> и копирай показаните URL на сървъра и stream key. <strong>Ако бутонът External Encoder липсва</strong>, свържи се с поддръжката на BongaCams и поискай активиране на външното кодиране на акаунта.",
     "tips": [
         ("Няма External Encoder бутон? Поддръжка", "BongaCams активира външното кодиране акаунт по акаунт — ако опцията липсва от Broadcast settings, поддръжката я активира."),
         ("Съвпадай резолюцията", "BongaCams препоръчва резолюцията на уебкамерата и тази на излъчването да съвпадат — например и двете 1280×720."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Защо бутонът External Encoder не се появява в BongaCams?", "Външното кодиране не е активно по подразбиране на всеки акаунт — свържи се с поддръжката на BongaCams за активиране и бутонът ще се появи в Broadcast settings."),
         ("Трябва ли да верифицирам акаунта си в BongaCams?", "Да — излъчването изисква 18+, официален документ за проверка на възрастта и одобрение на акаунта преди да си на живо."),
         ("Какъв битрейт за BongaCams?", "RTMP ingest на BongaCams ограничава видео битрейта до около 6000 Kbps с 2-секунден keyframe — 3500–6000 на 1080p е оптималната зона; тествай upload-а първо."),
         ("SplitCam безплатен ли е за BongaCams?", "Да — напълно безплатен, без воден знак и без времево ограничение, така че енкодерът не намалява печалбите ти в токени в BongaCams."),
     ]},
    {"slug": "stripchat", "name": "Stripchat",
     "title": "Излъчване в Stripchat със SplitCam — Strip Cam Setup",
     "desc": "Излъчване в Stripchat — strip cam платформата — с безплатен SplitCam. Външен софтуер, token-ключ, сцени и наслагвания.",
     "kw": "strip cam, stripchat live stream, излъчване stripchat, stripchat external software, stripchat stream key, stripchat rtmp obs",
     "h1html": 'Как да излъчваш в <span class="accent">Stripchat</span> със SplitCam',
     "h1short": "Излъчване Stripchat",
     "card": "Външен софтуер за Stripchat стрийм.",
     "intro": "Stripchat е голяма кам платформа с фокус върху интерактивност. Режимът <em>external software</em> ти дава token-базиран ключ — постави го в безплатния <strong style='color:var(--text)'>SplitCam</strong>, за да излъчваш със сцени, наслагвания и филтри вместо плоска камера.",
     "quick": "Излъчване в Stripchat със SplitCam: инсталирай SplitCam, изгради сцената, в Stripchat избери <em>Switch to external software</em>, копирай stream key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи stream key от Stripchat.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "В Stripchat избери <strong>Switch to external software</strong>, после <strong>Show external software settings for the stream</strong>. Копирай stream key — Stripchat го показва като token. Дръж го частен.",
     "tips": [
         ("Съвпадай резолюцията със сайта", "FAQ на Stripchat предупреждава: резолюцията в твоя софтуер трябва да съвпада точно с тази на сайта, иначе видеото пикселира. Настрой и двете еднакво."),
         ("Внимание за минимума от 2 Mbps", "Stripchat сочи 2 Mbps upload като минимум — и казва директно, че не е достатъчно за OBS стрийминг или мултистрийминг. Цели се много по-високо."),
         ("Ключът е token", "Stream key на Stripchat е token — копирай точно, никога не споделяй, нулирай при изтичане."),
         _T_ETH,
     ],
     "faq": [
         ("Препоръчва ли Stripchat OBS / външен софтуер?", "Да — официалното FAQ на Stripchat препоръчва външен броудкаст софтуер като OBS «за постигане на най-добро видео и аудио качество». SplitCam работи по същия начин."),
         ("Как сменям Stripchat на външен софтуер?", "В Broadcast Center избери Switch to External Broadcast Software (OBS), после отвори external software settings, за да разкриеш stream key (token)."),
         ("Какъв битрейт за Stripchat?", "RTMP ingest приема до ~6000 Kbps с 2-секунден keyframe. 3500–6000 на 1080p е оптимално — но трябва да си доста над минимума от 2 Mbps, особено за OBS стрийминг."),
         ("SplitCam безплатен ли е за Stripchat?", "Да — без лицензионна такса, без воден знак, без времево ограничение: дори дълги интерактивни шоута в Stripchat не струват нищо от страна на енкодера."),
     ]},
    {"slug": "onlyfans", "name": "OnlyFans",
     "title": "На живо в OnlyFans със SplitCam — Авторизация или ключ",
     "desc": "На живо в OnlyFans с безплатен SplitCam — вход чрез авторизация или OBS Key, мулти-камера сцени, наслагвания. Без воден знак.",
     "kw": "на живо onlyfans, onlyfans live stream, onlyfans авторизация splitcam, onlyfans obs key, onlyfans streaming software",
     "h1html": 'Как да си на живо в <span class="accent">OnlyFans</span> със SplitCam',
     "h1short": "Live OnlyFans",
     "card": "Авторизирай веднъж или постави ключ — live в OnlyFans.",
     "intro": "Live в OnlyFans е за твоите абонати. SplitCam свързва по <strong style='color:var(--text)'>два начина</strong> — влизаш веднъж с OnlyFans акаунта и SplitCam взема stream key автоматично и го държи синхронизиран, или поставяш OBS Key ръчно. И в двата случая излъчваш с мулти-камера сцени, наслагвания и филтри.",
     "quick": "Live в OnlyFans със SplitCam: инсталирай SplitCam, изгради сцената, отвори Stream Settings &rarr; Add Channel &rarr; OnlyFans и избери <em>Авторизация</em> — влез с OnlyFans акаунт, SplitCam взема ключа автоматично — и натисни Go Live. С вързан акаунт можеш да сменяш параметрите на стрийма OnlyFans от SplitCam, без да отваряш сайта OnlyFans.",
     "steps": [
         ("Изтегли и инсталирай SplitCam",
          "SplitCam е безплатен софтуер за стрийминг за Windows и macOS — без регистрация, без карта, без воден знак. Това е енкодерът, който изпраща видеото ти към OnlyFans."),
         ("Настрой камера и сцена",
          "Отвори SplitCam и добави уебкамерата. Изгради сцената, която зрителите ще видят — наслагвания, текст, втора камера, beauty филтри или AI фон, всичко прилагано на живо."),
         ("Свързване — Метод 1: Авторизация (препоръчан)",
          "В SplitCam отвори <strong>Stream Settings</strong> &rarr; <strong>Add Channel</strong> &rarr; <strong>OnlyFans</strong> и избери <strong>Авторизация</strong>. Влез с имейл и парола от OnlyFans. SplitCam свързва акаунта ти, взема stream key автоматично и го държи синхронизиран — и ти позволява да управляваш параметрите на live-а OnlyFans от SplitCam, променяйки ги по време или след излъчването, без да отваряш сайта OnlyFans."),
         ("Свързване — Метод 2: Stream Key (ръчно)",
          "Предпочиташ да не влизаш? Използвай ключа. В OnlyFans иди <strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; секция <strong>Other</strong> и копирай <strong>OBS Key</strong>. В SplitCam, Add Channel &rarr; OnlyFans, постави в полето за ключ. Този ключ е статичен — за да смениш настройки по-късно се връщаш на сайта OnlyFans."),
         ("Go Live",
          "Без значение методът, натисни <strong>Go Live</strong> в SplitCam. С Метод 1 продължаваш да настройваш параметрите OnlyFans от SplitCam в реално време; с Метод 2 ключът остава така, както си го настроил."),
     ],
     "tips": [
         ("Авторизация vs Stream Key", "Два начина за свързване: <strong>Авторизация</strong> (влизаш веднъж, ключът се взема и синхронизира — най-лесният път) или <strong>Stream Key</strong> (копираш OBS Key в OnlyFans → Profile → Settings → Other и поставяш). Авторизацията спестява ръчното копи-пейст."),
         ("Сменяй настройки без да напускаш SplitCam", "С авторизация акаунтът остава вързан, така че настройваш параметрите live OnlyFans от SplitCam по време или след излъчването — без да минаваш през сайта OnlyFans."),
         ("Скромен битрейт", "RTMP ingest на OnlyFans ограничава видео битрейта до около 2500 Kbps — по-стегнато от повечето кам сайтове. Цели се на 720p–1080p при ~2000–2500."),
         _T_ETH,
     ],
     "faq": [
         ("Как свързвам OnlyFans със SplitCam?", "Два начина. <strong>Авторизация</strong> — Stream Settings → Add Channel → OnlyFans → влез с OnlyFans акаунт и SplitCam взема ключа автоматично. Или <strong>Stream Key</strong> — копирай OBS Key в OnlyFans → Profile → Settings → Other и постави."),
         ("Мога ли да сменям настройки live OnlyFans без да отварям сайта?", "Да — с метода Авторизация SplitCam остава свързан с OnlyFans акаунта, така че ключът и настройките синхронизират автоматично. Сменяш всичко от SplitCam по време или след излъчването, без да посещаваш onlyfans.com."),
         ("Какъв битрейт за OnlyFans?", "Скромен — RTMP ingest на OnlyFans ограничава битрейта до около 2500 Kbps, доста по-стегнато от други кам платформи. Цели се на 720p–1080p около 2000–2500 Kbps."),
         ("SplitCam безплатен ли е за live OnlyFans?", "Да — безплатен, без воден знак и без времево ограничение. Никакви разходи от страна на енкодера."),
     ]},
    {"slug": "camplace", "name": "CamPlace",
     "title": "Излъчване в CamPlace със SplitCam — Безплатно ръководство",
     "desc": "Излъчване в CamPlace с безплатен SplitCam — външен енкодер, RTMP ключ, сцени и наслагвания. Стъпка по стъпка, без воден знак.",
     "kw": "излъчване camplace, camplace broadcasting software, camplace rtmp, camplace external encoder, camplace stream key",
     "h1html": 'Как да излъчваш в <span class="accent">CamPlace</span> със SplitCam',
     "h1short": "Излъчване CamPlace",
     "card": "Външен енкодер за CamPlace стрийм.",
     "intro": "CamPlace е кам-стрийминг платформа. Няма публична OBS статия, така че <strong style='color:var(--text)'>видео ръководството горе</strong> е референцията — безплатният <strong style='color:var(--text)'>SplitCam</strong> свързва чрез стандартен RTMP и добавя сцени, наслагвания и AI фон, които базовата камера не прави.",
     "quick": "Излъчване в CamPlace със SplitCam: инсталирай SplitCam, изгради сцената, активирай външно/RTMP излъчване в CamPlace, копирай URL на сървъра и stream key, постави в SplitCam, Go Live. Следвай видеото за актуалния път."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи RTMP ключа от CamPlace.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "Влез в CamPlace и отвори настройките за излъчване. Превключи към опцията външен енкодер / RTMP / OBS, за да разкриеш <strong>URL на сървъра</strong> и <strong>stream key</strong>, копирай и двете. CamPlace не публикува официална OBS документация — <strong>видеото горе</strong> е най-сигурният път стъпка по стъпка през текущия интерфейс.",
     "tips": [
         ("Няма официално OBS ръководство — използвай видеото", "CamPlace няма публична статия за външни енкодери; видеото горе е референция за актуалния път."),
         ("Стандартен RTMP работи", "Макар недокументиран, CamPlace приема стандартен URL на RTMP сървър и ключ — SplitCam свързва като персонализирана RTMP дестинация."),
         ("Натрупвай наслагвания в SplitCam", "Цели на тип, име и социални handle-ове като слоеве на сцената — базовата камера на CamPlace не добавя такива неща."),
         _T_ETH,
     ],
     "faq": [
         ("CamPlace има ли официално OBS ръководство?", "Не е намерена публична статия за външни енкодери. CamPlace приема стандартен RTMP URL и ключ, така че SplitCam работи — следвай видеото."),
         ("Поддържа ли CamPlace външни енкодери?", "Да — приема стандартен RTMP stream key, така че SplitCam свързва като персонализирана RTMP дестинация."),
         ("Какъв битрейт за CamPlace?", "CamPlace не публикува официална цифра — използвай 3500–6000 Kbps на 1080p като безопасен диапазон и остави теста за скорост на SplitCam да определи реалния ти таван."),
         ("SplitCam безплатен ли е за CamPlace?", "Да — безплатен, без воден знак и без времево ограничение. Тъй като CamPlace не идва със собствен енкодер, безплатен RTMP инструмент върши работа."),
     ]},
    {"slug": "camsoda", "name": "CamSoda",
     "title": "CamSoda live със SplitCam — Безплатна настройка",
     "desc": "CamSoda live с безплатен SplitCam — Use OBS Broadcaster, регионални сървъри, сцени и наслагвания. Без воден знак.",
     "kw": "camsoda live, излъчване camsoda, camsoda obs broadcaster, camsoda rtmp obs, camsoda live broadcast",
     "h1html": 'Как да излъчваш в <span class="accent">CamSoda</span> със SplitCam',
     "h1short": "Излъчване CamSoda",
     "card": "Use OBS Broadcaster в CamSoda.",
     "intro": "CamSoda е американска кам платформа, известна с интерактивни и необичайни шоу формати. Поддържа OBS стрийминг официално — има бутон <strong style='color:var(--text)'>Use OBS Broadcaster</strong> на страницата Go Live и официално OBS ръководство в CamSoda wiki. Безплатният <strong style='color:var(--text)'>SplitCam</strong> работи по същия начин.",
     "quick": "Излъчване в CamSoda със SplitCam: инсталирай SplitCam, изгради сцената, кликни Use OBS Broadcaster на страницата Go Live на CamSoda, копирай URL и stream key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Кликни Use OBS Broadcaster в CamSoda.</li>"
              "<li>Постави URL + ключ в SplitCam.</li><li>Натисни Go Live.</li></ol>",
     "key_how": "На страницата <strong>Go Live</strong> на CamSoda кликни <strong>Use OBS Broadcaster</strong>. CamSoda показва URL на RTMP сървъра и stream key — копирай и двете. Избери регионалния сървър (Северна Америка, Европа, Азия и т.н.), който ти е най-близко. Wiki на CamSoda има пълно OBS ръководство, ако са ти нужни детайли.",
     "tips": [
         ("Верифицирай се за типове", "В CamSoda всеки може да излъчва, но за да получаваш типове трябва да завършиш процеса на верификация на CamSoda."),
         ("Избери най-близкия регионален сървър", "CamSoda предлага регионални ingest сървъри — най-близкият (NA / Европа / Азия / Южна Америка / Океания) намалява латентността и пропуснатите кадри."),
         ("Таван на 1080p / 30 fps", "Ingest на CamSoda стига до около 1080p, 30 fps и ~6000 Kbps — не натискай по-високо."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли CamSoda OBS / външни енкодери?", "Да — официално. Има бутон Use OBS Broadcaster на страницата Go Live и OBS ръководство в CamSoda wiki, така че SplitCam работи."),
         ("Трябва ли да се верифицирам в CamSoda?", "За излъчване — не. За получаване на типове — да; CamSoda изисква първо процеса на верификация."),
         ("Каква резолюция поддържа CamSoda?", "До 1920×1080 при 30 fps, около 6000 Kbps максимум на RTMP ingest."),
         ("SplitCam безплатен ли е за CamSoda?", "Да — безплатен, без воден знак и без времево ограничение. Работи с безплатния режим Use OBS Broadcaster на CamSoda, така че цялата верига не струва нищо."),
     ]},
    {"slug": "streamate", "name": "Streamate",
     "title": "Излъчване в Streamate със SplitCam — Интегриран канал",
     "desc": "Излъчване в Streamate с безплатен SplitCam — интегриран канал, SM Connect ключ, сцени и наслагвания. Без воден знак.",
     "kw": "streamate, streamate sm connect, излъчване streamate, streamate broadcasting software, streamate rtmp",
     "h1html": 'Как да излъчваш в <span class="accent">Streamate</span> със SplitCam',
     "h1short": "Излъчване Streamate",
     "card": "Streamate е интегриран канал в SplitCam — бърза настройка.",
     "intro": "Streamate е утвърдена кам платформа — и е една от <strong style='color:var(--text)'>предварително конфигурираните дестинации в SplitCam</strong>, в списъка с канали, така че настройката е по-бърза от ръчно RTMP въвеждане: избираш Streamate, поставяш ключа, готово.",
     "quick": "Излъчване в Streamate със SplitCam: инсталирай SplitCam, изгради сцената, в Streamate използвай <em>SM Connect → Start Show</em> и копирай ключа, после в SplitCam отвори <em>Stream Settings → Add Channel → Streamate</em> и постави."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи ключа Streamate чрез SM Connect.</li>"
              "<li>Add Channel → Streamate в SplitCam.</li><li>Натисни Go Live.</li></ol>",
     "key_how": "В Streamate отвори <strong>SM Connect</strong>, приеми условията, кликни <strong>Start Show</strong> отляво и затвори отворения прозорец — после копирай streaming ключа. В SplitCam отвори <strong>Stream Settings</strong> → <strong>Add Channel</strong>, избери <strong>Streamate</strong> от списъка и постави ключа. Зелен слайдер потвърждава връзката.",
     "tips": [
         ("Streamate е интегриран", "Без ръчен RTMP URL — SplitCam има Streamate в списъка Add Channel; само избираш и поставяш ключа."),
         ("Затвори SM Connect popup-а", "След Start Show Streamate отваря прозорец — затвори го; беше само за да разкрие streaming ключа."),
         ("Фиксирай резолюцията на 1080p", "Полето Video Resolution в SM Connect може да скочи на 1440 тихо, което не се доставя на практика и снижава качеството ти безмълвно — настрой ръчно на 1080p. Битрейт, който пада при статично изображение, е нормален: стриймът на Streamate е адаптивен."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Streamate интегриран ли е в SplitCam?", "Да — Streamate се появява в списъка Add Channel на SplitCam; избираш вместо да въвеждаш RTMP URL ръчно."),
         ("Къде е streaming ключът на Streamate?", "SM Connect → приеми условия → Start Show → затвори popup → копирай ключа."),
         ("Какъв битрейт за Streamate?", "Streamate не фиксира твърд таван — 3500–6000 Kbps на 1080p работи добре. Стриймът е адаптивен, така че по-нисък битрейт при статично изображение е нормален, не бъг."),
         ("SplitCam безплатен ли е за Streamate?", "Да — безплатен, без воден знак и без времево ограничение; и тъй като Streamate е интегриран канал в SplitCam, няма и отделен разход за енкодер."),
     ]},
    {"slug": "streamray", "name": "StreamRay",
     "title": "Излъчване в StreamRay cam със SplitCam — URL в чата",
     "desc": "Излъчване в StreamRay cam с безплатен SplitCam — URL публикуван в чата, OBS Broadcaster режим, сцени и наслагвания. Без воден знак.",
     "kw": "streamray, streamray cam, излъчване streamray, streamray obs broadcaster, streamray rtmp",
     "h1html": 'Как да излъчваш в <span class="accent">StreamRay</span> със SplitCam',
     "h1short": "Излъчване StreamRay",
     "card": "URL-в-чата външен енкодер за StreamRay.",
     "intro": "StreamRay има необичайна настройка за външен енкодер — доставя URL на стрийма в <strong style='color:var(--text)'>прозореца на чата на излъчването</strong> и не използва отделен stream key. Безплатният <strong style='color:var(--text)'>SplitCam</strong> се справя с този само-URL поток.",
     "quick": "Излъчване в StreamRay със SplitCam: инсталирай SplitCam, изгради сцената, в StreamRay активирай OBS Broadcaster, копирай URL на стрийма от прозореца на чата, постави в SplitCam (остави полето за ключ празно), Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Копирай URL на StreamRay от чата.</li>"
              "<li>Постави URL в SplitCam.</li><li>Натисни Go Live.</li></ol>",
     "key_how": "В StreamRay двойно кликни <strong>Broadcast Now</strong>, отвори менюто <strong>Other</strong>, избери <strong>OBS Broadcaster</strong> и <strong>Save and Close</strong>. StreamRay тогава публикува <strong>URL на стрийма в прозореца на чата</strong> — копирай оттам. Остави полето за stream key на SplitCam <strong>празно</strong>; StreamRay удостоверява само чрез URL.",
     "tips": [
         ("URL е в чата", "StreamRay не показва URL на стрийма в кутийка за настройки — публикува го в прозореца на чата на излъчването. Копирай оттам."),
         ("Остави полето за ключ празно", "StreamRay не използва отделен ключ — само URL. Не поставяй нищо в полето за ключ на SplitCam."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Къде е URL на стрийма на StreamRay?", "След активиране на OBS Broadcaster, StreamRay публикува URL в прозореца на чата — копирай от чата."),
         ("Защо няма stream key в StreamRay?", "StreamRay удостоверява само чрез URL — остави полето за ключ на SplitCam празно."),
         ("Какъв битрейт за StreamRay?", "StreamRay не обявява официален таван — цели се 3500–6000 Kbps на 1080p и пусни теста за скорост на SplitCam, тъй като само-URL потокът не дава обратна връзка за битрейт."),
         ("SplitCam безплатен ли е за StreamRay?", "Да — безплатен, без воден знак и без времево ограничение, което съвпада със само-URL потока на StreamRay: поставяш линк и си на живо."),
     ]},
    {"slug": "xlovecam", "name": "XLoveCam",
     "title": "Излъчване в XLoveCam със SplitCam — RTMP линк & ключ",
     "desc": "Излъчване в XLoveCam с безплатен SplitCam — RTMP линк и ключ, регионални сървъри, сцени и наслагвания. Без воден знак.",
     "kw": "xlovecam, x love cam, излъчване xlovecam, xlovecam rtmp link, xlovecam stream key",
     "h1html": 'Как да излъчваш в <span class="accent">XLoveCam</span> със SplitCam',
     "h1short": "Излъчване XLoveCam",
     "card": "RTMP линк + ключ за XLoveCam.",
     "intro": "XLoveCam е европейска многоезична кам платформа. Настройките на акаунта показват както <strong style='color:var(--text)'>RTMP линк</strong>, така и <strong style='color:var(--text)'>stream key</strong> — безплатният <strong style='color:var(--text)'>SplitCam</strong> взема и двете и излъчва с пълни сцени и наслагвания.",
     "quick": "Излъчване в XLoveCam със SplitCam: инсталирай SplitCam, изгради сцената, в XLoveCam отвори <em>My Account → settings</em>, копирай RTMP линк и stream key, постави и двете в SplitCam, започни шоуто."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Копирай RTMP линк + ключ от XLoveCam.</li><li>Постави и двете в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "В XLoveCam отвори <strong>My Account</strong> → <strong>settings</strong>. Настройките показват както <strong>RTMP линк</strong>, така и <strong>stream key</strong> — копирай и двете в полетата URL на сървъра и ключ на SplitCam, после <strong>Start your show</strong> в XLoveCam.",
     "tips": [
         ("Копирай линк И ключ", "XLoveCam ти дава RTMP линк И отделен stream key — нужни са и двете в SplitCam, не само едното."),
         ("Многоезична публика", "XLoveCam е европейска и многоезична — ясно текстово наслагване на твоя език помага на зрителите да те намерят."),
         ("Избери най-близкия сървър", "XLoveCam предлага регионални RTMP сървъри — Европа, Северна Америка, Южна Америка и Азия. Най-близкият намалява латентността и пропуснатите кадри."),
         _T_ETH,
     ],
     "faq": [
         ("Къде са RTMP данните на XLoveCam?", "My Account → settings — показва както RTMP линка, така и ключа."),
         ("Поддържа ли XLoveCam външни енкодери?", "Да — предоставя RTMP линк и ключ, така че SplitCam работи като енкодер."),
         ("Какъв битрейт за XLoveCam?", "XLoveCam не публикува фиксиран лимит; 3500–6000 Kbps на 1080p е оптимално. Избирането на най-близкия регионален сървър има същата важност — намалява пропуснатите кадри."),
         ("SplitCam безплатен ли е за XLoveCam?", "Да — безплатен, без воден знак и без времево ограничение. Достигане на многоезичната европейска публика на XLoveCam не струва софтуер."),
     ]},
    {"slug": "soulcams", "name": "SoulCams",
     "title": "Излъчване в SoulCams със SplitCam — OBS настройки",
     "desc": "Излъчване в SoulCams с безплатен SplitCam — OBS настройки, RTMP сървър и ключ, мулти-камера сцени и наслагвания.",
     "kw": "soul cams, soulcams, излъчване soulcams, soulcams obs, soulcams rtmp, soulcams broadcast",
     "h1html": 'Как да излъчваш в <span class="accent">SoulCams</span> със SplitCam',
     "h1short": "Излъчване SoulCams",
     "card": "OBS настройки за SoulCams.",
     "intro": "SoulCams е кам платформа, чиито OBS настройки показват <strong style='color:var(--text)'>RTMP сървър и stream key заедно</strong> в един прозорец. Постави и двете в безплатния <strong style='color:var(--text)'>SplitCam</strong>, за да излъчваш с мулти-камера сцени и наслагвания.",
     "quick": "Излъчване в SoulCams със SplitCam: инсталирай SplitCam, изгради сцената, в SoulCams кликни Go Online → Settings → OBS, копирай сървъра и ключа, постави и двете в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Отвори SoulCams Settings → OBS.</li><li>Постави сървър + ключ в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "В SoulCams влез и кликни <strong>Go Online</strong>, после отвори <strong>Settings</strong> → <strong>OBS</strong>. Прозорецът OBS показва <strong>RTMP сървър</strong> и <strong>stream key</strong> заедно — копирай и двете в SplitCam.",
     "tips": [
         ("Сървър и ключ един до друг", "SoulCams показва RTMP сървър и ключ в същия OBS прозорец — взимаш и двете с едно действие."),
         ("Go Online първо", "OBS настройките се появяват едва след клик Go Online в SoulCams — направи това преди да търсиш данните на енкодера."),
         ("Блокирай нежелани региони", "SoulCams позволява гео-блокиране от страна на модела — избираш кои страни не могат да виждат стрийма, преди да натиснеш Go Online."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Къде са OBS настройките на SoulCams?", "Влез, кликни Go Online, после Settings → OBS — RTMP сървърът и stream key се показват заедно."),
         ("Поддържа ли SoulCams външни енкодери?", "Да — OBS настройките дават RTMP сървър и ключ, така че SplitCam работи."),
         ("Какъв битрейт за SoulCams?", "SoulCams не дава официална цифра — цели се 3500–6000 Kbps на 1080p и тествай upload-а, тъй като OBS прозорецът не показва насоки за битрейт."),
         ("SplitCam безплатен ли е за SoulCams?", "Да — безплатен, без воден знак и без времево ограничение, така че пълно SoulCams шоу с мулти-камера сцени и наслагвания не струва нищо от страна на енкодера."),
     ]},
    {"slug": "imlive", "name": "ImLive",
     "title": "Излъчване в ImLive със SplitCam — Виртуална камера",
     "desc": "Im Live stream настройка с безплатен SplitCam — ImLive използва уебкамерата директно (без RTMP), свържи SplitCam като виртуална камера със сцени.",
     "kw": "im live stream, imlive splitcam, излъчване imlive, imlive виртуална камера, imlive webcam, im live cam",
     "h1html": 'Как да използваш <span class="accent">ImLive</span> със SplitCam',
     "h1short": "SplitCam в ImLive",
     "card": "Виртуална камера за ImLive — без RTMP.",
     "intro": "ImLive използва уебкамерата директно в браузъра — <strong style='color:var(--text)'>няма нито RTMP, нито stream key</strong>. Безплатният <strong style='color:var(--text)'>SplitCam</strong> свързва като <strong style='color:var(--text)'>виртуална камера</strong>: изграждаш сцената в SplitCam, после избираш SplitCam като камера в ImLive.",
     "quick": "Използване на SplitCam с ImLive: инсталирай SplitCam, изгради сцената с медийни слоеве, отвори ImLive и започни видео чат, в настройките на ImLive избери SplitCam като уебкамера и микрофон."
              "<ol><li>Инсталирай SplitCam.</li><li>Изгради сцена в SplitCam.</li>"
              "<li>Започни видео чат в ImLive.</li>"
              "<li>Избери SplitCam като ImLive камера.</li><li>Започни чата.</li></ol>",
     "steps": [
         ("Инсталирай SplitCam",
          "SplitCam е безплатен софтуер за Windows и macOS. Инсталирай — без воден знак, без регистрация. За ImLive работи като <strong>виртуална камера</strong>, не като RTMP енкодер."),
         ("Изгради сцена в SplitCam",
          "Отвори SplitCam и използвай <strong>Media Layers +</strong>, за да добавиш уебкамерата плюс наслагвания, текст, филтри или AI фон. Тази съставена сцена е това, което ImLive ще види като твоята камера."),
         ("Започни видео чат в ImLive",
          "Влез в сайта ImLive и кликни <strong>Start Video Chat</strong>, после отвори <strong>Go To Settings</strong>, за да стигнеш до опциите за камера и микрофон."),
         ("Избери SplitCam като камера",
          "В настройките на ImLive избери <strong>SplitCam</strong> като уебкамера И като микрофон. ImLive сега показва пълната ти SplitCam сцена вместо плоска уебкамера."),
         ("Започни Free Live Chat",
          "Кликни <strong>Free Live Chat</strong> в ImLive, за да си на живо. За да смениш визията в средата на сесията, редактирай сцената в SplitCam — ImLive обновява моментално."),
     ],
     "tips": [
         ("Не е нужен stream key", "ImLive няма RTMP — не търси URL на сървър или ключ. SplitCam е само избран като устройство-камера."),
         ("Настрой SplitCam и за микрофон", "Избери SplitCam за микрофон освен за камера, така че аудио миксът и шумоподтискането също да преминат в live."),
         ("Изгради сцена преди live", "ImLive показва каквото SplitCam изпраща — подреди слоевете преди да започнеш чата."),
         _T_TEST,
     ],
     "faq": [
         ("ImLive използва ли RTMP или stream key?", "Не — ImLive използва уебкамерата директно през браузъра. SplitCam свързва като виртуална камера, няма ключ за копиране."),
         ("Как избирам SplitCam в ImLive?", "Start Video Chat → Go To Settings → избери SplitCam като уебкамера и микрофон."),
         ("Мога ли да използвам наслагвания в ImLive?", "Да — изграждаш ги в SplitCam сцената; ImLive показва съставения резултат."),
         ("SplitCam безплатен ли е за ImLive?", "Да — безплатен, без воден знак и без времево ограничение. Като виртуална камера за ImLive не добавя цена или брандиране към твоя видео чат."),
     ]},
    {"slug": "vxlive", "name": "VXLive",
     "title": "Излъчване в VXLive със SplitCam — Официална поддръжка",
     "desc": "Излъчване в VXLive (VXModels / VISIT-X) с безплатен SplitCam — официален VISIT-X preset, сървър и ключ, сцени. Без воден знак.",
     "kw": "vxlive, visit-x, vxmodels splitcam, излъчване vxlive, visit-x stream, vxlive rtmp",
     "h1html": 'Как да излъчваш в <span class="accent">VXLive</span> със SplitCam',
     "h1short": "Излъчване VXLive",
     "card": "VXLive поддържа SplitCam официално (VISIT-X preset).",
     "intro": "VXLive (VXModels / VISIT-X) е кам платформа от немския пазар — и една от малкото, които <strong style='color:var(--text)'>поддържат SplitCam официално по име</strong>. VXModels има специална помощна статия за свързване на <strong style='color:var(--text)'>SplitCam</strong> към VXLive, а SplitCam предлага VISIT-X като готов канал preset.",
     "quick": "Излъчване в VXLive със SplitCam: инсталирай SplitCam, изгради сцената, в VXLive избери «Stream with third-party software», копирай URL на сървъра и ключа, в SplitCam избери VISIT-X preset и постави, Go Live в SplitCam, после GO ONLINE в VXLive."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи URL на сървъра + ключ от VXLive.</li>"
              "<li>Избери VISIT-X preset в SplitCam, постави.</li>"
              "<li>Go Live, после GO ONLINE в VXLive.</li></ol>",
     "key_how": "В VXLive избери <strong>Stream with third-party software</strong> и избери опцията за <strong>OBS, SplitCam или XSplit</strong>. VXLive предоставя <strong>URL на сървъра</strong> и <strong>stream key</strong>. В SplitCam избери <strong>VISIT-X</strong> като стрийминг платформа, постави и двете, натисни <strong>Go Live</strong> в SplitCam, после <strong>GO ONLINE</strong> в VXLive.",
     "tips": [
         ("VISIT-X е интегриран preset", "Не въвеждай суров RTMP URL — SplitCam има VISIT-X в списъка с платформи; само избираш и поставяш URL на сървъра и ключа."),
         ("Go-live в две стъпки", "В VXLive натискаш Go Live в SplitCam първо, после GO ONLINE в VXLive — и двете, в този ред."),
         ("Немски пазар", "Публиката на VXLive е предимно немскоговоряща — текстово наслагване или заглавие на немски помага да се свържеш със зрителите."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли VXLive SplitCam официално?", "Да — VXModels (VXLive) има официална помощна статия, посветена на настройката на SplitCam, и изброява SplitCam наред с OBS и XSplit като поддържан broadcasting софтуер."),
         ("Как свързвам SplitCam с VXLive?", "В VXLive избираш «Stream with third-party software», после в SplitCam избираш VISIT-X preset и поставяш URL на сървъра и stream key, предоставени от VXLive."),
         ("В SplitCam ли отивам на живо, или в VXLive?", "И двете — първо Go Live в SplitCam, после GO ONLINE в VXLive."),
         ("Защо VXModels препоръчва SplitCam?", "Официалната помощна статия на VXModels препоръчва SplitCam специално за елиминиране на артефакти и пикселация на уебкамерата и стабилизиране на връзката — не само като общ енкодер."),
     ]},
    {"slug": "virtwish", "name": "VirtWish",
     "title": "Излъчване в VirtWish със SplitCam — URL на стрийма & ключ",
     "desc": "Излъчване в VirtWish с безплатен SplitCam — Profile → Start Broadcast OBS секция, URL на стрийма и ключ, сцени и наслагвания.",
     "kw": "virtwish, излъчване virtwish, virtwish broadcasting software, virtwish rtmp, virtwish stream key, virtwish obs",
     "h1html": 'Как да излъчваш във <span class="accent">VirtWish</span> със SplitCam',
     "h1short": "Излъчване VirtWish",
     "card": "URL на стрийма + ключ за VirtWish.",
     "intro": "VirtWish е интерактивна кам платформа. Настройките за излъчване ти дават <strong style='color:var(--text)'>URL на стрийма и отделен stream key</strong> в OBS секция — безплатният <strong style='color:var(--text)'>SplitCam</strong> взема и двете и води шоуто със сцени и наслагвания.",
     "quick": "Излъчване във VirtWish със SplitCam: инсталирай SplitCam, изгради сцената, във VirtWish отвори <em>Profile → Start Broadcast</em> до OBS секцията, копирай линка и ключа, постави и двете в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи URL + ключ от VirtWish.</li><li>Постави и двете в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "Във VirtWish кликни иконата в горния десен ъгъл → <strong>Profile</strong> → <strong>Start Broadcast</strong>, после <strong>Start Broadcast</strong> отново, за да стигнеш до OBS секцията. <strong>Копирай линка от първия ред</strong> в полето Stream URL на SplitCam, а <strong>Stream Key</strong> отделно в полето за ключ.",
     "tips": [
         ("Линк на първия ред", "OBS секцията на VirtWish слага URL на стрийма на първия ред — копирай в Stream URL на SplitCam, после отделния ключ."),
         ("Два клика на Start Broadcast", "Натискаш Start Broadcast два пъти във VirtWish, за да стигнеш OBS секцията — очаквано, не бъг."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Къде са RTMP данните на VirtWish?", "Икона горе дясно → Profile → Start Broadcast два пъти → OBS секцията показва линка и stream key."),
         ("Поддържа ли VirtWish външни енкодери?", "Да — OBS секцията предоставя URL на стрийма и ключ, така че SplitCam работи."),
         ("Какъв битрейт за VirtWish?", "VirtWish не публикува официален таван; 3500–6000 Kbps на 1080p е безопасно. Съвпадай резолюцията на SplitCam с тази, зададена във VirtWish, за да избегнеш rescaling."),
         ("SplitCam безплатен ли е за VirtWish?", "Да — безплатен, без воден знак и без времево ограничение. Настройката URL-и-ключ на VirtWish струва само минутите, нужни за нея."),
     ]},
    {"slug": "xmodels", "name": "XModels",
     "title": "Излъчване в XModels със SplitCam — Безплатно ръководство",
     "desc": "Излъчване в XModels с безплатен SplitCam — опция външен енкодер в настройките на модел акаунта, RTMP ключ, сцени и наслагвания.",
     "kw": "xmodels, излъчване xmodels, xmodels broadcasting software, xmodels rtmp, xmodels external encoder",
     "h1html": 'Как да излъчваш в <span class="accent">XModels</span> със SplitCam',
     "h1short": "Излъчване XModels",
     "card": "Външен енкодер за XModels стрийм.",
     "intro": "XModels е кам-стрийминг платформа с вградена <strong style='color:var(--text)'>опция за външен енкодер</strong> в настройките на модел акаунта. Безплатният <strong style='color:var(--text)'>SplitCam</strong> излъчва там с мулти-камера сцени, наслагвания и филтри вместо една плоска камера.",
     "quick": "Излъчване в XModels със SplitCam: инсталирай SplitCam, изгради сцената, в XModels модел акаунта активирай опцията за външен енкодер, копирай URL на сървъра и stream key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Активирай външен енкодер в XModels настройките.</li>"
              "<li>Постави URL + ключ в SplitCam.</li><li>Натисни Go Live.</li></ol>",
     "key_how": "В <strong>настройките на модел акаунта</strong> на XModels активирай опцията <strong>излъчване чрез външен енкодер</strong>. XModels предоставя <strong>stream key</strong> — копирай в SplitCam. Ако опцията не е там, където очакваш, поддръжката на XModels е чрез FAQ чат на сайта и <strong>info@xmodels.com</strong>; видеото горе го показва също.",
     "tips": [
         ("В настройките на акаунта", "XModels слага опцията за външен енкодер в настройките на модел акаунта, не на отделен екран за излъчване."),
         ("Поддръжка: чат + имейл", "XModels няма голям публичен help център — FAQ чатът на сайта и info@xmodels.com са официалните канали за поддръжка."),
         ("Натрупвай наслагвания в SplitCam", "Цели на тип, име и социални handle-ове като слоеве на сцена — базовата камера на XModels не добавя такива."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли XModels външни енкодери?", "Да — настройките на модел акаунта включват опция за излъчване чрез външен енкодер, която предоставя stream key, така че SplitCam работи."),
         ("Къде да търся помощ за XModels?", "Поддръжката на XModels е чрез FAQ чат на сайта и имейла info@xmodels.com — няма голям публичен help център."),
         ("Какъв битрейт за XModels?", "XModels не документира официална цифра — използвай 3500–6000 Kbps на 1080p и пусни теста за скорост на SplitCam, тъй като поддръжката е само чат и имейл."),
         ("SplitCam безплатен ли е за XModels?", "Да — безплатен, без воден знак и без времево ограничение, така че излъчване към европейската мрежа на XModels не добавя софтуерен разход."),
     ]},
    {"slug": "flirt4free", "name": "Flirt4Free",
     "title": "Излъчване в Flirt for Free cam със SplitCam — Безплатно ръководство",
     "desc": "Излъчване в Flirt for Free cam с безплатен SplitCam — External Broadcast Form, RTMP URL и Stream Name, сцени и наслагвания.",
     "kw": "flirt for free cam, flirt 4 free cam, flirt4free, излъчване flirt4free, flirt4free external broadcast, flirt4free rtmp",
     "h1html": 'Как да излъчваш във <span class="accent">Flirt4Free</span> със SplitCam',
     "h1short": "Излъчване Flirt4Free",
     "card": "External Broadcast Form за Flirt4Free.",
     "intro": "Flirt4Free е една от най-старите кам платформи, в ефир от 90-те. Поддържа външно излъчване официално чрез <strong style='color:var(--text)'>External Broadcast Form</strong> — безплатният <strong style='color:var(--text)'>SplitCam</strong> изпраща стрийма, докато формулярът задава резолюцията и битрейта.",
     "quick": "Излъчване във Flirt4Free със SplitCam: инсталирай SplitCam, изгради сцената, отвори External Broadcast Form на Flirt4Free, копирай RTMP URL и Stream Name и задай резолюция/битрейт, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Отвори External Broadcast Form на Flirt4Free.</li>"
              "<li>Постави RTMP URL + Stream Name в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "В модел зоната на Flirt4Free отвори <strong>External Broadcast Form</strong>. За разлика от повечето кам сайтове, Flirt4Free ти дава <strong>RTMP URL</strong> и <strong>Stream Name</strong> (не «ключ»), плюс полета за резолюция и битрейт, които попълваш в самия формуляр. Копирай URL и Stream Name в полетата за сървър и ключ на SplitCam.",
     "tips": [
         ("Stream Name, не ключ", "Flirt4Free нарича удостоверението Stream Name. Поставяш го в полето stream key на SplitCam — играе същата роля."),
         ("Задай резолюция/битрейт във формуляра", "External Broadcast Form на Flirt4Free има собствени полета за резолюция и битрейт — изравни с настройките на SplitCam, за да не се прави rescaling на образа."),
         ("Историческа платформа", "Flirt4Free работи от 90-те — модел инструментите са зрели и External Broadcast Form е документирана част от тях."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли Flirt4Free външни енкодери?", "Да — официално, чрез External Broadcast Form, която предоставя RTMP URL и Stream Name. SplitCam работи като енкодер."),
         ("Откъде вземам RTMP данните на Flirt4Free?", "От External Broadcast Form в модел зоната — показва RTMP URL, Stream Name и полета за резолюция/битрейт."),
         ("Какъв битрейт за Flirt4Free?", "3500–6000 Kbps на 1080p — задай същата стойност в External Broadcast Form и в SplitCam."),
         ("SplitCam безплатен ли е за Flirt4Free?", "Да — безплатен, без воден знак и без времево ограничение, което съвпада с историческа платформа като Flirt4Free, където шоутата могат да са дълги."),
     ]},
    {"slug": "mfc-alerts", "name": "MFC Alerts",
     "title": "Добави MFC Alerts към стрийма със SplitCam",
     "desc": "Показвай анимирани tip alerts в твоя MyFreeCams стрийм — mfcalerts.com URL като Browser слой в безплатния SplitCam, над уебкамерата.",
     "kw": "mfc alerts, myfreecams alerts, добави mfc alerts, mfcalerts splitcam, myfreecams tip alerts, myfreecams alerts overlay",
     "h1html": 'Как да добавиш <span class="accent">MFC Alerts</span> към стрийма',
     "h1short": "Добави MFC Alerts",
     "card": "Показвай анимирани tip alerts в MyFreeCams стрийма.",
     "intro": "MFC Alerts показва анимирани ефекти в твоя MyFreeCams стрийм всеки път, когато зрител изпрати тип. Работи като <strong style='color:var(--text)'>Browser слой</strong> в безплатния <strong style='color:var(--text)'>SplitCam</strong> — настройваш веднъж и типовете задействат реакции на екрана на живо.",
     "quick": "Добавяне на MFC Alerts със SplitCam: инсталирай SplitCam, добави уебкамерата, отвори Browser таба и зареди mfcalerts.com, копирай твоя alerts URL, добави като Browser слой над уебкамерата, после тествай с тестов тип."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави уебкамерата.</li>"
              "<li>Вземи URL от mfcalerts.com.</li>"
              "<li>Добави като Browser слой над уебкамерата.</li>"
              "<li>Изпрати тестов тип.</li></ol>",
     "steps": [
         ("Инсталирай SplitCam и добави уебкамерата",
          "Инсталирай безплатния SplitCam за Windows или macOS, после добави <strong>уебкамерата</strong> като източник. MFC Alerts стои като слой върху тази камера."),
         ("Отвори Browser таб и иди на mfcalerts.com",
          "В SplitCam отвори таба <strong>Browser</strong> и навигирай към <strong>www.mfcalerts.com</strong>. Влез или се регистрирай, ако още нямаш mfcalerts.com акаунт."),
         ("Копирай твоя alerts URL",
          "В mfcalerts.com използвай <strong>Copy to clipboard</strong>, за да копираш личния си alerts URL — това е страницата, която рендира tip анимациите."),
         ("Добави URL като Browser слой — над уебкамерата",
          "Постави URL в Browser прозореца на SplitCam и кликни <strong>Add</strong>. После пренареди списъка с източници така, че <strong>MFC Alerts да е над уебкамерата</strong> (3-точково меню → Move Up). Ако стои под, ефектите остават скрити."),
         ("Тествай с тестов тип",
          "Отвори <strong>Settings → Send test tip</strong> и потвърди, че alert ефектът се появява над камерата. После излъчвай нормално в MyFreeCams — реалните типове сега задействат анимациите."),
     ],
     "tips": [
         ("MFC Alerts трябва да е над уебкамерата", "Най-честата грешка: ако MFC Alerts слоят е под уебкамерата в списъка с източници, ефектите остават скрити. Качи го."),
         ("Нужен е mfcalerts.com акаунт", "Alerts URL е личен — регистрирай се в mfcalerts.com първо, ако нямаш акаунт."),
         ("Изпрати тестов тип преди live", "Използвай Settings → Send test tip, за да потвърдиш, че overlay-ят работи — не откривай грешката в средата на шоуто."),
         _T_ETH,
     ],
     "faq": [
         ("Какво е MFC Alerts?", "Система за известия за MyFreeCams, която показва видео ефекти в стрийма, когато зрители изпращат типове — добавя се като Browser overlay в SplitCam."),
         ("Защо MFC Alerts не се появяват?", "Почти винаги е реда на слоевете — MFC Alerts Browser слоят трябва да е над уебкамерата в списъка с източници на SplitCam."),
         ("Нужен ли е акаунт за MFC Alerts?", "Да — регистрирай се в mfcalerts.com, за да получиш личния си alerts URL."),
         ("SplitCam безплатен ли е за това?", "Да — SplitCam е безплатен, без воден знак и без времево ограничение, а MFC Alerts browser overlay работи в него без допълнителни разходи."),
     ]},
    {"slug": "lovense", "name": "Lovense",
     "title": "Добави Lovense играчка към стрийма със SplitCam",
     "desc": "Свържи интерактивна Lovense играчка към кам стрийм с безплатен SplitCam — Lovense SplitCam Toolset, tip alerts на екрана, реакции.",
     "kw": "добави lovense към стрийм, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense interactive toy streaming",
     "h1html": 'Как да добавиш <span class="accent">Lovense играчка</span> към стрийма',
     "h1short": "Добави Lovense играчка",
     "card": "Свържи интерактивна Lovense играчка към кам стрийма.",
     "intro": "Пускаш кам стрийма през безплатния <strong style='color:var(--text)'>SplitCam</strong> и сдвояваш <strong style='color:var(--text)'>Lovense</strong> играчка, която реагира на токени. Lovense документира официален <strong style='color:var(--text)'>Lovense SplitCam Toolset</strong>, а SplitCam предоставя официален Lovense плъгин — интеграцията се поддържа и от двете страни.",
     "quick": "За добавяне на Lovense играчка към стрийма: инсталирай SplitCam и Lovense софтуера, сдвой играчката, свържи Lovense към кам платформата, добави Lovense статус като Browser слой в SplitCam, после излъчвай нормално."
              "<ol><li>Инсталирай SplitCam.</li><li>Инсталирай Lovense софтуер и сдвой играчка.</li>"
              "<li>Свържи Lovense към кам сайта.</li>"
              "<li>Добави Lovense overlay в SplitCam.</li><li>Натисни Go Live.</li></ol>",
     "steps": [
         ("Инсталирай SplitCam",
          "SplitCam е безплатен софтуер за стрийминг за Windows и macOS — енкодерът, който изпраща видеото към кам платформата. Инсталирай; без воден знак."),
         ("Инсталирай Lovense софтуера и сдвой играчката",
          "Инсталирай Lovense Connect / Lovense Stream (официалното desktop приложение). Включи играчката и сдвой чрез Bluetooth, така че приложението да показва свързано."),
         ("Свържи Lovense към кам платформата",
          "В Lovense приложението свържи кам акаунта си, така че играчката да реагира на токени / типове от зрителите. Повечето големи кам платформи се поддържат."),
         ("Добави Lovense overlay в SplitCam",
          "Lovense предоставя overlay/widget URL. Добави като <strong>Browser</strong> слой в SplitCam сцената, така че зрителите да виждат статуса на играчката и скорошните типове на екрана."),
         ("Изгради сцена и Go Live",
          "Добави камерата и другите наслагвания, постави RTMP ключа на кам платформата в SplitCam и кликни <strong>Go Live</strong>. Играчката реагира на типове в реално време."),
     ],
     "tips": [
         ("Използвай официалния Lovense SplitCam Toolset", "Lovense публикува SplitCam-специфичен toolset със собствено ръководство за инсталация — добавя overlay за активността на играчката и tip alerts, направени за SplitCam."),
         ("Актуализирай Lovense Cam Extension", "Toolset-ът изисква скорошен Lovense Cam Extension (30.1.4 или по-нов) — актуализирай преди live."),
         ("Дръж играчката заредена", "Почти празна батерия в средата на шоуто убива интерактивната част — зареди напълно преди live."),
         ("Тествай реакция на токени", "Изпрати малък тестов тип, за да потвърдиш, че играчката реагира, преди да отвориш стаята."),
         ("Провери изискванията за версия", "Lovense SplitCam Toolset изисква SplitCam 10.4.5 или по-нов. Lovense Cam Extension покрива официално Chaturbate, Stripchat, BongaCams, MyFreeCams и CamSoda — за всеки друг сайт използвай Generic URL интеграцията на Lovense."),
     ],
     "faq": [
         ("Поддържа ли Lovense SplitCam официално?", "Да — Lovense документира официален «Lovense SplitCam Toolset» със собствено ръководство за инсталация, а SplitCam предоставя официален Lovense плъгин. Интеграцията се поддържа и от двете страни."),
         ("Играчката свързва ли се директно с SplitCam?", "Не — играчката се сдвоява с Lovense приложението; SplitCam показва Lovense overlay и излъчва камерата."),
         ("Кои кам сайтове поддържат Lovense?", "Cam Extension на Lovense поддържа официално Chaturbate, Stripchat, BongaCams, MyFreeCams и CamSoda, с променлива поддръжка за други — провери актуалния списък в Lovense приложението."),
         ("Мога ли да показвам скорошни типове на екрана?", "Да — добави URL на Lovense widget като Browser слой в SplitCam."),
     ]},
    {"slug": "multistream-cams", "name": "Няколко кам сайта",
     "title": "Излъчване на няколко кам сайта едновременно със SplitCam",
     "desc": "Излъчване на MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat и още едновременно с безплатния multistreaming на SplitCam. Един клик, без воден знак.",
     "kw": "излъчване на няколко кам сайта, multistream cam sites, излъчване chaturbate и bongacams едновременно, multistream cam софтуер",
     "h1html": 'Как да излъчваш на <span class="accent">няколко кам сайта</span> едновременно',
     "h1short": "Кам мултистрийминг",
     "card": "Излъчване на няколко кам сайта едновременно.",
     "intro": "Безплатният <strong style='color:var(--text)'>SplitCam</strong> може да излъчва едно кодиране към <strong style='color:var(--text)'>няколко кам сайта едновременно</strong> — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat и още. Без воден знак, един клик.",
     "quick": "За излъчване на няколко кам сайта наведнъж: инсталирай SplitCam, изгради сцената, вземи URL на RTMP сървъра и stream key от всеки кам сайт, добави всички в настройките за multistreaming на SplitCam, кликни Go Live веднъж."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи RTMP ключ от всеки кам сайт.</li>"
              "<li>Добави всички ключове в multistream на SplitCam.</li>"
              "<li>Натисни Go Live веднъж.</li></ol>",
     "steps": [
         ("Инсталирай SplitCam",
          "SplitCam е безплатен софтуер за стрийминг за Windows и macOS с вграден multistreaming. Инсталирай — без воден знак, без регистрация."),
         ("Настрой камера и сцена",
          "Отвори SplitCam, добави уебкамерата и изгради сцената с наслагвания и филтри. Една сцена захранва всяка дестинация."),
         ("Вземи RTMP ключ от всеки кам сайт",
          "Във всяка кам платформа активирай външното/RTMP излъчване и копирай <strong>URL на сървъра</strong> и <strong>stream key</strong>. Повтори за всеки сайт, на който искаш да излъчваш — виж индивидуалните ръководства за платформите за точните пътища."),
         ("Добави всяка дестинация в SplitCam",
          "Отвори <strong>Stream Settings</strong> и добави всеки кам сайт като персонализирана RTMP дестинация — постави URL на сървъра и ключа. Маркирай всичко, което искаш да е на живо."),
         ("Кликни Go Live веднъж",
          "Натисни <strong>Go Live</strong>. SplitCam изпраща стрийма към всеки избран кам сайт едновременно, peer-to-peer, от едно единствено кодиране — без допълнителна такса."),
     ],
     "tips": [
         ("Следи upload-а си", "Мултистрийминг-ът умножава товара върху upload-а. Всяка дестинация консумира собствен битрейт — увери се, че връзката издържа сумата."),
         ("Провери правилата на платформите", "Някои кам сайтове забраняват едновременно излъчване другаде — потвърди преди мултистрийминг."),
         ("Кабел — не можеш да си позволиш drops тук", "Мултистрийминг-ът умножава товара върху upload-а, така че едно прекъсване на wi-fi може да събори всички дестинации едновременно. Кабел не е опционален тук."),
         ("Наблюдавай health monitor-а", "SplitCam показва статус по дестинация — пусни сайт, ако upload-ът ти не го издържа."),
     ],
     "faq": [
         ("SplitCam multistreaming безплатен ли е?", "Да — multistreaming-ът е вграден и безплатен, без такса на дестинация, без воден знак."),
         ("На колко кам сайта мога да излъчвам едновременно?", "Толкова, колкото upload-ът ти издържа — всяка дестинация консумира собствен битрейт."),
         ("Използва ли cloud relay?", "Не — SplitCam изпраща стриймовете peer-to-peer директно от PC-то към ingest на всяка платформа."),
         ("Multistreaming-ът забавя ли PC-то?", "Кодирането се прави веднъж и се преизползва; хардуерното кодиране държи CPU товара нисък. Upload bandwidth-ът е реалният лимит."),
     ]},
]
