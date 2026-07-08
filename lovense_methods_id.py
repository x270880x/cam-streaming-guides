# -*- coding: utf-8 -*-
LOVENSE_METHODS_ID = {
    "heading": "Atur Lovense di SplitCam — 3 langkah",
    "lead": "Ini mengikuti pengaturan tiga langkah resmi dari Lovense. <strong>Cam Extension</strong> "
            "membaca tip dari situs cam kamu, <strong>Lovense Connect</strong> adalah jembatan Bluetooth "
            "ke mainanmu, dan <strong>SplitCam Toolset</strong> menaruh overlay Lovense di dalam SplitCam, "
            "yang menyiarkan lewat RTMP. Semuanya gratis; tombol unduh menyesuaikan sistemmu secara otomatis.",
    "stage_word": "Langkah",
    "get_label": "Unduh",
    "do_label": "Lalu",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Membaca tip dari situs cam kamu — dipasang di Chrome atau Edge.",
            "get": ["camext"],
            "steps": [
                "Unduh Cam Extension lalu ekstrak file-nya.",
                "Buka <strong>chrome://extensions</strong> (atau <strong>edge://extensions</strong>), "
                "nyalakan <strong>Developer mode</strong> di kanan atas, klik <strong>Load unpacked</strong> "
                "lalu pilih folder <em>lovense_cam</em> yang sudah diekstrak.",
                "Klik ikon Lovense di toolbar dan masuk dengan akun Lovense kamu.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Jembatan yang berkomunikasi dengan mainanmu lewat Bluetooth.",
            "get": ["connect"],
            "steps": [
                "Di komputer: pasang Lovense Connect (disarankan memakai adaptor Bluetooth USB Lovense). "
                "Di ponsel: unduh aplikasi Lovense Connect dari Google Play atau App Store.",
                "Nyalakan mainanmu dan pasangkan di Connect sampai statusnya tersambung. Di aplikasi ponsel, "
                "pindai kode QR yang tampil di komputer untuk menautkan keduanya.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Menampilkan overlay Lovense di SplitCam dan menyiarkan stream kamu.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Pasang SplitCam, lalu pasang Lovense SplitCam Toolset — plugin yang menambahkan "
                "overlay Lovense ke SplitCam.",
                "Di Cam Extension, klik <strong>+</strong> untuk menambahkan situs cam kamu (Chaturbate, "
                "Stripchat, …) dan atur menu tip-mu, lalu buka tab <strong>Video Feedback</strong> "
                "dan pilih <strong>SplitCam</strong> dari daftar (OBS / SplitCam / Streamster).",
                "Di SplitCam, tambahkan sumber <strong>Lovense</strong> yang didaftarkan Toolset — "
                "overlay menu tip / status mainan muncul di scene kamu. Jaga tetap di atas layer lainnya.",
                "Tambahkan kameramu, tempel kunci RTMP situs cam-mu di <strong>Stream Settings</strong> "
                "SplitCam, lalu klik <strong>Go Live</strong> — overlay dan mainan bereaksi terhadap tip.",
            ],
        },
    ],
}
