# -*- coding: utf-8 -*-
"""Spanish content for cam-streaming-guides. Genuinely per-platform, FAQ-enriched."""

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
            ("Mucho margen de calidad", "El ingest RTMP de Chaturbate acepta hasta 4K, 60 fps y "
             "un bitrate muy alto — el límite es tu subida, no la plataforma. Usa un intervalo "
             "de fotogramas clave de 2 segundos."),
            ("Baja latencia por diseño", "Chaturbate entrega tu stream por HLS de baja latencia "
             "— unos 2–4 segundos de extremo a extremo —, así las propinas y reacciones de la "
             "audiencia van al ritmo de lo que haces en cámara."),
            ("Cable para el margen 4K", "Chaturbate acepta bitrates muy altos, así que "
             "enviarás muchos datos — un enlace Ethernet por cable mantiene ese stream "
             "estable donde el Wi-Fi perdería fotogramas."),
            ("Prueba la sala en privado primero", "Chaturbate te deja emitir antes de salir "
             "en público — haz una comprobación privada corta de cámara, audio y "
             "superposiciones."),
        ],
        "faq": [
            ("¿Chaturbate permite OBS / codificadores externos?", "Sí — Chaturbate admite "
             "oficialmente codificadores externos y tiene su artículo \"How do I set up OBS?\". "
             "Se activa con \"Use External Encoder to Broadcast\" en los ajustes de emisión."),
            ("¿Dónde está mi clave de stream de Chaturbate?", "Broadcast Yourself → My Broadcast "
             "→ View RTMP/OBS broadcast information and stream key. La clave es tu token."),
            ("¿Qué resolución y fps admite Chaturbate?", "El ingest RTMP de Chaturbate acepta "
             "hasta 3840×2160 (4K) y 60 fps con un intervalo de fotogramas clave de 2 segundos "
             "— mucho más margen que la mayoría de plataformas cam."),
            ("¿Qué bitrate para Chaturbate?", "3.500–6.000 Kbps a 1080p sobra. El techo de "
             "Chaturbate es muy alto, así que tu subida es el límite real — haz el test de "
             "velocidad de SplitCam primero."),
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
            ("Bitrate más bajo de lo normal", "El ingest de CAM4 limita el bitrate de vídeo a "
             "unos 3.000 Kbps — más bajo que la mayoría de sitios cam. No subas más."),
            ("Usa el preset oficial de CAM4", "La guía OBS de CAM4 indica CBR, intervalo de "
             "fotograma clave de 1 segundo y el preset x264 veryfast/superfast con "
             "tune=zerolatency y B-frames a 0 — y recomienda activar «cambiar el bitrate "
             "dinámicamente». Haz primero el test de conexión en speedtest.xcdnpro.com."),
            ("El cable gana al Wi-Fi en CAM4", "El ingest de CAM4 va por niveles según el "
             "ancho de banda — un enlace por cable mantiene un nivel estable en vez de bajar "
             "tu resolución en cada bajón de Wi-Fi."),
            ("Prueba cámara y geo-ajustes", "Haz una emisión privada corta en CAM4 para "
             "revisar cámara, audio y geo-restricciones antes de abrir la sala."),
        ],
        "faq": [
            ("¿CAM4 admite oficialmente OBS / codificadores externos?", "Sí — CAM4 tiene una "
             "guía oficial de OBS en su sitio de soporte y recomienda la opción External "
             "Encoder. SplitCam usa la misma ruta RTMP."),
            ("¿Puedo geo-bloquear mi emisión de CAM4?", "Sí — CAM4 tiene geo-restricción "
             "integrada para ocultar tu emisión en ciertos países. Se ajusta en CAM4."),
            ("¿Dónde está la clave de stream de CAM4?", "Broadcast → Broadcast & Earn Money → "
             "Start Broadcast → External Encoder → Get Stream Key."),
            ("¿Qué bitrate para CAM4?", "Más bajo que en otros sitios — el ingest de CAM4 "
             "limita el vídeo a unos 3.000 Kbps a 30 fps con fotograma clave de 1 segundo. La "
             "guía OBS oficial de CAM4 trae una tabla por test de velocidad; no pases de ~3.000."),
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
            ("Un fotograma perdido es una propina perdida", "En un show largo en BongaCams, "
             "la inestabilidad del Wi-Fi te cuesta propinas — lleva un cable Ethernet al PC "
             "de emisión."),
            ("Prueba cuando soporte active la codificación", "Cuando BongaCams active la "
             "codificación externa, haz una emisión privada corta para confirmar cámara, "
             "audio y superposiciones."),
        ],
        "faq": [
            ("¿Por qué falta el botón External Encoder en BongaCams?", "La codificación externa "
             "no está activada para toda cuenta — contacta con soporte de BongaCams y el botón "
             "aparecerá en Broadcast settings."),
            ("¿Necesito verificar mi cuenta en BongaCams?", "Sí — para emitir hay que ser mayor "
             "de 18, tener un documento de identidad válido para verificar la edad y pasar la "
             "aprobación de la cuenta antes de salir en directo."),
            ("¿Qué bitrate para BongaCams?", "El ingest RTMP de BongaCams limita el vídeo a "
             "unos 6.000 Kbps con fotograma clave de 2 segundos — 3.500–6.000 a 1080p es ideal; "
             "comprueba tu subida primero."),
            ("¿SplitCam es gratis para BongaCams?", "Sí — totalmente gratis, sin marca de "
             "agua ni límite de tiempo, así que el codificador nunca se come tus ingresos de "
             "tokens en BongaCams ni limita la duración del show."),
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
            ("Iguala exactamente la resolución del sitio", "El FAQ de Stripchat advierte que la "
             "resolución de tu software debe coincidir exactamente con la del sitio, o el vídeo "
             "se pixela. Pon la misma en ambos."),
            ("Atento al mínimo de 2 Mbps", "Stripchat indica 2 Mbps de subida como mínimo — y "
             "explícitamente no es suficiente para emitir con OBS ni para multiemisión "
             "simultánea. Apunta muy por encima."),
            ("La clave es un token", "La clave de Stripchat es un token — cópiala exacta, no la "
             "compartas, reiníciala si se filtra."),
            ("Por cable y muy por encima de 2 Mbps", "El mínimo de 2 Mbps de Stripchat no "
             "basta para emitir con codificador — un enlace por cable más margen real sobre "
             "ese mínimo mantienen el show fluido."),
        ],
        "faq": [
            ("¿Stripchat recomienda OBS / software externo?", "Sí — el propio FAQ de Stripchat "
             "aconseja software externo como OBS \"para lograr mejor calidad de vídeo y audio\". "
             "SplitCam funciona igual."),
            ("¿Cómo cambio Stripchat a software externo?", "En el Broadcast Center elige Switch "
             "to External Broadcast Software (OBS), luego abre los ajustes de software externo "
             "para ver la clave (token)."),
            ("¿Qué bitrate para Stripchat?", "Su ingest RTMP acepta hasta ~6.000 Kbps con "
             "fotograma clave de 2 segundos. 3.500–6.000 a 1080p es ideal — pero necesitas muy "
             "por encima del mínimo de 2 Mbps, sobre todo emitiendo con OBS."),
            ("¿SplitCam es gratis para Stripchat?", "Sí — sin cuota de licencia, marca de "
             "agua ni límite de tiempo, así que incluso los shows interactivos largos en "
             "Stripchat no cuestan nada del lado del codificador."),
        ],
    },
    {
        "slug": "onlyfans", "name": "OnlyFans",
        "title": "Cómo emitir en directo en OnlyFans con SplitCam — autorización o clave",
        "desc": "Emite en directo en OnlyFans con SplitCam gratis. Conecta por autorización "
                "(inicia sesión una vez y la clave se sincroniza sola) o pega la OBS Key a "
                "mano — escenas, superposiciones, sin marca de agua.",
        "kw": "cómo emitir en directo en onlyfans, onlyfans autorización splitcam, "
              "onlyfans obs key, onlyfans software de emisión",
        "h1html": 'Cómo emitir en directo en <span class="accent">OnlyFans</span> con SplitCam',
        "h1short": "Directo en OnlyFans",
        "card": "Autoriza una vez o pega la clave — directo en OnlyFans.",
        "intro": "El directo de OnlyFans es para tus suscriptores. SplitCam conecta de "
                 "<strong style='color:var(--text)'>dos formas</strong> — inicia sesión una vez "
                 "con tu cuenta de OnlyFans y SplitCam obtiene la clave de stream y la mantiene "
                 "sincronizada automáticamente, o pega la OBS Key a mano. En ambos casos emites "
                 "con escenas de varias cámaras, superposiciones y filtros.",
        "quick": "Emite en directo en OnlyFans con SplitCam: instala SplitCam, monta tu escena, "
                 "abre Stream Settings &rarr; Add Channel &rarr; OnlyFans y elige "
                 "<em>Autorización</em> — inicia sesión con tu cuenta de OnlyFans y SplitCam "
                 "obtiene la clave automáticamente — luego pulsa Go Live. Con la cuenta "
                 "conectada puedes cambiar los ajustes de OnlyFans dentro de SplitCam, sin "
                 "abrir el sitio de OnlyFans.",
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software de streaming gratuito para Windows y macOS — sin registro, "
             "sin tarjeta, sin marca de agua. Es el codificador que envía tu vídeo a OnlyFans."),
            ("Configura tu cámara y escena",
             "Abre SplitCam y añade tu webcam. Monta la escena que verán los espectadores — "
             "superposiciones, texto, una segunda cámara, filtros de belleza o un fondo con "
             "IA, aplicados en directo."),
            ("Conexión — Método 1: Autorización (recomendado)",
             "En SplitCam abre <strong>Stream Settings</strong> &rarr; <strong>Add "
             "Channel</strong> &rarr; <strong>OnlyFans</strong> y elige "
             "<strong>Autorización</strong>. Inicia sesión con tu email y contraseña de "
             "OnlyFans. SplitCam conecta con tu cuenta, obtiene la clave de stream "
             "automáticamente y la mantiene sincronizada — y te deja gestionar los ajustes del "
             "directo de OnlyFans dentro de SplitCam, cambiándolos durante o después de la "
             "emisión sin abrir el sitio de OnlyFans."),
            ("Conexión — Método 2: Stream Key (manual)",
             "¿Prefieres no iniciar sesión? Usa la clave. En OnlyFans ve a "
             "<strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; la sección "
             "<strong>Other</strong> y copia la <strong>OBS Key</strong>. En SplitCam, Add "
             "Channel &rarr; OnlyFans, pégala en el campo de clave. Esta clave es estática — "
             "para cambiar ajustes después vuelves al sitio de OnlyFans."),
            ("Pulsa Go Live",
             "Con cualquiera de los métodos, pulsa <strong>Go Live</strong> en SplitCam. Con el "
             "Método 1 puedes seguir ajustando los parámetros de OnlyFans desde SplitCam sobre "
             "la marcha; con el Método 2 la clave queda tal como la pusiste."),
        ],
        "tips": [
            ("Autorización vs Stream Key", "Dos formas de conectar: "
             "<strong>Autorización</strong> (inicias sesión una vez, la clave se obtiene y se "
             "mantiene sincronizada — lo más fácil) o <strong>Stream Key</strong> (copia la OBS "
             "Key en OnlyFans → Profile → Settings → Other y pégala). La autorización no "
             "requiere copiar nada a mano."),
            ("Cambia ajustes sin salir de SplitCam", "Con autorización la cuenta sigue "
             "conectada, así que puedes ajustar los parámetros del directo de OnlyFans dentro "
             "de SplitCam a mitad de emisión o después — sin pasar por el sitio de OnlyFans."),
            ("Mantén el bitrate bajo", "El ingest RTMP de OnlyFans limita el vídeo a unos "
             "2.500 Kbps — más estricto que la mayoría. Apunta a 720p–1080p a ~2.000–2.500."),
            _T_ETH,
        ],
        "faq": [
            ("¿Cómo conecto OnlyFans con SplitCam?", "De dos formas. "
             "<strong>Autorización</strong> — Stream Settings → Add Channel → OnlyFans → inicia "
             "sesión con tu cuenta de OnlyFans y SplitCam obtiene la clave automáticamente. O "
             "<strong>Stream Key</strong> — copia la OBS Key en OnlyFans → Profile → Settings → "
             "Other y pégala."),
            ("¿Puedo cambiar los ajustes del directo de OnlyFans sin abrir el sitio?", "Sí — "
             "con el método Autorización SplitCam sigue conectado a tu cuenta de OnlyFans, así "
             "que la clave y los ajustes se sincronizan solos. Puedes cambiarlos dentro de "
             "SplitCam durante la emisión o después, sin visitar onlyfans.com."),
            ("¿Qué bitrate para OnlyFans?", "Mantenlo modesto — el ingest RTMP de OnlyFans "
             "limita el vídeo a unos 2.500 Kbps, mucho más estricto que otras plataformas cam. "
             "Apunta a 720p–1080p a ~2.000–2.500 Kbps."),
            ("¿SplitCam es gratis para directos de OnlyFans?", "Sí — gratis, sin marca de agua, "
             "sin límite."),
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
        "intro": "CamPlace es una plataforma de streaming cam. No tiene artículo público de "
                 "ayuda sobre OBS, así que la <strong style='color:var(--text)'>guía en vídeo "
                 "de arriba</strong> es la referencia — <strong style='color:var(--text)'>"
                 "SplitCam</strong> gratis conecta por RTMP estándar y añade escenas, "
                 "superposiciones y fondo con IA que una cámara básica no puede.",
        "quick": "Emite en CamPlace con SplitCam: instala SplitCam, monta tu escena, activa la "
                 "emisión externa/RTMP en CamPlace, copia la URL del servidor y la clave, "
                 "pégalas en SplitCam, Go Live. Sigue la guía en vídeo de arriba."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la clave RTMP de CamPlace.</li><li>Pégala en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en CamPlace y abre tus ajustes de emisión. Cambia a la opción "
                   "de codificador externo / RTMP / OBS para ver la <strong>URL del "
                   "servidor</strong> y la <strong>clave</strong>, copia ambas. CamPlace no "
                   "publica documentación oficial de OBS, así que la <strong>guía en vídeo de "
                   "arriba</strong> es el recorrido más fiable de la interfaz actual.",
        "tips": [
            ("Sin guía OBS oficial — usa el vídeo", "CamPlace no tiene artículo público de "
             "soporte sobre codificadores externos; la guía en vídeo de arriba es la "
             "referencia de la ruta actual."),
            ("El RTMP estándar funciona", "Aun sin docs, CamPlace acepta una URL de servidor "
             "RTMP estándar y una clave — SplitCam conecta como destino RTMP personalizado."),
            ("Superpón en SplitCam", "Objetivos de tokens, tu nombre y redes como capas de "
             "escena — la cámara básica de CamPlace no puede añadirlas."),
            ("Usa conexión por cable", "Sin documentación oficial de codificador de CamPlace "
             "a la que recurrir, un enlace Ethernet estable elimina las caídas de conexión "
             "como variable mientras sigues la guía en vídeo."),
        ],
        "faq": [
            ("¿CamPlace tiene una guía OBS oficial?", "No se encontró artículo público de "
             "soporte sobre codificadores externos. CamPlace sí acepta una URL RTMP estándar y "
             "clave, así que SplitCam funciona — sigue la guía en vídeo de arriba."),
            ("¿CamPlace admite codificadores externos?", "Sí — acepta una clave RTMP estándar, "
             "así que SplitCam conecta como destino RTMP personalizado."),
            ("¿SplitCam es gratis para CamPlace?", "Sí — gratis, sin marca de agua ni límite "
             "de tiempo. Como CamPlace no trae codificador propio, una herramienta RTMP "
             "gratuita es todo lo que necesitas."),
            ("¿Qué bitrate para CamPlace?", "CamPlace no publica una cifra oficial — toma "
             "3.500–6.000 Kbps a 1080p como rango seguro y deja que el test de velocidad de "
             "SplitCam fije tu techo real."),
        ],
    },
    {
        "slug": "camsoda", "name": "CamSoda",
        "title": "Cómo emitir en CamSoda con SplitCam — Use OBS Broadcaster",
        "desc": "Emite en CamSoda con SplitCam gratis. Botón Use OBS Broadcaster, guía OBS "
                "oficial en la wiki, servidores regionales. Sin marca de agua.",
        "kw": "cómo emitir en camsoda, camsoda live, camsoda obs broadcaster, camsoda rtmp",
        "h1html": 'Cómo emitir en <span class="accent">CamSoda</span> con SplitCam',
        "h1short": "Emitir en CamSoda",
        "card": "Configuración vía Use OBS Broadcaster de CamSoda.",
        "intro": "CamSoda es una plataforma cam de EE. UU. conocida por formatos de show "
                 "novedosos e interactivos. Admite oficialmente la emisión con OBS — hay un "
                 "botón <strong style='color:var(--text)'>Use OBS Broadcaster</strong> en la "
                 "página Go Live y una guía OBS oficial en la wiki de CamSoda. "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis funciona igual.",
        "quick": "Emite en CamSoda con SplitCam: instala SplitCam, monta tu escena, pulsa Use "
                 "OBS Broadcaster en la página Go Live de CamSoda, copia la URL del servidor y "
                 "la clave, pégalas en SplitCam, Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Pulsa Use OBS Broadcaster en CamSoda.</li>"
                 "<li>Pega URL y clave en SplitCam.</li><li>Pulsa Go Live.</li></ol>",
        "key_how": "En la página <strong>Go Live</strong> de CamSoda, pulsa <strong>Use OBS "
                   "Broadcaster</strong>. CamSoda muestra la URL del servidor RTMP y la clave — "
                   "copia ambas. Elige el servidor regional (Norteamérica, Europa, Asia, etc.) "
                   "más cercano. La wiki de CamSoda tiene una guía OBS completa si necesitas "
                   "detalle.",
        "tips": [
            ("Verifícate para recibir propinas", "En CamSoda cualquiera puede emitir, pero para "
             "recibir propinas debes completar la solicitud de verificación de CamSoda."),
            ("Elige el servidor regional más cercano", "CamSoda ofrece servidores de ingest "
             "regionales — el más cercano (NA / Europa / Asia / Sudamérica / Oceanía) reduce el "
             "lag y los fotogramas perdidos."),
            ("Tope a 1080p / 30 fps", "El ingest de CamSoda llega hasta unos 1080p, 30 fps y "
             "~6.000 Kbps — no hace falta subir más."),
            ("Cable hacia tu servidor regional", "Combina una conexión por cable con el "
             "servidor de ingest regional de CamSoda más cercano — juntos mantienen baja la "
             "latencia y los fotogramas perdidos."),
        ],
        "faq": [
            ("¿CamSoda admite OBS / codificadores externos?", "Sí — oficialmente. Hay un botón "
             "Use OBS Broadcaster en la página Go Live y una guía OBS en la wiki de CamSoda, "
             "así que SplitCam funciona."),
            ("¿Necesito verificarme en CamSoda?", "Para emitir, no. Para recibir propinas, sí — "
             "CamSoda requiere completar antes su solicitud de verificación."),
            ("¿Qué resolución admite CamSoda?", "Hasta 1920×1080 a 30 fps, unos 6.000 Kbps "
             "máximo en su ingest RTMP."),
            ("¿SplitCam es gratis para CamSoda?", "Sí — gratis, sin marca de agua ni límite "
             "de tiempo. Funciona junto al propio modo gratuito Use OBS Broadcaster de "
             "CamSoda, así que toda la cadena no cuesta nada."),
            ("¿Qué ajustes de audio y codificador usa CamSoda?", "El ingest de CamSoda admite "
             "audio AAC hasta 160 Kbps y vídeo H.264 con preset tune=zerolatency. CamSoda "
             "también es un servicio integrado en OBS, así que en SplitCam funciona como un "
             "destino RTMP estándar."),
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
            ("Fija la resolución en 1080p", "El campo Video Resolution de SM Connect puede "
             "saltar a 1440, que en realidad no se entrega y baja tu calidad sin avisar — "
             "ponlo en 1080p a mano. Que el bitrate caiga en una imagen fija es normal: el "
             "feed de Streamate es adaptativo."),
            ("Usa conexión por cable", "El feed de Streamate ya baja el bitrate bajo presión "
             "— no añadas encima la inestabilidad del Wi-Fi; lleva un cable Ethernet."),
            ("Prueba primero con SM Connect", "Inicia un show privado corto vía SM Connect "
             "para confirmar el slider verde y tu escena antes de salir en público."),
        ],
        "faq": [
            ("¿Streamate está integrado en SplitCam?", "Sí — Streamate aparece en la lista Add "
             "Channel de SplitCam, lo seleccionas en vez de escribir una URL RTMP."),
            ("¿Dónde está la clave de stream de Streamate?", "SM Connect → aceptar términos → "
             "Start Show → cerrar la ventana → copiar la clave."),
            ("¿SplitCam es gratis para Streamate?", "Sí — gratis, sin marca de agua ni "
             "límite de tiempo; y como Streamate es un canal integrado de SplitCam, tampoco "
             "hay coste de codificador aparte."),
            ("¿Qué bitrate para Streamate?", "Streamate no fija un techo duro — 3.500–6.000 "
             "Kbps a 1080p funciona bien. El feed es adaptativo, así que un bitrate más bajo "
             "en una imagen fija es normal, no un fallo."),
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
            ("Cable para el flujo de solo-URL", "StreamRay autentica solo por URL — un "
             "enlace por cable evita una reconexión a mitad de show que te enviaría de vuelta "
             "a la ventana de chat por la URL."),
            ("Prueba antes de emitir", "Haz una prueba privada corta de StreamRay para "
             "confirmar que la URL se pegó bien y la escena se ve correcta."),
        ],
        "faq": [
            ("¿Dónde está la URL del stream de StreamRay?", "Tras activar OBS Broadcaster, "
             "StreamRay publica la URL en la ventana de chat — cópiala del chat."),
            ("¿Por qué StreamRay no tiene clave de stream?", "StreamRay autentica solo por URL "
             "— deja el campo de clave de SplitCam vacío."),
            ("¿SplitCam es gratis para StreamRay?", "Sí — gratis, sin marca de agua ni "
             "límite de tiempo, lo que encaja con el flujo de solo-URL de StreamRay, donde "
             "solo pegas un enlace y emites."),
            ("¿Qué bitrate para StreamRay?", "StreamRay no indica un techo oficial — apunta "
             "a 3.500–6.000 Kbps a 1080p y haz el test de velocidad de SplitCam, ya que el "
             "flujo de solo-URL no da retorno de bitrate."),
        ],
    },
    {
        "slug": "xlovecam", "name": "XLoveCam",
        "title": "Cómo emitir en XLoveCam con SplitCam — enlace RTMP y clave",
        "desc": "Emite en XLoveCam con SplitCam gratis. Encuentra el enlace RTMP y la clave en "
                "My Account → settings, servidores regionales. Sin marca de agua.",
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
            ("Elige el servidor más cercano", "XLoveCam ofrece servidores de ingest regionales "
             "— Europa (Países Bajos, Rumanía), Norteamérica, Sudamérica, Asia. El más cercano "
             "reduce la latencia."),
            ("Audiencia multilingüe", "XLoveCam es europea y multilingüe — una superposición de "
             "texto clara en tu idioma ayuda a que te encuentren."),
            ("El cable gana al Wi-Fi", "Tras elegir el servidor de XLoveCam más cercano, una "
             "conexión por cable es la otra mitad de un stream estable — evita que los "
             "fotogramas caigan en un show largo."),
        ],
        "faq": [
            ("¿Dónde están los datos RTMP de XLoveCam?", "My Account → settings — muestra el "
             "enlace RTMP y la clave."),
            ("¿XLoveCam admite codificadores externos?", "Sí — XLoveCam ofrece un modo oficial "
             "de emisión por OBS con enlace RTMP y clave, así que SplitCam funciona."),
            ("¿SplitCam es gratis para XLoveCam?", "Sí — gratis, sin marca de agua ni límite "
             "de tiempo, así que llegar a la audiencia europea multilingüe de XLoveCam no "
             "supone coste de software."),
            ("¿Qué bitrate para XLoveCam?", "XLoveCam no publica un límite fijo; 3.500–6.000 "
             "Kbps a 1080p es ideal. Elegir el servidor regional más cercano importa igual — "
             "reduce los fotogramas perdidos."),
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
            ("Bloquea las regiones que no quieras", "SoulCams admite el bloqueo por países "
             "desde el lado de la modelo — elige qué países no pueden ver tu emisión antes de "
             "pulsar Go Online."),
            ("Usa conexión por cable", "SoulCams muestra servidor y clave juntos para "
             "empezar rápido — mantén el propio stream igual de sólido con un cable "
             "Ethernet."),
            ("Prueba tras Go Online", "Los ajustes OBS solo aparecen tras Go Online — ya "
             "conectado, haz una prueba privada corta antes de llevar la sala a público."),
        ],
        "faq": [
            ("¿Dónde están los ajustes OBS de SoulCams?", "Inicia sesión, pulsa Go Online, "
             "luego Settings → OBS — el servidor RTMP y la clave se muestran juntos."),
            ("¿SoulCams admite codificadores externos?", "Sí — sus ajustes OBS dan un servidor "
             "RTMP y clave, así que SplitCam funciona."),
            ("¿SplitCam es gratis para SoulCams?", "Sí — gratis, sin marca de agua ni límite "
             "de tiempo, así que un show completo en SoulCams con escenas de varias cámaras "
             "y superposiciones no cuesta nada de codificar."),
            ("¿Qué bitrate para SoulCams?", "SoulCams no da una cifra oficial — apunta a "
             "3.500–6.000 Kbps a 1080p y comprueba tu subida primero, ya que su ventana OBS "
             "no muestra guía de bitrate."),
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
            ("Prueba primero la cámara virtual", "Antes de iniciar un chat en ImLive, "
             "confirma que la cámara virtual de SplitCam funciona — revísala en la vista "
             "previa de ajustes de ImLive."),
        ],
        "faq": [
            ("¿ImLive usa RTMP o clave de stream?", "No — ImLive usa tu webcam directamente vía "
             "navegador y no tiene documentación oficial de OBS. SplitCam se conecta como "
             "cámara virtual, no hay clave que copiar."),
            ("¿Cómo elijo SplitCam en ImLive?", "Start Video Chat → Go To Settings → elige "
             "SplitCam como webcam y micrófono."),
            ("¿SplitCam es gratis para ImLive?", "Sí — gratis, sin marca de agua ni límite "
             "de tiempo. Como cámara virtual para ImLive no añade coste ni marca a tu "
             "videochat."),
            ("¿Puedo usar superposiciones en ImLive?", "Sí — móntalas en la escena de SplitCam; "
             "ImLive muestra el resultado compuesto."),
        ],
    },
    {
        "slug": "vxlive", "name": "VXLive",
        "title": "Cómo emitir en VXLive con SplitCam — soporte oficial",
        "desc": "VXLive (VXModels) admite oficialmente SplitCam: hay artículo de ayuda y preset "
                "VISIT-X. Stream with third-party software, servidor + clave.",
        "kw": "cómo emitir en vxlive, vxlive splitcam, vxmodels splitcam, visit-x splitcam",
        "h1html": 'Cómo emitir en <span class="accent">VXLive</span> con SplitCam',
        "h1short": "Emitir en VXLive",
        "card": "VXLive admite oficialmente SplitCam (preset VISIT-X).",
        "intro": "VXLive (VXModels / VISIT-X) es una plataforma cam del mercado alemán — y una "
                 "de las pocas que <strong style='color:var(--text)'>admite oficialmente "
                 "SplitCam por su nombre</strong>. VXModels tiene un artículo de ayuda dedicado "
                 "para conectar <strong style='color:var(--text)'>SplitCam</strong> con VXLive, "
                 "y SplitCam trae VISIT-X como preset de canal listo para usar.",
        "quick": "Emite en VXLive con SplitCam: instala SplitCam, monta tu escena, en VXLive "
                 "elige \"Stream with third-party software\", copia la URL del servidor y la "
                 "clave, en SplitCam elige el preset VISIT-X y pégalas, Go Live en SplitCam, "
                 "luego GO ONLINE en VXLive."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue la URL del servidor + clave de VXLive.</li>"
                 "<li>Elige el preset VISIT-X en SplitCam, pega.</li>"
                 "<li>Go Live, luego GO ONLINE en VXLive.</li></ol>",
        "key_how": "En VXLive, elige <strong>Stream with third-party software</strong> y la "
                   "opción para <strong>OBS, SplitCam o XSplit</strong>. VXLive da una "
                   "<strong>URL de servidor</strong> y una <strong>clave de stream</strong>. En "
                   "SplitCam, elige <strong>VISIT-X</strong> como plataforma, pega ambas, pulsa "
                   "<strong>Go Live</strong> en SplitCam, luego <strong>GO ONLINE</strong> en "
                   "VXLive.",
        "tips": [
            ("VISIT-X es un preset integrado", "No introduces una URL RTMP cruda — SplitCam "
             "tiene VISIT-X en su lista de plataformas, selecciónalo y pega URL y clave."),
            ("Salida en directo en dos pasos", "En VXLive pulsas Go Live en SplitCam primero, "
             "luego GO ONLINE en VXLive — ambos, en ese orden."),
            ("Plataforma del mercado alemán", "La audiencia de VXLive es mayormente "
             "germanoparlante — una superposición o título en alemán ayuda a conectar."),
            ("Usa conexión por cable", "La salida en directo en dos pasos de VXLive significa "
             "que una caída a mitad de show te cuesta ambas reconexiones — un enlace por "
             "cable lo hace mucho menos probable."),
        ],
        "faq": [
            ("¿VXLive admite oficialmente SplitCam?", "Sí — VXModels (VXLive) tiene un artículo "
             "de ayuda oficial dedicado a configurar SplitCam, y lista SplitCam junto a OBS y "
             "XSplit como software de emisión admitido."),
            ("¿Cómo conecto SplitCam con VXLive?", "En VXLive elige \"Stream with third-party "
             "software\", luego en SplitCam elige el preset VISIT-X y pega la URL del servidor "
             "y la clave que da VXLive."),
            ("¿Dónde pulso \"en directo\", en SplitCam o VXLive?", "En ambos — primero Go Live "
             "en SplitCam, luego GO ONLINE en VXLive."),
            ("¿SplitCam es gratis para VXLive?", "Sí — gratis, sin marca de agua ni límite "
             "de tiempo. VXModels lista SplitCam como software admitido, así que es a la vez "
             "gratuito y reconocido oficialmente."),
            ("¿Por qué VXModels recomienda SplitCam?", "El artículo de ayuda oficial de "
             "VXModels recomienda SplitCam concretamente para eliminar los artefactos de "
             "imagen y la pixelación de la webcam y estabilizar la conexión — no solo como "
             "codificador genérico."),
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
            ("Usa conexión por cable", "VirtWish da una URL y una clave aparte — un enlace "
             "por cable evita una reconexión que te haría pasar de nuevo por los dos clics de "
             "Start Broadcast."),
            ("Prueba antes de salir en directo", "Haz una emisión privada corta de VirtWish "
             "para confirmar que la URL y la clave cayeron en los campos correctos de "
             "SplitCam."),
        ],
        "faq": [
            ("¿Dónde están los datos RTMP de VirtWish?", "Icono arriba a la derecha → Profile → "
             "Start Broadcast dos veces → la sección OBS muestra el enlace y la clave."),
            ("¿VirtWish admite codificadores externos?", "Sí — su sección OBS da una URL de "
             "stream y clave, así que SplitCam funciona."),
            ("¿SplitCam es gratis para VirtWish?", "Sí — gratis, sin marca de agua ni límite "
             "de tiempo, así que la configuración de VirtWish con URL del stream y clave no "
             "cuesta más que los pocos minutos que lleva."),
            ("¿Qué bitrate para VirtWish?", "VirtWish no publica un techo oficial; "
             "3.500–6.000 Kbps a 1080p es un rango seguro. Iguala la resolución de SplitCam a "
             "la fijada en VirtWish para evitar el reescalado."),
        ],
    },
    {
        "slug": "xmodels", "name": "XModels",
        "title": "Cómo emitir en XModels con SplitCam — guía gratuita",
        "desc": "Emite en XModels con SplitCam gratis. Opción de codificador externo en los "
                "ajustes de la cuenta de modelo. Escenas, superposiciones, sin marca de agua.",
        "kw": "cómo emitir en xmodels, xmodels software de emisión, xmodels rtmp",
        "h1html": 'Cómo emitir en <span class="accent">XModels</span> con SplitCam',
        "h1short": "Emitir en XModels",
        "card": "Opción de codificador externo en la cuenta de XModels.",
        "intro": "XModels es una plataforma de streaming cam con una "
                 "<strong style='color:var(--text)'>opción de codificador externo</strong> "
                 "integrada en los ajustes de la cuenta de modelo. "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis emite a ella con "
                 "escenas, superposiciones y filtros en vez de una sola cámara plana.",
        "quick": "Emite en XModels con SplitCam: instala SplitCam, monta tu escena, en tu "
                 "cuenta de modelo de XModels activa la opción de codificador externo, copia la "
                 "URL del servidor y la clave, pégalas en SplitCam, Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Activa el codificador externo en los ajustes de XModels.</li>"
                 "<li>Pega URL y clave en SplitCam.</li><li>Pulsa Go Live.</li></ol>",
        "key_how": "En los <strong>ajustes de tu cuenta de modelo</strong> de XModels, activa "
                   "la opción de <strong>emisión por codificador externo</strong>. XModels da "
                   "una <strong>clave de stream</strong> — cópiala en SplitCam. Si la opción no "
                   "está donde esperas, el soporte de XModels va por chat FAQ en el sitio e "
                   "<strong>info@xmodels.com</strong>; la guía en vídeo de arriba también la "
                   "muestra.",
        "tips": [
            ("Está en los ajustes de la cuenta", "XModels pone la opción de codificador externo "
             "dentro de los ajustes de la cuenta de modelo, no en una pantalla aparte."),
            ("El soporte es chat + email", "XModels no tiene un gran centro de ayuda público — "
             "su chat FAQ en el sitio e info@xmodels.com son las vías oficiales de soporte."),
            ("Superpón en SplitCam", "Objetivos de tokens, tu nombre y redes como capas de "
             "escena — la cámara básica de XModels no puede añadirlas."),
            ("Usa conexión por cable", "El soporte de XModels es solo por chat y email — un "
             "enlace Ethernet estable te ahorra una vuelta lenta con soporte si el stream se "
             "cae."),
        ],
        "faq": [
            ("¿XModels admite codificadores externos?", "Sí — los ajustes de la cuenta de "
             "modelo incluyen una opción de emisión por codificador externo que da una clave, "
             "así que SplitCam funciona."),
            ("¿Dónde consigo ayuda con XModels?", "El soporte de XModels es vía su chat FAQ en "
             "el sitio y el email info@xmodels.com — no hay un gran centro de ayuda público."),
            ("¿SplitCam es gratis para XModels?", "Sí — gratis, sin marca de agua ni límite "
             "de tiempo, así que emitir a la red europea de XModels no añade coste de "
             "software."),
            ("¿Qué bitrate para XModels?", "XModels no documenta una cifra oficial — usa "
             "3.500–6.000 Kbps a 1080p y haz el test de velocidad de SplitCam, ya que el "
             "soporte de XModels es solo por chat y email."),
        ],
    },
    {
        "slug": "flirt4free", "name": "Flirt4Free",
        "title": "Cómo emitir en Flirt4Free con SplitCam — External Broadcast Form",
        "desc": "Emite en Flirt4Free con SplitCam gratis. El External Broadcast Form da RTMP "
                "URL y Stream Name + campos de resolución/bitrate. Sin marca de agua.",
        "kw": "cómo emitir en flirt4free, flirt4free external broadcast, flirt4free rtmp",
        "h1html": 'Cómo emitir en <span class="accent">Flirt4Free</span> con SplitCam',
        "h1short": "Emitir en Flirt4Free",
        "card": "Configuración vía External Broadcast Form de Flirt4Free.",
        "intro": "Flirt4Free es una de las plataformas cam más longevas, online desde los años "
                 "90. Admite oficialmente la emisión externa mediante un "
                 "<strong style='color:var(--text)'>External Broadcast Form</strong> — "
                 "<strong style='color:var(--text)'>SplitCam</strong> gratis envía el stream "
                 "mientras el formulario fija tu resolución y bitrate.",
        "quick": "Emite en Flirt4Free con SplitCam: instala SplitCam, monta tu escena, abre el "
                 "External Broadcast Form de Flirt4Free, copia la RTMP URL y el Stream Name y "
                 "fija resolución/bitrate, pégalos en SplitCam, Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Abre el External Broadcast Form de Flirt4Free.</li>"
                 "<li>Pega la RTMP URL + Stream Name en SplitCam.</li><li>Pulsa Go Live.</li></ol>",
        "key_how": "En el área de modelo de Flirt4Free, abre el <strong>External Broadcast "
                   "Form</strong>. A diferencia de la mayoría de sitios cam, Flirt4Free da una "
                   "<strong>RTMP URL</strong> y un <strong>Stream Name</strong> (no una "
                   "\"clave\"), más campos de resolución y bitrate que rellenas en el "
                   "formulario. Copia la URL y el Stream Name en los campos de servidor y clave "
                   "de SplitCam.",
        "tips": [
            ("Es un Stream Name, no una clave", "Flirt4Free llama Stream Name a la credencial. "
             "Pégala en el campo de clave de SplitCam — cumple la misma función."),
            ("Fija resolución/bitrate en el formulario", "El External Broadcast Form de "
             "Flirt4Free tiene sus propios campos de resolución y bitrate — iguálalos a los "
             "ajustes de SplitCam para que la imagen no se reescale."),
            ("Una plataforma consolidada", "Flirt4Free funciona desde los años 90 — sus "
             "herramientas de modelo son maduras y el External Broadcast Form es parte "
             "documentada de ellas."),
            ("Usa conexión por cable", "El External Broadcast Form de Flirt4Free fija tu "
             "resolución y bitrate — un enlace por cable mantiene el stream en esos valores "
             "sin bajones de Wi-Fi."),
        ],
        "faq": [
            ("¿Flirt4Free admite codificadores externos?", "Sí — oficialmente, mediante su "
             "External Broadcast Form, que da una RTMP URL y un Stream Name. SplitCam funciona "
             "como codificador."),
            ("¿Dónde consigo los datos RTMP de Flirt4Free?", "Del External Broadcast Form en el "
             "área de modelo — muestra la RTMP URL, el Stream Name y campos de "
             "resolución/bitrate."),
            ("¿SplitCam es gratis para Flirt4Free?", "Sí — gratis, sin marca de agua ni "
             "límite de tiempo, lo que viene bien para una plataforma tan veterana como "
             "Flirt4Free, donde los shows pueden ser largos."),
            ("¿Qué bitrate para Flirt4Free?", "3.500–6.000 Kbps a 1080p — pon el mismo valor en "
             "el External Broadcast Form y en SplitCam."),
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
            ("¿Alertas atascadas? Refresca la caché", "Si los efectos de alerta dejan de "
             "aparecer, haz clic derecho en la capa Browser de MFC Alerts y elige \"Refresh "
             "cache of current page\" — eso limpia una superposición obsoleta."),
            ("Usa conexión por cable", "MFC Alerts es una superposición de navegador en vivo "
             "que reacciona a las propinas — un enlace por cable evita que se entrecorten "
             "tanto la cámara como las animaciones de alertas."),
        ],
        "faq": [
            ("¿Qué es MFC Alerts?", "Un sistema de notificaciones para MyFreeCams que muestra "
             "efectos de vídeo en tu emisión cuando los espectadores dan propina — añadido como "
             "superposición Browser en SplitCam."),
            ("¿Por qué no se ven mis MFC Alerts?", "Casi siempre el orden de capas — la capa "
             "Browser de MFC Alerts debe ir encima de la webcam en la lista de fuentes."),
            ("¿Y cómo emito al propio MyFreeCams?", "MyFreeCams admite oficialmente la emisión "
             "por OBS (su plugin Sidekick fue descontinuado — la wiki aconseja \"usa OBS\"). "
             "Recomendado: 720p, 30 fps, ~2.500 Kbps — SplitCam conecta igual."),
            ("¿SplitCam es gratis para esto?", "Sí — SplitCam es gratis, sin marca de agua "
             "ni límite de tiempo, y la superposición de navegador MFC Alerts funciona "
             "dentro de él sin coste extra."),
        ],
    },
    {
        "slug": "lovense", "name": "Lovense",
        "title": "Cómo añadir un juguete Lovense a tu emisión con SplitCam",
        "desc": "Conecta un juguete interactivo Lovense a tu emisión cam con SplitCam gratis. "
                "Lovense tiene un Lovense SplitCam Toolset oficial.",
        "kw": "cómo añadir lovense a la emisión, lovense splitcam toolset, lovense cam stream, "
              "juguete interactivo lovense streaming",
        "h1html": 'Cómo añadir un <span class="accent">juguete Lovense</span> a tu emisión',
        "h1short": "Añadir un juguete Lovense",
        "card": "Conecta un juguete interactivo Lovense a tu emisión cam.",
        "intro": "Emite con <strong style='color:var(--text)'>SplitCam</strong> gratis y vincula "
                 "un juguete interactivo <strong style='color:var(--text)'>Lovense</strong> "
                 "para que reaccione a los tokens. Lovense documenta un "
                 "<strong style='color:var(--text)'>Lovense SplitCam Toolset</strong> oficial, "
                 "y SplitCam trae un plugin oficial de Lovense — la integración está soportada "
                 "por ambos lados.",
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
            ("Usa el Lovense SplitCam Toolset oficial", "Lovense publica un toolset específico "
             "para SplitCam con su propia guía de instalación — añade la superposición de "
             "actividad del juguete y alertas de propinas hecha para SplitCam."),
            ("Actualiza la Lovense Cam Extension", "El toolset necesita una Lovense Cam "
             "Extension reciente (30.1.4 o más nueva) — actualízala antes de emitir."),
            ("Carga el juguete", "Una batería agotada a mitad de show mata la parte "
             "interactiva — cárgalo del todo antes de emitir."),
            ("Prueba la reacción", "Envía una pequeña propina de prueba para confirmar que el "
             "juguete reacciona antes de abrir la sala."),
            ("Ten en cuenta los requisitos de versión", "El Lovense SplitCam Toolset necesita "
             "SplitCam 10.4.5 o más nuevo. La Lovense Cam Extension cubre oficialmente "
             "Chaturbate, Stripchat, BongaCams, MyFreeCams y CamSoda — para cualquier otro "
             "sitio, usa la integración Generic URL de Lovense."),
        ],
        "faq": [
            ("¿Lovense admite oficialmente SplitCam?", "Sí — Lovense documenta un \"Lovense "
             "SplitCam Toolset\" oficial con su propia guía de instalación, y SplitCam trae un "
             "plugin oficial de Lovense. La integración está soportada por ambos lados."),
            ("¿El juguete se conecta directo a SplitCam?", "No — el juguete se vincula con la "
             "app de Lovense; SplitCam muestra la superposición y emite tu cámara."),
            ("¿Qué sitios cam admiten Lovense?", "La Cam Extension de Lovense admite "
             "oficialmente Chaturbate, Stripchat, BongaCams, MyFreeCams y CamSoda, con soporte "
             "variable para otros — consulta la lista en la app de Lovense."),
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
            ("Por cable — aquí no puedes permitirte una caída", "La multiemisión multiplica "
             "la carga de subida, así que un solo bajón de Wi-Fi puede parar todos los "
             "destinos a la vez. La conexión por cable no es opcional aquí."),
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
