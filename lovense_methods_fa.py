# -*- coding: utf-8 -*-
LOVENSE_METHODS_FA = {
    "heading": "‏راه‌اندازی Lovense روی SplitCam — ۳ مرحله",
    "lead": "این دقیقاً همان راه‌اندازی سه‌مرحله‌ای خودِ ‏<strong>Lovense</strong> است. ‏<strong>Cam Extension</strong> "
            "انعام‌ها را از سایت کم شما می‌خواند، ‏<strong>Lovense Connect</strong> پلِ Bluetooth به اسباب‌بازی "
            "شماست، و ‏<strong>SplitCam Toolset</strong> اوورلی Lovense را داخل SplitCam قرار می‌دهد که با RTMP "
            "پخش می‌کند. همه چیز رایگان است؛ دکمه‌های دانلود به‌طور خودکار با سیستم شما هماهنگ می‌شوند.",
    "stage_word": "مرحله",
    "get_label": "دانلود",
    "do_label": "سپس",
    "stages": [
        {
            "title": "‏Lovense Cam Extension",
            "role": "انعام‌ها را از سایت کم شما می‌خواند — روی Chrome یا Edge نصب می‌شود.",
            "get": ["camext"],
            "steps": [
                "‏Cam Extension را دانلود کرده و از حالت فشرده خارج کنید.",
                "‏<strong>chrome://extensions</strong> (یا <strong>edge://extensions</strong>) را باز کنید، "
                "‏<strong>Developer mode</strong> را در بالا سمت راست روشن کنید، روی <strong>Load unpacked</strong> "
                "کلیک کنید و پوشه‌ی از حالت فشرده خارج‌شده‌ی <em>lovense_cam</em> را انتخاب کنید.",
                "روی آیکون Lovense در نوار ابزار کلیک کنید و با حساب Lovense خود وارد شوید.",
            ],
        },
        {
            "title": "‏Lovense Connect",
            "role": "پلی که از طریق Bluetooth با اسباب‌بازی شما صحبت می‌کند.",
            "get": ["connect"],
            "steps": [
                "روی کامپیوتر: ‏Lovense Connect را نصب کنید (استفاده از آداپتور USB Bluetooth مخصوص Lovense "
                "توصیه می‌شود). روی گوشی: اپلیکیشن Lovense Connect را از Google Play یا App Store بگیرید.",
                "اسباب‌بازی را روشن کنید و در Connect آن را جفت کنید تا وضعیت متصل نشان داده شود. در اپلیکیشن "
                "گوشی، کد QR نمایش‌داده‌شده روی کامپیوتر را اسکن کنید تا به هم مرتبط شوند.",
            ],
        },
        {
            "title": "‏SplitCam + Toolset",
            "role": "اوورلی Lovense را در SplitCam نشان می‌دهد و استریم شما را پخش می‌کند.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "‏SplitCam را نصب کنید، سپس Lovense SplitCam Toolset را نصب کنید — پلاگینی که اوورلی "
                "Lovense را به SplitCam اضافه می‌کند.",
                "در ‏Cam Extension روی <strong>+</strong> کلیک کنید تا سایت کم خود (Chaturbate، "
                "Stripchat، …) را اضافه کنید و منوی انعام خود را تنظیم کنید، سپس تب <strong>Video Feedback</strong> "
                "را باز کنید و از فهرست (OBS / SplitCam / Streamster) گزینه <strong>SplitCam</strong> را انتخاب کنید.",
                "در ‏SplitCam، منبع <strong>Lovense</strong> را که Toolset ثبت کرده اضافه کنید — اوورلی "
                "منوی انعام / وضعیت اسباب‌بازی روی صحنه‌ی شما ظاهر می‌شود. آن را بالای سایر لایه‌ها نگه دارید.",
                "دوربین خود را اضافه کنید، کلید RTMP سایت کم خود را در <strong>Stream Settings</strong> "
                "اسپلیت‌کم جای‌گذاری کنید و روی <strong>Go Live</strong> کلیک کنید — اوورلی و اسباب‌بازی به انعام‌ها واکنش نشان می‌دهند.",
            ],
        },
    ],
}
