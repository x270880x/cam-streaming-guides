# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_FR = {
    "common": [
        (
            "Combien peut-on gagner en tant que créateur sur {name} ?",
            "Les revenus sur {name} dépendent de la taille de l'audience, des heures de direct et "
            "de la générosité des pourboires. Un créateur actif gagne en général entre 200 et "
            "3 000 $ par mois ; les meilleurs dépassent 10 000 $. Votre part de revenus suit la "
            "grille de commissions de {name} — vérifiez l'accord créateur avant de passer en direct."
        ),
        (
            "{name} est-il sûr pour les créateurs en direct ?",
            "{name} exige une vérification d'âge et d'identité avant tout versement, ce qui protège "
            "les créateurs contre la fraude. Utilisez un pseudonyme, ne partagez jamais de données "
            "personnelles à la caméra, activez les blocages géographiques pour cacher votre direct "
            "depuis votre région d'origine, et traitez chaque demande de spectateur comme une "
            "transaction. Les surimpressions et l'arrière-plan IA de SplitCam permettent aussi de "
            "masquer ou de remplacer votre véritable décor."
        ),
        (
            "Quels documents faut-il pour devenir créateur sur {name} ?",
            "{name} demande en général une pièce d'identité officielle avec photo (passeport, "
            "permis de conduire ou carte d'identité), un selfie avec le document en main, et un "
            "formulaire fiscal pour la cagnotte (W-9 aux États-Unis, W-8BEN hors États-Unis). "
            "La validation prend habituellement 24 à 72 heures ; une fois acceptée, vous pouvez "
            "passer en direct le jour même."
        ),
        (
            "Puis-je diffuser sur {name} depuis mon téléphone ?",
            "{name} propose en général une application mobile pour créateur ou un studio mobile "
            "via le navigateur, mais l'expérience reste limitée — pas de surimpressions, pas de "
            "seconde caméra, pas d'arrière-plan IA. Pour une qualité de production complète, "
            "diffusez depuis un ordinateur avec SplitCam et utilisez votre téléphone comme "
            "deuxième caméra (SplitCam accepte le flux IP-camera des téléphones)."
        ),
    ],
    "stream": (
        "{name} prend-il en charge OBS ou un encodeur externe ?",
        "Oui — {name} fournit une URL de serveur RTMP et une clé de flux dans le panneau créateur. "
        "Collez les deux dans <strong>Paramètres de diffusion → RTMP personnalisé</strong> de "
        "SplitCam, réglez sur 1920×1080 à 30 ips avec un débit de 4 000 à 5 000 Kbps, puis cliquez "
        "sur <strong>Passer en direct</strong>. La voie RTMP personnalisé vous donne accès à toute "
        "la composition de scène SplitCam (multi-caméras, surimpressions, filtres)."
    ),
    "vcam": (
        "Puis-je utiliser SplitCam comme caméra virtuelle sur {name} ?",
        "Oui — le direct de {name} s'exécute dans le navigateur, donc SplitCam apparaît comme une "
        "webcam appelée <strong>\"SplitCam Video Driver\"</strong>. Ouvrez le studio créateur "
        "{name}, cliquez sur le sélecteur de caméra dans le navigateur et choisissez SplitCam. "
        "Votre scène composée (surimpressions, seconde caméra, filtres, arrière-plan IA) parvient "
        "aux spectateurs comme un flux webcam unique."
    ),
}
