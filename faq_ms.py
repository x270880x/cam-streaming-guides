# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_MS = {
    "common": [
        (
            "Berapakah pendapatan model di {name}?",
            "Pendapatan di {name} bergantung pada saiz audiens, jumlah jam siaran dan tabiat memberi tip. "
            "Penyiar aktif biasanya membawa pulang $200–$3,000 sebulan; pencapai teratas mencecah "
            "$10,000+. Bahagian hasil anda mengikut struktur komisen {name} — semak perjanjian "
            "model sebelum mula siaran langsung."
        ),
        (
            "Adakah {name} selamat untuk penyiar?",
            "{name} memerlukan pengesahan umur dan ID sebelum pembayaran, yang melindungi model "
            "daripada penipuan. Gunakan nama samaran, jangan sekali-kali kongsi data peribadi di "
            "depan kamera, aktifkan sekatan geo untuk menyembunyikan siaran anda daripada wilayah "
            "asal, dan anggap setiap permintaan penonton sebagai urus niaga. Tindanan dan latar "
            "belakang AI SplitCam juga boleh menyembunyikan atau menggantikan persekitaran sebenar anda."
        ),
        (
            "Apakah dokumen yang saya perlukan untuk menjadi model di {name}?",
            "{name} biasanya memerlukan ID foto yang dikeluarkan kerajaan (pasport, lesen memandu "
            "atau kad pengenalan), swafoto memegang ID tersebut, dan borang cukai/pembayaran (W-9 "
            "untuk AS, W-8BEN untuk bukan AS). Kelulusan biasanya mengambil masa 24–72 jam; setelah "
            "diluluskan anda boleh mula siaran langsung pada hari yang sama."
        ),
        (
            "Bolehkah saya membuat siaran di {name} dari telefon saya?",
            "{name} biasanya menawarkan aplikasi penyiar mudah alih atau penyiar web mudah alih, "
            "tetapi pengalamannya terhad — tiada tindanan, tiada kamera kedua, tiada latar belakang "
            "AI. Untuk kualiti produksi penuh, buat siaran dari komputer dengan SplitCam dan "
            "gunakan telefon anda sebagai kamera kedua (SplitCam menerima input IP-camera daripada telefon)."
        ),
    ],
    "stream": (
        "Adakah {name} menyokong OBS atau pengekod luaran?",
        "Ya — {name} menyediakan URL pelayan RTMP dan kunci strim di panel penyiar. "
        "Tampal kedua-duanya ke dalam <strong>Stream Settings → Custom RTMP</strong> SplitCam, "
        "tetapkan 1920×1080 pada 30 fps dengan kadar bit 4,000–5,000 Kbps, dan klik "
        "<strong>Go Live</strong>. Laluan Custom RTMP memberikan anda komposisi adegan SplitCam "
        "yang penuh (berbilang kamera, tindanan, penapis)."
    ),
    "vcam": (
        "Bolehkah saya menggunakan SplitCam sebagai kamera maya di {name}?",
        "Ya — siaran langsung {name} berjalan dalam pelayar, jadi SplitCam didaftarkan sebagai "
        "webcam bernama <strong>\"SplitCam Video Driver\"</strong>. Buka penyiar {name}, klik "
        "pemilih kamera dalam pelayar, dan pilih SplitCam. Adegan komposit anda (tindanan, kamera "
        "kedua, penapis, latar belakang AI) sampai kepada penonton sebagai satu suapan webcam."
    ),
}
