# -*- coding: utf-8 -*-
LOVENSE_METHODS_VI = {
        "heading": "Cài đặt Lovense trên SplitCam — 3 bước",
        "lead": "Quy trình này giống hệt ba bước cài đặt của chính Lovense. <strong>Cam Extension</strong> "
                "đọc tiền tip từ trang cam của bạn, <strong>Lovense Connect</strong> là cầu nối Bluetooth "
                "tới đồ chơi, còn <strong>SplitCam Toolset</strong> đưa lớp phủ Lovense vào bên trong "
                "SplitCam để phát qua RTMP. Tất cả đều miễn phí; các nút tải tự động khớp với hệ điều hành "
                "của bạn.",
        "stage_word": "Bước",
        "get_label": "Tải về",
        "do_label": "Sau đó",
        "stages": [
            {
                "title": "Lovense Cam Extension",
                "role": "Đọc tiền tip từ trang cam của bạn — cài vào Chrome hoặc Edge.",
                "get": ["camext"],
                "steps": [
                    "Tải Cam Extension về và giải nén.",
                    "Mở <strong>chrome://extensions</strong> (hoặc <strong>edge://extensions</strong>), "
                    "bật <strong>Developer mode</strong> ở góc trên bên phải, nhấn <strong>Load unpacked</strong> "
                    "rồi chọn thư mục <em>lovense_cam</em> vừa giải nén.",
                    "Nhấn biểu tượng Lovense trên thanh công cụ và đăng nhập bằng tài khoản Lovense của bạn.",
                ],
            },
            {
                "title": "Lovense Connect",
                "role": "Cầu nối giao tiếp với đồ chơi của bạn qua Bluetooth.",
                "get": ["connect"],
                "steps": [
                    "Trên máy tính: cài Lovense Connect (nên dùng bộ chuyển Bluetooth USB của Lovense). "
                    "Trên điện thoại: tải ứng dụng Lovense Connect từ Google Play hoặc App Store.",
                    "Bật đồ chơi lên và ghép nối trong Connect cho tới khi hiện trạng thái đã kết nối. Trên "
                    "ứng dụng điện thoại, quét mã QR hiển thị trên máy tính để liên kết chúng.",
                ],
            },
            {
                "title": "SplitCam + Toolset",
                "role": "Hiển thị lớp phủ Lovense trong SplitCam và phát luồng của bạn.",
                "get": ["splitcam", "toolset"],
                "steps": [
                    "Cài SplitCam, sau đó cài Lovense SplitCam Toolset — plugin thêm lớp phủ Lovense "
                    "vào SplitCam.",
                    "Trong Cam Extension, nhấn <strong>+</strong> để thêm trang cam của bạn (Chaturbate, "
                    "Stripchat, …) và thiết lập menu tip, rồi mở thẻ <strong>Video Feedback</strong> "
                    "và chọn <strong>SplitCam</strong> trong danh sách (OBS / SplitCam / Streamster).",
                    "Trong SplitCam, thêm nguồn <strong>Lovense</strong> mà Toolset đã đăng ký — lớp phủ "
                    "menu tip / trạng thái đồ chơi sẽ xuất hiện trên cảnh của bạn. Giữ nó nằm trên các lớp khác.",
                    "Thêm camera của bạn, dán khóa RTMP của trang cam vào <strong>Stream Settings</strong> "
                    "trong SplitCam, rồi nhấn <strong>Go Live</strong> — lớp phủ và đồ chơi phản ứng theo tiền tip.",
                ],
            },
        ],
}
