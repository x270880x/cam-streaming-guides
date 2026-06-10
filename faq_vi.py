# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_VI = {
    "common": [
        (
            "Người mẫu có thể kiếm được bao nhiêu trên {name}?",
            "Thu nhập trên {name} phụ thuộc vào quy mô khán giả, số giờ phát trực tiếp và thói quen "
            "tip của người xem. Các broadcaster hoạt động thường xuyên kiếm được 200–3.000 USD mỗi "
            "tháng; những người dẫn đầu đạt mức 10.000 USD trở lên. Tỷ lệ chia doanh thu của bạn "
            "tuân theo cơ cấu hoa hồng của {name} — hãy đọc kỹ thỏa thuận người mẫu trước khi lên sóng."
        ),
        (
            "{name} có an toàn cho broadcaster không?",
            "{name} yêu cầu xác minh tuổi và giấy tờ tùy thân trước khi thanh toán, điều này bảo vệ "
            "người mẫu khỏi gian lận. Hãy dùng nghệ danh, không bao giờ chia sẻ dữ liệu cá nhân "
            "trước camera, bật chặn theo khu vực địa lý để ẩn luồng phát của bạn khỏi vùng nhà mình, "
            "và xem mọi yêu cầu của người xem như một giao dịch. Lớp phủ overlay và nền AI của "
            "SplitCam cũng có thể che giấu hoặc thay thế khung cảnh thực của bạn."
        ),
        (
            "Tôi cần những giấy tờ gì để trở thành người mẫu trên {name}?",
            "{name} thường yêu cầu giấy tờ tùy thân có ảnh do chính phủ cấp (hộ chiếu, bằng lái xe "
            "hoặc CMND/CCCD), một ảnh selfie cầm giấy tờ đó, và biểu mẫu thuế/thanh toán (W-9 cho "
            "Mỹ, W-8BEN cho ngoài Mỹ). Việc phê duyệt thường mất 24–72 giờ; sau khi được duyệt bạn "
            "có thể lên sóng ngay trong ngày."
        ),
        (
            "Tôi có thể phát trực tiếp trên {name} từ điện thoại không?",
            "{name} thường cung cấp ứng dụng broadcaster di động hoặc trình broadcaster trên "
            "mobile-web, nhưng trải nghiệm bị giới hạn — không có overlay, không camera thứ hai, "
            "không nền AI. Để đạt chất lượng sản xuất đầy đủ, hãy phát từ máy tính với SplitCam và "
            "dùng điện thoại làm camera thứ hai (SplitCam chấp nhận đầu vào IP-camera từ điện thoại)."
        ),
    ],
    "stream": (
        "{name} có hỗ trợ OBS hoặc bộ mã hóa bên ngoài không?",
        "Có — {name} cung cấp URL máy chủ RTMP và stream key trong bảng điều khiển broadcaster. "
        "Dán cả hai vào <strong>Stream Settings → Custom RTMP</strong> của SplitCam, đặt 1920×1080 "
        "ở 30 fps với bitrate 4.000–5.000 Kbps, và nhấn <strong>Go Live</strong>. Tuyến Custom "
        "RTMP cho bạn toàn bộ khả năng dựng cảnh của SplitCam (đa camera, overlay, bộ lọc)."
    ),
    "vcam": (
        "Tôi có thể dùng SplitCam làm camera ảo trên {name} không?",
        "Có — bản phát trực tiếp của {name} chạy trong trình duyệt, nên SplitCam được nhận dạng "
        "như một webcam có tên <strong>\"SplitCam Video Driver\"</strong>. Mở trang broadcaster "
        "của {name}, nhấn vào bộ chọn camera trong trình duyệt, và chọn SplitCam. Cảnh đã dựng của "
        "bạn (overlay, camera thứ hai, bộ lọc, nền AI) sẽ đến với người xem dưới dạng một luồng "
        "webcam duy nhất."
    ),
}
