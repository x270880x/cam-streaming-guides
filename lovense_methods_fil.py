# -*- coding: utf-8 -*-
LOVENSE_METHODS_FIL = {
    "heading": "I-set up ang Lovense sa SplitCam — 3 hakbang",
    "lead": "Sinusunod nito ang sariling tatlong-hakbang na setup ng Lovense. Binabasa ng "
            "<strong>Cam Extension</strong> ang mga tip mula sa iyong cam site, ang "
            "<strong>Lovense Connect</strong> ang Bluetooth bridge papunta sa iyong toy, at "
            "inilalagay ng <strong>SplitCam Toolset</strong> ang Lovense overlay sa loob ng "
            "SplitCam, na nagba-broadcast sa pamamagitan ng RTMP. Libre lahat; awtomatikong "
            "tumutugma ang mga download button sa iyong system.",
    "stage_word": "Hakbang",
    "get_label": "I-download",
    "do_label": "Pagkatapos",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Binabasa ang mga tip mula sa iyong cam site — nag-i-install sa Chrome o Edge.",
            "get": ["camext"],
            "steps": [
                "I-download ang Cam Extension at i-unzip ito.",
                "Buksan ang <strong>chrome://extensions</strong> (o <strong>edge://extensions</strong>), "
                "i-on ang <strong>Developer mode</strong> sa kanang itaas, i-click ang <strong>Load unpacked</strong> "
                "at piliin ang na-unzip na <em>lovense_cam</em> folder.",
                "I-click ang Lovense icon sa toolbar at mag-log in gamit ang iyong Lovense account.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Ang bridge na nakikipag-usap sa iyong toy sa pamamagitan ng Bluetooth.",
            "get": ["connect"],
            "steps": [
                "Sa computer: i-install ang Lovense Connect (inirerekomenda ang Lovense USB Bluetooth "
                "adapter). Sa phone: kunin ang Lovense Connect app mula sa Google Play o App Store.",
                "I-on ang iyong toy at i-pair ito sa Connect hanggang lumabas na connected. Sa phone app, "
                "i-scan ang QR code na ipinapakita sa iyong computer para pagdugtungin sila.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Ipinapakita ang Lovense overlay sa SplitCam at nagba-broadcast ng iyong stream.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "I-install ang SplitCam, tapos i-install ang Lovense SplitCam Toolset — ang plugin na "
                "nagdadagdag ng Lovense overlay sa SplitCam.",
                "Sa Cam Extension, i-click ang <strong>+</strong> para idagdag ang iyong cam site (Chaturbate, "
                "Stripchat, …) at i-set ang iyong tip menu, tapos buksan ang <strong>Video Feedback</strong> "
                "tab at piliin ang <strong>SplitCam</strong> mula sa listahan (OBS / SplitCam / Streamster).",
                "Sa SplitCam, idagdag ang <strong>Lovense</strong> source na na-register ng Toolset — lalabas "
                "ang tip-menu / toy-status overlay sa iyong scene. Panatilihin itong nasa ibabaw ng iba mong layers.",
                "Idagdag ang iyong camera, i-paste ang RTMP key ng iyong cam site sa <strong>Stream "
                "Settings</strong> ng SplitCam, at i-click ang <strong>Go Live</strong> — tutugon ang overlay at toy sa mga tip.",
            ],
        },
    ],
}
