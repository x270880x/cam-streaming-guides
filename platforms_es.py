# -*- coding: utf-8 -*-
"""Spanish content for cam-streaming-guides. One dict per platform (all 19)."""

_TIPS_ES = {
    "eth": ("Conexión por cable", "Ethernet es más estable que el Wi-Fi. Un fotograma perdido en "
            "directo es una propina perdida — mantén la conexión sólida."),
    "ovl": ("Superposiciones en SplitCam", "Añade texto de objetivos, tus redes y un logo como "
            "capas de escena. El emisor del navegador no puede; SplitCam sí."),
    "test": ("Haz una prueba privada", "Una emisión de prueba corta verifica cámara, audio y "
             "encuadre antes de abrir la sala."),
    "hw": ("Codificación por hardware", "SplitCam detecta NVENC / QuickSync / AMF — la "
           "codificación corre en la GPU y el equipo no se ralentiza."),
}


def _p(slug, name):
    return {
        "slug": slug, "name": name,
        "title": f"Cómo emitir en {name} con SplitCam — guía gratuita",
        "desc": f"Guía paso a paso para emitir en {name} con SplitCam gratis — codificador RTMP "
                f"externo, escenas, superposiciones, sin marca de agua.",
        "kw": f"cómo emitir en {name.lower()}, {name.lower()} software de emisión, "
              f"{name.lower()} rtmp, {name.lower()} obs",
        "h1html": f'Cómo emitir en <span class="accent">{name}</span> con SplitCam',
        "h1short": f"Emitir en {name}",
        "card": f"Configuración del codificador externo para {name}.",
        "intro": f"El <strong style='color:var(--text)'>SplitCam</strong> gratuito funciona como "
                 f"tu codificador para {name} — escenas con varias cámaras, superposiciones, "
                 f"filtros y fondo con IA que el emisor básico no tiene. Sin marca de agua.",
        "quick": f"Para emitir en {name} con SplitCam: instala SplitCam, monta tu escena, activa "
                 f"la emisión externa (RTMP) en {name}, copia la URL del servidor y la clave de "
                 f"stream, pégalas en SplitCam y pulsa Go Live."
                 f"<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 f"<li>Consigue la clave RTMP de {name}.</li><li>Pégala en SplitCam.</li>"
                 f"<li>Pulsa Go Live.</li></ol>",
        "key_how": f"Inicia sesión en {name} y abre los ajustes de emisión. Cambia el método a "
                   f"<strong>codificador externo / OBS / RTMP</strong>. {name} mostrará una "
                   f"<strong>URL de servidor</strong> y una <strong>clave de stream</strong> — "
                   f"copia ambas. Mantén la clave en privado.",
        "tips": [_TIPS_ES["eth"], _TIPS_ES["ovl"], _TIPS_ES["test"], _TIPS_ES["hw"]],
        "faq": [
            (f"¿SplitCam es gratis para {name}?",
             "Sí — 100% gratis, sin marca de agua en tu emisión, sin límite de tiempo."),
            (f"¿Por qué usar SplitCam y no el emisor del navegador de {name}?",
             "El emisor del navegador es una sola cámara sin superposiciones. SplitCam añade "
             "escenas con varias cámaras, superposiciones de texto, filtros y codificación por "
             "hardware."),
            (f"¿Qué bitrate usar para {name}?",
             "3.500–6.000 Kbps para 1080p, 2.000–4.000 para 720p. Comprueba tu subida con el test "
             "de velocidad de SplitCam primero."),
            (f"¿Puedo emitir en {name} y otros sitios a la vez?",
             "Sí — la multiemisión de SplitCam envía un stream a varios sitios cam a la vez."),
        ],
    }


