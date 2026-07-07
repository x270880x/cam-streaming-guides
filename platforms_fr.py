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
        "title": "Diffuser sur Chaturbate avec SplitCam — token RTMP",
        "desc": "Diffuser sur Chaturbate avec SplitCam : encodeur externe et token RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur chaturbate, chaturbate, chaturbate broadcast, chaturbate obs, chaturbate external encoder, chaturbate rtmp, chaturbate stream key",
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
        "title": "Diffuser sur CAM4 avec SplitCam — encodeur externe",
        "desc": "Diffuser sur CAM4 avec SplitCam : encodeur externe, clé RTMP et géo-blocage, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur cam4, cam4, cam4 broadcast, cam4 obs, cam4 external encoder, cam4 rtmp, cam4 stream key",
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
        "title": "Diffuser sur BongaCams avec SplitCam — encodeur",
        "desc": "Diffuser sur BongaCams avec SplitCam : encodeur externe et clé RTMP, gratuit, sans filigrane, scènes multicaméras, overlays et fond IA.",
        "kw": "diffuser sur bongacams, bongacams, bongacams broadcast, bongacams obs, bongacams external encoder, bongacams rtmp, bongacams stream key",
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
        "title": "Diffuser sur Stripchat avec SplitCam — encodeur",
        "desc": "Diffuser sur Stripchat avec SplitCam : logiciel externe et clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur stripchat, stripchat, stripchat broadcast, stripchat obs, stripchat external encoder, stripchat rtmp, stripchat stream key",
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
        "title": "Passer en live sur OnlyFans avec SplitCam",
        "desc": "Passer en live sur OnlyFans avec SplitCam : autorisation ou clé OBS, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "passer en live sur onlyfans, onlyfans, onlyfans live, onlyfans broadcast, onlyfans obs, onlyfans stream key, onlyfans rtmp",
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
        "title": "Diffuser sur CamPlace avec SplitCam — encodeur",
        "desc": "Diffuser sur CamPlace avec SplitCam : encodeur externe et clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur camplace, camplace, camplace broadcast, camplace obs, camplace external encoder, camplace rtmp, camplace stream key",
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
        "title": "Diffuser sur CamSoda avec SplitCam — encodeur",
        "desc": "Diffuser sur CamSoda avec SplitCam : Use OBS Broadcaster et clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur camsoda, camsoda, camsoda broadcast, camsoda obs, camsoda external encoder, camsoda rtmp, camsoda stream key",
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
        "title": "Diffuser sur Streamate avec SplitCam — SM Connect",
        "desc": "Diffuser sur Streamate avec SplitCam : canal intégré et clé SM Connect, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur streamate, streamate, streamate broadcast, streamate obs, streamate sm connect, streamate rtmp, streamate stream key",
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
        "title": "Diffuser sur StreamRay avec SplitCam — encodeur",
        "desc": "Diffuser sur StreamRay avec SplitCam : OBS Broadcaster et URL RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur streamray, streamray, streamray broadcast, streamray obs, streamray external encoder, streamray rtmp, streamray stream key",
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
        "title": "Diffuser sur XLoveCam avec SplitCam — lien RTMP",
        "desc": "Diffuser sur XLoveCam avec SplitCam : lien RTMP et clé de stream, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur xlovecam, xlovecam, xlovecam broadcast, xlovecam obs, xlovecam external encoder, xlovecam rtmp, xlovecam stream key",
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
        "title": "Diffuser sur SoulCams avec SplitCam — encodeur",
        "desc": "Diffuser sur SoulCams avec SplitCam : paramètres OBS, serveur et clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur soulcams, soulcams, soulcams broadcast, soulcams obs, soulcams external encoder, soulcams rtmp, soulcams stream key",
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
        "title": "Diffuser sur ImLive avec SplitCam — caméra virtuelle",
        "desc": "Diffuser sur ImLive avec SplitCam : caméra virtuelle, sans RTMP, gratuit, sans filigrane, scènes multicaméras, overlays et filtres.",
        "kw": "diffuser sur imlive, imlive, imlive virtual camera, imlive caméra virtuelle, imlive broadcast, imlive webcam, imlive obs",
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
        "title": "Diffuser sur VXLive avec SplitCam — preset VISIT-X",
        "desc": "Diffuser sur VXLive (VISIT-X) avec SplitCam : preset officiel, serveur et clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur vxlive, vxlive, vxlive broadcast, vxlive obs, vxlive external encoder, vxlive rtmp, visit-x, vxmodels",
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
        "title": "Diffuser sur VirtWish avec SplitCam — encodeur",
        "desc": "Diffuser sur VirtWish avec SplitCam : section OBS, URL et clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur virtwish, virtwish, virtwish broadcast, virtwish obs, virtwish external encoder, virtwish rtmp, virtwish stream key",
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
        "title": "Diffuser sur XModels avec SplitCam — encodeur",
        "desc": "Diffuser sur XModels avec SplitCam : encodeur externe et clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur xmodels, xmodels, xmodels broadcast, xmodels obs, xmodels external encoder, xmodels rtmp, xmodels stream key",
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
        "title": "Diffuser sur Flirt4Free avec SplitCam — encodeur",
        "desc": "Diffuser sur Flirt4Free avec SplitCam : External Broadcast Form, URL et Stream Name RTMP, gratuit, sans filigrane, scènes et overlays.",
        "kw": "diffuser sur flirt4free, flirt4free, flirt4free broadcast, flirt4free obs, flirt4free external encoder, flirt4free rtmp, flirt4free stream key",
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
        "desc": "Ajouter MFC Alerts à votre stream MyFreeCams avec SplitCam : alertes de tips animées en couche Browser, gratuit, sans filigrane.",
        "kw": "ajouter mfc alerts, mfc alerts, myfreecams, myfreecams alerts, mfcalerts overlay, myfreecams tip alerts, mfc alerts splitcam",
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
        "desc": "Ajouter un toy Lovense à votre stream SplitCam : appli Lovense Connect, Cam Extension et Toolset officiel, avec alertes de tips à l'écran.",
        "kw": "ajouter lovense au stream, lovense, lovense cam stream, lovense splitcam toolset, lovense cam extension, lovense connect, alertes de tips lovense, toy interactif lovense, overlay toy lovense",
        "h1html": 'Comment ajouter un <span class="accent">toy Lovense</span> à votre stream',
        "h1short": "Ajouter un toy Lovense",
        "card": "Brancher un toy Lovense interactif à votre stream cam.",
        "intro": "Diffusez votre stream cam via <strong style='color:var(--text)'>SplitCam</strong> "
                 "gratuit et appairez un toy <strong style='color:var(--text)'>Lovense</strong> "
                 "interactif pour qu'il réagisse aux tips. Vous installez trois choses : "
                 "<strong>SplitCam</strong> (l'encodeur), l'appli <strong>Lovense Connect</strong> "
                 "(le pont Bluetooth vers le toy) et la <strong>Lovense Cam Extension</strong> pour "
                 "Chrome/Edge (elle lit les tips et alimente l'overlay à l'écran). Lovense publie "
                 "aussi un <strong style='color:var(--text)'>Lovense SplitCam Toolset</strong> "
                 "officiel sur la page plugins de SplitCam — l'intégration est supportée des deux côtés.",
        "quick": "Pour ajouter un toy Lovense à votre stream : installez SplitCam, l'appli Lovense "
                 "Connect et la Lovense Cam Extension, appairez le toy, liez l'extension à votre site "
                 "cam, ajoutez l'overlay Lovense comme couche Browser dans SplitCam, puis diffusez "
                 "comme d'habitude."
                 "<ol><li>Installez SplitCam.</li>"
                 "<li>Installez Lovense Connect &amp; appairez le toy.</li>"
                 "<li>Installez la Lovense Cam Extension (Chrome/Edge).</li>"
                 "<li>Liez l'extension à votre site cam + ajoutez l'overlay dans SplitCam.</li>"
                 "<li>Appuyez sur Go Live.</li></ol>",
        "key_how": "Le toy ne communique jamais directement avec SplitCam. La chaîne est la suivante : "
                   "un spectateur envoie un tip sur votre site cam &rarr; la <strong>Lovense Cam "
                   "Extension</strong> dans votre navigateur le détecte &rarr; elle envoie une commande "
                   "à l'appli <strong>Lovense Connect</strong> sur localhost &rarr; Connect fait vibrer "
                   "le toy en Bluetooth. Le seul rôle de SplitCam est d'afficher l'<strong>overlay "
                   "Lovense</strong> (état du toy + tips récents) comme couche Browser et de diffuser "
                   "votre caméra. Il n'existe pas d'appli « Lovense Browser » séparée — c'est une "
                   "<em>extension</em> de navigateur pour Chrome ou Edge.",
        "steps": [
            ("Installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — l'encodeur qui "
             "envoie votre vidéo à votre plateforme cam. Installez-le ; pas de filigrane, pas d'inscription."),
            ("Installez Lovense Connect et appairez votre toy",
             "Installez l'appli <strong>Lovense Connect</strong> (desktop, depuis lovense.com/connect) "
             "— ou utilisez <strong>Lovense Remote</strong> sur votre téléphone. C'est le pont qui "
             "parle au toy en Bluetooth. Allumez le toy et appairez-le jusqu'à ce que l'app l'affiche "
             "comme connecté."),
            ("Installez la Lovense Cam Extension",
             "Ajoutez la <strong>Lovense Cam Extension</strong> à Chrome ou Edge (version 30.1.4 ou "
             "plus récente) et connectez-vous avec votre compte Lovense. Il n'y a pas de « Lovense "
             "Browser » autonome — c'est cette extension qui lit les tips et alimente l'overlay. Pour "
             "les widgets spécifiques à SplitCam, récupérez aussi le <strong>Lovense SplitCam "
             "Toolset</strong> officiel sur la page plugins de SplitCam (splitcam.com/more-plugins)."),
            ("Liez l'extension à votre site cam et ajoutez l'overlay dans SplitCam",
             "Dans la Cam Extension, cliquez sur <strong>+</strong> pour ajouter votre site cam "
             "(Chaturbate, Stripchat, etc.), réglez vos niveaux de tips, puis ouvrez l'onglet "
             "<strong>Video Feedback</strong> et choisissez <strong>SplitCam</strong>. Copiez l'URL "
             "d'overlay fournie et ajoutez-la comme couche <strong>Browser</strong> dans votre scène "
             "SplitCam pour que les spectateurs voient l'état du toy et les tips récents."),
            ("Composez votre scène et Go Live",
             "Ajoutez votre caméra et les autres overlays, collez la clé RTMP de votre plateforme cam "
             "dans SplitCam et cliquez <strong>Go Live</strong>. Le toy réagit désormais aux tips en "
             "temps réel."),
        ],
        "tips": [
            ("Trois installations, dans l'ordre", "SplitCam (encodeur) + Lovense Connect (pont "
             "Bluetooth) + Lovense Cam Extension (lecteur de tips / overlay). Il en manque une et le "
             "toy ne réagit pas à l'écran."),
            ("Une extension, pas un navigateur", "Il n'y a pas de « Lovense Browser » séparé à "
             "télécharger — la Lovense Cam Extension s'installe dans Chrome ou Edge. Gardez-la à jour "
             "(30.1.4 ou plus) sinon l'overlay SplitCam risque de ne pas charger."),
            ("Gardez le toy chargé", "Une batterie qui meurt en plein show tue l'interactif — "
             "chargez à fond avant de passer en live."),
            ("Testez la réaction au tip", "Envoyez un petit tip de test pour vérifier que le toy "
             "réagit avant l'ouverture publique de la salle."),
            ("Vérifiez les versions requises", "Le Lovense SplitCam Toolset demande SplitCam 10.4.5 "
             "ou plus. La Lovense Cam Extension couvre officiellement Chaturbate, Stripchat, "
             "BongaCams, MyFreeCams et CamSoda — pour tout autre site, utilisez l'intégration "
             "Generic URL de Lovense."),
        ],
        "faq": [
            ("Que dois-je installer pour Lovense sur SplitCam ?", "Trois choses : <strong>SplitCam</strong> "
             "(l'encodeur), l'appli <strong>Lovense Connect</strong> (relie le toy en Bluetooth) et la "
             "<strong>Lovense Cam Extension</strong> pour Chrome/Edge (lit les tips et alimente "
             "l'overlay). En option, ajoutez le Lovense SplitCam Toolset officiel depuis splitcam.com/more-plugins."),
            ("Y a-t-il un « Lovense Browser » à télécharger ?", "Non. Il n'existe pas de navigateur "
             "Lovense autonome — c'est la <strong>Lovense Cam Extension</strong>, qui s'installe dans "
             "Chrome ou Edge. L'appairage du toy est géré par l'appli séparée Lovense Connect (desktop) "
             "ou Lovense Remote (mobile)."),
            ("Le toy se branche-t-il directement à SplitCam ?", "Non — le toy s'appaire avec l'appli "
             "Lovense Connect en Bluetooth ; la Cam Extension lit les tips et SplitCam se contente "
             "d'afficher l'overlay et de diffuser votre caméra."),
            ("Quels sites cam supportent Lovense ?", "La Cam Extension de Lovense supporte "
             "officiellement Chaturbate, Stripchat, BongaCams, MyFreeCams et CamSoda, avec un support "
             "variable pour les autres — consultez l'app Lovense pour la liste actuelle."),
            ("Puis-je afficher les tips récents à l'écran ?", "Oui — la Cam Extension vous donne une "
             "URL d'overlay ; ajoutez-la comme couche Browser dans SplitCam et les spectateurs voient "
             "l'état du toy et les tips récents."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Plusieurs sites cam",
        "title": "Diffuser sur plusieurs sites cam à la fois avec SplitCam",
        "desc": "Diffuser sur Chaturbate, BongaCams, CAM4, Stripchat et plus en même temps avec la multidiffusion SplitCam : un clic, gratuit, sans filigrane.",
        "kw": "diffuser sur plusieurs sites cam, multidiffusion cam, multistream cam, logiciel multidiffusion cam, diffuser chaturbate et bongacams, multistream rtmp",
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
    {
        "slug": "livejasmin", "name": "LiveJasmin",
        "title": "Diffuser sur LiveJasmin avec SplitCam — encodeur HD",
        "desc": "Diffuser sur LiveJasmin avec SplitCam : encodeur externe du Model Center, clé RTMP HD 1080p, gratuit, sans filigrane, scènes multicaméras.",
        "kw": "diffuser sur livejasmin, livejasmin, livejasmin broadcast, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key",
        "h1html": 'Comment diffuser sur <span class="accent">LiveJasmin</span> avec SplitCam',
        "h1short": "Diffuser sur LiveJasmin",
        "card": "Configuration de l'encodeur externe pour le Model Center HD-only de LiveJasmin.",
        "intro": "LiveJasmin est le navire amiral de Docler Holding — l'un des plus gros réseaux cam au monde, et une plateforme exclusivement HD. Son outil de diffusion préféré est le client propriétaire <strong>JasminCAM</strong>, mais le Model Center expose aussi une voie standard <strong>External Encoder</strong> à laquelle <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte — pour streamer avec scènes multicaméras, filtres beauté et overlays sur le même flux HD.",
        "quick": "Pour diffuser sur LiveJasmin avec SplitCam : installer SplitCam, composer la scène HD, dans le Model Center aller dans <em>Settings → Broadcast → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène HD.</li>"
                 "<li>Récupérer URL et stream key depuis le Model Center.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous sur <strong>modelcenter.livejasmin.com</strong>, ouvrez <strong>Settings → Broadcast → External Encoder</strong>. Le Model Center affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. <strong>Note :</strong> les nouveaux comptes doivent être validés (48–72 h) avant que l'option encodeur externe apparaisse, et la plateforme impose une sortie HD uniquement.",
        "tips": [
            ("HD ou vous êtes déclassée", "LiveJasmin c'est HD only — en dessous de 1280×720 vous risquez de n'apparaître que sur les listes à faible rémunération, en dessous de 1080p vous perdez l'éligibilité 'Premium'. Visez 1920×1080 à 30 fps, 4 000–6 000 Kbps."),
            ("JasminCAM vs encodeur externe", "Le client maison JasminCAM de Docler donne la conformité HD la plus propre, mais les encodeurs externes (OBS, SplitCam, vMix) sont officiellement supportés une fois le compte validé — ils débloquent les scènes multicaméras et les overlays que JasminCAM ne sait pas faire."),
            ("Free chat ≠ show privé", "Le Free chat est en preview — pas de nu. C'est en privé et en Gold show que la modèle gagne. Pensez votre scène pour qu'elle tienne la route habillée ET en mode show."),
            _T_ETH,
        ],
        "faq": [
            ("LiveJasmin supporte-t-il officiellement les encodeurs externes comme SplitCam ?", "Oui — le Model Center propose une option External Encoder dans Settings → Broadcast. JasminCAM est le client recommandé, mais OBS, SplitCam et les autres encodeurs RTMP sont explicitement listés comme supportés dès que votre compte modèle est validé."),
            ("Où je récupère ma stream key LiveJasmin ?", "Dans le Model Center : Settings → Broadcast → External Encoder. L'URL serveur et la stream key unique apparaissent là — copiez les deux dans les champs RTMP personnalisé de SplitCam. La clé est liée à votre compte ; traitez-la comme un mot de passe."),
            ("Quel bitrate utiliser pour LiveJasmin ?", "LiveJasmin est HD only — visez 1920×1080 à 30 fps, 4 000–6 000 Kbps avec un keyframe de 2 secondes. En dessous, vous perdez le label Premium et vous êtes déclassée."),
            ("SplitCam est-il gratuit avec LiveJasmin ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. Le seul 'coût', c'est de tenir les exigences HD de LiveJasmin, ce que SplitCam gère nativement avec sa composition de scène 1080p et ses filtres beauté."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. C'est l'encodeur qui envoie votre vidéo HD vers LiveJasmin."),
            ("Composez votre scène HD",
             "Ouvrez SplitCam et ajoutez votre webcam en mode 1080p. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — LiveJasmin exige une qualité HD et votre scène composée doit faire premium aussi bien en Free chat qu'en privé."),
            ("Récupérez votre URL et stream key LiveJasmin",
             "Connectez-vous sur <strong>modelcenter.livejasmin.com</strong> (votre compte doit d'abord être validé — typiquement 48–72 h après l'inscription). Ouvrez <strong>Settings → Broadcast → External Encoder</strong>. La page révèle une <strong>URL serveur</strong> et une <strong>stream key</strong> unique. Copiez les deux."),
            ("Connectez SplitCam à LiveJasmin",
             "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur LiveJasmin et la stream key dans les champs RTMP personnalisé. Réglez le bitrate à 4 000–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes. Lancez d'abord le speed test intégré — un flux HD est exigeant."),
            ("Cliquez Go Live",
             "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne dans le Model Center LiveJasmin. En ~10 secondes votre flux HD atteint le réseau LiveJasmin. Les diffusions suivantes se font en un clic — ouvrez SplitCam, Go Live, puis connectez-vous sur LiveJasmin."),
        ],
    },
    {
        "slug": "myfreecams", "name": "MyFreeCams",
        "title": "Diffuser sur MyFreeCams avec SplitCam — encodeur",
        "desc": "Diffuser sur MyFreeCams avec SplitCam : External Broadcaster du Model Admin, clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur myfreecams, myfreecams, myfreecams broadcast, myfreecams obs, myfreecams external encoder, mfc rtmp, mfc stream key",
        "h1html": 'Comment diffuser sur <span class="accent">MyFreeCams</span> avec SplitCam',
        "h1short": "Diffuser sur MyFreeCams",
        "card": "Configuration broadcaster externe pour le Model Admin à tokens de MFC.",
        "intro": "MyFreeCams (MFC) est l'une des plus anciennes plateformes cam — économie 100 % tokens, pas de parcours d'approbation modèle, et une base fidèle de membres Premium. Son <em>Model Web Broadcaster</em> par défaut est un outil navigateur mono-caméra, mais le Model Admin expose aussi une option <strong>External Broadcaster</strong> à laquelle <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte — débloquant scènes multicaméras, overlays et filtres sur le même flux monétisé en tokens.",
        "quick": "Pour diffuser sur MyFreeCams avec SplitCam : installer SplitCam, composer la scène, dans <em>Model Admin → Broadcaster</em> basculer du Web Broadcaster vers External Broadcaster, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL et stream key depuis Model Admin.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à MyFreeCams, ouvrez <strong>Model Admin → Broadcaster</strong> et basculez de <em>Web Broadcaster</em> vers <strong>External Broadcaster</strong>. La page affiche une <strong>URL serveur</strong> (rtmp://publish.myfreecams.com…) et une <strong>stream key</strong> liées à votre compte modèle — copiez les deux dans les champs RTMP personnalisé de SplitCam. La clé est liée au compte ; traitez-la comme un mot de passe et réinitialisez-la si elle fuit.",
        "tips": [
            ("Tokens MFC, pas d'abonnements", "MFC est en pure économie pourboires/tokens — les membres Premium peuvent passer en privé, mais le gros du revenu vient des pourboires en free chat. Pensez une scène qui rapporte habillée et en mode casual, pas seulement en show nu."),
            ("Web Broadcaster vs External — choisissez une fois", "Le Web Broadcaster par défaut est mono-caméra, source unique. External Broadcaster débloque multi-scène, overlays, filtres beauté via SplitCam/OBS. À basculer dans Model Admin → Broadcaster avant de passer en ligne."),
            ("Intégration MFC Alerts", "Les alertes animées de pourboires à l'écran viennent de mfcalerts.com — ajoutez l'URL d'alerte comme calque Browser dans SplitCam, au-dessus de la caméra. Voir notre guide MFC Alerts pour le montage overlay complet."),
            _T_ETH,
        ],
        "faq": [
            ("MyFreeCams supporte-t-il officiellement les broadcasters externes comme SplitCam ?", "Oui — Model Admin propose une option External Broadcaster qui expose une URL serveur RTMP standard et une stream key. OBS, SplitCam, vMix et les autres encodeurs RTMP fonctionnent ; MFC supporte explicitement cette option dans sa documentation modèle."),
            ("Où je récupère ma stream key MFC ?", "Model Admin → Broadcaster → basculer vers External Broadcaster. L'URL serveur (rtmp://publish.myfreecams.com…) et la stream key apparaissent là. Copiez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour MyFreeCams ?", "MFC accepte jusqu'à ~6 000 Kbps avec un keyframe de 2 secondes. Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps — c'est votre upload qui sera la vraie limite. Lancez d'abord le speed test SplitCam."),
            ("SplitCam est-il gratuit avec MyFreeCams ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option External Broadcaster elle-même est gratuite dans Model Admin. Coût broadcaster total : zéro."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. C'est l'encodeur qui envoie votre vidéo vers MyFreeCams."),
            ("Composez votre scène",
             "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — tout est appliqué en live avant que le flux ne quitte votre PC. Pensez à ajouter l'URL mfcalerts.com comme calque Browser pour les alertes animées de pourboires."),
            ("Basculez sur External Broadcaster dans Model Admin",
             "Connectez-vous à MyFreeCams. Ouvrez <strong>Model Admin → Broadcaster</strong>. Basculez de <em>Web Broadcaster</em> vers <strong>External Broadcaster</strong>. La page révèle une <strong>URL serveur</strong> et une <strong>stream key</strong> unique. Copiez les deux."),
            ("Connectez SplitCam à MyFreeCams",
             "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur MFC et la stream key dans les champs RTMP personnalisé. Réglez le bitrate à 3 500–6 000 Kbps en 1920×1080, 30 fps, avec un keyframe de 2 secondes. Lancez d'abord le speed test intégré."),
            ("Cliquez Go Live",
             "Appuyez sur <strong>Go Live</strong> dans SplitCam. En ~10 secondes votre flux atteint MyFreeCams. Les diffusions suivantes se font en un clic — ouvrez SplitCam, Go Live."),
        ],
    },
    {
        "slug": "cherry-tv", "name": "Cherry.tv",
        "title": "Diffuser sur Cherry.tv avec SplitCam — encodeur",
        "desc": "Diffuser sur Cherry.tv avec SplitCam : encodeur externe du Streamer Dashboard, clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur cherry.tv, cherry.tv, cherry.tv broadcast, cherry.tv obs, cherry.tv external encoder, cherry.tv rtmp, cherry.tv stream key",
        "h1html": 'Comment diffuser sur <span class="accent">Cherry.tv</span> avec SplitCam',
        "h1short": "Diffuser sur Cherry.tv",
        "card": "Configuration de l'encodeur externe pour le Streamer Dashboard de Cherry.tv.",
        "intro": "Cherry.tv est une plateforme cam plus récente, en forte croissance, avec une dimension Web3 — paiements crypto-friendly et barrières d'entrée plus basses que les réseaux historiques type LiveJasmin. Le broadcaster par défaut est basé navigateur, mais le <strong>Streamer Dashboard</strong> expose aussi une voie standard <strong>External Encoder</strong> à laquelle <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte — vous permettant de streamer avec scènes multicaméras, overlays et filtres.",
        "quick": "Pour diffuser sur Cherry.tv avec SplitCam : installer SplitCam, composer la scène, dans le Streamer Dashboard ouvrir <em>Broadcast Settings → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL et stream key depuis le Streamer Dashboard.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte streamer Cherry.tv, ouvrez le <strong>Streamer Dashboard</strong> et allez dans <strong>Broadcast Settings → External Encoder</strong>. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. Les nouveaux comptes streamer doivent passer une vérification basique (généralement rapide — Cherry.tv a un onboarding plus léger que les réseaux cam historiques) avant que l'option encodeur externe ne soit pleinement active.",
        "tips": [
            ("Entrée plus light, trafic en hausse", "L'onboarding Cherry.tv est plus rapide que celui des plateformes historiques (pas de revue Docler à 72 h). Combiné avec le trafic en croissance, c'est un bon spot early-mover pour construire une base de followers avant que la concurrence se resserre."),
            ("Paiements crypto disponibles", "Cherry.tv supporte le retrait en crypto en plus du fiat standard — utile si vous êtes dans une région où les paiements des réseaux cam classiques sont lents ou restreints."),
            ("Browser broadcaster vs externe", "Le broadcaster navigateur est pratique mais à source unique. SplitCam via External Encoder débloque scènes multicaméras, overlays, filtres beauté et fond IA que l'outil navigateur ne sait pas faire."),
            _T_ETH,
        ],
        "faq": [
            ("Cherry.tv supporte-t-il officiellement les encodeurs externes comme SplitCam ?", "Oui — le Streamer Dashboard inclut External Encoder dans Broadcast Settings. La plateforme fournit une URL serveur RTMP standard et une stream key ; OBS, SplitCam et les autres encodeurs RTMP s'y connectent sans problème."),
            ("Où je récupère ma stream key Cherry.tv ?", "Streamer Dashboard → Broadcast Settings → External Encoder. L'URL serveur et la stream key apparaissent là — copiez les deux dans les champs RTMP personnalisé de SplitCam. La clé est liée au compte ; traitez-la comme un mot de passe."),
            ("Quel bitrate utiliser pour Cherry.tv ?", "Cherry.tv accepte les réglages cam-quality standards — poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test intégré de SplitCam."),
            ("SplitCam est-il gratuit avec Cherry.tv ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de Cherry.tv est gratuite à activer. Coût broadcaster total : zéro."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. C'est l'encodeur qui envoie votre vidéo vers Cherry.tv."),
            ("Composez votre scène",
             "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — tout est appliqué en live. L'audience Cherry.tv est plus jeune et plus rodée aux plateformes, donc une scène soignée aide à sortir du lot."),
            ("Récupérez votre URL et stream key Cherry.tv",
             "Connectez-vous à votre compte streamer Cherry.tv, ouvrez le <strong>Streamer Dashboard</strong> et allez dans <strong>Broadcast Settings → External Encoder</strong>. La page révèle une <strong>URL serveur</strong> et une <strong>stream key</strong> unique. Copiez les deux."),
            ("Connectez SplitCam à Cherry.tv",
             "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur Cherry.tv et la stream key dans les champs RTMP personnalisé. Réglez le bitrate à 3 500–6 000 Kbps en 1920×1080, 30 fps, avec un keyframe de 2 secondes. Lancez d'abord le speed test intégré."),
            ("Cliquez Go Live",
             "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis le Streamer Dashboard sur Cherry.tv. En ~10 secondes votre flux atteint Cherry.tv. Les diffusions suivantes se font en un clic — ouvrez SplitCam, Go Live, puis passez en ligne sur Cherry.tv."),
        ],
    },
    {
        "slug": "amateurtv", "name": "AmateurTV",
        "title": "Diffuser sur AmateurTV avec SplitCam — encodeur",
        "desc": "Diffuser sur AmateurTV avec SplitCam : encodeur externe du Model Panel, clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur amateurtv, amateurtv, amateurtv broadcast, amateurtv obs, amateurtv external encoder, amateurtv rtmp, amateurtv stream key",
        "h1html": 'Comment diffuser sur <span class="accent">AmateurTV</span> avec SplitCam',
        "h1short": "Diffuser sur AmateurTV",
        "card": "Configuration de l'encodeur externe pour le réseau hispanophone d'AmateurTV.",
        "intro": "AmateurTV est LE réseau cam hispanophone — gros trafic en Espagne, au Mexique, en Argentine et dans toute la LatAm. Le broadcaster par défaut du Model Panel passe par navigateur, mais une voie standard <strong>External Encoder</strong> est aussi exposée, et <strong style='color:var(--text)'>SplitCam</strong> gratuit s'y connecte — pour diffuser avec scènes multicaméras, filtres beauté et overlays auprès d'un public hispanophone que les réseaux US-centric servent mal.",
        "quick": "Pour diffuser sur AmateurTV avec SplitCam : installer SplitCam, composer la scène, dans le Model Panel ouvrir <em>Broadcast Settings → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL et stream key depuis le Model Panel.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte modèle AmateurTV, ouvrez le <strong>Model Panel</strong> et allez dans <strong>Broadcast Settings → External Encoder</strong>. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. Les nouveaux comptes doivent passer une vérification d'identité avant de passer en ligne.",
        "tips": [
            ("Public hispanophone d'abord", "Le trafic AmateurTV est massivement hispanophone — l'Espagne en journée, la LatAm sur les heures de soirée US. Titres de salle, textes en surimpression et overlays en espagnol convertissent largement mieux que de l'anglais seul."),
            ("Le fuseau LatAm est votre prime time", "Le pic de trafic correspond au soir LatAm (UTC-3 à UTC-6). Si vous êtes souple, diffuser fin de soirée CET / matinée Asie touche Espagne et LatAm en même temps."),
            ("Payouts mid-tier solides", "Pas le RPM le plus élevé du secteur, mais AmateurTV paie régulièrement, et le créneau hispanophone est nettement moins saturé que les top réseaux US."),
            _T_ETH,
        ],
        "faq": [
            ("AmateurTV supporte-t-il officiellement les encodeurs externes comme SplitCam ?", "Oui — le Model Panel inclut une option External Encoder dans Broadcast Settings. AmateurTV fournit une URL serveur RTMP standard et une stream key ; OBS, SplitCam, vMix et les autres encodeurs RTMP s'y connectent."),
            ("Où je récupère ma stream key AmateurTV ?", "Model Panel → Broadcast Settings → External Encoder. L'URL serveur et la stream key apparaissent là. Copiez les deux dans les champs RTMP personnalisé de SplitCam. La clé est liée au compte."),
            ("Quel bitrate utiliser pour AmateurTV ?", "Réglages cam-quality standards — poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test intégré de SplitCam."),
            ("SplitCam est-il gratuit avec AmateurTV ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe d'AmateurTV est gratuite à activer."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. C'est l'encodeur qui envoie votre vidéo vers AmateurTV."),
            ("Composez votre scène",
             "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA. Mettez vos textes d'overlay en espagnol — le public hispanophone d'AmateurTV le remarque."),
            ("Récupérez votre URL et stream key AmateurTV",
             "Connectez-vous à votre compte modèle AmateurTV, ouvrez le <strong>Model Panel</strong> et allez dans <strong>Broadcast Settings → External Encoder</strong>. La page révèle une <strong>URL serveur</strong> et une <strong>stream key</strong> unique. Copiez les deux."),
            ("Connectez SplitCam à AmateurTV",
             "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur AmateurTV et la stream key dans les champs RTMP personnalisé. Réglez le bitrate à 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes. Lancez d'abord le speed test intégré."),
            ("Cliquez Go Live",
             "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis le Model Panel sur AmateurTV. En ~10 secondes votre flux atteint le réseau. Les diffusions suivantes se font en un clic — ouvrez SplitCam, Go Live."),
        ],
    },
    {
        "slug": "camster", "name": "Camster",
        "title": "Diffuser sur Camster avec SplitCam — encodeur",
        "desc": "Diffuser sur Camster avec SplitCam : encodeur externe du Model Hub, clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur camster, camster, camster broadcast, camster obs, camster external encoder, camster rtmp, camster stream key",
        "h1html": 'Comment diffuser sur <span class="accent">Camster</span> avec SplitCam',
        "h1short": "Diffuser sur Camster",
        "card": "Configuration de l'encodeur externe pour le Model Hub de Camster.",
        "intro": "Camster est une plateforme cam mid-tier établie — plus petite que Chaturbate ou LiveJasmin, mais avec une base d'utilisateurs fidèle et des payouts corrects. Le broadcaster par défaut du Model Hub passe par navigateur, mais une voie standard <strong>External Encoder</strong> est aussi exposée, et <strong style='color:var(--text)'>SplitCam</strong> gratuit s'y connecte — pour diffuser avec scènes multicaméras, overlays et filtres que le broadcaster natif ne sait pas faire.",
        "quick": "Pour diffuser sur Camster avec SplitCam : installer SplitCam, composer la scène, dans le Model Hub ouvrir <em>Broadcast Settings → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL et stream key depuis le Model Hub.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte modèle Camster, ouvrez le <strong>Model Hub</strong> et allez dans <strong>Broadcast Settings → External Encoder</strong>. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. La clé est liée au compte ; traitez-la comme un mot de passe.",
        "tips": [
            ("Mid-tier = moins de concurrence", "Camster a un trafic stable mais nettement moins de broadcasters que les réseaux du haut — plus facile de remonter en page d'accueil avec une scène soignée et un planning régulier."),
            ("Broadcaster navigateur vs externe", "Le broadcaster du navigateur est mono-source. SplitCam via External Encoder débloque scènes multicaméras, overlays, filtres beauté et fond IA."),
            ("Payouts stables, split correct", "Le split de Camster est correct pour du mid-tier — pas le plus élevé du marché, mais des paiements mensuels fiables et peu de plaintes côté retards de versement."),
            _T_ETH,
        ],
        "faq": [
            ("Camster supporte-t-il officiellement les encodeurs externes comme SplitCam ?", "Oui — le Model Hub propose une option External Encoder dans Broadcast Settings. URL serveur RTMP standard et stream key ; OBS, SplitCam et les autres encodeurs RTMP s'y connectent."),
            ("Où je récupère ma stream key Camster ?", "Model Hub → Broadcast Settings → External Encoder. L'URL serveur et la stream key apparaissent là. Copiez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour Camster ?", "Réglages cam-quality standards — poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test intégré de SplitCam."),
            ("SplitCam est-il gratuit avec Camster ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de Camster est gratuite."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène",
             "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — tout est appliqué en live."),
            ("Récupérez votre URL et stream key Camster",
             "Connectez-vous à votre compte modèle Camster, ouvrez le <strong>Model Hub</strong> et allez dans <strong>Broadcast Settings → External Encoder</strong>. La page révèle une <strong>URL serveur</strong> et une <strong>stream key</strong> unique. Copiez les deux."),
            ("Connectez SplitCam à Camster",
             "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur Camster et la stream key dans les champs RTMP personnalisé. Réglez le bitrate à 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes. Lancez d'abord le speed test intégré."),
            ("Cliquez Go Live",
             "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis le Model Hub. En ~10 secondes votre flux atteint Camster."),
        ],
    },
    {
        "slug": "camversity", "name": "Camversity",
        "title": "Diffuser sur Camversity avec SplitCam — encodeur",
        "desc": "Diffuser sur Camversity avec SplitCam : encodeur externe du Performer Dashboard, clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur camversity, camversity, camversity broadcast, camversity obs, camversity external encoder, camversity rtmp, camversity stream key",
        "h1html": 'Comment diffuser sur <span class="accent">Camversity</span> avec SplitCam',
        "h1short": "Diffuser sur Camversity",
        "card": "Configuration de l'encodeur externe pour le Performer Dashboard de Camversity.",
        "intro": "Camversity est une plateforme cam indépendante en croissance, focalisée sur des outils favorables au performer et des commissions plus basses que les réseaux historiques. Le broadcaster par défaut du Performer Dashboard passe par navigateur, mais une voie standard <strong>External Encoder</strong> est aussi exposée, et <strong style='color:var(--text)'>SplitCam</strong> gratuit s'y connecte — pour diffuser avec scènes multicaméras, overlays et filtres.",
        "quick": "Pour diffuser sur Camversity avec SplitCam : installer SplitCam, composer la scène, dans le Performer Dashboard ouvrir <em>Stream Settings → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL et stream key depuis le Performer Dashboard.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte performer Camversity, ouvrez le <strong>Performer Dashboard</strong> et allez dans <strong>Stream Settings → External Encoder</strong>. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. Les nouveaux comptes passent une vérification d'identité standard avant de passer en ligne.",
        "tips": [
            ("Split favorable au performer", "Le split de Camversity est plus favorable au performer que celui des réseaux historiques — utile à comparer à votre plateforme principale si vous débutez en cam."),
            ("Onboarding plus léger que Docler", "La vérification Camversity est plus rapide que les 48–72 h de LiveJasmin, tout en restant sérieuse (pas de modèles non vérifiés). Bon entre-deux."),
            ("Composez une scène, pas juste une webcam", "Le broadcaster par défaut du Performer Dashboard est mono-source. SplitCam via External Encoder débloque multicaméras, overlays, filtres beauté."),
            _T_ETH,
        ],
        "faq": [
            ("Camversity supporte-t-il officiellement les encodeurs externes comme SplitCam ?", "Oui — le Performer Dashboard propose une option External Encoder dans Stream Settings. URL serveur RTMP standard et stream key ; OBS, SplitCam, vMix s'y connectent."),
            ("Où je récupère ma stream key Camversity ?", "Performer Dashboard → Stream Settings → External Encoder. L'URL serveur et la stream key apparaissent là."),
            ("Quel bitrate utiliser pour Camversity ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test intégré de SplitCam."),
            ("SplitCam est-il gratuit avec Camversity ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de Camversity est gratuite."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène",
             "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Récupérez votre URL et stream key Camversity",
             "Connectez-vous à votre compte performer Camversity, ouvrez le <strong>Performer Dashboard</strong> et allez dans <strong>Stream Settings → External Encoder</strong>. La page révèle une <strong>URL serveur</strong> et une <strong>stream key</strong> unique. Copiez les deux."),
            ("Connectez SplitCam à Camversity",
             "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur Camversity et la stream key dans les champs RTMP personnalisé. Réglez le bitrate à 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live",
             "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis le Performer Dashboard. En ~10 secondes votre flux atteint Camversity."),
        ],
    },
    {
        "slug": "skyprivate", "name": "SkyPrivate",
        "title": "Diffuser sur SkyPrivate avec SplitCam — caméra virtuelle",
        "desc": "Diffuser sur SkyPrivate avec SplitCam : caméra virtuelle pour les appels Skype pay-per-minute, gratuit, sans filigrane, scènes multicaméras.",
        "kw": "diffuser sur skyprivate, skyprivate, skyprivate virtual camera, skyprivate caméra virtuelle, skyprivate splitcam, skype cam privé, skyprivate broadcast",
        "h1html": 'Comment utiliser <span class="accent">SkyPrivate</span> avec SplitCam',
        "h1short": "SplitCam sur SkyPrivate",
        "card": "Configuration caméra virtuelle pour les appels cam SkyPrivate basés sur Skype.",
        "intro": "SkyPrivate est une plateforme cam à part — au lieu d'un broadcast RTMP, elle monétise des <strong>appels cam privés pay-per-minute via Skype</strong>. Le client réserve et paie à la minute via le marketplace SkyPrivate, et la visio elle-même passe sur Skype. <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte en <strong>caméra virtuelle</strong> : composez votre scène dans SplitCam, puis choisissez SplitCam comme caméra dans Skype avant de répondre à un appel réservé via SkyPrivate.",
        "quick": "Pour utiliser SkyPrivate avec SplitCam : installer SplitCam, composer la scène, installer Skype avec l'add-on SkyPrivate, dans <em>Video Settings</em> de Skype choisir SplitCam comme caméra et micro, puis répondre aux appels réservés via SkyPrivate — Skype livre votre scène composée au client."
                 "<ol><li>Installer SplitCam.</li><li>Composer la scène dans SplitCam.</li>"
                 "<li>Installer Skype + add-on SkyPrivate.</li>"
                 "<li>Choisir SplitCam comme caméra dans Skype.</li>"
                 "<li>Prendre les appels.</li></ol>",
        "key_how": "SkyPrivate n'utilise ni RTMP ni stream key — il s'appuie sur Skype comme transport vidéo, avec un add-on de facturation à la minute. Installez Skype, installez l'add-on navigateur/desktop SkyPrivate, puis dans Skype ouvrez <strong>Settings → Audio &amp; Video → Camera</strong> et choisissez <strong>SplitCam</strong> à la place de votre webcam. La scène composée de SplitCam (overlays, multicaméras, filtres beauté) devient ce que voit le client SkyPrivate via Skype.",
        "tips": [
            ("Pas de RTMP — flux caméra virtuelle", "Ne cherchez ni URL serveur ni stream key. SkyPrivate passe par Skype, et Skype voit simplement SplitCam comme une webcam. Composez la scène dans SplitCam, puis choisissez SplitCam dans les réglages caméra de Skype."),
            ("Mettez SplitCam aussi en micro", "Dans les réglages Audio de Skype, choisissez SplitCam comme micro en plus de la caméra — c'est comme ça que la suppression de bruit, l'audio mixé et la musique d'intro arrivent au client."),
            ("Faites un appel test Skype", "Avant votre premier appel payant SkyPrivate, lancez un appel test gratuit Skype (Echo / Sound Test Service) pour vérifier que SplitCam est bien la caméra active et que la scène est correctement composée."),
            _T_TEST,
        ],
        "faq": [
            ("SkyPrivate utilise-t-il RTMP ou une stream key ?", "Ni l'un ni l'autre. SkyPrivate gère la réservation et la facturation ; la vidéo passe en réalité par Skype. Pas besoin d'URL serveur RTMP ni de stream key — il suffit de configurer SplitCam comme caméra dans Skype."),
            ("Comment sélectionner SplitCam dans Skype pour SkyPrivate ?", "Ouvrez Skype Settings → Audio &amp; Video → Camera, choisissez SplitCam dans la liste. Faites pareil dans Microphone. Les appels SkyPrivate arrivent ensuite comme des appels Skype classiques, avec votre scène SplitCam en caméra."),
            ("Puis-je utiliser overlays et filtres beauté avec SkyPrivate ?", "Oui — composez-les dans votre scène SplitCam. Skype ne reçoit que le résultat composé comme une caméra unique, donc tout ce que SplitCam compose (overlays, filtres beauté, fond IA, scènes multicaméras) est visible côté client SkyPrivate."),
            ("SplitCam est-il gratuit pour SkyPrivate ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. En caméra virtuelle pour les appels SkyPrivate via Skype il n'ajoute ni coût ni marquage à l'appel."),
        ],
        "steps": [
            ("Installez SplitCam",
             "SplitCam est gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Pour SkyPrivate il sert de <strong>caméra virtuelle</strong> que Skype reconnaît comme n'importe quelle webcam."),
            ("Composez votre scène dans SplitCam",
             "Ouvrez SplitCam et utilisez <strong>Media Layers +</strong> pour ajouter votre webcam plus overlays, texte, filtres beauté ou fond IA. C'est cette scène composée que Skype livrera au client SkyPrivate."),
            ("Installez Skype et l'add-on SkyPrivate",
             "Installez Skype sur le même PC, connectez-vous, puis installez l'add-on / l'app desktop SkyPrivate en suivant l'onboarding SkyPrivate. L'add-on s'occupe de la facturation à la minute côté SkyPrivate."),
            ("Choisissez SplitCam comme caméra et micro dans Skype",
             "Dans Skype ouvrez <strong>Settings → Audio &amp; Video</strong>. Réglez <strong>Camera = SplitCam</strong> et <strong>Microphone = SplitCam</strong>. Lancez un appel test rapide Skype (Echo / Sound Test Service) pour vérifier le rendu image et son."),
            ("Répondez aux appels SkyPrivate",
             "Quand un client SkyPrivate réserve un appel payant, il arrive comme un appel Skype — décrochez. Il voit votre scène composée SplitCam ; SkyPrivate facture à la minute. Vous pouvez ajuster la scène en cours d'appel en l'éditant dans SplitCam — Skype met à jour instantanément."),
        ],
    },
    {
        "slug": "manyvids", "name": "ManyVids",
        "title": "Passer en live sur MV Live (ManyVids) avec SplitCam",
        "desc": "Passer en live sur MV Live de ManyVids avec SplitCam : encodeur externe du Creator Studio, clé RTMP, gratuit, sans filigrane, scènes multicaméras.",
        "kw": "passer en live sur manyvids, manyvids, mv live, manyvids live, manyvids obs, mv live external encoder, manyvids rtmp, manyvids stream key",
        "h1html": 'Comment diffuser sur <span class="accent">MV Live</span> avec SplitCam',
        "h1short": "Diffuser sur MV Live",
        "card": "Configuration de l'encodeur externe pour le Creator Studio MV Live de ManyVids.",
        "intro": "ManyVids est une plateforme d'économie de créateur — ventes de clips, vidéos custom, abonnements fan club et le produit live <strong>MV Live</strong>. Le broadcaster par défaut du Creator Studio passe par navigateur, mais une voie standard <strong>External Encoder</strong> est aussi exposée, et <strong style='color:var(--text)'>SplitCam</strong> gratuit s'y connecte — pour diffuser avec scènes multicaméras, overlays et filtres sur la même plateforme creator-friendly.",
        "quick": "Pour diffuser sur MV Live avec SplitCam : installer SplitCam, composer la scène, dans le Creator Studio ouvrir <em>MV Live → Broadcast Settings → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL et stream key depuis le Creator Studio.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte créateur ManyVids, ouvrez le <strong>Creator Studio</strong> et allez dans <strong>MV Live → Broadcast Settings → External Encoder</strong>. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. Les comptes créateurs doivent être entièrement vérifiés (ID + fiscalité) avant que MV Live soit disponible.",
        "tips": [
            ("Économie de créateur, pas que du live", "ManyVids n'est pas une plateforme cam pure — MV Live est une source de revenus parmi d'autres, aux côtés des ventes de clips, des vidéos custom et des abonnements fan club. Servez-vous du live pour pousser les viewers vers vos autres monétisations."),
            ("Tipping par tokens dans MV Live", "MV Live a son propre système de tipping par tokens dans la salle. Préparez des menus d'objectifs et des triggers de récompense façon Chaturbate / Stripchat — ça convertit bien sur l'audience existante de ManyVids."),
            ("Browser vs encodeur externe", "Le broadcaster intégré navigateur du Creator Studio est mono-caméra. SplitCam via External Encoder débloque multicaméras, overlays et filtres."),
            _T_ETH,
        ],
        "faq": [
            ("MV Live (ManyVids) supporte-t-il les encodeurs externes comme SplitCam ?", "Oui — la section MV Live du Creator Studio propose une option External Encoder dans Broadcast Settings. URL serveur RTMP standard et stream key ; OBS, SplitCam, vMix s'y connectent."),
            ("Où je récupère ma stream key MV Live ?", "Creator Studio → MV Live → Broadcast Settings → External Encoder. URL serveur et stream key apparaissent là — copiez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour MV Live ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test intégré de SplitCam."),
            ("SplitCam est-il gratuit avec MV Live ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de ManyVids est gratuite dans le Creator Studio."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène",
             "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — parfait pour les menus d'objectifs et triggers de récompense MV Live."),
            ("Récupérez votre URL et stream key MV Live",
             "Connectez-vous à votre compte créateur ManyVids, ouvrez le <strong>Creator Studio</strong> et allez dans <strong>MV Live → Broadcast Settings → External Encoder</strong>. La page révèle une <strong>URL serveur</strong> et une <strong>stream key</strong> unique. Copiez les deux."),
            ("Connectez SplitCam à MV Live",
             "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur MV Live et la stream key dans les champs RTMP personnalisé. Réglez le bitrate à 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live",
             "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis démarrez la diffusion MV Live depuis le Creator Studio. En ~10 secondes votre flux atteint l'audience MV Live."),
        ],
    },
    {
        "slug": "fansly", "name": "Fansly",
        "title": "Passer en live sur Fansly avec SplitCam — encodeur",
        "desc": "Passer en live sur Fansly avec SplitCam : encodeur externe du Creator Dashboard, clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "passer en live sur fansly, fansly, fansly live, fansly broadcast, fansly obs, fansly external encoder, fansly rtmp, fansly stream key",
        "h1html": 'Comment diffuser sur <span class="accent">Fansly Live</span> avec SplitCam',
        "h1short": "Diffuser sur Fansly",
        "card": "Configuration de l'encodeur externe pour le Creator Dashboard de Fansly.",
        "intro": "Fansly est un concurrent direct d'OnlyFans, avec des règles de contenu plus souples et une base de créateurs en pleine croissance — abonnements, pay-per-view et le produit live <strong>Fansly Live</strong>. Le broadcaster par défaut passe par navigateur, mais le <strong>Creator Dashboard</strong> expose aussi une voie standard <strong>External Encoder</strong> à laquelle <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte — pour diffuser avec scènes multicaméras, overlays et filtres vers votre base d'abonnés.",
        "quick": "Pour diffuser sur Fansly Live avec SplitCam : installer SplitCam, composer la scène, dans le Creator Dashboard ouvrir <em>Live → Broadcast Settings → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL et stream key depuis le Creator Dashboard.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte créateur Fansly, ouvrez le <strong>Creator Dashboard</strong> et allez dans <strong>Live → Broadcast Settings → External Encoder</strong>. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. Les comptes créateurs doivent passer une vérification d'identité avant que Fansly Live soit activé.",
        "tips": [
            ("Audience d'abonnés d'abord", "L'audience de Fansly est en abonnement — votre live touche des gens qui vous paient déjà tous les mois. Préparez du contenu qui récompense la fidélité (Q&amp;R exclusifs, coulisses, objectifs de pourboire custom) plutôt que de courir après les métriques de salle publique."),
            ("Pourboires en plus des abonnements", "Fansly Live supporte le tipping en direct en plus de l'abonnement de base. Les revenus combinés peuvent dépasser le tipping pur des plateformes cam pour les créateurs établis."),
            ("Broadcaster navigateur vs externe", "Le broadcaster navigateur par défaut est mono-source. SplitCam via External Encoder débloque multicaméras, overlays, filtres beauté et fond IA, au niveau de finition du contenu payant pour abonnés."),
            _T_ETH,
        ],
        "faq": [
            ("Fansly Live supporte-t-il les encodeurs externes comme SplitCam ?", "Oui — la section Live du Creator Dashboard propose une option External Encoder dans Broadcast Settings. URL serveur RTMP standard et stream key ; OBS, SplitCam, vMix s'y connectent."),
            ("Où je récupère ma stream key Fansly ?", "Creator Dashboard → Live → Broadcast Settings → External Encoder. URL serveur et stream key apparaissent là. Copiez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour Fansly Live ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test intégré de SplitCam."),
            ("SplitCam est-il gratuit avec Fansly ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de Fansly est gratuite dans le Creator Dashboard."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène",
             "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — une scène soignée colle aux attentes premium de vos abonnés payants."),
            ("Récupérez votre URL et stream key Fansly",
             "Connectez-vous à votre compte créateur Fansly, ouvrez le <strong>Creator Dashboard</strong> et allez dans <strong>Live → Broadcast Settings → External Encoder</strong>. La page révèle une <strong>URL serveur</strong> et une <strong>stream key</strong> unique. Copiez les deux."),
            ("Connectez SplitCam à Fansly",
             "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur Fansly et la stream key dans les champs RTMP personnalisé. Réglez le bitrate à 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live",
             "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis démarrez la diffusion Fansly Live depuis le Creator Dashboard. En ~10 secondes votre flux atteint vos abonnés Fansly."),
        ],
    },
    {
        "slug": "ifriends", "name": "iFriends",
        "title": "Diffuser sur iFriends avec SplitCam — encodeur",
        "desc": "Diffuser sur iFriends avec SplitCam : encodeur externe du Model Center, clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur ifriends, ifriends, ifriends broadcast, ifriends obs, ifriends external encoder, ifriends rtmp, ifriends stream key",
        "h1html": 'Comment diffuser sur <span class="accent">iFriends</span> avec SplitCam',
        "h1short": "Diffuser sur iFriends",
        "card": "Configuration de l'encodeur externe pour le Model Center historique d'iFriends.",
        "intro": "iFriends (WebPower) est l'un des plus anciens réseaux cam indépendants — discrètement rentable, base d'utilisateurs fidèle et un <strong>Model Center</strong> conçu bien avant la mode des broadcasters par navigateur. La plateforme propose un parcours standard <strong>External Encoder</strong> depuis le Model Center auquel <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte — pour diffuser avec des scènes multicaméras modernes, des overlays et des filtres sur ce réseau bien implanté.",
        "quick": "Pour diffuser sur iFriends avec SplitCam : installer SplitCam, composer la scène, dans le Model Center ouvrir <em>Broadcast Settings → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL et stream key depuis le Model Center.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte modèle iFriends, ouvrez le <strong>Model Center</strong> et allez dans <strong>Broadcast Settings → External Encoder</strong>. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. L'approbation des nouveaux comptes modèles chez iFriends est exigeante mais légitime ; une fois vérifiée, l'option encodeur externe reste disponible indéfiniment.",
        "tips": [
            ("Audience longue traîne, réseau historique", "iFriends tourne depuis la fin des années 90 avec une base d'utilisateurs fidèle — beaucoup sont des abonnés de longue date, pas des nouveaux venus. Revenus stables pour les modèles installées, croissance plus lente pour les nouvelles."),
            ("Broadcaster navigateur vs externe", "L'ancien broadcaster d'iFriends date d'avant l'UX multicaméra moderne. Passer à SplitCam via External Encoder est un vrai bond en avant — scènes multicaméras, overlays et filtres beauté que l'ancien outil ne peut pas offrir."),
            ("Paiements stables, moins de mauvaises surprises", "La maison mère d'iFriends (WebPower) paie ses modèles avec fiabilité depuis des décennies — calendriers de paiement plus lents que les plateformes crypto-friendly récentes, mais très peu de mauvaises histoires."),
            _T_ETH,
        ],
        "faq": [
            ("iFriends supporte-t-il officiellement les encodeurs externes comme SplitCam ?", "Oui — le Model Center propose une option External Encoder dans Broadcast Settings. URL serveur RTMP standard et stream key ; OBS, SplitCam, vMix s'y connectent une fois votre compte approuvé."),
            ("Où je récupère ma stream key iFriends ?", "Model Center → Broadcast Settings → External Encoder. URL serveur et stream key apparaissent là — copiez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour iFriends ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test intégré de SplitCam."),
            ("SplitCam est-il gratuit avec iFriends ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe d'iFriends est gratuite dans le Model Center."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène",
             "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — une scène moderne et soignée se démarque sur ce réseau historique."),
            ("Récupérez votre URL et stream key iFriends",
             "Connectez-vous à votre compte modèle iFriends, ouvrez le <strong>Model Center</strong> et allez dans <strong>Broadcast Settings → External Encoder</strong>. La page révèle une <strong>URL serveur</strong> et une <strong>stream key</strong> unique. Copiez les deux."),
            ("Connectez SplitCam à iFriends",
             "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur iFriends et la stream key dans les champs RTMP personnalisé. Réglez le bitrate à 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live",
             "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis le Model Center iFriends. En ~10 secondes votre flux atteint le réseau."),
        ],
    },
    {
        "slug": "babestation", "name": "Babestation",
        "title": "Diffuser sur Babestation avec SplitCam — encodeur",
        "desc": "Diffuser sur Babestation avec SplitCam : encodeur externe du Performer Hub, clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur babestation, babestation, babestation broadcast, babestation obs, babestation external encoder, babestation rtmp, babestation stream key",
        "h1html": 'Comment diffuser sur <span class="accent">Babestation</span> avec SplitCam',
        "h1short": "Diffuser sur Babestation",
        "card": "Configuration de l'encodeur externe pour le Performer Hub britannique de Babestation.",
        "intro": "Babestation est le réseau leader de TV adulte et cam au Royaume-Uni — un hybride de chaînes de télévision et d'un produit cam en direct alimenté par les performeuses connectées au Performer Hub. La plateforme propose un parcours standard <strong>External Encoder</strong> depuis le Performer Hub auquel <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte — pour permettre aux performeuses indépendantes britanniques de diffuser avec scènes multicaméras, overlays et filtres beauté qui dépassent le broadcaster par défaut au look studio TV.",
        "quick": "Pour diffuser sur Babestation avec SplitCam : installer SplitCam, composer la scène, dans le Performer Hub ouvrir <em>Broadcast Settings → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL et stream key depuis le Performer Hub.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte performeuse Babestation, ouvrez le <strong>Performer Hub</strong> et allez dans <strong>Broadcast Settings → External Encoder</strong>. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. L'onboarding des performeuses au Royaume-Uni inclut une vérification d'identité, en application de la réglementation britannique de vérification d'âge.",
        "tips": [
            ("Audience et horaires britanniques d'abord", "Le pic de trafic de Babestation tombe sur la soirée / nuit britannique (GMT/BST). Si vous êtes dans un autre fuseau, diffuser pendant la nuit UK rapporte nettement plus que viser votre prime time local."),
            ("Finition studio TV attendue", "La marque Babestation est liée à ses chaînes TV — les viewers attendent des décors et un éclairage plus produits qu'un stream webcam classique. Les scènes SplitCam (overlays, texte brandé, fond IA) aident à coller à l'esthétique soignée de la plateforme."),
            ("Performeuses indépendantes vs studio", "Babestation travaille à la fois avec des studios britanniques et des performeuses indépendantes. Les indépendantes connectées via External Encoder ont le même modèle de paiement que les caméras alimentées par studio."),
            _T_ETH,
        ],
        "faq": [
            ("Babestation supporte-t-il les encodeurs externes comme SplitCam ?", "Oui — le Performer Hub propose une option External Encoder dans Broadcast Settings. URL serveur RTMP standard et stream key ; OBS, SplitCam, vMix s'y connectent une fois la vérification performeuse terminée."),
            ("Où je récupère ma stream key Babestation ?", "Performer Hub → Broadcast Settings → External Encoder. URL serveur et stream key apparaissent là — copiez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour Babestation ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. La bande passante montante au Royaume-Uni est généralement solide, mais lancez d'abord le speed test SplitCam."),
            ("SplitCam est-il gratuit avec Babestation ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de Babestation est gratuite dans le Performer Hub."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène",
             "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — collez à la finition studio TV de Babestation pour vous démarquer."),
            ("Récupérez votre URL et stream key Babestation",
             "Connectez-vous à votre compte performeuse Babestation, ouvrez le <strong>Performer Hub</strong> et allez dans <strong>Broadcast Settings → External Encoder</strong>. La page révèle une <strong>URL serveur</strong> et une <strong>stream key</strong> unique. Copiez les deux."),
            ("Connectez SplitCam à Babestation",
             "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur Babestation et la stream key dans les champs RTMP personnalisé. Réglez le bitrate à 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live",
             "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis le Performer Hub. En ~10 secondes votre flux atteint l'audience britannique de Babestation."),
        ],
    },
    {
        "slug": "adultwork", "name": "AdultWork",
        "title": "Diffuser sur AdultWork avec SplitCam — encodeur",
        "desc": "Diffuser sur AdultWork avec SplitCam : encodeur externe du Members Area, clé RTMP, gratuit, sans filigrane, scènes multicaméras et overlays.",
        "kw": "diffuser sur adultwork, adultwork, adultwork broadcast, adultwork obs, adultwork external encoder, adultwork rtmp, adultwork stream key",
        "h1html": 'Comment diffuser sur <span class="accent">AdultWork</span> avec SplitCam',
        "h1short": "Diffuser sur AdultWork",
        "card": "Configuration de l'encodeur externe pour la fonction cam du Members Area britannique d'AdultWork.",
        "intro": "AdultWork est le marketplace britannique établi des services pour adultes — connu surtout pour les réservations escort, la vente de photos / vidéos et les services téléphoniques, avec une <strong>fonction webcam</strong> en direct à côté. La plateforme propose un parcours standard <strong>External Encoder</strong> depuis le Members Area auquel <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte — pour permettre aux performeuses indépendantes britanniques d'ajouter des revenus cam en direct avec scènes multicaméras, overlays et filtres.",
        "quick": "Pour diffuser sur AdultWork avec SplitCam : installer SplitCam, composer la scène, dans le Members Area ouvrir <em>Members → Broadcasting → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL et stream key depuis le Members Area.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte performeuse AdultWork, ouvrez le <strong>Members Area</strong> et allez dans <strong>Members → Broadcasting → External Encoder</strong>. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. La vérification AdultWork est obligatoire pour la fonction cam en direct et couvre la conformité à la vérification d'âge britannique.",
        "tips": [
            ("Cross-sell depuis les autres services AdultWork", "La force d'AdultWork est sa base de clients existante — vos viewers réservent peut-être déjà vos services photo / vidéo / téléphone. Utilisez les lives cam pour faire du cross-sell auprès des clients qui n'ont pas encore essayé votre cam, pas pour courir après des inconnus."),
            ("Le Members Area est le point d'entrée", "Ne cherchez pas le broadcaster sur la partie publique du site — tout le côté performeuse vit dans le Members Area. Réglages de diffusion, paiements, gestion de contenu sont là."),
            ("Centré UK mais paiements internationaux", "L'essentiel du trafic est UK/UE. Les paiements fonctionnent à l'international via virement bancaire / e-wallet standard, avec des calendriers hebdomadaires fréquents sur la plateforme."),
            _T_ETH,
        ],
        "faq": [
            ("AdultWork supporte-t-il les encodeurs externes comme SplitCam ?", "Oui — le Members Area propose une option External Encoder dans Broadcasting. URL serveur RTMP standard et stream key ; OBS, SplitCam, vMix s'y connectent une fois la performeuse vérifiée."),
            ("Où je récupère ma stream key AdultWork ?", "Members Area → Members → Broadcasting → External Encoder. URL serveur et stream key apparaissent là — copiez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour AdultWork ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test intégré de SplitCam."),
            ("SplitCam est-il gratuit avec AdultWork ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe d'AdultWork est gratuite dans le Members Area."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam",
             "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène",
             "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — utilisez les overlays pour mettre en avant votre contenu AdultWork / vos services téléphoniques et faire du cross-sell pendant le live."),
            ("Récupérez votre URL et stream key AdultWork",
             "Connectez-vous à votre compte performeuse AdultWork, ouvrez le <strong>Members Area</strong> et allez dans <strong>Members → Broadcasting → External Encoder</strong>. La page révèle une <strong>URL serveur</strong> et une <strong>stream key</strong> unique. Copiez les deux."),
            ("Connectez SplitCam à AdultWork",
             "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur AdultWork et la stream key dans les champs RTMP personnalisé. Réglez le bitrate à 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live",
             "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis le Members Area. En ~10 secondes votre flux atteint l'audience d'AdultWork."),
        ],
    },
    {
        "slug": "jerkmate", "name": "Jerkmate",
        "title": "Diffuser sur Jerkmate avec SplitCam — SM Connect",
        "desc": "Diffuser sur Jerkmate avec SplitCam : Jerkmate puise ses modèles dans le réseau Streamate, vous streamez via SM Connect, gratuit, sans filigrane.",
        "kw": "diffuser sur jerkmate, jerkmate, jerkmate broadcast, jerkmate obs, jerkmate streamate, jerkmate sm connect, jerkmate rtmp",
        "h1html": 'Comment streamer sur <span class="accent">Jerkmate</span> avec SplitCam',
        "h1short": "Streamer sur Jerkmate",
        "card": "Jerkmate puise ses modèles dans le réseau Streamate — streamez via SM Connect + SplitCam.",
        "intro": "Jerkmate est l'une des marques cam les plus recherchées, connue pour son matchmaker IA qui associe spectateurs et performeurs en live. Elle ne gère pas son propre broadcaster — Jerkmate <strong>puise ses modèles live dans le réseau Streamate</strong>. Vous diffusez en tant que modèle du réseau Streamate, et votre show est distribué sur Jerkmate et ses sites partenaires. Comme Streamate est <strong style='color:var(--text)'>préconfiguré dans la liste des canaux de SplitCam</strong>, <strong style='color:var(--text)'>SplitCam</strong> gratuit vous laisse ajouter scènes multi-caméras, overlays et filtres sans aucune saisie RTMP manuelle.",
        "quick": "Diffuser sur Jerkmate avec SplitCam : installer SplitCam, composer la scène, s'inscrire comme modèle sur le réseau Streamate qui alimente Jerkmate, ouvrir <em>SM Connect → Start Show</em> et copier la clé, puis dans SplitCam ouvrir <em>Stream Settings → Add Channel → Streamate</em>, la coller et Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>S'inscrire comme modèle du réseau Streamate.</li>"
                 "<li>Récupérer la clé via SM Connect.</li>"
                 "<li>Add Channel → Streamate, Go Live.</li></ol>",
        "key_how": "Les cams live de Jerkmate viennent du <strong>réseau de diffusion Streamate</strong> — il n'existe pas d'« Jerkmate encoder » séparé. Inscrivez-vous via le programme modèle de Jerkmate ou directement sur le réseau Streamate, ouvrez <strong>SM Connect</strong>, acceptez les conditions, cliquez sur <strong>Start Show</strong> et copiez votre clé de streaming. Dans SplitCam, ouvrez <strong>Stream Settings → Add Channel</strong>, choisissez <strong>Streamate</strong> dans la liste intégrée et collez la clé. Votre flux atteint alors Jerkmate et les sites partenaires du réseau d'un seul coup.",
        "tips": [
            ("C'est le réseau Streamate en dessous", "Ne cherchez pas de broadcaster spécifique à Jerkmate — vous diffusez sur Streamate et Jerkmate le redistribue. Tout ce qui marche pour Streamate (SM Connect, le canal SplitCam intégré) marche pour Jerkmate."),
            ("Convertissez le trafic du matchmaker IA", "Le matchmaker de Jerkmate dirige les spectateurs vers les modèles qui collent à leurs choix — une scène SplitCam soignée avec overlays et bon cadrage convertit ces spectateurs ciblés bien mieux qu'une webcam plate."),
            ("Un flux, plusieurs sites", "Diffuser sur le réseau Streamate vous place sur Jerkmate et ses sites partenaires en même temps — plus de portée avec un seul stream SplitCam, sans réglage supplémentaire."),
            _T_ETH,
        ],
        "faq": [
            ("Jerkmate a-t-il son propre broadcaster ou sa clé de stream ?", "Non — Jerkmate puise ses modèles live dans le réseau Streamate. Vous diffusez en tant que modèle du réseau Streamate via SM Connect, et votre show apparaît automatiquement sur Jerkmate."),
            ("Comment récupérer ma clé de stream Jerkmate ?", "Via SM Connect côté modèle du réseau Streamate : accepter les conditions → Start Show → copier la clé. Collez-la dans le canal Streamate intégré à SplitCam — aucune URL RTMP manuelle nécessaire."),
            ("Quel débit pour Jerkmate ?", "Verrouillez le 1080p à 30 fps. Le flux du réseau est adaptatif, donc un débit plus bas sur une image fixe est normal. Lancez le test de vitesse de SplitCam et utilisez une connexion filaire."),
            ("SplitCam est-il gratuit pour Jerkmate ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. Streamate (qui alimente Jerkmate) est un canal intégré à SplitCam, donc pas de coût d'encodeur séparé."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — une scène solide convertit les spectateurs ciblés de Jerkmate."),
            ("Inscrivez-vous comme modèle et récupérez votre clé", "Inscrivez-vous via le programme modèle de Jerkmate ou directement sur le <strong>réseau Streamate</strong> qui l'alimente. Ouvrez <strong>SM Connect</strong>, acceptez les conditions, cliquez sur <strong>Start Show</strong> et copiez votre clé de streaming."),
            ("Ajoutez Streamate comme canal dans SplitCam", "Ouvrez <strong>Stream Settings → Add Channel</strong>, choisissez <strong>Streamate</strong> dans la liste intégrée et collez la clé — pas d'URL RTMP manuelle. Verrouillez la résolution à 1080p."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam — un slider vert confirme la connexion. Votre show part sur le réseau Streamate et apparaît sur Jerkmate."),
        ],
    },
    {
        "slug": "justforfans", "name": "JustForFans",
        "title": "Passer en live sur JustForFans avec SplitCam",
        "desc": "Passer en live sur JustForFans avec SplitCam : caméra virtuelle ou clé RTMP, gratuit, sans filigrane, scènes multicaméras, overlays et filtres.",
        "kw": "passer en live sur justforfans, justforfans, justforfans live, justforfans virtual camera, justforfans caméra virtuelle, justforfans obs, justforfans rtmp",
        "h1html": 'Comment passer en live sur <span class="accent">JustForFans</span> avec SplitCam',
        "h1short": "Live sur JustForFans",
        "card": "Utilisez SplitCam comme caméra virtuelle dans le broadcaster live de JustForFans.",
        "intro": "JustForFans (JFF) est une plateforme d'abonnement détenue par les créateurs — une alternative à OnlyFans de longue date, fondée par des performeurs, avec abonnements, pay-per-view et un live basé sur le navigateur. Son broadcaster live n'affiche qu'une simple webcam ; le pointer vers <strong style='color:var(--text)'>SplitCam</strong> gratuit comme <strong>caméra virtuelle</strong> débloque scènes multi-caméras, overlays et filtres. Si votre tableau de bord créateur expose aussi une option encodeur externe / clé de stream, SplitCam se connecte plutôt en RTMP.",
        "quick": "Live sur JustForFans avec SplitCam : installer SplitCam, composer la scène, démarrer une diffusion live sur JFF, et dans le sélecteur de caméra du broadcaster choisir <em>SplitCam</em> comme webcam — puis passer en live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Démarrer une diffusion live sur JFF.</li>"
                 "<li>Sélectionner SplitCam dans le menu déroulant caméra.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Le live de JustForFans tourne dans le navigateur. Composez votre scène dans SplitCam — il s'enregistre comme une webcam système nommée <strong>\"SplitCam Video Driver\"</strong> — puis ouvrez le broadcaster live de JFF et, dans le menu déroulant caméra, sélectionnez <strong>SplitCam</strong> au lieu de votre webcam brute. Votre scène composée remplace la caméra plate. Si le tableau de bord créateur de JFF propose une option <strong>encodeur externe / clé de stream</strong>, collez plutôt cette clé dans les champs RTMP personnalisé de SplitCam.",
        "tips": [
            ("La caméra virtuelle marche partout", "Même quand le live d'une plateforme est uniquement dans le navigateur, SplitCam apparaît comme une webcam sélectionnable — votre scène multi-caméras, vos overlays et vos filtres fonctionnent donc sur JFF sans la moindre clé de stream."),
            ("Détenu par les créateurs, pensé pour les performeurs", "JFF est géré par des performeurs et garde une base d'abonnés fidèle. Des overlays qui font la promo croisée de votre PPV ou de votre abonnement convertissent bien auprès d'un public qui paie déjà."),
            ("Autorisez la caméra dans le navigateur", "Si SplitCam n'apparaît pas dans la liste caméra de JFF, vérifiez d'abord que SplitCam tourne et que le navigateur a l'autorisation caméra — puis rechargez le broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Comment SplitCam se connecte-t-il à JustForFans ?", "Le live de JFF est basé sur le navigateur, donc SplitCam se connecte comme caméra virtuelle : choisissez SplitCam dans le sélecteur de caméra du broadcaster JFF. Aucune clé de stream nécessaire."),
            ("Puis-je utiliser des overlays et plusieurs caméras sur JFF ?", "Oui — composez la scène dans SplitCam (deuxième caméra, overlays, filtres beauté ou fond IA) et JFF voit la scène finie comme une seule webcam."),
            ("JustForFans prend-il en charge OBS ou les encodeurs externes ?", "Le live de JFF passe avant tout par navigateur/webcam. Si votre tableau de bord créateur affiche une option encodeur externe ou clé de stream, collez-la dans les champs RTMP personnalisé de SplitCam ; sinon, utilisez la méthode caméra virtuelle."),
            ("SplitCam est-il gratuit pour JustForFans ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Il installe une caméra virtuelle que le navigateur peut sélectionner."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — appliqués en direct."),
            ("Démarrez une diffusion live sur JFF", "Connectez-vous à votre compte créateur JustForFans et ouvrez le broadcaster live pour lancer un stream auprès de vos abonnés."),
            ("Sélectionnez SplitCam comme caméra", "Dans le menu déroulant caméra du broadcaster JFF, choisissez <strong>SplitCam</strong> au lieu de votre webcam brute — votre scène composée remplace la caméra plate. (Ou, si disponible, collez la clé encodeur externe de JFF dans les champs RTMP personnalisé de SplitCam.)"),
            ("Go Live", "Lancez la diffusion — votre scène SplitCam, vos overlays et vos filtres atteignent vos abonnés JustForFans."),
        ],
    },
    {
        "slug": "fanvue", "name": "Fanvue",
        "title": "Passer en live sur Fanvue avec SplitCam",
        "desc": "Passer en live sur Fanvue avec SplitCam comme caméra virtuelle : scènes multicaméras, overlays et filtres pour vos abonnés, gratuit, sans filigrane.",
        "kw": "passer en live sur fanvue, fanvue live, fanvue stream, fanvue obs, fanvue caméra virtuelle, fanvue créateur, fanvue diffusion",
        "h1html": 'Comment passer en live sur <span class="accent">Fanvue</span> avec SplitCam',
        "h1short": "Live sur Fanvue",
        "card": "Utilisez SplitCam comme caméra virtuelle pour le live Fanvue.",
        "intro": "Fanvue est une plateforme d'abonnement créateur britannique en pleine croissance — une alternative à OnlyFans réputée pour son ouverture aux créateurs et à l'IA, avec abonnements, pay-per-view et live. Son broadcaster live tourne dans le navigateur ; le pointer vers <strong style='color:var(--text)'>SplitCam</strong> gratuit comme <strong>caméra virtuelle</strong> débloque scènes multi-caméras, overlays et filtres. Si votre tableau de bord créateur expose une option encodeur externe / clé de stream, SplitCam se connecte plutôt en RTMP.",
        "quick": "Live sur Fanvue avec SplitCam : installer SplitCam, composer la scène, démarrer une diffusion live sur Fanvue, et dans le sélecteur de caméra du broadcaster choisir <em>SplitCam</em> — puis passer en live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Démarrer une diffusion live sur Fanvue.</li>"
                 "<li>Sélectionner SplitCam dans le menu déroulant caméra.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Le live de Fanvue tourne dans le navigateur. Composez votre scène dans SplitCam — il s'enregistre comme une webcam système nommée <strong>\"SplitCam Video Driver\"</strong> — puis ouvrez le broadcaster live de Fanvue et, dans le menu déroulant caméra, sélectionnez <strong>SplitCam</strong> au lieu de votre webcam brute. Si votre tableau de bord créateur propose une option <strong>encodeur externe / clé de stream</strong>, collez plutôt cette clé dans les champs RTMP personnalisé de SplitCam.",
        "tips": [
            ("La caméra virtuelle marche partout", "Même quand le live d'une plateforme est uniquement dans le navigateur, SplitCam apparaît comme une webcam sélectionnable — scènes multi-caméras, overlays et filtres fonctionnent sur Fanvue sans la moindre clé de stream."),
            ("Ouvert aux créateurs et à l'IA", "Fanvue accueille les créateurs IA et paie proprement. Des overlays qui font la promo croisée de votre abonnement ou de votre PPV convertissent bien un public qui paie déjà."),
            ("Autorisez la caméra dans le navigateur", "Si SplitCam n'apparaît pas dans la liste caméra de Fanvue, vérifiez d'abord que SplitCam tourne et que le navigateur a l'autorisation caméra, puis rechargez."),
            _T_TEST,
        ],
        "faq": [
            ("Comment SplitCam se connecte-t-il à Fanvue ?", "Le live de Fanvue est basé sur le navigateur, donc SplitCam se connecte comme caméra virtuelle : choisissez SplitCam dans le sélecteur de caméra. Aucune clé de stream nécessaire."),
            ("Puis-je utiliser des overlays et plusieurs caméras sur Fanvue ?", "Oui — composez la scène dans SplitCam (deuxième caméra, overlays, filtres beauté ou fond IA) et Fanvue voit la scène finie comme une seule webcam."),
            ("Fanvue prend-il en charge OBS ou les encodeurs externes ?", "Le live de Fanvue passe avant tout par navigateur/webcam. Si votre tableau de bord affiche une option encodeur externe ou clé de stream, collez-la dans les champs RTMP personnalisé de SplitCam ; sinon, utilisez la méthode caméra virtuelle."),
            ("SplitCam est-il gratuit pour Fanvue ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Il installe une caméra virtuelle que le navigateur peut sélectionner."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — appliqués en direct."),
            ("Démarrez une diffusion live sur Fanvue", "Connectez-vous à votre compte créateur Fanvue et ouvrez le broadcaster live pour lancer un stream auprès de vos abonnés."),
            ("Sélectionnez SplitCam comme caméra", "Dans le menu déroulant caméra de Fanvue, choisissez <strong>SplitCam</strong> au lieu de votre webcam brute — votre scène composée remplace la caméra plate. (Ou, si disponible, collez une clé de stream dans les champs RTMP personnalisé de SplitCam.)"),
            ("Go Live", "Lancez la diffusion — votre scène SplitCam, vos overlays et vos filtres atteignent vos abonnés Fanvue."),
        ],
    },
    {
        "slug": "loyalfans", "name": "LoyalFans",
        "title": "Passer en live sur LoyalFans avec SplitCam",
        "desc": "Passer en live sur LoyalFans avec SplitCam comme caméra virtuelle : scènes multicaméras, overlays et filtres pour vos abonnés, gratuit, sans filigrane.",
        "kw": "passer en live sur loyalfans, loyalfans live, loyalfans stream, loyalfans obs, loyalfans caméra virtuelle, loyalfans diffusion, loyal fans",
        "h1html": 'Comment passer en live sur <span class="accent">LoyalFans</span> avec SplitCam',
        "h1short": "Live sur LoyalFans",
        "card": "Utilisez SplitCam comme caméra virtuelle pour le live LoyalFans.",
        "intro": "LoyalFans est une plateforme d'abonnement créateur avec abonnements, pay-per-view, tips et une fonction <strong>live cam</strong> intégrée. Le broadcaster live tourne dans le navigateur ; brancher <strong style='color:var(--text)'>SplitCam</strong> gratuit comme <strong>caméra virtuelle</strong> ajoute scènes multi-caméras, overlays et filtres par-dessus la webcam standard. Si votre tableau de bord expose une option encodeur externe / clé de stream, SplitCam se connecte plutôt en RTMP.",
        "quick": "Live sur LoyalFans avec SplitCam : installer SplitCam, composer la scène, démarrer une diffusion live sur LoyalFans, et choisir <em>SplitCam</em> dans le sélecteur de caméra du broadcaster — puis passer en live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Démarrer une diffusion live sur LoyalFans.</li>"
                 "<li>Sélectionner SplitCam dans le menu déroulant caméra.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Le live de LoyalFans tourne dans le navigateur. Composez votre scène dans SplitCam — il s'enregistre comme une webcam système nommée <strong>\"SplitCam Video Driver\"</strong> — puis ouvrez le broadcaster live de LoyalFans et sélectionnez <strong>SplitCam</strong> dans le menu déroulant caméra. Si une option <strong>clé de stream / encodeur externe</strong> apparaît dans votre tableau de bord créateur, collez-la plutôt dans les champs RTMP personnalisé de SplitCam.",
        "tips": [
            ("Caméra virtuelle, sans clé", "Un live basé sur navigateur récupère quand même toute votre scène SplitCam — overlays, deuxième caméra et filtres — simplement en sélectionnant SplitCam comme webcam."),
            ("Les tips récompensent la qualité", "LoyalFans repose sur les tips ; des overlays d'objectifs de tips à l'écran et une scène soignée poussent les tippeurs plus qu'une webcam plate."),
            ("Autorisez la caméra dans le navigateur", "Si SplitCam n'est pas dans la liste caméra de LoyalFans, lancez d'abord SplitCam, autorisez l'accès caméra dans le navigateur, puis rechargez le broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Comment SplitCam se connecte-t-il à LoyalFans ?", "Le live de LoyalFans est basé sur le navigateur, donc SplitCam se connecte comme caméra virtuelle — choisissez SplitCam dans le sélecteur de caméra. Aucune clé de stream nécessaire."),
            ("Puis-je utiliser des overlays et plusieurs caméras sur LoyalFans ?", "Oui — composez la scène dans SplitCam (deuxième caméra, overlays, filtres beauté ou fond IA) ; LoyalFans la voit comme une seule webcam."),
            ("LoyalFans prend-il en charge OBS ou les encodeurs externes ?", "Son live passe avant tout par navigateur/webcam. Si votre tableau de bord affiche une option clé de stream, collez-la dans les champs RTMP personnalisé de SplitCam ; sinon, utilisez la méthode caméra virtuelle."),
            ("SplitCam est-il gratuit pour LoyalFans ?", "Oui — gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Il installe une caméra virtuelle que le navigateur peut sélectionner."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte d'objectif de tips, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Démarrez une diffusion live sur LoyalFans", "Connectez-vous à votre compte LoyalFans et ouvrez le broadcaster live pour passer en live auprès de vos abonnés."),
            ("Sélectionnez SplitCam comme caméra", "Dans le menu déroulant caméra de LoyalFans, choisissez <strong>SplitCam</strong> au lieu de votre webcam brute — votre scène remplace la caméra plate. (Ou, si disponible, collez une clé de stream dans les champs RTMP personnalisé de SplitCam.)"),
            ("Go Live", "Lancez la diffusion — votre scène SplitCam atteint votre audience LoyalFans."),
        ],
    },
    {
        "slug": "fancentro", "name": "FanCentro",
        "title": "Passer en live sur FanCentro avec SplitCam",
        "desc": "Passer en live sur FanCentro avec SplitCam comme caméra virtuelle : scènes multicaméras, overlays et filtres pour vos abonnés, gratuit, sans filigrane.",
        "kw": "passer en live sur fancentro, fancentro live, fancentro stream, fancentro obs, fancentro caméra virtuelle, fancentro diffusion, fan centro",
        "h1html": 'Comment passer en live sur <span class="accent">FanCentro</span> avec SplitCam',
        "h1short": "Live sur FanCentro",
        "card": "Utilisez SplitCam comme caméra virtuelle pour le live FanCentro.",
        "intro": "FanCentro est une plateforme de monétisation créateur de longue date — abonnements, messages pay-per-view, contenu et live. Son live tourne dans le navigateur ; brancher <strong style='color:var(--text)'>SplitCam</strong> gratuit comme <strong>caméra virtuelle</strong> ajoute scènes multi-caméras, overlays et filtres au-delà de la simple webcam. Si votre tableau de bord expose une option encodeur externe / clé de stream, SplitCam se connecte plutôt en RTMP.",
        "quick": "Live sur FanCentro avec SplitCam : installer SplitCam, composer la scène, démarrer une diffusion live sur FanCentro, et choisir <em>SplitCam</em> dans le sélecteur de caméra du broadcaster — puis passer en live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Démarrer une diffusion live sur FanCentro.</li>"
                 "<li>Sélectionner SplitCam dans le menu déroulant caméra.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Le live de FanCentro tourne dans le navigateur. Composez votre scène dans SplitCam — il s'enregistre comme une webcam système nommée <strong>\"SplitCam Video Driver\"</strong> — puis ouvrez le broadcaster live de FanCentro et choisissez <strong>SplitCam</strong> dans le menu déroulant caméra. Si une option <strong>clé de stream / encodeur externe</strong> est proposée, collez-la plutôt dans les champs RTMP personnalisé de SplitCam.",
        "tips": [
            ("La caméra virtuelle marche partout", "Un live uniquement navigateur récupère quand même toute votre scène SplitCam — overlays, deuxième caméra et filtres — en sélectionnant SplitCam comme webcam."),
            ("Faites du cross-sell sur votre funnel", "FanCentro est bâti autour des funnels créateur et du PPV. Des overlays qui promeuvent votre abonnement ou vos messages payants convertissent vos spectateurs live en acheteurs."),
            ("Autorisez la caméra dans le navigateur", "Si SplitCam n'est pas listé, lancez d'abord SplitCam, autorisez l'accès caméra dans le navigateur, puis rechargez le broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Comment SplitCam se connecte-t-il à FanCentro ?", "Le live de FanCentro est basé sur le navigateur, donc SplitCam se connecte comme caméra virtuelle — choisissez SplitCam dans le sélecteur de caméra. Aucune clé de stream nécessaire."),
            ("Puis-je utiliser des overlays et plusieurs caméras sur FanCentro ?", "Oui — composez la scène dans SplitCam ; FanCentro voit la scène finie comme une seule webcam."),
            ("FanCentro prend-il en charge OBS ou les encodeurs externes ?", "Son live passe avant tout par navigateur/webcam. Si une option clé de stream apparaît dans votre tableau de bord, collez-la dans les champs RTMP personnalisé de SplitCam ; sinon, utilisez la méthode caméra virtuelle."),
            ("SplitCam est-il gratuit pour FanCentro ?", "Oui — gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Il installe une caméra virtuelle que le navigateur peut sélectionner."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Démarrez une diffusion live sur FanCentro", "Connectez-vous à votre compte FanCentro et ouvrez le broadcaster live pour passer en live auprès de vos abonnés."),
            ("Sélectionnez SplitCam comme caméra", "Dans le menu déroulant caméra de FanCentro, choisissez <strong>SplitCam</strong> au lieu de votre webcam brute. (Ou, si disponible, collez une clé de stream dans les champs RTMP personnalisé de SplitCam.)"),
            ("Go Live", "Lancez la diffusion — votre scène SplitCam atteint vos abonnés FanCentro."),
        ],
    },
    {
        "slug": "ismygirl", "name": "IsMyGirl",
        "title": "Passer en live sur IsMyGirl avec SplitCam",
        "desc": "Passer en live sur IsMyGirl avec SplitCam comme caméra virtuelle : scènes multicaméras, overlays et filtres pour vos abonnés, gratuit, sans filigrane.",
        "kw": "passer en live sur ismygirl, ismygirl live, ismygirl stream, ismygirl obs, ismygirl caméra virtuelle, ismygirl diffusion, is my girl",
        "h1html": 'Comment passer en live sur <span class="accent">IsMyGirl</span> avec SplitCam',
        "h1short": "Live sur IsMyGirl",
        "card": "Utilisez SplitCam comme caméra virtuelle pour le live IsMyGirl.",
        "intro": "IsMyGirl est une plateforme d'abonnement créateur — une alternative à OnlyFans avec abonnements, contenu payant et live, réputée pour son accompagnement créateur très présent. Le broadcaster live tourne dans le navigateur ; brancher <strong style='color:var(--text)'>SplitCam</strong> gratuit comme <strong>caméra virtuelle</strong> apporte scènes multi-caméras, overlays et filtres. Si votre tableau de bord expose une option encodeur externe / clé de stream, SplitCam se connecte plutôt en RTMP.",
        "quick": "Live sur IsMyGirl avec SplitCam : installer SplitCam, composer la scène, démarrer une diffusion live sur IsMyGirl, et sélectionner <em>SplitCam</em> dans le sélecteur de caméra du broadcaster — puis passer en live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Démarrer une diffusion live sur IsMyGirl.</li>"
                 "<li>Sélectionner SplitCam dans le menu déroulant caméra.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Le live d'IsMyGirl tourne dans le navigateur. Composez votre scène dans SplitCam — il s'enregistre comme une webcam système nommée <strong>\"SplitCam Video Driver\"</strong> — puis ouvrez le broadcaster live d'IsMyGirl et choisissez <strong>SplitCam</strong> dans le menu déroulant caméra. Si une option <strong>clé de stream / encodeur externe</strong> apparaît, collez-la plutôt dans les champs RTMP personnalisé de SplitCam.",
        "tips": [
            ("Caméra virtuelle, sans clé", "Un live uniquement navigateur récupère quand même toute votre scène SplitCam — overlays, deuxième caméra et filtres — en sélectionnant SplitCam comme webcam."),
            ("Profitez de l'accompagnement créateur", "IsMyGirl met en avant un fort accompagnement et de la promo créateur. Une scène SplitCam soignée plus des overlays de cross-sell tirent le meilleur du trafic qu'ils vous envoient."),
            ("Autorisez la caméra dans le navigateur", "Si SplitCam n'est pas listé, lancez d'abord SplitCam, autorisez l'accès caméra, puis rechargez le broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Comment SplitCam se connecte-t-il à IsMyGirl ?", "Le live d'IsMyGirl est basé sur le navigateur, donc SplitCam se connecte comme caméra virtuelle — choisissez SplitCam dans le sélecteur de caméra. Aucune clé de stream nécessaire."),
            ("Puis-je utiliser des overlays et plusieurs caméras sur IsMyGirl ?", "Oui — composez la scène dans SplitCam ; IsMyGirl la voit comme une seule webcam."),
            ("IsMyGirl prend-il en charge OBS ou les encodeurs externes ?", "Son live passe avant tout par navigateur/webcam. Si une option clé de stream apparaît, collez-la dans les champs RTMP personnalisé de SplitCam ; sinon, utilisez la méthode caméra virtuelle."),
            ("SplitCam est-il gratuit pour IsMyGirl ?", "Oui — gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Il installe une caméra virtuelle que le navigateur peut sélectionner."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Démarrez une diffusion live sur IsMyGirl", "Connectez-vous à votre compte IsMyGirl et ouvrez le broadcaster live pour passer en live auprès de vos abonnés."),
            ("Sélectionnez SplitCam comme caméra", "Dans le menu déroulant caméra d'IsMyGirl, choisissez <strong>SplitCam</strong> au lieu de votre webcam brute. (Ou, si disponible, collez une clé de stream dans les champs RTMP personnalisé de SplitCam.)"),
            ("Go Live", "Lancez la diffusion — votre scène SplitCam atteint vos abonnés IsMyGirl."),
        ],
    },
    {
        "slug": "dxlive", "name": "DXLive",
        "title": "Diffuser sur DXLive avec SplitCam — encodeur",
        "desc": "Diffuser sur DXLive avec SplitCam : encodeur externe pour le réseau cam premium japonais, scènes multicaméras et overlays, gratuit, sans filigrane.",
        "kw": "diffuser sur dxlive, dxlive, dxlive broadcast, dxlive obs, dxlive external encoder, dxlive rtmp, dxlive performer",
        "h1html": 'Comment diffuser sur <span class="accent">DXLive</span> avec SplitCam',
        "h1short": "Diffuser sur DXLive",
        "card": "Configuration de l'encodeur externe pour le réseau cam premium DXLive.",
        "intro": "DXLive est un réseau webcam premium établi, populaire au Japon et dans toute l'Asie, bâti sur un modèle au paiement à la minute avec un public fidèle. L'espace performeuse propose un parcours standard <strong>External Encoder</strong> auquel <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte — pour diffuser avec scènes multicaméras, overlays et filtres beauté au lieu d'une simple webcam plate.",
        "quick": "Pour diffuser sur DXLive avec SplitCam : installer SplitCam, composer la scène, dans l'espace performeuse ouvrir les paramètres <em>External Encoder / broadcast</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL + stream key depuis l'espace performeuse.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte performeuse DXLive et ouvrez les paramètres <strong>broadcast / External Encoder</strong> dans l'espace performeuse. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. La vérification DXLive est obligatoire avant l'activation de la fonction cam en direct.",
        "tips": [
            ("Pensé pour le marché asiatique", "Le public de DXLive penche vers le Japon / l'Asie et paie à la minute. Calez vos shows sur les soirées JST et la base fidèle et payante convertit bien."),
            ("La qualité bat la webcam brute", "Une scène SplitCam propre avec overlays et filtres beauté se démarque sur un réseau premium au paiement à la minute, où les spectateurs attendent de la qualité."),
            ("Utilisez l'encodeur externe, pas juste la webcam", "Passer par le RTMP de SplitCam plutôt que la cam basique du navigateur, c'est ce qui débloque scènes multicaméras et filtres."),
            _T_ETH,
        ],
        "faq": [
            ("DXLive supporte-t-il les encodeurs externes comme SplitCam ?", "Oui — l'espace performeuse propose un parcours standard External Encoder / RTMP. Copiez l'URL serveur et la stream key dans SplitCam une fois la vérification faite."),
            ("Où je récupère ma stream key DXLive ?", "Dans les paramètres broadcast / External Encoder de l'espace performeuse — URL serveur et stream key apparaissent là. Collez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour DXLive ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test intégré de SplitCam."),
            ("SplitCam est-il gratuit avec DXLive ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de DXLive est gratuite dans l'espace performeuse."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Récupérez votre URL et stream key DXLive", "Connectez-vous à votre compte performeuse DXLive et ouvrez les paramètres <strong>broadcast / External Encoder</strong>. Copiez l'<strong>URL serveur</strong> et la <strong>stream key</strong>."),
            ("Connectez SplitCam à DXLive", "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur DXLive et la stream key dans les champs RTMP personnalisé. Réglez 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis l'espace performeuse. En ~10 secondes votre flux atteint l'audience de DXLive."),
        ],
    },
    {
        "slug": "streamen", "name": "Streamen",
        "title": "Diffuser sur Streamen avec SplitCam — encodeur",
        "desc": "Diffuser sur Streamen avec SplitCam : encodeur externe, scènes multicaméras, overlays et filtres beauté, gratuit, sans filigrane, sans inscription.",
        "kw": "diffuser sur streamen, streamen, streamen broadcast, streamen obs, streamen external encoder, streamen rtmp, streamen.tv",
        "h1html": 'Comment diffuser sur <span class="accent">Streamen</span> avec SplitCam',
        "h1short": "Diffuser sur Streamen",
        "card": "Configuration de l'encodeur externe pour la plateforme cam Streamen.",
        "intro": "Streamen est une plateforme cam live où les modèles diffusent vers un public porté par les tips. Ses paramètres de diffusion proposent un parcours standard <strong>External Encoder</strong> auquel <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte — pour streamer avec scènes multicaméras, overlays et filtres plutôt qu'une simple webcam plate.",
        "quick": "Pour diffuser sur Streamen avec SplitCam : installer SplitCam, composer la scène, dans le tableau de bord modèle ouvrir <em>broadcast settings → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL + stream key depuis le tableau de bord.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte modèle Streamen et ouvrez la section <strong>broadcast settings / External Encoder</strong>. Elle affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. La vérification du compte modèle est obligatoire avant l'activation de la diffusion.",
        "tips": [
            ("Public porté par les tips", "Les spectateurs de Streamen donnent des tips — des objectifs de tips à l'écran et une scène soignée poussent plus de tips qu'une webcam plate."),
            ("L'encodeur externe débloque les scènes", "Passer par le RTMP de SplitCam au lieu de la cam basique du navigateur, c'est ce qui active mises en page multicaméras, overlays et filtres."),
            ("Verrouillez votre résolution", "Réglez le 1080p à la main pour que le flux ne baisse pas discrètement la qualité ; un débit qui descend sur une image fixe est normal sur les flux adaptatifs."),
            _T_ETH,
        ],
        "faq": [
            ("Streamen supporte-t-il les encodeurs externes comme SplitCam ?", "Oui — les paramètres de diffusion proposent un parcours standard External Encoder / RTMP. Copiez l'URL serveur et la stream key dans SplitCam une fois la vérification faite."),
            ("Où je récupère ma stream key Streamen ?", "Dans les paramètres broadcast / External Encoder de votre tableau de bord modèle — URL serveur et stream key apparaissent là. Collez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour Streamen ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test de SplitCam."),
            ("SplitCam est-il gratuit avec Streamen ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de Streamen est gratuite dans le tableau de bord."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte d'objectif de tips, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Récupérez votre URL et stream key Streamen", "Connectez-vous à votre compte modèle Streamen, ouvrez <strong>broadcast settings → External Encoder</strong>, et copiez l'<strong>URL serveur</strong> et la <strong>stream key</strong>."),
            ("Connectez SplitCam à Streamen", "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur Streamen et la stream key dans les champs RTMP personnalisé. Réglez 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis votre tableau de bord. En ~10 secondes votre flux atteint l'audience de Streamen."),
        ],
    },
    {
        "slug": "xcams", "name": "XCams",
        "title": "Diffuser sur XCams avec SplitCam — encodeur",
        "desc": "Diffuser sur XCams avec SplitCam : encodeur externe pour la communauté cam européenne, scènes multicaméras, overlays et filtres, gratuit, sans filigrane.",
        "kw": "diffuser sur xcams, xcams, xcams broadcast, xcams obs, xcams external encoder, xcams rtmp, x cams",
        "h1html": 'Comment diffuser sur <span class="accent">XCams</span> avec SplitCam',
        "h1short": "Diffuser sur XCams",
        "card": "Configuration de l'encodeur externe pour la communauté européenne XCams.",
        "intro": "XCams est une communauté cam live européenne — forte en Italie, en France et en Espagne — bâtie autour des shows en direct et d'une économie de tips et de shows privés. L'espace modèle propose un parcours standard <strong>External Encoder</strong> auquel <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte, pour diffuser avec scènes multicaméras, overlays et filtres beauté.",
        "quick": "Pour diffuser sur XCams avec SplitCam : installer SplitCam, composer la scène, dans l'espace modèle ouvrir <em>broadcast / External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL + stream key depuis l'espace modèle.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte modèle XCams et ouvrez les paramètres <strong>broadcast / External Encoder</strong> dans l'espace modèle. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. La vérification XCams est obligatoire avant de diffuser.",
        "tips": [
            ("Prime time européen", "Le trafic XCams culmine en soirée UE (CET). Diffuser à ces heures sur-performe nettement les heures creuses sur cette communauté."),
            ("Les shows privés récompensent la qualité", "XCams fonctionne sur les shows privés / spy — une scène SplitCam soignée avec overlays convertit les curieux en privés payants."),
            ("L'encodeur externe débloque les scènes", "Passer par le RTMP de SplitCam au lieu de la cam du navigateur active mises en page multicaméras, overlays et filtres."),
            _T_ETH,
        ],
        "faq": [
            ("XCams supporte-t-il les encodeurs externes comme SplitCam ?", "Oui — l'espace modèle propose un parcours standard External Encoder / RTMP. Copiez l'URL serveur et la stream key dans SplitCam une fois la vérification faite."),
            ("Où je récupère ma stream key XCams ?", "Dans les paramètres broadcast / External Encoder de l'espace modèle — URL serveur et stream key apparaissent là. Collez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour XCams ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test de SplitCam."),
            ("SplitCam est-il gratuit avec XCams ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de XCams est gratuite dans l'espace modèle."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Récupérez votre URL et stream key XCams", "Connectez-vous à votre compte modèle XCams, ouvrez <strong>broadcast / External Encoder</strong>, et copiez l'<strong>URL serveur</strong> et la <strong>stream key</strong>."),
            ("Connectez SplitCam à XCams", "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur XCams et la stream key dans les champs RTMP personnalisé. Réglez 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis l'espace modèle. En ~10 secondes votre flux atteint l'audience de XCams."),
        ],
    },
    {
        "slug": "camcontacts", "name": "CamContacts",
        "title": "Diffuser sur CamContacts avec SplitCam — encodeur",
        "desc": "Diffuser sur CamContacts avec SplitCam : encodeur externe pour le site cam au paiement à la minute, scènes multicaméras et overlays, sans filigrane.",
        "kw": "diffuser sur camcontacts, camcontacts, camcontacts broadcast, camcontacts obs, camcontacts external encoder, camcontacts rtmp, cam contacts",
        "h1html": 'Comment diffuser sur <span class="accent">CamContacts</span> avec SplitCam',
        "h1short": "Diffuser sur CamContacts",
        "card": "Configuration de l'encodeur externe pour la cam au paiement à la minute de CamContacts.",
        "intro": "CamContacts est l'un des plus anciens sites cam indépendants — un modèle au paiement à la minute avec un public mûr et fidèle, et une réputation de paiements réguliers. L'espace performeuse propose un parcours standard <strong>External Encoder</strong> auquel <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte, pour diffuser avec scènes multicaméras, overlays et filtres beauté.",
        "quick": "Pour diffuser sur CamContacts avec SplitCam : installer SplitCam, composer la scène, dans l'espace performeuse ouvrir les paramètres <em>External Encoder / broadcast</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL + stream key depuis l'espace performeuse.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte performeuse CamContacts et ouvrez les paramètres <strong>broadcast / External Encoder</strong> dans l'espace performeuse. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. La vérification CamContacts est obligatoire pour la fonction cam en direct.",
        "tips": [
            ("Public mûr et fidèle", "CamContacts tourne depuis des décennies avec des membres de longue date — des habitués plus stables et plus payants qu'un site gratuit à fort turnover, mais une croissance plus lente pour les nouvelles venues."),
            ("Le paiement à la minute récompense la rétention", "Gardez les spectateurs en temps payant grâce à une scène soignée et des overlays ; la qualité prolonge les sessions sur un modèle à la minute."),
            ("L'encodeur externe débloque les scènes", "Passer par le RTMP de SplitCam plutôt que la cam basique active mises en page multicaméras, overlays et filtres."),
            _T_ETH,
        ],
        "faq": [
            ("CamContacts supporte-t-il les encodeurs externes comme SplitCam ?", "Oui — l'espace performeuse propose un parcours standard External Encoder / RTMP. Copiez l'URL serveur et la stream key dans SplitCam une fois la vérification faite."),
            ("Où je récupère ma stream key CamContacts ?", "Dans les paramètres broadcast / External Encoder de l'espace performeuse — URL serveur et stream key apparaissent là. Collez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour CamContacts ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test de SplitCam."),
            ("SplitCam est-il gratuit avec CamContacts ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de CamContacts est gratuite dans l'espace performeuse."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Récupérez votre URL et stream key CamContacts", "Connectez-vous à votre compte performeuse CamContacts, ouvrez les paramètres <strong>broadcast / External Encoder</strong>, et copiez l'<strong>URL serveur</strong> et la <strong>stream key</strong>."),
            ("Connectez SplitCam à CamContacts", "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur CamContacts et la stream key dans les champs RTMP personnalisé. Réglez 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis l'espace performeuse. En ~10 secondes votre flux atteint l'audience de CamContacts."),
        ],
    },
    {
        "slug": "royalcams", "name": "RoyalCams",
        "title": "Diffuser sur RoyalCams avec SplitCam — encodeur",
        "desc": "Diffuser sur RoyalCams avec SplitCam : encodeur externe pour le site cam gratuit à tokens, scènes multicaméras, overlays et filtres, sans filigrane.",
        "kw": "diffuser sur royalcams, royalcams, royalcams broadcast, royalcams obs, royalcams external encoder, royalcams rtmp, royal cams",
        "h1html": 'Comment diffuser sur <span class="accent">RoyalCams</span> avec SplitCam',
        "h1short": "Diffuser sur RoyalCams",
        "card": "Configuration de l'encodeur externe pour le site cam à tokens RoyalCams.",
        "intro": "RoyalCams est un site cam gratuit à tokens — des salles publiques ouvertes financées par les tips, avec des shows privés par-dessus. Les paramètres de diffusion proposent un parcours standard <strong>External Encoder</strong> auquel <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte, pour streamer avec scènes multicaméras, overlays et filtres beauté au lieu d'une simple webcam plate.",
        "quick": "Pour diffuser sur RoyalCams avec SplitCam : installer SplitCam, composer la scène, dans le tableau de bord modèle ouvrir <em>broadcast settings → External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL + stream key depuis le tableau de bord.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte modèle RoyalCams et ouvrez la section <strong>broadcast settings / External Encoder</strong>. Elle affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. La vérification du compte modèle est obligatoire avant de diffuser.",
        "tips": [
            ("Les salles à tokens récompensent la qualité", "Les salles publiques de RoyalCams tournent aux tips — des overlays d'objectifs de tips et une scène soignée convertissent les curieux en tippeurs et en shows privés."),
            ("Convertissez en shows privés", "Utilisez une scène publique forte pour faire l'upsell vers les shows privés, là où se trouvent les vrais gains sur les sites cam à tokens."),
            ("L'encodeur externe débloque les scènes", "Passer par le RTMP de SplitCam plutôt que la cam du navigateur active mises en page multicaméras, overlays et filtres."),
            _T_ETH,
        ],
        "faq": [
            ("RoyalCams supporte-t-il les encodeurs externes comme SplitCam ?", "Oui — les paramètres de diffusion proposent un parcours standard External Encoder / RTMP. Copiez l'URL serveur et la stream key dans SplitCam une fois la vérification faite."),
            ("Où je récupère ma stream key RoyalCams ?", "Dans les paramètres broadcast / External Encoder de votre tableau de bord modèle — URL serveur et stream key apparaissent là. Collez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour RoyalCams ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test de SplitCam."),
            ("SplitCam est-il gratuit avec RoyalCams ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de RoyalCams est gratuite dans le tableau de bord."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte d'objectif de tips, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Récupérez votre URL et stream key RoyalCams", "Connectez-vous à votre compte modèle RoyalCams, ouvrez <strong>broadcast settings → External Encoder</strong>, et copiez l'<strong>URL serveur</strong> et la <strong>stream key</strong>."),
            ("Connectez SplitCam à RoyalCams", "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur RoyalCams et la stream key dans les champs RTMP personnalisé. Réglez 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis votre tableau de bord. En ~10 secondes votre flux atteint l'audience de RoyalCams."),
        ],
    },
    {
        "slug": "modelhub", "name": "Modelhub",
        "title": "Diffuser sur Modelhub avec SplitCam — encodeur",
        "desc": "Diffuser sur Modelhub Live avec SplitCam : encodeur externe pour la plateforme créateur de Pornhub, scènes multicaméras et overlays, sans filigrane.",
        "kw": "diffuser sur modelhub, modelhub, modelhub live, modelhub broadcast, modelhub obs, modelhub external encoder, modelhub rtmp",
        "h1html": 'Comment diffuser sur <span class="accent">Modelhub</span> avec SplitCam',
        "h1short": "Diffuser sur Modelhub",
        "card": "Configuration de l'encodeur externe pour Modelhub Live (Pornhub).",
        "intro": "Modelhub est la plateforme créateur de Pornhub — vente de vidéos, abonnements de fans et un produit <strong>live cam</strong> avec un trafic d'entonnoir massif venu du réseau Pornhub. Le tableau de bord modèle propose un parcours standard <strong>External Encoder</strong> auquel <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte, pour diffuser avec scènes multicaméras, overlays et filtres beauté.",
        "quick": "Pour diffuser sur Modelhub avec SplitCam : installer SplitCam, composer la scène, dans le tableau de bord modèle ouvrir <em>Live → broadcast / External Encoder</em>, copier l'URL serveur et la stream key, les coller dans SplitCam, Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li>"
                 "<li>Récupérer URL + stream key depuis le tableau de bord.</li>"
                 "<li>Coller dans SplitCam.</li>"
                 "<li>Appuyer sur Go Live.</li></ol>",
        "key_how": "Connectez-vous à votre compte modèle Modelhub et ouvrez les paramètres <strong>Live / broadcast / External Encoder</strong> dans le tableau de bord. La page affiche une <strong>URL serveur</strong> et une <strong>stream key</strong> liées à votre compte — copiez les deux dans les champs RTMP personnalisé de SplitCam. La vérification du compte modèle auprès du réseau est obligatoire avant de passer en live.",
        "tips": [
            ("Trafic d'entonnoir énorme", "Modelhub attire des spectateurs du réseau Pornhub — une scène SplitCam soignée convertit ce vaste public occasionnel en spectateurs live et abonnés payants."),
            ("Faites du cross-sell sur vos vidéos", "Utilisez des overlays pour orienter les spectateurs live vers vos vidéos et votre abonnement Modelhub — la plateforme est bâtie pour cet entonnoir."),
            ("L'encodeur externe débloque les scènes", "Passer par le RTMP de SplitCam plutôt que la cam basique active mises en page multicaméras, overlays et filtres."),
            _T_ETH,
        ],
        "faq": [
            ("Modelhub supporte-t-il les encodeurs externes comme SplitCam ?", "Oui — le tableau de bord modèle propose un parcours standard External Encoder / RTMP pour Modelhub Live. Copiez l'URL serveur et la stream key dans SplitCam une fois la vérification faite."),
            ("Où je récupère ma stream key Modelhub ?", "Dans les paramètres Live / broadcast / External Encoder du tableau de bord — URL serveur et stream key apparaissent là. Collez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Quel bitrate utiliser pour Modelhub ?", "Poussez du 1920×1080 à 30 fps, 3 500–6 000 Kbps avec un keyframe de 2 secondes. Lancez d'abord le speed test de SplitCam."),
            ("SplitCam est-il gratuit avec Modelhub ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps. L'option encodeur externe de Modelhub est gratuite dans le tableau de bord."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, texte, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Récupérez votre URL et stream key Modelhub", "Connectez-vous à votre compte modèle Modelhub, ouvrez <strong>Live → broadcast / External Encoder</strong>, et copiez l'<strong>URL serveur</strong> et la <strong>stream key</strong>."),
            ("Connectez SplitCam à Modelhub", "Dans SplitCam ouvrez <strong>Stream Settings</strong>, collez l'URL serveur Modelhub et la stream key dans les champs RTMP personnalisé. Réglez 3 500–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis le tableau de bord. En ~10 secondes votre flux atteint l'audience de Modelhub."),
        ],
    },
    {
        "slug": "xhamsterlive", "name": "xHamsterLive",
        "title": "Diffuser sur xHamsterLive avec SplitCam (RTMP/OBS)",
        "desc": "Diffusez sur xHamsterLive avec SplitCam gratuit en RTMP — scènes multicaméras, overlays et filtres. Trafic mainstream xHamster, sans filigrane.",
        "kw": "diffuser sur xhamsterlive, xhamsterlive obs, xhamsterlive rtmp, xhamster live broadcast, xhamsterlive modèle, x hamster live cam, xhamsterlive studio, xhamster live stream key",
        "h1html": 'Comment diffuser sur <span class="accent">xHamsterLive</span> avec SplitCam',
        "h1short": "Diffuser sur xHamsterLive",
        "card": "SplitCam gratuit → diffusion RTMP/OBS vers xHamsterLive.",
        "intro": "xHamsterLive est la branche live-cam de xHamster — même technologie de broadcaster que Stripchat, mais alimentée par le trafic mainstream de xHamster, l'un des plus grands viviers de spectateurs adultes. Les modèles diffusent via le <strong>Studio</strong> xHamsterLive, qui prend en charge à la fois le broadcaster webcam dans le navigateur et un <strong>encodeur externe en RTMP</strong>. Avec <strong style='color:var(--text)'>SplitCam</strong> gratuit, vous diffusez en encodeur externe pour des scènes multicaméras complètes, overlays et filtres — ou, si vous utilisez le broadcaster navigateur, pointez xHamsterLive vers SplitCam en <strong>caméra virtuelle</strong> pour le même résultat.",
        "quick": "Diffuser sur xHamsterLive avec SplitCam : installer SplitCam, composer la scène, copier l'URL serveur + stream key du Studio xHamsterLive, les coller dans les paramètres RTMP de SplitCam, appuyer sur Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li><li>Copier URL + stream key depuis Studio xHamsterLive → External Encoder.</li><li>Coller dans le RTMP personnalisé de SplitCam.</li><li>Cliquer Go Live.</li></ol>",
        "key_how": "Le Studio xHamsterLive affiche aux broadcasters un onglet <strong>External Encoder</strong> avec une URL serveur et une stream key. Collez les deux dans <strong>Stream Settings → Custom RTMP</strong> de SplitCam ; réglez 4 000–6 000 Kbps en 1920×1080, 30 fps, keyframe de 2 secondes. Cliquez <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis le Studio. Si vous préférez le broadcaster navigateur, ouvrez-le et choisissez <strong>SplitCam</strong> dans le menu déroulant caméra — votre scène composée remplace votre webcam brute.",
        "tips": [
            ("Trafic xHamster, moteur Stripchat", "Mêmes outils broadcaster que Stripchat (panneau Studio, menu de tips, Lovense) mais avec l'entonnoir mainstream de xHamster — un autre mix d'audience atterrit dans votre room."),
            ("Encodeur externe si possible", "Le RTMP depuis SplitCam offre un bitrate stable et des scènes multicaméras/overlays complètes ; le broadcaster navigateur convient, mais limite les options de composition."),
            ("Les menus de tips convertissent le mainstream", "Beaucoup de visiteurs xHamster découvrent le cam — un menu de tips clair à l'écran et une jauge d'objectif fixent les attentes et boostent la conversion par session."),
            _T_TEST,
        ],
        "faq": [
            ("xHamsterLive c'est pareil que Stripchat ?", "Il tourne sur le moteur broadcaster de Stripchat, mais la marque et la source de trafic diffèrent — xHamster y dirige son audience mainstream, donc le profil des spectateurs n'est pas le même qu'une inscription Stripchat seule."),
            ("Où récupérer la stream key xHamsterLive ?", "Dans le Studio xHamsterLive, ouvrez le panneau <em>Broadcast</em> ou <em>External Encoder</em> — vous y verrez une URL serveur et une stream key. Collez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Broadcaster navigateur ou RTMP ?", "L'encodeur externe (RTMP) est préférable pour les modèles sérieux — bitrate stable et scènes SplitCam complètes. Le broadcaster navigateur fonctionne aussi : choisissez SplitCam comme webcam."),
            ("SplitCam est-il gratuit avec xHamsterLive ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, un menu de tips, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — appliqués en direct."),
            ("Récupérez l'URL + clé du Studio xHamsterLive", "Connectez-vous à xHamsterLive, ouvrez le Studio, basculez sur <strong>External Encoder</strong>, et copiez l'<strong>URL serveur</strong> et votre <strong>stream key</strong>."),
            ("Connectez SplitCam à xHamsterLive", "Dans SplitCam → <strong>Stream Settings → Custom RTMP</strong>, collez l'URL et la clé. Réglez 4 000–6 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis le Studio xHamsterLive. En ~10 secondes votre flux atterrit dans la liste publique."),
        ],
    },
    {
        "slug": "premium-chat", "name": "Premium.Chat",
        "title": "Utiliser SplitCam sur Premium.Chat — appels payants",
        "desc": "SplitCam gratuit en caméra virtuelle sur Premium.Chat — appels vidéo payants à la minute, scènes multicaméras, overlays et filtres. Sans filigrane.",
        "kw": "utiliser splitcam sur premium chat, premium chat appel vidéo, premium chat caméra virtuelle, premium.chat paiement à la minute, premium chat modèle, premium chat conseiller, premium chat live, plateforme appel vidéo splitcam",
        "h1html": 'Comment utiliser SplitCam sur <span class="accent">Premium.Chat</span>',
        "h1short": "Premium.Chat avec SplitCam",
        "card": "Utilisez SplitCam comme caméra virtuelle pour les appels payants Premium.Chat.",
        "intro": "Premium.Chat est une plateforme payante à la minute : vous fixez votre tarif par minute pour le chat, l'audio ou les <strong>appels vidéo</strong>, vous partagez votre lien personnel, et les clients payent pour vous parler. Les appels tournent dans le navigateur, ce qui veut dire que <strong style='color:var(--text)'>SplitCam</strong> gratuit se branche directement en <strong>caméra virtuelle</strong> — scènes multicaméras, overlays, filtres d'éclairage et fond IA atteignent l'appelant sans changer le fonctionnement de Premium.Chat.",
        "quick": "Utiliser SplitCam sur Premium.Chat : installer SplitCam, composer une scène propre pour les appels vidéo, accepter un appel entrant Premium.Chat, et dans le sélecteur de caméra de l'appel choisir <em>SplitCam</em>."
                 "<ol><li>Installer SplitCam.</li><li>Mettre en place votre scène (bon éclairage, overlay optionnel).</li><li>Fixer votre tarif à la minute sur Premium.Chat.</li><li>Accepter l'appel vidéo entrant.</li><li>Sélectionner SplitCam comme caméra.</li></ol>",
        "key_how": "Les appels Premium.Chat se passent dans le navigateur. SplitCam installe une webcam virtuelle appelée <strong>\"SplitCam Video Driver\"</strong> — quand un appel démarre, cliquez sur le menu icône-caméra dans la fenêtre d'appel Premium.Chat et basculez de votre webcam intégrée vers <strong>SplitCam</strong>. Votre scène composée (vraie caméra + overlays + filtres) devient ce que voit l'appelant.",
        "tips": [
            ("Premium.Chat c'est à la minute, pas du streaming", "Contrairement aux rooms à tips façon Chaturbate, vous êtes payé à la minute. Un éclairage doux, un son clair et un fond IA évoquent davantage une consultation premium qu'un cam public."),
            ("Promouvez votre lien, pas un profil", "Premium.Chat vous donne un lien personnel à glisser sur les réseaux sociaux, dans la bio OnlyFans ou un Linktree — c'est ainsi que les appelants vous trouvent."),
            ("Overlays seulement si utiles", "Sur un appel 1-à-1, les overlays lourds distraient. Utilisez SplitCam pour la qualité caméra, l'éclairage et le fond — gardez l'écran centré sur vous."),
            _T_TEST,
        ],
        "faq": [
            ("Comment SplitCam se connecte-t-il à Premium.Chat ?", "En caméra virtuelle. Les appels Premium.Chat tournent dans le navigateur ; choisissez SplitCam dans le sélecteur de caméra de l'appel — pas de stream key, pas de RTMP."),
            ("Premium.Chat prend-il en charge OBS ?", "Premium.Chat est basé navigateur, donc OBS se branche de la même façon que SplitCam — en caméra virtuelle. SplitCam est l'option plus légère, gratuite et sans filigrane."),
            ("Puis-je utiliser une deuxième caméra ou un overlay sur Premium.Chat ?", "Oui — composez la scène dans SplitCam (deuxième caméra, overlays, filtres) et Premium.Chat voit une seule webcam. À utiliser avec parcimonie en appel 1-à-1."),
            ("SplitCam est-il gratuit ?", "Oui — gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Il installe une caméra virtuelle utilisable par le navigateur."),
            ("Préparez votre scène pour les appels", "Ouvrez SplitCam, ajoutez votre webcam, soignez l'éclairage, ajoutez éventuellement un fond IA ou un overlay discret. Gardez un cadrage propre — c'est un appel payant, pas une scène publique."),
            ("Fixez votre tarif sur Premium.Chat", "Connectez-vous à Premium.Chat, fixez votre tarif à la minute pour les appels vidéo et copiez votre lien personnel. Partagez-le sur les réseaux ou dans vos bios."),
            ("Acceptez l'appel vidéo entrant", "Quand un client paie pour du temps, la demande d'appel arrive. Acceptez-la dans le tableau de bord Premium.Chat."),
            ("Sélectionnez SplitCam comme caméra", "Dans le menu icône-caméra de la fenêtre d'appel, basculez de votre webcam intégrée vers <strong>SplitCam</strong>. Votre scène composée atteint maintenant l'appelant."),
        ],
    },
    {
        "slug": "arousr", "name": "Arousr",
        "title": "Utiliser SplitCam sur Arousr — sexting et vidéo",
        "desc": "SplitCam gratuit en caméra virtuelle sur Arousr — scènes multicaméras, overlays et filtres pour sexting, audio et vidéo payants. Sans filigrane.",
        "kw": "utiliser splitcam sur arousr, arousr vidéo chat, arousr caméra virtuelle, arousr cam girl, arousr modèle, plateforme sexting splitcam, arousr live, arousr diffusion",
        "h1html": 'Comment utiliser SplitCam sur <span class="accent">Arousr</span>',
        "h1short": "Arousr avec SplitCam",
        "card": "Utilisez SplitCam comme caméra virtuelle pour le vidéo-chat Arousr.",
        "intro": "Arousr est une plateforme payante de <strong>sexting + appels audio + vidéo-chat</strong> — les clients achètent des crédits pour vous écrire, vous parler ou vous voir en vidéo, et vous êtes payé par session. La partie vidéo tourne dans le navigateur (ou dans l'application mobile Arousr sur téléphone), ce qui signifie que <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte en <strong>caméra virtuelle</strong> sur desktop : scènes multicaméras, overlays, filtres d'éclairage et fond IA passent directement chez le client.",
        "quick": "Utiliser SplitCam sur Arousr : installer SplitCam, composer la scène, accepter une demande vidéo Arousr entrante, et dans le sélecteur de caméra choisir <em>SplitCam</em>."
                 "<ol><li>Installer SplitCam.</li><li>Préparer scène + éclairage.</li><li>Fixer vos tarifs sexting/vidéo sur Arousr.</li><li>Accepter la demande vidéo entrante.</li><li>Sélectionner SplitCam dans le menu déroulant caméra.</li></ol>",
        "key_how": "La vidéo web d'Arousr tourne dans le navigateur. SplitCam installe une webcam virtuelle appelée <strong>\"SplitCam Video Driver\"</strong> — quand une session vidéo démarre dans le tableau de bord Arousr, basculez la caméra dans la fenêtre de session vers <strong>SplitCam</strong>. La scène composée (caméra + overlays + filtres) devient ce que voit le client. Sur l'application mobile Arousr, les caméras virtuelles ne sont pas disponibles — utilisez la vraie caméra du téléphone là-bas et gardez SplitCam pour les sessions desktop.",
        "tips": [
            ("Les sessions sont payées au temps", "Les clients achètent des crédits à la minute (ou par message pour le texte). Une vidéo soignée — bon éclairage, fond IA, filtre beauté — se rentabilise par des sessions plus longues."),
            ("Sexting d'abord, vidéo en upsell", "L'essentiel des revenus Arousr passe par le texte. Un court aperçu vidéo pendant un sext chat fait basculer le client vers une session vidéo complète — c'est là que le tarif à la minute prend le relais."),
            ("App mobile ≠ desktop", "Les caméras virtuelles marchent dans la vidéo navigateur sur desktop. L'application mobile Arousr utilise directement la caméra du téléphone — même workflow, autre outil."),
            _T_TEST,
        ],
        "faq": [
            ("Comment SplitCam se connecte-t-il à Arousr ?", "En caméra virtuelle. Le vidéo-chat Arousr tourne dans le navigateur sur desktop — choisissez SplitCam dans le sélecteur de caméra. Aucune stream key requise."),
            ("Arousr prend-il en charge OBS ?", "Arousr est basé navigateur, donc OBS se branche de la même façon que SplitCam — en caméra virtuelle. SplitCam est l'option gratuite sans filigrane."),
            ("Puis-je utiliser des overlays sur une session sexting + vidéo ?", "Oui — composez la scène dans SplitCam (éclairage, overlay, deuxième caméra) et Arousr voit une seule webcam. Restez léger sur les overlays en 1-à-1."),
            ("SplitCam est-il gratuit avec Arousr ?", "Oui — gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Il installe une caméra virtuelle sélectionnable par le navigateur."),
            ("Composez votre scène", "Ouvrez SplitCam, ajoutez votre webcam, peaufinez l'éclairage, ajoutez un fond IA ou un filtre beauté en option. Restez dans une ambiance intime — c'est une session payante en 1-à-1, pas une scène publique."),
            ("Fixez vos tarifs sur Arousr", "Connectez-vous à Arousr, fixez votre tarif par message et votre tarif vidéo à la minute, et vérifiez que votre profil est validé pour pouvoir recevoir des demandes."),
            ("Acceptez la demande vidéo entrante", "Quand un client lance une session vidéo depuis un sext chat ou directement, acceptez-la dans le tableau de bord Arousr."),
            ("Sélectionnez SplitCam comme caméra", "Dans le menu déroulant caméra de la fenêtre de session, basculez de votre webcam intégrée vers <strong>SplitCam</strong>. Votre scène composée atteint maintenant le client."),
        ],
    },
    {
        "slug": "cams-com", "name": "Cams.com",
        "title": "Diffuser sur Cams.com avec SplitCam (RTMP/OBS)",
        "desc": "Diffusez sur Cams.com avec SplitCam gratuit en RTMP — scènes multicaméras, overlays et filtres. Touchez la base de membres payants d'AFF. Sans filigrane.",
        "kw": "diffuser sur cams.com, cams.com obs, cams.com rtmp, cams.com modèle, cams.com broadcaster, cams.com stream key, adult friend finder cams, cams.com live, cams com inscription modèle",
        "h1html": 'Comment diffuser sur <span class="accent">Cams.com</span> avec SplitCam',
        "h1short": "Diffuser sur Cams.com",
        "card": "SplitCam gratuit → flux RTMP vers le réseau Cams.com / AFF.",
        "intro": "Cams.com est la branche cam du réseau AdultFriendFinder — l'un des plus anciens écosystèmes dating + cam en ligne, avec une importante base de <strong>membres déjà payants</strong> qui circulent depuis AFF, AmateurMatch et d'autres sites FriendFinder. Les modèles diffusent depuis le <strong>Model Center</strong> de Cams.com, qui prend en charge le broadcaster dans le navigateur comme un <strong>encodeur externe en RTMP</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuit diffuse en RTMP pour des scènes multicaméras complètes, overlays et filtres — ou, dans le broadcaster navigateur, s'enregistre comme <strong>caméra virtuelle</strong> pour le même résultat.",
        "quick": "Diffuser sur Cams.com : installer SplitCam, composer la scène, récupérer l'URL serveur RTMP + stream key Cams.com depuis le Model Center, les coller dans SplitCam, cliquer Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li><li>Copier URL serveur + clé depuis Cams.com Model Center → External Encoder.</li><li>Coller dans le RTMP personnalisé de SplitCam.</li><li>Cliquer Go Live.</li></ol>",
        "key_how": "Le Model Center de Cams.com propose un onglet <strong>External Encoder / OBS</strong> avec une URL serveur et une stream key. Collez les deux dans <strong>Stream Settings → Custom RTMP</strong> de SplitCam ; réglez 3 500–5 000 Kbps en 1920×1080, 30 fps, keyframe de 2 secondes. Cliquez <strong>Go Live</strong> dans SplitCam, puis lancez votre show depuis le Model Center. Si vous préférez le broadcaster dans le navigateur, choisissez plutôt <strong>SplitCam</strong> dans le menu déroulant caméra.",
        "tips": [
            ("Le cross-traffic AFF = membres payants", "Cams.com attire des spectateurs depuis des comptes AdultFriendFinder qui ont déjà un moyen de paiement enregistré — pas la même chose qu'une audience d'inscription récente. La conversion en privé et les tips tendent à être plus élevés."),
            ("L'encodeur externe l'emporte sur le navigateur", "Le RTMP depuis SplitCam offre un bitrate propre et permet de composer des scènes multicaméras avec overlays ; le broadcaster navigateur fonctionne mais bride la production."),
            ("Servez-vous des outils de privé", "Cams.com mise sur les sessions privées/exclusives. Un menu de tips et un chemin clair vers le privé (en overlay) augmentent nettement le revenu par spectateur."),
            _T_TEST,
        ],
        "faq": [
            ("Cams.com c'est pareil qu'AdultFriendFinder ?", "Même réseau parent. Cams.com est la marque de diffusion cam ; les spectateurs peuvent arriver via AFF, AmateurMatch et d'autres sites FriendFinder, ce qui pèse lourd dans son trafic."),
            ("Où récupérer la stream key Cams.com ?", "Dans le Model Center de Cams.com, ouvrez l'onglet <em>External Encoder</em> ou <em>OBS</em> — vous y verrez une URL serveur et une stream key. Collez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Broadcaster navigateur ou RTMP ?", "Le RTMP (encodeur externe) est préférable — bitrate stable, scènes SplitCam complètes. Le broadcaster navigateur sert de plan B : choisissez SplitCam comme webcam."),
            ("SplitCam est-il gratuit avec Cams.com ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, un menu de tips, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — appliqués en direct."),
            ("Récupérez votre URL + stream key Cams.com", "Connectez-vous au Model Center de Cams.com, ouvrez l'onglet <strong>External Encoder / OBS</strong>, et copiez l'<strong>URL serveur</strong> et la <strong>stream key</strong>."),
            ("Connectez SplitCam à Cams.com", "Dans SplitCam → <strong>Stream Settings → Custom RTMP</strong>, collez l'URL et la clé. Réglez 3 500–5 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne depuis le Model Center. Votre flux atterrit dans le réseau Cams.com / AFF en ~10 secondes."),
        ],
    },
    {
        "slug": "stripcamfun", "name": "StripCamFun",
        "title": "Diffuser sur StripCamFun avec SplitCam (RTMP/OBS)",
        "desc": "Diffusez sur StripCamFun avec SplitCam gratuit en RTMP — scènes multicaméras, overlays et filtres pour une audience cam indé. Sans filigrane.",
        "kw": "diffuser sur stripcamfun, stripcamfun obs, stripcamfun rtmp, stripcamfun modèle, stripcamfun broadcast, strip cam fun inscription modèle, stripcamfun stream key, site cam indé obs",
        "h1html": 'Comment diffuser sur <span class="accent">StripCamFun</span> avec SplitCam',
        "h1short": "Diffuser sur StripCamFun",
        "card": "SplitCam gratuit → diffusion RTMP/OBS vers StripCamFun.",
        "intro": "StripCamFun est un site live-cam indépendant — plus petit que les géants façon Chaturbate, mais avec une vraie audience moins saturée et nettement moins de concurrence broadcaster par niche. Les modèles diffusent depuis le panneau modèle de StripCamFun, qui propose une option <strong>encodeur externe / RTMP</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuit se connecte en RTMP pour des scènes multicaméras complètes, overlays et filtres — et là où un broadcaster navigateur est proposé, SplitCam s'enregistre aussi comme <strong>caméra virtuelle</strong>.",
        "quick": "Diffuser sur StripCamFun : installer SplitCam, composer la scène, copier l'URL serveur + stream key StripCamFun, les coller dans les paramètres RTMP de SplitCam, appuyer sur Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li><li>Copier URL + stream key depuis panneau modèle StripCamFun → External Encoder.</li><li>Coller dans le RTMP personnalisé de SplitCam.</li><li>Cliquer Go Live.</li></ol>",
        "key_how": "Ouvrez le tableau de bord modèle StripCamFun et la section <strong>External Encoder / OBS</strong>. Copiez l'URL serveur et votre stream key dans <strong>Stream Settings → Custom RTMP</strong> de SplitCam ; réglez 3 500–5 000 Kbps en 1920×1080, 30 fps, keyframe de 2 secondes. Cliquez <strong>Go Live</strong> dans SplitCam, puis passez vous-même en ligne depuis le tableau de bord.",
        "tips": [
            ("Petit vivier, visibilité plus facile", "Sur un site Tier 1 vous êtes un parmi des milliers en ligne ; sur StripCamFun la liste broadcaster est courte — une scène SplitCam soignée ressort plus vite en page d'accueil."),
            ("Cross-broadcast pour la portée", "Les sites cam indé se marient bien avec le multi-streaming. Utilisez SplitCam pour diffuser simultanément sur StripCamFun et un site plus grand pour capter les tippeurs des deux viviers."),
            ("Misez sur le tagging de niche", "Les audiences indé cherchent par niche plus que par notoriété. Des tags précis + un overlay de scène qui nomme la niche attirent les spectateurs depuis la liste."),
            _T_TEST,
        ],
        "faq": [
            ("Où récupérer la stream key StripCamFun ?", "Dans le tableau de bord modèle, ouvrez l'onglet <em>External Encoder / OBS</em> — vous y verrez une URL serveur et une stream key. Collez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Diffuser sur StripCamFun est-il sûr ?", "Comme sur tout site cam indé, lisez le contrat modèle et les conditions de paiement avant de passer en live. Utilisez un vrai email et vérifiez votre méthode de paiement d'abord."),
            ("Puis-je multi-streamer vers StripCamFun et un autre site cam ?", "Oui — SplitCam peut pousser vers plusieurs endpoints RTMP personnalisés en même temps. Vérifiez d'abord les règles d'exclusivité de chaque site."),
            ("SplitCam est-il gratuit avec StripCamFun ?", "Oui — gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, un menu de tips, une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — appliqués en direct."),
            ("Récupérez votre URL + stream key StripCamFun", "Connectez-vous au tableau de bord modèle StripCamFun, ouvrez <strong>External Encoder / OBS</strong>, et copiez l'<strong>URL serveur</strong> et la <strong>stream key</strong>."),
            ("Connectez SplitCam à StripCamFun", "Dans SplitCam → <strong>Stream Settings → Custom RTMP</strong>, collez l'URL et la clé. Réglez 3 500–5 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne dans le tableau de bord StripCamFun. Votre flux atterrit sur la liste publique en ~10 secondes."),
        ],
    },
    {
        "slug": "mym-fans", "name": "MYM.fans",
        "title": "Passer en live sur MYM.fans avec SplitCam — caméra virtuelle",
        "desc": "Passer en live sur MYM.fans (le OnlyFans français) avec SplitCam gratuit comme caméra virtuelle — scènes multicaméras, overlays et filtres. Sans filigrane.",
        "kw": "passer en live sur mym, mym.fans live, mym fans caméra virtuelle, créateur mym, mym france, mym live stream, mym obs, mym fans diffusion, influenceur mym",
        "h1html": 'Comment passer en live sur <span class="accent">MYM.fans</span> avec SplitCam',
        "h1short": "Live sur MYM.fans",
        "card": "SplitCam en caméra virtuelle pour les lives MYM.fans.",
        "intro": "MYM.fans est la première plateforme française de créateurs par abonnement — la réponse hexagonale à OnlyFans, avec abonnements, contenu payant à l'unité, cagnottes (tips) et une fonctionnalité <strong>live</strong> intégrée pour les fans. Son broadcaster tourne dans le navigateur, donc brancher <strong style='color:var(--text)'>SplitCam</strong> gratuit en <strong>caméra virtuelle</strong> ajoute scènes multicaméras, overlays et filtres par-dessus la webcam standard. Si le tableau de bord créateur expose une option d'encodeur externe, SplitCam peut aussi se connecter en RTMP.",
        "quick": "Live sur MYM.fans avec SplitCam : installer SplitCam, composer la scène, lancer un live sur MYM, et dans le sélecteur de caméra du broadcaster choisir <em>SplitCam</em> — puis passer en direct."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li><li>Lancer un live sur MYM.fans.</li><li>Sélectionner SplitCam dans la liste des caméras.</li><li>Go Live.</li></ol>",
        "key_how": "Le live MYM.fans tourne dans le navigateur. Composez la scène dans SplitCam — elle s'enregistre comme une webcam appelée <strong>« SplitCam Video Driver »</strong> — puis ouvrez le broadcaster live de MYM et sélectionnez <strong>SplitCam</strong> dans la liste des caméras. Si une option <strong>clé de stream / encodeur externe</strong> est proposée dans votre tableau de bord créateur, collez-la dans les champs RTMP personnalisé de SplitCam.",
        "tips": [
            ("La plus grosse plateforme créateurs FR", "MYM est le n°1 des plateformes de fans en France, avec une audience française/européenne habituée à payer en euros. Une scène SplitCam soignée + des overlays en français convertissent mieux qu'une webcam brute."),
            ("La caméra virtuelle marche sans clé de stream", "Un live navigateur récupère quand même toute votre scène SplitCam — deuxième caméra, overlays, filtres beauté ou fond IA — simplement en sélectionnant SplitCam comme webcam."),
            ("Cross-sell du contenu payant pendant le live", "MYM est construit autour du payant. Des overlays à l'écran qui promeuvent l'abonnement ou un message payant à débloquer transforment les spectateurs du live en abonnés payants."),
            _T_TEST,
        ],
        "faq": [
            ("Comment SplitCam se connecte-t-il à MYM.fans ?", "Le live MYM passe par le navigateur, donc SplitCam se connecte en caméra virtuelle — choisissez SplitCam dans le sélecteur de caméra. Pas besoin de clé de stream."),
            ("Puis-je utiliser des overlays et plusieurs caméras sur MYM ?", "Oui — composez la scène dans SplitCam (deuxième caméra, overlays, fond IA) ; MYM voit la scène finie comme une seule webcam."),
            ("MYM.fans gère-t-il OBS ou les encodeurs externes ?", "Le live est principalement basé navigateur/webcam. Si votre tableau de bord propose une option clé de stream, collez-la dans les champs RTMP personnalisé de SplitCam ; sinon, utilisez la caméra virtuelle."),
            ("SplitCam est-il gratuit avec MYM.fans ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Il installe une caméra virtuelle que le navigateur sait sélectionner."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, du texte (en français si votre audience est FR), une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Lancez un live sur MYM.fans", "Connectez-vous à votre compte créateur MYM et ouvrez le broadcaster live pour démarrer une diffusion pour vos abonnés."),
            ("Sélectionnez SplitCam comme caméra", "Dans la liste des caméras de MYM, choisissez <strong>SplitCam</strong> au lieu de votre webcam brute — votre scène composée remplace la caméra plate. (Ou collez une clé de stream dans les champs RTMP personnalisé de SplitCam si l'option existe.)"),
            ("Go Live", "Lancez la diffusion — votre scène SplitCam, ses overlays et filtres arrivent chez vos abonnés MYM."),
        ],
    },
    {
        "slug": "fc2-live", "name": "FC2 Live",
        "title": "Diffuser sur FC2 Live avec SplitCam (RTMP/OBS)",
        "desc": "Diffuser sur FC2 Live (1er site cam du Japon) avec SplitCam gratuit en RTMP — scènes multicaméras, overlays et filtres. Sans filigrane.",
        "kw": "diffuser sur fc2 live, fc2 live obs, fc2 live rtmp, fc2 live broadcast, fc2 live配信, fc2 live stream key, fc2 live modèle, fc2 live japon, fc2 ライブ",
        "h1html": 'Comment diffuser sur <span class="accent">FC2 Live</span> avec SplitCam',
        "h1short": "Diffuser sur FC2 Live",
        "card": "SplitCam gratuit → diffusion RTMP/OBS vers FC2 Live.",
        "intro": "FC2 Live est la plus grosse plateforme de live-streaming du Japon — une audience massive, une section adulte dédiée et un flux de shows payants séparé qui en font l'un des marchés cam les plus rentables d'Asie. Les modèles diffusent depuis le panneau broadcaster FC2, qui prend en charge à la fois le broadcaster navigateur et un <strong>encodeur externe en RTMP</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuit diffuse en RTMP pour des scènes multicaméras complètes, overlays et filtres.",
        "quick": "Diffuser sur FC2 Live avec SplitCam : installer SplitCam, composer la scène, copier l'URL serveur + stream key du broadcaster FC2, les coller dans les paramètres RTMP de SplitCam, appuyer sur Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li><li>Copier URL + stream key depuis le panneau broadcaster FC2.</li><li>Coller dans le RTMP personnalisé de SplitCam.</li><li>Cliquer Go Live.</li></ol>",
        "key_how": "Ouvrez le panneau broadcaster FC2 Live et basculez sur <strong>External Encoder / RTMP</strong>. Copiez l'URL serveur et votre stream key dans <strong>Stream Settings → Custom RTMP</strong> de SplitCam ; réglez 3 500–5 000 Kbps en 1920×1080, 30 fps, keyframe de 2 secondes. Cliquez <strong>Go Live</strong> dans SplitCam, puis démarrez votre show depuis le tableau de bord FC2.",
        "tips": [
            ("Énorme audience japonaise", "FC2 est Tier 1 au Japon — les spectateurs sont locaux, habitués à payer en yens, et plutôt portés sur les shows payants longs. Des overlays en japonais (menu de tips en 円 / JPY) font nettement grimper la conversion."),
            ("La section adulte est séparée", "FC2 a à la fois des lives grand public et adultes. Réglez correctement la catégorie de la salle avant de passer en direct — les shows adultes ne se découvrent pas depuis la section générale."),
            ("Encodeur externe pour un bitrate stable", "L'audience japonaise, très mobile, est sensible aux pertes de trames. Le RTMP depuis SplitCam à 4 Mbps stables fait mieux que le broadcaster navigateur côté fiabilité."),
            _T_TEST,
        ],
        "faq": [
            ("Où récupérer la stream key FC2 Live ?", "Dans le panneau broadcaster FC2 Live, basculez sur <em>External Encoder</em> ou <em>OBS</em> — vous y verrez une URL serveur et une stream key. Collez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Broadcaster navigateur ou RTMP ?", "Le RTMP (encodeur externe) est préférable — bitrate stable, scènes SplitCam complètes. Le broadcaster navigateur sert de plan B : choisissez SplitCam comme webcam."),
            ("Faut-il un compte japonais pour diffuser sur FC2 ?", "Un compte FC2 est requis, et le streaming adulte demande des étapes supplémentaires de vérification d'âge côté modèle. Suivez le parcours d'inscription FC2."),
            ("SplitCam est-il gratuit avec FC2 Live ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays, un menu de tips en 円 (JPY), une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — appliqués en direct."),
            ("Récupérez votre URL + stream key FC2 Live", "Connectez-vous à FC2, ouvrez le panneau broadcaster Live, basculez sur <strong>External Encoder</strong>, et copiez l'<strong>URL serveur</strong> et votre <strong>stream key</strong>."),
            ("Connectez SplitCam à FC2 Live", "Dans SplitCam → <strong>Stream Settings → Custom RTMP</strong>, collez l'URL et la clé. Réglez 3 500–5 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis démarrez le show depuis le tableau de bord FC2. Votre flux atterrit sur la liste publique en ~10 secondes."),
        ],
    },
    {
        "slug": "boosty", "name": "Boosty",
        "title": "Passer en live sur Boosty avec SplitCam — caméra virtuelle",
        "desc": "Passer en live sur Boosty (plateforme créateurs RU) avec SplitCam gratuit en caméra virtuelle — scènes multicaméras, overlays et filtres. Sans filigrane.",
        "kw": "passer en live sur boosty, boosty live, boosty stream, boosty caméra virtuelle, créateur boosty, бусти прямой эфир, boosty obs, boosty live payant, boosty abonné",
        "h1html": 'Comment passer en live sur <span class="accent">Boosty</span> avec SplitCam',
        "h1short": "Live sur Boosty",
        "card": "SplitCam en caméra virtuelle pour les lives Boosty.",
        "intro": "Boosty est la plus grosse plateforme russe de monétisation pour créateurs — un service à la Patreon avec abonnements, posts payants, cagnottes (tips) et une fonctionnalité <strong>direct live</strong>, dont l'audience inclut des créateurs adultes aux côtés du grand public. Son live tourne dans le navigateur, donc brancher <strong style='color:var(--text)'>SplitCam</strong> gratuit en <strong>caméra virtuelle</strong> ajoute des scènes multicaméras, overlays et filtres qu'une webcam brute ne donnerait pas aux abonnés.",
        "quick": "Live sur Boosty avec SplitCam : installer SplitCam, composer la scène, lancer un live sur Boosty, et sélectionner <em>SplitCam</em> dans la liste des caméras du broadcaster — puis passer en direct."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li><li>Lancer un live sur Boosty.</li><li>Sélectionner SplitCam dans la liste des caméras.</li><li>Go Live.</li></ol>",
        "key_how": "Le live Boosty tourne dans le navigateur. Composez la scène dans SplitCam — elle s'enregistre comme une webcam appelée <strong>« SplitCam Video Driver »</strong> — puis ouvrez le broadcaster live Boosty et choisissez <strong>SplitCam</strong> dans la liste des caméras au lieu de votre webcam brute.",
        "tips": [
            ("La plus grosse plateforme créateurs de Russie", "Boosty a remplacé Patreon pour beaucoup de créateurs RU après les sanctions ; l'audience est fidèle et habituée à payer en roubles. Une scène SplitCam soignée avec des overlays en russe convertit bien."),
            ("Lives par palier d'abonnement", "Boosty permet de verrouiller un live par palier d'abonné. SplitCam fonctionne avec tous les paliers — l'encodeur se moque du palier du spectateur, vous diffusez une fois et Boosty gère l'accès."),
            ("Overlay tips et contenu payant à débloquer", "Boosty prend en charge les posts payants à débloquer et les tips. Un overlay à l'écran qui détaille les avantages du palier fait grimper la conversion pendant les lives."),
            _T_TEST,
        ],
        "faq": [
            ("Comment SplitCam se connecte-t-il à Boosty ?", "Le live Boosty passe par le navigateur, donc SplitCam se connecte en caméra virtuelle — choisissez SplitCam dans le sélecteur de caméra. Pas besoin de clé de stream."),
            ("Puis-je utiliser des overlays sur un live Boosty ?", "Oui — composez la scène dans SplitCam (overlays, deuxième caméra, fond IA) ; Boosty voit une seule webcam. Les abonnés récupèrent la scène composée complète."),
            ("Boosty gère-t-il OBS ou les encodeurs externes ?", "Le live Boosty est principalement basé navigateur. Si une option clé de stream apparaît dans votre tableau de bord créateur, collez-la dans les champs RTMP personnalisé de SplitCam ; sinon, utilisez la caméra virtuelle."),
            ("SplitCam est-il gratuit avec Boosty ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Il installe une caméra virtuelle que le navigateur sait sélectionner."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays (en russe pour votre audience), une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Lancez un live sur Boosty", "Connectez-vous à votre compte créateur Boosty et ouvrez le broadcaster live. Réglez le verrouillage par palier si vous voulez le live derrière un niveau payant."),
            ("Sélectionnez SplitCam comme caméra", "Dans la liste des caméras de Boosty, choisissez <strong>SplitCam</strong> au lieu de votre webcam brute — votre scène composée remplace la caméra plate."),
            ("Go Live", "Lancez la diffusion — votre scène SplitCam, ses overlays et filtres arrivent chez vos abonnés Boosty."),
        ],
    },
    {
        "slug": "amateurcommunity", "name": "AmateurCommunity",
        "title": "Diffuser sur AmateurCommunity avec SplitCam (RTMP)",
        "desc": "Diffuser sur AmateurCommunity (1er site cam amateur d'Allemagne) avec SplitCam gratuit en RTMP — scènes multicaméras, overlays et filtres. Sans filigrane.",
        "kw": "diffuser sur amateurcommunity, amateurcommunity obs, amateurcommunity rtmp, amateur community deutschland, amateurcommunity modèle, ac community broadcast, amateurcommunity live, amateur cam deutschland",
        "h1html": 'Comment diffuser sur <span class="accent">AmateurCommunity</span> avec SplitCam',
        "h1short": "Diffuser sur AmateurCommunity",
        "card": "SplitCam gratuit → diffusion RTMP vers AmateurCommunity (DE).",
        "intro": "AmateurCommunity est le plus gros site cam et community amateur d'Allemagne — actif depuis le début des années 2000, avec une audience germanophone profondément fidèle et habituée à payer pour du contenu et des lives. Les modèles diffusent depuis le panneau modèle AC, qui prend en charge un <strong>encodeur externe en RTMP</strong> ainsi que le broadcaster navigateur. <strong style='color:var(--text)'>SplitCam</strong> gratuit diffuse en RTMP pour des scènes multicaméras complètes, overlays et filtres — des overlays en allemand parlent directement à l'audience locale.",
        "quick": "Diffuser sur AmateurCommunity : installer SplitCam, composer la scène, copier l'URL serveur + stream key AC depuis le panneau modèle, les coller dans les paramètres RTMP de SplitCam, appuyer sur Go Live."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li><li>Copier URL + stream key depuis panneau modèle AC.</li><li>Coller dans le RTMP personnalisé de SplitCam.</li><li>Cliquer Go Live.</li></ol>",
        "key_how": "Ouvrez le panneau modèle AmateurCommunity et l'onglet <strong>External Encoder / OBS</strong>. Copiez l'URL serveur et votre stream key dans <strong>Stream Settings → Custom RTMP</strong> de SplitCam ; réglez 3 500–5 000 Kbps en 1920×1080, 30 fps, keyframe de 2 secondes. Cliquez <strong>Go Live</strong> dans SplitCam, puis passez vous-même en ligne depuis le panneau.",
        "tips": [
            ("Audience germanophone qui paie en euros", "L'audience d'AmateurCommunity est massivement DACH (DE/AT/CH) et paie en euros — overlays, menu de tips et chat en allemand convertissent nettement mieux que l'anglais."),
            ("Combo PPV premium + live", "AC permet de vendre du PPV à côté du live. Un live qui teasе le PPV (avec un overlay à l'écran) fait grimper les ventes PPV pendant et après la diffusion."),
            ("Encodeur externe pour une qualité stable", "L'audience d'AC s'attend à une vraie production ; le RTMP à 4 Mbps stables depuis SplitCam bat le bitrate variable du broadcaster navigateur."),
            _T_TEST,
        ],
        "faq": [
            ("Où récupérer la stream key AmateurCommunity ?", "Dans le panneau modèle AC, ouvrez l'onglet <em>External Encoder</em> ou <em>OBS</em> — vous y verrez une URL serveur et une stream key. Collez les deux dans les champs RTMP personnalisé de SplitCam."),
            ("Broadcaster navigateur ou RTMP ?", "Le RTMP (encodeur externe) est préférable pour les modèles sérieux — bitrate stable, scènes SplitCam complètes. Le broadcaster navigateur sert de plan B : choisissez SplitCam comme webcam."),
            ("Faut-il être en Allemagne pour diffuser sur AC ?", "Non, mais l'audience est germanophone. Les modèles de partout peuvent s'inscrire — passer la vérification modèle et les formulaires fiscaux est l'étape principale."),
            ("SplitCam est-il gratuit avec AmateurCommunity ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays (en allemand — « Trinkgeld » / « PPV freischalten »), une deuxième caméra ou votre téléphone, filtres beauté ou fond IA — appliqués en direct."),
            ("Récupérez votre URL + stream key AmateurCommunity", "Connectez-vous au panneau modèle AC, ouvrez <strong>External Encoder / OBS</strong>, et copiez l'<strong>URL serveur</strong> et la <strong>stream key</strong>."),
            ("Connectez SplitCam à AmateurCommunity", "Dans SplitCam → <strong>Stream Settings → Custom RTMP</strong>, collez l'URL et la clé. Réglez 3 500–5 000 Kbps en 1920×1080, 30 fps, keyframe 2 secondes."),
            ("Cliquez Go Live", "Appuyez sur <strong>Go Live</strong> dans SplitCam, puis passez en ligne dans le panneau modèle AC. Votre flux atterrit sur la liste publique en ~10 secondes."),
        ],
    },
    {
        "slug": "myfans-jp", "name": "MyFans.jp",
        "title": "Live sur MyFans.jp avec SplitCam (caméra virtuelle)",
        "desc": "Passer en live sur MyFans.jp (le OnlyFans japonais) avec SplitCam gratuit en caméra virtuelle — scènes multicaméras, overlays, filtres. Sans filigrane.",
        "kw": "passer en live sur myfans, myfans.jp live, myfans 配信, myfans caméra virtuelle, créateur myfans, マイファンズ, myfans japon, myfans broadcast, myfans abonné",
        "h1html": 'Comment passer en live sur <span class="accent">MyFans.jp</span> avec SplitCam',
        "h1short": "Live sur MyFans.jp",
        "card": "SplitCam en caméra virtuelle pour les lives MyFans.jp.",
        "intro": "MyFans.jp est la première plateforme d'abonnement créateurs du Japon — la réponse japonaise à OnlyFans, avec abonnements, pay-per-view, tips (投げ銭) et une fonctionnalité <strong>live</strong> intégrée pour les fans. Son broadcaster tourne dans le navigateur, donc brancher <strong style='color:var(--text)'>SplitCam</strong> gratuit en <strong>caméra virtuelle</strong> ajoute des scènes multicaméras, overlays et filtres qu'une webcam brute ne donnerait pas. Si votre tableau de bord créateur propose une option encodeur externe, SplitCam peut aussi se connecter en RTMP.",
        "quick": "Live sur MyFans.jp avec SplitCam : installer SplitCam, composer la scène, lancer un live sur MyFans, et choisir <em>SplitCam</em> dans la liste des caméras du broadcaster — puis passer en direct."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li><li>Lancer un live sur MyFans.jp.</li><li>Sélectionner SplitCam dans la liste des caméras.</li><li>Go Live.</li></ol>",
        "key_how": "Le live MyFans.jp tourne dans le navigateur. Composez la scène dans SplitCam — elle s'enregistre comme une webcam appelée <strong>« SplitCam Video Driver »</strong> — puis ouvrez le broadcaster live MyFans et choisissez <strong>SplitCam</strong> dans la liste des caméras. Si une option <strong>stream key / encodeur externe</strong> apparaît dans votre tableau de bord créateur, collez-la plutôt dans les champs RTMP personnalisé de SplitCam.",
        "tips": [
            ("La plus grosse plateforme de fans du Japon", "MyFans est la plateforme d'abonnement créateurs n°1 au Japon, avec une audience JP native qui paie en 円 (JPY). Des overlays en japonais et une scène SplitCam soignée convertissent bien mieux qu'une webcam brute."),
            ("Caméra virtuelle, pas besoin de stream key", "Un live uniquement navigateur passe quand même toute votre scène SplitCam — deuxième caméra, overlays, filtres beauté ou fond IA — en choisissant simplement SplitCam comme webcam."),
            ("Cross-sell PPV pendant le live", "MyFans est construit autour des 投げ銭 (tips) et des posts payants. Un overlay à l'écran qui annonce votre pack PPV ou un objectif de tips fait nettement grimper le revenu pendant un live."),
            _T_TEST,
        ],
        "faq": [
            ("Comment SplitCam se connecte-t-il à MyFans.jp ?", "Le live MyFans passe par le navigateur, donc SplitCam se connecte en caméra virtuelle — choisissez SplitCam dans le sélecteur de caméra. Pas besoin de stream key."),
            ("Puis-je utiliser des overlays et plusieurs caméras sur MyFans ?", "Oui — composez la scène dans SplitCam (deuxième caméra, overlays, fond IA) ; MyFans voit la scène finie comme une seule webcam."),
            ("MyFans.jp prend-il en charge OBS ou les encodeurs externes ?", "Son live est principalement basé navigateur/webcam. Si une option stream key apparaît dans votre tableau de bord, collez-la dans les champs RTMP personnalisé de SplitCam ; sinon, utilisez la méthode caméra virtuelle."),
            ("SplitCam est-il gratuit avec MyFans.jp ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Il installe une caméra virtuelle que le navigateur sait sélectionner."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays (en japonais — 「投げ銭」「PPV解放」 pour votre audience), une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Lancez un live sur MyFans.jp", "Connectez-vous à votre compte créateur MyFans et ouvrez le broadcaster live (配信) pour démarrer une diffusion pour vos abonnés."),
            ("Sélectionnez SplitCam comme caméra", "Dans la liste des caméras de MyFans, choisissez <strong>SplitCam</strong> au lieu de votre webcam brute — votre scène composée remplace la caméra plate. (Ou collez une stream key dans les champs RTMP personnalisé de SplitCam si disponible.)"),
            ("Go Live", "Lancez la diffusion — votre scène SplitCam, ses overlays et filtres arrivent chez vos abonnés MyFans."),
        ],
    },
    {
        "slug": "privacy-com-br", "name": "Privacy.com.br",
        "title": "Passer en live sur Privacy.com.br avec SplitCam",
        "desc": "Ao vivo sur Privacy.com.br (OnlyFans brésilien) avec SplitCam gratuit en caméra virtuelle — scènes multicaméras, overlays, filtres. Sans filigrane.",
        "kw": "passer en live sur privacy, privacy.com.br ao vivo, privacy live, privacy brasil, privacy caméra virtuelle, créateur privacy, privacy broadcast, privacy br criadora, privacy assinante",
        "h1html": 'Comment passer en live sur <span class="accent">Privacy.com.br</span> avec SplitCam',
        "h1short": "Live sur Privacy.com.br",
        "card": "SplitCam en caméra virtuelle pour les ao vivo Privacy.com.br.",
        "intro": "Privacy.com.br est la première plateforme d'abonnement créateurs du Brésil — la réponse brésilienne à OnlyFans, avec assinaturas, pay-per-view, gorjetas et une fonctionnalité <strong>ao vivo</strong> (live) intégrée pour les fãs. Son broadcaster tourne dans le navigateur, donc brancher <strong style='color:var(--text)'>SplitCam</strong> gratuit en <strong>caméra virtuelle</strong> ajoute des scènes multicaméras, overlays et filtres qu'une webcam brute ne donnerait pas. Si votre tableau de bord créateur propose une option encodeur externe, SplitCam peut aussi se connecter en RTMP.",
        "quick": "Live sur Privacy.com.br avec SplitCam : installer SplitCam, composer la scène, lancer un ao vivo sur Privacy, et choisir <em>SplitCam</em> dans la liste des caméras du broadcaster — puis passer en direct."
                 "<ol><li>Installer SplitCam.</li><li>Ajouter caméra + scène.</li><li>Lancer un ao vivo sur Privacy.com.br.</li><li>Sélectionner SplitCam dans la liste des caméras.</li><li>Go Live.</li></ol>",
        "key_how": "Le ao vivo de Privacy.com.br tourne dans le navigateur. Composez la scène dans SplitCam — elle s'enregistre comme une webcam appelée <strong>« SplitCam Video Driver »</strong> — puis ouvrez le broadcaster live Privacy et choisissez <strong>SplitCam</strong> dans la liste des caméras. Si une option <strong>stream key / encodeur externe</strong> est proposée, collez-la plutôt dans les champs RTMP personnalisé de SplitCam.",
        "tips": [
            ("La plus grosse plateforme de fans du Brésil", "Privacy est la plateforme d'abonnement créateurs n°1 au Brésil, avec une audience lusophone habituée à payer en BRL via PIX. Des overlays en portugais et une scène SplitCam soignée convertissent bien mieux qu'une webcam brute."),
            ("Caméra virtuelle, pas besoin de stream key", "Un live uniquement navigateur passe quand même toute votre scène SplitCam — deuxième caméra, overlays, filtres beauté ou fond IA — en choisissant simplement SplitCam comme webcam."),
            ("Menus de tips + PPV pendant l'ao vivo", "Privacy prend en charge les gorjetas (tips) et les posts payants. Un overlay à l'écran qui annonce votre pack PPV ou un meta-de-gorjeta fait grimper le revenu pendant un live."),
            _T_TEST,
        ],
        "faq": [
            ("Comment SplitCam se connecte-t-il à Privacy.com.br ?", "Le ao vivo de Privacy passe par le navigateur, donc SplitCam se connecte en caméra virtuelle — choisissez SplitCam dans le sélecteur de caméra. Pas besoin de stream key."),
            ("Puis-je utiliser des overlays et plusieurs caméras sur Privacy ?", "Oui — composez la scène dans SplitCam (deuxième caméra, overlays, fond IA) ; Privacy voit la scène finie comme une seule webcam."),
            ("Privacy.com.br prend-il en charge OBS ou les encodeurs externes ?", "Son ao vivo est principalement basé navigateur/webcam. Si une option stream key apparaît dans votre tableau de bord, collez-la dans les champs RTMP personnalisé de SplitCam ; sinon, utilisez la méthode caméra virtuelle."),
            ("SplitCam est-il gratuit avec Privacy.com.br ?", "Oui — SplitCam est gratuit, sans filigrane et sans limite de temps."),
        ],
        "steps": [
            ("Téléchargez et installez SplitCam", "SplitCam est un logiciel de streaming gratuit pour Windows et macOS — pas d'inscription, pas de carte, pas de filigrane. Il installe une caméra virtuelle que le navigateur sait sélectionner."),
            ("Composez votre scène", "Ouvrez SplitCam et ajoutez votre webcam. Empilez overlays en portugais (« gorjeta », « desbloquear PPV »), une deuxième caméra ou votre téléphone, filtres beauté ou fond IA."),
            ("Lancez un ao vivo sur Privacy.com.br", "Connectez-vous à votre compte créateur Privacy et ouvrez le broadcaster ao vivo pour démarrer une diffusion pour vos abonnés."),
            ("Sélectionnez SplitCam comme caméra", "Dans la liste des caméras de Privacy, choisissez <strong>SplitCam</strong> au lieu de votre webcam brute — votre scène composée remplace la caméra plate. (Ou collez une stream key dans les champs RTMP personnalisé de SplitCam si disponible.)"),
            ("Go Live", "Lancez la diffusion — votre scène SplitCam, ses overlays et filtres arrivent chez vos abonnés Privacy.com.br."),
        ],
    },
]
