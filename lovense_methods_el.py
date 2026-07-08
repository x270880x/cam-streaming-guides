# -*- coding: utf-8 -*-
LOVENSE_METHODS_EL = {
    "heading": "Ρύθμιση του Lovense στο SplitCam — 3 βήματα",
    "lead": "Ακολουθεί την ίδια ρύθμιση τριών βημάτων της Lovense. Το <strong>Cam Extension</strong> "
            "διαβάζει τα φιλοδωρήματα από τη σελίδα κάμερας, το <strong>Lovense Connect</strong> είναι η "
            "γέφυρα Bluetooth προς το παιχνίδι σου, και το <strong>SplitCam Toolset</strong> τοποθετεί το "
            "overlay της Lovense μέσα στο SplitCam, που μεταδίδει μέσω RTMP. Όλα είναι δωρεάν· τα κουμπιά "
            "λήψης προσαρμόζονται αυτόματα στο σύστημά σου.",
    "stage_word": "Βήμα",
    "get_label": "Λήψη",
    "do_label": "Έπειτα",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Διαβάζει τα φιλοδωρήματα από τη σελίδα κάμεράς σου — εγκαθίσταται σε Chrome ή Edge.",
            "get": ["camext"],
            "steps": [
                "Κατέβασε το Cam Extension και αποσυμπίεσέ το.",
                "Άνοιξε το <strong>chrome://extensions</strong> (ή <strong>edge://extensions</strong>), "
                "ενεργοποίησε τη <strong>Developer mode</strong> επάνω δεξιά, κάνε κλικ στο "
                "<strong>Load unpacked</strong> και επίλεξε τον αποσυμπιεσμένο φάκελο <em>lovense_cam</em>.",
                "Κάνε κλικ στο εικονίδιο Lovense στη γραμμή εργαλείων και συνδέσου με τον λογαριασμό σου Lovense.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Η γέφυρα που επικοινωνεί με το παιχνίδι σου μέσω Bluetooth.",
            "get": ["connect"],
            "steps": [
                "Σε υπολογιστή: εγκατέστησε το Lovense Connect (συνιστάται προσαρμογέας Lovense USB Bluetooth). "
                "Σε κινητό: κατέβασε την εφαρμογή Lovense Connect από το Google Play ή το App Store.",
                "Άναψε το παιχνίδι σου και ζευγάρωσέ το στο Connect μέχρι να εμφανιστεί συνδεδεμένο. Στην εφαρμογή "
                "κινητού, σάρωσε τον κωδικό QR που εμφανίζεται στον υπολογιστή σου για να τα συνδέσεις.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Εμφανίζει το overlay της Lovense στο SplitCam και μεταδίδει τη ροή σου.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Εγκατέστησε το SplitCam και μετά εγκατέστησε το Lovense SplitCam Toolset — το πρόσθετο που "
                "προσθέτει το overlay της Lovense στο SplitCam.",
                "Στο Cam Extension, κάνε κλικ στο <strong>+</strong> για να προσθέσεις τη σελίδα κάμεράς σου "
                "(Chaturbate, Stripchat, …) και όρισε το μενού φιλοδωρημάτων, έπειτα άνοιξε την καρτέλα "
                "<strong>Video Feedback</strong> και επίλεξε <strong>SplitCam</strong> από τη λίστα "
                "(OBS / SplitCam / Streamster).",
                "Στο SplitCam, πρόσθεσε την πηγή <strong>Lovense</strong> που κατέγραψε το Toolset — το overlay "
                "μενού φιλοδωρημάτων / κατάστασης παιχνιδιού εμφανίζεται στη σκηνή σου. Κράτησέ το πάνω από τα "
                "άλλα επίπεδά σου.",
                "Πρόσθεσε την κάμερά σου, επικόλλησε το κλειδί RTMP της σελίδας κάμεράς σου στις "
                "<strong>Stream Settings</strong> του SplitCam και κάνε κλικ στο <strong>Go Live</strong> — το "
                "overlay και το παιχνίδι αντιδρούν στα φιλοδωρήματα.",
            ],
        },
    ],
}
