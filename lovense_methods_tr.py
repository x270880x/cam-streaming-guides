# -*- coding: utf-8 -*-
LOVENSE_METHODS_TR = {
        "heading": "Lovense'i SplitCam'de kurun — 3 adım",
        "lead": "Bu, Lovense'in kendi üç adımlı kurulumunu birebir izler. <strong>Cam Extension</strong> "
                "kamera sitenizden gelen bahşişleri okur, <strong>Lovense Connect</strong> oyuncağınıza "
                "giden Bluetooth köprüsüdür ve <strong>SplitCam Toolset</strong>, RTMP üzerinden yayın "
                "yapan SplitCam'in içine Lovense kaplamasını yerleştirir. Her şey ücretsizdir; indirme "
                "düğmeleri sisteminize otomatik olarak uyum sağlar.",
        "stage_word": "Adım",
        "get_label": "İndir",
        "do_label": "Ardından",
        "stages": [
            {
                "title": "Lovense Cam Extension",
                "role": "Kamera sitenizden gelen bahşişleri okur — Chrome veya Edge'e kurulur.",
                "get": ["camext"],
                "steps": [
                    "Cam Extension'ı indirin ve arşivden çıkarın.",
                    "<strong>chrome://extensions</strong> (veya <strong>edge://extensions</strong>) adresini "
                    "açın, sağ üstteki <strong>Developer mode</strong>'u açın, <strong>Load unpacked</strong>'e "
                    "tıklayın ve arşivden çıkardığınız <em>lovense_cam</em> klasörünü seçin.",
                    "Araç çubuğundaki Lovense simgesine tıklayın ve Lovense hesabınızla giriş yapın.",
                ],
            },
            {
                "title": "Lovense Connect",
                "role": "Oyuncağınızla Bluetooth üzerinden konuşan köprü.",
                "get": ["connect"],
                "steps": [
                    "Bilgisayarda: Lovense Connect'i kurun (bir Lovense USB Bluetooth adaptörü önerilir). "
                    "Telefonda: Lovense Connect uygulamasını Google Play veya App Store'dan edinin.",
                    "Oyuncağınızı açın ve bağlı görünene kadar Connect içinde eşleştirin. Telefon "
                    "uygulamasında, ikisini bağlamak için bilgisayarınızda görünen QR kodunu tarayın.",
                ],
            },
            {
                "title": "SplitCam + Toolset",
                "role": "SplitCam içinde Lovense kaplamasını gösterir ve yayınınızı iletir.",
                "get": ["splitcam", "toolset"],
                "steps": [
                    "SplitCam'i kurun, ardından Lovense SplitCam Toolset'i kurun — SplitCam'e Lovense "
                    "kaplamasını ekleyen eklenti.",
                    "Cam Extension'da, kamera sitenizi (Chaturbate, Stripchat, …) eklemek için "
                    "<strong>+</strong>'ya tıklayın ve bahşiş menünüzü ayarlayın, ardından <strong>Video "
                    "Feedback</strong> sekmesini açın ve listeden (OBS / SplitCam / Streamster) "
                    "<strong>SplitCam</strong>'i seçin.",
                    "SplitCam'de, Toolset'in kaydettiği <strong>Lovense</strong> kaynağını ekleyin — bahşiş "
                    "menüsü / oyuncak durumu kaplaması sahnenizde belirir. Onu diğer katmanlarınızın "
                    "üzerinde tutun.",
                    "Kameranızı ekleyin, kamera sitenizin RTMP anahtarını SplitCam'in <strong>Stream "
                    "Settings</strong> bölümüne yapıştırın ve <strong>Go Live</strong>'a tıklayın — kaplama "
                    "ve oyuncak bahşişlere tepki verir.",
                ],
            },
        ],
}
