# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_HI = {
    "common": [
        (
            "{name} पर मॉडल कितनी कमाई कर सकते हैं?",
            "{name} पर कमाई दर्शकों की संख्या, स्ट्रीमिंग के घंटों और टिप देने के व्यवहार पर निर्भर करती है। "
            "सक्रिय ब्रॉडकास्टर आमतौर पर हर महीने $200–$3,000 कमाते हैं; शीर्ष कलाकार "
            "$10,000+ तक पहुँचते हैं। आपकी आय का हिस्सा {name} की कमीशन संरचना के अनुसार होता है — लाइव "
            "होने से पहले मॉडल अनुबंध अवश्य देखें।"
        ),
        (
            "क्या {name} ब्रॉडकास्टरों के लिए सुरक्षित है?",
            "{name} भुगतान से पहले आयु और पहचान सत्यापन माँगता है, जो मॉडलों को धोखाधड़ी से बचाता है। "
            "स्टेज नाम का उपयोग करें, कैमरे पर कभी भी व्यक्तिगत डेटा साझा न करें, अपने घर के क्षेत्र से स्ट्रीम "
            "छिपाने के लिए geo-blocks सक्षम करें, और हर दर्शक के अनुरोध को लेन-देन के रूप में मानें। "
            "SplitCam के overlays और AI background आपके वास्तविक परिवेश को छिपाने या बदलने में भी "
            "मदद कर सकते हैं।"
        ),
        (
            "{name} पर मॉडल बनने के लिए मुझे कौन से दस्तावेज़ चाहिए?",
            "{name} को आमतौर पर सरकार द्वारा जारी फोटो आईडी (passport, driver's license "
            "या ID card), आईडी पकड़े हुए एक selfie, और एक tax/payout फॉर्म (अमेरिका के लिए W-9, "
            "गैर-अमेरिकी के लिए W-8BEN) की आवश्यकता होती है। स्वीकृति में आमतौर पर 24–72 घंटे लगते हैं; "
            "स्वीकृति मिलते ही आप उसी दिन लाइव हो सकते हैं।"
        ),
        (
            "क्या मैं अपने फोन से {name} पर स्ट्रीम कर सकता हूँ?",
            "{name} आमतौर पर एक mobile broadcaster app या mobile-web broadcaster प्रदान करता है, लेकिन "
            "अनुभव सीमित होता है — कोई overlays नहीं, कोई दूसरा कैमरा नहीं, कोई AI background नहीं। पूर्ण "
            "प्रोडक्शन क्वालिटी के लिए, SplitCam वाले कंप्यूटर से ब्रॉडकास्ट करें और अपने फोन को दूसरे कैमरे के "
            "रूप में उपयोग करें (SplitCam फोन से IP-camera input स्वीकार करता है)।"
        ),
    ],
    "stream": (
        "क्या {name} OBS या किसी बाहरी encoder का समर्थन करता है?",
        "हाँ — {name} broadcaster panel में एक RTMP server URL और एक stream key प्रदान करता है। "
        "दोनों को SplitCam के <strong>Stream Settings → Custom RTMP</strong> में paste करें, "
        "1920×1080 को 30 fps और 4,000–5,000 Kbps bitrate पर सेट करें, और <strong>Go Live</strong> पर क्लिक करें। "
        "Custom RTMP रूट आपको पूर्ण SplitCam scene composition देता है (multi-camera, overlays, filters)।"
    ),
    "vcam": (
        "क्या मैं {name} पर SplitCam को virtual camera के रूप में उपयोग कर सकता हूँ?",
        "हाँ — {name} का लाइव browser में चलता है, इसलिए SplitCam एक webcam के रूप में पंजीकृत होता है जिसे "
        "<strong>\"SplitCam Video Driver\"</strong> कहा जाता है। {name} broadcaster खोलें, browser में camera "
        "selector पर क्लिक करें, और SplitCam चुनें। आपका composed scene (overlays, दूसरा कैमरा, "
        "filters, AI background) एकल webcam feed के रूप में दर्शकों तक पहुँचता है।"
    ),
}
