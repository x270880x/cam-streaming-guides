# -*- coding: utf-8 -*-
LOVENSE_METHODS_MS = {
    "heading": "Sediakan Lovense pada SplitCam — 3 langkah",
    "lead": "Ini mengikut susunan tiga langkah rasmi Lovense. <strong>Cam Extension</strong> membaca "
            "tip daripada laman cam anda, <strong>Lovense Connect</strong> ialah jambatan Bluetooth ke "
            "mainan anda, dan <strong>SplitCam Toolset</strong> meletakkan tindihan Lovense di dalam "
            "SplitCam, yang menyiarkan melalui RTMP. Semuanya percuma; butang muat turun sepadan dengan "
            "sistem anda secara automatik.",
    "stage_word": "Langkah",
    "get_label": "Muat turun",
    "do_label": "Kemudian",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Membaca tip daripada laman cam anda — dipasang ke dalam Chrome atau Edge.",
            "get": ["camext"],
            "steps": [
                "Muat turun Cam Extension dan nyahzip failnya.",
                "Buka <strong>chrome://extensions</strong> (atau <strong>edge://extensions</strong>), "
                "hidupkan <strong>Developer mode</strong> di penjuru kanan atas, klik <strong>Load unpacked</strong> "
                "dan pilih folder <em>lovense_cam</em> yang telah dinyahzip.",
                "Klik ikon Lovense pada bar alat dan log masuk dengan akaun Lovense anda.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Jambatan yang berhubung dengan mainan anda melalui Bluetooth.",
            "get": ["connect"],
            "steps": [
                "Pada komputer: pasang Lovense Connect (penyesuai Bluetooth USB Lovense amat "
                "disyorkan). Pada telefon: dapatkan aplikasi Lovense Connect daripada Google Play atau App Store.",
                "Hidupkan mainan anda dan pasangkannya dalam Connect sehingga ia menunjukkan telah "
                "disambung. Pada aplikasi telefon, imbas kod QR yang dipaparkan pada komputer anda untuk memautkannya.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Memaparkan tindihan Lovense dalam SplitCam dan menyiarkan strim anda.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Pasang SplitCam, kemudian pasang Lovense SplitCam Toolset — plugin yang menambah "
                "tindihan Lovense pada SplitCam.",
                "Dalam Cam Extension, klik <strong>+</strong> untuk menambah laman cam anda (Chaturbate, "
                "Stripchat, …) dan tetapkan menu tip anda, kemudian buka tab <strong>Video Feedback</strong> "
                "dan pilih <strong>SplitCam</strong> daripada senarai (OBS / SplitCam / Streamster).",
                "Dalam SplitCam, tambah sumber <strong>Lovense</strong> yang didaftarkan oleh Toolset — "
                "tindihan menu tip / status mainan muncul pada babak anda. Kekalkan ia di atas lapisan lain.",
                "Tambah kamera anda, tampal kunci RTMP laman cam anda dalam <strong>Stream Settings</strong> "
                "SplitCam, dan klik <strong>Go Live</strong> — tindihan dan mainan bertindak balas terhadap tip.",
            ],
        },
    ],
}