PLATFORMS_ES = [
    _p("chaturbate", "Chaturbate"),
    _p("cam4", "CAM4"),
    _p("bongacams", "BongaCams"),
    _p("stripchat", "Stripchat"),
    {**_p("onlyfans", "OnlyFans"),
     "title": "Cómo emitir en directo en OnlyFans con SplitCam — guía gratuita",
     "h1html": 'Cómo emitir en directo en <span class="accent">OnlyFans</span> con SplitCam',
     "h1short": "Directo en OnlyFans",
     "intro": "Usa el <strong style='color:var(--text)'>SplitCam</strong> gratuito para tu "
              "directo de OnlyFans — escenas con varias cámaras, superposiciones y filtros que la "
              "cámara básica de la app no tiene. Sin marca de agua.",
     "key_how": "En OnlyFans, inicia un nuevo directo y abre los <strong>ajustes de "
                "streaming</strong>. Elige emitir con software externo — OnlyFans mostrará una "
                "<strong>URL de servidor RTMP</strong> y una <strong>clave de stream</strong>. "
                "Copia ambas en SplitCam y mantén la clave en privado."},
    _p("camplace", "CamPlace"),
    _p("camsoda", "CamSoda"),
    _p("streamate", "Streamate"),
    _p("streamray", "StreamRay"),
    _p("xlovecam", "XLoveCam"),
    _p("soulcams", "SoulCams"),
    _p("imlive", "ImLive"),
    _p("vxlive", "VXLive"),
    _p("virtwish", "Virtwish"),
    _p("xmodels", "XModels"),
    _p("flirt4free", "Flirt4Free"),
    {
        "slug": "mfc-alerts", "name": "MyFreeCams",
        "title": "Cómo emitir en MyFreeCams y añadir alertas con SplitCam",
        "desc": "Emite en MyFreeCams con SplitCam gratis y muestra alertas de propinas en vivo "
                "como superposición. Paso a paso, sin marca de agua.",
        "kw": "cómo emitir en myfreecams, alertas mfc, myfreecams software de emisión, "
              "myfreecams obs",
        "h1html": 'Cómo emitir en <span class="accent">MyFreeCams</span> + alertas',
        "h1short": "Emitir en MyFreeCams",
        "card": "Emite en MyFreeCams y muestra alertas de propinas.",
        "intro": "El <strong style='color:var(--text)'>SplitCam</strong> gratuito es tu "
                 "codificador para MyFreeCams — y puede mostrar "
                 "<strong style='color:var(--text)'>alertas de propinas</strong> como capa de "
                 "escena usando un Browser Source. Sin marca de agua.",
        "quick": "Para emitir en MyFreeCams con alertas: instala SplitCam, monta tu escena, añade "
                 "tu página de alertas MFC como Browser Source, consigue la clave RTMP de "
                 "MyFreeCams, pégala en SplitCam y pulsa Go Live."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Añade las alertas MFC como Browser Source.</li>"
                 "<li>Pega la clave RTMP de MFC.</li><li>Pulsa Go Live.</li></ol>",
        "key_how": "Inicia sesión en MyFreeCams y abre los ajustes de emisión. Elige "
                   "<strong>codificador externo / RTMP</strong> para obtener la <strong>URL del "
                   "servidor</strong> y la <strong>clave de stream</strong>. Para mostrar "
                   "alertas, añade la página del widget de alertas MFC como capa "
                   "<strong>Browser Source</strong> en SplitCam.",
        "tips": [
            ("Browser Source para alertas", "Apunta un Browser Source de SplitCam a la URL del "
             "widget de alertas MFC — las notificaciones de propinas aparecen solas."),
            _TIPS_ES["eth"],
            ("Coloca bien las alertas", "Sitúa la superposición de alertas donde se vea pero no "
             "tape tu cámara."),
            ("Propina de prueba", "Envía una pequeña propina de prueba para confirmar que la "
             "superposición funciona."),
        ],
        "faq": [
            ("¿SplitCam es gratis para MyFreeCams?", "Sí — gratis, sin marca de agua, sin "
             "límites."),
            ("¿Cómo funcionan las alertas MFC en SplitCam?", "Añade tu página de alertas MFC "
             "como capa Browser Source; SplitCam la renderiza en vivo sobre tu cámara."),
            ("¿MyFreeCams admite codificadores externos?", "Sí — MyFreeCams acepta RTMP, así que "
             "SplitCam funciona como codificador."),
            ("¿Qué bitrate para MyFreeCams?", "3.500–6.000 Kbps a 1080p; comprueba la subida "
             "primero."),
        ],
    },
    {
        "slug": "lovense", "name": "Lovense",
        "title": "Cómo añadir un juguete Lovense a tu emisión con SplitCam",
        "desc": "Conecta un juguete interactivo Lovense a tu emisión cam y muéstralo en pantalla "
                "con SplitCam gratis. Paso a paso, sin marca de agua.",
        "kw": "cómo añadir lovense a la emisión, lovense cam stream, lovense splitcam, "
              "juguete interactivo lovense streaming",
        "h1html": 'Cómo añadir un <span class="accent">juguete Lovense</span> a tu emisión',
        "h1short": "Añadir un juguete Lovense",
        "card": "Conecta un juguete interactivo Lovense a tu emisión cam.",
        "intro": "Emite con el <strong style='color:var(--text)'>SplitCam</strong> gratuito y "
                 "vincula un juguete interactivo <strong style='color:var(--text)'>Lovense</strong> "
                 "para que reaccione a los tokens — con el estado visible en pantalla.",
        "quick": "Para añadir un juguete Lovense a tu emisión: instala SplitCam y el software de "
                 "Lovense, vincula el juguete, conecta Lovense a tu plataforma cam, añade el "
                 "estado de Lovense como Browser Source en SplitCam y emite normalmente."
                 "<ol><li>Instala SplitCam.</li><li>Instala y vincula el software de Lovense.</li>"
                 "<li>Conecta Lovense a tu sitio cam.</li>"
                 "<li>Añade la superposición de Lovense en SplitCam.</li>"
                 "<li>Pulsa Go Live.</li></ol>",
        "steps": [
            ("Instala SplitCam",
             "SplitCam es software de streaming gratuito para Windows y macOS — es el codificador "
             "que envía tu vídeo a tu plataforma cam. Descárgalo e instálalo; sin marca de agua."),
            ("Instala y vincula el software de Lovense",
             "Instala la app oficial Lovense Connect / Lovense Stream. Enciende tu juguete y "
             "vincúlalo por Bluetooth hasta que la app lo muestre conectado."),
            ("Conecta Lovense a tu plataforma cam",
             "En la app de Lovense, conecta tu cuenta del sitio cam para que el juguete reaccione "
             "a los tokens y propinas de los espectadores."),
            ("Añade la superposición de Lovense en SplitCam",
             "Lovense ofrece una URL de widget. Añádela como capa <strong>Browser Source</strong> "
             "en tu escena de SplitCam para que los espectadores vean el estado del juguete."),
            ("Monta tu escena y emite",
             "Añade tu cámara y otras superposiciones, pega la clave RTMP de tu plataforma cam en "
             "SplitCam y pulsa <strong>Go Live</strong>. El juguete reacciona a las propinas en "
             "tiempo real."),
        ],
        "tips": [
            ("Carga el juguete", "Una batería agotada a mitad de show mata la parte interactiva — "
             "cárgalo del todo antes de emitir."),
            ("Prueba la reacción", "Envía una pequeña propina de prueba para confirmar que el "
             "juguete reacciona."),
            ("Muestra la superposición", "Un estado de Lovense visible indica a los espectadores "
             "que dar propina hace algo — genera más propinas."),
            ("Bluetooth estable", "Mantén el juguete cerca del PC para evitar cortes."),
        ],
        "faq": [
            ("¿SplitCam es gratis para esto?", "Sí — SplitCam es gratis y sin marca de agua. El "
             "software de Lovense también es gratuito."),
            ("¿El juguete se conecta directo a SplitCam?", "No — el juguete se vincula con la app "
             "de Lovense; SplitCam solo muestra la superposición y emite tu cámara."),
            ("¿Qué sitios cam admiten Lovense?", "La mayoría de las grandes plataformas cam se "
             "integran con Lovense — consulta la lista actual en la app de Lovense."),
            ("¿Puedo mostrar propinas recientes en pantalla?", "Sí — añade la URL del widget de "
             "Lovense como Browser Source en SplitCam."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Varios sitios cam",
        "title": "Cómo emitir en varios sitios cam a la vez con SplitCam",
        "desc": "Emite en BongaCams, Chaturbate, CAM4, Stripchat y más al mismo tiempo con la "
                "multiemisión gratuita de SplitCam. Paso a paso, sin marca de agua.",
        "kw": "emitir en varios sitios cam, multiemisión cam, emitir en chaturbate y bongacams a "
              "la vez, software de multiemisión cam",
        "h1html": 'Cómo emitir en <span class="accent">varios sitios cam</span> a la vez',
        "h1short": "Multiemisión cam",
        "card": "Emite en varios sitios cam simultáneamente.",
        "intro": "El <strong style='color:var(--text)'>SplitCam</strong> gratuito puede emitir un "
                 "solo stream a <strong style='color:var(--text)'>varios sitios cam a la "
                 "vez</strong> — BongaCams, Chaturbate, CAM4, Stripchat y más. Sin marca de agua.",
        "quick": "Para emitir en varios sitios cam a la vez: instala SplitCam, monta tu escena, "
                 "consigue la URL del servidor RTMP y la clave de cada sitio cam, añádelas todas "
                 "en los ajustes de multiemisión de SplitCam y pulsa Go Live una vez."
                 "<ol><li>Instala SplitCam.</li><li>Añade cámara y escena.</li>"
                 "<li>Consigue una clave RTMP de cada sitio cam.</li>"
                 "<li>Añade todas las claves en la multiemisión de SplitCam.</li>"
                 "<li>Pulsa Go Live una vez.</li></ol>",
        "steps": [
            ("Instala SplitCam",
             "SplitCam es software de streaming gratuito para Windows y macOS con multiemisión "
             "integrada. Descárgalo e instálalo — sin marca de agua ni registro."),
            ("Configura tu cámara y escena",
             "Abre SplitCam, añade tu webcam y monta la escena con superposiciones y filtros. Una "
             "escena alimenta todos los destinos."),
            ("Consigue una clave RTMP de cada sitio cam",
             "En cada plataforma cam, activa la emisión externa / RTMP y copia su <strong>URL de "
             "servidor</strong> y su <strong>clave de stream</strong>. Repite para cada sitio."),
            ("Añade cada destino en SplitCam",
             "Abre <strong>Ajustes de stream</strong> y añade cada sitio cam como destino RTMP "
             "personalizado — pega su URL y clave. Marca todos los que quieras emitir."),
            ("Pulsa Go Live una vez",
             "Pulsa <strong>Go Live</strong>. SplitCam envía tu stream a todos los sitios cam "
             "seleccionados a la vez, peer-to-peer, desde una sola codificación — sin coste extra."),
        ],
        "tips": [
            ("Cuida tu subida", "La multiemisión multiplica la carga de subida. Cada destino "
             "consume su propio bitrate — asegúrate de que tu conexión soporta el total."),
            _TIPS_ES["eth"],
            ("Revisa las reglas", "Algunos sitios cam restringen emitir a la vez en otro lado — "
             "confírmalo antes de multiemitir."),
            ("Monitor de estado", "SplitCam muestra el estado por destino — quita un sitio si tu "
             "subida no da abasto."),
        ],
        "faq": [
            ("¿La multiemisión es gratis en SplitCam?", "Sí — la multiemisión está integrada y es "
             "gratis, sin coste por destino ni marca de agua."),
            ("¿A cuántos sitios cam puedo emitir a la vez?", "A tantos como soporte tu ancho de "
             "banda de subida — cada destino consume su propio bitrate."),
            ("¿Usa un relé en la nube?", "No — SplitCam envía los streams peer-to-peer "
             "directamente desde tu PC al servidor de cada plataforma."),
            ("¿La multiemisión ralentiza mi PC?", "La codificación se hace una vez y se "
             "reutiliza; la codificación por hardware mantiene baja la carga de CPU."),
        ],
    },
]
