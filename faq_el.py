# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_EL = {
    "common": [
        (
            "Πόσα μπορούν να κερδίσουν τα μοντέλα στο {name};",
            "Τα κέρδη στο {name} εξαρτώνται από το μέγεθος του κοινού, τις ώρες μετάδοσης και τη "
            "συμπεριφορά φιλοδωρημάτων. Οι ενεργοί broadcasters συνήθως παίρνουν σπίτι 200–3.000 $ "
            "τον μήνα· οι κορυφαίοι performers φτάνουν τα 10.000 $+. Το μερίδιό σας ακολουθεί τη "
            "δομή προμηθειών του {name} — ελέγξτε τη σύμβαση μοντέλου πριν βγείτε live."
        ),
        (
            "Είναι το {name} ασφαλές για τους broadcasters;",
            "Το {name} απαιτεί επαλήθευση ηλικίας και ταυτότητας πριν την πληρωμή, κάτι που "
            "προστατεύει τα μοντέλα από απάτη. Χρησιμοποιήστε καλλιτεχνικό όνομα, μην μοιράζεστε "
            "ποτέ προσωπικά δεδομένα στην κάμερα, ενεργοποιήστε geo-blocks για να κρύψετε τη "
            "μετάδοσή σας από την περιοχή σας και αντιμετωπίστε κάθε αίτημα θεατή ως συναλλακτικό. "
            "Τα overlays του SplitCam και το AI background μπορούν επίσης να κρύψουν ή να "
            "αντικαταστήσουν τον πραγματικό σας χώρο."
        ),
        (
            "Τι έγγραφα χρειάζομαι για να γίνω μοντέλο στο {name};",
            "Το {name} συνήθως απαιτεί επίσημη φωτογραφική ταυτότητα (διαβατήριο, δίπλωμα οδήγησης "
            "ή ταυτότητα), μια selfie όπου κρατάτε την ταυτότητα, και ένα φορολογικό έντυπο "
            "πληρωμής (W-9 για ΗΠΑ, W-8BEN για εκτός ΗΠΑ). Η έγκριση συνήθως διαρκεί 24–72 ώρες· "
            "μόλις εγκριθείτε μπορείτε να βγείτε live την ίδια μέρα."
        ),
        (
            "Μπορώ να κάνω stream στο {name} από το κινητό μου;",
            "Το {name} συνήθως προσφέρει εφαρμογή broadcaster για κινητά ή mobile-web broadcaster, "
            "αλλά η εμπειρία είναι περιορισμένη — χωρίς overlays, χωρίς δεύτερη κάμερα, χωρίς AI "
            "background. Για πλήρη ποιότητα παραγωγής, κάντε μετάδοση από υπολογιστή με SplitCam "
            "και χρησιμοποιήστε το κινητό σας ως δεύτερη κάμερα (το SplitCam δέχεται είσοδο "
            "IP-camera από κινητά)."
        ),
    ],
    "stream": (
        "Υποστηρίζει το {name} OBS ή εξωτερικό encoder;",
        "Ναι — το {name} παρέχει RTMP server URL και stream key στο πάνελ broadcaster. "
        "Επικολλήστε και τα δύο στο <strong>Stream Settings → Custom RTMP</strong> του SplitCam, "
        "ρυθμίστε 1920×1080 στα 30 fps με bitrate 4.000–5.000 Kbps και κάντε κλικ στο "
        "<strong>Go Live</strong>. Η διαδρομή Custom RTMP σας δίνει πλήρη σύνθεση σκηνής SplitCam "
        "(πολλαπλές κάμερες, overlays, φίλτρα)."
    ),
    "vcam": (
        "Μπορώ να χρησιμοποιήσω το SplitCam ως virtual camera στο {name};",
        "Ναι — το live του {name} τρέχει στον browser, οπότε το SplitCam καταχωρείται ως webcam "
        "με όνομα <strong>\"SplitCam Video Driver\"</strong>. Ανοίξτε τον broadcaster του {name}, "
        "κάντε κλικ στον επιλογέα κάμερας του browser και επιλέξτε SplitCam. Η συντεθειμένη "
        "σκηνή σας (overlays, δεύτερη κάμερα, φίλτρα, AI background) φτάνει στους θεατές ως "
        "μία ροή webcam."
    ),
}
