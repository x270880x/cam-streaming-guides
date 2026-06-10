# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_ID = {
    "common": [
        (
            "Berapa penghasilan model di {name}?",
            "Penghasilan di {name} bergantung pada ukuran audiens, jam siaran, dan kebiasaan memberi tip. "
            "Broadcaster aktif biasanya membawa pulang $200–$3.000 per bulan; performer top mencapai "
            "$10.000+. Bagian pendapatan Anda mengikuti struktur komisi {name} — periksa perjanjian "
            "model sebelum mulai siaran."
        ),
        (
            "Apakah {name} aman untuk broadcaster?",
            "{name} mewajibkan verifikasi usia dan identitas sebelum pembayaran, yang melindungi model "
            "dari penipuan. Gunakan nama panggung, jangan pernah membagikan data pribadi di kamera, "
            "aktifkan geo-block untuk menyembunyikan siaran dari wilayah asal Anda, dan perlakukan "
            "setiap permintaan penonton sebagai transaksi. Overlay dan AI background SplitCam juga "
            "dapat menyembunyikan atau mengganti lingkungan asli Anda."
        ),
        (
            "Dokumen apa yang dibutuhkan untuk menjadi model di {name}?",
            "{name} biasanya membutuhkan kartu identitas berfoto yang dikeluarkan pemerintah (paspor, "
            "SIM, atau KTP), selfie sambil memegang ID, dan formulir pajak/pembayaran (W-9 untuk AS, "
            "W-8BEN untuk non-AS). Persetujuan biasanya memakan waktu 24–72 jam; setelah disetujui "
            "Anda bisa langsung siaran di hari yang sama."
        ),
        (
            "Bisakah saya siaran di {name} dari ponsel?",
            "{name} biasanya menawarkan aplikasi broadcaster mobile atau broadcaster mobile-web, tetapi "
            "pengalamannya terbatas — tanpa overlay, tanpa kamera kedua, tanpa AI background. Untuk "
            "kualitas produksi penuh, siaran dari komputer dengan SplitCam dan gunakan ponsel Anda "
            "sebagai kamera kedua (SplitCam menerima input IP-camera dari ponsel)."
        ),
    ],
    "stream": (
        "Apakah {name} mendukung OBS atau encoder eksternal?",
        "Ya — {name} menyediakan URL server RTMP dan stream key di panel broadcaster. "
        "Tempelkan keduanya ke <strong>Stream Settings → Custom RTMP</strong> SplitCam, atur "
        "1920×1080 pada 30 fps dengan bitrate 4.000–5.000 Kbps, dan klik <strong>Go Live</strong>. "
        "Jalur Custom RTMP memberi Anda komposisi scene SplitCam penuh (multi-kamera, overlay, filter)."
    ),
    "vcam": (
        "Bisakah saya menggunakan SplitCam sebagai virtual camera di {name}?",
        "Ya — live {name} berjalan di browser, jadi SplitCam terdaftar sebagai webcam bernama "
        "<strong>\"SplitCam Video Driver\"</strong>. Buka broadcaster {name}, klik pemilih kamera "
        "di browser, lalu pilih SplitCam. Scene yang sudah Anda susun (overlay, kamera kedua, "
        "filter, AI background) sampai ke penonton sebagai satu feed webcam."
    ),
}
