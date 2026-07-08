# -*- coding: utf-8 -*-
"""Arabic (ar) translation of the Lovense 3-step SplitCam guide. RTL language."""

LOVENSE_METHODS_AR = {
    "heading": "إعداد ‏Lovense على ‏SplitCam — 3 خطوات",
    "lead": "هذا يعكس إعداد ‏Lovense الرسمي المكوّن من ثلاث خطوات. تقرأ <strong>‏Cam Extension</strong> "
            "الإكراميات من موقع الكام الخاص بك، و<strong>‏Lovense Connect</strong> هي جسر ‏Bluetooth "
            "إلى لعبتك، بينما تضع <strong>‏SplitCam Toolset</strong> تراكب ‏Lovense داخل ‏SplitCam، "
            "التي تبث عبر ‏RTMP. كل شيء مجاني؛ وأزرار التنزيل تطابق نظامك تلقائياً.",
    "stage_word": "الخطوة",
    "get_label": "التنزيل",
    "do_label": "ثم",
    "stages": [
        {
            "title": "‏Lovense Cam Extension",
            "role": "تقرأ الإكراميات من موقع الكام الخاص بك — تُثبَّت في ‏Chrome أو ‏Edge.",
            "get": ["camext"],
            "steps": [
                "نزّل ‏Cam Extension وفك ضغطها.",
                "افتح <strong>chrome://extensions</strong> (أو <strong>edge://extensions</strong>)، "
                "فعّل <strong>Developer mode</strong> في أعلى اليمين، انقر <strong>Load unpacked</strong> "
                "واختر مجلد <em>lovense_cam</em> الذي فككت ضغطه.",
                "انقر أيقونة ‏Lovense في شريط الأدوات وسجّل الدخول بحساب ‏Lovense الخاص بك.",
            ],
        },
        {
            "title": "‏Lovense Connect",
            "role": "الجسر الذي يتواصل مع لعبتك عبر ‏Bluetooth.",
            "get": ["connect"],
            "steps": [
                "على الكمبيوتر: ثبّت ‏Lovense Connect (يُنصح بمحوّل ‏Lovense USB Bluetooth). "
                "على الهاتف: احصل على تطبيق ‏Lovense Connect من ‏Google Play أو ‏App Store.",
                "شغّل لعبتك وأقرنها في ‏Connect حتى تظهر متصلة. في تطبيق الهاتف، امسح رمز ‏QR "
                "المعروض على الكمبيوتر لربطهما.",
            ],
        },
        {
            "title": "‏SplitCam + Toolset",
            "role": "تعرض تراكب ‏Lovense في ‏SplitCam وتبث بثك.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "ثبّت ‏SplitCam، ثم ثبّت ‏Lovense SplitCam Toolset — الإضافة التي تضيف تراكب "
                "‏Lovense إلى ‏SplitCam.",
                "في ‏Cam Extension، انقر <strong>+</strong> لإضافة موقع الكام الخاص بك (‏Chaturbate، "
                "‏Stripchat، …) واضبط قائمة الإكراميات، ثم افتح علامة التبويب <strong>Video Feedback</strong> "
                "واختر <strong>‏SplitCam</strong> من القائمة (‏OBS / ‏SplitCam / ‏Streamster).",
                "في ‏SplitCam، أضف مصدر <strong>‏Lovense</strong> الذي سجّلته ‏Toolset — يظهر تراكب "
                "قائمة الإكراميات / حالة اللعبة على مشهدك. أبقِه فوق طبقاتك الأخرى.",
                "أضف كاميرتك، الصق مفتاح ‏RTMP لموقع الكام في <strong>Stream Settings</strong> بـ ‏SplitCam، "
                "وانقر <strong>Go Live</strong> — يتفاعل التراكب واللعبة مع الإكراميات.",
            ],
        },
    ],
}
