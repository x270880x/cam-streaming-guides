# -*- coding: utf-8 -*-
LOVENSE_METHODS_HI = {
    "heading": "SplitCam पर Lovense सेट करें — 3 स्टेप",
    "lead": "यह बिल्कुल Lovense के अपने तीन-स्टेप सेटअप जैसा है। <strong>Cam Extension</strong> आपकी "
            "कैम साइट से टिप्स पढ़ता है, <strong>Lovense Connect</strong> आपके टॉय तक का Bluetooth पुल है, "
            "और <strong>SplitCam Toolset</strong> Lovense ओवरले को SplitCam के अंदर लाता है, जो RTMP पर "
            "ब्रॉडकास्ट करता है। सब कुछ मुफ़्त है; डाउनलोड बटन अपने-आप आपके सिस्टम के हिसाब से मिल जाते हैं।",
    "stage_word": "स्टेप",
    "get_label": "डाउनलोड",
    "do_label": "फिर",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "आपकी कैम साइट से टिप्स पढ़ता है — Chrome या Edge में इंस्टॉल होता है।",
            "get": ["camext"],
            "steps": [
                "Cam Extension डाउनलोड करें और उसे अनज़िप करें।",
                "<strong>chrome://extensions</strong> (या <strong>edge://extensions</strong>) खोलें, "
                "ऊपर-दाईं ओर <strong>Developer mode</strong> ऑन करें, <strong>Load unpacked</strong> पर "
                "क्लिक करें और अनज़िप की गई <em>lovense_cam</em> फ़ोल्डर चुनें।",
                "टूलबार में Lovense आइकन पर क्लिक करें और अपने Lovense अकाउंट से लॉग इन करें।",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "वह पुल जो Bluetooth के ज़रिए आपके टॉय से बात करता है।",
            "get": ["connect"],
            "steps": [
                "कंप्यूटर पर: Lovense Connect इंस्टॉल करें (Lovense USB Bluetooth अडैप्टर की सलाह दी "
                "जाती है)। फ़ोन पर: Google Play या App Store से Lovense Connect ऐप लें।",
                "अपना टॉय ऑन करें और Connect में तब तक पेयर करें जब तक वह कनेक्टेड न दिखे। फ़ोन ऐप में, "
                "अपने कंप्यूटर पर दिख रहे QR कोड को स्कैन करके उन्हें लिंक करें।",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "SplitCam में Lovense ओवरले दिखाता है और आपकी स्ट्रीम ब्रॉडकास्ट करता है।",
            "get": ["splitcam", "toolset"],
            "steps": [
                "SplitCam इंस्टॉल करें, फिर Lovense SplitCam Toolset इंस्टॉल करें — वह प्लगइन जो SplitCam "
                "में Lovense ओवरले जोड़ता है।",
                "Cam Extension में, अपनी कैम साइट (Chaturbate, Stripchat, …) जोड़ने के लिए <strong>+</strong> "
                "पर क्लिक करें और अपना टिप मेन्यू सेट करें, फिर <strong>Video Feedback</strong> टैब खोलें और "
                "सूची (OBS / SplitCam / Streamster) में से <strong>SplitCam</strong> चुनें।",
                "SplitCam में, Toolset ने जो <strong>Lovense</strong> सोर्स रजिस्टर किया है उसे जोड़ें — "
                "टिप-मेन्यू / टॉय-स्टेटस ओवरले आपके सीन पर दिखने लगेगा। इसे अपनी बाकी लेयरों के ऊपर रखें।",
                "अपना कैमरा जोड़ें, अपनी कैम साइट की RTMP की SplitCam की <strong>Stream Settings</strong> में "
                "पेस्ट करें, और <strong>Go Live</strong> पर क्लिक करें — ओवरले और टॉय टिप्स पर रिएक्ट करते हैं।",
            ],
        },
    ],
}
