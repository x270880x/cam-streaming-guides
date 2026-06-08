# -*- coding: utf-8 -*-
"""Spanish content for cam-streaming-guides. Genuinely per-platform, FAQ-enriched."""

_T_ETH = ("Conexión por cable", "Ethernet es más fiable que el Wi-Fi para un directo largo — "
          "un fotograma perdido es una propina perdida. Lleva un cable al PC de streaming.")
_T_TEST = ("Haz una prueba privada primero", "Una emisión de prueba corta verifica cámara, "
           "audio, encuadre y superposiciones antes de abrir la sala.")

PLATFORMS_ES = [
    {
        "slug": "chaturbate", "name": "Chaturbate",
        "title": "Cómo transmitir en Chaturbate con SplitCam — token y RTMP",
        "desc": "Cómo transmitir en Chaturbate con SplitCam gratis — token de emisión, RTMP, escenas multicámara y superposiciones. Sin marca de agua.",
        "kw": "cómo transmitir en chaturbate, chaturbate, chaturbate broadcast, chaturbate obs, chaturbate external encoder, chaturbate rtmp, chaturbate stream key, chaturbate broadcast token",
        "h1html": 'Cómo transmitir en <span class="accent">Chaturbate</span> con SplitCam',
        "h1short": "Transmitir en Chaturbate",
        "card": "Configuración por token y codificador externo de Chaturbate.",
        "steps": [
            None,
            ("Monta una escena de varias cámaras", "Añade tu webcam en SplitCam y superpón "
             "una segunda cámara o el teléfono, superposiciones y filtros de belleza o fondo "
             "con IA. El emisor de Chaturbate muestra una sola cámara plana — tu escena "
             "compuesta la sustituye."),
            None,
            ("Pega el token en SplitCam", "Abre Stream Settings y pega el token de emisión en "
             "el campo de clave RTMP personalizado. Chaturbate tiene mucho margen — pon 1080p "
             "a 3.500–6.000 Kbps con fotograma clave de 2 segundos."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam — tu escena llega a la sala en unos "
             "10 segundos. La baja latencia de Chaturbate mantiene las propinas y reacciones "
             "al ritmo de lo que haces."),
        ],
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
        "title": "Cómo transmitir en CAM4 con SplitCam — codificador externo",
        "desc": "Cómo transmitir en CAM4 con SplitCam gratis — External Encoder, clave de stream, geo-bloqueo y superposiciones. Sin marca de agua.",
        "kw": "cómo transmitir en cam4, cam4, cam4 broadcast, cam4 obs, cam4 external encoder, cam4 rtmp, cam4 stream key",
        "h1html": 'Cómo transmitir en <span class="accent">CAM4</span> con SplitCam',
        "h1short": "Transmitir en CAM4",
        "card": "External Encoder de CAM4 con geo-controles.",
        "steps": [
            None,
            ("Configura tu escena y geo-bloqueo", "Añade tu webcam y superposiciones en "
             "SplitCam, y decide en CAM4 qué países ocultar antes de empezar."),
            None,
            ("Pega la clave de CAM4", "Pega la clave en Stream Settings de SplitCam — un "
             "slider verde lo confirma. Mantén el bitrate cerca de 3.000 Kbps: el ingest de "
             "CAM4 limita más que la mayoría."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam y luego inicia la emisión en CAM4. "
             "Vigila que el slider siga verde — rojo significa revisar la clave."),
        ],
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
        "title": "Cómo transmitir en BongaCams con SplitCam — RTMP",
        "desc": "Cómo transmitir en BongaCams con SplitCam gratis — External Encoder, escenas multicámara y superposiciones, fondo IA. Sin marca de agua.",
        "kw": "cómo transmitir en bongacams, bongacams, bongacams broadcast, bongacams obs, bongacams external encoder, bongacams rtmp, bongacams stream key, bongcams",
        "h1html": 'Cómo transmitir en <span class="accent">BongaCams</span> con SplitCam',
        "h1short": "Transmitir en BongaCams",
        "card": "External Encoder de BongaCams.",
        "steps": [
            None,
            ("Iguala la resolución de la escena", "Añade tu webcam y superposiciones en "
             "SplitCam y pon la misma resolución que usa BongaCams — por ejemplo 1280×720 en "
             "ambos lados — para que la imagen no se reescale."),
            None,
            ("Pega la URL y la clave de BongaCams", "Pega la URL del servidor y la clave en "
             "los campos RTMP personalizados de SplitCam. Si nunca apareció el botón External "
             "Encoder, pide antes al soporte de BongaCams que lo active."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam para emitir a BongaCams. Haz primero "
             "una prueba privada corta de cámara y audio."),
        ],
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
        "title": "Cómo transmitir en Stripchat con SplitCam — software externo",
        "desc": "Cómo transmitir en Stripchat — la plataforma strip cam — con SplitCam gratis. Software externo, clave-token, escenas y superposiciones.",
        "kw": "cómo transmitir en stripchat, stripchat, strip cam, stripchat broadcast, stripchat obs, stripchat external encoder, stripchat rtmp, stripchat stream key",
        "h1html": 'Cómo transmitir en <span class="accent">Stripchat</span> con SplitCam',
        "h1short": "Transmitir en Stripchat",
        "card": "Configuración de software externo para Stripchat.",
        "steps": [
            None,
            ("Monta tu escena a la resolución del sitio", "Añade tu webcam, superposiciones y "
             "filtros en SplitCam. Pon en SplitCam exactamente la resolución elegida en "
             "Stripchat, o el vídeo se pixela."),
            None,
            ("Pega el token de Stripchat", "Pega la clave-token en el campo de clave RTMP de "
             "SplitCam. Mantente muy por encima del mínimo de 2 Mbps — apunta a 3.500–6.000 "
             "Kbps a 1080p."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam y luego pulsa Start Show en "
             "Stripchat — cambiar a software externo por sí solo no te hace público."),
        ],
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
        "title": "Cómo transmitir en directo en OnlyFans con SplitCam",
        "desc": "Cómo transmitir en directo en OnlyFans con SplitCam gratis — autorización con un clic o OBS Key, escenas multicámara y superposiciones.",
        "kw": "cómo transmitir en directo en onlyfans, onlyfans, onlyfans live, onlyfans obs, onlyfans obs key, onlyfans stream key, onlyfans broadcast",
        "h1html": 'Cómo transmitir en directo en <span class="accent">OnlyFans</span> con SplitCam',
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
        "title": "Cómo transmitir en CamPlace con SplitCam — guía gratuita",
        "desc": "Cómo transmitir en CamPlace con SplitCam gratis — codificador externo, clave RTMP, escenas y superposiciones. Sin marca de agua, paso a paso.",
        "kw": "cómo transmitir en camplace, camplace, camplace broadcast, camplace obs, camplace external encoder, camplace rtmp, camplace stream key",
        "h1html": 'Cómo transmitir en <span class="accent">CamPlace</span> con SplitCam',
        "h1short": "Transmitir en CamPlace",
        "card": "Configuración del codificador externo para CamPlace.",
        "steps": [
            None,
            ("Monta tu escena", "Añade tu webcam en SplitCam y superpón superposiciones, una "
             "segunda cámara y filtros — extras que el emisor básico de CamPlace no puede "
             "producir."),
            None,
            ("Pega la URL del servidor y la clave de CamPlace", "Pega ambas en los campos "
             "RTMP personalizados de SplitCam. CamPlace no publica especificaciones, así que "
             "sigue la guía en vídeo de arriba y deja que el test de velocidad fije tu "
             "bitrate."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam para iniciar la emisión en "
             "CamPlace. Haz primero una prueba privada corta, ya que no hay documentación "
             "oficial a la que recurrir."),
        ],
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
        "title": "Cómo transmitir en CamSoda con SplitCam — OBS Broadcaster",
        "desc": "Cómo emitir CamSoda live con SplitCam gratis — Use OBS Broadcaster, servidores regionales, escenas y superposiciones. Sin marca de agua.",
        "kw": "cómo transmitir en camsoda, camsoda, camsoda live, camsoda broadcast, camsoda obs, camsoda obs broadcaster, camsoda rtmp, camsoda stream key",
        "h1html": 'Cómo transmitir en <span class="accent">CamSoda</span> con SplitCam',
        "h1short": "Transmitir en CamSoda",
        "card": "Configuración de emisión en CamSoda vía RTMP.",
        "steps": [
            None,
            ("Monta tu escena", "Añade tu webcam, superposiciones y filtros en SplitCam. "
             "CamSoda destaca por formatos interactivos — las superposiciones de objetivos y "
             "juegos encajan aquí."),
            None,
            ("Pega la URL del servidor y la clave de CamSoda", "Pega ambas en SplitCam, "
             "eligiendo el servidor regional de CamSoda (NA, Europa, Asia, etc.) más cercano. "
             "Limita la calidad a 1080p/30 fps, ~6.000 Kbps."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam para emitir a CamSoda. Ten en cuenta "
             "que debes completar la verificación de CamSoda antes de poder recibir "
             "propinas."),
        ],
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
        "title": "Cómo transmitir en Streamate con SplitCam — canal integrado",
        "desc": "Cómo transmitir en Streamate con SplitCam gratis — canal integrado, clave SM Connect, escenas y superposiciones. Configuración rápida.",
        "kw": "cómo transmitir en streamate, streamate, streamate sm connect, streamate broadcast, streamate obs, streamate stream key, streamate rtmp",
        "h1html": 'Cómo transmitir en <span class="accent">Streamate</span> con SplitCam',
        "h1short": "Transmitir en Streamate",
        "card": "Streamate es un canal integrado de SplitCam — setup rápido.",
        "steps": [
            None,
            ("Monta tu escena", "Añade tu webcam, superposiciones y filtros en SplitCam antes "
             "de conseguir la clave."),
            None,
            ("Añade Streamate como canal", "En SplitCam abre Stream Settings → Add Channel, "
             "elige Streamate de la lista integrada y pega la clave de SM Connect — sin URL "
             "RTMP manual. Fija la resolución en 1080p."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam — un slider verde confirma la "
             "conexión. El feed es adaptativo, así que un bitrate más bajo en una imagen fija "
             "es normal."),
        ],
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
        "title": "Cómo transmitir en StreamRay con SplitCam — URL chat",
        "desc": "Cómo transmitir en StreamRay cam con SplitCam gratis — URL desde el chat, OBS Broadcaster, escenas y superposiciones. Sin marca de agua.",
        "kw": "cómo transmitir en streamray, streamray, streamray cam, streamray broadcast, streamray obs, streamray obs broadcaster, streamray rtmp",
        "h1html": 'Cómo transmitir en <span class="accent">StreamRay</span> con SplitCam',
        "h1short": "Transmitir en StreamRay",
        "card": "Configuración de StreamRay — la URL viene del chat.",
        "steps": [
            None,
            ("Monta tu escena", "Añade tu webcam y superposiciones en SplitCam antes de "
             "activar el OBS Broadcaster de StreamRay."),
            None,
            ("Pega la URL de StreamRay — deja la clave vacía", "Copia la URL del stream que "
             "StreamRay publica en la ventana de chat al campo de servidor de SplitCam. "
             "StreamRay autentica solo por URL, así que deja el campo de clave vacío."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam para emitir a StreamRay. Prueba "
             "antes en privado para confirmar que la URL se pegó bien."),
        ],
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
        "title": "Cómo transmitir en XLoveCam con SplitCam — RTMP",
        "desc": "Cómo transmitir en XLoveCam con SplitCam gratis — enlace RTMP y clave, servidores regionales, escenas y superposiciones. Sin marca de agua.",
        "kw": "cómo transmitir en xlovecam, xlovecam, x love cam, xlovecam broadcast, xlovecam obs, xlovecam rtmp, xlovecam stream key",
        "h1html": 'Cómo transmitir en <span class="accent">XLoveCam</span> con SplitCam',
        "h1short": "Transmitir en XLoveCam",
        "card": "Enlace RTMP + clave para XLoveCam.",
        "steps": [
            None,
            ("Monta tu escena", "Añade tu webcam, superposiciones y una superposición de "
             "texto clara en tu idioma — la audiencia de XLoveCam es europea y multilingüe."),
            None,
            ("Pega el enlace y la clave de XLoveCam", "Copia el enlace RTMP y la clave aparte "
             "desde My Account → settings en SplitCam. Elige el servidor regional más cercano "
             "para reducir la latencia."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam y luego usa Start your show en "
             "XLoveCam."),
        ],
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
        "title": "Cómo transmitir en SoulCams con SplitCam — ajustes OBS",
        "desc": "Cómo transmitir en SoulCams con SplitCam gratis — ajustes OBS, servidor RTMP y clave, escenas multicámara y superposiciones.",
        "kw": "cómo transmitir en soulcams, soulcams, soul cams, soulcams broadcast, soulcams obs, soulcams external encoder, soulcams rtmp, soulcams stream key",
        "h1html": 'Cómo transmitir en <span class="accent">SoulCams</span> con SplitCam',
        "h1short": "Transmitir en SoulCams",
        "card": "Configuración de SoulCams vía RTMP.",
        "steps": [
            None,
            ("Monta tu escena", "Añade tu webcam, superposiciones y filtros en SplitCam, y "
             "decide en SoulCams qué países bloquear antes de salir online."),
            None,
            ("Pega el servidor y la clave de SoulCams", "Desde los ajustes OBS de SoulCams, "
             "copia el servidor RTMP y la clave — mostrados juntos — en los campos RTMP "
             "personalizados de SplitCam."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam para emitir a SoulCams. Los datos "
             "OBS solo aparecen tras Go Online, así que hazlo primero."),
        ],
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
        "desc": "Cómo usar SplitCam en ImLive — ImLive usa la webcam directamente (sin RTMP), conecta SplitCam como cámara virtual con escenas.",
        "kw": "cómo transmitir en imlive, imlive, im live stream, imlive virtual camera, imlive cámara virtual, imlive webcam, imlive splitcam",
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
        "title": "Cómo transmitir en VXLive con SplitCam — soporte oficial",
        "desc": "Cómo transmitir en VXLive (VXModels / VISIT-X) con SplitCam gratis — preset VISIT-X oficial, servidor y clave, escenas. Sin marca de agua.",
        "kw": "cómo transmitir en vxlive, vxlive, visit-x, vxmodels, vxlive obs, vxlive external encoder, vxlive rtmp, vxlive stream key",
        "h1html": 'Cómo transmitir en <span class="accent">VXLive</span> con SplitCam',
        "h1short": "Transmitir en VXLive",
        "card": "VXLive admite oficialmente SplitCam (preset VISIT-X).",
        "steps": [
            None,
            ("Monta tu escena", "Añade tu webcam y superposiciones en SplitCam — un título o "
             "texto en alemán encaja con la audiencia mayormente germanoparlante de VXLive."),
            None,
            ("Usa el preset VISIT-X", "En SplitCam elige VISIT-X de la lista de plataformas y "
             "pega la URL del servidor y la clave que VXLive da en \"Stream with third-party "
             "software\"."),
            ("Salida en directo en dos pasos", "Pulsa Go Live en SplitCam primero, luego "
             "pulsa GO ONLINE en VXLive — ambos, en ese orden."),
        ],
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
        "title": "Cómo transmitir en VirtWish con SplitCam — RTMP",
        "desc": "Cómo transmitir en VirtWish con SplitCam gratis — Profile → Start Broadcast → sección OBS, URL del stream y clave, escenas y superposiciones.",
        "kw": "cómo transmitir en virtwish, virtwish, virtwish broadcast, virtwish obs, virtwish external encoder, virtwish rtmp, virtwish stream key",
        "h1html": 'Cómo transmitir en <span class="accent">VirtWish</span> con SplitCam',
        "h1short": "Transmitir en VirtWish",
        "card": "URL del stream + clave para VirtWish.",
        "steps": [
            None,
            ("Monta tu escena", "Añade tu webcam, superposiciones y filtros en SplitCam antes "
             "de abrir los ajustes de emisión de VirtWish."),
            None,
            ("Pega la URL y la clave de VirtWish", "Copia el enlace de la primera línea de la "
             "sección OBS de VirtWish al campo Stream URL de SplitCam, y la Stream Key aparte "
             "en el campo de clave."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam para iniciar la emisión en "
             "VirtWish. Prueba antes en privado para confirmar que la URL y la clave entraron "
             "bien."),
        ],
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
        "title": "Cómo transmitir en XModels con SplitCam — guía gratuita",
        "desc": "Cómo transmitir en XModels con SplitCam gratis — opción de codificador externo en ajustes de la cuenta, clave RTMP, escenas y superposiciones.",
        "kw": "cómo transmitir en xmodels, xmodels, xmodels broadcast, xmodels obs, xmodels external encoder, xmodels rtmp, xmodels stream key",
        "h1html": 'Cómo transmitir en <span class="accent">XModels</span> con SplitCam',
        "h1short": "Transmitir en XModels",
        "card": "Opción de codificador externo en la cuenta de XModels.",
        "steps": [
            None,
            ("Monta tu escena", "Añade tu webcam, superposiciones y filtros en SplitCam — "
             "extras que la cámara básica de XModels no añade."),
            None,
            ("Pega la clave de XModels", "Activa la opción de codificador externo en los "
             "ajustes de tu cuenta de modelo de XModels y pega la clave de stream en "
             "SplitCam. Si la opción no está donde esperas, el chat FAQ de XModels e "
             "info@xmodels.com ayudan."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam y luego inicia la emisión en tu "
             "cuenta de XModels."),
        ],
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
        "title": "Cómo transmitir en Flirt4Free con SplitCam — RTMP",
        "desc": "Cómo transmitir en Flirt for Free cam con SplitCam gratis — External Broadcast Form, RTMP URL y Stream Name, escenas y superposiciones.",
        "kw": "cómo transmitir en flirt4free, flirt4free, flirt for free cam, flirt 4 free cam, flirt4free broadcast, flirt4free obs, flirt4free external encoder, flirt4free rtmp",
        "h1html": 'Cómo transmitir en <span class="accent">Flirt4Free</span> con SplitCam',
        "h1short": "Transmitir en Flirt4Free",
        "card": "Configuración vía External Broadcast Form de Flirt4Free.",
        "steps": [
            None,
            ("Monta tu escena", "Añade tu webcam, superposiciones y filtros en SplitCam."),
            None,
            ("Pega la URL y el Stream Name de Flirt4Free", "Desde el External Broadcast Form, "
             "copia la RTMP URL y el Stream Name en los campos de servidor y clave de "
             "SplitCam, y pon en el formulario la misma resolución y bitrate que en "
             "SplitCam."),
            ("Pulsa Go Live", "Pulsa Go Live en SplitCam y luego inicia tu show desde el "
             "área de modelo de Flirt4Free."),
        ],
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
        "desc": "Añade MFC Alerts (alertas de propinas de MyFreeCams) a tu emisión con SplitCam gratis — capa Browser, efectos animados con propinas.",
        "kw": "cómo añadir mfc alerts, mfc alerts, myfreecams, myfreecams alertas de propinas, mfcalerts splitcam, mfc alerts overlay",
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
        "desc": "Cómo añadir un juguete Lovense interactivo a tu emisión con SplitCam gratis — Lovense SplitCam Toolset, alertas de propinas en pantalla.",
        "kw": "cómo añadir lovense al stream, lovense, lovense splitcam, lovense splitcam toolset, lovense cam, lovense juguete interactivo, lovense alertas de propinas",
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
        "title": "Cómo transmitir en varios sitios cam a la vez con SplitCam",
        "desc": "Transmitir en varios sitios cam a la vez con SplitCam gratis — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat. Un clic, sin marca de agua.",
        "kw": "transmitir en varios sitios cam a la vez, multistream cam, multiemisión cam, transmitir en chaturbate y bongacams a la vez, software de multiemisión cam, multistreaming cam rtmp",
        "h1html": 'Cómo transmitir en <span class="accent">varios sitios cam</span> a la vez',
        "h1short": "Multiemisión cam",
        "card": "Transmite en varios sitios cam simultáneamente.",
        "intro": "<strong style='color:var(--text)'>SplitCam</strong> gratis puede emitir un "
                 "solo stream a <strong style='color:var(--text)'>varios sitios cam a la "
                 "vez</strong> — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat y más. Sin "
                 "marca de agua, con un clic.",
        "quick": "Para transmitir en varios sitios cam a la vez: instala SplitCam, monta tu escena, "
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
    {
        "slug": "livejasmin", "name": "LiveJasmin",
        "title": "Cómo transmitir en LiveJasmin con SplitCam — HD RTMP",
        "desc": "Cómo transmitir en LiveJasmin con SplitCam gratis — codificador externo del Model Center, HD 1080p, escenas multicámara y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en livejasmin, livejasmin, livejasmin broadcast, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key",
        "h1html": 'Cómo transmitir en <span class="accent">LiveJasmin</span> con SplitCam',
        "h1short": "Transmitir en LiveJasmin",
        "card": "Configuración del codificador externo para el Model Center de LiveJasmin, solo HD.",
        "intro": "LiveJasmin es el buque insignia de Docler Holding — una de las redes cam más grandes del mundo y una plataforma solo HD. Su transmisor preferido es el cliente propietario <strong>JasminCAM</strong>, pero el Model Center también expone una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y te deja transmitir con escenas multicámara, filtros de belleza y overlays sobre la misma señal HD.",
        "quick": "Para transmitir en LiveJasmin con SplitCam: instala SplitCam, monta tu escena HD, en el Model Center entra a <em>Settings → Broadcast → External Encoder</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena HD.</li>"
                 "<li>Saca URL y stream key del Model Center.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en <strong>modelcenter.livejasmin.com</strong>, abre <strong>Settings → Broadcast → External Encoder</strong>. El Model Center muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. <strong>Nota:</strong> las cuentas nuevas tienen que estar aprobadas (48–72 horas) antes de que aparezca la opción de codificador externo, y la plataforma exige salida solo en HD.",
        "tips": [
            ("HD o te penalizan en el ranking", "LiveJasmin es solo HD — por debajo de 1280×720 el sitio te mete en las listas de menor pago, y por debajo de 1080p pierdes la etiqueta 'Premium'. Apunta a 1920×1080 a 30 fps, 4.000–6.000 Kbps."),
            ("JasminCAM vs codificador externo", "JasminCAM, el cliente oficial de Docler, da el cumplimiento HD más limpio, pero los codificadores externos (OBS, SplitCam, vMix) están oficialmente soportados una vez aprobada la cuenta — y desbloquean escenas multicámara y overlays que JasminCAM no hace."),
            ("Free chat no es show privado", "El Free chat es solo preview — sin desnudez. El dinero está en los shows privados y Gold. Diseña tu escena para que luzca fuerte vestida Y en modo show."),
            _T_ETH,
        ],
        "faq": [
            ("¿LiveJasmin soporta oficialmente codificadores externos como SplitCam?", "Sí — el Model Center incluye la opción External Encoder en Settings → Broadcast. JasminCAM es el cliente recomendado, pero OBS, SplitCam y otros codificadores RTMP están listados explícitamente como soportados en cuanto te aprueban la cuenta de modelo."),
            ("¿De dónde saco la stream key de LiveJasmin?", "Dentro del Model Center: Settings → Broadcast → External Encoder. Ahí aparecen la URL del servidor y la stream key única — copia ambas en los campos de RTMP personalizado de SplitCam. La clave está ligada a tu cuenta; trátala como una contraseña."),
            ("¿Qué bitrate uso para LiveJasmin?", "LiveJasmin es solo HD — apunta a 1920×1080 a 30 fps, 4.000–6.000 Kbps con intervalo de keyframe de 2 segundos. Por debajo pierdes el sello Premium y te penalizan en el ranking."),
            ("¿SplitCam es gratis para usar con LiveJasmin?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. El único 'coste' es cumplir los requisitos HD de LiveJasmin, algo que SplitCam hace nativamente con su composición de escena 1080p y los filtros de belleza."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua. Es el codificador que envía tu vídeo HD a LiveJasmin."),
            ("Monta tu escena HD",
             "Abre SplitCam y añade tu webcam en modo 1080p. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — LiveJasmin exige calidad HD y tu escena tiene que verse premium tanto en Free chat como en privado."),
            ("Saca tu URL y stream key de LiveJasmin",
             "Inicia sesión en <strong>modelcenter.livejasmin.com</strong> (la cuenta tiene que estar aprobada primero — normalmente 48–72 horas tras el alta). Abre <strong>Settings → Broadcast → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> única. Copia ambas."),
            ("Conecta SplitCam a LiveJasmin",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de LiveJasmin y la stream key en los campos de RTMP personalizado. Pon bitrate a 4.000–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos. Lanza primero el test de velocidad integrado — los streams HD son exigentes."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online en el Model Center de LiveJasmin. En unos 10 segundos tu señal HD llega a la red de LiveJasmin. Las próximas emisiones son de un clic — abre SplitCam, Go Live y conéctate en LiveJasmin."),
        ],
    },
    {
        "slug": "myfreecams", "name": "MyFreeCams",
        "title": "Cómo transmitir en MyFreeCams con SplitCam — RTMP",
        "desc": "Cómo transmitir en MyFreeCams con SplitCam gratis — External Broadcaster del Model Admin, clave RTMP, escenas multicámara y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en myfreecams, myfreecams, mfc, myfreecams broadcast, myfreecams obs, mfc external encoder, mfc rtmp, mfc stream key",
        "h1html": 'Cómo transmitir en <span class="accent">MyFreeCams</span> con SplitCam',
        "h1short": "Transmitir en MyFreeCams",
        "card": "Configuración de broadcaster externo para el Model Admin de MFC basado en tokens.",
        "intro": "MyFreeCams (MFC) es una de las plataformas cam más veteranas — economía de tokens pura, sin la odisea de aprobación de modelo, y una base fiel de miembros Premium. Su <em>Model Web Broadcaster</em> por defecto es una herramienta de navegador de una sola cámara, pero el Model Admin también expone una opción de <strong>External Broadcaster</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y desbloquea escenas multicámara, overlays y filtros sobre la misma señal monetizada por tokens.",
        "quick": "Para transmitir en MyFreeCams con SplitCam: instala SplitCam, monta tu escena, en <em>Model Admin → Broadcaster</em> cambia de Web Broadcaster a External Broadcaster, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key desde Model Admin.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en MyFreeCams, abre <strong>Model Admin → Broadcaster</strong> y cambia de <em>Web Broadcaster</em> a <strong>External Broadcaster</strong>. La página revela una <strong>URL de servidor</strong> (rtmp://publish.myfreecams.com…) y una <strong>stream key</strong> ligadas a tu cuenta de modelo — copia ambas en los campos de RTMP personalizado de SplitCam. La clave está ligada a la cuenta; trátala como una contraseña y resetéala si se filtra.",
        "tips": [
            ("Tokens MFC, no suscripciones", "MFC es economía pura de propinas y tokens — los miembros Premium pueden hacer privados, pero el grueso del dinero está en las propinas del free chat. Diseña una escena que rente vestida y casual, no solo en shows desnudos."),
            ("Web Broadcaster vs External — elige una vez", "El Web Broadcaster por defecto es de una sola cámara y fuente única. External Broadcaster desbloquea multi-escena, overlays y filtros de belleza vía SplitCam u OBS. Cámbialo en Model Admin → Broadcaster antes de salir al aire."),
            ("Integración con MFC Alerts", "Las alertas animadas de propinas en pantalla salen de mfcalerts.com — añade la URL de la alerta como capa Browser en SplitCam, por encima de la cámara. Mira nuestra guía de MFC Alerts para el montaje completo del overlay."),
            _T_ETH,
        ],
        "faq": [
            ("¿MyFreeCams soporta oficialmente broadcasters externos como SplitCam?", "Sí — Model Admin tiene una opción External Broadcaster que expone una URL de servidor RTMP estándar y una stream key. OBS, SplitCam, vMix y otros codificadores RTMP funcionan; MFC respalda explícitamente la opción en su documentación para modelos."),
            ("¿De dónde saco mi stream key de MFC?", "Model Admin → Broadcaster → cambia a External Broadcaster. Ahí aparecen la URL del servidor (rtmp://publish.myfreecams.com…) y la stream key. Copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para MyFreeCams?", "MFC acepta hasta ~6.000 Kbps con un intervalo de keyframe de 2 segundos. Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps — tu subida es el límite real. Lanza primero el speed test de SplitCam."),
            ("¿SplitCam es gratis para usar con MyFreeCams?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La propia opción External Broadcaster es gratis dentro de Model Admin. Coste total de broadcaster: cero."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua. Es el codificador que envía tu vídeo a MyFreeCams."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — todo se aplica en vivo antes de que la señal salga de tu PC. Considera añadir la URL de mfcalerts.com como capa Browser para las alertas animadas de propinas."),
            ("Cambia a External Broadcaster en Model Admin",
             "Inicia sesión en MyFreeCams. Abre <strong>Model Admin → Broadcaster</strong>. Cambia de <em>Web Broadcaster</em> a <strong>External Broadcaster</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> única. Copia ambas."),
            ("Conecta SplitCam a MyFreeCams",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de MFC y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con intervalo de keyframe de 2 segundos. Lanza primero el speed test integrado."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam. En unos 10 segundos tu señal llega a MyFreeCams. Las próximas emisiones son de un clic — abre SplitCam, Go Live."),
        ],
    },
    {
        "slug": "cherry-tv", "name": "Cherry.tv",
        "title": "Cómo transmitir en Cherry.tv con SplitCam — RTMP",
        "desc": "Cómo transmitir en Cherry.tv con SplitCam gratis — codificador externo del Streamer Dashboard, clave RTMP, escenas y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en cherry.tv, cherry.tv, cherry tv, cherry.tv broadcast, cherry.tv obs, cherry.tv external encoder, cherry.tv rtmp, cherry.tv stream key",
        "h1html": 'Cómo transmitir en <span class="accent">Cherry.tv</span> con SplitCam',
        "h1short": "Transmitir en Cherry.tv",
        "card": "Configuración del codificador externo para el Streamer Dashboard de Cherry.tv.",
        "intro": "Cherry.tv es una plataforma cam más nueva y en plena expansión con un toque Web3 — pagos cripto-friendly y menos barreras de entrada que las redes legacy como LiveJasmin. El broadcaster por defecto va por navegador, pero el <strong>Streamer Dashboard</strong> también expone una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y te deja transmitir con escenas multicámara, overlays y filtros.",
        "quick": "Para transmitir en Cherry.tv con SplitCam: instala SplitCam, monta tu escena, en el Streamer Dashboard abre <em>Broadcast Settings → External Encoder</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del Streamer Dashboard.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de streamer de Cherry.tv, abre el <strong>Streamer Dashboard</strong> y entra en <strong>Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. Las cuentas nuevas de streamer tienen que pasar una verificación básica (normalmente rápida — Cherry.tv tiene un onboarding más ligero que las redes cam legacy) antes de que la opción de codificador externo quede totalmente activa.",
        "tips": [
            ("Entrada más ligera, tráfico al alza", "El onboarding de Cherry.tv es más rápido que el de las plataformas legacy (sin revisión Docler estilo 72 horas). Combinado con el tráfico en crecimiento, es un buen sitio early-mover para construir base de seguidores antes de que se apriete la competencia."),
            ("Pagos en cripto disponibles", "Cherry.tv soporta retiro en cripto junto al fiat estándar — útil si estás en una región donde los pagos de las redes cam tradicionales son lentos o están restringidos."),
            ("Browser broadcaster vs externo", "El broadcaster por navegador es cómodo pero de fuente única. SplitCam vía External Encoder desbloquea escenas multicámara, overlays, filtros de belleza y fondo IA que la herramienta de navegador no puede hacer."),
            _T_ETH,
        ],
        "faq": [
            ("¿Cherry.tv soporta oficialmente codificadores externos como SplitCam?", "Sí — el Streamer Dashboard incluye External Encoder dentro de Broadcast Settings. La plataforma da una URL de servidor RTMP estándar y una stream key; OBS, SplitCam y otros codificadores RTMP se conectan sin problema."),
            ("¿De dónde saco mi stream key de Cherry.tv?", "Streamer Dashboard → Broadcast Settings → External Encoder. La URL del servidor y la stream key aparecen ahí — copia ambas en los campos de RTMP personalizado de SplitCam. La clave está ligada a la cuenta; trátala como una contraseña."),
            ("¿Qué bitrate uso para Cherry.tv?", "Cherry.tv acepta los ajustes cam-quality estándar — lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test integrado de SplitCam."),
            ("¿SplitCam es gratis para usar con Cherry.tv?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de Cherry.tv es gratis de activar. Coste total de broadcaster: cero."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua. Es el codificador que envía tu vídeo a Cherry.tv."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — todo se aplica en vivo. La audiencia de Cherry.tv es más joven y más experta en plataformas, así que una escena pulida ayuda a destacar."),
            ("Saca tu URL y stream key de Cherry.tv",
             "Inicia sesión en tu cuenta de streamer de Cherry.tv, abre el <strong>Streamer Dashboard</strong> y entra en <strong>Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> única. Copia ambas."),
            ("Conecta SplitCam a Cherry.tv",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de Cherry.tv y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos. Lanza primero el speed test integrado."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde el Streamer Dashboard en Cherry.tv. En unos 10 segundos tu señal llega a Cherry.tv. Las próximas emisiones son de un clic — abre SplitCam, Go Live y ponte online en Cherry.tv."),
        ],
    },
    {
        "slug": "amateurtv", "name": "AmateurTV",
        "title": "Cómo transmitir en AmateurTV con SplitCam — RTMP",
        "desc": "Cómo transmitir en AmateurTV con SplitCam gratis — codificador externo del Model Panel, red cam en español, escenas y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en amateurtv, amateurtv, amateur.tv, amateurtv broadcast, amateurtv obs, amateurtv external encoder, amateurtv rtmp, amateurtv stream key",
        "h1html": 'Cómo transmitir en <span class="accent">AmateurTV</span> con SplitCam',
        "h1short": "Transmitir en AmateurTV",
        "card": "Configuración del codificador externo para la red hispanohablante de AmateurTV.",
        "intro": "AmateurTV es la red cam hispanohablante por excelencia — tráfico fuerte en España, México, Argentina y toda LatAm, con un público que prefiere hablar y consumir en español. El broadcaster por defecto del Model Panel va por navegador, pero también expone una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y te deja transmitir con escenas multicámara, filtros de belleza y overlays a un público hispano que las redes US-centric no atienden igual de bien.",
        "quick": "Para transmitir en AmateurTV con SplitCam: instala SplitCam, monta tu escena, en el Model Panel entra a <em>Broadcast Settings → External Encoder</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del Model Panel.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de modelo de AmateurTV, abre el <strong>Model Panel</strong> y entra en <strong>Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. Las cuentas nuevas necesitan verificación de ID antes de salir al aire.",
        "tips": [
            ("Habla en español, siempre", "El tráfico de AmateurTV es abrumadoramente hispanohablante — España de día, LatAm en horario tarde-noche americano. Títulos de sala, texto en pantalla y overlays en español rinden muchísimo más que cualquier inglés solo. Si eres latina o española, esta red juega en tu cancha."),
            ("Horario LatAm = tu mejor turno", "El pico de tráfico coincide con la tarde-noche de LatAm (UTC-3 a UTC-6). Si tienes flexibilidad, emitir de madrugada en horario europeo / mañana asiática pega de lleno con los picos de España y LatAm a la vez."),
            ("Pagos mid-tier estables", "No es el RPM más alto del sector, pero AmateurTV paga puntual y el nicho hispano tiene mucha menos competencia que las top de EE. UU. Para alguien que empieza en habla hispana, es una de las rampas más sanas."),
            _T_ETH,
        ],
        "faq": [
            ("¿AmateurTV soporta oficialmente codificadores externos como SplitCam?", "Sí — el Model Panel incluye la opción External Encoder dentro de Broadcast Settings. AmateurTV da una URL de servidor RTMP estándar y una stream key; OBS, SplitCam, vMix y cualquier codificador RTMP se conectan sin problema."),
            ("¿De dónde saco mi stream key de AmateurTV?", "Model Panel → Broadcast Settings → External Encoder. Tanto la URL del servidor como la stream key aparecen ahí. Cópialas en los campos de RTMP personalizado de SplitCam. La clave está ligada a la cuenta."),
            ("¿Qué bitrate uso para AmateurTV?", "Configuración cam-quality estándar — lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test integrado de SplitCam."),
            ("¿SplitCam es gratis para usar con AmateurTV?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de AmateurTV es gratis de activar."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua. Es el codificador que envía tu vídeo a AmateurTV."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA. Pon los textos de overlay en español — la audiencia hispana de AmateurTV lo nota y convierte mejor."),
            ("Saca tu URL y stream key de AmateurTV",
             "Inicia sesión en tu cuenta de modelo de AmateurTV, abre el <strong>Model Panel</strong> y entra en <strong>Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> única. Copia ambas."),
            ("Conecta SplitCam a AmateurTV",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de AmateurTV y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos. Lanza primero el speed test integrado."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde el Model Panel de AmateurTV. En unos 10 segundos tu señal llega a la red. Las próximas emisiones son de un clic — abre SplitCam, Go Live."),
        ],
    },
    {
        "slug": "camster", "name": "Camster",
        "title": "Cómo transmitir en Camster con SplitCam — RTMP",
        "desc": "Cómo transmitir en Camster con SplitCam gratis — codificador externo del Model Hub, clave RTMP, escenas multicámara y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en camster, camster, camster broadcast, camster obs, camster external encoder, camster rtmp, camster stream key",
        "h1html": 'Cómo transmitir en <span class="accent">Camster</span> con SplitCam',
        "h1short": "Transmitir en Camster",
        "card": "Configuración del codificador externo para el Model Hub de Camster.",
        "intro": "Camster es una plataforma cam mid-tier asentada — más pequeña que Chaturbate o LiveJasmin, pero con una base de usuarios fiel y pagos razonables. El broadcaster por defecto del Model Hub va por navegador, pero también expone una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y te deja transmitir con escenas multicámara, overlays y filtros que el broadcaster nativo no puede dar.",
        "quick": "Para transmitir en Camster con SplitCam: instala SplitCam, monta tu escena, en el Model Hub entra a <em>Broadcast Settings → External Encoder</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del Model Hub.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de modelo de Camster, abre el <strong>Model Hub</strong> y entra en <strong>Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. La clave está ligada a la cuenta; trátala como una contraseña.",
        "tips": [
            ("Mid-tier = menos competencia", "Camster tiene tráfico estable pero menos broadcasters que las redes top — es más fácil aparecer en portada con una escena cuidada y un horario constante."),
            ("Broadcaster del navegador vs externo", "El broadcaster por navegador es de fuente única. SplitCam vía External Encoder desbloquea escenas multicámara, overlays, filtros de belleza y fondo IA."),
            ("Pagos estables y split justo", "El split de Camster es razonable para el mid-tier — no es el más alto del sector, pero los pagos mensuales llegan puntuales y casi no hay quejas de retrasos."),
            _T_ETH,
        ],
        "faq": [
            ("¿Camster soporta oficialmente codificadores externos como SplitCam?", "Sí — el Model Hub incluye la opción External Encoder dentro de Broadcast Settings. URL de servidor RTMP estándar y stream key; OBS, SplitCam y cualquier codificador RTMP se conectan."),
            ("¿De dónde saco mi stream key de Camster?", "Model Hub → Broadcast Settings → External Encoder. Tanto la URL del servidor como la stream key aparecen ahí. Cópialas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para Camster?", "Configuración cam-quality estándar — lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test integrado de SplitCam."),
            ("¿SplitCam es gratis para usar con Camster?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de Camster es gratis."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — todo se aplica en vivo."),
            ("Saca tu URL y stream key de Camster",
             "Inicia sesión en tu cuenta de modelo de Camster, abre el <strong>Model Hub</strong> y entra en <strong>Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> única. Copia ambas."),
            ("Conecta SplitCam a Camster",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de Camster y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos. Lanza primero el speed test integrado."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde el Model Hub. En unos 10 segundos tu señal llega a Camster."),
        ],
    },
    {
        "slug": "camversity", "name": "Camversity",
        "title": "Cómo transmitir en Camversity con SplitCam — RTMP",
        "desc": "Cómo transmitir en Camversity con SplitCam gratis — codificador externo del Performer Dashboard, clave RTMP, escenas y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en camversity, camversity, camversity broadcast, camversity obs, camversity external encoder, camversity rtmp, camversity stream key",
        "h1html": 'Cómo transmitir en <span class="accent">Camversity</span> con SplitCam',
        "h1short": "Transmitir en Camversity",
        "card": "Configuración del codificador externo para el Performer Dashboard de Camversity.",
        "intro": "Camversity es una plataforma cam independiente en pleno crecimiento, con foco en herramientas pensadas para el performer y comisiones más bajas que las redes legacy. El broadcaster por defecto del Performer Dashboard va por navegador, pero también expone una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y te deja transmitir con escenas multicámara, overlays y filtros.",
        "quick": "Para transmitir en Camversity con SplitCam: instala SplitCam, monta tu escena, en el Performer Dashboard abre <em>Stream Settings → External Encoder</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del Performer Dashboard.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de performer de Camversity, abre el <strong>Performer Dashboard</strong> y entra en <strong>Stream Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. Las cuentas nuevas pasan una verificación de ID estándar antes de salir al aire.",
        "tips": [
            ("Split más amable con el performer", "El reparto de Camversity favorece más al performer que las redes legacy — vale la pena compararlo con tu plataforma principal si estás empezando en cam."),
            ("Onboarding más ligero que Docler", "La verificación de Camversity es más rápida que la espera de 48–72 horas de LiveJasmin, sin dejar de ser legítima (nada de modelos sin verificar). Buen punto medio."),
            ("Monta escena, no solo webcam", "El broadcaster por defecto del Performer Dashboard es de fuente única. SplitCam vía External Encoder desbloquea multicámara, overlays y filtros de belleza."),
            _T_ETH,
        ],
        "faq": [
            ("¿Camversity soporta oficialmente codificadores externos como SplitCam?", "Sí — el Performer Dashboard incluye la opción External Encoder dentro de Stream Settings. URL de servidor RTMP estándar y stream key; OBS, SplitCam, vMix se conectan."),
            ("¿De dónde saco mi stream key de Camversity?", "Performer Dashboard → Stream Settings → External Encoder. Tanto la URL del servidor como la stream key aparecen ahí."),
            ("¿Qué bitrate uso para Camversity?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test integrado de SplitCam."),
            ("¿SplitCam es gratis para usar con Camversity?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de Camversity es gratis."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA."),
            ("Saca tu URL y stream key de Camversity",
             "Inicia sesión en tu cuenta de performer de Camversity, abre el <strong>Performer Dashboard</strong> y entra en <strong>Stream Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> única. Copia ambas."),
            ("Conecta SplitCam a Camversity",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de Camversity y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde el Performer Dashboard. En unos 10 segundos tu señal llega a Camversity."),
        ],
    },
    {
        "slug": "skyprivate", "name": "SkyPrivate",
        "title": "Cómo usar SkyPrivate con SplitCam — cámara virtual",
        "desc": "Cómo usar SkyPrivate con SplitCam gratis como cámara virtual — llamadas cam privadas por Skype, escenas multicámara y filtros. Sin marca de agua.",
        "kw": "cómo usar skyprivate, skyprivate, sky private cam, skyprivate virtual camera, skyprivate cámara virtual, skype cam privado, skyprivate splitcam",
        "h1html": 'Cómo usar <span class="accent">SkyPrivate</span> con SplitCam',
        "h1short": "SplitCam en SkyPrivate",
        "card": "Configuración de cámara virtual para las llamadas cam de SkyPrivate basadas en Skype.",
        "intro": "SkyPrivate es una plataforma cam única — en lugar de un broadcast RTMP, monetiza <strong>llamadas cam privadas pay-per-minute por Skype</strong>. El cliente reserva y paga por minuto en el marketplace de SkyPrivate, y la videollamada en sí va por Skype. <strong style='color:var(--text)'>SplitCam</strong> gratis se conecta como <strong>cámara virtual</strong>: monta tu escena en SplitCam y luego elige SplitCam como cámara dentro de Skype antes de aceptar una llamada reservada por SkyPrivate.",
        "quick": "Para usar SkyPrivate con SplitCam: instala SplitCam, monta tu escena, instala Skype con el add-on de SkyPrivate, en <em>Video Settings</em> de Skype elige SplitCam como cámara y micrófono, y atiende las llamadas reservadas por SkyPrivate — Skype entrega tu escena ya compuesta al cliente."
                 "<ol><li>Instala SplitCam.</li><li>Monta la escena en SplitCam.</li>"
                 "<li>Instala Skype + add-on de SkyPrivate.</li>"
                 "<li>Elige SplitCam como cámara en Skype.</li>"
                 "<li>Atiende las llamadas.</li></ol>",
        "key_how": "SkyPrivate no usa RTMP ni stream key — usa Skype como transporte de vídeo con un add-on de facturación por minuto. Instala Skype, instala el add-on de navegador/escritorio de SkyPrivate y luego en Skype abre <strong>Settings → Audio &amp; Video → Camera</strong> y elige <strong>SplitCam</strong> en lugar de tu webcam. La escena compuesta de SplitCam (overlays, multicámara, filtros de belleza) es lo que ve el cliente de SkyPrivate a través de Skype.",
        "tips": [
            ("Sin RTMP — flujo de cámara virtual", "No busques URL de servidor ni stream key. SkyPrivate va por Skype, y Skype simplemente ve a SplitCam como un dispositivo de webcam. Monta la escena en SplitCam y luego elige SplitCam en los ajustes de cámara de Skype."),
            ("Pon SplitCam también como micrófono", "En Audio de Skype elige SplitCam como micrófono además de cámara — así llegan al cliente la supresión de ruido, el audio mezclado y la música de intro."),
            ("Haz una llamada de prueba en Skype", "Antes de tu primera llamada de pago de SkyPrivate, lanza una llamada de prueba gratuita en Skype (Echo / Sound Test Service) para confirmar que SplitCam es la cámara activa y que la escena se compone bien."),
            _T_TEST,
        ],
        "faq": [
            ("¿SkyPrivate usa RTMP o stream key?", "Ninguno de los dos. SkyPrivate gestiona la reserva y la facturación; el vídeo real va por Skype. No te hace falta URL de servidor RTMP ni stream key — basta con configurar SplitCam como cámara dentro de Skype."),
            ("¿Cómo selecciono SplitCam en Skype para SkyPrivate?", "Abre Skype Settings → Audio &amp; Video → Camera y elige SplitCam de la lista. Haz lo mismo en Microphone. Las llamadas de SkyPrivate llegan como llamadas normales de Skype con tu escena de SplitCam de cámara."),
            ("¿Puedo usar overlays y filtros de belleza con SkyPrivate?", "Sí — móntalos dentro de tu escena de SplitCam. Skype solo recibe el resultado compuesto como una única cámara, así que todo lo que SplitCam componga (overlays, filtros de belleza, fondo IA, escenas multicámara) lo ve el cliente de SkyPrivate."),
            ("¿SplitCam es gratis para SkyPrivate?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. Como cámara virtual para las llamadas SkyPrivate vía Skype no añade coste ni marca a la llamada."),
        ],
        "steps": [
            ("Instala SplitCam",
             "SplitCam es gratis para Windows y macOS — sin registro, sin tarjeta, sin marca de agua. Para SkyPrivate actúa como <strong>cámara virtual</strong> que Skype reconoce como una webcam más."),
            ("Monta tu escena en SplitCam",
             "Abre SplitCam y usa <strong>Media Layers +</strong> para añadir tu webcam más overlays, texto, filtros de belleza o fondo IA. Esa escena compuesta es lo que Skype entrega al cliente de SkyPrivate."),
            ("Instala Skype y el add-on de SkyPrivate",
             "Instala Skype en el mismo PC, inicia sesión y luego instala el add-on / app de escritorio de SkyPrivate siguiendo su onboarding. El add-on gestiona la facturación por minuto del lado de SkyPrivate."),
            ("Elige SplitCam como cámara y micro en Skype",
             "En Skype abre <strong>Settings → Audio &amp; Video</strong>. Pon <strong>Camera = SplitCam</strong> y <strong>Microphone = SplitCam</strong>. Lanza una llamada de prueba rápida en Skype (Echo / Sound Test Service) para comprobar que la escena se ve y se oye bien."),
            ("Atiende las llamadas de SkyPrivate",
             "Cuando un cliente de SkyPrivate reserve una llamada de pago llegará como llamada de Skype — acéptala. Ve tu escena compuesta de SplitCam; SkyPrivate cobra por minuto. Puedes ajustar la escena en mitad de la llamada editándola en SplitCam — Skype actualiza al instante."),
        ],
    },
    {
        "slug": "manyvids", "name": "ManyVids",
        "title": "Cómo transmitir en MV Live (ManyVids) con SplitCam",
        "desc": "Cómo transmitir en MV Live de ManyVids con SplitCam gratis — codificador externo del Creator Studio, clave RTMP, escenas y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en mv live, manyvids, mv live, manyvids live, manyvids broadcast, mv live obs, mv live external encoder, manyvids stream key",
        "h1html": 'Cómo transmitir en <span class="accent">MV Live</span> con SplitCam',
        "h1short": "Transmitir en MV Live",
        "card": "Configuración del codificador externo para el Creator Studio de MV Live (ManyVids).",
        "intro": "ManyVids es una plataforma de economía de creador — venta de clips, vídeos personalizados, suscripciones a fan club y el producto de directo <strong>MV Live</strong>. El broadcaster por defecto del Creator Studio va por navegador, pero también expone una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y te deja transmitir con escenas multicámara, overlays y filtros en la misma plataforma creator-friendly.",
        "quick": "Para transmitir en MV Live con SplitCam: instala SplitCam, monta tu escena, en el Creator Studio abre <em>MV Live → Broadcast Settings → External Encoder</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del Creator Studio.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de creator de ManyVids, abre el <strong>Creator Studio</strong> y entra en <strong>MV Live → Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. Las cuentas de creator tienen que estar totalmente verificadas (ID + impuestos) antes de que MV Live esté disponible.",
        "tips": [
            ("Economía de creador, no solo directo", "ManyVids no es una plataforma cam pura — MV Live es una vía de ingresos junto a la venta de clips, los vídeos personalizados y las suscripciones a fan club. Usa los directos para empujar al público hacia tus otras monetizaciones."),
            ("Tipping con tokens dentro de MV Live", "MV Live tiene su propio sistema de tipping con tokens dentro de la sala. Planifica menús de objetivos y triggers de recompensa estilo Chaturbate / Stripchat — convierten bien con el público de ManyVids."),
            ("Browser vs codificador externo", "El broadcaster en navegador del Creator Studio es de cámara única. SplitCam vía External Encoder desbloquea multicámara, overlays y filtros."),
            _T_ETH,
        ],
        "faq": [
            ("¿MV Live (ManyVids) soporta codificadores externos como SplitCam?", "Sí — la sección de MV Live del Creator Studio incluye la opción External Encoder dentro de Broadcast Settings. URL de servidor RTMP estándar y stream key; OBS, SplitCam, vMix se conectan."),
            ("¿De dónde saco mi stream key de MV Live?", "Creator Studio → MV Live → Broadcast Settings → External Encoder. URL del servidor y stream key aparecen ahí — copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para MV Live?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test integrado de SplitCam."),
            ("¿SplitCam es gratis para usar con MV Live?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de ManyVids es gratis en el Creator Studio."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — perfecto para los menús de objetivos y triggers de recompensa de MV Live."),
            ("Saca tu URL y stream key de MV Live",
             "Inicia sesión en tu cuenta de creator de ManyVids, abre el <strong>Creator Studio</strong> y entra en <strong>MV Live → Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> única. Copia ambas."),
            ("Conecta SplitCam a MV Live",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de MV Live y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego lanza la emisión de MV Live desde el Creator Studio. En unos 10 segundos tu señal llega a la audiencia de MV Live."),
        ],
    },
    {
        "slug": "fansly", "name": "Fansly",
        "title": "Cómo transmitir en directo en Fansly con SplitCam",
        "desc": "Cómo transmitir en Fansly Live con SplitCam gratis — codificador externo del Creator Dashboard, clave RTMP, escenas y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en directo en fansly, fansly, fansly live, fansly broadcast, fansly obs, fansly external encoder, fansly rtmp, fansly stream key",
        "h1html": 'Cómo transmitir en <span class="accent">Fansly Live</span> con SplitCam',
        "h1short": "Transmitir en Fansly",
        "card": "Configuración del codificador externo para el Creator Dashboard de Fansly.",
        "intro": "Fansly es un competidor directo de OnlyFans con reglas de contenido más permisivas y una base de creators en crecimiento — suscripciones, pay-per-view y el producto de directo <strong>Fansly Live</strong>. El broadcaster por defecto va por navegador, pero el <strong>Creator Dashboard</strong> también expone una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y te deja transmitir con escenas multicámara, overlays y filtros para tu base de suscriptores.",
        "quick": "Para transmitir en Fansly Live con SplitCam: instala SplitCam, monta tu escena, en el Creator Dashboard abre <em>Live → Broadcast Settings → External Encoder</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del Creator Dashboard.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de creator de Fansly, abre el <strong>Creator Dashboard</strong> y entra en <strong>Live → Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. Las cuentas de creator necesitan verificación de ID antes de que Fansly Live se active.",
        "tips": [
            ("Audiencia suscriptora primero", "El público de Fansly es de suscripción — tu directo llega a gente que ya te paga al mes. Planifica contenido que premie la fidelidad (Q&amp;A exclusivos, contenido entre bastidores, objetivos de propina personalizados) en vez de perseguir métricas de sala pública."),
            ("Propinas además de la suscripción", "Fansly Live soporta propinas en directo además de la suscripción base. Los ingresos combinados pueden superar al tipping de las plataformas cam puras para creators ya establecidos."),
            ("Broadcaster en navegador vs externo", "El broadcaster por defecto de navegador es de una sola fuente. SplitCam vía External Encoder desbloquea multicámara, overlays, filtros de belleza y fondo IA que igualan el acabado del contenido de pago para suscriptores."),
            _T_ETH,
        ],
        "faq": [
            ("¿Fansly Live soporta codificadores externos como SplitCam?", "Sí — la sección de Live del Creator Dashboard incluye la opción External Encoder dentro de Broadcast Settings. URL de servidor RTMP estándar y stream key; OBS, SplitCam, vMix se conectan."),
            ("¿De dónde saco mi stream key de Fansly?", "Creator Dashboard → Live → Broadcast Settings → External Encoder. URL del servidor y stream key aparecen ahí. Copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para Fansly Live?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test integrado de SplitCam."),
            ("¿SplitCam es gratis para usar con Fansly?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de Fansly es gratis en el Creator Dashboard."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — una escena pulida está a la altura de lo que esperan tus suscriptores de pago."),
            ("Saca tu URL y stream key de Fansly",
             "Inicia sesión en tu cuenta de creator de Fansly, abre el <strong>Creator Dashboard</strong> y entra en <strong>Live → Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> única. Copia ambas."),
            ("Conecta SplitCam a Fansly",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de Fansly y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego lanza la emisión de Fansly Live desde el Creator Dashboard. En unos 10 segundos tu señal llega a tus suscriptores de Fansly."),
        ],
    },
    {
        "slug": "ifriends", "name": "iFriends",
        "title": "Cómo transmitir en iFriends con SplitCam — RTMP",
        "desc": "Cómo transmitir en iFriends con SplitCam gratis — codificador externo del Model Center, clave RTMP, escenas multicámara y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en ifriends, ifriends, ifriends broadcast, ifriends obs, ifriends external encoder, ifriends rtmp, ifriends stream key",
        "h1html": 'Cómo transmitir en <span class="accent">iFriends</span> con SplitCam',
        "h1short": "Transmitir en iFriends",
        "card": "Configuración del codificador externo para el Model Center veterano de iFriends.",
        "intro": "iFriends (WebPower) es una de las redes cam independientes más veteranas — discretamente rentable, base de usuarios fiel y un <strong>Model Center</strong> creado antes de que los broadcasters por navegador fueran habituales. La plataforma admite una ruta estándar de <strong>External Encoder</strong> desde el Model Center a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y te deja transmitir con escenas multicámara modernas, overlays y filtros en esta red consolidada.",
        "quick": "Para transmitir en iFriends con SplitCam: instala SplitCam, monta tu escena, en el Model Center abre <em>Broadcast Settings → External Encoder</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del Model Center.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de modelo de iFriends, abre el <strong>Model Center</strong> y entra en <strong>Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. La aprobación de nuevas cuentas de modelo en iFriends es exigente pero legítima; una vez verificada, la opción de codificador externo queda disponible indefinidamente.",
        "tips": [
            ("Audiencia de cola larga, red veterana", "iFriends funciona desde finales de los 90 con una base de usuarios fiel — muchos son suscriptores de largo plazo, no visitantes nuevos. Ingresos estables para modelos consolidadas, crecimiento más lento para recién llegadas."),
            ("Broadcaster del navegador vs externo", "El broadcaster antiguo de iFriends se creó antes del UX multicámara moderno. Pasarte a SplitCam vía External Encoder es un salto notable — escenas multicámara, overlays y filtros de belleza que la herramienta antigua no puede dar."),
            ("Pagos estables, menos sorpresas", "La matriz de iFriends (WebPower) lleva décadas pagando a sus modelos con fiabilidad — calendarios de pago más lentos que las plataformas cripto-friendly nuevas, pero muy pocas historias de terror."),
            _T_ETH,
        ],
        "faq": [
            ("¿iFriends soporta oficialmente codificadores externos como SplitCam?", "Sí — el Model Center incluye una opción External Encoder dentro de Broadcast Settings. URL de servidor RTMP estándar y stream key; OBS, SplitCam, vMix se conectan una vez aprobada tu cuenta."),
            ("¿De dónde saco mi stream key de iFriends?", "Model Center → Broadcast Settings → External Encoder. URL del servidor y stream key aparecen ahí — copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para iFriends?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test integrado de SplitCam."),
            ("¿SplitCam es gratis para usar con iFriends?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de iFriends es gratis en el Model Center."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — una escena moderna y pulida destaca en esta red veterana."),
            ("Saca tu URL y stream key de iFriends",
             "Inicia sesión en tu cuenta de modelo de iFriends, abre el <strong>Model Center</strong> y entra en <strong>Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> única. Copia ambas."),
            ("Conecta SplitCam a iFriends",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de iFriends y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde el Model Center de iFriends. En unos 10 segundos tu señal llega a la red."),
        ],
    },
    {
        "slug": "babestation", "name": "Babestation",
        "title": "Cómo transmitir en Babestation con SplitCam — RTMP",
        "desc": "Cómo transmitir en Babestation con SplitCam gratis — codificador externo del Performer Hub, clave RTMP, escenas multicámara y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en babestation, babestation, babestation cam, babestation broadcast, babestation obs, babestation external encoder, babestation rtmp, babestation stream key",
        "h1html": 'Cómo transmitir en <span class="accent">Babestation</span> con SplitCam',
        "h1short": "Transmitir en Babestation",
        "card": "Configuración del codificador externo para el Performer Hub británico de Babestation.",
        "intro": "Babestation es la red británica líder de TV adulta y cam — un híbrido de canales de televisión y un producto cam en directo alimentado por performers conectadas al Performer Hub. La plataforma admite una ruta estándar de <strong>External Encoder</strong> desde el Performer Hub a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y permite a performers británicas independientes transmitir con escenas multicámara, overlays y filtros de belleza que superan al broadcaster por defecto, con estética de estudio de TV.",
        "quick": "Para transmitir en Babestation con SplitCam: instala SplitCam, monta tu escena, en el Performer Hub abre <em>Broadcast Settings → External Encoder</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del Performer Hub.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de performer de Babestation, abre el <strong>Performer Hub</strong> y entra en <strong>Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. El alta de performers en Reino Unido incluye verificación de ID por la normativa británica de verificación de edad.",
        "tips": [
            ("Audiencia y horario británicos primero", "El tráfico fuerte de Babestation es la franja de tarde-noche y madrugada en Reino Unido (GMT/BST). Si estás en otra zona horaria, emitir en horario nocturno británico rinde mucho más que tu prime time local."),
            ("Se espera acabado de estudio de TV", "La marca de Babestation va ligada a sus canales de televisión — el público espera escenarios y luz más producidos que un stream normal de webcam. Las escenas de SplitCam (overlays, texto branded, fondo IA) ayudan a igualar la estética pulida de la plataforma."),
            ("Performers independientes vs estudio", "Babestation trabaja tanto con estudios británicos como con performers independientes. Las performers independientes conectadas vía External Encoder tienen el mismo modelo de pago que las cámaras alimentadas por estudio."),
            _T_ETH,
        ],
        "faq": [
            ("¿Babestation soporta codificadores externos como SplitCam?", "Sí — el Performer Hub incluye una opción External Encoder dentro de Broadcast Settings. URL de servidor RTMP estándar y stream key; OBS, SplitCam, vMix se conectan una vez completada la verificación de performer."),
            ("¿De dónde saco mi stream key de Babestation?", "Performer Hub → Broadcast Settings → External Encoder. URL del servidor y stream key aparecen ahí — copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para Babestation?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. El ancho de subida en Reino Unido suele ir fino, pero lanza primero el speed test de SplitCam."),
            ("¿SplitCam es gratis para usar con Babestation?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de Babestation es gratis en el Performer Hub."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — iguala el acabado de estudio de TV de Babestation para destacar."),
            ("Saca tu URL y stream key de Babestation",
             "Inicia sesión en tu cuenta de performer de Babestation, abre el <strong>Performer Hub</strong> y entra en <strong>Broadcast Settings → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> única. Copia ambas."),
            ("Conecta SplitCam a Babestation",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de Babestation y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde el Performer Hub. En unos 10 segundos tu señal llega a la audiencia británica de Babestation."),
        ],
    },
    {
        "slug": "adultwork", "name": "AdultWork",
        "title": "Cómo transmitir en AdultWork con SplitCam — RTMP",
        "desc": "Cómo transmitir en AdultWork con SplitCam gratis — codificador externo del Members Area, clave RTMP, escenas multicámara y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en adultwork, adultwork, adultwork cam, adultwork broadcast, adultwork obs, adultwork external encoder, adultwork rtmp, adultwork stream key",
        "h1html": 'Cómo transmitir en <span class="accent">AdultWork</span> con SplitCam',
        "h1short": "Transmitir en AdultWork",
        "card": "Configuración del codificador externo para la función cam del Members Area británico de AdultWork.",
        "intro": "AdultWork es el marketplace británico consolidado de servicios adultos — conocido sobre todo por reservas de escort, venta de fotos / vídeos y servicios de teléfono, con una <strong>función webcam</strong> en directo al lado. La plataforma admite una ruta estándar de <strong>External Encoder</strong> desde el Members Area a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y deja a performers británicas independientes sumar ingresos de cam en directo con escenas multicámara, overlays y filtros.",
        "quick": "Para transmitir en AdultWork con SplitCam: instala SplitCam, monta tu escena, en el Members Area abre <em>Members → Broadcasting → External Encoder</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key desde el Members Area.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de performer de AdultWork, abre el <strong>Members Area</strong> y entra en <strong>Members → Broadcasting → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. La verificación en AdultWork es obligatoria para la función de cam en directo y cubre el cumplimiento de la verificación de edad en Reino Unido.",
        "tips": [
            ("Cross-sell desde otros servicios de AdultWork", "La fuerza de AdultWork es su base de clientes existente — quien te ve igual ya reserva tus fotos / vídeos / servicios de teléfono. Usa los streams en directo para hacer cross-sell con clientes que aún no han probado tu cam, no para perseguir desconocidos."),
            ("El Members Area es la puerta de entrada", "No busques el broadcaster en la parte pública — todo lo de performer está dentro del Members Area. Ajustes de emisión, pagos, gestión de contenido viven ahí."),
            ("Centrado en Reino Unido pero con pagos internacionales", "La mayoría del tráfico es de Reino Unido / UE. Los pagos funcionan a nivel internacional vía transferencia bancaria / monedero electrónico estándar, con calendarios semanales habituales en la plataforma."),
            _T_ETH,
        ],
        "faq": [
            ("¿AdultWork soporta codificadores externos como SplitCam?", "Sí — el Members Area incluye una opción External Encoder dentro de Broadcasting. URL de servidor RTMP estándar y stream key; OBS, SplitCam, vMix se conectan una vez verificada la performer."),
            ("¿De dónde saco mi stream key de AdultWork?", "Members Area → Members → Broadcasting → External Encoder. URL del servidor y stream key aparecen ahí — copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para AdultWork?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test integrado de SplitCam."),
            ("¿SplitCam es gratis para usar con AdultWork?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de AdultWork es gratis en el Members Area."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — usa overlays para anunciar tu contenido de AdultWork / servicios de teléfono y hacer cross-sell durante el directo."),
            ("Saca tu URL y stream key de AdultWork",
             "Inicia sesión en tu cuenta de performer de AdultWork, abre el <strong>Members Area</strong> y entra en <strong>Members → Broadcasting → External Encoder</strong>. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> única. Copia ambas."),
            ("Conecta SplitCam a AdultWork",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de AdultWork y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde el Members Area. En unos 10 segundos tu señal llega a la audiencia de AdultWork."),
        ],
    },
    {
        "slug": "jerkmate", "name": "Jerkmate",
        "title": "Cómo transmitir en Jerkmate con SplitCam — Streamate",
        "desc": "Cómo transmitir en Jerkmate con SplitCam gratis — Jerkmate emite por la red Streamate vía SM Connect, escenas multicámara y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en jerkmate, jerkmate, jerkmate streamate, jerkmate sm connect, jerkmate broadcast, jerkmate obs, ser modelo de jerkmate, jerkmate cam",
        "h1html": 'Cómo transmitir en <span class="accent">Jerkmate</span> con SplitCam',
        "h1short": "Transmitir en Jerkmate",
        "card": "Jerkmate saca sus modelos de la red Streamate — emite vía SM Connect + SplitCam.",
        "intro": "Jerkmate es una de las marcas cam más buscadas, conocida por su emparejador con IA que conecta a los espectadores con modelos en directo. No tiene broadcaster propio — Jerkmate <strong>saca sus modelos en directo de la red Streamate</strong>. Emites como modelo de la red Streamate y tu show se distribuye a Jerkmate y a sus sitios asociados. Como Streamate viene <strong style='color:var(--text)'>preconfigurado dentro de SplitCam</strong> en la lista de canales, <strong style='color:var(--text)'>SplitCam</strong> gratis te deja añadir escenas multicámara, superposiciones y filtros sin escribir ninguna URL RTMP a mano.",
        "quick": "Emite en Jerkmate con SplitCam: instala SplitCam, monta tu escena, date de alta como modelo en la red Streamate que alimenta Jerkmate, abre <em>SM Connect → Start Show</em> y copia la clave, luego en SplitCam abre <em>Stream Settings → Add Channel → Streamate</em>, pégala y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Date de alta como modelo de la red Streamate.</li>"
                 "<li>Consigue la clave vía SM Connect.</li>"
                 "<li>Add Channel → Streamate, Go Live.</li></ol>",
        "key_how": "Las cams en directo de Jerkmate vienen de la <strong>red de emisión Streamate</strong> — no existe un \"Jerkmate encoder\" aparte. Date de alta por el programa de modelos de Jerkmate o directamente en la red Streamate, abre <strong>SM Connect</strong>, acepta los términos, pulsa <strong>Start Show</strong> y copia tu clave de stream. En SplitCam abre <strong>Stream Settings → Add Channel</strong>, elige <strong>Streamate</strong> de la lista integrada y pega la clave. Tu emisión llega entonces a Jerkmate y a los sitios asociados de la red a la vez.",
        "tips": [
            ("Por debajo es la red Streamate", "No busques un broadcaster específico de Jerkmate — emites en Streamate y Jerkmate lo redistribuye. Todo lo que sirve para Streamate (SM Connect, el canal integrado de SplitCam) sirve para Jerkmate."),
            ("Aprovecha el tráfico del emparejador con IA", "El matchmaker de Jerkmate canaliza espectadores hacia las modelos que encajan con sus gustos — una escena pulida de SplitCam, con superposiciones y buen encuadre, convierte a esos espectadores emparejados mucho mejor que una webcam plana."),
            ("Un solo feed, muchos sitios", "Emitir a la red Streamate te pone en Jerkmate y en sus sitios asociados a la vez — más alcance desde un único stream de SplitCam, sin configuración extra."),
            _T_ETH,
        ],
        "faq": [
            ("¿Jerkmate tiene su propio broadcaster o clave de stream?", "No — Jerkmate saca sus modelos en directo de la red Streamate. Emites como modelo de la red Streamate vía SM Connect y tu show aparece en Jerkmate automáticamente."),
            ("¿Cómo consigo mi clave de stream de Jerkmate?", "Por SM Connect, del lado de modelo de la red Streamate: acepta los términos → Start Show → copia la clave. Pégala en el canal Streamate integrado de SplitCam — sin URL RTMP manual."),
            ("¿Qué bitrate uso para Jerkmate?", "Fija 1080p a 30 fps. El feed de la red es adaptativo, así que un bitrate más bajo en una imagen fija es normal. Lanza el speed test de SplitCam y usa conexión por cable."),
            ("¿SplitCam es gratis para Jerkmate?", "Sí — SplitCam es gratis, sin marca de agua ni límite de tiempo. Streamate (que alimenta Jerkmate) es un canal integrado de SplitCam, así que no hay coste de codificador aparte."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete superposiciones, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — una escena potente convierte a los espectadores que Jerkmate te empareja."),
            ("Date de alta como modelo y consigue tu clave",
             "Regístrate por el programa de modelos de Jerkmate o directamente en la <strong>red Streamate</strong> que lo alimenta. Abre <strong>SM Connect</strong>, acepta los términos, pulsa <strong>Start Show</strong> y copia tu clave de stream."),
            ("Añade Streamate como canal en SplitCam",
             "Abre <strong>Stream Settings → Add Channel</strong>, elige <strong>Streamate</strong> de la lista integrada y pega la clave — sin URL RTMP manual. Fija la resolución en 1080p."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam — un slider verde confirma la conexión. Tu show sale por toda la red Streamate y aparece en Jerkmate."),
        ],
    },
    {
        "slug": "justforfans", "name": "JustForFans",
        "title": "Cómo transmitir en directo en JustForFans con SplitCam",
        "desc": "Cómo transmitir en directo en JustForFans con SplitCam gratis como cámara virtual — escenas multicámara, superposiciones y filtros. Sin marca de agua.",
        "kw": "cómo transmitir en directo en justforfans, justforfans, justforfans live, jff live stream, justforfans virtual camera, justforfans cámara virtual, justfor.fans cam",
        "h1html": 'Cómo transmitir en directo en <span class="accent">JustForFans</span> con SplitCam',
        "h1short": "Directo en JustForFans",
        "card": "Usa SplitCam como cámara virtual en el broadcaster en directo de JustForFans.",
        "intro": "JustForFans (JFF) es una plataforma de suscripción propiedad de creators — una alternativa veterana a OnlyFans fundada por performers, con suscripciones, pay-per-view y una función de directo basada en navegador. Su broadcaster en directo muestra una sola webcam plana; apuntarlo a <strong style='color:var(--text)'>SplitCam</strong> gratis como <strong>cámara virtual</strong> desbloquea escenas multicámara, superposiciones y filtros. Si tu creator dashboard también expone una opción de codificador externo / clave de stream, SplitCam se conecta por RTMP en su lugar.",
        "quick": "Emite en directo en JustForFans con SplitCam: instala SplitCam, monta tu escena, inicia una emisión en directo en JFF y en el selector de cámara del broadcaster elige <em>SplitCam</em> como webcam — luego ponte en directo."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Inicia una emisión en directo en JFF.</li>"
                 "<li>Elige SplitCam en el desplegable de cámara.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "El directo de JustForFans va por navegador. Monta tu escena en SplitCam — se registra como una webcam del sistema llamada <strong>\"SplitCam Video Driver\"</strong> — y luego abre el broadcaster en directo de JFF y, en el desplegable de cámara, elige <strong>SplitCam</strong> en vez de tu webcam normal. Tu escena compuesta sustituye la cámara plana. Si el creator dashboard de JFF ofrece una opción de <strong>codificador externo / clave de stream</strong>, pega esa clave en los campos de RTMP personalizado de SplitCam en su lugar.",
        "tips": [
            ("La cámara virtual funciona en cualquier sitio", "Aunque el directo de una plataforma sea solo de navegador, SplitCam aparece como una webcam seleccionable — así tu escena multicámara, superposiciones y filtros funcionan en JFF sin necesidad de ninguna clave de stream."),
            ("Propiedad de creators, hecha para performers", "JFF está gestionada por performers y mantiene una base de suscriptores fiel. Las superposiciones que promocionan tu PPV o suscripción convierten bien ante un público que ya paga."),
            ("Da permiso de cámara al navegador", "Si SplitCam no aparece en la lista de cámaras de JFF, asegúrate de tener SplitCam abierto primero y de que el navegador tenga permiso de cámara — luego recarga el broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("¿Cómo conecta SplitCam con JustForFans?", "El directo de JFF va por navegador, así que SplitCam se conecta como cámara virtual: elige SplitCam en el selector de cámara del broadcaster de JFF. No hace falta clave de stream."),
            ("¿Puedo usar superposiciones y varias cámaras en JFF?", "Sí — monta la escena en SplitCam (segunda cámara, superposiciones, filtros de belleza o fondo IA) y JFF ve la escena terminada como una sola webcam."),
            ("¿JustForFans admite OBS o codificadores externos?", "El directo de JFF es principalmente de navegador / webcam. Si tu creator dashboard muestra una opción de codificador externo o clave de stream, pégala en los campos de RTMP personalizado de SplitCam; si no, usa el método de cámara virtual."),
            ("¿SplitCam es gratis para usar con JustForFans?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua. Instala una cámara virtual que el navegador puede seleccionar."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete superposiciones, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — aplicados en directo."),
            ("Inicia una emisión en directo en JFF",
             "Inicia sesión en tu cuenta de creator de JustForFans y abre el broadcaster en directo para empezar una emisión para tus suscriptores."),
            ("Elige SplitCam como tu cámara",
             "En el desplegable de cámara del broadcaster de JFF, elige <strong>SplitCam</strong> en vez de tu webcam normal — tu escena compuesta sustituye la cámara plana. (O, si está disponible, pega la clave de codificador externo de JFF en los campos de RTMP personalizado de SplitCam.)"),
            ("Pulsa Go Live",
             "Inicia la emisión — tu escena de SplitCam, superposiciones y filtros llegan a tus suscriptores de JustForFans."),
        ],
    },
    {
        "slug": "fanvue", "name": "Fanvue",
        "title": "Cómo transmitir en directo en Fanvue con SplitCam",
        "desc": "Cómo transmitir en directo en Fanvue con SplitCam gratis como cámara virtual — escenas multicámara, superposiciones y filtros. Sin marca de agua.",
        "kw": "cómo transmitir en directo en fanvue, fanvue, fanvue live, fanvue stream, fanvue cámara virtual, fanvue virtual camera, fanvue creator",
        "h1html": 'Cómo transmitir en directo en <span class="accent">Fanvue</span> con SplitCam',
        "h1short": "Directo en Fanvue",
        "card": "Usa SplitCam como cámara virtual en el broadcaster en directo de Fanvue.",
        "intro": "Fanvue es una plataforma de suscripción británica en plena expansión — una alternativa a OnlyFans conocida por ser amable con creators y con la IA, con suscripciones, pay-per-view y directo. Su broadcaster en directo funciona en el navegador, así que apuntarlo a <strong style='color:var(--text)'>SplitCam</strong> gratis como <strong>cámara virtual</strong> desbloquea escenas multicámara, superposiciones y filtros. Si tu creator dashboard expone una opción de codificador externo / clave de stream, SplitCam se conecta por RTMP en su lugar.",
        "quick": "Emite en directo en Fanvue con SplitCam: instala SplitCam, monta tu escena, inicia una emisión en directo en Fanvue y en el selector de cámara del broadcaster elige <em>SplitCam</em> — luego ponte en directo."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Inicia una emisión en directo en Fanvue.</li>"
                 "<li>Elige SplitCam en el desplegable de cámara.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "El directo de Fanvue va por navegador. Monta tu escena en SplitCam — se registra como una webcam del sistema llamada <strong>\"SplitCam Video Driver\"</strong> — y luego abre el broadcaster en directo de Fanvue y, en el desplegable de cámara, elige <strong>SplitCam</strong> en vez de tu webcam normal. Si tu creator dashboard ofrece una opción de <strong>codificador externo / clave de stream</strong>, pega esa clave en los campos de RTMP personalizado de SplitCam en su lugar.",
        "tips": [
            ("La cámara virtual funciona en cualquier sitio", "Aunque el directo de una plataforma sea solo de navegador, SplitCam aparece como una webcam seleccionable — así tu escena multicámara, superposiciones y filtros funcionan en Fanvue sin necesidad de ninguna clave de stream."),
            ("Amable con creators y con la IA", "Fanvue da la bienvenida a creators de IA y paga con transparencia. Las superposiciones que promocionan tu suscripción o tu PPV convierten bien ante un público que ya está pagando."),
            ("Da permiso de cámara al navegador", "Si SplitCam no aparece en la lista de cámaras de Fanvue, asegúrate de tener SplitCam abierto primero y de que el navegador tenga permiso de cámara — luego recarga."),
            _T_TEST,
        ],
        "faq": [
            ("¿Cómo conecta SplitCam con Fanvue?", "El directo de Fanvue va por navegador, así que SplitCam se conecta como cámara virtual: elige SplitCam en el selector de cámara. No hace falta clave de stream."),
            ("¿Puedo usar superposiciones y varias cámaras en Fanvue?", "Sí — monta la escena en SplitCam (segunda cámara, superposiciones, filtros de belleza o fondo IA) y Fanvue ve la escena terminada como una sola webcam."),
            ("¿Fanvue admite OBS o codificadores externos?", "El directo de Fanvue es principalmente de navegador / webcam. Si tu dashboard muestra una opción de codificador externo o clave de stream, pégala en los campos de RTMP personalizado de SplitCam; si no, usa el método de cámara virtual."),
            ("¿SplitCam es gratis para usar con Fanvue?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua. Instala una cámara virtual que el navegador puede seleccionar."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete superposiciones, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA — aplicados en directo."),
            ("Inicia una emisión en directo en Fanvue",
             "Inicia sesión en tu cuenta de creator de Fanvue y abre el broadcaster en directo para empezar una emisión para tus suscriptores."),
            ("Elige SplitCam como tu cámara",
             "En el desplegable de cámara de Fanvue, elige <strong>SplitCam</strong> en vez de tu webcam normal — tu escena compuesta sustituye la cámara plana. (O, si está disponible, pega una clave de stream en los campos de RTMP personalizado de SplitCam.)"),
            ("Pulsa Go Live",
             "Inicia la emisión — tu escena de SplitCam, superposiciones y filtros llegan a tus suscriptores de Fanvue."),
        ],
    },
    {
        "slug": "loyalfans", "name": "LoyalFans",
        "title": "Cómo transmitir en directo en LoyalFans con SplitCam",
        "desc": "Cómo transmitir en directo en LoyalFans con SplitCam gratis como cámara virtual — escenas multicámara, superposiciones y filtros. Sin marca de agua.",
        "kw": "cómo transmitir en directo en loyalfans, loyalfans, loyalfans live, loyalfans stream, loyalfans cámara virtual, loyalfans virtual camera, loyal fans",
        "h1html": 'Cómo transmitir en directo en <span class="accent">LoyalFans</span> con SplitCam',
        "h1short": "Directo en LoyalFans",
        "card": "Usa SplitCam como cámara virtual en el broadcaster en directo de LoyalFans.",
        "intro": "LoyalFans es una plataforma de suscripción para creators — con suscripciones, pay-per-view, propinas y una función de <strong>cam en directo</strong> integrada. Su broadcaster en directo funciona en el navegador, así que conectar <strong style='color:var(--text)'>SplitCam</strong> gratis como <strong>cámara virtual</strong> suma escenas multicámara, superposiciones y filtros sobre la webcam estándar. Si tu dashboard expone una opción de codificador externo / clave de stream, SplitCam se conecta por RTMP en su lugar.",
        "quick": "Emite en directo en LoyalFans con SplitCam: instala SplitCam, monta tu escena, inicia una emisión en directo en LoyalFans y elige <em>SplitCam</em> en el selector de cámara del broadcaster — luego ponte en directo."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Inicia una emisión en directo en LoyalFans.</li>"
                 "<li>Elige SplitCam en el desplegable de cámara.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "El directo de LoyalFans va por navegador. Monta tu escena en SplitCam — se registra como una webcam del sistema llamada <strong>\"SplitCam Video Driver\"</strong> — y luego abre el broadcaster en directo de LoyalFans y elige <strong>SplitCam</strong> en el desplegable de cámara. Si en tu creator dashboard aparece una opción de <strong>clave de stream / codificador externo</strong>, pégala en los campos de RTMP personalizado de SplitCam en su lugar.",
        "tips": [
            ("Cámara virtual, sin clave", "El directo por navegador igual recibe tu escena completa de SplitCam — superposiciones, segunda cámara y filtros — con solo elegir SplitCam como webcam."),
            ("Las propinas premian la producción", "LoyalFans se apoya en las propinas; las superposiciones con metas de propina y una escena pulida empujan más a los tippers que una webcam plana."),
            ("Da permiso de cámara al navegador", "Si SplitCam no está en la lista de cámaras de LoyalFans, abre SplitCam primero, permite el acceso a la cámara en el navegador y recarga el broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("¿Cómo conecta SplitCam con LoyalFans?", "El directo de LoyalFans va por navegador, así que SplitCam se conecta como cámara virtual — elige SplitCam en el selector de cámara. No hace falta clave de stream."),
            ("¿Puedo usar superposiciones y varias cámaras en LoyalFans?", "Sí — compón la escena en SplitCam (segunda cámara, superposiciones, filtros de belleza o fondo IA); LoyalFans la ve como una sola webcam."),
            ("¿LoyalFans admite OBS o codificadores externos?", "Su directo es principalmente de navegador / webcam. Si tu dashboard muestra una opción de clave de stream, pégala en los campos de RTMP personalizado de SplitCam; si no, usa el método de cámara virtual."),
            ("¿SplitCam es gratis para usar con LoyalFans?", "Sí — gratis, sin marca de agua y sin límite de tiempo."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua. Instala una cámara virtual que el navegador puede seleccionar."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete superposiciones, texto de meta de propina, una segunda cámara o el móvil, filtros de belleza o un fondo IA."),
            ("Inicia una emisión en directo en LoyalFans",
             "Inicia sesión en tu cuenta de LoyalFans y abre el broadcaster en directo para ponerte en directo ante tus suscriptores."),
            ("Elige SplitCam como tu cámara",
             "En el desplegable de cámara de LoyalFans, elige <strong>SplitCam</strong> en vez de tu webcam normal — tu escena sustituye la cámara plana. (O, si está disponible, pega una clave de stream en los campos de RTMP personalizado de SplitCam.)"),
            ("Pulsa Go Live",
             "Inicia la emisión — tu escena de SplitCam llega a tu audiencia de LoyalFans."),
        ],
    },
    {
        "slug": "fancentro", "name": "FanCentro",
        "title": "Cómo transmitir en directo en FanCentro con SplitCam",
        "desc": "Cómo transmitir en directo en FanCentro con SplitCam gratis como cámara virtual — escenas multicámara, superposiciones y filtros. Sin marca de agua.",
        "kw": "cómo transmitir en directo en fancentro, fancentro, fancentro live, fancentro stream, fancentro cámara virtual, fancentro virtual camera, fan centro",
        "h1html": 'Cómo transmitir en directo en <span class="accent">FanCentro</span> con SplitCam',
        "h1short": "Directo en FanCentro",
        "card": "Usa SplitCam como cámara virtual en el broadcaster en directo de FanCentro.",
        "intro": "FanCentro es una plataforma veterana de monetización para creators — con suscripciones, mensajes de pay-per-view, contenido y directo. Su directo funciona en el navegador, así que conectar <strong style='color:var(--text)'>SplitCam</strong> gratis como <strong>cámara virtual</strong> suma escenas multicámara, superposiciones y filtros más allá de la webcam simple. Si tu dashboard expone una opción de codificador externo / clave de stream, SplitCam se conecta por RTMP en su lugar.",
        "quick": "Emite en directo en FanCentro con SplitCam: instala SplitCam, monta tu escena, inicia una emisión en directo en FanCentro y elige <em>SplitCam</em> en el selector de cámara del broadcaster — luego ponte en directo."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Inicia una emisión en directo en FanCentro.</li>"
                 "<li>Elige SplitCam en el desplegable de cámara.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "El directo de FanCentro va por navegador. Monta tu escena en SplitCam — se registra como una webcam del sistema llamada <strong>\"SplitCam Video Driver\"</strong> — y luego abre el broadcaster en directo de FanCentro y elige <strong>SplitCam</strong> en el desplegable de cámara. Si se ofrece una opción de <strong>clave de stream / codificador externo</strong>, pégala en los campos de RTMP personalizado de SplitCam en su lugar.",
        "tips": [
            ("La cámara virtual funciona en cualquier sitio", "El directo solo de navegador igual recibe tu escena completa de SplitCam — superposiciones, segunda cámara y filtros — eligiendo SplitCam como webcam."),
            ("Haz cross-sell de tu funnel", "FanCentro gira en torno a los funnels de creator y el PPV. Las superposiciones que promocionan tu suscripción o tus mensajes de pago convierten en compradores a tus espectadores en directo."),
            ("Da permiso de cámara al navegador", "Si SplitCam no aparece en la lista, abre SplitCam primero, permite el acceso a la cámara en el navegador y recarga el broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("¿Cómo conecta SplitCam con FanCentro?", "El directo de FanCentro va por navegador, así que SplitCam se conecta como cámara virtual — elige SplitCam en el selector de cámara. No hace falta clave de stream."),
            ("¿Puedo usar superposiciones y varias cámaras en FanCentro?", "Sí — monta la escena en SplitCam; FanCentro ve la escena terminada como una sola webcam."),
            ("¿FanCentro admite OBS o codificadores externos?", "Su directo es principalmente de navegador / webcam. Si en tu dashboard aparece una opción de clave de stream, pégala en los campos de RTMP personalizado de SplitCam; si no, usa el método de cámara virtual."),
            ("¿SplitCam es gratis para usar con FanCentro?", "Sí — gratis, sin marca de agua y sin límite de tiempo."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua. Instala una cámara virtual que el navegador puede seleccionar."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete superposiciones, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA."),
            ("Inicia una emisión en directo en FanCentro",
             "Inicia sesión en tu cuenta de FanCentro y abre el broadcaster en directo para ponerte en directo ante tus suscriptores."),
            ("Elige SplitCam como tu cámara",
             "En el desplegable de cámara de FanCentro, elige <strong>SplitCam</strong> en vez de tu webcam normal. (O, si está disponible, pega una clave de stream en los campos de RTMP personalizado de SplitCam.)"),
            ("Pulsa Go Live",
             "Inicia la emisión — tu escena de SplitCam llega a tus suscriptores de FanCentro."),
        ],
    },
    {
        "slug": "ismygirl", "name": "IsMyGirl",
        "title": "Cómo transmitir en directo en IsMyGirl con SplitCam",
        "desc": "Cómo transmitir en directo en IsMyGirl con SplitCam gratis como cámara virtual — escenas multicámara, superposiciones y filtros. Sin marca de agua.",
        "kw": "cómo transmitir en directo en ismygirl, ismygirl, ismygirl live, ismygirl stream, ismygirl cámara virtual, ismygirl virtual camera, is my girl",
        "h1html": 'Cómo transmitir en directo en <span class="accent">IsMyGirl</span> con SplitCam',
        "h1short": "Directo en IsMyGirl",
        "card": "Usa SplitCam como cámara virtual en el broadcaster en directo de IsMyGirl.",
        "intro": "IsMyGirl es una plataforma de suscripción para creators — una alternativa a OnlyFans con suscripciones, contenido de pago y directo, conocida por su soporte cercano a creators. Su broadcaster en directo funciona en el navegador, así que conectar <strong style='color:var(--text)'>SplitCam</strong> gratis como <strong>cámara virtual</strong> aporta escenas multicámara, superposiciones y filtros. Si tu dashboard expone una opción de codificador externo / clave de stream, SplitCam se conecta por RTMP en su lugar.",
        "quick": "Emite en directo en IsMyGirl con SplitCam: instala SplitCam, monta tu escena, inicia una emisión en directo en IsMyGirl y elige <em>SplitCam</em> en el selector de cámara del broadcaster — luego ponte en directo."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Inicia una emisión en directo en IsMyGirl.</li>"
                 "<li>Elige SplitCam en el desplegable de cámara.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "El directo de IsMyGirl va por navegador. Monta tu escena en SplitCam — se registra como una webcam del sistema llamada <strong>\"SplitCam Video Driver\"</strong> — y luego abre el broadcaster en directo de IsMyGirl y elige <strong>SplitCam</strong> en el desplegable de cámara. Si aparece una opción de <strong>clave de stream / codificador externo</strong>, pégala en los campos de RTMP personalizado de SplitCam en su lugar.",
        "tips": [
            ("Cámara virtual, sin clave", "El directo solo de navegador igual recibe tu escena completa de SplitCam — superposiciones, segunda cámara y filtros — eligiendo SplitCam como webcam."),
            ("Aprovecha el soporte a creators", "IsMyGirl presume de soporte y promoción fuertes para creators. Una escena pulida de SplitCam más superposiciones de cross-sell sacan el máximo partido al tráfico que te envían."),
            ("Da permiso de cámara al navegador", "Si SplitCam no aparece en la lista, abre SplitCam primero, permite el acceso a la cámara y recarga el broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("¿Cómo conecta SplitCam con IsMyGirl?", "El directo de IsMyGirl va por navegador, así que SplitCam se conecta como cámara virtual — elige SplitCam en el selector de cámara. No hace falta clave de stream."),
            ("¿Puedo usar superposiciones y varias cámaras en IsMyGirl?", "Sí — compón la escena en SplitCam; IsMyGirl la ve como una sola webcam."),
            ("¿IsMyGirl admite OBS o codificadores externos?", "Su directo es principalmente de navegador / webcam. Si aparece una opción de clave de stream, pégala en los campos de RTMP personalizado de SplitCam; si no, usa el método de cámara virtual."),
            ("¿SplitCam es gratis para usar con IsMyGirl?", "Sí — gratis, sin marca de agua y sin límite de tiempo."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua. Instala una cámara virtual que el navegador puede seleccionar."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete superposiciones, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA."),
            ("Inicia una emisión en directo en IsMyGirl",
             "Inicia sesión en tu cuenta de IsMyGirl y abre el broadcaster en directo para ponerte en directo ante tus suscriptores."),
            ("Elige SplitCam como tu cámara",
             "En el desplegable de cámara de IsMyGirl, elige <strong>SplitCam</strong> en vez de tu webcam normal. (O, si está disponible, pega una clave de stream en los campos de RTMP personalizado de SplitCam.)"),
            ("Pulsa Go Live",
             "Inicia la emisión — tu escena de SplitCam llega a tus suscriptores de IsMyGirl."),
        ],
    },
    {
        "slug": "dxlive", "name": "DXLive",
        "title": "Cómo transmitir en DXLive con SplitCam — RTMP",
        "desc": "Cómo transmitir en DXLive con SplitCam gratis — codificador externo de la red premium japonesa, escenas multicámara y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en dxlive, dxlive, dxlive broadcast, dxlive obs, dxlive external encoder, dxlive rtmp, dxlive performer",
        "h1html": 'Cómo transmitir en <span class="accent">DXLive</span> con SplitCam',
        "h1short": "Transmitir en DXLive",
        "card": "Configuración del codificador externo para la red cam premium de DXLive.",
        "intro": "DXLive es una red de webcam premium consolidada, popular en Japón y en toda Asia, construida sobre un modelo de pago por minuto con una audiencia fiel. El área de performer admite una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — y te deja transmitir con escenas multicámara, overlays y filtros de belleza en lugar de una sola webcam plana.",
        "quick": "Para transmitir en DXLive con SplitCam: instala SplitCam, monta tu escena, en el área de performer abre los ajustes de <em>codificador externo / emisión</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del área de performer.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de performer de DXLive y abre los ajustes de <strong>emisión / codificador externo</strong> en el área de performer. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. La verificación en DXLive es obligatoria antes de activar la función de cam en directo.",
        "tips": [
            ("Pensada para el mercado asiático", "La audiencia de DXLive se inclina hacia Japón / Asia y paga por minuto. Programa tus shows para las tardes en horario JST y esa base fiel y de pago convierte bien."),
            ("El acabado gana a la webcam cruda", "Una escena limpia de SplitCam con overlays y filtros de belleza destaca en una red premium de pago por minuto donde el público espera calidad."),
            ("Usa el codificador externo, no solo la webcam", "Enrutar por el RTMP de SplitCam en lugar de la cam básica del navegador es lo que desbloquea las escenas multicámara y los filtros."),
            _T_ETH,
        ],
        "faq": [
            ("¿DXLive soporta codificadores externos como SplitCam?", "Sí — el área de performer expone una ruta estándar de codificador externo / RTMP. Copia la URL del servidor y la stream key en SplitCam tras la verificación."),
            ("¿De dónde saco mi stream key de DXLive?", "En los ajustes de emisión / codificador externo del área de performer — la URL del servidor y la stream key aparecen ahí. Copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para DXLive?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test integrado de SplitCam."),
            ("¿SplitCam es gratis para usar con DXLive?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de DXLive es gratis en el área de performer."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA."),
            ("Saca tu URL y stream key de DXLive",
             "Inicia sesión en tu cuenta de performer de DXLive y abre los ajustes de <strong>emisión / codificador externo</strong>. Copia la <strong>URL de servidor</strong> y la <strong>stream key</strong>."),
            ("Conecta SplitCam a DXLive",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de DXLive y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde el área de performer. En unos 10 segundos tu señal llega a la audiencia de DXLive."),
        ],
    },
    {
        "slug": "streamen", "name": "Streamen",
        "title": "Cómo transmitir en Streamen con SplitCam — RTMP",
        "desc": "Cómo transmitir en Streamen con SplitCam gratis — codificador externo, escenas multicámara, overlays y filtros de belleza. Sin marca de agua.",
        "kw": "cómo transmitir en streamen, streamen, streamen broadcast, streamen obs, streamen external encoder, streamen rtmp, streamen.tv",
        "h1html": 'Cómo transmitir en <span class="accent">Streamen</span> con SplitCam',
        "h1short": "Transmitir en Streamen",
        "card": "Configuración del codificador externo para la plataforma cam Streamen.",
        "intro": "Streamen es una plataforma de cam en directo donde las modelos emiten ante una audiencia movida por las propinas. Sus ajustes de emisión exponen una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis — para que transmitas con escenas multicámara, overlays y filtros en lugar de una sola webcam simple.",
        "quick": "Para transmitir en Streamen con SplitCam: instala SplitCam, monta tu escena, en tu dashboard de modelo abre <em>ajustes de emisión → codificador externo</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del dashboard.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de modelo de Streamen y abre la sección de <strong>ajustes de emisión / codificador externo</strong>. Muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. La verificación de modelo es obligatoria antes de poder emitir.",
        "tips": [
            ("Audiencia movida por propinas", "Los espectadores de Streamen dan propinas — las metas de propina en pantalla y una escena pulida empujan más propinas que una webcam plana."),
            ("El codificador externo desbloquea escenas", "Enrutar por el RTMP de SplitCam en lugar de la cam básica del navegador es lo que habilita las composiciones multicámara, los overlays y los filtros."),
            ("Fija tu resolución", "Pon 1080p a mano para que el feed no baje calidad en silencio; que el bitrate caiga en una imagen fija es normal en feeds adaptativos."),
            _T_ETH,
        ],
        "faq": [
            ("¿Streamen soporta codificadores externos como SplitCam?", "Sí — los ajustes de emisión exponen una ruta estándar de codificador externo / RTMP. Copia la URL del servidor y la stream key en SplitCam tras la verificación."),
            ("¿De dónde saco mi stream key de Streamen?", "En los ajustes de emisión / codificador externo de tu dashboard de modelo — la URL del servidor y la stream key aparecen ahí. Copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para Streamen?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test de SplitCam."),
            ("¿SplitCam es gratis para usar con Streamen?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de Streamen es gratis en el dashboard."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto de meta de propina, una segunda cámara o el móvil, filtros de belleza o un fondo IA."),
            ("Saca tu URL y stream key de Streamen",
             "Inicia sesión en tu cuenta de modelo de Streamen, abre <strong>ajustes de emisión → codificador externo</strong> y copia la <strong>URL de servidor</strong> y la <strong>stream key</strong>."),
            ("Conecta SplitCam a Streamen",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de Streamen y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde tu dashboard. En unos 10 segundos tu señal llega a la audiencia de Streamen."),
        ],
    },
    {
        "slug": "xcams", "name": "XCams",
        "title": "Cómo transmitir en XCams con SplitCam — RTMP",
        "desc": "Cómo transmitir en XCams con SplitCam gratis — codificador externo para la comunidad cam europea, escenas multicámara y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en xcams, xcams, xcams broadcast, xcams obs, xcams external encoder, xcams rtmp, x cams",
        "h1html": 'Cómo transmitir en <span class="accent">XCams</span> con SplitCam',
        "h1short": "Transmitir en XCams",
        "card": "Configuración del codificador externo para la comunidad europea XCams.",
        "intro": "XCams es una comunidad europea de cam en directo — fuerte en Italia, Francia y España — construida en torno a shows en directo y una economía de propinas y shows privados. El área de modelo admite una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis, para que transmitas con escenas multicámara, overlays y filtros de belleza.",
        "quick": "Para transmitir en XCams con SplitCam: instala SplitCam, monta tu escena, en el área de modelo abre <em>emisión / codificador externo</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del área de modelo.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de modelo de XCams y abre los ajustes de <strong>emisión / codificador externo</strong> en el área de modelo. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. La verificación en XCams es obligatoria antes de emitir.",
        "tips": [
            ("Prime time europeo", "El tráfico de XCams alcanza su pico en las tardes europeas (CET). Emitir en esas horas rinde mucho más que fuera de pico en esta comunidad."),
            ("Los shows privados premian la calidad", "XCams funciona con shows privados / espía — una escena pulida de SplitCam con overlays convierte a los curiosos en privados de pago."),
            ("El codificador externo desbloquea escenas", "Enrutar por el RTMP de SplitCam en lugar de la cam del navegador habilita las composiciones multicámara, los overlays y los filtros."),
            _T_ETH,
        ],
        "faq": [
            ("¿XCams soporta codificadores externos como SplitCam?", "Sí — el área de modelo expone una ruta estándar de codificador externo / RTMP. Copia la URL del servidor y la stream key en SplitCam tras la verificación."),
            ("¿De dónde saco mi stream key de XCams?", "En los ajustes de emisión / codificador externo del área de modelo — la URL del servidor y la stream key aparecen ahí. Copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para XCams?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test de SplitCam."),
            ("¿SplitCam es gratis para usar con XCams?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de XCams es gratis en el área de modelo."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA."),
            ("Saca tu URL y stream key de XCams",
             "Inicia sesión en tu cuenta de modelo de XCams, abre <strong>emisión / codificador externo</strong> y copia la <strong>URL de servidor</strong> y la <strong>stream key</strong>."),
            ("Conecta SplitCam a XCams",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de XCams y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde el área de modelo. En unos 10 segundos tu señal llega a la audiencia de XCams."),
        ],
    },
    {
        "slug": "camcontacts", "name": "CamContacts",
        "title": "Cómo transmitir en CamContacts con SplitCam — RTMP",
        "desc": "Cómo transmitir en CamContacts con SplitCam gratis — codificador externo del sitio cam de pago por minuto, con escenas y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en camcontacts, camcontacts, camcontacts broadcast, camcontacts obs, camcontacts external encoder, camcontacts rtmp, cam contacts",
        "h1html": 'Cómo transmitir en <span class="accent">CamContacts</span> con SplitCam',
        "h1short": "Transmitir en CamContacts",
        "card": "Configuración del codificador externo para la cam de pago por minuto de CamContacts.",
        "intro": "CamContacts es uno de los sitios cam independientes más veteranos — un modelo de pago por minuto con una audiencia madura y fiel y fama de pagar con regularidad. El área de performer admite una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis, para que transmitas con escenas multicámara, overlays y filtros de belleza.",
        "quick": "Para transmitir en CamContacts con SplitCam: instala SplitCam, monta tu escena, en el área de performer abre los ajustes de <em>codificador externo / emisión</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del área de performer.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de performer de CamContacts y abre los ajustes de <strong>emisión / codificador externo</strong> en el área de performer. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. La verificación en CamContacts es obligatoria para la función de cam en directo.",
        "tips": [
            ("Audiencia madura y fiel", "CamContacts lleva décadas funcionando con miembros de largo plazo — regulares más estables y de mayor gasto que un sitio gratuito con mucha rotación, aunque con crecimiento más lento para recién llegadas."),
            ("El pago por minuto premia la retención", "Mantén a los espectadores en tiempo de pago con una escena pulida y overlays; el acabado alarga las sesiones en un modelo por minuto."),
            ("El codificador externo desbloquea escenas", "Enrutar por el RTMP de SplitCam en lugar de la cam básica habilita las composiciones multicámara, los overlays y los filtros."),
            _T_ETH,
        ],
        "faq": [
            ("¿CamContacts soporta codificadores externos como SplitCam?", "Sí — el área de performer expone una ruta estándar de codificador externo / RTMP. Copia la URL del servidor y la stream key en SplitCam tras la verificación."),
            ("¿De dónde saco mi stream key de CamContacts?", "En los ajustes de emisión / codificador externo del área de performer — la URL del servidor y la stream key aparecen ahí. Copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para CamContacts?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test de SplitCam."),
            ("¿SplitCam es gratis para usar con CamContacts?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de CamContacts es gratis en el área de performer."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA."),
            ("Saca tu URL y stream key de CamContacts",
             "Inicia sesión en tu cuenta de performer de CamContacts, abre los ajustes de <strong>emisión / codificador externo</strong> y copia la <strong>URL de servidor</strong> y la <strong>stream key</strong>."),
            ("Conecta SplitCam a CamContacts",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de CamContacts y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde el área de performer. En unos 10 segundos tu señal llega a la audiencia de CamContacts."),
        ],
    },
    {
        "slug": "royalcams", "name": "RoyalCams",
        "title": "Cómo transmitir en RoyalCams con SplitCam — RTMP",
        "desc": "Cómo transmitir en RoyalCams con SplitCam gratis — codificador externo del sitio cam por tokens, escenas y overlays. Sin marca de agua.",
        "kw": "cómo transmitir en royalcams, royalcams, royalcams broadcast, royalcams obs, royalcams external encoder, royalcams rtmp, royal cams",
        "h1html": 'Cómo transmitir en <span class="accent">RoyalCams</span> con SplitCam',
        "h1short": "Transmitir en RoyalCams",
        "card": "Configuración del codificador externo para el sitio cam por tokens de RoyalCams.",
        "intro": "RoyalCams es un sitio cam gratuito basado en tokens — salas públicas abiertas financiadas por propinas, con shows privados por encima. Los ajustes de emisión admiten una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis, para que transmitas con escenas multicámara, overlays y filtros de belleza en lugar de una sola webcam plana.",
        "quick": "Para transmitir en RoyalCams con SplitCam: instala SplitCam, monta tu escena, en tu dashboard de modelo abre <em>ajustes de emisión → codificador externo</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del dashboard.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de modelo de RoyalCams y abre la sección de <strong>ajustes de emisión / codificador externo</strong>. Muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. La verificación de modelo es obligatoria antes de emitir.",
        "tips": [
            ("Las salas por tokens premian la producción", "Las salas públicas de RoyalCams funcionan con propinas — las superposiciones con metas de propina y una escena pulida convierten a los curiosos en tippers y shows privados."),
            ("Reconduce hacia shows privados", "Usa una escena pública potente para hacer upsell de shows privados, donde están las ganancias reales en los sitios cam por tokens."),
            ("El codificador externo desbloquea escenas", "Enrutar por el RTMP de SplitCam en lugar de la cam del navegador habilita las composiciones multicámara, los overlays y los filtros."),
            _T_ETH,
        ],
        "faq": [
            ("¿RoyalCams soporta codificadores externos como SplitCam?", "Sí — los ajustes de emisión exponen una ruta estándar de codificador externo / RTMP. Copia la URL del servidor y la stream key en SplitCam tras la verificación."),
            ("¿De dónde saco mi stream key de RoyalCams?", "En los ajustes de emisión / codificador externo de tu dashboard de modelo — la URL del servidor y la stream key aparecen ahí. Copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para RoyalCams?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test de SplitCam."),
            ("¿SplitCam es gratis para usar con RoyalCams?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de RoyalCams es gratis en el dashboard."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto de meta de propina, una segunda cámara o el móvil, filtros de belleza o un fondo IA."),
            ("Saca tu URL y stream key de RoyalCams",
             "Inicia sesión en tu cuenta de modelo de RoyalCams, abre <strong>ajustes de emisión → codificador externo</strong> y copia la <strong>URL de servidor</strong> y la <strong>stream key</strong>."),
            ("Conecta SplitCam a RoyalCams",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de RoyalCams y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde tu dashboard. En unos 10 segundos tu señal llega a la audiencia de RoyalCams."),
        ],
    },
    {
        "slug": "modelhub", "name": "Modelhub",
        "title": "Cómo transmitir en Modelhub con SplitCam — RTMP",
        "desc": "Cómo transmitir en Modelhub Live con SplitCam gratis — codificador externo de la plataforma de creators de Pornhub. Sin marca de agua.",
        "kw": "cómo transmitir en modelhub, modelhub, modelhub live, modelhub broadcast, modelhub obs, modelhub external encoder, modelhub rtmp",
        "h1html": 'Cómo transmitir en <span class="accent">Modelhub</span> con SplitCam',
        "h1short": "Transmitir en Modelhub",
        "card": "Configuración del codificador externo para Modelhub Live (Pornhub).",
        "intro": "Modelhub es la plataforma de creators de Pornhub — venta de vídeos, suscripciones de fans y un producto de <strong>cam en directo</strong> con un enorme tráfico de entrada desde la red de Pornhub. El dashboard de modelo admite una ruta estándar de <strong>External Encoder</strong> a la que se conecta <strong style='color:var(--text)'>SplitCam</strong> gratis, para que transmitas con escenas multicámara, overlays y filtros de belleza.",
        "quick": "Para transmitir en Modelhub con SplitCam: instala SplitCam, monta tu escena, en el dashboard de modelo abre <em>Live → emisión / codificador externo</em>, copia la URL del servidor y la stream key, pégalas en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara + escena.</li>"
                 "<li>Saca URL y stream key del dashboard.</li>"
                 "<li>Pégalas en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en tu cuenta de modelo de Modelhub y abre los ajustes de <strong>Live / emisión / codificador externo</strong> en el dashboard. La página muestra una <strong>URL de servidor</strong> y una <strong>stream key</strong> ligadas a tu cuenta — copia ambas en los campos de RTMP personalizado de SplitCam. La verificación de modelo con la red es obligatoria antes de ponerte en directo.",
        "tips": [
            ("Enorme tráfico de entrada", "Modelhub atrae espectadores de la red de Pornhub — una escena pulida de SplitCam convierte a ese público amplio y casual en espectadores de pago y suscriptores."),
            ("Haz cross-sell de tus vídeos", "Usa overlays para dirigir a los espectadores en directo hacia tus vídeos de Modelhub y tu suscripción — la plataforma está pensada para ese funnel."),
            ("El codificador externo desbloquea escenas", "Enrutar por el RTMP de SplitCam en lugar de la cam básica habilita las composiciones multicámara, los overlays y los filtros."),
            _T_ETH,
        ],
        "faq": [
            ("¿Modelhub soporta codificadores externos como SplitCam?", "Sí — el dashboard de modelo expone una ruta estándar de codificador externo / RTMP para Modelhub Live. Copia la URL del servidor y la stream key en SplitCam tras la verificación."),
            ("¿De dónde saco mi stream key de Modelhub?", "En los ajustes de Live / emisión / codificador externo del dashboard — la URL del servidor y la stream key aparecen ahí. Copia ambas en los campos de RTMP personalizado de SplitCam."),
            ("¿Qué bitrate uso para Modelhub?", "Lanza 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe de 2 segundos. Lanza primero el speed test de SplitCam."),
            ("¿SplitCam es gratis para usar con Modelhub?", "Sí — SplitCam es gratis, sin marca de agua y sin límite de tiempo. La opción de codificador externo de Modelhub es gratis en el dashboard."),
        ],
        "steps": [
            ("Descarga e instala SplitCam",
             "SplitCam es software gratuito de streaming en directo para Windows y macOS — sin registro, sin tarjeta, sin marca de agua."),
            ("Monta tu escena",
             "Abre SplitCam y añade tu webcam. Mete overlays, texto, una segunda cámara o el móvil, filtros de belleza o un fondo IA."),
            ("Saca tu URL y stream key de Modelhub",
             "Inicia sesión en tu cuenta de modelo de Modelhub, abre <strong>Live → emisión / codificador externo</strong> y copia la <strong>URL de servidor</strong> y la <strong>stream key</strong>."),
            ("Conecta SplitCam a Modelhub",
             "En SplitCam abre <strong>Stream Settings</strong>, pega la URL del servidor de Modelhub y la stream key en los campos de RTMP personalizado. Pon bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe de 2 segundos."),
            ("Pulsa Go Live",
             "Pulsa <strong>Go Live</strong> en SplitCam y luego ponte online desde el dashboard. En unos 10 segundos tu señal llega a la audiencia de Modelhub."),
        ],
    },
]
