# -*- coding: utf-8 -*-
LOVENSE_METHODS_ES = {
    "heading": "Configura Lovense en SplitCam — 3 pasos",
    "lead": "Esto reproduce la propia configuración en tres pasos de Lovense. La "
            "<strong>Cam Extension</strong> lee las propinas de tu sitio de cam, "
            "<strong>Lovense Connect</strong> es el puente Bluetooth con tu juguete y el "
            "<strong>SplitCam Toolset</strong> coloca la superposición de Lovense dentro de "
            "SplitCam, que emite por RTMP. Todo es gratis; los botones de descarga se "
            "ajustan a tu sistema automáticamente.",
    "stage_word": "Paso",
    "get_label": "Descargar",
    "do_label": "Luego",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Lee las propinas de tu sitio de cam — se instala en Chrome o Edge.",
            "get": ["camext"],
            "steps": [
                "Descarga la Cam Extension y descomprímela.",
                "Abre <strong>chrome://extensions</strong> (o <strong>edge://extensions</strong>), "
                "activa el <strong>Developer mode</strong> arriba a la derecha, haz clic en "
                "<strong>Load unpacked</strong> y selecciona la carpeta <em>lovense_cam</em> descomprimida.",
                "Haz clic en el icono de Lovense en la barra de herramientas e inicia sesión con tu cuenta de Lovense.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "El puente que se comunica con tu juguete por Bluetooth.",
            "get": ["connect"],
            "steps": [
                "En un ordenador: instala Lovense Connect (se recomienda un adaptador Bluetooth USB de "
                "Lovense). En un móvil: consigue la app Lovense Connect en Google Play o en la App Store.",
                "Enciende tu juguete y vincúlalo en Connect hasta que aparezca como conectado. En la app del "
                "móvil, escanea el código QR que se muestra en tu ordenador para enlazarlos.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Muestra la superposición de Lovense en SplitCam y emite tu transmisión.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Instala SplitCam y luego instala el Lovense SplitCam Toolset — el plugin que añade "
                "la superposición de Lovense a SplitCam.",
                "En la Cam Extension, haz clic en <strong>+</strong> para añadir tu sitio de cam (Chaturbate, "
                "Stripchat, …) y configura tu menú de propinas; luego abre la pestaña <strong>Video Feedback</strong> "
                "y elige <strong>SplitCam</strong> de la lista (OBS / SplitCam / Streamster).",
                "En SplitCam, añade la fuente <strong>Lovense</strong> que registró el Toolset — la "
                "superposición de menú de propinas / estado del juguete aparece en tu escena. Mantenla por encima de tus otras capas.",
                "Añade tu cámara, pega la clave RTMP de tu sitio de cam en los <strong>Stream "
                "Settings</strong> de SplitCam y haz clic en <strong>Go Live</strong> — la superposición y el juguete reaccionan a las propinas.",
            ],
        },
    ],
}
