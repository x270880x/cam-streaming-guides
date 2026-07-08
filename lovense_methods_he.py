# -*- coding: utf-8 -*-
LOVENSE_METHODS_HE = {
    "heading": "הגדרת ‏Lovense ב‏SplitCam — 3 שלבים",
    "lead": "התהליך הזה תואם להתקנה בת שלושת השלבים של ‏Lovense עצמה. ה‏<strong>Cam Extension</strong> "
            "קורא את הטיפים מאתר הקאם שלך, ‏<strong>Lovense Connect</strong> הוא גשר ה‏Bluetooth "
            "אל הצעצוע, וה‏<strong>SplitCam Toolset</strong> ממקם את שכבת ‏Lovense בתוך "
            "‏SplitCam, שמשדרת דרך ‏RTMP. הכול חינם; כפתורי ההורדה מתאימים את עצמם "
            "למערכת שלך אוטומטית.",
    "stage_word": "שלב",
    "get_label": "הורדה",
    "do_label": "אחר כך",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "קורא את הטיפים מאתר הקאם שלך — מותקן ב‏Chrome או ב‏Edge.",
            "get": ["camext"],
            "steps": [
                "הורד את ה‏Cam Extension וחלץ אותו מהזיפ.",
                "פתח את ‏<strong>chrome://extensions</strong> (או ‏<strong>edge://extensions</strong>), "
                "הפעל את ‏<strong>Developer mode</strong> בפינה הימנית העליונה, לחץ על ‏<strong>Load unpacked</strong> "
                "ובחר בתיקייה המחולצת ‏<em>lovense_cam</em>.",
                "לחץ על סמל ‏Lovense בסרגל הכלים והתחבר עם חשבון ה‏Lovense שלך.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "הגשר שמדבר עם הצעצוע שלך דרך ‏Bluetooth.",
            "get": ["connect"],
            "steps": [
                "במחשב: התקן את ‏Lovense Connect (מומלץ מתאם ‏Bluetooth של ‏Lovense דרך ‏USB). "
                "בטלפון: הורד את אפליקציית ‏Lovense Connect מ‏Google Play או מ‏App Store.",
                "הדלק את הצעצוע ובצע לו התאמה ב‏Connect עד שהוא מוצג כמחובר. באפליקציית הטלפון, "
                "סרוק את קוד ה‏QR שמוצג במחשב כדי לקשר ביניהם.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "מציג את שכבת ‏Lovense בתוך ‏SplitCam ומשדר את הסטרים שלך.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "התקן את ‏SplitCam, ואז התקן את ה‏Lovense SplitCam Toolset — התוסף שמוסיף "
                "את שכבת ‏Lovense אל ‏SplitCam.",
                "ב‏Cam Extension, לחץ על ‏<strong>+</strong> כדי להוסיף את אתר הקאם שלך (‏Chaturbate, "
                "‏Stripchat, …) והגדר את תפריט הטיפים שלך, ואז פתח את הלשונית ‏<strong>Video Feedback</strong> "
                "ובחר ‏<strong>SplitCam</strong> מהרשימה (‏OBS / ‏SplitCam / ‏Streamster).",
                "ב‏SplitCam, הוסף את מקור ה‏<strong>Lovense</strong> שה‏Toolset רשם — "
                "שכבת תפריט הטיפים / מצב הצעצוע מופיעה בסצנה שלך. השאר אותה מעל שאר השכבות.",
                "הוסף את המצלמה שלך, הדבק את מפתח ה‏RTMP של אתר הקאם שלך ב‏<strong>Stream "
                "Settings</strong> של ‏SplitCam, ולחץ על ‏<strong>Go Live</strong> — השכבה והצעצוע מגיבים לטיפים.",
            ],
        },
    ],
}
