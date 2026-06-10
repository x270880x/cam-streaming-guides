# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_TR = {
    "common": [
        (
            "{name} üzerinde modeller ne kadar kazanabilir?",
            "{name} platformundaki kazançlar izleyici sayısına, yayın saatlerine ve bahşiş "
            "davranışına bağlıdır. Aktif yayıncılar genellikle ayda 200–3.000 dolar kazanır; "
            "en iyi performans gösterenler 10.000 doların üzerine çıkar. Gelir payınız {name} "
            "komisyon yapısına göre belirlenir — yayına geçmeden önce model sözleşmesini inceleyin."
        ),
        (
            "{name} yayıncılar için güvenli mi?",
            "{name} ödemeden önce yaş ve kimlik doğrulaması ister; bu, modelleri dolandırıcılığa "
            "karşı korur. Sahne adı kullanın, kamerada asla kişisel bilgi paylaşmayın, yayınınızı "
            "kendi bölgenizden gizlemek için coğrafi engelleme aktif edin ve her izleyici talebini "
            "ticari bir işlem olarak değerlendirin. SplitCam'in overlay'leri ve yapay zeka arka "
            "planı da gerçek ortamınızı gizleyebilir veya değiştirebilir."
        ),
        (
            "{name} üzerinde model olmak için hangi belgeler gerekli?",
            "{name} genellikle devlet tarafından verilmiş fotoğraflı bir kimlik (pasaport, ehliyet "
            "veya kimlik kartı), kimliği tutarken çekilmiş bir selfie ve bir vergi/ödeme formu "
            "(ABD için W-9, ABD dışı için W-8BEN) ister. Onay genellikle 24–72 saat sürer; "
            "onaylandıktan sonra aynı gün yayına geçebilirsiniz."
        ),
        (
            "{name} üzerinde telefonumdan yayın yapabilir miyim?",
            "{name} genellikle bir mobil yayıncı uygulaması veya mobil-web yayıncı arayüzü sunar, "
            "ancak deneyim sınırlıdır — overlay yok, ikinci kamera yok, yapay zeka arka planı yok. "
            "Tam prodüksiyon kalitesi için SplitCam ile bir bilgisayardan yayın yapın ve "
            "telefonunuzu ikinci kamera olarak kullanın (SplitCam telefonlardan IP-kamera "
            "girişini kabul eder)."
        ),
    ],
    "stream": (
        "{name} OBS veya harici bir encoder destekliyor mu?",
        "Evet — {name} yayıncı panelinde bir RTMP sunucu URL'si ve yayın anahtarı sağlar. "
        "Her ikisini de SplitCam'in <strong>Stream Settings → Custom RTMP</strong> bölümüne "
        "yapıştırın, 30 fps'de 1920×1080 ve 4.000–5.000 Kbps bitrate ayarlayın ve "
        "<strong>Go Live</strong>'a tıklayın. Custom RTMP yolu size tam SplitCam sahne "
        "kompozisyonu sağlar (çoklu kamera, overlay'ler, filtreler)."
    ),
    "vcam": (
        "SplitCam'i {name} üzerinde sanal kamera olarak kullanabilir miyim?",
        "Evet — {name}'in canlı yayını tarayıcıda çalışır, bu yüzden SplitCam "
        "<strong>\"SplitCam Video Driver\"</strong> adlı bir webcam olarak kaydedilir. "
        "{name} yayıncı arayüzünü açın, tarayıcıdaki kamera seçiciye tıklayın ve SplitCam'i "
        "seçin. Oluşturduğunuz sahne (overlay'ler, ikinci kamera, filtreler, yapay zeka "
        "arka planı) izleyicilere tek bir webcam akışı olarak ulaşır."
    ),
}
