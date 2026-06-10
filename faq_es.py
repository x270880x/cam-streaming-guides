# -*- coding: utf-8 -*-
# Plantillas de FAQ adicionales que se añaden a cada guía de plataforma.
# Cubren consultas informativas de alto volumen (ingresos / seguridad / registro / móvil)
# que no aparecen en el bloque de 4 FAQ específicas de cada plataforma en platforms_<lang>.py.
#
# Formato: las entradas de "common" se aplican a todas las plataformas; "stream" o "vcam"
# se elige según el METHOD de la plataforma. {name} se sustituye por el nombre de la plataforma.

FAQ_EXTRA_ES = {
    "common": [
        (
            "¿Cuánto pueden ganar las modelos en {name}?",
            "Los ingresos en {name} dependen del tamaño de la audiencia, las horas emitidas y las "
            "propinas. Las difusoras activas suelen llevarse entre $200 y $3,000 al mes; las mejores "
            "superan los $10,000. Tu porcentaje de ingresos sigue la estructura de comisiones de "
            "{name}: revisa el contrato de modelo antes de salir en directo."
        ),
        (
            "¿Es {name} segura para las difusoras?",
            "{name} exige verificación de edad y de identidad antes de pagar, lo que protege a las "
            "modelos del fraude. Usa un nombre artístico, no compartas nunca datos personales en "
            "cámara, activa el bloqueo geográfico para ocultar tu emisión en tu región y trata cada "
            "petición del espectador como una transacción. Los overlays y el fondo con IA de "
            "SplitCam también te permiten ocultar o reemplazar tu entorno real."
        ),
        (
            "¿Qué documentos necesito para hacerme modelo en {name}?",
            "{name} suele pedir un documento oficial con foto (pasaporte, carné de conducir o DNI), "
            "una selfi sosteniendo el documento y un formulario fiscal/de pagos (W-9 para EE. UU., "
            "W-8BEN para no residentes en EE. UU.). La aprobación suele tardar de 24 a 72 horas; "
            "una vez aprobada, puedes emitir el mismo día."
        ),
        (
            "¿Puedo emitir en {name} desde el móvil?",
            "{name} normalmente ofrece una app móvil para difusoras o un panel móvil web, pero la "
            "experiencia es limitada: sin overlays, sin segunda cámara y sin fondo con IA. Para una "
            "calidad de producción completa, emite desde un ordenador con SplitCam y usa el móvil "
            "como segunda cámara (SplitCam admite entrada de cámara IP desde móviles)."
        ),
    ],
    "stream": (
        "¿{name} es compatible con OBS o un codificador externo?",
        "Sí: {name} proporciona una URL de servidor RTMP y una clave de emisión en el panel de "
        "difusora. Pégalas en <strong>Configuración de emisión → RTMP personalizado</strong> de "
        "SplitCam, ajusta 1920×1080 a 30 fps con un bitrate de 4,000–5,000 Kbps y pulsa "
        "<strong>Salir en directo</strong>. La ruta RTMP personalizado te da toda la composición "
        "de escenas de SplitCam (multicámara, overlays, filtros)."
    ),
    "vcam": (
        "¿Puedo usar SplitCam como cámara virtual en {name}?",
        "Sí: el directo de {name} corre en el navegador, así que SplitCam se registra como una "
        "webcam llamada <strong>\"SplitCam Video Driver\"</strong>. Abre el panel de difusora de "
        "{name}, pulsa el selector de cámara del navegador y elige SplitCam. Tu escena compuesta "
        "(overlays, segunda cámara, filtros, fondo con IA) llega a los espectadores como una única "
        "señal de webcam."
    ),
}
