# -*- coding: utf-8 -*-
"""Spanish content for cam-streaming-guides. Genuinely per-platform (not templated)."""

_T_ETH = ("Conexión por cable", "Ethernet es más fiable que el Wi-Fi para un directo largo — "
          "un fotograma perdido es una propina perdida. Lleva un cable al PC de streaming.")
_T_TEST = ("Haz una prueba privada primero", "Una emisión de prueba corta verifica cámara, "
           "audio, encuadre y superposiciones antes de abrir la sala.")

PLATFORMS_ES = [
    {
        "slug": "chaturbate", "name": "Chaturbate",
        "title": "Cómo emitir en Chaturbate con SplitCam — token y RTMP",
        "desc": "Emite en Chaturbate con SplitCam gratis. Consigue tu token de emisión en "
                "Broadcast Yourself, enruta el codificador externo por SplitCam — escenas, "
                "superposiciones, sin marca de agua.",
        "kw": "cómo emitir en chaturbate, chaturbate broadcast token, chaturbate rtmp obs, "
              "chaturbate codificador externo",
        "h1html": 'Cómo emitir en <span class="accent">Chaturbate</span> con SplitCam',
        "h1short": "Emitir en Chaturbate",
        "card": "Configuración por token y codificador externo de Chaturbate.",
        "intro": "Chaturbate es una de las mayores plataformas cam, basada en una economía de "
                 "tokens. Su emisor de navegador es una sola cámara plana — enrutar por el "
                 "<strong style='color:var(--text)'>codificador externo</strong> con "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis desbloquea escenas "
                 "con varias cámaras, superposiciones y filtros sobre el mismo stream de token.",
        "quick": "Emite en Chaturbate con SplitCam: instala SplitCam, monta tu escena, abre "
                 "<em>Broadcast Yourself → My Broadcast</em>, copia tu token de emisión, pégalo "
                 "en SplitCam, pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Copia tu token de emisión de Chaturbate.</li><li>Pégalo en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "En Chaturbate, pulsa <strong>Broadcast Yourself</strong> para abrir la "
                   "página <strong>My Broadcast</strong>, luego <strong>View RTMP/OBS broadcast "
                   "information and stream key</strong>. La clave se muestra como tu "
                   "<strong>token de emisión</strong> — cópialo. Funciona como una contraseña; "
                   "no lo publiques.",
        "tips": [
            ("Tu token es la clave", "Chaturbate usa tu token de emisión en lugar de una clave "
             "genérica. Trátalo como una contraseña; reinícialo si se filtra."),
            ("Usa el preset recomendado de SplitCam", "La guía de Chaturbate apunta a un preset "
             "recomendado — los ajustes automáticos de SplitCam lo igualan."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿Chaturbate permite OBS / codificadores externos?", "Sí — Chaturbate expone datos "
             "RTMP/OBS y un token en Broadcast Yourself, así que SplitCam funciona."),
            ("¿Dónde está mi clave de stream de Chaturbate?", "Broadcast Yourself → My Broadcast "
             "→ View RTMP/OBS broadcast information and stream key. La clave es tu token."),
            ("¿SplitCam es gratis para Chaturbate?", "Sí — 100% gratis, sin marca de agua, sin "
             "límite de tiempo."),
            ("¿Qué bitrate para Chaturbate?", "3.500–6.000 Kbps a 1080p. Prueba tu subida con "
             "el test de velocidad de SplitCam primero."),
        ],
    },
    {
        "slug": "cam4", "name": "CAM4",
        "title": "Cómo emitir en CAM4 con SplitCam — codificador externo",
        "desc": "Emite en CAM4 con SplitCam gratis. Abre Broadcast & Earn Money, External "
                "Encoder, Get Stream Key, ajusta geo-restricciones — escenas y superposiciones.",
        "kw": "cómo emitir en cam4, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
        "h1html": 'Cómo emitir en <span class="accent">CAM4</span> con SplitCam',
        "h1short": "Emitir en CAM4",
        "card": "External Encoder de CAM4 con geo-controles.",
        "intro": "CAM4 es una plataforma cam global con geo-controles integrados — puedes "
                 "ocultar tu emisión en países concretos. Enrutar por "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis como codificador "
                 "externo añade cambio de escenas y superposiciones que el emisor básico no "
                 "puede.",
        "quick": "Emite en CAM4 con SplitCam: instala SplitCam, monta tu escena, en CAM4 abre "
                 "<em>Broadcast &amp; Earn Money → Start Broadcast → External Encoder</em>, Get "
                 "Stream Key, pégala en SplitCam, Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la clave de CAM4.</li><li>Pégala en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "En CAM4, pulsa <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn "
                   "Money</strong> → <strong>Start Broadcast</strong>, luego <strong>External "
                   "Encoder</strong> arriba. Rellena fecha de nacimiento, género y país, usa "
                   "<strong>Get Stream Key</strong> y cópiala. Un slider verde en Stream "
                   "Settings de SplitCam confirma la conexión.",
        "tips": [
            ("Ajusta tus geo-restricciones", "CAM4 permite ocultar tu emisión en países y "
             "regiones concretas — configúralo en CAM4 antes de emitir si lo necesitas."),
            ("Vigila el slider verde", "El setup de CAM4 muestra un slider verde en Stream "
             "Settings de SplitCam cuando la clave se acepta — rojo significa revisarla."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿Puedo geo-bloquear mi emisión de CAM4?", "Sí — CAM4 tiene geo-restricción "
             "integrada para ocultar tu emisión en ciertos países. Se ajusta en CAM4."),
            ("¿Dónde está la clave de stream de CAM4?", "Broadcast → Broadcast & Earn Money → "
             "Start Broadcast → External Encoder → Get Stream Key."),
            ("¿SplitCam es gratis para CAM4?", "Sí — gratis, sin marca de agua, sin límites."),
            ("¿Qué bitrate para CAM4?", "3.500–6.000 Kbps a 1080p; comprueba tu subida primero."),
        ],
    },
    {
        "slug": "bongacams", "name": "BongaCams",
        "title": "Cómo emitir en BongaCams con SplitCam — codificador externo",
        "desc": "Emite en BongaCams con SplitCam gratis. Broadcast settings → Select Encoder → "
                "External Encoder. Si falta el botón, soporte lo activa.",
        "kw": "cómo emitir en bongacams, bongacams external encoder, bongacams rtmp obs",
        "h1html": 'Cómo emitir en <span class="accent">BongaCams</span> con SplitCam',
        "h1short": "Emitir en BongaCams",
        "card": "External Encoder de BongaCams.",
        "intro": "BongaCams es una plataforma cam global. La emisión por codificador externo no "
                 "siempre está activada por defecto — una vez habilitada, "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis lleva la emisión "
                 "con escenas, superposiciones y fondo con IA.",
        "quick": "Emite en BongaCams con SplitCam: instala SplitCam, monta tu escena, en "
                 "BongaCams abre <em>Options → Broadcast settings → Select Encoder → External "
                 "Encoder</em>, copia la URL y la clave, pega en SplitCam, Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la URL y clave de BongaCams.</li><li>Pega en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "En BongaCams, abre <strong>Options</strong> → <strong>Broadcast "
                   "settings</strong> → <strong>Select Encoder</strong> → <strong>External "
                   "Encoder</strong> y copia la URL del servidor y la clave. <strong>Si el "
                   "botón External Encoder no aparece</strong>, contacta con el soporte de "
                   "BongaCams y pide que activen la codificación externa en tu cuenta.",
        "tips": [
            ("¿Sin botón External Encoder? Soporte", "BongaCams restringe la codificación "
             "externa — si la opción falta en Broadcast settings, soporte debe activarla."),
            ("Iguala tu resolución", "BongaCams recomienda que la resolución de webcam y de "
             "emisión coincidan — por ejemplo, ambas a 1280×720."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿Por qué falta el botón External Encoder en BongaCams?", "La codificación externa "
             "no está activada para toda cuenta — contacta con soporte de BongaCams y el botón "
             "aparecerá en Broadcast settings."),
            ("¿BongaCams admite emisión por OBS?", "Sí — vía la opción External Encoder, así "
             "que SplitCam funciona una vez activada."),
            ("¿SplitCam es gratis para BongaCams?", "Sí — gratis, sin marca de agua, sin "
             "límites."),
            ("¿Qué bitrate para BongaCams?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
        ],
    },
    {
        "slug": "stripchat", "name": "Stripchat",
        "title": "Cómo emitir en Stripchat con SplitCam — software externo",
        "desc": "Emite en Stripchat con SplitCam gratis. Switch to external software, copia la "
                "clave-token, lleva escenas y superposiciones. Sin marca de agua.",
        "kw": "cómo emitir en stripchat, stripchat external software, stripchat stream key, "
              "stripchat rtmp obs",
        "h1html": 'Cómo emitir en <span class="accent">Stripchat</span> con SplitCam',
        "h1short": "Emitir en Stripchat",
        "card": "Configuración de software externo para Stripchat.",
        "intro": "Stripchat es una gran plataforma cam centrada en la interactividad. Su modo "
                 "<em>external software</em> te da una clave basada en token — pásala a "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis para emitir con "
                 "escenas, superposiciones y filtros en vez de una sola cámara plana.",
        "quick": "Emite en Stripchat con SplitCam: instala SplitCam, monta tu escena, en "
                 "Stripchat elige <em>Switch to external software</em>, copia la clave, pégala "
                 "en SplitCam, Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la clave de Stripchat.</li><li>Pégala en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "En Stripchat, elige <strong>Switch to external software</strong>, luego "
                   "abre <strong>Show external software settings for the stream</strong>. Copia "
                   "la clave de stream — Stripchat la muestra como un token. Mantenla privada.",
        "tips": [
            ("La clave es un token", "La clave de Stripchat es un token — cópiala exacta, no la "
             "compartas, reiníciala si se filtra."),
            ("Iguala tu resolución", "Stripchat recomienda que la resolución de webcam y "
             "emisión coincidan — por ejemplo ambas a 1280×720."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿Cómo cambio Stripchat a software externo?", "En tu vista de emisión elige Switch "
             "to external software, luego abre los ajustes de software externo para ver la "
             "clave."),
            ("¿Stripchat permite OBS / SplitCam?", "Sí — el modo external software acepta "
             "cualquier codificador RTMP, incluido SplitCam."),
            ("¿SplitCam es gratis para Stripchat?", "Sí — gratis, sin marca de agua, sin "
             "límites."),
            ("¿Qué bitrate para Stripchat?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
        ],
    },
    {
        "slug": "onlyfans", "name": "OnlyFans",
        "title": "Cómo emitir en directo en OnlyFans con SplitCam — OBS Key",
        "desc": "Emite en directo en OnlyFans con SplitCam gratis. Encuentra la OBS Key en "
                "Settings → Other, enrútala por SplitCam para escenas y superposiciones.",
        "kw": "cómo emitir en directo en onlyfans, onlyfans obs key, onlyfans directo, "
              "onlyfans software de emisión",
        "h1html": 'Cómo emitir en directo en <span class="accent">OnlyFans</span> con SplitCam',
        "h1short": "Directo en OnlyFans",
        "card": "Configuración de OBS Key para directos de OnlyFans.",
        "intro": "El directo de OnlyFans es para tus suscriptores, y la plataforma expone una "
                 "sola <strong style='color:var(--text)'>OBS Key</strong> — sin URL de "
                 "servidor. <strong style='color:var(--text)'>SplitCam</strong> gratis "
                 "convierte esa clave en una producción real: escenas con varias cámaras, "
                 "superposiciones y filtros.",
        "quick": "Emite en directo en OnlyFans con SplitCam: instala SplitCam, monta tu escena, "
                 "en OnlyFans abre <em>Profile → Settings → Other</em>, copia la OBS Key, pégala "
                 "en SplitCam, Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Copia tu OBS Key de OnlyFans.</li><li>Pégala en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "En OnlyFans, ve a <strong>Profile</strong> → <strong>Settings</strong> → la "
                   "sección <strong>Other</strong>. Copia el valor del campo <strong>OBS "
                   "Key</strong>. OnlyFans solo da esta clave — no hay URL de servidor aparte, "
                   "deja el campo de servidor de SplitCam por defecto.",
        "tips": [
            ("Solo OBS Key, sin URL de servidor", "A diferencia de la mayoría de sitios cam, "
             "OnlyFans expone solo una OBS Key en Settings → Other — no busques una URL."),
            ("Marca el stream para los clips", "Añade tu handle y objetivos como "
             "superposiciones — los clips de un directo de OnlyFans siguen reconocibles."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿Dónde está la OBS Key de OnlyFans?", "Profile → Settings → la sección Other — el "
             "campo se llama OBS Key."),
            ("¿OnlyFans admite software de emisión?", "Sí — el directo de OnlyFans acepta una "
             "clave tipo OBS, así que SplitCam funciona como codificador."),
            ("¿SplitCam es gratis para directos de OnlyFans?", "Sí — gratis, sin marca de agua, "
             "sin límite."),
            ("¿Qué bitrate para OnlyFans?", "3.500–6.000 Kbps a 1080p; haz el test primero."),
        ],
    },
    {
        "slug": "camplace", "name": "CamPlace",
        "title": "Cómo emitir en CamPlace con SplitCam — guía gratuita",
        "desc": "Emite en CamPlace con SplitCam gratis — codificador externo, escenas con "
                "varias cámaras, superposiciones y filtros. Paso a paso, sin marca de agua.",
        "kw": "cómo emitir en camplace, camplace software de emisión, camplace rtmp",
        "h1html": 'Cómo emitir en <span class="accent">CamPlace</span> con SplitCam',
        "h1short": "Emitir en CamPlace",
        "card": "Configuración del codificador externo para CamPlace.",
        "intro": "CamPlace es una plataforma de streaming cam. Enrutar tu emisión por "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis añade escenas con "
                 "varias cámaras, superposiciones, filtros y fondo con IA que una cámara de "
                 "navegador básica no puede.",
        "quick": "Emite en CamPlace con SplitCam: instala SplitCam, monta tu escena, activa la "
                 "emisión externa/RTMP en CamPlace, copia la URL del servidor y la clave, "
                 "pégalas en SplitCam, Go Live. La guía en vídeo de arriba lo muestra."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la clave RTMP de CamPlace.</li><li>Pégala en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en CamPlace y abre tus ajustes de emisión. Cambia a la opción "
                   "de codificador externo / RTMP / OBS para ver la <strong>URL del "
                   "servidor</strong> y la <strong>clave</strong>, copia ambas. La guía en "
                   "vídeo de arriba muestra la ruta exacta en la interfaz actual de CamPlace.",
        "tips": [
            ("Sigue la guía en vídeo", "La interfaz de CamPlace cambia con el tiempo — el vídeo "
             "de arriba muestra la ruta actual a los ajustes del codificador."),
            ("Superpón en SplitCam", "Objetivos de tokens, tu nombre y redes como capas de "
             "escena — la cámara básica de CamPlace no puede añadirlas."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿CamPlace admite codificadores externos?", "Sí — CamPlace acepta una clave RTMP, "
             "así que SplitCam funciona como codificador."),
            ("¿SplitCam es gratis para CamPlace?", "Sí — gratis, sin marca de agua, sin límite."),
            ("¿Qué bitrate para CamPlace?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
            ("¿Puedo usar dos cámaras en CamPlace?", "Sí — añade varias cámaras como fuentes de "
             "escena en SplitCam."),
        ],
    },
    {
        "slug": "camsoda", "name": "CamSoda",
        "title": "Cómo emitir en CamSoda con SplitCam — guía gratuita",
        "desc": "Emite en CamSoda con SplitCam gratis — codificador externo, escenas, "
                "superposiciones y filtros. Con guía en vídeo, sin marca de agua.",
        "kw": "cómo emitir en camsoda, camsoda live, camsoda software de emisión, camsoda rtmp",
        "h1html": 'Cómo emitir en <span class="accent">CamSoda</span> con SplitCam',
        "h1short": "Emitir en CamSoda",
        "card": "Configuración del codificador externo para CamSoda.",
        "intro": "CamSoda es una plataforma cam de EE. UU. conocida por formatos de show "
                 "novedosos e interactivos. <strong style='color:var(--text)'>SplitCam</strong> "
                 "gratis funciona como su codificador — escenas, superposiciones, filtros y "
                 "codificación por hardware para una emisión más cuidada.",
        "quick": "Emite en CamSoda con SplitCam: instala SplitCam, monta tu escena, activa el "
                 "OBS / codificador externo en CamSoda, copia la URL del servidor y la clave, "
                 "pégalas en SplitCam, Go Live. Mira la guía en vídeo de arriba."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la clave RTMP de CamSoda.</li><li>Pégala en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en CamSoda y abre tus ajustes de emisión. Elige la opción "
                   "<strong>OBS / codificador externo</strong> para obtener la URL del servidor "
                   "RTMP y la clave, copia ambas. La guía en vídeo de arriba muestra la ruta de "
                   "menú exacta de CamSoda.",
        "tips": [
            ("Mira la guía en vídeo", "La UI de emisión de CamSoda se sigue mejor visualmente — "
             "el vídeo de arriba muestra la ruta actual del codificador."),
            ("Produce, no solo apuntes una cámara", "CamSoda premia los shows distintivos — usa "
             "escenas y superposiciones de SplitCam para destacar."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿CamSoda admite codificadores externos?", "Sí — CamSoda acepta un stream "
             "RTMP/OBS, así que SplitCam funciona como codificador."),
            ("¿SplitCam es gratis para CamSoda?", "Sí — gratis, sin marca de agua, sin límite."),
            ("¿Qué bitrate para CamSoda?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
            ("¿Puedo multiemitir CamSoda?", "Sí — SplitCam puede emitir a varios sitios cam "
             "desde una sola codificación."),
        ],
    },
    {
        "slug": "streamate", "name": "Streamate",
        "title": "Cómo emitir en Streamate con SplitCam — canal integrado",
        "desc": "Emite en Streamate con SplitCam gratis. Streamate es un canal integrado en "
                "SplitCam: usa SM Connect, copia la clave, Add Channel → Streamate.",
        "kw": "cómo emitir en streamate, streamate sm connect, streamate rtmp, "
              "streamate software de emisión",
        "h1html": 'Cómo emitir en <span class="accent">Streamate</span> con SplitCam',
        "h1short": "Emitir en Streamate",
        "card": "Streamate es un canal integrado de SplitCam — setup rápido.",
        "intro": "Streamate es una plataforma cam consolidada — y es uno de los destinos "
                 "<strong style='color:var(--text)'>preconfigurados dentro de SplitCam</strong> "
                 "en la lista de canales, así que el setup es más rápido que un RTMP manual: "
                 "elige Streamate, pega la clave, listo.",
        "quick": "Emite en Streamate con SplitCam: instala SplitCam, monta tu escena, en "
                 "Streamate usa <em>SM Connect → Start Show</em> y copia la clave, luego en "
                 "SplitCam abre <em>Stream Settings → Add Channel → Streamate</em> y pégala."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la clave de Streamate vía SM Connect.</li>"
                 "<li>Add Channel → Streamate en SplitCam.</li><li>Pulsa Go Live.</li></ol>",
        "key_how": "En Streamate, abre <strong>SM Connect</strong>, acepta los términos, pulsa "
                   "<strong>Start Show</strong> a la izquierda y cierra la ventana que se abre "
                   "— luego copia tu clave de stream. En SplitCam, abre <strong>Stream "
                   "Settings</strong> → <strong>Add Channel</strong>, elige "
                   "<strong>Streamate</strong> de la lista y pega la clave.",
        "tips": [
            ("Streamate es un canal integrado", "No necesitas una URL RTMP manual — SplitCam "
             "tiene Streamate en su lista Add Channel, solo selecciónalo y pega la clave."),
            ("Cierra la ventana de SM Connect", "Tras Start Show, Streamate abre una ventana — "
             "ciérrala; solo la necesitabas para ver la clave."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿Streamate está integrado en SplitCam?", "Sí — Streamate aparece en la lista Add "
             "Channel de SplitCam, lo seleccionas en vez de escribir una URL RTMP."),
            ("¿Dónde está la clave de stream de Streamate?", "SM Connect → aceptar términos → "
             "Start Show → cerrar la ventana → copiar la clave."),
            ("¿SplitCam es gratis para Streamate?", "Sí — gratis, sin marca de agua, sin "
             "límite."),
            ("¿Qué bitrate para Streamate?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
        ],
    },
    {
        "slug": "streamray", "name": "StreamRay",
        "title": "Cómo emitir en StreamRay con SplitCam — URL desde el chat",
        "desc": "Emite en StreamRay con SplitCam gratis. StreamRay publica la URL del stream en "
                "la ventana de chat y no usa clave — SplitCam maneja ese flujo.",
        "kw": "cómo emitir en streamray, streamray obs broadcaster, streamray cam, streamray rtmp",
        "h1html": 'Cómo emitir en <span class="accent">StreamRay</span> con SplitCam',
        "h1short": "Emitir en StreamRay",
        "card": "Configuración de StreamRay — la URL viene del chat.",
        "intro": "StreamRay tiene un setup de codificador externo inusual — te entrega la URL "
                 "del stream dentro de la <strong style='color:var(--text)'>ventana de "
                 "chat</strong> y no usa clave aparte. "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis maneja bien ese "
                 "flujo de solo-URL.",
        "quick": "Emite en StreamRay con SplitCam: instala SplitCam, monta tu escena, en "
                 "StreamRay activa el OBS Broadcaster, copia la URL del stream desde la ventana "
                 "de chat, pégala en SplitCam (deja el campo de clave vacío), Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Copia la URL de StreamRay desde el chat.</li>"
                 "<li>Pega la URL en SplitCam.</li><li>Pulsa Go Live.</li></ol>",
        "key_how": "En StreamRay, pulsa <strong>Broadcast Now</strong> dos veces, abre el menú "
                   "<strong>Other</strong>, elige <strong>OBS Broadcaster</strong> y "
                   "<strong>Save and Close</strong>. StreamRay publica entonces tu <strong>URL "
                   "del stream en la ventana de chat</strong> — cópiala de ahí. Deja el campo "
                   "de clave de SplitCam <strong>vacío</strong>; StreamRay autentica por URL.",
        "tips": [
            ("La URL está en el chat", "StreamRay no muestra la URL en un cuadro de ajustes — "
             "la publica en la ventana de chat de tu emisión. Cópiala de ahí."),
            ("Deja la clave vacía", "StreamRay no usa clave aparte — solo la URL. No rellenes "
             "el campo de clave en SplitCam."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿Dónde está la URL del stream de StreamRay?", "Tras activar OBS Broadcaster, "
             "StreamRay publica la URL en la ventana de chat — cópiala del chat."),
            ("¿Por qué StreamRay no tiene clave de stream?", "StreamRay autentica solo por URL "
             "— deja el campo de clave de SplitCam vacío."),
            ("¿SplitCam es gratis para StreamRay?", "Sí — gratis, sin marca de agua, sin "
             "límite."),
            ("¿Qué bitrate para StreamRay?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
        ],
    },
    {
        "slug": "xlovecam", "name": "XLoveCam",
        "title": "Cómo emitir en XLoveCam con SplitCam — enlace RTMP y clave",
        "desc": "Emite en XLoveCam con SplitCam gratis. Encuentra el enlace RTMP y la clave en "
                "My Account → settings, lleva escenas y superposiciones. Sin marca de agua.",
        "kw": "cómo emitir en xlovecam, xlovecam rtmp, xlovecam stream key, x love cam",
        "h1html": 'Cómo emitir en <span class="accent">XLoveCam</span> con SplitCam',
        "h1short": "Emitir en XLoveCam",
        "card": "Enlace RTMP + clave para XLoveCam.",
        "intro": "XLoveCam es una plataforma cam europea y multilingüe. Sus ajustes de cuenta "
                 "exponen un <strong style='color:var(--text)'>enlace RTMP</strong> y una "
                 "<strong style='color:var(--text)'>clave de stream</strong> — "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis toma ambos y emite "
                 "con escenas y superposiciones completas.",
        "quick": "Emite en XLoveCam con SplitCam: instala SplitCam, monta tu escena, en "
                 "XLoveCam abre <em>My Account → settings</em>, copia el enlace RTMP y la "
                 "clave, pega ambos en SplitCam, inicia tu show."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Copia el enlace RTMP + clave de XLoveCam.</li>"
                 "<li>Pega ambos en SplitCam.</li><li>Pulsa Go Live.</li></ol>",
        "key_how": "En XLoveCam, abre <strong>My Account</strong> → <strong>settings</strong>. "
                   "Los ajustes contienen un <strong>enlace RTMP</strong> y una <strong>clave "
                   "de stream</strong> — copia ambos en los campos de URL y clave de SplitCam, "
                   "luego usa <strong>Start your show</strong> en XLoveCam.",
        "tips": [
            ("Copia enlace y clave", "XLoveCam da un enlace RTMP Y una clave aparte — necesitas "
             "ambos en SplitCam, no solo uno."),
            ("Audiencia multilingüe", "XLoveCam es europea y multilingüe — una superposición de "
             "texto clara en tu idioma ayuda a que los espectadores te encuentren."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿Dónde están los datos RTMP de XLoveCam?", "My Account → settings — muestra el "
             "enlace RTMP y la clave."),
            ("¿XLoveCam admite codificadores externos?", "Sí — da un enlace RTMP y clave, así "
             "que SplitCam funciona."),
            ("¿SplitCam es gratis para XLoveCam?", "Sí — gratis, sin marca de agua, sin límite."),
            ("¿Qué bitrate para XLoveCam?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
        ],
    },
    {
        "slug": "soulcams", "name": "SoulCams",
        "title": "Cómo emitir en SoulCams con SplitCam — ajustes OBS",
        "desc": "Emite en SoulCams con SplitCam gratis. Go Online → Settings → OBS muestra el "
                "servidor RTMP y la clave juntos. Escenas, superposiciones.",
        "kw": "cómo emitir en soulcams, soulcams obs, soul cams, soulcams rtmp",
        "h1html": 'Cómo emitir en <span class="accent">SoulCams</span> con SplitCam',
        "h1short": "Emitir en SoulCams",
        "card": "Configuración de SoulCams vía ajustes OBS.",
        "intro": "SoulCams es una plataforma cam cuyos ajustes OBS muestran el "
                 "<strong style='color:var(--text)'>servidor RTMP y la clave juntos</strong> en "
                 "una ventana. Pon ambos en <strong style='color:var(--text)'>SplitCam</strong> "
                 "gratis para emitir con escenas y superposiciones.",
        "quick": "Emite en SoulCams con SplitCam: instala SplitCam, monta tu escena, en "
                 "SoulCams pulsa Go Online → Settings → OBS, copia el servidor y la clave, pega "
                 "ambos en SplitCam, Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Abre SoulCams Settings → OBS.</li>"
                 "<li>Pega servidor y clave en SplitCam.</li><li>Pulsa Go Live.</li></ol>",
        "key_how": "En SoulCams, inicia sesión y pulsa <strong>Go Online</strong>, luego abre "
                   "<strong>Settings</strong> → <strong>OBS</strong>. La ventana OBS muestra el "
                   "<strong>servidor RTMP</strong> y la <strong>clave</strong> juntos — copia "
                   "ambos en SplitCam.",
        "tips": [
            ("Servidor y clave, lado a lado", "SoulCams muestra el servidor RTMP y la clave en "
             "la misma ventana OBS — toma ambos de una vez."),
            ("Go Online primero", "Los ajustes OBS solo aparecen tras pulsar Go Online en "
             "SoulCams — hazlo antes de buscar los datos del codificador."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿Dónde están los ajustes OBS de SoulCams?", "Inicia sesión, pulsa Go Online, "
             "luego Settings → OBS — el servidor RTMP y la clave se muestran juntos."),
            ("¿SoulCams admite codificadores externos?", "Sí — sus ajustes OBS dan un servidor "
             "RTMP y clave, así que SplitCam funciona."),
            ("¿SplitCam es gratis para SoulCams?", "Sí — gratis, sin marca de agua, sin límite."),
            ("¿Qué bitrate para SoulCams?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
        ],
    },
    {
        "slug": "imlive", "name": "ImLive",
        "title": "Cómo usar SplitCam en ImLive — cámara virtual",
        "desc": "ImLive usa tu webcam directamente — sin RTMP. Conecta SplitCam como cámara "
                "virtual para que tus escenas, superposiciones y filtros salgan en ImLive.",
        "kw": "cómo emitir en imlive, imlive splitcam, imlive cámara virtual, imlive webcam",
        "h1html": 'Cómo usar <span class="accent">ImLive</span> con SplitCam',
        "h1short": "Usar SplitCam en ImLive",
        "card": "Cámara virtual para ImLive — sin RTMP.",
        "intro": "ImLive usa tu webcam directamente en el navegador — <strong "
                 "style='color:var(--text)'>no hay RTMP ni clave de stream</strong>. "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis se conecta como "
                 "<strong style='color:var(--text)'>cámara virtual</strong>: monta tu escena en "
                 "SplitCam y luego elige SplitCam como cámara dentro de ImLive.",
        "quick": "Usa SplitCam en ImLive: instala SplitCam, monta tu escena con capas de medios, "
                 "abre ImLive e inicia un videochat, en los ajustes de ImLive elige SplitCam "
                 "como webcam y micrófono."
                 "<ol><li>Instala SplitCam.</li><li>Monta tu escena en SplitCam.</li>"
                 "<li>Inicia un videochat en ImLive.</li>"
                 "<li>Elige SplitCam como cámara de ImLive.</li><li>Inicia el chat.</li></ol>",
        "steps": [
            ("Instala SplitCam",
             "SplitCam es software gratuito para Windows y macOS. Instálalo — sin marca de "
             "agua, sin registro. En ImLive funciona como <strong>cámara virtual</strong>, no "
             "como codificador RTMP."),
            ("Monta tu escena en SplitCam",
             "Abre SplitCam y usa <strong>Media Layers +</strong> para añadir tu webcam más "
             "superposiciones, texto, filtros o fondo con IA. Esa escena compuesta es lo que "
             "ImLive verá como tu cámara."),
            ("Inicia un videochat en ImLive",
             "Ve al sitio de ImLive y pulsa <strong>Start Video Chat</strong>, luego abre "
             "<strong>Go To Settings</strong> para llegar a las opciones de cámara y micrófono."),
            ("Elige SplitCam como tu cámara",
             "En los ajustes de ImLive, elige <strong>SplitCam</strong> como webcam y como "
             "micrófono. ImLive mostrará tu escena completa de SplitCam en vez de una webcam "
             "plana."),
            ("Inicia tu Free Live Chat",
             "Pulsa <strong>Free Live Chat</strong> en ImLive para emitir. Para cambiar tu "
             "aspecto en directo, edita la escena en SplitCam — se actualiza en ImLive al "
             "instante."),
        ],
        "tips": [
            ("No necesitas clave de stream", "ImLive no tiene RTMP — no busques URL ni clave. "
             "SplitCam solo se selecciona como dispositivo de cámara."),
            ("Pon SplitCam también de micrófono", "Elige SplitCam para el micrófono además de "
             "la cámara para que tu mezcla de audio y supresión de ruido pasen al directo."),
            ("Monta la escena antes de emitir", "ImLive muestra lo que SplitCam emita — ordena "
             "tus capas antes de iniciar el chat."),
            _T_TEST,
        ],
        "faq": [
            ("¿ImLive usa RTMP o clave de stream?", "No — ImLive usa tu webcam directamente. "
             "SplitCam se conecta como cámara virtual, no hay clave que copiar."),
            ("¿Cómo elijo SplitCam en ImLive?", "Start Video Chat → Go To Settings → elige "
             "SplitCam como webcam y micrófono."),
            ("¿SplitCam es gratis para ImLive?", "Sí — gratis, sin marca de agua, sin límite."),
            ("¿Puedo usar superposiciones en ImLive?", "Sí — móntalas en la escena de SplitCam; "
             "ImLive muestra el resultado compuesto."),
        ],
    },
    {
        "slug": "vxlive", "name": "VXLive",
        "title": "Cómo emitir en VXLive con SplitCam — guía gratuita",
        "desc": "Emite en VXLive con SplitCam gratis — codificador externo, escenas, "
                "superposiciones y filtros. Con guía en vídeo, sin marca de agua.",
        "kw": "cómo emitir en vxlive, vxlive software de emisión, vxlive rtmp",
        "h1html": 'Cómo emitir en <span class="accent">VXLive</span> con SplitCam',
        "h1short": "Emitir en VXLive",
        "card": "Configuración del codificador externo para VXLive.",
        "intro": "VXLive es una plataforma cam del mercado alemán. "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis funciona como su "
                 "codificador — escenas con varias cámaras, superposiciones, filtros y "
                 "codificación por hardware para una emisión más limpia.",
        "quick": "Emite en VXLive con SplitCam: instala SplitCam, monta tu escena, activa el "
                 "codificador externo en VXLive, copia la URL del servidor y la clave, pégalas "
                 "en SplitCam, Go Live. La guía en vídeo de arriba muestra la ruta."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la clave RTMP de VXLive.</li><li>Pégala en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en VXLive y abre tus ajustes de emisión. Elige la opción "
                   "<strong>codificador externo / RTMP</strong> para obtener la URL del "
                   "servidor y la clave, copia ambas. La guía en vídeo de arriba muestra la "
                   "ruta exacta de VXLive.",
        "tips": [
            ("Plataforma del mercado alemán", "La audiencia de VXLive es mayormente "
             "germanoparlante — una superposición o título en alemán ayuda a conectar."),
            ("Sigue la guía en vídeo", "La UI de emisión de VXLive se sigue mejor visualmente — "
             "el vídeo de arriba muestra la ruta actual del codificador."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿VXLive admite codificadores externos?", "Sí — VXLive acepta un stream RTMP/OBS, "
             "así que SplitCam funciona como codificador."),
            ("¿SplitCam es gratis para VXLive?", "Sí — gratis, sin marca de agua, sin límite."),
            ("¿Qué bitrate para VXLive?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
            ("¿Puedo multiemitir VXLive?", "Sí — SplitCam puede emitir a varios sitios cam a la "
             "vez desde una codificación."),
        ],
    },
    {
        "slug": "virtwish", "name": "VirtWish",
        "title": "Cómo emitir en VirtWish con SplitCam — URL del stream y clave",
        "desc": "Emite en VirtWish con SplitCam gratis. Profile → Start Broadcast → la sección "
                "OBS da la URL del stream y la clave. Escenas, superposiciones.",
        "kw": "cómo emitir en virtwish, virtwish software de emisión, virtwish rtmp, virtwish obs",
        "h1html": 'Cómo emitir en <span class="accent">VirtWish</span> con SplitCam',
        "h1short": "Emitir en VirtWish",
        "card": "URL del stream + clave para VirtWish.",
        "intro": "VirtWish es una plataforma cam interactiva. Sus ajustes de emisión te dan una "
                 "<strong style='color:var(--text)'>URL del stream y una clave aparte</strong> "
                 "en una sección OBS — <strong style='color:var(--text)'>SplitCam</strong> "
                 "gratis toma ambas y lleva el show con escenas y superposiciones.",
        "quick": "Emite en VirtWish con SplitCam: instala SplitCam, monta tu escena, en "
                 "VirtWish abre <em>Profile → Start Broadcast</em> hasta la sección OBS, copia "
                 "el enlace y la clave, pega ambos en SplitCam, Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la URL + clave de VirtWish.</li>"
                 "<li>Pega ambos en SplitCam.</li><li>Pulsa Go Live.</li></ol>",
        "key_how": "En VirtWish, pulsa el icono arriba a la derecha → <strong>Profile</strong> "
                   "→ <strong>Start Broadcast</strong>, luego <strong>Start Broadcast</strong> "
                   "otra vez para llegar a la sección OBS. <strong>Copia el enlace de la "
                   "primera línea</strong> en el campo Stream URL de SplitCam, y copia la "
                   "<strong>Stream Key</strong> aparte en el campo de clave.",
        "tips": [
            ("El enlace está en la primera línea", "La sección OBS de VirtWish pone la URL del "
             "stream en la primera línea — cópiala en Stream URL de SplitCam, luego la clave."),
            ("Dos clics de Start Broadcast", "Pulsas Start Broadcast dos veces en VirtWish para "
             "llegar a la sección OBS — es lo esperado, no un fallo."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿Dónde están los datos RTMP de VirtWish?", "Icono arriba a la derecha → Profile → "
             "Start Broadcast dos veces → la sección OBS muestra el enlace y la clave."),
            ("¿VirtWish admite codificadores externos?", "Sí — su sección OBS da una URL de "
             "stream y clave, así que SplitCam funciona."),
            ("¿SplitCam es gratis para VirtWish?", "Sí — gratis, sin marca de agua, sin límite."),
            ("¿Qué bitrate para VirtWish?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
        ],
    },
    {
        "slug": "xmodels", "name": "XModels",
        "title": "Cómo emitir en XModels con SplitCam — guía gratuita",
        "desc": "Emite en XModels con SplitCam gratis — codificador externo, escenas, "
                "superposiciones y filtros. Con guía en vídeo, sin marca de agua.",
        "kw": "cómo emitir en xmodels, xmodels software de emisión, xmodels rtmp",
        "h1html": 'Cómo emitir en <span class="accent">XModels</span> con SplitCam',
        "h1short": "Emitir en XModels",
        "card": "Configuración del codificador externo para XModels.",
        "intro": "XModels es una plataforma de streaming cam. Con "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis emites con escenas "
                 "de varias cámaras, superposiciones, filtros y fondo con IA en vez de una sola "
                 "cámara plana.",
        "quick": "Emite en XModels con SplitCam: instala SplitCam, monta tu escena, activa el "
                 "codificador externo en XModels, copia la URL del servidor y la clave, pégalas "
                 "en SplitCam, Go Live. Mira la guía en vídeo de arriba."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la clave RTMP de XModels.</li><li>Pégala en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en XModels y abre tus ajustes de emisión. Cambia a la opción "
                   "<strong>codificador externo / RTMP</strong> para ver la URL del servidor y "
                   "la clave, copia ambas. La guía en vídeo de arriba recorre la ruta actual de "
                   "XModels.",
        "tips": [
            ("Sigue la guía en vídeo", "El vídeo de arriba muestra la ruta actual a los ajustes "
             "del codificador de XModels — las interfaces cambian con el tiempo."),
            ("Superpón en SplitCam", "Objetivos de tokens, tu nombre y redes como capas de "
             "escena — la cámara básica de XModels no puede añadirlas."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿XModels admite codificadores externos?", "Sí — XModels acepta un stream RTMP/OBS, "
             "así que SplitCam funciona como codificador."),
            ("¿SplitCam es gratis para XModels?", "Sí — gratis, sin marca de agua, sin límite."),
            ("¿Qué bitrate para XModels?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
            ("¿Puedo usar dos cámaras en XModels?", "Sí — añade varias cámaras como fuentes de "
             "escena en SplitCam."),
        ],
    },
    {
        "slug": "flirt4free", "name": "Flirt4Free",
        "title": "Cómo emitir en Flirt4Free con SplitCam — guía gratuita",
        "desc": "Emite en Flirt4Free con SplitCam gratis — codificador externo, escenas, "
                "superposiciones y filtros. Con guía en vídeo, sin marca de agua.",
        "kw": "cómo emitir en flirt4free, flirt4free software de emisión, flirt4free rtmp",
        "h1html": 'Cómo emitir en <span class="accent">Flirt4Free</span> con SplitCam',
        "h1short": "Emitir en Flirt4Free",
        "card": "Configuración del codificador externo para Flirt4Free.",
        "intro": "Flirt4Free es una de las plataformas cam más longevas, online desde los años "
                 "90. <strong style='color:var(--text)'>SplitCam</strong> gratis funciona como "
                 "su codificador — escenas, superposiciones y filtros para una emisión pulida y "
                 "de aspecto moderno.",
        "quick": "Emite en Flirt4Free con SplitCam: instala SplitCam, monta tu escena, activa "
                 "el codificador externo en el área de modelo de Flirt4Free, copia la URL del "
                 "servidor y la clave, pégalas en SplitCam, Go Live. La guía en vídeo lo muestra."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la clave RTMP de Flirt4Free.</li><li>Pégala en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en el área de modelo de Flirt4Free y abre tus ajustes de "
                   "emisión. Elige la opción <strong>codificador externo / RTMP</strong> para "
                   "obtener la URL del servidor y la clave, copia ambas. La guía en vídeo de "
                   "arriba muestra los pasos exactos.",
        "tips": [
            ("Una plataforma consolidada", "Flirt4Free funciona desde los años 90 — sus "
             "herramientas de modelo son maduras; la opción de codificador externo está en los "
             "ajustes de emisión."),
            ("Sigue la guía en vídeo", "El vídeo de arriba muestra la ruta actual al "
             "codificador de Flirt4Free."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("¿Flirt4Free admite codificadores externos?", "Sí — Flirt4Free acepta un stream "
             "RTMP/OBS, así que SplitCam funciona como codificador."),
            ("¿SplitCam es gratis para Flirt4Free?", "Sí — gratis, sin marca de agua, sin "
             "límite."),
            ("¿Qué bitrate para Flirt4Free?", "3.500–6.000 Kbps a 1080p; comprueba tu subida."),
            ("¿Puedo multiemitir Flirt4Free?", "Sí — SplitCam puede emitir a varios sitios cam "
             "a la vez."),
        ],
    },
    {
        "slug": "mfc-alerts", "name": "MFC Alerts",
        "title": "Cómo añadir MFC Alerts a tu emisión con SplitCam",
        "desc": "Muestra alertas animadas de propinas en tu emisión de MyFreeCams. Añade tu URL "
                "de mfcalerts.com como capa Browser en SplitCam — encima de la webcam.",
        "kw": "mfc alerts, cómo añadir mfc alerts, myfreecams alertas de propinas, mfcalerts splitcam",
        "h1html": 'Cómo añadir <span class="accent">MFC Alerts</span> a tu emisión',
        "h1short": "Añadir MFC Alerts",
        "card": "Muestra alertas animadas de propinas en tu emisión de MyFreeCams.",
        "intro": "MFC Alerts muestra efectos animados en tu emisión de MyFreeCams cada vez que "
                 "un espectador da propina. Funciona como una "
                 "<strong style='color:var(--text)'>capa Browser</strong> dentro de "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis — configúralo una "
                 "vez y las propinas disparan reacciones en pantalla en directo.",
        "quick": "Añade MFC Alerts con SplitCam: instala SplitCam, añade tu webcam, abre la "
                 "pestaña Browser y carga mfcalerts.com, copia tu URL de alertas, añádela como "
                 "capa Browser encima de la webcam, prueba con una propina de prueba."
                 "<ol><li>Instala SplitCam.</li><li>Añade tu webcam.</li>"
                 "<li>Consigue tu URL en mfcalerts.com.</li>"
                 "<li>Añádela como capa Browser encima de la webcam.</li>"
                 "<li>Envía una propina de prueba.</li></ol>",
        "steps": [
            ("Instala SplitCam y añade tu webcam",
             "Instala SplitCam gratis para Windows o macOS, luego añade tu <strong>webcam</strong> "
             "como fuente. MFC Alerts irá como capa encima de esta cámara."),
            ("Abre la pestaña Browser y ve a mfcalerts.com",
             "En SplitCam, abre la pestaña <strong>Browser</strong> y navega a "
             "<strong>www.mfcalerts.com</strong>. Inicia sesión, o regístrate si aún no tienes "
             "cuenta en mfcalerts.com."),
            ("Copia tu URL de alertas",
             "En mfcalerts.com, usa <strong>Copy to clipboard</strong> para copiar tu URL "
             "personal de alertas — es la página que renderiza las animaciones de propinas."),
            ("Añade la URL como capa Browser — encima de la webcam",
             "Pega la URL en la ventana Browser de SplitCam y pulsa <strong>Add</strong>. Luego "
             "reordena la lista de fuentes para que <strong>MFC Alerts quede encima de tu "
             "webcam</strong> (menú de 3 puntos → Move Up). Si está debajo, los efectos no se "
             "ven."),
            ("Prueba con una propina de prueba",
             "Abre <strong>Settings → Send test tip</strong> y confirma que el efecto aparece "
             "sobre tu cámara. Luego emite a MyFreeCams como siempre — las propinas reales "
             "disparan las animaciones."),
        ],
        "tips": [
            ("MFC Alerts debe ir encima de la webcam", "El error más común: si la capa MFC "
             "Alerts está debajo de la webcam en la lista de fuentes, los efectos se ocultan. "
             "Súbela."),
            ("Necesitas cuenta en mfcalerts.com", "La URL de alertas es personal — regístrate "
             "primero en mfcalerts.com si no tienes cuenta."),
            ("Envía una propina de prueba antes", "Usa Settings → Send test tip para confirmar "
             "que la superposición funciona — no lo descubras a mitad del show."),
            _T_ETH,
        ],
        "faq": [
            ("¿Qué es MFC Alerts?", "Un sistema de notificaciones para MyFreeCams que muestra "
             "efectos de vídeo en tu emisión cuando los espectadores dan propina — añadido como "
             "superposición Browser en SplitCam."),
            ("¿Por qué no se ven mis MFC Alerts?", "Casi siempre el orden de capas — la capa "
             "Browser de MFC Alerts debe ir encima de la webcam en la lista de fuentes."),
            ("¿Necesito cuenta para MFC Alerts?", "Sí — regístrate en mfcalerts.com para "
             "obtener tu URL personal de alertas."),
            ("¿SplitCam es gratis para esto?", "Sí — SplitCam es gratis, sin marca de agua, "
             "sin límites."),
        ],
    },
    {
        "slug": "lovense", "name": "Lovense",
        "title": "Cómo añadir un juguete Lovense a tu emisión con SplitCam",
        "desc": "Conecta un juguete interactivo Lovense a tu emisión cam y muestra su estado en "
                "pantalla con SplitCam gratis. Paso a paso, sin marca de agua.",
        "kw": "cómo añadir lovense a la emisión, lovense cam stream, lovense splitcam, "
              "juguete interactivo lovense streaming",
        "h1html": 'Cómo añadir un <span class="accent">juguete Lovense</span> a tu emisión',
        "h1short": "Añadir un juguete Lovense",
        "card": "Conecta un juguete interactivo Lovense a tu emisión cam.",
        "intro": "Emite con <strong style='color:var(--text)'>SplitCam</strong> gratis y vincula "
                 "un juguete interactivo <strong style='color:var(--text)'>Lovense</strong> "
                 "para que reaccione a los tokens — con el estado visible en pantalla.",
        "quick": "Para añadir un juguete Lovense a tu emisión: instala SplitCam y el software "
                 "de Lovense, vincula el juguete, conecta Lovense a tu plataforma cam, añade el "
                 "estado de Lovense como capa Browser en SplitCam y emite normalmente."
                 "<ol><li>Instala SplitCam.</li><li>Instala y vincula el software de Lovense.</li>"
                 "<li>Conecta Lovense a tu sitio cam.</li>"
                 "<li>Añade la superposición de Lovense en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "steps": [
            ("Instala SplitCam",
             "SplitCam es software de streaming gratuito para Windows y macOS — el codificador "
             "que envía tu vídeo a tu plataforma cam. Instálalo; sin marca de agua."),
            ("Instala y vincula el software de Lovense",
             "Instala la app oficial Lovense Connect / Lovense Stream. Enciende tu juguete y "
             "vincúlalo por Bluetooth hasta que la app lo muestre conectado."),
            ("Conecta Lovense a tu plataforma cam",
             "En la app de Lovense, conecta tu cuenta del sitio cam para que el juguete "
             "reaccione a los tokens y propinas de los espectadores."),
            ("Añade la superposición de Lovense en SplitCam",
             "Lovense ofrece una URL de widget. Añádela como capa <strong>Browser</strong> en "
             "tu escena de SplitCam para que los espectadores vean el estado del juguete."),
            ("Monta tu escena y emite",
             "Añade tu cámara y otras superposiciones, pega la clave RTMP de tu plataforma cam "
             "en SplitCam y pulsa <strong>Go Live</strong>. El juguete reacciona en tiempo "
             "real."),
        ],
        "tips": [
            ("Carga el juguete", "Una batería agotada a mitad de show mata la parte "
             "interactiva — cárgalo del todo antes de emitir."),
            ("Prueba la reacción", "Envía una pequeña propina de prueba para confirmar que el "
             "juguete reacciona antes de abrir la sala."),
            ("Muestra la superposición", "Un estado de Lovense visible indica a los "
             "espectadores que dar propina hace algo — genera más propinas."),
            ("Bluetooth estable", "Mantén el juguete cerca del PC para evitar cortes."),
        ],
        "faq": [
            ("¿SplitCam es gratis para esto?", "Sí — SplitCam es gratis y sin marca de agua. El "
             "software de Lovense también es gratuito."),
            ("¿El juguete se conecta directo a SplitCam?", "No — el juguete se vincula con la "
             "app de Lovense; SplitCam muestra la superposición y emite tu cámara."),
            ("¿Qué sitios cam admiten Lovense?", "La mayoría de las grandes plataformas cam se "
             "integran con Lovense — consulta la lista en la app de Lovense."),
            ("¿Puedo mostrar propinas recientes en pantalla?", "Sí — añade la URL del widget de "
             "Lovense como capa Browser en SplitCam."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Varios sitios cam",
        "title": "Cómo emitir en varios sitios cam a la vez con SplitCam",
        "desc": "Emite en MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat y más al mismo "
                "tiempo con la multiemisión gratuita de SplitCam. Sin marca de agua.",
        "kw": "emitir en varios sitios cam, multiemisión cam, emitir en chaturbate y bongacams "
              "a la vez, software de multiemisión cam",
        "h1html": 'Cómo emitir en <span class="accent">varios sitios cam</span> a la vez',
        "h1short": "Multiemisión cam",
        "card": "Emite en varios sitios cam simultáneamente.",
        "intro": "<strong style='color:var(--text)'>SplitCam</strong> gratis puede emitir un "
                 "solo stream a <strong style='color:var(--text)'>varios sitios cam a la "
                 "vez</strong> — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat y más. Sin "
                 "marca de agua, con un clic.",
        "quick": "Para emitir en varios sitios cam a la vez: instala SplitCam, monta tu escena, "
                 "consigue la URL del servidor RTMP y la clave de cada sitio cam, añádelas "
                 "todas en los ajustes de multiemisión de SplitCam, pulsa Go Live una vez."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue una clave RTMP de cada sitio cam.</li>"
                 "<li>Añade todas las claves en la multiemisión.</li>"
                 "<li>Pulsa Go Live una vez.</li></ol>",
        "steps": [
            ("Instala SplitCam",
             "SplitCam es software de streaming gratuito para Windows y macOS con multiemisión "
             "integrada. Instálalo — sin marca de agua ni registro."),
            ("Configura tu cámara y escena",
             "Abre SplitCam, añade tu webcam y monta la escena con superposiciones y filtros. "
             "Una escena alimenta todos los destinos."),
            ("Consigue una clave RTMP de cada sitio cam",
             "En cada plataforma cam, activa la emisión externa / RTMP y copia su <strong>URL "
             "de servidor</strong> y su <strong>clave</strong>. Repite para cada sitio — las "
             "rutas exactas están en las guías individuales de cada plataforma."),
            ("Añade cada destino en SplitCam",
             "Abre <strong>Stream Settings</strong> y añade cada sitio cam como destino RTMP "
             "personalizado — pega su URL y clave. Marca todos los que quieras emitir."),
            ("Pulsa Go Live una vez",
             "Pulsa <strong>Go Live</strong>. SplitCam envía tu stream a todos los sitios cam "
             "seleccionados a la vez, peer-to-peer, desde una codificación — sin coste extra."),
        ],
        "tips": [
            ("Cuida tu subida", "La multiemisión multiplica la carga de subida. Cada destino "
             "consume su propio bitrate — asegúrate de que tu conexión soporta el total."),
            ("Revisa las reglas de cada sitio", "Algunos sitios cam restringen emitir a la vez "
             "en otro lado — confírmalo antes de multiemitir."),
            _T_ETH,
            ("Monitor de estado", "SplitCam muestra el estado por destino — quita un sitio si "
             "tu subida no da abasto."),
        ],
        "faq": [
            ("¿La multiemisión es gratis en SplitCam?", "Sí — la multiemisión está integrada y "
             "es gratis, sin coste por destino ni marca de agua."),
            ("¿A cuántos sitios cam puedo emitir a la vez?", "A tantos como soporte tu ancho de "
             "banda de subida — cada destino consume su propio bitrate."),
            ("¿Usa un relé en la nube?", "No — SplitCam envía los streams peer-to-peer "
             "directamente desde tu PC al servidor de cada plataforma."),
            ("¿La multiemisión ralentiza mi PC?", "La codificación se hace una vez y se "
             "reutiliza; la codificación por hardware mantiene baja la carga de CPU."),
        ],
    },
]
