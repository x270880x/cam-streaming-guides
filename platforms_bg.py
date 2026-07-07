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
     "kw": "как да излъчвате на chaturbate, chaturbate, chaturbate broadcast, chaturbate obs, chaturbate external encoder, chaturbate rtmp, chaturbate stream key",
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
     "kw": "как да излъчвате на cam4, cam4, cam4 broadcast, cam4 obs, cam4 external encoder, cam4 rtmp, cam4 stream key",
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
     "kw": "как да излъчвате на bongacams, bongacams, bongacams broadcast, bongacams obs, bongacams external encoder, bongacams rtmp, bongacams stream key",
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
     "kw": "как да излъчвате на stripchat, stripchat, stripchat broadcast, stripchat obs, stripchat external encoder, stripchat rtmp, stripchat stream key",
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
     "kw": "как да излъчвате на живо в onlyfans, onlyfans, onlyfans live, onlyfans broadcast, onlyfans obs, onlyfans rtmp, onlyfans stream key",
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
     "title": "Излъчване в CamPlace със SplitCam — RTMP & ключ",
     "desc": "Излъчване в CamPlace с безплатен SplitCam — външен енкодер, RTMP ключ, сцени и наслагвания. Стъпка по стъпка, без воден знак.",
     "kw": "как да излъчвате на camplace, camplace, camplace broadcast, camplace obs, camplace external encoder, camplace rtmp, camplace stream key",
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
     "kw": "как да излъчвате на camsoda, camsoda, camsoda broadcast, camsoda obs, camsoda external encoder, camsoda rtmp, camsoda stream key",
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
     "kw": "как да излъчвате на streamate, streamate, streamate broadcast, streamate obs, streamate sm connect, streamate rtmp, streamate stream key",
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
     "kw": "как да излъчвате на streamray, streamray, streamray broadcast, streamray obs, streamray external encoder, streamray rtmp, streamray stream key",
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
     "kw": "как да излъчвате на xlovecam, xlovecam, xlovecam broadcast, xlovecam obs, xlovecam external encoder, xlovecam rtmp, xlovecam stream key",
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
     "kw": "как да излъчвате на soulcams, soulcams, soulcams broadcast, soulcams obs, soulcams external encoder, soulcams rtmp, soulcams stream key",
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
     "kw": "как да излъчвате на imlive, imlive, imlive broadcast, imlive virtual camera, imlive виртуална камера, imlive webcam, imlive splitcam",
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
     "kw": "как да излъчвате на vxlive, vxlive, vxlive broadcast, vxlive obs, vxlive external encoder, vxlive rtmp, vxlive stream key, visit-x",
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
     "title": "Излъчване във VirtWish със SplitCam — RTMP & ключ",
     "desc": "Излъчване във VirtWish с безплатен SplitCam — външен енкодер, URL на стрийма и RTMP ключ, сцени и наслагвания. Без воден знак.",
     "kw": "как да излъчвате на virtwish, virtwish, virtwish broadcast, virtwish obs, virtwish external encoder, virtwish rtmp, virtwish stream key",
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
     "title": "Излъчване в XModels със SplitCam — RTMP & ключ",
     "desc": "Излъчване в XModels с безплатен SplitCam — външен енкодер в модел акаунта, RTMP ключ, сцени и наслагвания. Без воден знак.",
     "kw": "как да излъчвате на xmodels, xmodels, xmodels broadcast, xmodels obs, xmodels external encoder, xmodels rtmp, xmodels stream key",
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
     "title": "Излъчване в Flirt4Free със SplitCam — RTMP & ключ",
     "desc": "Излъчване във Flirt4Free с безплатен SplitCam — External Broadcast Form, RTMP URL и Stream Name, сцени и наслагвания. Без воден знак.",
     "kw": "как да излъчвате на flirt4free, flirt4free, flirt for free cam, flirt4free broadcast, flirt4free obs, flirt4free external encoder, flirt4free rtmp",
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
     "kw": "добавяне на mfc alerts към стрийма, mfc alerts, myfreecams, myfreecams alerts, myfreecams tip alerts, mfcalerts overlay, mfcalerts splitcam",
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
     "desc": "Свържи Lovense играчка към SplitCam стрийма — Lovense Connect, Cam Extension и официалния SplitCam Toolset, с tip alerts на екрана.",
     "kw": "добавяне на lovense към стрийма, lovense, lovense cam stream, lovense splitcam toolset, lovense cam extension, lovense connect, lovense tip alerts, lovense interactive toy streaming, lovense toy overlay",
     "h1html": 'Как да добавиш <span class="accent">Lovense играчка</span> към стрийма',
     "h1short": "Добави Lovense играчка",
     "card": "Свържи интерактивна Lovense играчка към кам стрийма.",
     "intro": "Пускаш кам стрийма през безплатния <strong style='color:var(--text)'>SplitCam</strong> и сдвояваш "
              "интерактивна <strong style='color:var(--text)'>Lovense</strong> играчка, така че тя да реагира на "
              "бакшишите. Инсталираш три неща: <strong>SplitCam</strong> (енкодерът), приложението "
              "<strong>Lovense Connect</strong> (Bluetooth мостът до играчката) и "
              "<strong>Lovense Cam Extension</strong> за Chrome/Edge (то чете бакшишите и захранва overlay-а на екрана). "
              "Lovense публикува и официален <strong style='color:var(--text)'>Lovense SplitCam Toolset</strong> на "
              "страницата с плъгини на SplitCam — интеграцията се поддържа и от двете страни.",
     "quick": "За да добавиш Lovense играчка към стрийма: инсталирай SplitCam, приложението Lovense Connect и "
              "Lovense Cam Extension, сдвой играчката, свържи разширението към кам сайта, добави Lovense overlay "
              "като Browser слой в SplitCam, после излъчвай нормално."
              "<ol><li>Инсталирай SplitCam.</li>"
              "<li>Инсталирай Lovense Connect и сдвой играчката.</li>"
              "<li>Инсталирай Lovense Cam Extension (Chrome/Edge).</li>"
              "<li>Свържи разширението към кам сайта + добави overlay-а в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "Играчката никога не се свързва директно със SplitCam. Веригата е: зрител праща бакшиш на кам сайта "
                "&rarr; <strong>Lovense Cam Extension</strong> в браузъра го засича &rarr; изпраща команда до "
                "приложението <strong>Lovense Connect</strong> на localhost &rarr; Connect задвижва играчката по "
                "Bluetooth и тя вибрира. Единствената задача на SplitCam е да показва <strong>Lovense overlay</strong> "
                "(статус на играчката + скорошни бакшиши) като Browser слой и да излъчва камерата. Няма отделно "
                "приложение „Lovense Browser“ — това е браузърно <em>разширение</em> за Chrome или Edge.",
     "steps": [
         ("Инсталирай SplitCam",
          "SplitCam е безплатен софтуер за стрийминг за Windows и macOS — енкодерът, който изпраща видеото към кам платформата. Инсталирай; без воден знак, без регистрация."),
         ("Инсталирай Lovense Connect и сдвой играчката",
          "Инсталирай приложението <strong>Lovense Connect</strong> (desktop, от lovense.com/connect) — или използвай <strong>Lovense Remote</strong> на телефона. Това е мостът, който говори с играчката по Bluetooth. Включи играчката и я сдвой, докато приложението покаже свързано."),
         ("Инсталирай Lovense Cam Extension",
          "Добави <strong>Lovense Cam Extension</strong> към Chrome или Edge (версия 30.1.4 или по-нова) и влез с Lovense акаунта си. Няма самостоятелен „Lovense Browser“ — това е разширение, което чете бакшишите и захранва overlay-а. За SplitCam-специфични уиджети вземи и официалния <strong>Lovense SplitCam Toolset</strong> от страницата с плъгини на SplitCam (splitcam.com/more-plugins)."),
         ("Свържи разширението към кам сайта и добави overlay-а в SplitCam",
          "В Cam Extension кликни <strong>+</strong>, за да добавиш кам сайта си (Chaturbate, Stripchat и т.н.), задай нивата на бакшишите, после отвори раздела <strong>Video Feedback</strong> и избери <strong>SplitCam</strong>. Копирай overlay URL-а, който ти дава, и го добави като <strong>Browser</strong> слой в SplitCam сцената, за да виждат зрителите статуса на играчката и скорошните бакшиши."),
         ("Изгради сцена и Go Live",
          "Добави камерата и другите наслагвания, постави RTMP ключа на кам платформата в SplitCam и кликни <strong>Go Live</strong>. Играчката вече реагира на бакшишите в реално време."),
     ],
     "tips": [
         ("Три инсталации, по ред", "SplitCam (енкодер) + Lovense Connect (Bluetooth мост) + Lovense Cam Extension (четец на бакшиши / overlay). Пропуснеш ли едно, играчката няма да реагира на стрийма."),
         ("Разширение е, не браузър", "Няма отделен „Lovense Browser“ за сваляне — Lovense Cam Extension се инсталира в Chrome или Edge. Дръж го актуално (30.1.4 или по-ново), иначе SplitCam overlay-ът може да не се зареди."),
         ("Дръж играчката заредена", "Почти празна батерия в средата на шоуто убива интерактивната част — зареди напълно преди live."),
         ("Тествай реакцията на бакшиш", "Изпрати малък тестов бакшиш, за да потвърдиш, че играчката реагира, преди стаята да е публична."),
         ("Провери изискванията за версия", "Lovense SplitCam Toolset изисква SplitCam 10.4.5 или по-нов. Lovense Cam Extension покрива официално Chaturbate, Stripchat, BongaCams, MyFreeCams и CamSoda — за всеки друг сайт използвай Generic URL интеграцията на Lovense."),
     ],
     "faq": [
         ("Какво трябва да инсталирам за Lovense на SplitCam?", "Три неща: <strong>SplitCam</strong> (енкодерът), приложението <strong>Lovense Connect</strong> (свързва играчката по Bluetooth) и <strong>Lovense Cam Extension</strong> за Chrome/Edge (чете бакшишите и захранва overlay-а). По желание добави и официалния Lovense SplitCam Toolset от splitcam.com/more-plugins."),
         ("Има ли „Lovense Browser“, който трябва да сваля?", "Не. Няма самостоятелен Lovense браузър — това е <strong>Lovense Cam Extension</strong>, което се инсталира в Chrome или Edge. Сдвояването на играчката се поема от отделното приложение Lovense Connect (desktop) или Lovense Remote (телефон)."),
         ("Играчката свързва ли се директно с SplitCam?", "Не — играчката се сдвоява с приложението Lovense Connect по Bluetooth; Cam Extension чете бакшишите, а SplitCam само показва overlay-а и излъчва камерата."),
         ("Кои кам сайтове поддържат Lovense?", "Lovense Cam Extension поддържа официално Chaturbate, Stripchat, BongaCams, MyFreeCams и CamSoda, с променлива поддръжка за други — провери актуалния списък в Lovense приложението."),
         ("Мога ли да показвам скорошни бакшиши на екрана?", "Да — Cam Extension ти дава overlay URL; добави го като Browser слой в SplitCam и зрителите виждат статуса на играчката и скорошните бакшиши."),
     ]},
    {"slug": "multistream-cams", "name": "Няколко кам сайта",
     "title": "Излъчване на няколко кам сайта едновременно",
     "desc": "Излъчване на Chaturbate, BongaCams, CAM4, Stripchat и още едновременно с безплатния multistream на SplitCam. Един клик, без воден знак.",
     "kw": "излъчване на няколко кам сайта едновременно, multistream cam sites, multistream cam, излъчване chaturbate и bongacams едновременно, multistream софтуер",
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
    {"slug": "livejasmin", "name": "LiveJasmin",
     "title": "Излъчване в LiveJasmin със SplitCam — HD външен енкодер",
     "desc": "Излъчване в LiveJasmin с безплатен SplitCam — External Encoder на Model Center, HD 1080p, мулти-камера сцени и наслагвания. Без воден знак.",
     "kw": "как да излъчвате на livejasmin, livejasmin, livejasmin broadcast, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key",
     "h1html": 'Как да излъчваш в <span class="accent">LiveJasmin</span> със SplitCam',
     "h1short": "Излъчване LiveJasmin",
     "card": "Настройка с външен енкодер за HD-only Model Center на LiveJasmin.",
     "intro": "LiveJasmin е флагманът на Docler Holding — една от най-големите кам мрежи в света и HD-only платформа. Предпочитаният broadcaster е собственият им клиент <strong>JasminCAM</strong>, но Model Center излага и стандартен път през <strong>External Encoder</strong>, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — и излъчваш с мулти-камера сцени, beauty филтри и наслагвания на същия HD стрийм.",
     "quick": "Излъчване в LiveJasmin със SplitCam: инсталирай SplitCam, изгради HD сцената, в Model Center влез в <em>Settings → Broadcast → External Encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + HD сцена.</li>"
              "<li>Вземи URL и stream key от Model Center.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "Влез в <strong>modelcenter.livejasmin.com</strong>, отвори <strong>Settings → Broadcast → External Encoder</strong>. Model Center показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта ти — копирай и двете в полетата за custom RTMP в SplitCam. <strong>Забележка:</strong> новите акаунти трябва да бъдат одобрени (48–72 часа), преди опцията External Encoder да се появи, а платформата налага HD-only output.",
     "tips": [
         ("HD или те свалят в класирането", "LiveJasmin е HD-only — всичко под 1280×720 рискува да бъде показвано само в списъци с по-ниска печалба, всичко под 1080p губи «Premium» допустимост. Карай 1920×1080 при 30 fps, 4 000–6 000 Kbps."),
         ("JasminCAM срещу външен енкодер", "Собственият клиент JasminCAM на Docler дава най-чистото HD съответствие, но външните енкодери (OBS, SplitCam, vMix) са официално поддържани след като акаунтът ти е одобрен — те отключват мулти-камера сцени и наслагвания, които JasminCAM не може."),
         ("Free chat ≠ private show", "Free chat е само preview — без голота. Private и Gold show-овете са там, където моделът печели. Планирай сцената си да изглежда силна и облечена, И в show режим."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли LiveJasmin официално външни енкодери като SplitCam?", "Да — Model Center включва опция External Encoder в Settings → Broadcast. JasminCAM е препоръчаният клиент, но OBS, SplitCam и други RTMP енкодери са изрично изброени като поддържани след одобрение на моделския акаунт."),
         ("Откъде вземам моя stream key за LiveJasmin?", "В Model Center: Settings → Broadcast → External Encoder. Там се появяват и server URL, и уникалният stream key — копирай и двете в полетата за custom RTMP на SplitCam. Ключът е обвързан с акаунта ти; третирай го като парола."),
         ("Какъв bitrate да използвам за LiveJasmin?", "LiveJasmin е HD-only — цели 1920×1080 при 30 fps, 4 000–6 000 Kbps с keyframe интервал 2 секунди. Всичко осезаемо под това губи Premium етикета и те свалят в класирането."),
         ("SplitCam безплатен ли е за LiveJasmin?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Единственото «плащане» е покриването на HD изискванията на LiveJasmin, което SplitCam върши нативно с 1080p композиция на сцени и beauty филтри."),
     ],
     "steps": [
         ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Той е енкодерът, който изпраща HD видеото ти към LiveJasmin."),
         ("Изгради HD сцената", "Отвори SplitCam и добави уебкамерата си в 1080p режим. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty филтри или AI фон — LiveJasmin изисква HD качество, а композираната ти сцена трябва да изглежда premium както във free chat, ТАКА И в private show."),
         ("Вземи URL и stream key от LiveJasmin", "Влез в <strong>modelcenter.livejasmin.com</strong> (акаунтът ти трябва първо да бъде одобрен — обикновено 48–72 часа след регистрация). Отвори <strong>Settings → Broadcast → External Encoder</strong>. Страницата показва <strong>server URL</strong> и уникален <strong>stream key</strong>. Копирай и двете."),
         ("Свържи SplitCam с LiveJasmin", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на LiveJasmin и stream key в полетата за custom RTMP. Сложи bitrate 4 000–6 000 Kbps при 1920×1080, 30 fps, с 2-секунден keyframe. Първо пусни вградения speed тест — HD стриймове са взискателни."),
         ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се качи онлайн в Model Center на LiveJasmin. За ~10 секунди HD-то ти стига до мрежата на LiveJasmin. Следващите излъчвания са един клик — отваряш SplitCam, Go Live, после онлайн в LiveJasmin."),
     ],
    },
    {"slug": "myfreecams", "name": "MyFreeCams",
     "title": "Излъчване в MyFreeCams със SplitCam — RTMP & ключ",
     "desc": "Излъчване в MyFreeCams с безплатен SplitCam — Model Admin External Broadcaster, RTMP ключ, мулти-камера сцени и наслагвания. Без воден знак.",
     "kw": "как да излъчвате на myfreecams, myfreecams, mfc, myfreecams broadcast, myfreecams obs, mfc external broadcaster, mfc rtmp, mfc stream key",
     "h1html": 'Как да излъчваш в <span class="accent">MyFreeCams</span> със SplitCam',
     "h1short": "Излъчване MyFreeCams",
     "card": "Настройка с external broadcaster за токен-базирания Model Admin на MFC.",
     "intro": "MyFreeCams (MFC) е една от най-старите кам платформи — чиста токен икономика, без задушаващ модел-одобрителен филтър и лоялна Premium member база. Подразбиращият се Model Web Broadcaster е едно-камерен браузър инструмент, но <strong>Model Admin</strong> излага и опция <strong>External Broadcaster</strong>, към която безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — отключвайки мулти-камера сцени, наслагвания и филтри върху същия токен стрийм.",
     "quick": "Излъчване в MyFreeCams със SplitCam: инсталирай SplitCam, изгради сцената, в Model Admin → Broadcaster превключи от Web Broadcaster на External Broadcaster, копирай server URL и stream key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Превключи в Model Admin на External Broadcaster.</li><li>Постави URL+key в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "Влез в MyFreeCams, отвори <strong>Model Admin → Broadcaster</strong> и превключи от <strong>Web Broadcaster</strong> на <strong>External Broadcaster</strong>. Страницата показва <strong>server URL</strong> (rtmp://publish.myfreecams.com…) и <strong>stream key</strong>, обвързани с моделския ти акаунт — копирай и двете в полетата за custom RTMP в SplitCam.",
     "tips": [
         ("MFC tokens, не абонаменти", "MFC е чиста tipping/токен икономика — Premium members могат на private, но ежедневният ти хляб са бакшишите във free chat. Оптимизирай сцената за видимо tip menu и реакции на живо."),
         ("Web срещу External Broadcaster", "Подразбиращият се е single-source, само браузър webcam; External Broadcaster отключва мулти-камера сцени, наслагвания и beauty filters от SplitCam върху същия стрийм."),
         ("Интеграция с MFC Alerts", "Добави URL за alert-и от mfcalerts.com като Browser слой над камерата — получаваш анимирани tip alert-и, които подтикват зрителите към нови tokens."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли MFC външни broadcasters?", "Да — Model Admin има опция External Broadcaster, стандартен RTMP, OBS/SplitCam/vMix работят без проблем. Подразбиращият се Web Broadcaster е само бързата браузър версия."),
         ("Откъде вземам моя stream key за MFC?", "Model Admin → Broadcaster → External Broadcaster показва server URL (rtmp://publish.myfreecams.com…) и уникалния ти stream key. Копирай и двете в полетата за custom RTMP на SplitCam."),
         ("Какъв bitrate да използвам за MyFreeCams?", "До ~6 000 Kbps с 2-секунден keyframe; карай 1920×1080 при 30 fps, 3 500–6 000 Kbps. MFC не налага строго HD, но Premium members виждат разликата веднага."),
         ("SplitCam безплатен ли е за MFC?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. MFC също не таксува за използване на External Broadcaster — просто се свързваш през RTMP."),
     ],
     "steps": [
         ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Той е енкодерът, който изпраща видеото ти към MyFreeCams."),
         ("Изгради сцената", "Отвори SplitCam и добави webcam-а. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон. Добави URL-а на mfcalerts.com като Browser слой за анимирани tip alert-и докато стриймваш."),
         ("Превключи на External Broadcaster", "Влез в Model Admin → <strong>Broadcaster</strong> и превключи от <strong>Web Broadcaster</strong> на <strong>External Broadcaster</strong>. Страницата показва server URL (rtmp://publish.myfreecams.com…) и уникален stream key. Копирай и двете."),
         ("Свържи SplitCam с MFC", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на MFC и stream key в полетата за custom RTMP. Сложи bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, с 2-секунден keyframe."),
         ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam — за секунди се появяваш в списъка на MyFreeCams. Следващите излъчвания са един клик: отваряш SplitCam, Go Live."),
     ],
    },
    {"slug": "cherry-tv", "name": "Cherry.tv",
     "title": "Излъчване в Cherry.tv със SplitCam — External Encoder",
     "desc": "Излъчване в Cherry.tv с безплатен SplitCam — Streamer Dashboard external encoder, RTMP ключ, мулти-камера сцени и наслагвания. Без воден знак.",
     "kw": "как да излъчвате на cherry.tv, cherry.tv, cherry tv broadcast, cherry.tv obs, cherry.tv external encoder, cherry.tv rtmp, cherry.tv stream key",
     "h1html": 'Как да излъчваш в <span class="accent">Cherry.tv</span> със SplitCam',
     "h1short": "Излъчване Cherry.tv",
     "card": "Настройка с външен енкодер за Streamer Dashboard на Cherry.tv.",
     "intro": "Cherry.tv е по-нова, бързо растяща кам платформа с Web3 уклон — крипто-friendly изплащания и по-нисък праг за вход от стари мрежи като LiveJasmin. Подразбиращият се broadcaster е браузър-базиран, но <strong>Streamer Dashboard</strong> излага стандартен път през <strong>External Encoder</strong>, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва.",
     "quick": "Излъчване в Cherry.tv със SplitCam: инсталирай SplitCam, изгради сцената, в Streamer Dashboard → Broadcast Settings → External Encoder копирай URL+key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи URL и stream key от Streamer Dashboard.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "Влез в streamer акаунта си в Cherry.tv, отвори <strong>Streamer Dashboard → Broadcast Settings → External Encoder</strong>. Появяват се <strong>server URL</strong> и <strong>stream key</strong> — копирай и двете. Новите акаунти първо минават през базова верификация (бърза).",
     "tips": [
         ("По-лек вход, растящ трафик", "Без 72-часов Docler-style review — Cherry.tv одобрява много по-бързо и е добро early-mover място, с млада, platform-savvy аудитория."),
         ("Налични крипто изплащания", "Cherry.tv предлага плащания в крипто наред със стандартен fiat — полезно, ако искаш да избегнеш банкови триения или да получаваш по-дискретно."),
         ("Браузър broadcaster-ът е single-source", "Подразбиращият се браузър broadcaster е една камера; SplitCam през External Encoder отключва мулти-камера, наслагвания и beauty filters върху същия стрийм."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли Cherry.tv външни енкодери?", "Да — Streamer Dashboard включва опция External Encoder, стандартен RTMP. OBS, SplitCam и vMix работят веднага след верификация на акаунта."),
         ("Откъде вземам моя stream key за Cherry.tv?", "Streamer Dashboard → Broadcast Settings → External Encoder. Server URL и уникалният stream key са там — копирай и двете в полетата за custom RTMP на SplitCam."),
         ("Какъв bitrate да използвам за Cherry.tv?", "3 500–6 000 Kbps при 1920×1080, 30 fps, с 2-секунден keyframe. Аудиторията на Cherry.tv е млада и свикнала с добро качество — не пести от резолюция."),
         ("SplitCam безплатен ли е за Cherry.tv?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Cherry.tv не таксува отделно за използване на външен енкодер."),
     ],
     "steps": [
         ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Той е енкодерът, който изпраща видеото ти към Cherry.tv."),
         ("Изгради сцената", "Отвори SplitCam и добави webcam-а. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон — аудиторията на Cherry.tv е млада и platform-savvy, сцената трябва да изглежда модерно."),
         ("Вземи URL и stream key", "В streamer акаунта си отвори <strong>Streamer Dashboard → Broadcast Settings → External Encoder</strong>. Копирай server URL и уникалния stream key."),
         ("Свържи SplitCam с Cherry.tv", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на Cherry.tv и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
         ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се качи онлайн от Streamer Dashboard. За секунди се появяваш в списъците на Cherry.tv. Следващите излъчвания са един клик."),
     ],
    },
    {"slug": "amateurtv", "name": "AmateurTV",
     "title": "Излъчване в AmateurTV със SplitCam — External Encoder",
     "desc": "Излъчване в AmateurTV с безплатен SplitCam — Model Panel external encoder, RTMP ключ, мулти-камера сцени и наслагвания. Без воден знак.",
     "kw": "как да излъчвате на amateurtv, amateurtv, amateurtv broadcast, amateurtv obs, amateurtv external encoder, amateurtv rtmp, amateurtv stream key",
     "h1html": 'Как да излъчваш в <span class="accent">AmateurTV</span> със SplitCam',
     "h1short": "Излъчване AmateurTV",
     "card": "Настройка с външен енкодер за испаноговорящата мрежа AmateurTV.",
     "intro": "AmateurTV е водещата испаноговоряща кам мрежа — силна аудитория в Испания, Мексико, Аржентина и из цяла Латинска Америка. Подразбиращият се broadcaster в Model Panel работи в браузъра, но излага и стандартен път през <strong>external encoder</strong>, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — така стриймваш с мулти-камера сцени, beauty filters и наслагвания към hispanofonна аудитория, която US-центрираните мрежи не обслужват добре.",
     "quick": "Излъчване в AmateurTV със SplitCam: инсталирай SplitCam, изгради сцената, в Model Panel отвори <em>Broadcast Settings → External Encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи URL и stream key от Model Panel.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "Влез в модел акаунта си в AmateurTV, отвори <strong>Model Panel → Broadcast Settings → External Encoder</strong>. Появяват се <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Новите модел акаунти минават през ID верификация преди да тръгнат на живо.",
     "tips": [
         ("Първо hispanofonна аудитория", "Трафикът на AmateurTV е преобладаващо испаноговорящ — Испания през деня, LatAm във вечерните US часове. Заглавия на стриймове, текст в сцената и наслагвания на испански бият далеч само-на-английски в тази мрежа."),
         ("LatAm часовият пояс е твоето prime time", "Пиковият трафик корелира с LatAm вечерните часове (UTC-3 до UTC-6). Ако си гъвкав, излъчване късно вечер CET / рано сутрин азиатско време хваща и пика на Испания, и този на LatAm."),
         ("Стабилни mid-tier изплащания", "Не най-високият RPM в индустрията, но стабилен — AmateurTV плаща последователно, а hispanofonнaта ниша има по-малко конкуренция от топ US мрежите."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли AmateurTV официално външни енкодери като SplitCam?", "Да — Model Panel включва опция External Encoder под Broadcast Settings. AmateurTV предоставя стандартен RTMP server URL и stream key; OBS, SplitCam, vMix и други RTMP енкодери се връзват."),
         ("Откъде вземам моя stream key за AmateurTV?", "Model Panel → Broadcast Settings → External Encoder. Server URL и stream key се появяват там. Копирай и двете в полетата за custom RTMP на SplitCam. Ключът е обвързан с акаунта."),
         ("Какъв bitrate да използвам за AmateurTV?", "Стандартни cam-quality настройки — push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо вградения speed test на SplitCam."),
         ("SplitCam безплатен ли е за AmateurTV?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията External Encoder на AmateurTV се активира безплатно."),
     ],
     "steps": [
         ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Той е енкодерът, който изпраща видеото ти към AmateurTV."),
         ("Изгради сцената", "Отвори SplitCam и добави webcam-а. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон. Използвай испански текст в наслагванията за hispanofonнaта аудитория на AmateurTV."),
         ("Вземи URL и stream key за AmateurTV", "В модел акаунта си отвори <strong>Model Panel → Broadcast Settings → External Encoder</strong>. Копирай server URL и уникалния stream key."),
         ("Свържи SplitCam с AmateurTV", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на AmateurTV и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди. Пусни първо вградения speed test."),
         ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се качи онлайн от Model Panel в AmateurTV. За ~10 секунди стриймът стига мрежата. Следващите излъчвания са един клик — отваряш SplitCam, Go Live."),
     ],
    },
    {"slug": "camster", "name": "Camster",
     "title": "Излъчване в Camster със SplitCam — External Encoder",
     "desc": "Излъчване в Camster с безплатен SplitCam — Model Hub external encoder, RTMP ключ, мулти-камера сцени и наслагвания. Без воден знак.",
     "kw": "как да излъчвате на camster, camster, camster broadcast, camster obs, camster external encoder, camster rtmp, camster stream key",
     "h1html": 'Как да излъчваш в <span class="accent">Camster</span> със SplitCam',
     "h1short": "Излъчване Camster",
     "card": "Настройка с външен енкодер за Model Hub на Camster.",
     "intro": "Camster е установена mid-tier кам платформа — по-малка от Chaturbate или LiveJasmin, но с лоялна потребителска база и коректни изплащания. Подразбиращият се broadcaster в Model Hub работи в браузъра, но излага и стандартен път през <strong>external encoder</strong>, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — така стриймваш с мулти-камера сцени, наслагвания и филтри, които вграденият broadcaster не може да достави.",
     "quick": "Излъчване в Camster със SplitCam: инсталирай SplitCam, изгради сцената, в Model Hub отвори <em>Broadcast Settings → External Encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи URL и stream key от Model Hub.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "Влез в модел акаунта си в Camster, отвори <strong>Model Hub → Broadcast Settings → External Encoder</strong>. Появяват се <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Ключът е обвързан с акаунта; третирай го като парола.",
     "tips": [
         ("Mid-tier означава по-малко конкуренция", "Camster има стабилен трафик, но по-малко broadcaster-и от топ мрежите — по-лесно е да попаднеш на първата страница с изпипана сцена и последователен график."),
         ("Browser broadcaster срещу external", "Подразбиращият се браузър broadcaster е single-source. SplitCam през External Encoder отключва мулти-камера сцени, наслагвания, beauty filters и AI фон."),
         ("Стабилни изплащания, коректни сплитове", "Сплитът на приходите на Camster е справедлив за mid-tier — не най-високият в индустрията, но надеждни месечни изплащания и малко оплаквания от модели за забавени плащания."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли Camster официално външни енкодери като SplitCam?", "Да — Model Hub включва опция External Encoder под Broadcast Settings. Стандартен RTMP server URL и stream key; OBS, SplitCam и други RTMP енкодери се връзват."),
         ("Откъде вземам моя stream key за Camster?", "Model Hub → Broadcast Settings → External Encoder. Server URL и stream key се появяват там. Копирай и двете в полетата за custom RTMP на SplitCam."),
         ("Какъв bitrate да използвам за Camster?", "Стандартни cam-quality настройки — push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо вградения speed test на SplitCam."),
         ("SplitCam безплатен ли е за Camster?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията External Encoder на Camster е безплатна."),
     ],
     "steps": [
         ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
         ("Изгради сцената", "Отвори SplitCam и добави webcam-а. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон — всичко приложено на живо."),
         ("Вземи URL и stream key за Camster", "В модел акаунта си отвори <strong>Model Hub → Broadcast Settings → External Encoder</strong>. Копирай server URL и уникалния stream key."),
         ("Свържи SplitCam с Camster", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на Camster и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди. Пусни първо вградения speed test."),
         ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се качи онлайн от Model Hub в Camster. За ~10 секунди стриймът стига до Camster."),
     ],
    },
    {"slug": "camversity", "name": "Camversity",
     "title": "Излъчване в Camversity със SplitCam — External Encoder",
     "desc": "Излъчване в Camversity с безплатен SplitCam — Performer Dashboard external encoder, RTMP ключ, мулти-камера сцени и наслагвания. Без воден знак.",
     "kw": "как да излъчвате на camversity, camversity, camversity broadcast, camversity obs, camversity external encoder, camversity rtmp, camversity stream key",
     "h1html": 'Как да излъчваш в <span class="accent">Camversity</span> със SplitCam',
     "h1short": "Излъчване Camversity",
     "card": "Настройка с външен енкодер за Performer Dashboard на Camversity.",
     "intro": "Camversity е развиваща се независима кам платформа, фокусирана върху performer-friendly инструменти и по-ниски комисионни от наследените мрежи. Подразбиращият се broadcaster в Performer Dashboard работи в браузъра, но излага и стандартен път през <strong>external encoder</strong>, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — така стриймваш с мулти-камера сцени, наслагвания и филтри.",
     "quick": "Излъчване в Camversity със SplitCam: инсталирай SplitCam, изгради сцената, в Performer Dashboard отвори <em>Stream Settings → External Encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи URL и stream key от Performer Dashboard.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "Влез в performer акаунта си в Camversity, отвори <strong>Performer Dashboard → Stream Settings → External Encoder</strong>. Появяват се <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Новите акаунти минават през стандартна ID верификация преди да тръгнат на живо.",
     "tips": [
         ("Performer-friendly сплитове", "Сплитът на приходите на Camversity е по-благоприятен за performer-и от наследените мрежи — заслужава сравнение с настоящата ти основна платформа, ако си в началото на cam кариерата си."),
         ("По-лек onboarding от Docler", "Верификацията на Camversity е по-бърза от 48–72-часовото одобрение на LiveJasmin, но остава легитимна (без случайни / неверифицирани модели). Добър middle ground."),
         ("Изгради сцена, не просто webcam", "Подразбиращият се broadcaster в Performer Dashboard на Camversity е single-source. SplitCam през External Encoder отключва мулти-камера, наслагвания, beauty filters."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли Camversity официално външни енкодери като SplitCam?", "Да — Performer Dashboard включва опция External Encoder под Stream Settings. Стандартен RTMP server URL и stream key; OBS, SplitCam, vMix се връзват."),
         ("Откъде вземам моя stream key за Camversity?", "Performer Dashboard → Stream Settings → External Encoder. Server URL и stream key се появяват там."),
         ("Какъв bitrate да използвам за Camversity?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо вградения speed test на SplitCam."),
         ("SplitCam безплатен ли е за Camversity?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията External Encoder на Camversity е безплатна."),
     ],
     "steps": [
         ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
         ("Изгради сцената", "Отвори SplitCam и добави webcam-а. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон."),
         ("Вземи URL и stream key за Camversity", "В performer акаунта си отвори <strong>Performer Dashboard → Stream Settings → External Encoder</strong>. Копирай server URL и уникалния stream key."),
         ("Свържи SplitCam с Camversity", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на Camversity и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
         ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се качи онлайн от Performer Dashboard. За ~10 секунди стриймът стига до Camversity."),
     ],
    },
    {"slug": "skyprivate", "name": "SkyPrivate",
     "title": "SkyPrivate със SplitCam — виртуална камера в Skype",
     "desc": "Използвай SkyPrivate с безплатен SplitCam като виртуална камера — частни кам обаждания през Skype, мулти-камера сцени, beauty filters. Без воден знак.",
     "kw": "как да излъчвате на skyprivate, skyprivate, skyprivate virtual camera, skyprivate виртуална камера, skype cam private, skyprivate splitcam",
     "h1html": 'Как да използваш <span class="accent">SkyPrivate</span> със SplitCam',
     "h1short": "SplitCam в SkyPrivate",
     "card": "Настройка с виртуална камера за кам обаждания през Skype в SkyPrivate.",
     "intro": "SkyPrivate е необичайна кам платформа — вместо RTMP излъчване монетизира <strong>частни кам обаждания през Skype с плащане на минута</strong>. Клиентите резервират и плащат на минута през маркетплейса на SkyPrivate, а самото видео обаждане върви през Skype. Безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва като <strong>виртуална камера</strong>: изграждаш сцената в SplitCam, после избираш SplitCam за камера в Skype, преди да приемеш обаждане, резервирано през SkyPrivate.",
     "quick": "Използвай SkyPrivate със SplitCam: инсталирай SplitCam, изгради сцената, инсталирай Skype с add-on на SkyPrivate, в <em>Video Settings</em> на Skype избери SplitCam за камера и микрофон, после приемай обажданията, резервирани през SkyPrivate — Skype доставя композираната сцена на клиента."
              "<ol><li>Инсталирай SplitCam.</li><li>Изгради сцената в SplitCam.</li>"
              "<li>Инсталирай Skype + add-on на SkyPrivate.</li><li>Избери SplitCam за камера в Skype.</li>"
              "<li>Приемай обажданията.</li></ol>",
     "key_how": "SkyPrivate не използва RTMP или stream key — използва Skype за видео транспорта с add-on за фактуриране на минута. Инсталирай Skype, инсталирай браузърния/десктоп add-on на SkyPrivate, после в Skype отвори <strong>Settings → Audio &amp; Video → Camera</strong> и избери <strong>SplitCam</strong> вместо webcam-а си. Композираната сцена в SplitCam (наслагвания, мулти-камера, beauty filters) става това, което клиентът на SkyPrivate вижда през Skype.",
     "tips": [
         ("Без RTMP — поток с виртуална камера", "Не търси server URL или stream key. SkyPrivate върви през Skype, а Skype вижда SplitCam просто като webcam устройство. Изгради сцената в SplitCam, после избери SplitCam в настройките на камерата в Skype."),
         ("Сложи SplitCam и за микрофон", "В Audio настройките на Skype избери SplitCam и за микрофон, не само за камера — така noise-suppression, миксираното аудио и intro музиката стигат до клиента."),
         ("Добави тестово обаждане в Skype", "Преди първото платено обаждане в SkyPrivate направи безплатен тестов разговор в Skype (Echo / Sound Test Service), за да потвърдиш, че SplitCam е активната камера и че сцената е композирана правилно."),
         _T_TEST,
     ],
     "faq": [
         ("Използва ли SkyPrivate RTMP или stream key?", "Нито едното. SkyPrivate се занимава с фактурирането и резервациите; самото видео върви през Skype. Не ти трябва RTMP server URL или stream key — просто конфигурирай SplitCam за камера в Skype."),
         ("Как да избера SplitCam в Skype за SkyPrivate?", "Отвори Skype Settings → Audio &amp; Video → Camera, избери SplitCam от списъка. Същото направи и за Microphone. Обажданията на SkyPrivate след това идват като нормални Skype обаждания, с твоята SplitCam сцена като камера."),
         ("Мога ли да използвам наслагвания и beauty filters със SkyPrivate?", "Да — изгради ги в сцената си в SplitCam. Skype получава само композирания резултат като един камера feed, така че всичко, което SplitCam композира (наслагвания, beauty filters, AI фон, мулти-камера сцени), е видимо за клиента на SkyPrivate."),
         ("Безплатен ли е SplitCam за SkyPrivate?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Като виртуална камера за SkyPrivate обажданията през Skype не добавя цена или branding към обаждането."),
     ],
     "steps": [
         ("Инсталирай SplitCam", "SplitCam е безплатен за Windows и macOS — без регистрация, без карта, без воден знак. За SkyPrivate действа като <strong>виртуална камера</strong>, която Skype вижда като всеки webcam."),
         ("Изгради сцената в SplitCam", "Отвори SplitCam и използвай <strong>Media Layers +</strong>, за да добавиш webcam плюс наслагвания, текст, beauty filters или AI фон. Тази композирана сцена е това, което Skype ще достави на клиента на SkyPrivate."),
         ("Инсталирай Skype и add-on на SkyPrivate", "Инсталирай Skype на същия PC, влез в акаунта си, после инсталирай add-on / десктоп приложението на SkyPrivate по onboarding-а на SkyPrivate. Add-on-ът се занимава с фактурирането на минута от страна на SkyPrivate."),
         ("Избери SplitCam за камера и микрофон в Skype", "В Skype отвори <strong>Settings → Audio &amp; Video</strong>. Сложи <strong>Camera = SplitCam</strong> и <strong>Microphone = SplitCam</strong>. Пусни бързо тестово обаждане в Skype (Echo / Sound Test Service), за да потвърдиш, че сцената изглежда и звучи правилно."),
         ("Приемай обаждания SkyPrivate", "Когато клиент в SkyPrivate резервира платено обаждане, то идва като Skype обаждане — приеми го. Той вижда твоята композирана SplitCam сцена; SkyPrivate фактурира на минута. Промени сцената по време на обаждането, като я редактираш в SplitCam — Skype обновява моментално."),
     ],
    },
    {"slug": "manyvids", "name": "ManyVids",
     "title": "На живо в MV Live (ManyVids) със SplitCam",
     "desc": "Излизай на живо в MV Live на ManyVids с безплатен SplitCam — Creator Studio external encoder, RTMP ключ, мулти-камера сцени. Без воден знак.",
     "kw": "как да излъчвате на живо в manyvids, manyvids, mv live, manyvids live, manyvids obs, manyvids external encoder, manyvids rtmp, manyvids stream key",
     "h1html": 'Как да излъчваш в <span class="accent">MV Live</span> със SplitCam',
     "h1short": "Излъчване в MV Live",
     "card": "Настройка с външен енкодер за Creator Studio MV Live на ManyVids.",
     "intro": "ManyVids е платформа от тип creator-икономика — продажби на клипове, custom видеа, абонаменти за fan club и продукта за live-стрийминг <strong>MV Live</strong>. Подразбиращият се broadcaster в Creator Studio върви в браузъра, но излага и стандартен <strong>external encoder</strong> път, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — така стриймваш с мулти-камера сцени, наслагвания и филтри на същата creator-friendly платформа.",
     "quick": "Излъчване в MV Live със SplitCam: инсталирай SplitCam, изгради сцената, в Creator Studio отвори <em>MV Live → Broadcast Settings → External Encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи URL и stream key от Creator Studio.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "Влез в creator акаунта си в ManyVids, отвори <strong>Creator Studio</strong> и иди в <strong>MV Live → Broadcast Settings → External Encoder</strong>. Страницата показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Creator акаунтите трябва да са напълно верифицирани (ID + данъци), преди MV Live да стане достъпен.",
     "tips": [
         ("Creator-икономика, не само live", "ManyVids не е чисто кам платформа — MV Live е един източник на приходи редом с продажби на клипове, custom видеа и fan club абонаменти. Използвай live стрийма, за да насочваш зрителите към другите си начини за монетизация."),
         ("Tipping с токени в MV Live", "MV Live има собствена система за tipping с токени в стаята на живо. Планирай goal менюта и reward triggers подобно на Chaturbate / Stripchat — конвертират добре със съществуващата аудитория на ManyVids."),
         ("Браузър срещу външен енкодер", "Вграденият броузър broadcaster в Creator Studio е single-камера. SplitCam през External Encoder отключва мулти-камера сцени, наслагвания и филтри."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли MV Live (ManyVids) външни енкодери като SplitCam?", "Да — MV Live секцията в Creator Studio включва опция External Encoder под Broadcast Settings. Стандартен RTMP server URL и stream key; OBS, SplitCam, vMix се връзват."),
         ("Откъде вземам моя stream key за MV Live?", "Creator Studio → MV Live → Broadcast Settings → External Encoder. И server URL, и stream key се появяват там — копирай и двете в полетата за custom RTMP на SplitCam."),
         ("Какъв bitrate да използвам за MV Live?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо вградения speed test на SplitCam."),
         ("Безплатен ли е SplitCam за MV Live?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията External Encoder на ManyVids е безплатна в Creator Studio."),
     ],
     "steps": [
         ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
         ("Изгради сцената", "Отвори SplitCam и добави webcam-а. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон — идеално за MV Live build-ове с goal-reveal и reward triggers."),
         ("Вземи URL и stream key за MV Live", "Влез в creator акаунта си в ManyVids, отвори <strong>Creator Studio</strong>, навигирай до <strong>MV Live → Broadcast Settings → External Encoder</strong>. Страницата показва <strong>server URL</strong> и уникален <strong>stream key</strong>. Копирай и двете."),
         ("Свържи SplitCam с MV Live", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на MV Live и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
         ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после стартирай излъчването в MV Live от Creator Studio. За ~10 секунди стриймът ти стига до аудиторията на MV Live."),
     ],
    },
    {"slug": "fansly", "name": "Fansly",
     "title": "На живо в Fansly със SplitCam — External Encoder",
     "desc": "Излизай на живо във Fansly с безплатен SplitCam — Creator Dashboard external encoder, RTMP ключ, мулти-камера сцени и beauty filters. Без воден знак.",
     "kw": "как да излъчвате на живо във fansly, fansly, fansly live, fansly broadcast, fansly obs, fansly external encoder, fansly rtmp, fansly stream key",
     "h1html": 'Как да излъчваш в <span class="accent">Fansly Live</span> със SplitCam',
     "h1short": "Излъчване в Fansly",
     "card": "Настройка с външен енкодер за Creator Dashboard на Fansly.",
     "intro": "Fansly е директен конкурент на OnlyFans с по-разхлабени правила за съдържание и растяща база от creator-и — абонаменти, pay-per-view съдържание и продукта за live-стрийминг <strong>Fansly Live</strong>. Подразбиращият се broadcaster работи в браузъра, но <strong>Creator Dashboard</strong> излага и стандартен <strong>external encoder</strong> път, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — така стриймваш с мулти-камера сцени, наслагвания и филтри към базата си от абонати.",
     "quick": "Излъчване в Fansly Live със SplitCam: инсталирай SplitCam, изгради сцената, в Creator Dashboard отвори <em>Live → Broadcast Settings → External Encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
              "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
              "<li>Вземи URL и stream key от Creator Dashboard.</li><li>Постави в SplitCam.</li>"
              "<li>Натисни Go Live.</li></ol>",
     "key_how": "Влез в creator акаунта си във Fansly, отвори <strong>Creator Dashboard</strong> и навигирай до <strong>Live → Broadcast Settings → External Encoder</strong>. Страницата показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Creator акаунтите имат нужда от ID верификация, преди Fansly Live да бъде активиран.",
     "tips": [
         ("Аудитория от тип subscriber-first", "Аудиторията на Fansly е базирана на абонамент — твоят live стрийм стига до хора, които вече ти плащат месечно. Планирай съдържание, което възнаграждава лоялността (ексклузивно Q&amp;A, behind-the-scenes, custom tip goals), вместо да гониш метрики от публични стаи."),
         ("Tip-ове редом с абонаменти", "Fansly Live поддържа tipping в стрийма в допълнение към базовите абонаменти. Комбинираните приходи могат да надминат tipping-а на чистите кам платформи за утвърдените creator-и."),
         ("Браузър broadcaster vs външен", "Подразбиращият се браузър broadcaster е single-source. SplitCam през External Encoder отключва мулти-камера, наслагвания, beauty filters и AI фон, които пасват на полирания вид на премиум съдържание за абонати."),
         _T_ETH,
     ],
     "faq": [
         ("Поддържа ли Fansly Live външни енкодери като SplitCam?", "Да — Live секцията в Creator Dashboard включва опция External Encoder под Broadcast Settings. Стандартен RTMP server URL и stream key; OBS, SplitCam, vMix се връзват."),
         ("Откъде вземам моя stream key за Fansly?", "Creator Dashboard → Live → Broadcast Settings → External Encoder. И server URL, и stream key се появяват там. Копирай и двете в полетата за custom RTMP на SplitCam."),
         ("Какъв bitrate да използвам за Fansly Live?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо вградения speed test на SplitCam."),
         ("Безплатен ли е SplitCam за Fansly?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията External Encoder на Fansly е безплатна в Creator Dashboard."),
     ],
     "steps": [
         ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
         ("Изгради сцената", "Отвори SplitCam и добави webcam-а. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон — полирани сцени, които пасват на премиум очакванията на платящите абонати."),
         ("Вземи URL и stream key за Fansly", "Влез в creator акаунта си във Fansly, отвори <strong>Creator Dashboard</strong>, навигирай до <strong>Live → Broadcast Settings → External Encoder</strong>. Страницата показва <strong>server URL</strong> и уникален <strong>stream key</strong>. Копирай и двете."),
         ("Свържи SplitCam с Fansly", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на Fansly и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
         ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после стартирай излъчването на Fansly Live от Creator Dashboard. За ~10 секунди стриймът ти стига до абонатите във Fansly."),
     ],
    },
    {
        "slug": "ifriends", "name": "iFriends",
        "title": "Излъчване в iFriends със SplitCam — External Encoder",
        "desc": "Излъчване в iFriends с безплатен SplitCam — external encoder на Model Center, RTMP ключ, мулти-камера сцени и наслагвания. Без воден знак.",
        "kw": "как да излъчвате на ifriends, ifriends, ifriends broadcast, ifriends obs, ifriends external encoder, ifriends rtmp, ifriends stream key",
        "h1html": 'Как да излъчваш в <span class="accent">iFriends</span> със SplitCam',
        "h1short": "Излъчване iFriends",
        "card": "Настройка с external encoder за зрелия Model Center на iFriends.",
        "intro": "iFriends (WebPower) е една от най-дълголетните независими кам мрежи — тихо печеливша, с лоялна потребителска база и зрял Model Center, изграден още преди браузърните broadcaster-и да станат масови. Платформата поддържа стандартен път през <strong>external encoder</strong> от Model Center, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — така стриймваш със съвременни мулти-камера сцени, наслагвания и филтри в тази утвърдена мрежа.",
        "quick": "Излъчвай в iFriends със SplitCam: инсталирай SplitCam, изгради сцената, в Model Center отвори <em>Broadcast Settings → External Encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Вземи URL и stream key от Model Center.</li><li>Постави в SplitCam.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Влез в моделския си акаунт в iFriends, отвори <strong>Model Center</strong> и навигирай до <strong>Broadcast Settings → External Encoder</strong>. Страницата показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Одобрението на нови моделски акаунти в iFriends е стриктно, но коректно; веднъж верифициран, опцията external encoder остава достъпна за неограничено време.",
        "tips": [
            ("Зряла мрежа с дългосрочна публика", "iFriends работи още от края на 90-те с лоялна потребителска база — много от зрителите са дългогодишни абонати, а не случайни посетители. Стабилен доход за утвърдените модели, по-бавен старт за новодошлите."),
            ("Браузър broadcaster vs външен", "Старият broadcaster на iFriends е създаден преди модерния мулти-камера интерфейс. Преминаването към SplitCam през External Encoder е осезаемо подобрение — мулти-камера сцени, наслагвания и beauty filters, които старият инструмент не може да достави."),
            ("Редовни плащания, без изненади", "Компанията-майка (WebPower) плаща на моделите надеждно от десетилетия — графиците за изплащане са по-бавни от тези на новите крипто платформи, но почти няма негативни истории."),
            _T_ETH,
        ],
        "faq": [
            ("Поддържа ли iFriends официално външни енкодери като SplitCam?", "Да — Model Center включва опция External Encoder под Broadcast Settings. Стандартен RTMP server URL и stream key; OBS, SplitCam, vMix се връзват веднага щом акаунтът ти бъде одобрен."),
            ("Откъде вземам моя stream key за iFriends?", "Model Center → Broadcast Settings → External Encoder. И server URL, и stream key се появяват там. Копирай и двете в полетата за custom RTMP на SplitCam."),
            ("Какъв bitrate да използвам за iFriends?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо вградения speed test на SplitCam."),
            ("Безплатен ли е SplitCam за iFriends?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията external encoder на iFriends е безплатна в Model Center."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави webcam-а. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон — полираните модерни сцени се открояват в тази зряла мрежа."),
            ("Вземи URL и stream key за iFriends", "Влез в моделския си акаунт в iFriends, отвори <strong>Model Center</strong>, навигирай до <strong>Broadcast Settings → External Encoder</strong>. Страницата показва <strong>server URL</strong> и уникален <strong>stream key</strong>. Копирай и двете."),
            ("Свържи SplitCam с iFriends", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на iFriends и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от Model Center на iFriends. За ~10 секунди стриймът ти стига до мрежата."),
        ],
    },
    {
        "slug": "babestation", "name": "Babestation",
        "title": "Излъчване в Babestation със SplitCam — External Encoder",
        "desc": "Излъчване в Babestation с безплатен SplitCam — external encoder на Performer Hub, RTMP ключ, мулти-камера сцени и наслагвания. Без воден знак.",
        "kw": "как да излъчвате на babestation, babestation, babestation broadcast, babestation obs, babestation external encoder, babestation rtmp, babestation stream key",
        "h1html": 'Как да излъчваш в <span class="accent">Babestation</span> със SplitCam',
        "h1short": "Излъчване Babestation",
        "card": "Настройка с external encoder за UK Performer Hub на Babestation.",
        "intro": "Babestation е водещата UK adult TV / кам мрежа — хибрид между телевизионни канали и live кам продукт, захранван от изпълнители, влезли в Performer Hub. Платформата поддържа стандартен път през <strong>external encoder</strong> от Performer Hub, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — така независимите UK изпълнители стриймват с мулти-камера сцени, наслагвания и beauty filters, които надхвърлят базовия broadcaster в стил телевизионно студио на Babestation.",
        "quick": "Излъчвай в Babestation със SplitCam: инсталирай SplitCam, изгради сцената, в Performer Hub отвори <em>Broadcast Settings → External Encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Вземи URL и stream key от Performer Hub.</li><li>Постави в SplitCam.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Влез в изпълнителския си акаунт в Babestation, отвори <strong>Performer Hub</strong> и навигирай до <strong>Broadcast Settings → External Encoder</strong>. Страницата показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Регистрацията на UK изпълнители в Babestation включва проверка на самоличността съгласно британските изисквания за верификация на възрастта.",
        "tips": [
            ("UK публика и подходящ час", "Основният трафик на Babestation е в UK вечерните / нощните часове (GMT/BST). Ако си в друга часова зона, излъчването в късните британски часове превъзхожда значително местния прайм тайм в тази мрежа."),
            ("Очаква се студиен вид", "Брандът на Babestation е свързан с телевизионните ѝ канали — зрителите очакват по-продуцирани декори и осветление, отколкото при типичен webcam стрийм. Сцените в SplitCam (наслагвания, брандиран текст, AI фон) помагат да съответстваш на полирания вид на платформата."),
            ("Независими vs студийни изпълнители", "Babestation работи както с UK студия, така и с независими изпълнители. Независимите broadcaster-и, които се връзват през External Encoder, получават същия модел на изплащане като захранваните от студио камери."),
            _T_ETH,
        ],
        "faq": [
            ("Поддържа ли Babestation външни енкодери като SplitCam?", "Да — Performer Hub включва опция External Encoder под Broadcast Settings. Стандартен RTMP server URL и stream key; OBS, SplitCam, vMix се връзват след като верификацията на изпълнителя приключи."),
            ("Откъде вземам моя stream key за Babestation?", "Performer Hub → Broadcast Settings → External Encoder. И server URL, и stream key се появяват там. Копирай и двете в полетата за custom RTMP на SplitCam."),
            ("Какъв bitrate да използвам за Babestation?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. UK upload скоростите обикновено са добри, но пусни първо speed test на SplitCam."),
            ("Безплатен ли е SplitCam за Babestation?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията external encoder на Babestation е безплатна в Performer Hub."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави webcam-а. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон — съответствай на студийния продукционен вид на Babestation, за да се откроиш."),
            ("Вземи URL и stream key за Babestation", "Влез в изпълнителския си акаунт в Babestation, отвори <strong>Performer Hub</strong>, навигирай до <strong>Broadcast Settings → External Encoder</strong>. Страницата показва <strong>server URL</strong> и уникален <strong>stream key</strong>. Копирай и двете."),
            ("Свържи SplitCam с Babestation", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на Babestation и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от Performer Hub. За ~10 секунди стриймът ти стига до UK публиката на Babestation."),
        ],
    },
    {
        "slug": "adultwork", "name": "AdultWork",
        "title": "Излъчване в AdultWork със SplitCam — External Encoder",
        "desc": "Излъчване в AdultWork с безплатен SplitCam — external encoder на Members Area, RTMP ключ, мулти-камера сцени и наслагвания. Без воден знак.",
        "kw": "как да излъчвате на adultwork, adultwork, adultwork broadcast, adultwork obs, adultwork external encoder, adultwork rtmp, adultwork stream key",
        "h1html": 'Как да излъчваш в <span class="accent">AdultWork</span> със SplitCam',
        "h1short": "Излъчване AdultWork",
        "card": "Настройка с external encoder за кам функцията в UK Members Area на AdultWork.",
        "intro": "AdultWork е утвърденият UK маркетплейс за adult услуги — познат преди всичко с резервации на ескорт услуги, продажба на снимки / видео и телефонни услуги, с допълнителна live <strong>webcam функция</strong>. Платформата поддържа стандартен път през <strong>external encoder</strong> от Members Area, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — така независимите UK изпълнители добавят приходи от live кам с мулти-камера сцени, наслагвания и филтри.",
        "quick": "Излъчвай в AdultWork със SplitCam: инсталирай SplitCam, изгради сцената, в Members Area отвори <em>Members → Broadcasting → External Encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Вземи URL и stream key от Members Area.</li><li>Постави в SplitCam.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Влез в изпълнителския си акаунт в AdultWork, отвори <strong>Members Area</strong> и навигирай до <strong>Members → Broadcasting → External Encoder</strong>. Страницата показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Верификацията в AdultWork е задължителна за live кам функцията и покрива съответствието с британските изисквания за проверка на възрастта.",
        "tips": [
            ("Кръстосани продажби от другите услуги в AdultWork", "Силата на AdultWork е в съществуващата клиентска база — зрителите вероятно вече резервират снимки / видео / телефонни услуги от теб. Използвай live кам стриймовете, за да предлагаш кам на клиенти, които още не са го пробвали, вместо да гониш непознати."),
            ("Members Area е входната точка", "Не търси broadcaster-а в публичната част на сайта — всичко за изпълнителите е вътре в Members Area. Настройките за излъчване, изплащанията и управлението на съдържание са там."),
            ("UK-центрирана, но международни изплащания", "По-голямата част от трафика е UK/EU. Изплащанията работят международно чрез стандартен банков превод / е-портфейл, като седмичните графици са обичайни в платформата."),
            _T_ETH,
        ],
        "faq": [
            ("Поддържа ли AdultWork външни енкодери като SplitCam?", "Да — Members Area включва опция External Encoder под Broadcasting. Стандартен RTMP server URL и stream key; OBS, SplitCam, vMix се връзват след верификация на изпълнителя."),
            ("Откъде вземам моя stream key за AdultWork?", "Members Area → Members → Broadcasting → External Encoder. И server URL, и stream key се появяват там. Копирай и двете в полетата за custom RTMP на SplitCam."),
            ("Какъв bitrate да използвам за AdultWork?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо вградения speed test на SplitCam."),
            ("Безплатен ли е SplitCam за AdultWork?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията external encoder на AdultWork е безплатна в Members Area."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави webcam-а. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон — използвай наслагванията, за да рекламираш съдържанието / телефонните си услуги в AdultWork и да правиш кръстосани продажби по време на live-а."),
            ("Вземи URL и stream key за AdultWork", "Влез в изпълнителския си акаунт в AdultWork, отвори <strong>Members Area</strong>, навигирай до <strong>Members → Broadcasting → External Encoder</strong>. Страницата показва <strong>server URL</strong> и уникален <strong>stream key</strong>. Копирай и двете."),
            ("Свържи SplitCam с AdultWork", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на AdultWork и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от Members Area. За ~10 секунди стриймът ти стига до публиката на AdultWork."),
        ],
    },
    {
        "slug": "jerkmate", "name": "Jerkmate",
        "title": "Излъчване в Jerkmate със SplitCam — SM Connect",
        "desc": "Излъчване в Jerkmate с безплатен SplitCam — през Streamate мрежата и SM Connect, вграден канал, мулти-камера сцени. Без воден знак.",
        "kw": "как да излъчвате на jerkmate, jerkmate, jerkmate broadcast, jerkmate obs, jerkmate sm connect, jerkmate streamate, jerkmate stream key",
        "h1html": 'Как да излъчваш в <span class="accent">Jerkmate</span> със SplitCam',
        "h1short": "Излъчване Jerkmate",
        "card": "Jerkmate тегли моделите си от Streamate мрежата — стриймваш през SM Connect + SplitCam.",
        "intro": "Jerkmate е сред най-търсените кам брандове, познат с AI сватовника си, който свързва зрителите с модели на живо. Платформата няма собствен broadcaster — Jerkmate <strong>взема моделите си на живо от Streamate мрежата</strong>. Излъчваш като модел от Streamate мрежата, а шоуто ти се разпространява към Jerkmate и партньорските сайтове. Тъй като Streamate е <strong style='color:var(--text)'>предварително конфигуриран в списъка с канали на SplitCam</strong>, безплатният <strong style='color:var(--text)'>SplitCam</strong> ти позволява да добавиш мулти-камера сцени, наслагвания и филтри без ръчно RTMP въвеждане.",
        "quick": "Излъчване в Jerkmate със SplitCam: инсталирай SplitCam, изгради сцената, регистрирай се като модел в Streamate мрежата, която захранва Jerkmate, отвори <em>SM Connect → Start Show</em> и копирай ключа, после в SplitCam отвори <em>Stream Settings → Add Channel → Streamate</em>, постави и Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Регистрирай се като модел в Streamate мрежата.</li>"
                 "<li>Вземи ключа чрез SM Connect.</li>"
                 "<li>Add Channel → Streamate, Go Live.</li></ol>",
        "key_how": "Кам стриймовете на живо в Jerkmate идват от <strong>broadcasting мрежата Streamate</strong> — няма отделен \"Jerkmate encoder\". Регистрирай се през модел програмата на Jerkmate или директно в Streamate мрежата, отвори <strong>SM Connect</strong>, приеми условията, кликни <strong>Start Show</strong> и копирай streaming ключа. В SplitCam отвори <strong>Stream Settings → Add Channel</strong>, избери <strong>Streamate</strong> от вградения списък и постави ключа. Стриймът ти тогава стига едновременно до Jerkmate и партньорските сайтове на мрежата.",
        "tips": [
            ("Отдолу е Streamate мрежата", "Не търси broadcaster само за Jerkmate — излъчваш в Streamate, а Jerkmate го преразпространява. Всичко, което работи за Streamate (SM Connect, вграденият канал в SplitCam), работи и за Jerkmate."),
            ("Превърни AI-съвпадащия трафик", "Сватовникът на Jerkmate насочва зрителите към модели, които пасват на избора им — полирана SplitCam сцена с наслагвания и добро кадриране превръща тези съвпаднати зрители далеч по-добре от плоска уебкамера."),
            ("Един поток, много сайтове", "Излъчването в Streamate мрежата те поставя едновременно в Jerkmate и партньорските сайтове — по-широк обхват от един SplitCam стрийм, без допълнителна настройка."),
            _T_ETH,
        ],
        "faq": [
            ("Jerkmate има ли собствен broadcaster или stream key?", "Не — Jerkmate взема моделите си на живо от Streamate мрежата. Излъчваш като модел от Streamate мрежата чрез SM Connect, а шоуто ти се появява в Jerkmate автоматично."),
            ("Как получавам своя stream key за Jerkmate?", "През SM Connect от страната на модела в Streamate мрежата: приеми условията → Start Show → копирай ключа. Постави го във вградения Streamate канал на SplitCam — без ръчен RTMP URL."),
            ("Какъв битрейт за Jerkmate?", "Фиксирай 1080p при 30 fps. Потокът на мрежата е адаптивен, така че по-нисък битрейт при статичен кадър е нормален. Пусни теста за скорост на SplitCam и използвай кабелна връзка."),
            ("SplitCam безплатен ли е за Jerkmate?", "Да — SplitCam е безплатен, без воден знак и без времево ограничение. Streamate (който захранва Jerkmate) е вграден канал в SplitCam, така че няма отделен разход за енкодер."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон — силна сцена превръща съвпаднатите зрители на Jerkmate."),
            ("Регистрирай се като модел и вземи ключа", "Регистрирай се през модел програмата на Jerkmate или директно в <strong>Streamate мрежата</strong>, която го захранва. Отвори <strong>SM Connect</strong>, приеми условията, кликни <strong>Start Show</strong> и копирай streaming ключа."),
            ("Добави Streamate като канал в SplitCam", "Отвори <strong>Stream Settings → Add Channel</strong>, избери <strong>Streamate</strong> от вградения списък и постави ключа — без ръчен RTMP URL. Фиксирай резолюцията на 1080p."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam — зелен слайдер потвърждава връзката. Шоуто ти излиза през Streamate мрежата и се появява в Jerkmate."),
        ],
    },
    {
        "slug": "justforfans", "name": "JustForFans",
        "title": "На живо в JustForFans със SplitCam — виртуална камера",
        "desc": "Излизай на живо в JustForFans с безплатен SplitCam — виртуална камера или external encoder, мулти-камера сцени, наслагвания и филтри. Без воден знак.",
        "kw": "как да излъчвате на живо в justforfans, justforfans, justforfans live, justforfans virtual camera, justforfans виртуална камера, justforfans obs, justforfans broadcast",
        "h1html": 'Как да си на живо в <span class="accent">JustForFans</span> със SplitCam',
        "h1short": "Live JustForFans",
        "card": "Използвай SplitCam като виртуална камера в live broadcaster-а на JustForFans.",
        "intro": "JustForFans (JFF) е абонаментна платформа, притежавана от creator-и — дългогодишна алтернатива на OnlyFans, основана от изпълнители, с абонаменти, pay-per-view съдържание и live функция в браузъра. Нейният broadcaster показва само една плоска уебкамера; ако го насочиш към безплатния <strong style='color:var(--text)'>SplitCam</strong> като <strong>виртуална камера</strong>, отключваш мулти-камера сцени, наслагвания и филтри. Ако твоят creator dashboard излага и опция за external encoder / stream key, SplitCam се връзва вместо това през RTMP.",
        "quick": "Излизане на живо в JustForFans със SplitCam: инсталирай SplitCam, изгради сцената, започни live излъчване в JFF, и в селектора за камера на broadcaster-а избери <em>SplitCam</em> като своя уебкамера — после излез на живо."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Започни live излъчване в JFF.</li>"
                 "<li>Избери SplitCam от падащото меню за камера.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Live функцията на JustForFans върви в браузъра. Изгради сцената в SplitCam — той се регистрира като системна уебкамера с име <strong>\"SplitCam Video Driver\"</strong> — после отвори JFF live broadcaster-а и в падащото меню за камера избери <strong>SplitCam</strong> вместо суровата си уебкамера. Съставената ти сцена замества плоската камера. Ако creator dashboard-ът на JFF предлага опция за <strong>external encoder / stream key</strong>, постави този ключ в полетата за custom RTMP на SplitCam вместо това.",
        "tips": [
            ("Виртуалната камера работи навсякъде", "Дори когато live функцията на платформата е само в браузъра, SplitCam се появява като избираема уебкамера — така мулти-камера сцената, наслагванията и филтрите ти работят в JFF изобщо без stream key."),
            ("Притежавана от creator-и, приятелска към изпълнителите", "JFF се управлява от изпълнители и пази лоялна абонатска база. Наслагвания, които кръстосано продават твоето PPV или абонамент, се превръщат добре пред публика, която вече плаща."),
            ("Дай на браузъра достъп до камерата", "Ако SplitCam не се появява в списъка с камери на JFF, увери се, че SplitCam върви първо и че браузърът има разрешение за камера — после презареди broadcaster-а."),
            _T_TEST,
        ],
        "faq": [
            ("Как SplitCam се връзва с JustForFans?", "Live функцията на JFF е в браузъра, така че SplitCam се връзва като виртуална камера: избираш SplitCam в селектора за камера на JFF broadcaster-а. Не е нужен stream key."),
            ("Мога ли да използвам наслагвания и няколко камери в JFF?", "Да — изгради сцената в SplitCam (втора камера, наслагвания, beauty или AI-фон филтри), а JFF вижда готовата сцена като една уебкамера."),
            ("Поддържа ли JustForFans OBS или външни енкодери?", "Live функцията на JFF е предимно базирана на браузър/уебкамера. Ако твоят creator dashboard показва опция за external encoder или stream key, постави я в полетата за custom RTMP на SplitCam; иначе използвай метода с виртуална камера."),
            ("SplitCam безплатен ли е за JustForFans?", "Да — SplitCam е безплатен, без воден знак и без времево ограничение."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Инсталира виртуална камера, която браузърът може да избере."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон — прилагани на живо."),
            ("Започни live излъчване в JFF", "Влез в creator акаунта си в JustForFans и отвори live broadcaster-а, за да започнеш стрийм за абонатите си."),
            ("Избери SplitCam като своя камера", "В падащото меню за камера на JFF broadcaster-а избери <strong>SplitCam</strong> вместо суровата си уебкамера — съставената ти сцена замества плоската камера. (Или, ако е налична, постави external encoder ключа на JFF в полетата за custom RTMP на SplitCam.)"),
            ("Натисни Go Live", "Стартирай излъчването — твоята SplitCam сцена, наслагвания и филтри стигат до абонатите ти в JustForFans."),
        ],
    },
    {
        "slug": "fanvue", "name": "Fanvue",
        "title": "На живо в Fanvue със SplitCam — виртуална камера",
        "desc": "Излизай на живо в Fanvue с безплатен SplitCam като виртуална камера — мулти-камера сцени, наслагвания и филтри за абонатите ти. Без воден знак.",
        "kw": "как да си на живо в fanvue, fanvue live, fanvue stream, fanvue obs, fanvue виртуална камера, fanvue creator, fanvue broadcast",
        "h1html": 'Как да си на живо в <span class="accent">Fanvue</span> със SplitCam',
        "h1short": "Live Fanvue",
        "card": "Използвай SplitCam като виртуална камера за live в Fanvue.",
        "intro": "Fanvue е бързо растяща британска абонаментна платформа за creator-и — алтернатива на OnlyFans, известна с това, че е приятелска към creator-ите и към AI, с абонаменти, pay-per-view и live стрийминг. Нейният live broadcaster върви в браузъра, така че ако го насочиш към безплатния <strong style='color:var(--text)'>SplitCam</strong> като <strong>виртуална камера</strong>, отключваш мулти-камера сцени, наслагвания и филтри. Ако твоят creator dashboard излага опция за external encoder / stream key, SplitCam се връзва вместо това през RTMP.",
        "quick": "Излизане на живо в Fanvue със SplitCam: инсталирай SplitCam, изгради сцената, започни live в Fanvue, и в селектора за камера на broadcaster-а избери <em>SplitCam</em> — после излез на живо."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Започни live в Fanvue.</li>"
                 "<li>Избери SplitCam от падащото меню за камера.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Live функцията на Fanvue върви в браузъра. Изгради сцената в SplitCam — той се регистрира като уебкамера с име <strong>\"SplitCam Video Driver\"</strong> — после отвори live broadcaster-а на Fanvue и в падащото меню за камера избери <strong>SplitCam</strong> вместо суровата си уебкамера. Ако твоят creator dashboard предлага опция за <strong>external encoder / stream key</strong>, постави този ключ в полетата за custom RTMP на SplitCam вместо това.",
        "tips": [
            ("Виртуалната камера работи навсякъде", "Дори когато live функцията на платформата е само в браузъра, SplitCam се появява като избираема уебкамера — мулти-камера сцени, наслагвания и филтри работят във Fanvue изобщо без stream key."),
            ("Приятелска към creator-и и към AI", "Fanvue посреща AI creator-и и изплаща чисто. Наслагвания, които кръстосано продават твоя абонамент или PPV, се превръщат добре пред публика, която вече плаща."),
            ("Дай на браузъра достъп до камерата", "Ако SplitCam не се появи в списъка с камери на Fanvue, увери се, че SplitCam върви първо и че браузърът има разрешение за камера — после презареди."),
            _T_TEST,
        ],
        "faq": [
            ("Как SplitCam се връзва с Fanvue?", "Live функцията на Fanvue е в браузъра, така че SplitCam се връзва като виртуална камера: избираш SplitCam в селектора за камера. Не е нужен stream key."),
            ("Мога ли да използвам наслагвания и няколко камери във Fanvue?", "Да — изгради сцената в SplitCam (втора камера, наслагвания, beauty или AI-фон филтри), а Fanvue вижда готовата сцена като една уебкамера."),
            ("Поддържа ли Fanvue OBS или външни енкодери?", "Live функцията на Fanvue е предимно базирана на браузър/уебкамера. Ако твоят dashboard показва опция за external encoder или stream key, постави я в полетата за custom RTMP на SplitCam; иначе използвай метода с виртуална камера."),
            ("SplitCam безплатен ли е за Fanvue?", "Да — SplitCam е безплатен, без воден знак и без времево ограничение."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Инсталира виртуална камера, която браузърът може да избере."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон — прилагани на живо."),
            ("Започни live в Fanvue", "Влез в creator акаунта си във Fanvue и отвори live broadcaster-а, за да започнеш стрийм за абонатите си."),
            ("Избери SplitCam като своя камера", "В падащото меню за камера на Fanvue избери <strong>SplitCam</strong> вместо суровата си уебкамера — съставената ти сцена замества плоската камера. (Или, ако е налична, постави stream key в полетата за custom RTMP на SplitCam.)"),
            ("Натисни Go Live", "Стартирай излъчването — твоята SplitCam сцена, наслагвания и филтри стигат до абонатите ти във Fanvue."),
        ],
    },
    {
        "slug": "loyalfans", "name": "LoyalFans",
        "title": "На живо в LoyalFans със SplitCam — виртуална камера",
        "desc": "Излизай на живо в LoyalFans с безплатен SplitCam като виртуална камера — сцени, наслагвания и филтри за абонати и tip-ъри. Без воден знак.",
        "kw": "как да си на живо в loyalfans, loyalfans live, loyalfans stream, loyalfans obs, loyalfans виртуална камера, loyalfans broadcast, loyal fans",
        "h1html": 'Как да си на живо в <span class="accent">LoyalFans</span> със SplitCam',
        "h1short": "Live LoyalFans",
        "card": "Използвай SplitCam като виртуална камера за live в LoyalFans.",
        "intro": "LoyalFans е абонаментна платформа за creator-и с абонаменти, pay-per-view, tipping и вградена <strong>live cam</strong> функция. Live broadcaster-ът върви в браузъра, така че свързването на безплатния <strong style='color:var(--text)'>SplitCam</strong> като <strong>виртуална камера</strong> добавя мулти-камера сцени, наслагвания и филтри върху стандартната уебкамера. Ако твоят dashboard излага опция за external encoder / stream key, SplitCam се връзва вместо това през RTMP.",
        "quick": "Излизане на живо в LoyalFans със SplitCam: инсталирай SplitCam, изгради сцената, започни live в LoyalFans, и в селектора за камера на broadcaster-а избери <em>SplitCam</em> — после излез на живо."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Започни live в LoyalFans.</li>"
                 "<li>Избери SplitCam от падащото меню за камера.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Live функцията на LoyalFans върви в браузъра. Изгради сцената в SplitCam — той се регистрира като уебкамера с име <strong>\"SplitCam Video Driver\"</strong> — после отвори live broadcaster-а на LoyalFans и в падащото меню за камера избери <strong>SplitCam</strong>. Ако в твоя creator dashboard се появи опция за <strong>stream key / external encoder</strong>, постави я в полетата за custom RTMP на SplitCam вместо това.",
        "tips": [
            ("Виртуална камера, без нужда от ключ", "Базираният на браузър live пак получава пълната ти SplitCam сцена — наслагвания, втора камера и филтри — само като избереш SplitCam за уебкамера."),
            ("Tip-овете възнаграждават продукцията", "LoyalFans разчита на tipping; екранни наслагвания с tip-цели и полирана сцена тласкат tip-ърите повече от плоска уебкамера."),
            ("Дай на браузъра достъп до камерата", "Ако SplitCam не е в списъка с камери на LoyalFans, пусни първо SplitCam, разреши достъп до камера в браузъра, после презареди broadcaster-а."),
            _T_TEST,
        ],
        "faq": [
            ("Как SplitCam се връзва с LoyalFans?", "Live функцията на LoyalFans е в браузъра, така че SplitCam се връзва като виртуална камера — избираш SplitCam в селектора за камера. Не е нужен stream key."),
            ("Мога ли да използвам наслагвания и няколко камери в LoyalFans?", "Да — съчини сцената в SplitCam (втора камера, наслагвания, beauty или AI-фон филтри); LoyalFans я вижда като една уебкамера."),
            ("Поддържа ли LoyalFans OBS или външни енкодери?", "Live функцията е предимно базирана на браузър/уебкамера. Ако твоят dashboard показва опция за stream key, постави я в полетата за custom RTMP на SplitCam; иначе използвай метода с виртуална камера."),
            ("SplitCam безплатен ли е за LoyalFans?", "Да — безплатен, без воден знак и без времево ограничение."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Инсталира виртуална камера, която браузърът може да избере."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст с tip-цели, втора камера или телефона, beauty filters или AI фон."),
            ("Започни live в LoyalFans", "Влез в акаунта си в LoyalFans и отвори live broadcaster-а, за да излезеш на живо за абонатите си."),
            ("Избери SplitCam като своя камера", "В падащото меню за камера на LoyalFans избери <strong>SplitCam</strong> вместо суровата си уебкамера — сцената ти замества плоската камера. (Или, ако е налична, постави stream key в полетата за custom RTMP на SplitCam.)"),
            ("Натисни Go Live", "Стартирай излъчването — твоята SplitCam сцена стига до публиката ти в LoyalFans."),
        ],
    },
    {
        "slug": "fancentro", "name": "FanCentro",
        "title": "На живо в FanCentro със SplitCam — виртуална камера",
        "desc": "Излизай на живо във FanCentro с безплатен SplitCam като виртуална камера — сцени, наслагвания и филтри за абонатите ти. Без воден знак.",
        "kw": "как да си на живо в fancentro, fancentro live, fancentro stream, fancentro obs, fancentro виртуална камера, fancentro broadcast, fan centro",
        "h1html": 'Как да си на живо в <span class="accent">FanCentro</span> със SplitCam',
        "h1short": "Live FanCentro",
        "card": "Използвай SplitCam като виртуална камера за live в FanCentro.",
        "intro": "FanCentro е дългогодишна платформа за монетизация на creator-и — абонаменти, pay-per-view съобщения, съдържание и live стрийминг. Нейният live върви в браузъра, така че свързването на безплатния <strong style='color:var(--text)'>SplitCam</strong> като <strong>виртуална камера</strong> добавя мулти-камера сцени, наслагвания и филтри отвъд обикновената уебкамера. Ако твоят dashboard излага опция за external encoder / stream key, SplitCam се връзва вместо това през RTMP.",
        "quick": "Излизане на живо във FanCentro със SplitCam: инсталирай SplitCam, изгради сцената, започни live във FanCentro, и в селектора за камера на broadcaster-а избери <em>SplitCam</em> — после излез на живо."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Започни live във FanCentro.</li>"
                 "<li>Избери SplitCam от падащото меню за камера.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Live функцията на FanCentro върви в браузъра. Изгради сцената в SplitCam — той се регистрира като уебкамера с име <strong>\"SplitCam Video Driver\"</strong> — после отвори live broadcaster-а на FanCentro и в падащото меню за камера избери <strong>SplitCam</strong>. Ако се предлага опция за <strong>stream key / external encoder</strong>, постави я в полетата за custom RTMP на SplitCam вместо това.",
        "tips": [
            ("Виртуалната камера работи навсякъде", "Само-браузърен live пак получава пълната ти SplitCam сцена — наслагвания, втора камера и филтри — като избереш SplitCam за уебкамера."),
            ("Кръстосвай продажбите във фунията си", "FanCentro е изграден около creator фунии и PPV. Наслагвания, рекламиращи твоя абонамент или платени съобщения, превръщат live зрителите в купувачи."),
            ("Дай на браузъра достъп до камерата", "Ако SplitCam не е в списъка, пусни първо SplitCam, разреши достъп до камера в браузъра, после презареди broadcaster-а."),
            _T_TEST,
        ],
        "faq": [
            ("Как SplitCam се връзва с FanCentro?", "Live функцията на FanCentro е в браузъра, така че SplitCam се връзва като виртуална камера — избираш SplitCam в селектора за камера. Не е нужен stream key."),
            ("Мога ли да използвам наслагвания и няколко камери във FanCentro?", "Да — изгради сцената в SplitCam; FanCentro вижда готовата сцена като една уебкамера."),
            ("Поддържа ли FanCentro OBS или външни енкодери?", "Live функцията е предимно базирана на браузър/уебкамера. Ако в твоя dashboard се появи опция за stream key, постави я в полетата за custom RTMP на SplitCam; иначе използвай метода с виртуална камера."),
            ("SplitCam безплатен ли е за FanCentro?", "Да — безплатен, без воден знак и без времево ограничение."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Инсталира виртуална камера, която браузърът може да избере."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон."),
            ("Започни live във FanCentro", "Влез в акаунта си във FanCentro и отвори live broadcaster-а, за да излезеш на живо за абонатите си."),
            ("Избери SplitCam като своя камера", "В падащото меню за камера на FanCentro избери <strong>SplitCam</strong> вместо суровата си уебкамера. (Или, ако е наличен, постави stream key в полетата за custom RTMP на SplitCam.)"),
            ("Натисни Go Live", "Стартирай излъчването — твоята SplitCam сцена стига до абонатите ти във FanCentro."),
        ],
    },
    {
        "slug": "ismygirl", "name": "IsMyGirl",
        "title": "На живо в IsMyGirl със SplitCam — виртуална камера",
        "desc": "Излизай на живо в IsMyGirl с безплатен SplitCam като виртуална камера — сцени, наслагвания и филтри за абонатите ти. Без воден знак.",
        "kw": "как да си на живо в ismygirl, ismygirl live, ismygirl stream, ismygirl obs, ismygirl виртуална камера, ismygirl broadcast, is my girl",
        "h1html": 'Как да си на живо в <span class="accent">IsMyGirl</span> със SplitCam',
        "h1short": "Live IsMyGirl",
        "card": "Използвай SplitCam като виртуална камера за live в IsMyGirl.",
        "intro": "IsMyGirl е абонаментна платформа за creator-и — алтернатива на OnlyFans с абонаменти, платено съдържание и live стрийминг, известна с активната си подкрепа за creator-и. Live broadcaster-ът върви в браузъра, така че свързването на безплатния <strong style='color:var(--text)'>SplitCam</strong> като <strong>виртуална камера</strong> носи мулти-камера сцени, наслагвания и филтри. Ако твоят dashboard излага опция за external encoder / stream key, SplitCam се връзва вместо това през RTMP.",
        "quick": "Излизане на живо в IsMyGirl със SplitCam: инсталирай SplitCam, изгради сцената, започни live в IsMyGirl, и в селектора за камера на broadcaster-а избери <em>SplitCam</em> — после излез на живо."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Започни live в IsMyGirl.</li>"
                 "<li>Избери SplitCam от падащото меню за камера.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Live функцията на IsMyGirl върви в браузъра. Изгради сцената в SplitCam — той се регистрира като уебкамера с име <strong>\"SplitCam Video Driver\"</strong> — после отвори live broadcaster-а на IsMyGirl и в падащото меню за камера избери <strong>SplitCam</strong>. Ако се появи опция за <strong>stream key / external encoder</strong>, постави я в полетата за custom RTMP на SplitCam вместо това.",
        "tips": [
            ("Виртуална камера, без нужда от ключ", "Само-браузърен live пак получава пълната ти SplitCam сцена — наслагвания, втора камера и филтри — като избереш SplitCam за уебкамера."),
            ("Възползвай се от подкрепата за creator-и", "IsMyGirl рекламира силна подкрепа и промоция за creator-и. Полирана SplitCam сцена плюс наслагвания за кръстосана продажба извличат максимума от трафика, който ти насочват."),
            ("Дай на браузъра достъп до камерата", "Ако SplitCam не е в списъка, пусни първо SplitCam, разреши достъп до камера, после презареди broadcaster-а."),
            _T_TEST,
        ],
        "faq": [
            ("Как SplitCam се връзва с IsMyGirl?", "Live функцията на IsMyGirl е в браузъра, така че SplitCam се връзва като виртуална камера — избираш SplitCam в селектора за камера. Не е нужен stream key."),
            ("Мога ли да използвам наслагвания и няколко камери в IsMyGirl?", "Да — съчини сцената в SplitCam; IsMyGirl я вижда като една уебкамера."),
            ("Поддържа ли IsMyGirl OBS или външни енкодери?", "Live функцията е предимно базирана на браузър/уебкамера. Ако се появи опция за stream key, постави я в полетата за custom RTMP на SplitCam; иначе използвай метода с виртуална камера."),
            ("SplitCam безплатен ли е за IsMyGirl?", "Да — безплатен, без воден знак и без времево ограничение."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Инсталира виртуална камера, която браузърът може да избере."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон."),
            ("Започни live в IsMyGirl", "Влез в акаунта си в IsMyGirl и отвори live broadcaster-а, за да излезеш на живо за абонатите си."),
            ("Избери SplitCam като своя камера", "В падащото меню за камера на IsMyGirl избери <strong>SplitCam</strong> вместо суровата си уебкамера. (Или, ако е наличен, постави stream key в полетата за custom RTMP на SplitCam.)"),
            ("Натисни Go Live", "Стартирай излъчването — твоята SplitCam сцена стига до абонатите ти в IsMyGirl."),
        ],
    },
    {
        "slug": "dxlive", "name": "DXLive",
        "title": "Излъчване в DXLive със SplitCam — External Encoder",
        "desc": "Излъчване в DXLive с безплатен SplitCam — external encoder за японската премиум кам мрежа, мулти-камера сцени и наслагвания. Без воден знак.",
        "kw": "как да излъчвате на dxlive, dxlive broadcast, dxlive cam, dxlive obs, dxlive external encoder, dxlive rtmp, dxlive performer",
        "h1html": 'Как да излъчваш в <span class="accent">DXLive</span> със SplitCam',
        "h1short": "Излъчване DXLive",
        "card": "Настройка с external encoder за премиум кам мрежата на DXLive.",
        "intro": "DXLive е утвърдена премиум уебкам мрежа, популярна в Япония и из цяла Азия, изградена върху модел на плащане на минута с лоялна публика. Изпълнителската секция поддържа стандартен път през <strong>external encoder</strong>, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — за да излъчваш с мулти-камера сцени, наслагвания и beauty filters вместо с една плоска уебкамера.",
        "quick": "Излъчвай в DXLive със SplitCam: инсталирай SplitCam, изгради сцената, в изпълнителската секция отвори настройките за <em>external encoder / broadcast</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Вземи URL + stream key от изпълнителската секция.</li><li>Постави в SplitCam.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Влез в изпълнителския си акаунт в DXLive и отвори настройките за <strong>broadcast / external encoder</strong> в изпълнителската секция. Страницата показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Верификацията в DXLive е задължителна, преди да се активира live кам функцията.",
        "tips": [
            ("Създадена за азиатския пазар", "Публиката на DXLive клони към Япония/Азия и плаща на минута. Насрочи шоутата си за вечерите по JST и лоялната, плащаща база се превръща добре."),
            ("Полировката бие суровата уебкамера", "Чиста SplitCam сцена с наслагвания и beauty filters изпъква в премиум мрежа с плащане на минута, където зрителите очакват качество."),
            ("Използвай external encoder-а, не само уебкамерата", "Минаването през RTMP на SplitCam, а не през базовата браузърна камера, е това, което отключва мулти-камера сцени и филтри."),
            _T_ETH,
        ],
        "faq": [
            ("Поддържа ли DXLive външни енкодери като SplitCam?", "Да — изпълнителската секция излага стандартен external-encoder / RTMP път. Копирай server URL и stream key в SplitCam след верификация."),
            ("Откъде вземам моя stream key за DXLive?", "В настройките за broadcast / external encoder в изпълнителската секция — и server URL, и stream key се появяват там. Постави и двете в полетата за custom RTMP на SplitCam."),
            ("Какъв bitrate да използвам за DXLive?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо вградения speed test на SplitCam."),
            ("Безплатен ли е SplitCam за DXLive?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията external encoder на DXLive е безплатна в изпълнителската секция."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон."),
            ("Вземи URL и stream key за DXLive", "Влез в изпълнителския си акаунт в DXLive и отвори настройките за <strong>broadcast / external encoder</strong>. Копирай <strong>server URL</strong> и <strong>stream key</strong>."),
            ("Свържи SplitCam с DXLive", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на DXLive и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от изпълнителската секция. За ~10 секунди стриймът ти стига до публиката на DXLive."),
        ],
    },
    {
        "slug": "streamen", "name": "Streamen",
        "title": "Излъчване в Streamen със SplitCam — External Encoder",
        "desc": "Излъчване в Streamen с безплатен SplitCam — external encoder, мулти-камера сцени, наслагвания и beauty filters. Без воден знак.",
        "kw": "как да излъчвате на streamen, streamen broadcast, streamen cam, streamen obs, streamen external encoder, streamen rtmp, streamen.tv",
        "h1html": 'Как да излъчваш в <span class="accent">Streamen</span> със SplitCam',
        "h1short": "Излъчване Streamen",
        "card": "Настройка с external encoder за кам платформата Streamen.",
        "intro": "Streamen е live кам платформа, където моделите излъчват към публика, движена от tip-ове. Нейните broadcast настройки излагат стандартен път през <strong>external encoder</strong>, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва — така стриймваш с мулти-камера сцени, наслагвания и филтри вместо с една обикновена уебкамера.",
        "quick": "Излъчвай в Streamen със SplitCam: инсталирай SplitCam, изгради сцената, в модел dashboard-а отвори <em>broadcast settings → external encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Вземи URL + stream key от dashboard-а.</li><li>Постави в SplitCam.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Влез в модел акаунта си в Streamen и отвори секцията <strong>broadcast settings / external encoder</strong>. Тя показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Верификацията на модела е задължителна, преди да се активира излъчването.",
        "tips": [
            ("Публика, движена от tip-ове", "Зрителите на Streamen дават tip-ове — екранни tip-цели и полирана сцена тласкат повече tip-ове от плоска уебкамера."),
            ("External encoder-ът отключва сцените", "Минаването през RTMP на SplitCam вместо през базовата браузърна камера е това, което позволява мулти-камера разположения, наслагвания и филтри."),
            ("Заключи резолюцията", "Настрой 1080p ръчно, за да не сваля потокът качество тихо; bitrate, който пада при статичен кадър, е нормален при адаптивни потоци."),
            _T_ETH,
        ],
        "faq": [
            ("Поддържа ли Streamen външни енкодери като SplitCam?", "Да — broadcast настройките излагат стандартен external-encoder / RTMP път. Копирай server URL и stream key в SplitCam след верификация."),
            ("Откъде вземам моя stream key за Streamen?", "В broadcast / external encoder настройките на модел dashboard-а — и server URL, и stream key се появяват там. Постави и двете в полетата за custom RTMP на SplitCam."),
            ("Какъв bitrate да използвам за Streamen?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо speed test на SplitCam."),
            ("Безплатен ли е SplitCam за Streamen?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията external encoder на Streamen е безплатна в dashboard-а."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст с tip-цели, втора камера или телефона, beauty filters или AI фон."),
            ("Вземи URL и stream key за Streamen", "Влез в модел акаунта си в Streamen, отвори <strong>broadcast settings → external encoder</strong> и копирай <strong>server URL</strong> и <strong>stream key</strong>."),
            ("Свържи SplitCam със Streamen", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на Streamen и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от dashboard-а. За ~10 секунди стриймът ти стига до публиката на Streamen."),
        ],
    },
    {
        "slug": "xcams", "name": "XCams",
        "title": "Излъчване в XCams със SplitCam — External Encoder",
        "desc": "Излъчване в XCams с безплатен SplitCam — external encoder за европейската кам общност, сцени, наслагвания и филтри. Без воден знак.",
        "kw": "как да излъчвате на xcams, xcams broadcast, xcams cam, xcams obs, xcams external encoder, xcams rtmp, x cams",
        "h1html": 'Как да излъчваш в <span class="accent">XCams</span> със SplitCam',
        "h1short": "Излъчване XCams",
        "card": "Настройка с external encoder за европейската общност на XCams.",
        "intro": "XCams е европейска live кам общност — силна в Италия, Франция и Испания — изградена около live шоута и икономика на tip-ове и частни шоута. Модел секцията поддържа стандартен път през <strong>external encoder</strong>, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва, така че можеш да излъчваш с мулти-камера сцени, наслагвания и beauty filters.",
        "quick": "Излъчвай в XCams със SplitCam: инсталирай SplitCam, изгради сцената, в модел секцията отвори <em>broadcast / external encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Вземи URL + stream key от модел секцията.</li><li>Постави в SplitCam.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Влез в модел акаунта си в XCams и отвори настройките за <strong>broadcast / external encoder</strong> в модел секцията. Страницата показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Верификацията в XCams е задължителна, преди да излъчваш.",
        "tips": [
            ("Европейски prime time", "Трафикът на XCams пикира във вечерите по EU (CET). Излъчването в тези часове значително надминава извън-пиковото в тази общност."),
            ("Частните шоута възнаграждават качеството", "XCams върви на частни/spy шоута — полирана SplitCam сцена с наслагвания превръща разглеждащите в платени частни шоута."),
            ("External encoder-ът отключва сцените", "Минаването през RTMP на SplitCam вместо през браузърната камера позволява мулти-камера разположения, наслагвания и филтри."),
            _T_ETH,
        ],
        "faq": [
            ("Поддържа ли XCams външни енкодери като SplitCam?", "Да — модел секцията излага стандартен external-encoder / RTMP път. Копирай server URL и stream key в SplitCam след верификация."),
            ("Откъде вземам моя stream key за XCams?", "В broadcast / external encoder настройките на модел секцията — и server URL, и stream key се появяват там. Постави и двете в полетата за custom RTMP на SplitCam."),
            ("Какъв bitrate да използвам за XCams?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо speed test на SplitCam."),
            ("Безплатен ли е SplitCam за XCams?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията external encoder на XCams е безплатна в модел секцията."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон."),
            ("Вземи URL и stream key за XCams", "Влез в модел акаунта си в XCams, отвори <strong>broadcast / external encoder</strong> и копирай <strong>server URL</strong> и <strong>stream key</strong>."),
            ("Свържи SplitCam с XCams", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на XCams и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от модел секцията. За ~10 секунди стриймът ти стига до публиката на XCams."),
        ],
    },
    {
        "slug": "camcontacts", "name": "CamContacts",
        "title": "Излъчване в CamContacts със SplitCam — External Encoder",
        "desc": "Излъчване в CamContacts с безплатен SplitCam — external encoder за pay-per-minute кам сайта, сцени и наслагвания. Без воден знак.",
        "kw": "как да излъчвате на camcontacts, camcontacts broadcast, camcontacts cam, camcontacts obs, camcontacts external encoder, camcontacts rtmp, cam contacts",
        "h1html": 'Как да излъчваш в <span class="accent">CamContacts</span> със SplitCam',
        "h1short": "Излъчване CamContacts",
        "card": "Настройка с external encoder за pay-per-minute кам функцията на CamContacts.",
        "intro": "CamContacts е сред най-дълго съществуващите независими кам сайтове — модел с плащане на минута, със зряла, лоялна публика и репутация за стабилни изплащания. Изпълнителската секция поддържа стандартен път през <strong>external encoder</strong>, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва, така че можеш да излъчваш с мулти-камера сцени, наслагвания и beauty filters.",
        "quick": "Излъчвай в CamContacts със SplitCam: инсталирай SplitCam, изгради сцената, в изпълнителската секция отвори настройките за <em>external encoder / broadcast</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Вземи URL + stream key от изпълнителската секция.</li><li>Постави в SplitCam.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Влез в изпълнителския си акаунт в CamContacts и отвори настройките за <strong>broadcast / external encoder</strong> в изпълнителската секция. Страницата показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Верификацията в CamContacts е задължителна за live кам функцията.",
        "tips": [
            ("Зряла, лоялна публика", "CamContacts работи от десетилетия с дългосрочни членове — по-стабилни, по-плащащи редовни клиенти от сайт с висок churn и безплатен достъп, но по-бавен растеж за новодошлите."),
            ("Плащането на минута възнаграждава задържането", "Дръж зрителите в платено време с полирана сцена и наслагвания; продукционната стойност удължава сесиите при модел с плащане на минута."),
            ("External encoder-ът отключва сцените", "Минаването през RTMP на SplitCam, а не през базовата камера, позволява мулти-камера разположения, наслагвания и филтри."),
            _T_ETH,
        ],
        "faq": [
            ("Поддържа ли CamContacts външни енкодери като SplitCam?", "Да — изпълнителската секция излага стандартен external-encoder / RTMP път. Копирай server URL и stream key в SplitCam след верификация."),
            ("Откъде вземам моя stream key за CamContacts?", "В broadcast / external encoder настройките на изпълнителската секция — и server URL, и stream key се появяват там. Постави и двете в полетата за custom RTMP на SplitCam."),
            ("Какъв bitrate да използвам за CamContacts?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо speed test на SplitCam."),
            ("Безплатен ли е SplitCam за CamContacts?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията external encoder на CamContacts е безплатна в изпълнителската секция."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон."),
            ("Вземи URL и stream key за CamContacts", "Влез в изпълнителския си акаунт в CamContacts, отвори настройките за <strong>broadcast / external encoder</strong> и копирай <strong>server URL</strong> и <strong>stream key</strong>."),
            ("Свържи SplitCam с CamContacts", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на CamContacts и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от изпълнителската секция. За ~10 секунди стриймът ти стига до публиката на CamContacts."),
        ],
    },
    {
        "slug": "royalcams", "name": "RoyalCams",
        "title": "Излъчване в RoyalCams със SplitCam — External Encoder",
        "desc": "Излъчване в RoyalCams с безплатен SplitCam — external encoder за token-базирания кам сайт, сцени, наслагвания и филтри. Без воден знак.",
        "kw": "как да излъчвате на royalcams, royalcams broadcast, royalcams cam, royalcams obs, royalcams external encoder, royalcams rtmp, royal cams",
        "h1html": 'Как да излъчваш в <span class="accent">RoyalCams</span> със SplitCam',
        "h1short": "Излъчване RoyalCams",
        "card": "Настройка с external encoder за token кам сайта RoyalCams.",
        "intro": "RoyalCams е token-базиран безплатен кам сайт — отворени публични стаи, захранвани от tip-ове, с частни шоута отгоре. Broadcast настройките поддържат стандартен път през <strong>external encoder</strong>, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва, така че можеш да стриймваш с мулти-камера сцени, наслагвания и beauty filters вместо с една плоска уебкамера.",
        "quick": "Излъчвай в RoyalCams със SplitCam: инсталирай SplitCam, изгради сцената, в модел dashboard-а отвори <em>broadcast settings → external encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Вземи URL + stream key от dashboard-а.</li><li>Постави в SplitCam.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Влез в модел акаунта си в RoyalCams и отвори секцията <strong>broadcast settings / external encoder</strong>. Тя показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Верификацията на модела е задължителна, преди да излъчваш.",
        "tips": [
            ("Token стаите възнаграждават продукцията", "Публичните стаи на RoyalCams вървят на tip-ове — наслагвания с tip-цели и полирана сцена превръщат наблюдаващите в tip-ъри и частни шоута."),
            ("Превръщай в частни шоута", "Използвай силна публична сцена, за да тласкаш частни шоута, където са истинските печалби в token кам сайтовете."),
            ("External encoder-ът отключва сцените", "Минаването през RTMP на SplitCam, а не през браузърната камера, позволява мулти-камера разположения, наслагвания и филтри."),
            _T_ETH,
        ],
        "faq": [
            ("Поддържа ли RoyalCams външни енкодери като SplitCam?", "Да — broadcast настройките излагат стандартен external-encoder / RTMP път. Копирай server URL и stream key в SplitCam след верификация."),
            ("Откъде вземам моя stream key за RoyalCams?", "В broadcast / external encoder настройките на модел dashboard-а — и server URL, и stream key се появяват там. Постави и двете в полетата за custom RTMP на SplitCam."),
            ("Какъв bitrate да използвам за RoyalCams?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо speed test на SplitCam."),
            ("Безплатен ли е SplitCam за RoyalCams?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията external encoder на RoyalCams е безплатна в dashboard-а."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст с tip-цели, втора камера или телефона, beauty filters или AI фон."),
            ("Вземи URL и stream key за RoyalCams", "Влез в модел акаунта си в RoyalCams, отвори <strong>broadcast settings → external encoder</strong> и копирай <strong>server URL</strong> и <strong>stream key</strong>."),
            ("Свържи SplitCam с RoyalCams", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на RoyalCams и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от dashboard-а. За ~10 секунди стриймът ти стига до публиката на RoyalCams."),
        ],
    },
    {
        "slug": "modelhub", "name": "Modelhub",
        "title": "Излъчване в Modelhub със SplitCam — External Encoder",
        "desc": "Излъчване в Modelhub Live с безплатен SplitCam — external encoder за creator платформата на Pornhub, сцени, наслагвания и филтри. Без воден знак.",
        "kw": "как да излъчвате на modelhub, modelhub live, modelhub broadcast, modelhub obs, modelhub external encoder, modelhub rtmp, modelhub cam",
        "h1html": 'Как да излъчваш в <span class="accent">Modelhub</span> със SplitCam',
        "h1short": "Излъчване Modelhub",
        "card": "Настройка с external encoder за Modelhub Live (Pornhub).",
        "intro": "Modelhub е creator платформата на Pornhub — продажба на видеа, фен абонаменти и <strong>live cam</strong> продукт с огромен трафик в горната част на фунията от мрежата на Pornhub. Модел dashboard-ът поддържа стандартен път през <strong>external encoder</strong>, към който безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва, така че можеш да излъчваш с мулти-камера сцени, наслагвания и beauty filters.",
        "quick": "Излъчвай в Modelhub със SplitCam: инсталирай SplitCam, изгради сцената, в модел dashboard-а отвори <em>Live → broadcast / external encoder</em>, копирай server URL и stream key, постави в SplitCam, Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li>"
                 "<li>Вземи URL + stream key от dashboard-а.</li><li>Постави в SplitCam.</li>"
                 "<li>Натисни Go Live.</li></ol>",
        "key_how": "Влез в модел акаунта си в Modelhub и отвори настройките за <strong>Live / broadcast / external encoder</strong> в dashboard-а. Страницата показва <strong>server URL</strong> и <strong>stream key</strong>, обвързани с акаунта — копирай и двете в полетата за custom RTMP на SplitCam. Верификацията на модела с мрежата е задължителна, преди да излезеш на живо.",
        "tips": [
            ("Огромен трафик в горната част на фунията", "Modelhub привлича зрители от мрежата на Pornhub — полирана SplitCam сцена превръща тази голяма, случайна публика в плащащи live зрители и абонати."),
            ("Кръстосвай продажбата на видеата си", "Използвай наслагвания, за да насочваш live зрителите към видеата и абонамента ти в Modelhub — платформата е създадена за тази фуния."),
            ("External encoder-ът отключва сцените", "Минаването през RTMP на SplitCam, а не през базовата камера, позволява мулти-камера разположения, наслагвания и филтри."),
            _T_ETH,
        ],
        "faq": [
            ("Поддържа ли Modelhub външни енкодери като SplitCam?", "Да — модел dashboard-ът излага стандартен external-encoder / RTMP път за Modelhub Live. Копирай server URL и stream key в SplitCam след верификация."),
            ("Откъде вземам моя stream key за Modelhub?", "В Live / broadcast / external encoder настройките на dashboard-а — и server URL, и stream key се появяват там. Постави и двете в полетата за custom RTMP на SplitCam."),
            ("Какъв bitrate да използвам за Modelhub?", "Push 1920×1080 при 30 fps, 3 500–6 000 Kbps с 2-секунден keyframe. Пусни първо speed test на SplitCam."),
            ("Безплатен ли е SplitCam за Modelhub?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето. Опцията external encoder на Modelhub е безплатна в dashboard-а."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст, втора камера или телефона, beauty filters или AI фон."),
            ("Вземи URL и stream key за Modelhub", "Влез в модел акаунта си в Modelhub, отвори <strong>Live → broadcast / external encoder</strong> и копирай <strong>server URL</strong> и <strong>stream key</strong>."),
            ("Свържи SplitCam с Modelhub", "В SplitCam отвори <strong>Stream Settings</strong>, постави server URL на Modelhub и stream key в полетата за custom RTMP. Bitrate 3 500–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от dashboard-а. За ~10 секунди стриймът ти стига до публиката на Modelhub."),
        ],
    },
    {
        "slug": "xhamsterlive", "name": "xHamsterLive",
        "title": "Излъчване в xHamsterLive със SplitCam (RTMP/OBS)",
        "desc": "Излъчване в xHamsterLive с безплатен SplitCam през RTMP — мулти-камера сцени, наслагвания и филтри. Mainstream трафикът на xHamster. Без воден знак.",
        "kw": "как да излъчвате на xhamsterlive, xhamsterlive obs, xhamsterlive rtmp, xhamsterlive broadcast, xhamsterlive модел, xhamster live cam, xhamsterlive studio, xhamsterlive stream key",
        "h1html": 'Как да излъчваш в <span class="accent">xHamsterLive</span> със SplitCam',
        "h1short": "Излъчване xHamsterLive",
        "card": "Безплатен SplitCam → RTMP/OBS стрийм към xHamsterLive.",
        "intro": "xHamsterLive е live-cam секцията на xHamster — същата broadcaster технология като в Stripchat, но захранвана от mainstream трафика на xHamster, една от най-големите зрителски бази в индустрията. Моделите излъчват през xHamsterLive <strong>Studio</strong>, която поддържа както браузърния broadcaster, така и <strong>external encoder през RTMP</strong>. С безплатния <strong style='color:var(--text)'>SplitCam</strong> стриймваш като external encoder за пълни мулти-камера сцени, наслагвания и филтри — или, ако излъчваш от браузъра, насочваш xHamsterLive към SplitCam като <strong>виртуална камера</strong> със същия ефект.",
        "quick": "Излъчвай в xHamsterLive със SplitCam: инсталирай SplitCam, изгради сцената, копирай server URL + stream key от xHamsterLive Studio, постави в RTMP настройките на SplitCam, натисни Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li><li>Копирай URL + stream key от xHamsterLive Studio → External Encoder.</li><li>Постави в custom RTMP на SplitCam.</li><li>Натисни Go Live.</li></ol>",
        "key_how": "Studio на xHamsterLive показва на broadcaster-ите таб <strong>external encoder</strong> със server URL и stream key. Постави и двете в <strong>Stream Settings → Custom RTMP</strong> на SplitCam; избери 4 000–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди. Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от Studio. Ако предпочиташ браузърния broadcaster, отвори го и избери <strong>SplitCam</strong> от падащото меню за камера — твоята композирана сцена замества суровата уебкамера.",
        "tips": [
            ("Трафик от xHamster, енджин на Stripchat", "Същият broadcaster инструментариум като Stripchat (Studio панел, tip меню, Lovense), но с mainstream фуния на xHamster — друг профил на зрителя влиза в стаята ти."),
            ("Използвай external encoder, ако можеш", "RTMP от SplitCam дава стабилен bitrate и пълни мулти-камера сцени с наслагвания; браузърният broadcaster върши работа, но ограничава композирането."),
            ("Tip менютата конвертират mainstream зрители", "Много посетители на xHamster са нови за кам индустрията — чисто tip меню на екрана и goal bar задават очакванията и вдигат конверсията за сесия."),
            _T_TEST,
        ],
        "faq": [
            ("xHamsterLive същото нещо ли е като Stripchat?", "Върви на broadcaster енджина на Stripchat, но марката и източникът на трафик са различни — xHamster насочва тук mainstream публиката си, така че профилът на зрителя се различава от чист Stripchat акаунт."),
            ("Откъде вземам моя stream key за xHamsterLive?", "В xHamsterLive Studio отвори панела <em>Broadcast</em> или <em>External Encoder</em> — ще видиш server URL и stream key. Постави и двете в полетата за custom RTMP на SplitCam."),
            ("Браузърен broadcaster или RTMP?", "External encoder (RTMP) се предпочита от сериозните модели — стабилен bitrate и пълни SplitCam сцени. Браузърният broadcaster също работи: избери SplitCam като уебкамера."),
            ("Безплатен ли е SplitCam за xHamsterLive?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, tip меню, втора камера или телефона, beauty filters или AI фон — всичко на живо."),
            ("Вземи URL + ключ за xHamsterLive Studio", "Влез в xHamsterLive, отвори Studio, премини на <strong>External Encoder</strong> и копирай <strong>server URL</strong> и <strong>stream key</strong>."),
            ("Свържи SplitCam с xHamsterLive", "В SplitCam → <strong>Stream Settings → Custom RTMP</strong>, постави URL и ключа. Настрой 4 000–6 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от xHamsterLive Studio. За ~10 секунди стриймът ти стига до публичния списък."),
        ],
    },
    {
        "slug": "premium-chat", "name": "Premium.Chat",
        "title": "SplitCam за Premium.Chat — платени видео разговори",
        "desc": "Използвай безплатен SplitCam като виртуална камера в Premium.Chat — платени pay-per-minute видео разговори, сцени, наслагвания и филтри. Без воден знак.",
        "kw": "как да използвате splitcam в premium chat, premium chat видео разговор, premium chat виртуална камера, premium.chat pay per minute, premium chat модел, premium chat live, видео разговори платформа splitcam, premium chat advisor",
        "h1html": 'Как да използваш SplitCam в <span class="accent">Premium.Chat</span>',
        "h1short": "Premium.Chat със SplitCam",
        "card": "Използвай SplitCam като виртуална камера за платени разговори в Premium.Chat.",
        "intro": "Premium.Chat е платена pay-per-minute платформа: задаваш ставка на минута за чат, глас или <strong>видео разговори</strong>, споделяш личния си линк и клиентите плащат, за да говорят с теб. Разговорите вървят в браузъра, което значи, че безплатният <strong style='color:var(--text)'>SplitCam</strong> се включва директно като <strong>виртуална камера</strong> — мулти-камера сцени, наслагвания, светлинни филтри и AI фон стигат до клиента, без да се променя как работи Premium.Chat.",
        "quick": "Използвай SplitCam в Premium.Chat: инсталирай SplitCam, изгради чиста сцена за видео разговори, приеми входящ Premium.Chat разговор и в селектора за камера на разговора избери <em>SplitCam</em>."
                 "<ol><li>Инсталирай SplitCam.</li><li>Настрой сцената (добра светлина, евентуално наслагване).</li><li>Задай ставка на минута в Premium.Chat.</li><li>Приеми входящия видео разговор.</li><li>Избери SplitCam като камера.</li></ol>",
        "key_how": "Разговорите в Premium.Chat се случват в браузъра. SplitCam инсталира виртуална уебкамера с име <strong>\"SplitCam Video Driver\"</strong> — когато започне разговор, кликни менюто с икона на камера в прозореца на Premium.Chat разговора и превключи от вградената уебкамера на <strong>SplitCam</strong>. Композираната ти сцена (реална камера + наслагвания + филтри) става това, което вижда обаждащият се.",
        "tips": [
            ("Premium.Chat е на минута, не стрийминг", "За разлика от tip стаите тип chaturbate, тук ти плащат на минута. Мека светлина, чист звук и AI фон изглеждат по-скоро като премиум консултация, отколкото като публична камера."),
            ("Промотирай линка си, не профил", "Premium.Chat ти дава личен линк, който можеш да пуснеш в социалните, в bio на OnlyFans или в Linktree — така клиентите те намират."),
            ("Наслагвания само ако са полезни", "За разговори 1-на-1 тежките наслагвания разсейват. Използвай SplitCam за качество на камерата, светлина и фон — дръж екрана предимно върху теб."),
            _T_TEST,
        ],
        "faq": [
            ("Как SplitCam се връзва с Premium.Chat?", "Като виртуална камера. Разговорите в Premium.Chat вървят в браузъра; избираш SplitCam в селектора за камера на разговора — без stream key, без RTMP."),
            ("Поддържа ли Premium.Chat OBS?", "Premium.Chat е базиран на браузър, така че OBS се включва по същия начин като SplitCam — през виртуална камера. SplitCam е по-леката, безплатна опция без воден знак."),
            ("Мога ли да използвам втора камера или наслагване в Premium.Chat?", "Да — съчини сцената в SplitCam (втора камера, наслагвания, филтри) и Premium.Chat вижда една уебкамера. Използвай умерено при разговори 1-на-1."),
            ("Безплатен ли е SplitCam?", "Да — безплатен, без воден знак и без лимит на времето."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Инсталира виртуална камера, която браузърът може да използва."),
            ("Настрой сцената за разговори", "Отвори SplitCam, добави уебкамерата, нагласи светлината, опционално добави AI фон или фино наслагване. Дръж кадрирането чисто — това е платен разговор, не сцена."),
            ("Задай ставката си в Premium.Chat", "Влез в Premium.Chat, задай ставка на минута за видео разговори и копирай личния си линк. Сподели го в социалните или в bio."),
            ("Приеми входящия видео разговор", "Когато клиент плати за време, заявката за разговор пристига. Приеми я в dashboard-а на Premium.Chat."),
            ("Избери SplitCam като камера", "В менюто с икона на камера в прозореца на разговора превключи от вградената уебкамера на <strong>SplitCam</strong>. Композираната ти сцена вече стига до обаждащия се."),
        ],
    },
    {
        "slug": "arousr", "name": "Arousr",
        "title": "SplitCam за Arousr — секстинг и видео чат",
        "desc": "Използвай безплатен SplitCam като виртуална камера в Arousr видео чатове — сцени, наслагвания и филтри за платен секстинг, глас и видео. Без воден знак.",
        "kw": "как да използвате splitcam в arousr, arousr видео чат, arousr виртуална камера, arousr cam girl, arousr модел, секстинг платформа splitcam, arousr live, arousr broadcast",
        "h1html": 'Как да използваш SplitCam в <span class="accent">Arousr</span>',
        "h1short": "Arousr със SplitCam",
        "card": "Използвай SplitCam като виртуална камера за видео чат в Arousr.",
        "intro": "Arousr е платена платформа за <strong>секстинг + глас + видео чат</strong> — клиентите купуват кредити, за да пишат, говорят или да правят видео чат с моделите, и ти плащат за сесия. Видео страната върви в браузъра (или в мобилното приложение на Arousr на телефон), което значи, че безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва като <strong>виртуална камера</strong> на десктоп: мулти-камера сцени, наслагвания, светлинни филтри и AI фон отиват директно до клиента.",
        "quick": "Използвай SplitCam в Arousr: инсталирай SplitCam, настрой сцената, приеми входяща Arousr видео заявка и в селектора за камера избери <em>SplitCam</em>."
                 "<ol><li>Инсталирай SplitCam.</li><li>Настрой сцена + светлина.</li><li>Задай ставки за секстинг/видео в Arousr.</li><li>Приеми входящата видео заявка.</li><li>Избери SplitCam в падащото меню за камера.</li></ol>",
        "key_how": "Уеб видеото на Arousr върви в браузъра. SplitCam инсталира виртуална уебкамера с име <strong>\"SplitCam Video Driver\"</strong> — когато започне видео сесия в dashboard-а на Arousr, превключи камерата в прозореца на сесията на <strong>SplitCam</strong>. Композираната сцена (камера + наслагвания + филтри) става това, което вижда клиентът. В мобилното приложение на Arousr виртуалните камери не са налични — там използвай реалната камера на телефона и запази SplitCam за десктоп сесии.",
        "tips": [
            ("Сесиите се плащат на време", "Клиентите купуват кредити на минута (или на съобщение за текст). Полирано видео — добра светлина, AI фон, beauty filter — се отплаща в по-дълги сесии."),
            ("Първо секстинг, после видео upsell", "Повечето приходи в Arousr са от текст. Кратко видео преглед по време на секст чат прехвърля клиента към пълна видео сесия — там влиза ставката на минута."),
            ("Мобилни сесии ≠ десктоп", "Виртуалните камери работят в браузърно видео на десктоп. Мобилното приложение на Arousr използва камерата на телефона директно — същият workflow, различен инструмент."),
            _T_TEST,
        ],
        "faq": [
            ("Как SplitCam се връзва с Arousr?", "Като виртуална камера. Arousr видео чатът върви в браузъра на десктоп — избираш SplitCam в селектора за камера. Не е нужен stream key."),
            ("Поддържа ли Arousr OBS?", "Arousr е базиран на браузър, така че OBS се включва по същия начин като SplitCam — през виртуална камера. SplitCam е безплатната опция без воден знак."),
            ("Мога ли да използвам наслагвания на секстинг + видео сесия?", "Да — съчини сцената в SplitCam (светлина, наслагване, втора камера) и Arousr вижда една уебкамера. Дръж наслагванията дискретни при 1-на-1."),
            ("Безплатен ли е SplitCam за Arousr?", "Да — безплатен, без воден знак и без лимит на времето."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Инсталира виртуална камера, която браузърът може да избере."),
            ("Изгради сцената", "Отвори SplitCam, добави уебкамерата, нагласи светлината, добави опционално AI фон или beauty filter. Дръж го интимно — това е платена 1-на-1 сесия, не публична сцена."),
            ("Задай ставките си в Arousr", "Влез в Arousr, задай ставка на съобщение и на минута видео и се увери, че профилът ти е одобрен, за да могат да идват заявки."),
            ("Приеми входящата видео заявка", "Когато клиент инициира видео сесия от секстинг или директно, приеми я в dashboard-а на Arousr."),
            ("Избери SplitCam като камера", "В падащото меню за камера в прозореца на сесията превключи от вградената уебкамера на <strong>SplitCam</strong>. Композираната ти сцена вече стига до клиента."),
        ],
    },
    {
        "slug": "cams-com", "name": "Cams.com",
        "title": "Излъчване в Cams.com със SplitCam (RTMP/OBS)",
        "desc": "Излъчване в Cams.com с безплатен SplitCam през RTMP — мулти-камера сцени, наслагвания и филтри. Достъп до плащащата база на AFF. Без воден знак.",
        "kw": "как да излъчвате на cams.com, cams.com obs, cams.com rtmp, cams.com модел, cams.com broadcaster, cams.com stream key, adult friend finder cams, cams.com live, cams com model signup",
        "h1html": 'Как да излъчваш в <span class="accent">Cams.com</span> със SplitCam',
        "h1short": "Излъчване Cams.com",
        "card": "Безплатен SplitCam → RTMP стрийм към мрежата Cams.com / AFF.",
        "intro": "Cams.com е кам секцията на мрежата AdultFriendFinder — една от най-старите dating + кам екосистеми онлайн, със значителна база <strong>вече плащащи членове</strong>, които прииждат от AFF, AmateurMatch и други FriendFinder сайтове. Моделите излъчват от <strong>Model Center</strong> на Cams.com, който поддържа както браузърния broadcaster, така и <strong>external encoder през RTMP</strong>. Безплатният <strong style='color:var(--text)'>SplitCam</strong> стриймва през RTMP за пълни мулти-камера сцени, наслагвания и филтри — или, в браузърния broadcaster, се регистрира като <strong>виртуална камера</strong> със същия резултат.",
        "quick": "Излъчвай в Cams.com: инсталирай SplitCam, изгради сцената, вземи Cams.com RTMP server URL + stream key от Model Center, постави в SplitCam, натисни Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li><li>Копирай server URL + ключ от Cams.com Model Center → External Encoder.</li><li>Постави в custom RTMP на SplitCam.</li><li>Натисни Go Live.</li></ol>",
        "key_how": "Cams.com Model Center има таб <strong>External Encoder / OBS</strong> със server URL и stream key. Постави и двете в <strong>Stream Settings → Custom RTMP</strong> на SplitCam; избери 3 500–5 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди. Натисни <strong>Go Live</strong> в SplitCam, после стартирай шоуто от Model Center. Ако предпочиташ браузърния broadcaster, избери <strong>SplitCam</strong> от падащото меню за камера.",
        "tips": [
            ("AFF кръстосан трафик = плащащи членове", "Cams.com изтегля зрители от AdultFriendFinder акаунти, които вече имат метод за плащане в системата — различна публика от прясно регистрираните. Конверсията към private и tip-ове обикновено е по-висока."),
            ("External encoder бие браузъра", "RTMP от SplitCam дава чист bitrate и ти позволява да съчиняваш мулти-камера сцени с наслагвания; браузърният broadcaster работи, но ограничава продукцията."),
            ("Използвай private show инструментите", "Cams.com разчита на private/exclusive сесии. Tip меню и ясен път към private (в наслагване) забележимо вдигат приходите на зрител."),
            _T_TEST,
        ],
        "faq": [
            ("Cams.com същото нещо ли е като AdultFriendFinder?", "Същата майчина мрежа. Cams.com е кам-broadcasting марката; зрителите могат да дойдат през AFF, AmateurMatch и други FriendFinder сайтове, което е голяма част от трафика му."),
            ("Откъде вземам моя stream key за Cams.com?", "В Cams.com Model Center отвори таба <em>External Encoder</em> или <em>OBS</em> — ще видиш server URL и stream key. Постави и двете в полетата за custom RTMP на SplitCam."),
            ("Браузърен broadcaster или RTMP?", "RTMP (external encoder) се предпочита — стабилен bitrate, пълни SplitCam сцени. Браузърният broadcaster върши работа като резерва: избери SplitCam като уебкамера."),
            ("Безплатен ли е SplitCam за Cams.com?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, tip меню, втора камера или телефона, beauty filters или AI фон — всичко на живо."),
            ("Вземи URL + stream key за Cams.com", "Влез в Cams.com Model Center, отвори таба <strong>External Encoder / OBS</strong> и копирай <strong>server URL</strong> и <strong>stream key</strong>."),
            ("Свържи SplitCam с Cams.com", "В SplitCam → <strong>Stream Settings → Custom RTMP</strong>, постави URL и ключа. Настрой 3 500–5 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от Model Center. Стриймът ти стига до мрежата Cams.com / AFF за ~10 секунди."),
        ],
    },
    {
        "slug": "stripcamfun", "name": "StripCamFun",
        "title": "Излъчване в StripCamFun със SplitCam (RTMP/OBS)",
        "desc": "Излъчване в StripCamFun с безплатен SplitCam през RTMP — мулти-камера сцени, наслагвания и филтри за инди кам публика. Без воден знак, без регистрация.",
        "kw": "как да излъчвате на stripcamfun, stripcamfun obs, stripcamfun rtmp, stripcamfun модел, stripcamfun broadcast, strip cam fun model signup, stripcamfun stream key, инди кам сайт obs",
        "h1html": 'Как да излъчваш в <span class="accent">StripCamFun</span> със SplitCam',
        "h1short": "Излъчване StripCamFun",
        "card": "Безплатен SplitCam → RTMP/OBS стрийм към StripCamFun.",
        "intro": "StripCamFun е независим live-cam сайт — по-малък от гигантите от ранга на Chaturbate, но с реална, по-малко наситена публика и забележимо по-малка конкуренция между broadcaster-ите на ниша. Моделите излъчват от модел панела на StripCamFun, който излага опция за <strong>external encoder / RTMP</strong>. Безплатният <strong style='color:var(--text)'>SplitCam</strong> се връзва през RTMP за пълни мулти-камера сцени, наслагвания и филтри — а където е наличен браузърен broadcaster, SplitCam също се регистрира като <strong>виртуална камера</strong>.",
        "quick": "Излъчвай в StripCamFun: инсталирай SplitCam, изгради сцената, копирай StripCamFun server URL + stream key, постави в RTMP настройките на SplitCam, натисни Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li><li>Копирай URL + stream key от модел панела на StripCamFun → External Encoder.</li><li>Постави в custom RTMP на SplitCam.</li><li>Натисни Go Live.</li></ol>",
        "key_how": "Отвори модел dashboard-а на StripCamFun и секцията <strong>External Encoder / OBS</strong>. Копирай server URL и stream key в <strong>Stream Settings → Custom RTMP</strong> на SplitCam; настрой 3 500–5 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди. Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от dashboard-а.",
        "tips": [
            ("По-малък басейн, по-лесна видимост", "На сайт от Tier-1 си един от хиляди онлайн; в StripCamFun списъкът на broadcaster-и е къс — полирана SplitCam сцена изпъква на началната страница по-бързо."),
            ("Кръстосвай излъчването за обхват", "Инди кам сайтовете вървят добре с мултистрийминг. Използвай SplitCam, за да стриймваш едновременно към StripCamFun и към по-голям сайт, за да задържиш tip-ърите от двата басейна."),
            ("Залагай на нишови тагове", "Инди публиките търсят по ниша повече, отколкото по звездност. Конкретни тагове + наслагване със сцена, което именува нишата, изтегля зрителите от листинга."),
            _T_TEST,
        ],
        "faq": [
            ("Откъде вземам stream key за StripCamFun?", "В модел dashboard-а отвори таба <em>External Encoder / OBS</em> — ще видиш server URL и stream key. Постави и двете в полетата за custom RTMP на SplitCam."),
            ("Безопасно ли е да се излъчва в StripCamFun?", "Като всеки инди кам сайт, провери модел договора и условията за изплащане, преди да излезеш на живо. Използвай реален имейл и първо верифицирай метода си за изплащане."),
            ("Мога ли да мултистриймвам към StripCamFun и друг кам сайт?", "Да — SplitCam може да push-ва към няколко custom RTMP endpoint-а едновременно. Първо потвърди правилата за ексклузивност на всеки сайт."),
            ("Безплатен ли е SplitCam за StripCamFun?", "Да — безплатен, без воден знак и без лимит на времето."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, tip меню, втора камера или телефона, beauty filters или AI фон — всичко на живо."),
            ("Вземи URL + stream key за StripCamFun", "Влез в модел dashboard-а на StripCamFun, отвори <strong>External Encoder / OBS</strong> и копирай <strong>server URL</strong> и <strong>stream key</strong>."),
            ("Свържи SplitCam със StripCamFun", "В SplitCam → <strong>Stream Settings → Custom RTMP</strong>, постави URL и ключа. Настрой 3 500–5 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн в dashboard-а на StripCamFun. Стриймът ти стига до публичния списък за ~10 секунди."),
        ],
    },
    {
        "slug": "mym-fans", "name": "MYM.fans",
        "title": "На живо в MYM.fans със SplitCam — виртуална камера",
        "desc": "Излизай на живо в MYM.fans (френския OnlyFans) с безплатен SplitCam като виртуална камера — сцени, наслагвания и филтри. Без воден знак.",
        "kw": "как да излъчвате на живо в mym, mym.fans live, mym fans виртуална камера, mym creator, mym france, mym live stream, mym obs, mym fans broadcast, mym influencer",
        "h1html": 'Как да излизаш на живо в <span class="accent">MYM.fans</span> със SplitCam',
        "h1short": "На живо в MYM.fans",
        "card": "Използвай SplitCam като виртуална камера за MYM.fans live.",
        "intro": "MYM.fans е водещата френска creator-абонаментна платформа — френският отговор на OnlyFans, с абонаменти, pay-per-view, бакшиши и вградена функция за <strong>live stream</strong> за феновете. Broadcaster-ът ѝ върви в браузъра, така че насочването на безплатния <strong style='color:var(--text)'>SplitCam</strong> към MYM като <strong>виртуална камера</strong> добавя мулти-камера сцени, наслагвания и филтри върху стандартната уебкамера. Ако твоят creator dashboard излага опция за external encoder, SplitCam може да се свърже и през RTMP.",
        "quick": "Излизай на живо в MYM.fans със SplitCam: инсталирай SplitCam, изгради сцената, започни live в MYM и в селектора за камера на broadcaster-а избери <em>SplitCam</em> — после Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li><li>Започни live в MYM.fans.</li><li>Избери SplitCam в падащото меню за камера.</li><li>Натисни Go Live.</li></ol>",
        "key_how": "Live на MYM.fans върви в браузъра. Изгради сцената в SplitCam — той се регистрира като уебкамера с име <strong>\"SplitCam Video Driver\"</strong> — после отвори live broadcaster-а на MYM и избери <strong>SplitCam</strong> в падащото меню за камера. Ако в твоя creator dashboard е достъпна опция за <strong>stream-key / external-encoder</strong>, постави я в полетата за custom RTMP на SplitCam.",
        "tips": [
            ("Най-голямата френска creator платформа", "MYM е #1 fan-платформа във Франция, с френска/европейска публика, която е свикнала да плаща в EUR. Полирана сцена в SplitCam + наслагвания на френски конвертират по-добре от обикновена уебкамера."),
            ("Виртуалната камера работи без stream key", "Браузърното live пак получава пълната ти сцена от SplitCam — втора камера, наслагвания, beauty filters или AI фон — просто чрез избиране на SplitCam за уебкамера."),
            ("Cross-sell на PPV по време на live", "MYM е изградена около платено съдържание. Наслагвания на екрана, които промотират абонамента или отключването на PPV съобщения, превръщат live зрителите в платящи абонати."),
            _T_TEST,
        ],
        "faq": [
            ("Как SplitCam се свързва с MYM.fans?", "Live на MYM е в браузъра, така че SplitCam се свързва като виртуална камера — избери SplitCam в селектора за камера. Не е нужен stream key."),
            ("Мога ли да използвам наслагвания и няколко камери в MYM?", "Да — изгради сцената в SplitCam (втора камера, наслагвания, AI фон); MYM вижда готовата сцена като една уебкамера."),
            ("Поддържа ли MYM.fans OBS или външни енкодери?", "Live е основно браузърно/уебкамерно. Ако твоят dashboard предлага опция за stream key, постави я в полетата за custom RTMP на SplitCam; иначе използвай метода с виртуална камера."),
            ("Безплатен ли е SplitCam за MYM.fans?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Инсталира виртуална камера, която браузърът може да избере."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, текст (на френски, ако публиката ти е FR), втора камера или телефона, beauty filters или AI фон."),
            ("Започни live в MYM.fans", "Влез в своя MYM creator акаунт и отвори live broadcaster-а, за да започнеш стрийм за абонатите си."),
            ("Избери SplitCam за камера", "В падащото меню за камера на MYM избери <strong>SplitCam</strong> вместо суровата уебкамера — твоята композирана сцена замества плоската камера. (Или постави stream key в полетата за custom RTMP на SplitCam, ако е наличен.)"),
            ("Go Live", "Стартирай излъчването — твоята сцена в SplitCam, наслагванията и филтрите стигат до абонатите ти в MYM."),
        ],
    },
    {
        "slug": "fc2-live", "name": "FC2 Live",
        "title": "Излъчване в FC2 Live със SplitCam (RTMP/OBS)",
        "desc": "Излъчване в FC2 Live (най-големият live-cam в Япония) с безплатен SplitCam през RTMP — сцени, наслагвания и филтри. Без воден знак.",
        "kw": "как да излъчвате на fc2 live, fc2 live obs, fc2 live rtmp, fc2 live broadcast, fc2 live配信, fc2 live stream key, fc2 live model, fc2 live japan, fc2 ライブ",
        "h1html": 'Как да излъчваш в <span class="accent">FC2 Live</span> със SplitCam',
        "h1short": "Излъчване FC2 Live",
        "card": "Безплатен SplitCam → RTMP/OBS стрийм към FC2 Live.",
        "intro": "FC2 Live е най-голямата платформа за live-streaming в Япония — масова зрителска база, обособена adult секция и отделен платен show поток, който я прави един от най-доходоносните кам пазари в Азия. Моделите излъчват от broadcaster панела на FC2, който поддържа както браузърния broadcaster, така и <strong>external encoder през RTMP</strong>. Безплатният <strong style='color:var(--text)'>SplitCam</strong> стриймва през RTMP за пълни мулти-камера сцени, наслагвания и филтри.",
        "quick": "Излъчвай в FC2 Live със SplitCam: инсталирай SplitCam, изгради сцената, копирай server URL + stream key от broadcaster панела на FC2, постави в RTMP настройките на SplitCam, натисни Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li><li>Копирай URL + stream key от broadcaster панела на FC2.</li><li>Постави в custom RTMP на SplitCam.</li><li>Натисни Go Live.</li></ol>",
        "key_how": "Отвори broadcaster панела на FC2 Live и превключи на <strong>External Encoder / RTMP</strong>. Копирай server URL и твоя stream key в <strong>Stream Settings → Custom RTMP</strong> на SplitCam; настрой 3 500–5 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди. Натисни <strong>Go Live</strong> в SplitCam, после стартирай шоуто си от dashboard-а на FC2.",
        "tips": [
            ("Огромна японска публика", "FC2 е Tier 1 в Япония — зрителите са местни, свикнали да плащат в JPY, и предпочитат по-дълги платени шоута. Текст на наслагване на японски (напр. tip меню в 円 / JPY) забележимо вдига конверсията."),
            ("Adult секцията е отделена", "FC2 има едновременно общи и adult лайвове. Настрой правилно категорията на стаята преди go-live — adult шоутата не могат да бъдат открити от общата секция."),
            ("Използвай external encoder за стабилен битрейт", "Японската мобилна публика е чувствителна към изпуснати кадри. RTMP от SplitCam при стабилни 4 Mbps бие браузърния broadcaster по надеждност."),
            _T_TEST,
        ],
        "faq": [
            ("Откъде вземам stream key за FC2 Live?", "В broadcaster панела на FC2 Live превключи на <em>External Encoder</em> или <em>OBS</em> — ще видиш server URL и stream key. Постави и двете в полетата за custom RTMP на SplitCam."),
            ("Браузърен broadcaster или RTMP?", "RTMP (external encoder) е за предпочитане — стабилен битрейт, пълни сцени от SplitCam. Браузърният broadcaster работи като резерв: избери SplitCam за уебкамера."),
            ("Трябва ли ми японски акаунт, за да стриймвам в FC2?", "Изисква се FC2 акаунт, а adult стриймването има допълнителни стъпки за проверка на възрастта на модела. Следвай onboarding-а на FC2."),
            ("Безплатен ли е SplitCam за FC2 Live?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания, tip меню в 円 (JPY), втора камера или телефона, beauty filters или AI фон — всичко на живо."),
            ("Вземи URL + stream key за FC2 Live", "Влез в FC2, отвори broadcaster панела за Live, превключи на <strong>External Encoder</strong> и копирай <strong>server URL</strong> и твоя <strong>stream key</strong>."),
            ("Свържи SplitCam с FC2 Live", "В SplitCam → <strong>Stream Settings → Custom RTMP</strong>, постави URL и ключа. Настрой 3 500–5 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после стартирай шоуто от dashboard-а на FC2. Стриймът ти стига до публичния списък за ~10 секунди."),
        ],
    },
    {
        "slug": "boosty", "name": "Boosty",
        "title": "На живо в Boosty със SplitCam — виртуална камера",
        "desc": "Излизай на живо в Boosty (руската creator платформа) с безплатен SplitCam като виртуална камера — мулти-камера сцени, наслагвания и филтри. Без воден знак.",
        "kw": "как да излъчвате на живо в boosty, boosty live, boosty stream, boosty виртуална камера, boosty creator, бусти прямой эфир, boosty obs, boosty paid live, boosty subscriber",
        "h1html": 'Как да излизаш на живо в <span class="accent">Boosty</span> със SplitCam',
        "h1short": "На живо в Boosty",
        "card": "Използвай SplitCam като виртуална камера за Boosty live.",
        "intro": "Boosty е най-голямата руска платформа за creator-монетизация — услуга в стил Patreon с абонаменти, платени публикации, бакшиши и функция за <strong>live broadcast</strong>, с creator аудитория, която включва adult creator-и наред с mainstream. Live върви в браузъра, така че свързването на безплатния <strong style='color:var(--text)'>SplitCam</strong> като <strong>виртуална камера</strong> добавя мулти-камера сцени, наслагвания и филтри, които абонатите не биха получили от обикновена уебкамера.",
        "quick": "Излизай на живо в Boosty със SplitCam: инсталирай SplitCam, изгради сцената, започни live в Boosty и избери <em>SplitCam</em> в падащото меню за камера на broadcaster-а — после Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li><li>Започни live в Boosty.</li><li>Избери SplitCam в падащото меню за камера.</li><li>Натисни Go Live.</li></ol>",
        "key_how": "Live на Boosty върви в браузъра. Изгради сцената в SplitCam — той се регистрира като уебкамера с име <strong>\"SplitCam Video Driver\"</strong> — после отвори live broadcaster-а на Boosty и избери <strong>SplitCam</strong> в падащото меню за камера вместо суровата уебкамера.",
        "tips": [
            ("Най-голямата creator платформа в Русия", "Boosty замени Patreon за много RU creator-и след санкциите, така че публиката е лоялна и свикнала да плаща в RUB. Полирана сцена в SplitCam с наслагвания на руски конвертира добре."),
            ("Live шоута по абонаментен tier", "Boosty позволява да gate-неш live стриймове по абонаментен tier. SplitCam работи с всички tier-и — енкодерът не го интересува на какъв tier е зрителят, ти стриймваш веднъж, а Boosty управлява достъпа."),
            ("Наслагване за бакшиш и pay-per-view", "Boosty поддържа платени unlock-вания на публикации и бакшиши. Наслагване на екрана, което изброява предимствата по tier-и, вдига конверсията по време на live стрийма."),
            _T_TEST,
        ],
        "faq": [
            ("Как SplitCam се свързва с Boosty?", "Live на Boosty е в браузъра, така че SplitCam се свързва като виртуална камера — избери SplitCam в селектора за камера. Не е нужен stream key."),
            ("Мога ли да използвам наслагвания на Boosty live?", "Да — композирай сцената в SplitCam (наслагвания, втора камера, AI фон); Boosty вижда една уебкамера. Абонатите получават пълната композирана сцена."),
            ("Поддържа ли Boosty OBS или външни енкодери?", "Live на Boosty е основно браузърно. Ако в creator панела ти се появи опция за stream key, постави я в полетата за custom RTMP на SplitCam; иначе използвай метода с виртуална камера."),
            ("Безплатен ли е SplitCam за Boosty?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Инсталира виртуална камера, която браузърът може да избере."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания (на руски за публиката ти), втора камера или телефона, beauty filters или AI фон."),
            ("Започни live в Boosty", "Влез в своя Boosty creator акаунт и отвори live broadcaster-а. Настрой gating по tier, ако искаш live-ът да е зад платено ниво."),
            ("Избери SplitCam за камера", "В падащото меню за камера на Boosty избери <strong>SplitCam</strong> вместо суровата уебкамера — твоята композирана сцена замества плоската камера."),
            ("Go Live", "Стартирай излъчването — твоята сцена в SplitCam, наслагванията и филтрите стигат до абонатите ти в Boosty."),
        ],
    },
    {
        "slug": "amateurcommunity", "name": "AmateurCommunity",
        "title": "Излъчване в AmateurCommunity със SplitCam (RTMP)",
        "desc": "Излъчване в AmateurCommunity (най-големият любителски кам в Германия) с безплатен SplitCam през RTMP — сцени, наслагвания и филтри. Без воден знак.",
        "kw": "как да излъчвате на amateurcommunity, amateurcommunity obs, amateurcommunity rtmp, amateur community deutschland, amateurcommunity model, ac community broadcast, amateurcommunity live, amateur cam deutschland",
        "h1html": 'Как да излъчваш в <span class="accent">AmateurCommunity</span> със SplitCam',
        "h1short": "Излъчване AmateurCommunity",
        "card": "Безплатен SplitCam → RTMP стрийм към AmateurCommunity (DE).",
        "intro": "AmateurCommunity е най-голямата германска любителска кам и content общност — функционира от началото на 2000-те с дълбоко лоялна немскоговоряща публика, която е свикнала да плаща за съдържание и live шоута. Моделите излъчват от модел панела на AC, който поддържа <strong>external encoder през RTMP</strong>, както и браузърния broadcaster. Безплатният <strong style='color:var(--text)'>SplitCam</strong> стриймва през RTMP за пълни мулти-камера сцени, наслагвания и филтри — наслагвания на немски говорят директно на местната публика.",
        "quick": "Излъчвай в AmateurCommunity: инсталирай SplitCam, изгради сцената, копирай AC server URL + stream key от модел панела, постави в RTMP настройките на SplitCam, натисни Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li><li>Копирай URL + stream key от AC модел панела.</li><li>Постави в custom RTMP на SplitCam.</li><li>Натисни Go Live.</li></ol>",
        "key_how": "Отвори модел панела на AmateurCommunity и таба <strong>External Encoder / OBS</strong>. Копирай server URL и твоя stream key в <strong>Stream Settings → Custom RTMP</strong> на SplitCam; настрой 3 500–5 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди. Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн от панела.",
        "tips": [
            ("Немскоговоряща, немско-плащаща публика", "Публиката на AmateurCommunity е преобладаващо DACH (DE/AT/CH) и плаща в EUR — наслагвания, tip меню и on-stream чат на немски конвертират забележимо по-добре от английския."),
            ("Premium PPV + live комбо", "AC ти позволява да продаваш PPV съдържание заедно с live. Live шоу, което тийзва PPV (с наслагване на екрана), обикновено вдига PPV продажбите по време и след излъчването."),
            ("External encoder за стабилно качество", "Публиката на AC очаква висока продукция; RTMP при стабилни 4 Mbps от SplitCam бие променливия битрейт на браузърния broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Откъде вземам stream key за AmateurCommunity?", "В модел панела на AC отвори таба <em>External Encoder</em> или <em>OBS</em> — ще видиш server URL и stream key. Постави и двете в полетата за custom RTMP на SplitCam."),
            ("Браузърен broadcaster или RTMP?", "RTMP (external encoder) е за предпочитане за сериозни модели — стабилен битрейт, пълни сцени от SplitCam. Браузърният broadcaster работи като резерв: избери SplitCam за уебкамера."),
            ("Трябва ли да съм в Германия, за да стриймвам в AC?", "Не, но публиката е немскоговоряща. Модели отвсякъде могат да се регистрират — основната стъпка е преминаването на модел верификацията и данъчните формуляри."),
            ("Безплатен ли е SplitCam за AmateurCommunity?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания (на немски — \"Trinkgeld\" / \"PPV freischalten\"), втора камера или телефона, beauty filters или AI фон — всичко на живо."),
            ("Вземи URL + stream key за AmateurCommunity", "Влез в модел панела на AC, отвори <strong>External Encoder / OBS</strong> и копирай <strong>server URL</strong> и <strong>stream key</strong>."),
            ("Свържи SplitCam с AmateurCommunity", "В SplitCam → <strong>Stream Settings → Custom RTMP</strong>, постави URL и ключа. Настрой 3 500–5 000 Kbps при 1920×1080, 30 fps, keyframe на 2 секунди."),
            ("Натисни Go Live", "Натисни <strong>Go Live</strong> в SplitCam, после се пусни онлайн в модел панела на AC. Стриймът ти стига до публичния списък за ~10 секунди."),
        ],
    },
    {
        "slug": "myfans-jp", "name": "MyFans.jp",
        "title": "На живо в MyFans.jp със SplitCam — виртуална камера",
        "desc": "На живо в MyFans.jp (японската OnlyFans алтернатива) с безплатен SplitCam като виртуална камера — сцени, наслагвания, филтри. Без воден знак.",
        "kw": "как да излъчвате на живо в myfans, myfans.jp live, myfans 配信, myfans виртуална камера, myfans creator, マイファンズ, myfans japan, myfans broadcast, myfans subscriber",
        "h1html": 'Как да излизаш на живо в <span class="accent">MyFans.jp</span> със SplitCam',
        "h1short": "На живо в MyFans.jp",
        "card": "Използвай SplitCam като виртуална камера за MyFans.jp live.",
        "intro": "MyFans.jp е водещата японска creator-subscription платформа — японският отговор на OnlyFans, с абонаменти, pay-per-view, бакшиши (投げ銭) и вградена функция <strong>live stream</strong> за фенове. Broadcaster-ът върви в браузъра, така че насочването на безплатния <strong style='color:var(--text)'>SplitCam</strong> към MyFans като <strong>виртуална камера</strong> добавя мулти-камера сцени, наслагвания и филтри, които обикновена уебкамера не може да достави. Ако creator dashboard-ът ти предлага опция за external encoder, SplitCam може да се свърже и през RTMP.",
        "quick": "Излизай на живо в MyFans.jp със SplitCam: инсталирай SplitCam, изгради сцената, започни live в MyFans и в селектора за камера на broadcaster-а избери <em>SplitCam</em> — после Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li><li>Започни live в MyFans.jp.</li><li>Избери SplitCam в падащото меню за камера.</li><li>Натисни Go Live.</li></ol>",
        "key_how": "Live на MyFans.jp върви в браузъра. Изгради сцената в SplitCam — той се регистрира като уебкамера с име <strong>\"SplitCam Video Driver\"</strong> — после отвори live broadcaster-а на MyFans и избери <strong>SplitCam</strong> в падащото меню за камера. Ако в creator dashboard-а се появи опция за <strong>stream key / external encoder</strong>, постави я вместо това в полетата за custom RTMP на SplitCam.",
        "tips": [
            ("Най-голямата fan-платформа в Япония", "MyFans е #1 creator-subscription платформата в Япония, с JP-родна публика, която плаща в 円 (JPY). Наслагвания на японски и полирана сцена в SplitCam конвертират далеч по-добре от обикновена уебкамера."),
            ("Виртуална камера, без нужда от stream key", "Само-в-браузъра live пак получава пълната ти сцена от SplitCam — втора камера, наслагвания, beauty filters или AI фон — само като избереш SplitCam за уебкамера."),
            ("Cross-sell PPV по време на live", "MyFans е изграден около 投げ銭 (бакшиши) и платени публикации. Наслагване на екрана, което споменава твоя PPV пакет или tip-цел, забележимо вдига приходите по време на live."),
            _T_TEST,
        ],
        "faq": [
            ("Как SplitCam се свързва с MyFans.jp?", "Live на MyFans е в браузъра, така че SplitCam се свързва като виртуална камера — избери SplitCam в селектора за камера. Не е нужен stream key."),
            ("Мога ли да използвам наслагвания и няколко камери на MyFans?", "Да — изгради сцената в SplitCam (втора камера, наслагвания, AI фон); MyFans вижда готовата сцена като една уебкамера."),
            ("Поддържа ли MyFans.jp OBS или външни енкодери?", "Live е основно базиран на браузър/уебкамера. Ако в dashboard-а ти се появи опция за stream key, постави я в полетата за custom RTMP на SplitCam; иначе използвай метода с виртуална камера."),
            ("Безплатен ли е SplitCam за MyFans.jp?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Инсталира виртуална камера, която браузърът може да избере."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания (на японски — 「投げ銭」「PPV解放」 за публиката ти), втора камера или телефона, beauty filters или AI фон."),
            ("Започни live в MyFans.jp", "Влез в своя MyFans creator акаунт и отвори live broadcaster-а (配信), за да стартираш стрийм за абонатите си."),
            ("Избери SplitCam за камера", "В падащото меню за камера на MyFans избери <strong>SplitCam</strong> вместо суровата уебкамера — твоята композирана сцена замества плоската камера. (Или постави stream key в полетата за custom RTMP на SplitCam, ако е наличен.)"),
            ("Go Live", "Стартирай излъчването — твоята сцена в SplitCam, наслагванията и филтрите стигат до абонатите ти в MyFans."),
        ],
    },
    {
        "slug": "privacy-com-br", "name": "Privacy.com.br",
        "title": "На живо в Privacy.com.br със SplitCam — виртуална камера",
        "desc": "Ao vivo в Privacy.com.br (бразилската OnlyFans) с безплатен SplitCam като виртуална камера — сцени, наслагвания, филтри. Без воден знак.",
        "kw": "как да излъчвате на живо в privacy, privacy.com.br ao vivo, privacy live, privacy brasil, privacy виртуална камера, privacy creator, privacy broadcast, privacy br criadora, privacy assinante",
        "h1html": 'Как да излизаш на живо в <span class="accent">Privacy.com.br</span> със SplitCam',
        "h1short": "На живо в Privacy.com.br",
        "card": "Използвай SplitCam като виртуална камера за Privacy.com.br ao vivo.",
        "intro": "Privacy.com.br е водещата бразилска creator-subscription платформа — бразилският отговор на OnlyFans, с assinaturas, pay-per-view, gorjetas и вградена функция <strong>ao vivo</strong> (live stream) за fãs. Broadcaster-ът върви в браузъра, така че насочването на безплатния <strong style='color:var(--text)'>SplitCam</strong> към Privacy като <strong>виртуална камера</strong> добавя мулти-камера сцени, наслагвания и филтри, които плоска уебкамера не може да достави. Ако creator dashboard-ът ти предлага опция за external encoder, SplitCam може да се свърже и през RTMP.",
        "quick": "Излизай на живо в Privacy.com.br със SplitCam: инсталирай SplitCam, изгради сцената, започни ao vivo в Privacy и в селектора за камера на broadcaster-а избери <em>SplitCam</em> — после Go Live."
                 "<ol><li>Инсталирай SplitCam.</li><li>Добави камера + сцена.</li><li>Започни ao vivo в Privacy.com.br.</li><li>Избери SplitCam в падащото меню за камера.</li><li>Натисни Go Live.</li></ol>",
        "key_how": "Ao vivo на Privacy.com.br върви в браузъра. Изгради сцената в SplitCam — той се регистрира като уебкамера с име <strong>\"SplitCam Video Driver\"</strong> — после отвори live broadcaster-а на Privacy и избери <strong>SplitCam</strong> в падащото меню за камера. Ако се предлага опция за <strong>stream key / external encoder</strong>, постави я вместо това в полетата за custom RTMP на SplitCam.",
        "tips": [
            ("Най-голямата fan-платформа в Бразилия", "Privacy е #1 creator-subscription платформата в Бразилия, с португалоговоряща публика, свикнала да плаща в BRL през PIX. Наслагвания на португалски + полирана сцена в SplitCam конвертират много по-добре от обикновена уебкамера."),
            ("Виртуална камера, без нужда от stream key", "Само-в-браузъра live пак получава пълната ти сцена от SplitCam — втора камера, наслагвания, beauty filters или AI фон — само като избереш SplitCam за уебкамера."),
            ("Tip менюта + PPV по време на ao vivo", "Privacy поддържа gorjetas (бакшиши) и платени публикации. Наслагване на екрана, което споменава твоя PPV пакет или meta-de-gorjeta, вдига приходите по време на live."),
            _T_TEST,
        ],
        "faq": [
            ("Как SplitCam се свързва с Privacy.com.br?", "Ao vivo на Privacy е в браузъра, така че SplitCam се свързва като виртуална камера — избери SplitCam в селектора за камера. Не е нужен stream key."),
            ("Мога ли да използвам наслагвания и няколко камери на Privacy?", "Да — изгради сцената в SplitCam (втора камера, наслагвания, AI фон); Privacy вижда готовата сцена като една уебкамера."),
            ("Поддържа ли Privacy.com.br OBS или външни енкодери?", "Ao vivo е основно базирано на браузър/уебкамера. Ако в dashboard-а ти се появи опция за stream key, постави я в полетата за custom RTMP на SplitCam; иначе използвай метода с виртуална камера."),
            ("Безплатен ли е SplitCam за Privacy.com.br?", "Да — SplitCam е безплатен, без воден знак и без лимит на времето."),
        ],
        "steps": [
            ("Свали и инсталирай SplitCam", "SplitCam е безплатен софтуер за live-streaming за Windows и macOS — без регистрация, без карта, без воден знак. Инсталира виртуална камера, която браузърът може да избере."),
            ("Изгради сцената", "Отвори SplitCam и добави уебкамерата. Сложи отгоре наслагвания на португалски (\"gorjeta\", \"desbloquear PPV\"), втора камера или телефона, beauty filters или AI фон."),
            ("Започни ao vivo в Privacy.com.br", "Влез в своя Privacy creator акаунт и отвори ao-vivo broadcaster-а, за да стартираш live за абонатите си."),
            ("Избери SplitCam за камера", "В падащото меню за камера на Privacy избери <strong>SplitCam</strong> вместо суровата уебкамера — твоята композирана сцена замества плоската камера. (Или постави stream key в полетата за custom RTMP на SplitCam, ако е наличен.)"),
            ("Go Live", "Стартирай излъчването — твоята сцена в SplitCam, наслагванията и филтрите стигат до абонатите ти в Privacy.com.br."),
        ],
    },
]
