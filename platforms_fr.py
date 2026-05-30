# -*- coding: utf-8 -*-
"""French content for cam-streaming-guides. One dict per platform, written natively
for French-speaking audiences (France, Belgium, Switzerland, Québec)."""

_T_ETH = ("Connexion filaire", "L'Ethernet est plus fiable que le Wi-Fi pour un long live — "
          "une trame perdue, c'est un tip perdu. Tire un câble jusqu'au PC de stream.")
_T_TEST = ("Test privé d'abord", "Fais une courte diffusion de test pour vérifier caméra, son, "
           "cadrage et overlays avant d'ouvrir la salle au public.")

PLATFORMS_FR = [
    {
        "slug": "chaturbate", "name": "Chaturbate",
        "title": "Streamer sur Chaturbate avec SplitCam — Token & RTMP",
        "desc": "Diffuser sur Chaturbate avec SplitCam gratuit — token de diffusion, RTMP, scènes multi-caméras et overlays. Sans filigrane, sans inscription.",
        "kw": "streamer sur chaturbate, chaturbate broadcast token, chaturbate rtmp obs, chaturbate encodeur externe, chaturbate live",
        "h1html": 'Comment streamer sur <span class="accent">Chaturbate</span> avec SplitCam',
        "h1short": "Streamer sur Chaturbate",
        "card": "Configuration par token via encodeur externe pour Chaturbate.",
        "intro": "Chaturbate est l'une des plus grandes plateformes cam, bâtie sur une économie de tokens. Son broadcaster intégré au navigateur n'est qu'une caméra plate — passer par l'<strong style='color:var(--text)'>encodeur externe</strong> avec <strong style='color:var(--text)'>SplitCam</strong> gratuit ouvre les scènes multi-caméras, les overlays et les filtres sur ce même stream basé sur token.",
        "quick": "Diffuser sur Chaturbate avec SplitCam : installer SplitCam, composer la scène, sur Chaturbate ouvrir <em>Broadcast Yourself → My Broadcast</em>, copier le token de diffusion, le coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Copier le token de diffusion Chaturbate.</li><li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Sur Chaturbate, cliquez sur <strong>Broadcast Yourself</strong> pour ouvrir la page <strong>My Broadcast</strong>, puis sur <strong>View RTMP/OBS broadcast information and stream key</strong>. La clé apparaît comme votre <strong>token de diffusion</strong> — copiez-la. Elle fonctionne comme un mot de passe ; ne la publiez jamais.",
        "tips": [
            ("Le token est la clé", "Chaturbate utilise votre token de diffusion à la place d'une clé de stream générique. Traitez-le comme un mot de passe, réinitialisez s'il fuit."),
            ("Beaucoup de marge", "L'ingest RTMP de Chaturbate accepte jusqu'à la 4K, 60 fps et un débit très élevé — la limite c'est votre upload, pas la plateforme. Intervalle de keyframe : 2 secondes."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Chaturbate autorise-t-il OBS / les encodeurs externes ?", "Oui — Chaturbate prend officiellement en charge les encodeurs externes et possède son propre article d'aide « How do I set up OBS? ». Activez-le via « Use External Encoder to Broadcast » dans les paramètres de diffusion."),
            ("Où se trouve ma clé de stream Chaturbate ?", "Broadcast Yourself → My Broadcast → View RTMP/OBS broadcast information and stream key. La clé est votre token de diffusion."),
            ("Quel débit pour Chaturbate ?", "3 500 à 6 000 Kbps en 1080p suffisent largement. Le plafond de Chaturbate est très élevé — la vraie limite est votre upload ; lancez d'abord le test de vitesse de SplitCam."),
            ("SplitCam est-il gratuit pour Chaturbate ?", "Oui — entièrement gratuit, sans filigrane et sans limite de temps : l'encodeur ne mange pas vos gains en tokens."),
        ],
    },
    {
        "slug": "cam4", "name": "CAM4",
        "title": "Streamer sur CAM4 avec SplitCam — External Encoder",
        "desc": "Diffuser sur CAM4 avec SplitCam gratuit — External Encoder, clé de stream, géo-blocage et overlays. Sans filigrane, guide gratuit.",
        "kw": "streamer sur cam4, cam4.com, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
        "h1html": 'Comment streamer sur <span class="accent">CAM4</span> avec SplitCam',
        "h1short": "Streamer sur CAM4",
        "card": "External Encoder pour CAM4, avec géo-contrôles.",
        "intro": "CAM4 est une plateforme cam-and-earn mondiale avec des géo-contrôles intégrés — vous pouvez masquer votre diffusion dans certains pays. Passer par <strong style='color:var(--text)'>SplitCam</strong> gratuit comme encodeur externe ajoute les changements de scène et les overlays que le broadcaster de base ne sait pas faire.",
        "quick": "Diffuser sur CAM4 avec SplitCam : installer SplitCam, composer la scène, sur CAM4 ouvrir <em>Broadcast &amp; Earn Money → Start Broadcast → External Encoder</em>, Get Stream Key, coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer la clé CAM4.</li><li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Sur CAM4, cliquez sur <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn Money</strong> → <strong>Start Broadcast</strong>, puis sur <strong>External Encoder</strong> en haut. Remplissez date de naissance, genre et pays, puis cliquez sur <strong>Get Stream Key</strong> et copiez-la. Un slider vert dans les Stream Settings de SplitCam confirme la connexion.",
        "tips": [
            ("Définissez vos géo-restrictions", "CAM4 vous laisse masquer la diffusion dans des pays et régions précis — réglez ça côté CAM4 avant le live si besoin."),
            ("Surveillez le slider vert", "Le setup CAM4 affiche un slider vert dans les Stream Settings de SplitCam dès que la clé est acceptée — rouge signifie : re-vérifier la clé."),
            ("Débit plus bas que la moyenne", "L'ingest CAM4 plafonne le débit vidéo autour de 3 000 Kbps — plus bas que la plupart des sites cam. Ne pousse pas au-delà."),
            _T_ETH,
        ],
        "faq": [
            ("CAM4 prend-il officiellement en charge OBS / les encodeurs externes ?", "Oui — CAM4 a un OBS Guide officiel sur son site de support et recommande l'option External Encoder pour la meilleure expérience. SplitCam utilise le même chemin RTMP."),
            ("Puis-je géo-bloquer ma diffusion CAM4 ?", "Oui — CAM4 a une géo-restriction intégrée pour masquer la diffusion dans certains pays. Le réglage se fait sur CAM4, pas dans SplitCam."),
            ("Où est la clé de stream CAM4 ?", "Broadcast → Broadcast & Earn Money → Start Broadcast → External Encoder → Get Stream Key."),
            ("Quel débit pour CAM4 ?", "Plus bas que la moyenne — l'ingest CAM4 plafonne autour de 3 000 Kbps à 30 fps avec un keyframe de 1 seconde. Le tableau officiel basé sur le test de vitesse recommande de ne pas dépasser ~3 000."),
        ],
    },
    {
        "slug": "bongacams", "name": "BongaCams",
        "title": "Streamer sur BongaCams avec SplitCam — External Encoder",
        "desc": "Diffuser sur BongaCams avec SplitCam gratuit — External Encoder, scènes multi-caméras, overlays et fond IA. Sans filigrane.",
        "kw": "bongacams, bongcams, streamer sur bongacams, bongacams external encoder, bongacams rtmp obs",
        "h1html": 'Comment streamer sur <span class="accent">BongaCams</span> avec SplitCam',
        "h1short": "Streamer sur BongaCams",
        "card": "Configuration External Encoder pour BongaCams.",
        "intro": "BongaCams est une plateforme cam mondiale. La diffusion par encodeur externe n'y est pas activée par défaut — une fois débloquée, <strong style='color:var(--text)'>SplitCam</strong> gratuit pilote le stream avec scènes multi-caméras, overlays et fond IA.",
        "quick": "Diffuser sur BongaCams avec SplitCam : installer SplitCam, composer la scène, sur BongaCams ouvrir <em>Options → Broadcast settings → Select Encoder → External Encoder</em>, copier l'URL et la clé, coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer l'URL et la clé BongaCams.</li><li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Sur BongaCams, ouvrez <strong>Options</strong> → <strong>Broadcast settings</strong> → <strong>Select Encoder</strong> → <strong>External Encoder</strong> et copiez l'URL serveur et la clé de stream. <strong>Si le bouton External Encoder est absent</strong>, contactez le support BongaCams et demandez l'activation de l'encodage externe sur votre compte.",
        "tips": [
            ("Pas de bouton External Encoder ? Support", "BongaCams gate l'encodage externe — si l'option manque dans Broadcast settings, c'est le support qui l'active."),
            ("Faites correspondre les résolutions", "BongaCams recommande que la résolution webcam et la résolution stream soient identiques — par exemple les deux en 1280×720."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Pourquoi le bouton External Encoder n'apparaît-il pas ?", "L'encodage externe n'est pas activé par défaut sur tous les comptes — contactez le support BongaCams pour l'activer, puis le bouton apparaît dans Broadcast settings."),
            ("Faut-il vérifier le compte BongaCams ?", "Oui — diffuser exige d'avoir 18+, une pièce d'identité officielle valide pour la vérification d'âge, et la validation du compte avant le live."),
            ("Quel débit pour BongaCams ?", "L'ingest RTMP plafonne le débit vidéo autour de 6 000 Kbps avec keyframe de 2 secondes — 3 500 à 6 000 en 1080p est le sweet spot ; testez votre upload."),
            ("SplitCam est-il gratuit pour BongaCams ?", "Oui — totalement gratuit, sans filigrane ni limite de temps, donc l'encodeur ne touche pas vos gains de tokens BongaCams."),
        ],
    },
    {
        "slug": "stripchat", "name": "Stripchat",
        "title": "Streamer sur Stripchat avec SplitCam — Setup Strip Cam",
        "desc": "Diffuser sur Stripchat — la plateforme strip cam — avec SplitCam gratuit. Logiciel externe, clé-token, scènes et overlays.",
        "kw": "strip cam, stripchat live stream, streamer sur stripchat, stripchat external software, stripchat stream key, stripchat rtmp obs",
        "h1html": 'Comment streamer sur <span class="accent">Stripchat</span> avec SplitCam',
        "h1short": "Streamer sur Stripchat",
        "card": "Setup logiciel externe pour les diffusions Stripchat.",
        "intro": "Stripchat est une grosse plateforme cam centrée sur l'interactivité. Son mode <em>external software</em> vous donne une clé basée sur token — branchez-la dans <strong style='color:var(--text)'>SplitCam</strong> gratuit pour diffuser avec scènes, overlays et filtres, au lieu d'une simple caméra plate.",
        "quick": "Diffuser sur Stripchat avec SplitCam : installer SplitCam, composer la scène, sur Stripchat choisir <em>Switch to external software</em>, copier la clé de stream, la coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer la clé Stripchat.</li><li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Sur Stripchat, choisissez <strong>Switch to external software</strong>, puis ouvrez <strong>Show external software settings for the stream</strong>. Copiez la clé de stream — Stripchat l'affiche comme un token. Gardez-la privée.",
        "tips": [
            ("Calez la résolution sur celle du site", "La FAQ de Stripchat prévient : la résolution dans votre logiciel doit correspondre exactement à celle réglée sur le site, sinon l'image pixelise. Réglez les deux à l'identique."),
            ("Le minimum 2 Mbps ne suffit pas", "Stripchat indique 2 Mbps d'upload comme minimum — et précise explicitement que ce n'est pas suffisant pour un stream OBS ni pour de la multidiffusion. Visez bien au-dessus."),
            ("La clé est un token", "La clé de stream Stripchat est un token — copiez-la exactement, ne la partagez jamais, réinitialisez-la si elle fuit."),
            _T_ETH,
        ],
        "faq": [
            ("Stripchat recommande-t-il OBS / un logiciel externe ?", "Oui — la FAQ officielle de Stripchat conseille les logiciels de diffusion externes comme OBS « pour obtenir une meilleure qualité vidéo et audio ». SplitCam fonctionne de la même manière."),
            ("Comment basculer Stripchat sur logiciel externe ?", "Dans le Broadcast Center, choisissez Switch to External Broadcast Software (OBS), puis ouvrez les paramètres du logiciel externe pour révéler la clé de stream (token)."),
            ("Quel débit pour Stripchat ?", "L'ingest RTMP accepte jusqu'à ~6 000 Kbps avec keyframe de 2 secondes. 3 500 à 6 000 en 1080p est idéal — mais il faut bien plus que le minimum 2 Mbps, surtout en streaming OBS."),
            ("SplitCam est-il gratuit pour Stripchat ?", "Oui — pas de frais de licence, ni filigrane, ni limite de temps : même les longs shows interactifs sur Stripchat ne coûtent rien côté encodeur."),
        ],
    },
    {
        "slug": "onlyfans", "name": "OnlyFans",
        "title": "Passer en live sur OnlyFans avec SplitCam — Autorisation ou clé",
        "desc": "Passer en live sur OnlyFans avec SplitCam gratuit — connexion par autorisation ou OBS Key, scènes multi-caméras, overlays. Sans filigrane.",
        "kw": "passer en live sur onlyfans, onlyfans live stream, onlyfans autorisation splitcam, onlyfans obs key, onlyfans logiciel streaming",
        "h1html": 'Comment passer en live sur <span class="accent">OnlyFans</span> avec SplitCam',
        "h1short": "Live sur OnlyFans",
        "card": "Autoriser une fois ou coller la clé — live sur OnlyFans.",
        "intro": "Le live OnlyFans s'adresse à vos abonnés. SplitCam se connecte de <strong style='color:var(--text)'>deux façons</strong> — connectez-vous une fois avec vos identifiants OnlyFans et SplitCam récupère et garde synchronisée la clé de stream automatiquement, ou collez l'OBS Key à la main. Dans les deux cas vous diffusez avec scènes multi-caméras, overlays et filtres.",
        "quick": "Live sur OnlyFans avec SplitCam : installer SplitCam, composer la scène, ouvrir Stream Settings &rarr; Add Channel &rarr; OnlyFans et choisir <em>Autorisation</em> — se connecter avec son compte OnlyFans, SplitCam récupère la clé automatiquement — puis Go Live. Avec le compte connecté, vous modifiez les paramètres de stream OnlyFans dans SplitCam, sans ouvrir le site OnlyFans.",
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. C'est l'encodeur qui envoie votre vidéo à OnlyFans."),
            ("Configurez votre caméra et votre scène",
             "Ouvrez SplitCam et ajoutez votre webcam. Composez la scène que verront les spectateurs — overlays, texte, une seconde caméra, filtres beauté ou fond IA, appliqués en direct."),
            ("Connexion — Méthode 1 : Autorisation (recommandée)",
             "Dans SplitCam, ouvrez <strong>Stream Settings</strong> &rarr; <strong>Add Channel</strong> &rarr; <strong>OnlyFans</strong> et choisissez <strong>Autorisation</strong>. Connectez-vous avec votre e-mail et mot de passe OnlyFans. SplitCam se connecte à votre compte, récupère la clé de stream automatiquement et la garde synchronisée — et vous permet de gérer les paramètres du live OnlyFans depuis SplitCam, en les modifiant pendant ou après la diffusion sans aller sur le site OnlyFans."),
            ("Connexion — Méthode 2 : Stream Key (manuelle)",
             "Vous préférez ne pas vous connecter ? Passez par la clé. Sur OnlyFans, allez dans <strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; section <strong>Other</strong> et copiez l'<strong>OBS Key</strong>. Dans SplitCam, Add Channel &rarr; OnlyFans, collez-la dans le champ clé. Cette clé est statique — pour changer les réglages ensuite, retournez sur le site OnlyFans."),
            ("Go Live",
             "Quelle que soit la méthode, appuyez sur <strong>Go Live</strong> dans SplitCam. Avec la Méthode 1 vous pouvez continuer à ajuster les paramètres OnlyFans depuis SplitCam à la volée ; avec la Méthode 2 la clé reste exactement comme vous l'avez réglée."),
        ],
        "tips": [
            ("Autorisation vs Stream Key", "Deux façons de se connecter : <strong>Autorisation</strong> (se connecter une fois, la clé est récupérée et synchronisée — le plus simple) ou <strong>Stream Key</strong> (copier l'OBS Key depuis OnlyFans → Profile → Settings → Other et la coller). L'autorisation évite le copier-coller manuel."),
            ("Modifier les paramètres sans quitter SplitCam", "Avec l'autorisation, le compte reste connecté : vous ajustez les paramètres du live OnlyFans depuis SplitCam pendant ou après le stream — sans détour par le site OnlyFans."),
            ("Restez modeste sur le débit", "L'ingest RTMP d'OnlyFans plafonne le débit vidéo autour de 2 500 Kbps — plus strict que la plupart des sites cam. Visez 720p–1080p à ~2 000–2 500."),
            _T_ETH,
        ],
        "faq": [
            ("Comment connecter OnlyFans à SplitCam ?", "Deux façons. <strong>Autorisation</strong> — Stream Settings → Add Channel → OnlyFans → se connecter avec son compte OnlyFans, et SplitCam récupère la clé automatiquement. Ou <strong>Stream Key</strong> — copier l'OBS Key depuis OnlyFans → Profile → Settings → Other et la coller."),
            ("Puis-je changer les paramètres du live OnlyFans sans ouvrir le site ?", "Oui — avec la méthode Autorisation, SplitCam reste connecté à votre compte OnlyFans, donc la clé et les réglages se synchronisent automatiquement. Vous pouvez les modifier dans SplitCam pendant ou après le stream, sans visiter onlyfans.com."),
            ("Quel débit pour OnlyFans ?", "Restez modeste — l'ingest RTMP d'OnlyFans plafonne le débit vidéo autour de 2 500 Kbps, bien plus strict que la plupart des plateformes cam. Visez 720p–1080p autour de 2 000–2 500 Kbps."),
            ("SplitCam est-il gratuit pour les lives OnlyFans ?", "Oui — gratuit, sans filigrane, sans limite de temps. Aucun coût côté encodeur."),
        ],
    },
    {
        "slug": "camplace", "name": "CamPlace",
        "title": "Streamer sur CamPlace avec SplitCam — Guide gratuit",
        "desc": "Diffuser sur CamPlace avec SplitCam gratuit — encodeur externe, clé RTMP, scènes et overlays. Guide pas à pas, sans filigrane.",
        "kw": "streamer sur camplace, camplace logiciel diffusion, camplace rtmp, camplace external encoder, camplace stream key",
        "h1html": 'Comment streamer sur <span class="accent">CamPlace</span> avec SplitCam',
        "h1short": "Streamer sur CamPlace",
        "card": "Setup encodeur externe pour les diffusions CamPlace.",
        "intro": "CamPlace est une plateforme cam-streaming. Elle ne publie pas d'article d'aide OBS, donc le <strong style='color:var(--text)'>guide vidéo ci-dessus</strong> sert de référence — <strong style='color:var(--text)'>SplitCam</strong> gratuit se branche via RTMP standard et apporte scènes, overlays et fond IA qu'une caméra de base ne peut pas faire.",
        "quick": "Diffuser sur CamPlace avec SplitCam : installer SplitCam, composer la scène, activer la diffusion externe/RTMP dans CamPlace, copier l'URL serveur et la clé, les coller dans SplitCam, Go Live. Suivez le guide vidéo ci-dessus pour le chemin actuel."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer la clé RTMP CamPlace.</li><li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à CamPlace et ouvrez vos paramètres de diffusion. Basculez sur l'option encodeur externe / RTMP / OBS pour révéler l'<strong>URL serveur</strong> et la <strong>clé de stream</strong>, et copiez les deux. CamPlace ne publie pas de documentation OBS officielle — le <strong>guide vidéo ci-dessus</strong> reste la marche à suivre la plus fiable pour l'interface actuelle.",
        "tips": [
            ("Pas de guide OBS officiel — la vidéo", "CamPlace n'a pas d'article d'aide public sur les encodeurs externes ; le guide vidéo ci-dessus est la référence pour le chemin actuel."),
            ("Le RTMP standard fonctionne", "Même sans doc, CamPlace accepte une URL serveur RTMP standard et une clé — SplitCam se branche comme une destination RTMP personnalisée classique."),
            ("Empilez vos overlays dans SplitCam", "Objectifs de tips, pseudo et réseaux sociaux comme couches de scène — la caméra de base CamPlace ne peut pas les ajouter."),
            _T_ETH,
        ],
        "faq": [
            ("CamPlace a-t-il un guide OBS officiel ?", "Aucun article d'aide public sur les encodeurs externes trouvé. CamPlace accepte une URL RTMP et une clé standard, donc SplitCam fonctionne — suivez le guide vidéo ci-dessus."),
            ("CamPlace prend-il en charge les encodeurs externes ?", "Oui — il accepte une clé RTMP standard, donc SplitCam se branche comme une destination RTMP personnalisée."),
            ("Quel débit pour CamPlace ?", "CamPlace ne publie pas de chiffre officiel — prenez 3 500 à 6 000 Kbps en 1080p comme plage sûre et laissez le test de vitesse SplitCam fixer votre vrai plafond."),
            ("SplitCam est-il gratuit pour CamPlace ?", "Oui — gratuit, sans filigrane et sans limite de temps. Comme CamPlace ne livre pas son propre encodeur, un outil RTMP gratuit suffit."),
        ],
    },
    {
        "slug": "camsoda", "name": "CamSoda",
        "title": "CamSoda live avec SplitCam — Setup gratuit",
        "desc": "CamSoda live avec SplitCam gratuit — Use OBS Broadcaster, serveurs régionaux, scènes et overlays. Sans filigrane, guide gratuit.",
        "kw": "camsoda live, streamer sur camsoda, camsoda obs broadcaster, camsoda rtmp obs, camsoda live broadcast",
        "h1html": 'Comment streamer sur <span class="accent">CamSoda</span> avec SplitCam',
        "h1short": "Streamer sur CamSoda",
        "card": "Setup via Use OBS Broadcaster pour CamSoda.",
        "intro": "CamSoda est une plateforme cam US connue pour ses formats de shows interactifs et originaux. Elle supporte officiellement la diffusion via OBS — il y a un bouton <strong style='color:var(--text)'>Use OBS Broadcaster</strong> sur la page Go Live et un guide OBS officiel dans le wiki CamSoda. <strong style='color:var(--text)'>SplitCam</strong> gratuit fonctionne pareillement.",
        "quick": "Diffuser sur CamSoda avec SplitCam : installer SplitCam, composer la scène, cliquer sur Use OBS Broadcaster sur la page Go Live de CamSoda, copier l'URL serveur et la clé, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Cliquer sur Use OBS Broadcaster sur CamSoda.</li>"
                 "<li>Coller URL serveur + clé dans SplitCam.</li><li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Sur la page <strong>Go Live</strong> de CamSoda, cliquez sur <strong>Use OBS Broadcaster</strong>. CamSoda affiche l'URL serveur RTMP et la clé de stream — copiez les deux. Choisissez le serveur régional (Amérique du Nord, Europe, Asie, etc.) le plus proche de vous. Le wiki CamSoda contient un guide OBS complet si vous voulez le détail.",
        "tips": [
            ("Faites-vous vérifier pour les tips", "Sur CamSoda tout le monde peut diffuser, mais il faut compléter la procédure de vérification CamSoda avant de pouvoir recevoir des tips."),
            ("Choisissez le serveur régional le plus proche", "CamSoda propose des serveurs d'ingest régionaux — choisir le plus proche (NA / Europe / Asie / Amérique du Sud / Océanie) réduit la latence et les frames perdues."),
            ("Plafond à 1080p / 30 fps", "L'ingest CamSoda culmine vers 1080p, 30 fps et ~6 000 Kbps — inutile de monter plus haut."),
            _T_ETH,
        ],
        "faq": [
            ("CamSoda prend-il en charge OBS / les encodeurs externes ?", "Oui — officiellement. Il y a un bouton Use OBS Broadcaster sur la page Go Live et un guide OBS dans le wiki CamSoda, donc SplitCam fonctionne."),
            ("Faut-il se faire vérifier sur CamSoda ?", "Pour diffuser, non. Pour recevoir des tips, oui — CamSoda exige d'avoir complété sa procédure de vérification."),
            ("Quelle résolution CamSoda prend-il en charge ?", "Jusqu'à 1920×1080 à 30 fps, environ 6 000 Kbps maximum sur son ingest RTMP."),
            ("SplitCam est-il gratuit pour CamSoda ?", "Oui — gratuit, sans filigrane et sans limite de temps. Il fonctionne aux côtés du mode Use OBS Broadcaster gratuit de CamSoda, donc toute la chaîne ne coûte rien."),
        ],
    },
    {
        "slug": "streamate", "name": "Streamate",
        "title": "Streamer sur Streamate avec SplitCam — Canal intégré",
        "desc": "Diffuser sur Streamate avec SplitCam gratuit — canal intégré, clé SM Connect, scènes et overlays. Sans filigrane, setup rapide.",
        "kw": "streamate, streamate sm connect, streamer sur streamate, streamate logiciel diffusion, streamate rtmp",
        "h1html": 'Comment streamer sur <span class="accent">Streamate</span> avec SplitCam',
        "h1short": "Streamer sur Streamate",
        "card": "Streamate est un canal intégré dans SplitCam — setup rapide.",
        "intro": "Streamate est une plateforme cam établie — et c'est l'une des destinations <strong style='color:var(--text)'>préconfigurées dans SplitCam</strong>, dans la liste des canaux ; le setup est donc plus rapide qu'une entrée RTMP manuelle : on sélectionne Streamate, on colle la clé, terminé.",
        "quick": "Diffuser sur Streamate avec SplitCam : installer SplitCam, composer la scène, sur Streamate utiliser <em>SM Connect → Start Show</em> pour récupérer la clé, puis dans SplitCam ouvrir <em>Stream Settings → Add Channel → Streamate</em> et la coller."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer la clé Streamate via SM Connect.</li>"
                 "<li>Add Channel → Streamate dans SplitCam.</li><li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Sur Streamate, ouvrez <strong>SM Connect</strong>, acceptez les conditions, cliquez sur <strong>Start Show</strong> à gauche et fermez la fenêtre qui s'ouvre — puis copiez votre clé de streaming. Dans SplitCam, ouvrez <strong>Stream Settings</strong> → <strong>Add Channel</strong>, choisissez <strong>Streamate</strong> dans la liste et collez la clé. Un slider vert confirme la connexion.",
        "tips": [
            ("Streamate est un canal intégré", "Pas besoin d'une URL RTMP manuelle — SplitCam a Streamate dans sa liste Add Channel ; sélectionnez-le et collez la clé, c'est tout."),
            ("Fermez la pop-up SM Connect", "Après Start Show, Streamate ouvre une fenêtre — fermez-la, elle ne servait qu'à révéler la clé."),
            ("Verrouillez la résolution à 1080p", "Le champ Video Resolution de SM Connect peut sauter à 1440, qui n'est en réalité pas diffusé et fait silencieusement baisser votre qualité — réglez 1080p à la main. Un débit qui descend sur une image fixe est normal : le flux Streamate est adaptatif."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Streamate est-il intégré à SplitCam ?", "Oui — Streamate apparaît dans la liste Add Channel de SplitCam, vous le sélectionnez au lieu de saisir une URL RTMP à la main."),
            ("Où trouver la clé de streaming Streamate ?", "SM Connect → accepter les conditions → Start Show → fermer la pop-up → copier la clé."),
            ("Quel débit pour Streamate ?", "Streamate ne fixe pas de plafond strict — 3 500 à 6 000 Kbps en 1080p fonctionne bien. Le flux est adaptatif, donc un débit plus bas sur une image fixe est normal, pas un bug."),
            ("SplitCam est-il gratuit pour Streamate ?", "Oui — gratuit, sans filigrane ni limite de temps ; et comme Streamate est un canal intégré à SplitCam, pas de coût d'encodeur tiers non plus."),
        ],
    },
    {
        "slug": "streamray", "name": "StreamRay",
        "title": "Streamer sur StreamRay cam avec SplitCam — URL du chat",
        "desc": "Diffuser sur StreamRay cam avec SplitCam gratuit — URL postée dans le chat, mode OBS Broadcaster, scènes et overlays. Sans filigrane.",
        "kw": "streamray, streamray cam, streamer sur streamray, streamray obs broadcaster, streamray rtmp",
        "h1html": 'Comment streamer sur <span class="accent">StreamRay</span> avec SplitCam',
        "h1short": "Streamer sur StreamRay",
        "card": "Setup encodeur externe URL-from-chat pour StreamRay.",
        "intro": "StreamRay a un setup d'encodeur externe inhabituel — l'URL de stream vous est donnée dans la <strong style='color:var(--text)'>fenêtre de chat de la diffusion</strong> et il n'y a pas de clé de stream séparée. <strong style='color:var(--text)'>SplitCam</strong> gratuit gère sans souci ce workflow uniquement-URL.",
        "quick": "Diffuser sur StreamRay avec SplitCam : installer SplitCam, composer la scène, sur StreamRay activer l'OBS Broadcaster, copier l'URL de stream depuis la fenêtre de chat, la coller dans SplitCam (laisser le champ clé vide), Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Copier l'URL StreamRay depuis le chat.</li>"
                 "<li>Coller l'URL dans SplitCam.</li><li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Sur StreamRay, cliquez deux fois sur <strong>Broadcast Now</strong>, ouvrez le menu <strong>Other</strong>, choisissez <strong>OBS Broadcaster</strong> et <strong>Save and Close</strong>. StreamRay poste alors votre <strong>URL de stream dans la fenêtre de chat</strong> — copiez-la de là. Laissez le champ clé de SplitCam <strong>vide</strong> ; StreamRay s'authentifie par URL uniquement.",
        "tips": [
            ("L'URL est dans le chat", "StreamRay n'affiche pas l'URL de stream dans une boîte de paramètres — elle est postée dans votre fenêtre de chat de diffusion. Copiez-la de là."),
            ("Laissez la clé vide", "StreamRay n'utilise pas de clé séparée — seulement l'URL. Ne remplissez pas le champ clé dans SplitCam."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Où est l'URL de stream StreamRay ?", "Après activation de l'OBS Broadcaster, StreamRay poste l'URL dans la fenêtre de chat — copiez-la depuis le chat."),
            ("Pourquoi pas de clé StreamRay ?", "StreamRay s'authentifie par URL uniquement — laissez le champ clé de SplitCam vide."),
            ("Quel débit pour StreamRay ?", "StreamRay n'indique pas de plafond officiel — visez 3 500 à 6 000 Kbps en 1080p et lancez le test de vitesse SplitCam, puisque le mode URL-only ne donne aucun retour sur le débit."),
            ("SplitCam est-il gratuit pour StreamRay ?", "Oui — gratuit, sans filigrane et sans limite de temps, ce qui colle bien au flux URL-only de StreamRay où vous collez un seul lien et c'est parti."),
        ],
    },
    {
        "slug": "xlovecam", "name": "XLoveCam",
        "title": "Streamer sur XLoveCam avec SplitCam — Lien RTMP & clé",
        "desc": "Diffuser sur XLoveCam avec SplitCam gratuit — lien RTMP et clé, serveurs régionaux, scènes et overlays. Sans filigrane, guide gratuit.",
        "kw": "xlovecam, x love cam, streamer sur xlovecam, xlovecam rtmp link, xlovecam stream key",
        "h1html": 'Comment streamer sur <span class="accent">XLoveCam</span> avec SplitCam',
        "h1short": "Streamer sur XLoveCam",
        "card": "Setup lien RTMP + clé pour XLoveCam.",
        "intro": "XLoveCam est une plateforme cam européenne et multilingue. Ses paramètres de compte exposent à la fois un <strong style='color:var(--text)'>lien RTMP</strong> et une <strong style='color:var(--text)'>clé de stream</strong> — <strong style='color:var(--text)'>SplitCam</strong> gratuit prend les deux et diffuse avec scènes et overlays complets.",
        "quick": "Diffuser sur XLoveCam avec SplitCam : installer SplitCam, composer la scène, sur XLoveCam ouvrir <em>My Account → settings</em>, copier le lien RTMP et la clé de stream, coller les deux dans SplitCam, démarrer votre show."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Copier le lien RTMP + la clé XLoveCam.</li><li>Coller les deux dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Sur XLoveCam, ouvrez <strong>My Account</strong> → <strong>settings</strong>. Les paramètres contiennent à la fois un <strong>lien RTMP</strong> et une <strong>clé de stream</strong> — copiez les deux dans les champs URL serveur et clé de SplitCam, puis utilisez <strong>Start your show</strong> sur XLoveCam.",
        "tips": [
            ("Copiez le lien ET la clé", "XLoveCam donne un lien RTMP ET une clé de stream séparée — il vous faut les deux dans SplitCam, pas l'un sans l'autre."),
            ("Public multilingue", "XLoveCam est européen et multilingue — un overlay texte clair dans votre langue aide les spectateurs à vous trouver."),
            ("Choisissez le serveur le plus proche", "XLoveCam opère des serveurs RTMP régionaux — Europe, Amérique du Nord, Amérique du Sud et Asie. Choisir le plus proche réduit la latence et les frames perdues."),
            _T_ETH,
        ],
        "faq": [
            ("Où sont les infos RTMP XLoveCam ?", "My Account → settings — la page affiche à la fois le lien RTMP et la clé."),
            ("XLoveCam prend-il en charge les encodeurs externes ?", "Oui — il fournit un lien RTMP et une clé, donc SplitCam fonctionne comme encodeur."),
            ("Quel débit pour XLoveCam ?", "XLoveCam ne publie pas de limite fixe ; 3 500 à 6 000 Kbps en 1080p est idéal. Choisir le serveur régional le plus proche compte autant — ça réduit les frames perdues."),
            ("SplitCam est-il gratuit pour XLoveCam ?", "Oui — gratuit, sans filigrane et sans limite de temps. Atteindre le public européen multilingue de XLoveCam ne coûte rien côté logiciel."),
        ],
    },
    {
        "slug": "soulcams", "name": "SoulCams",
        "title": "Streamer sur SoulCams avec SplitCam — Paramètres OBS",
        "desc": "Diffuser sur SoulCams avec SplitCam gratuit — paramètres OBS, serveur RTMP et clé, scènes multi-caméras et overlays.",
        "kw": "soul cams, soulcams, streamer sur soulcams, soulcams obs, soulcams rtmp, soulcams broadcast",
        "h1html": 'Comment streamer sur <span class="accent">SoulCams</span> avec SplitCam',
        "h1short": "Streamer sur SoulCams",
        "card": "Setup paramètres OBS pour SoulCams.",
        "intro": "SoulCams est une plateforme cam dont les paramètres OBS affichent le <strong style='color:var(--text)'>serveur RTMP et la clé de stream ensemble</strong> dans une seule fenêtre. Mettez les deux dans <strong style='color:var(--text)'>SplitCam</strong> gratuit pour diffuser avec scènes multi-caméras et overlays.",
        "quick": "Diffuser sur SoulCams avec SplitCam : installer SplitCam, composer la scène, sur SoulCams cliquer sur Go Online → Settings → OBS, copier serveur et clé, coller les deux dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Ouvrir SoulCams Settings → OBS.</li><li>Coller serveur + clé dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Sur SoulCams, connectez-vous et cliquez sur <strong>Go Online</strong>, puis ouvrez <strong>Settings</strong> → <strong>OBS</strong>. La fenêtre OBS affiche le <strong>serveur RTMP</strong> et la <strong>clé de stream</strong> ensemble — copiez les deux dans SplitCam.",
        "tips": [
            ("Serveur et clé côte à côte", "SoulCams affiche serveur RTMP et clé dans la même fenêtre OBS — récupérez-les ensemble d'un coup."),
            ("Go Online d'abord", "Les paramètres OBS n'apparaissent qu'après avoir cliqué sur Go Online sur SoulCams — faites-le avant de chercher les détails d'encodeur."),
            ("Bloquez les régions non désirées", "SoulCams permet le blocage par pays côté modèle — choisissez quels pays ne peuvent pas voir votre diffusion avant de cliquer Go Online."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Où sont les paramètres OBS SoulCams ?", "Connectez-vous, cliquez sur Go Online, puis Settings → OBS — serveur RTMP et clé de stream sont affichés ensemble."),
            ("SoulCams prend-il en charge les encodeurs externes ?", "Oui — ses paramètres OBS fournissent serveur RTMP et clé, donc SplitCam fonctionne."),
            ("Quel débit pour SoulCams ?", "SoulCams ne donne pas de chiffre officiel — visez 3 500 à 6 000 Kbps en 1080p et testez votre upload d'abord, puisque la fenêtre OBS n'affiche aucune indication de débit."),
            ("SplitCam est-il gratuit pour SoulCams ?", "Oui — gratuit, sans filigrane ni limite de temps, donc un show complet sur SoulCams avec scènes multi-caméras et overlays ne coûte rien à encoder."),
        ],
    },
    {
        "slug": "imlive", "name": "ImLive",
        "title": "Streamer sur ImLive avec SplitCam — Caméra virtuelle",
        "desc": "Setup Im Live stream avec SplitCam gratuit — ImLive utilise la webcam directement (pas de RTMP), brancher SplitCam comme caméra virtuelle avec scènes.",
        "kw": "im live stream, imlive splitcam, streamer sur imlive, imlive caméra virtuelle, imlive webcam, im live cam",
        "h1html": 'Comment utiliser <span class="accent">ImLive</span> avec SplitCam',
        "h1short": "SplitCam sur ImLive",
        "card": "Setup caméra virtuelle pour ImLive — pas besoin de RTMP.",
        "intro": "ImLive utilise votre webcam directement dans le navigateur — il n'y a <strong style='color:var(--text)'>ni RTMP ni clé de stream</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuit se branche comme <strong style='color:var(--text)'>caméra virtuelle</strong> : composez la scène dans SplitCam, puis choisissez SplitCam comme caméra dans ImLive.",
        "quick": "Utiliser SplitCam sur ImLive : installer SplitCam, composer la scène avec des couches média, ouvrir ImLive et démarrer un chat vidéo, puis dans les paramètres ImLive sélectionner SplitCam comme webcam et micro."
                 "<ol><li>Installer SplitCam.</li><li>Composer la scène dans SplitCam.</li>"
                 "<li>Démarrer un chat vidéo sur ImLive.</li>"
                 "<li>Choisir SplitCam comme caméra ImLive.</li><li>Démarrer le chat.</li></ol>",
        "steps": [
            ("Installez SplitCam",
             "SplitCam est un logiciel gratuit pour Windows et macOS. Installez-le — pas de filigrane, pas d'inscription. Sur ImLive il fonctionne comme <strong>caméra virtuelle</strong>, pas comme encodeur RTMP."),
            ("Composez votre scène dans SplitCam",
             "Ouvrez SplitCam et utilisez <strong>Media Layers +</strong> pour ajouter votre webcam et tous les overlays, texte, filtres ou fond IA. Cette scène composée est ce qu'ImLive verra comme votre caméra."),
            ("Démarrez un chat vidéo sur ImLive",
             "Allez sur le site ImLive et cliquez sur <strong>Start Video Chat</strong>, puis ouvrez <strong>Go To Settings</strong> pour atteindre les options caméra et micro."),
            ("Choisissez SplitCam comme caméra",
             "Dans les paramètres ImLive, choisissez <strong>SplitCam</strong> comme webcam ET comme micro. ImLive affiche maintenant votre scène SplitCam complète au lieu d'une webcam plate."),
            ("Démarrez votre Free Live Chat",
             "Cliquez sur <strong>Free Live Chat</strong> sur ImLive pour passer en live. Pour changer votre look en cours de session, modifiez la scène dans SplitCam — ImLive se met à jour instantanément."),
        ],
        "tips": [
            ("Pas besoin de clé de stream", "ImLive n'a pas de RTMP — ne cherchez ni URL serveur ni clé. SplitCam est juste sélectionné comme périphérique caméra."),
            ("Mettez aussi SplitCam comme micro", "Choisissez SplitCam pour le micro en plus de la caméra, pour que votre mix audio et la réduction de bruit passent dans le live."),
            ("Composez la scène avant le live", "ImLive affiche ce que SplitCam sort — arrangez vos couches avant de démarrer le chat."),
            _T_TEST,
        ],
        "faq": [
            ("ImLive utilise-t-il RTMP ou une clé de stream ?", "Non — ImLive utilise votre webcam directement via le navigateur. SplitCam se branche comme caméra virtuelle, donc rien à copier."),
            ("Comment choisir SplitCam sur ImLive ?", "Start Video Chat → Go To Settings → choisir SplitCam comme webcam et micro."),
            ("Puis-je utiliser des overlays sur ImLive ?", "Oui — composez-les dans la scène SplitCam ; ImLive affiche le résultat composé."),
            ("SplitCam est-il gratuit pour ImLive ?", "Oui — gratuit, sans filigrane et sans limite de temps. Comme caméra virtuelle pour ImLive, il n'ajoute ni coût ni branding à votre chat vidéo."),
        ],
    },
    {
        "slug": "vxlive", "name": "VXLive",
        "title": "Streamer sur VXLive avec SplitCam — Support officiel",
        "desc": "Diffuser sur VXLive (VXModels / VISIT-X) avec SplitCam gratuit — preset VISIT-X officiel, serveur et clé, scènes. Sans filigrane.",
        "kw": "vxlive, visit-x, vxmodels splitcam, streamer sur vxlive, visit-x stream, vxlive rtmp",
        "h1html": 'Comment streamer sur <span class="accent">VXLive</span> avec SplitCam',
        "h1short": "Streamer sur VXLive",
        "card": "VXLive supporte SplitCam officiellement (preset VISIT-X).",
        "intro": "VXLive (VXModels / VISIT-X) est une plateforme cam du marché allemand — et l'une des rares à <strong style='color:var(--text)'>supporter officiellement SplitCam par son nom</strong>. VXModels a un article d'aide dédié pour brancher <strong style='color:var(--text)'>SplitCam</strong> à VXLive, et SplitCam livre VISIT-X comme preset de canal prêt à l'emploi.",
        "quick": "Diffuser sur VXLive avec SplitCam : installer SplitCam, composer la scène, sur VXLive choisir « Stream with third-party software », copier URL serveur et clé, dans SplitCam sélectionner le preset VISIT-X et coller, Go Live dans SplitCam, puis GO ONLINE dans VXLive."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL serveur + clé VXLive.</li>"
                 "<li>Choisir le preset VISIT-X dans SplitCam, coller.</li>"
                 "<li>Go Live, puis GO ONLINE dans VXLive.</li></ol>",
        "key_how": "Dans VXLive, choisissez <strong>Stream with third-party software</strong> et sélectionnez l'option pour <strong>OBS, SplitCam ou XSplit</strong>. VXLive fournit une <strong>URL serveur</strong> et une <strong>clé de stream</strong>. Dans SplitCam, choisissez <strong>VISIT-X</strong> comme plateforme de streaming, collez les deux, appuyez sur <strong>Go Live</strong> dans SplitCam, puis sur <strong>GO ONLINE</strong> dans VXLive.",
        "tips": [
            ("VISIT-X est un preset intégré", "Vous ne saisissez pas d'URL RTMP brute — SplitCam a VISIT-X dans sa liste de plateformes ; sélectionnez-le et collez simplement URL serveur et clé."),
            ("Go-live en deux temps", "Sur VXLive vous appuyez sur Go Live dans SplitCam d'abord, puis sur GO ONLINE dans VXLive — les deux, dans cet ordre."),
            ("Marché germanophone", "Le public VXLive est majoritairement germanophone — un overlay texte ou titre en allemand aide la connexion avec les spectateurs."),
            _T_ETH,
        ],
        "faq": [
            ("VXLive supporte-t-il SplitCam officiellement ?", "Oui — VXModels (VXLive) a un article d'aide officiel dédié à la configuration de SplitCam, et liste SplitCam aux côtés d'OBS et XSplit comme logiciel de diffusion supporté."),
            ("Comment brancher SplitCam à VXLive ?", "Dans VXLive, choisissez « Stream with third-party software », puis dans SplitCam sélectionnez le preset VISIT-X et collez l'URL serveur et la clé fournies par VXLive."),
            ("Je passe en live dans SplitCam ou VXLive ?", "Les deux — d'abord Go Live dans SplitCam, puis GO ONLINE dans VXLive."),
            ("Pourquoi VXModels recommande-t-il SplitCam ?", "L'article d'aide officiel VXModels recommande SplitCam spécifiquement pour éliminer les artefacts d'image et la pixelisation de la webcam et stabiliser la connexion — pas comme un simple encodeur générique."),
        ],
    },
    {
        "slug": "virtwish", "name": "VirtWish",
        "title": "Streamer sur VirtWish avec SplitCam — URL & clé de stream",
        "desc": "Diffuser sur VirtWish avec SplitCam gratuit — Profile → Start Broadcast section OBS, URL de stream et clé, scènes et overlays.",
        "kw": "virtwish, streamer sur virtwish, virtwish logiciel diffusion, virtwish rtmp, virtwish stream key, virtwish obs",
        "h1html": 'Comment streamer sur <span class="accent">VirtWish</span> avec SplitCam',
        "h1short": "Streamer sur VirtWish",
        "card": "Setup URL de stream + clé pour VirtWish.",
        "intro": "VirtWish est une plateforme cam interactive. Ses paramètres de diffusion vous donnent une <strong style='color:var(--text)'>URL de stream et une clé de stream séparée</strong> dans une section OBS — <strong style='color:var(--text)'>SplitCam</strong> gratuit prend les deux et fait tourner le show avec scènes et overlays.",
        "quick": "Diffuser sur VirtWish avec SplitCam : installer SplitCam, composer la scène, sur VirtWish ouvrir <em>Profile → Start Broadcast</em> pour atteindre la section OBS, copier le lien et la clé, coller les deux dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL + clé VirtWish.</li><li>Coller les deux dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Sur VirtWish, cliquez sur l'icône en haut à droite → <strong>Profile</strong> → <strong>Start Broadcast</strong>, puis à nouveau <strong>Start Broadcast</strong> pour atteindre la section OBS. <strong>Copiez le lien de la première ligne</strong> dans le champ Stream URL de SplitCam, et la <strong>Stream Key</strong> séparément dans le champ clé.",
        "tips": [
            ("Le lien est sur la première ligne", "La section OBS de VirtWish place l'URL de stream sur la première ligne — copiez-la dans Stream URL de SplitCam, puis la clé séparément."),
            ("Deux clics sur Start Broadcast", "Vous cliquez sur Start Broadcast deux fois sur VirtWish pour atteindre la section OBS — c'est normal, pas un bug."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Où sont les infos RTMP VirtWish ?", "Icône en haut à droite → Profile → Start Broadcast deux fois → la section OBS affiche le lien et la clé de stream."),
            ("VirtWish prend-il en charge les encodeurs externes ?", "Oui — sa section OBS fournit une URL de stream et une clé, donc SplitCam fonctionne."),
            ("Quel débit pour VirtWish ?", "VirtWish ne publie pas de plafond officiel ; 3 500 à 6 000 Kbps en 1080p est une plage sûre. Faites correspondre la résolution SplitCam à celle réglée sur VirtWish pour éviter le redimensionnement."),
            ("SplitCam est-il gratuit pour VirtWish ?", "Oui — gratuit, sans filigrane et sans limite de temps. Le setup URL-et-clé de VirtWish ne coûte que les quelques minutes nécessaires."),
        ],
    },
    {
        "slug": "xmodels", "name": "XModels",
        "title": "Streamer sur XModels avec SplitCam — Guide gratuit",
        "desc": "Diffuser sur XModels avec SplitCam gratuit — option encodeur externe dans les paramètres du compte modèle, clé RTMP, scènes et overlays.",
        "kw": "xmodels, streamer sur xmodels, xmodels logiciel diffusion, xmodels rtmp, xmodels external encoder",
        "h1html": 'Comment streamer sur <span class="accent">XModels</span> avec SplitCam',
        "h1short": "Streamer sur XModels",
        "card": "Setup encodeur externe pour les diffusions XModels.",
        "intro": "XModels est une plateforme cam-streaming avec une <strong style='color:var(--text)'>option encodeur externe</strong> intégrée aux paramètres du compte modèle. <strong style='color:var(--text)'>SplitCam</strong> gratuit y diffuse avec scènes multi-caméras, overlays et filtres au lieu d'une simple caméra plate.",
        "quick": "Diffuser sur XModels avec SplitCam : installer SplitCam, composer la scène, dans le compte modèle XModels activer l'option encodeur externe, copier l'URL serveur et la clé de stream, coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Activer l'encodeur externe dans les paramètres du compte XModels.</li>"
                 "<li>Coller URL serveur + clé dans SplitCam.</li><li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Dans les <strong>paramètres de votre compte modèle</strong> XModels, activez l'option <strong>diffusion depuis un encodeur externe</strong>. XModels fournit une <strong>clé de stream</strong> — copiez-la dans SplitCam. Si l'option n'est pas où vous l'attendez, le support XModels passe par le chat FAQ sur le site et <strong>info@xmodels.com</strong> ; le guide vidéo ci-dessus la montre aussi.",
        "tips": [
            ("Elle est dans les paramètres du compte", "XModels place l'option encodeur externe dans les paramètres du compte modèle, pas sur un écran de diffusion séparé."),
            ("Support : chat + email", "XModels n'a pas de grand centre d'aide public — son chat FAQ sur le site et info@xmodels.com sont les canaux de support officiels."),
            ("Empilez les overlays dans SplitCam", "Objectifs de tips, pseudo et réseaux sociaux comme couches de scène — la caméra de base XModels ne peut pas les ajouter."),
            _T_ETH,
        ],
        "faq": [
            ("XModels prend-il en charge les encodeurs externes ?", "Oui — les paramètres du compte modèle contiennent une option de diffusion par encodeur externe qui fournit une clé de stream, donc SplitCam fonctionne."),
            ("Où obtenir de l'aide sur XModels ?", "Le support XModels passe par son chat FAQ sur le site et l'email info@xmodels.com — il n'y a pas de grand centre d'aide public."),
            ("Quel débit pour XModels ?", "XModels ne documente pas de chiffre officiel — utilisez 3 500 à 6 000 Kbps en 1080p et lancez le test de vitesse SplitCam, puisque le support XModels est uniquement chat et email."),
            ("SplitCam est-il gratuit pour XModels ?", "Oui — gratuit, sans filigrane et sans limite de temps, donc diffuser sur le réseau européen XModels n'ajoute aucun coût logiciel."),
        ],
    },
    {
        "slug": "flirt4free", "name": "Flirt4Free",
        "title": "Streamer sur Flirt for Free cam avec SplitCam — Guide gratuit",
        "desc": "Diffuser sur Flirt for Free cam avec SplitCam gratuit — External Broadcast Form, RTMP URL et Stream Name, scènes et overlays.",
        "kw": "flirt for free cam, flirt 4 free cam, flirt4free, streamer sur flirt4free, flirt4free external broadcast, flirt4free rtmp",
        "h1html": 'Comment streamer sur <span class="accent">Flirt4Free</span> avec SplitCam',
        "h1short": "Streamer sur Flirt4Free",
        "card": "Setup External Broadcast Form pour Flirt4Free.",
        "intro": "Flirt4Free est l'une des plateformes cam les plus anciennes, en ligne depuis les années 1990. Elle supporte officiellement la diffusion externe via un <strong style='color:var(--text)'>External Broadcast Form</strong> — <strong style='color:var(--text)'>SplitCam</strong> gratuit envoie le stream pendant que le formulaire règle votre résolution et débit.",
        "quick": "Diffuser sur Flirt4Free avec SplitCam : installer SplitCam, composer la scène, ouvrir le External Broadcast Form de Flirt4Free, copier la RTMP URL et le Stream Name et régler résolution/débit, coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Ouvrir le External Broadcast Form de Flirt4Free.</li>"
                 "<li>Coller la RTMP URL + le Stream Name dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Dans l'espace modèle Flirt4Free, ouvrez le <strong>External Broadcast Form</strong>. Contrairement à la plupart des sites cam, Flirt4Free vous donne une <strong>RTMP URL</strong> et un <strong>Stream Name</strong> (pas une « clé »), plus des champs résolution et débit que vous remplissez dans le formulaire même. Copiez l'URL et le Stream Name dans les champs serveur et clé de SplitCam.",
        "tips": [
            ("C'est un Stream Name, pas une clé", "Flirt4Free appelle ces identifiants Stream Name. Collez-le dans le champ clé de stream de SplitCam — il joue le même rôle."),
            ("Réglez résolution/débit dans le formulaire", "Le External Broadcast Form de Flirt4Free a ses propres champs résolution et débit — alignez-les sur vos paramètres SplitCam pour que l'image ne soit pas redimensionnée."),
            ("Plateforme historique", "Flirt4Free tourne depuis les années 1990 — ses outils modèles sont matures et le External Broadcast Form en est une partie documentée."),
            _T_ETH,
        ],
        "faq": [
            ("Flirt4Free supporte-t-il les encodeurs externes ?", "Oui — officiellement, via son External Broadcast Form, qui fournit une RTMP URL et un Stream Name. SplitCam fonctionne comme encodeur."),
            ("Où récupérer les infos RTMP Flirt4Free ?", "Depuis le External Broadcast Form dans l'espace modèle — il affiche la RTMP URL, le Stream Name et les champs résolution/débit."),
            ("Quel débit pour Flirt4Free ?", "3 500 à 6 000 Kbps en 1080p — réglez la même valeur dans le External Broadcast Form et dans SplitCam."),
            ("SplitCam est-il gratuit pour Flirt4Free ?", "Oui — gratuit, sans filigrane et sans limite de temps, ce qui convient à une plateforme historique comme Flirt4Free où les shows peuvent durer longtemps."),
        ],
    },
    {
        "slug": "mfc-alerts", "name": "MFC Alerts",
        "title": "Ajouter MFC Alerts à votre stream avec SplitCam",
        "desc": "Afficher des alertes de tips animées sur votre stream MyFreeCams — URL mfcalerts.com en couche Browser dans SplitCam gratuit, au-dessus de la webcam.",
        "kw": "mfc alerts, myfreecams alerts, ajouter mfc alerts, mfcalerts splitcam, myfreecams tip alerts, myfreecams alerts overlay",
        "h1html": 'Comment ajouter <span class="accent">MFC Alerts</span> à votre stream',
        "h1short": "Ajouter MFC Alerts",
        "card": "Afficher des alertes de tips animées sur votre stream MyFreeCams.",
        "intro": "MFC Alerts affiche des effets animés sur votre stream MyFreeCams chaque fois qu'un spectateur envoie un tip. Ça tourne comme <strong style='color:var(--text)'>couche Browser</strong> dans <strong style='color:var(--text)'>SplitCam</strong> gratuit — configurez une fois et les tips déclenchent des réactions à l'écran en direct.",
        "quick": "Ajouter MFC Alerts avec SplitCam : installer SplitCam, ajouter votre webcam, ouvrir l'onglet Browser et charger mfcalerts.com, copier votre URL d'alertes, l'ajouter comme couche Browser au-dessus de la webcam, puis tester avec un tip de test."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter votre webcam.</li>"
                 "<li>Récupérer votre URL sur mfcalerts.com.</li>"
                 "<li>Ajouter-la comme couche Browser au-dessus de la webcam.</li>"
                 "<li>Envoyer un tip de test.</li></ol>",
        "steps": [
            ("Installez SplitCam et ajoutez votre webcam",
             "Installez SplitCam gratuit pour Windows ou macOS, puis ajoutez votre <strong>webcam</strong> comme source. MFC Alerts viendra comme couche par-dessus cette caméra."),
            ("Ouvrez l'onglet Browser et allez sur mfcalerts.com",
             "Dans SplitCam, ouvrez l'onglet <strong>Browser</strong> et naviguez vers <strong>www.mfcalerts.com</strong>. Connectez-vous, ou inscrivez-vous si vous n'avez pas encore de compte mfcalerts.com."),
            ("Copiez votre URL d'alertes",
             "Sur mfcalerts.com, utilisez <strong>Copy to clipboard</strong> pour copier votre URL d'alertes personnelle — c'est la page qui rend les animations de tips."),
            ("Ajoutez l'URL comme couche Browser — au-dessus de la webcam",
             "Collez l'URL dans la fenêtre Browser de SplitCam et cliquez <strong>Add</strong>. Puis réorganisez la liste de sources pour que <strong>MFC Alerts soit au-dessus de votre webcam</strong> (menu 3 points → Move Up). En dessous de la webcam, les effets sont masqués."),
            ("Testez avec un tip de test",
             "Ouvrez <strong>Settings → Send test tip</strong> et vérifiez que l'effet d'alerte apparaît sur votre caméra. Puis diffusez sur MyFreeCams comme d'habitude — les tips réels déclenchent maintenant les animations."),
        ],
        "tips": [
            ("MFC Alerts doit être au-dessus de la webcam", "L'erreur la plus fréquente : si la couche MFC Alerts est sous la webcam dans la liste de sources, les effets sont cachés. Remontez-la."),
            ("Vous avez besoin d'un compte mfcalerts.com", "L'URL d'alertes est personnelle à votre compte — inscrivez-vous sur mfcalerts.com d'abord si vous n'en avez pas."),
            ("Envoyez un tip de test avant le live", "Utilisez Settings → Send test tip pour vérifier que l'overlay fonctionne — ne découvrez pas le problème en plein show."),
            _T_ETH,
        ],
        "faq": [
            ("Qu'est-ce que MFC Alerts ?", "Un système de notifications pour MyFreeCams qui affiche des effets vidéo sur votre stream quand les spectateurs envoient des tips — ajouté comme overlay Browser dans SplitCam."),
            ("Pourquoi mes MFC Alerts ne s'affichent-elles pas ?", "Presque toujours l'ordre des couches — la couche Browser MFC Alerts doit être au-dessus de la webcam dans la liste de sources SplitCam."),
            ("Faut-il un compte pour MFC Alerts ?", "Oui — inscrivez-vous sur mfcalerts.com pour obtenir votre URL d'alertes personnelle."),
            ("SplitCam est-il gratuit pour ça ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps, et l'overlay navigateur MFC Alerts tourne à l'intérieur sans coût additionnel."),
        ],
    },
    {
        "slug": "lovense", "name": "Lovense",
        "title": "Ajouter un toy Lovense à votre stream avec SplitCam",
        "desc": "Brancher un toy Lovense interactif sur votre stream cam avec SplitCam gratuit — Lovense SplitCam Toolset, alertes de tips à l'écran, réactions.",
        "kw": "ajouter lovense au stream, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense toy interactif streaming",
        "h1html": 'Comment ajouter un <span class="accent">toy Lovense</span> à votre stream',
        "h1short": "Ajouter un toy Lovense",
        "card": "Brancher un toy Lovense interactif à votre stream cam.",
        "intro": "Diffusez votre stream cam via <strong style='color:var(--text)'>SplitCam</strong> gratuit et appairez un toy <strong style='color:var(--text)'>Lovense</strong> qui réagit aux tokens. Lovense documente officiellement un <strong style='color:var(--text)'>Lovense SplitCam Toolset</strong>, et SplitCam livre un plugin Lovense officiel — l'intégration est supportée des deux côtés.",
        "quick": "Pour ajouter un toy Lovense à votre stream : installer SplitCam et le logiciel Lovense, appairer le toy, lier Lovense à votre plateforme cam, ajouter le statut Lovense comme couche Browser dans SplitCam, puis diffuser comme d'habitude."
                 "<ol><li>Installer SplitCam.</li><li>Installer &amp; appairer le logiciel Lovense.</li>"
                 "<li>Lier Lovense à votre site cam.</li>"
                 "<li>Ajouter l'overlay Lovense dans SplitCam.</li><li>Appuyer sur Go Live.</li></ol>",
        "steps": [
            ("Installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — l'encodeur qui envoie votre vidéo à votre plateforme cam. Installez-le ; pas de filigrane."),
            ("Installez et appairez le logiciel Lovense",
             "Installez Lovense Connect / Lovense Stream (l'app desktop officielle). Allumez votre toy et appairez-le en Bluetooth pour que l'app l'affiche comme connecté."),
            ("Liez Lovense à votre plateforme cam",
             "Dans l'app Lovense, connectez votre compte cam pour que le toy réagisse aux tokens / tips des spectateurs. La plupart des grandes plateformes cam sont prises en charge."),
            ("Ajoutez l'overlay Lovense dans SplitCam",
             "Lovense fournit une URL d'overlay / widget. Ajoutez-la comme couche <strong>Browser</strong> dans votre scène SplitCam pour que les spectateurs voient l'état du toy et les tips récents à l'écran."),
            ("Composez votre scène et Go Live",
             "Ajoutez votre caméra et les autres overlays, collez la clé RTMP de votre plateforme cam dans SplitCam et cliquez <strong>Go Live</strong>. Le toy réagit aux tips en temps réel."),
        ],
        "tips": [
            ("Utilisez le Lovense SplitCam Toolset officiel", "Lovense publie un toolset spécifique à SplitCam avec son propre guide d'installation — il ajoute l'overlay activité-toy et alertes-tips conçu pour SplitCam."),
            ("Mettez à jour la Lovense Cam Extension", "Le toolset requiert une Lovense Cam Extension récente (30.1.4 ou plus) — mettez-la à jour avant le live."),
            ("Gardez le toy chargé", "Une batterie qui meurt en plein show tue l'interactif — chargez à fond avant de passer en live."),
            ("Testez la réaction au token", "Envoyez un petit tip de test pour vérifier que le toy réagit avant l'ouverture publique de la salle."),
            ("Vérifiez les versions requises", "Le Lovense SplitCam Toolset demande SplitCam 10.4.5 ou plus. La Lovense Cam Extension couvre officiellement Chaturbate, Stripchat, BongaCams, MyFreeCams et CamSoda — pour tout autre site, utilisez l'intégration Generic URL de Lovense."),
        ],
        "faq": [
            ("Lovense supporte-t-il SplitCam officiellement ?", "Oui — Lovense documente un « Lovense SplitCam Toolset » officiel avec son propre guide d'installation, et SplitCam livre un plugin Lovense officiel. L'intégration est supportée des deux côtés."),
            ("Le toy se branche-t-il directement à SplitCam ?", "Non — le toy s'appaire avec l'app Lovense ; SplitCam affiche l'overlay Lovense et diffuse votre caméra."),
            ("Quels sites cam supportent Lovense ?", "La Cam Extension de Lovense supporte officiellement Chaturbate, Stripchat, BongaCams, MyFreeCams et CamSoda, avec un support variable pour les autres — consultez l'app Lovense pour la liste actuelle."),
            ("Puis-je afficher les tips récents à l'écran ?", "Oui — ajoutez l'URL du widget Lovense comme couche Browser dans SplitCam."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Plusieurs sites cam",
        "title": "Diffuser sur plusieurs sites cam à la fois avec SplitCam",
        "desc": "Streamer sur MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat et d'autres en même temps avec la multidiffusion SplitCam gratuite. Un clic, sans filigrane.",
        "kw": "diffuser sur plusieurs sites cam, multistream cam sites, streamer chaturbate et bongacams en même temps, logiciel multidiffusion cam",
        "h1html": 'Comment diffuser sur <span class="accent">plusieurs sites cam</span> à la fois',
        "h1short": "Multidiffusion cam",
        "card": "Diffuser sur plusieurs sites cam simultanément.",
        "intro": "<strong style='color:var(--text)'>SplitCam</strong> gratuit peut diffuser un seul encodage sur <strong style='color:var(--text)'>plusieurs sites cam en même temps</strong> — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat et d'autres. Sans filigrane, en un clic.",
        "quick": "Pour diffuser sur plusieurs sites cam à la fois : installer SplitCam, composer la scène, récupérer l'URL serveur RTMP et la clé de stream de chaque site cam, toutes les ajouter dans les paramètres de multidiffusion de SplitCam, cliquer Go Live une fois."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer une clé RTMP par site cam.</li>"
                 "<li>Ajouter toutes les clés dans la multidiffusion SplitCam.</li>"
                 "<li>Appuyer sur Go Live une fois.</li></ol>",
        "steps": [
            ("Installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS avec multidiffusion intégrée. Installez-le — pas de filigrane, pas d'inscription."),
            ("Configurez votre caméra et votre scène",
             "Ouvrez SplitCam, ajoutez votre webcam et composez votre scène avec overlays et filtres. Une seule scène alimente chaque destination."),
            ("Récupérez une clé RTMP de chaque site cam",
             "Sur chaque plateforme cam, activez la diffusion externe / RTMP et copiez son <strong>URL serveur</strong> et sa <strong>clé de stream</strong>. Répétez pour chaque site visé — consultez les guides individuels par plateforme pour les chemins exacts."),
            ("Ajoutez chaque destination dans SplitCam",
             "Ouvrez <strong>Stream Settings</strong> et ajoutez chaque site cam comme destination RTMP personnalisée — collez son URL serveur et sa clé. Cochez tous ceux que vous voulez en direct."),
            ("Cliquez Go Live une fois",
             "Appuyez sur <strong>Go Live</strong>. SplitCam envoie votre stream simultanément à chaque site cam sélectionné, en peer-to-peer, depuis un seul encodage — sans frais supplémentaires."),
        ],
        "tips": [
            ("Surveillez votre upload", "La multidiffusion multiplie la charge d'upload. Chaque destination consomme son propre débit — assurez-vous que votre connexion supporte le total."),
            ("Vérifiez les règles de chaque plateforme", "Certains sites cam restreignent la diffusion simultanée ailleurs — confirmez avant de multidiffuser."),
            ("Câble — vous ne pouvez pas vous offrir une coupure ici", "La multidiffusion multiplie la charge d'upload, donc une seule chute de Wi-Fi peut bloquer toutes les destinations d'un coup. Le câble n'est pas optionnel ici."),
            ("Surveillez le moniteur de santé", "SplitCam affiche l'état par destination — coupez un site si votre upload ne suit pas."),
        ],
        "faq": [
            ("La multidiffusion est-elle gratuite dans SplitCam ?", "Oui — la multidiffusion est intégrée et gratuite, pas de frais par destination, pas de filigrane."),
            ("Sur combien de sites cam puis-je diffuser à la fois ?", "Autant que votre bande passante d'upload supporte — chaque destination consomme son propre débit."),
            ("Est-ce que ça passe par un relais cloud ?", "Non — SplitCam envoie les streams en peer-to-peer directement depuis votre PC vers le serveur d'ingest de chaque plateforme."),
            ("La multidiffusion ralentit-elle mon PC ?", "L'encodage est fait une seule fois et réutilisé ; l'encodage matériel maintient la charge CPU basse. La bande passante d'upload est la vraie limite."),
        ],
    },
]
