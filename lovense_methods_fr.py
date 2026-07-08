# -*- coding: utf-8 -*-
LOVENSE_METHODS_FR = {
    "heading": "Configurer Lovense sur SplitCam — 3 étapes",
    "lead": "Cette méthode reprend la configuration en trois étapes de Lovense. La "
            "<strong>Cam Extension</strong> lit les pourboires de votre site cam, "
            "<strong>Lovense Connect</strong> fait le pont Bluetooth avec votre jouet, et le "
            "<strong>SplitCam Toolset</strong> intègre l'overlay Lovense dans SplitCam, qui "
            "diffuse en RTMP. Tout est gratuit ; les boutons de téléchargement s'adaptent "
            "automatiquement à votre système.",
    "stage_word": "Étape",
    "get_label": "Télécharger",
    "do_label": "Ensuite",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Lit les pourboires de votre site cam — s'installe dans Chrome ou Edge.",
            "get": ["camext"],
            "steps": [
                "Téléchargez la Cam Extension et décompressez-la.",
                "Ouvrez <strong>chrome://extensions</strong> (ou <strong>edge://extensions</strong>), "
                "activez le <strong>Developer mode</strong> en haut à droite, cliquez sur <strong>Load unpacked</strong> "
                "et sélectionnez le dossier <em>lovense_cam</em> décompressé.",
                "Cliquez sur l'icône Lovense dans la barre d'outils et connectez-vous avec votre compte Lovense.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Le pont qui communique avec votre jouet en Bluetooth.",
            "get": ["connect"],
            "steps": [
                "Sur ordinateur : installez Lovense Connect (un adaptateur Bluetooth USB Lovense est "
                "recommandé). Sur téléphone : récupérez l'application Lovense Connect sur Google Play ou l'App Store.",
                "Allumez votre jouet et appairez-le dans Connect jusqu'à ce qu'il apparaisse connecté. Sur "
                "l'application mobile, scannez le QR affiché sur votre ordinateur pour les relier.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Affiche l'overlay Lovense dans SplitCam et diffuse votre stream.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Installez SplitCam, puis installez le Lovense SplitCam Toolset — le plugin qui ajoute "
                "l'overlay Lovense à SplitCam.",
                "Dans la Cam Extension, cliquez sur <strong>+</strong> pour ajouter votre site cam (Chaturbate, "
                "Stripchat, …) et configurez votre menu de pourboires, puis ouvrez l'onglet <strong>Video Feedback</strong> "
                "et choisissez <strong>SplitCam</strong> dans la liste (OBS / SplitCam / Streamster).",
                "Dans SplitCam, ajoutez la source <strong>Lovense</strong> enregistrée par le Toolset — l'overlay "
                "menu de pourboires / statut du jouet apparaît sur votre scène. Gardez-le au-dessus de vos autres calques.",
                "Ajoutez votre caméra, collez la clé RTMP de votre site cam dans les <strong>Stream "
                "Settings</strong> de SplitCam, et cliquez sur <strong>Go Live</strong> — l'overlay et le jouet réagissent aux pourboires.",
            ],
        },
    ],
}
