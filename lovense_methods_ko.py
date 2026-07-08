# -*- coding: utf-8 -*-
LOVENSE_METHODS_KO = {
    "heading": "SplitCam에서 Lovense 설정하기 — 3단계",
    "lead": "이 과정은 Lovense 공식 3단계 설정을 그대로 따릅니다. <strong>Cam Extension</strong>은 "
            "캠 사이트의 팁을 읽어오고, <strong>Lovense Connect</strong>는 토이와 연결되는 "
            "Bluetooth 브리지이며, <strong>SplitCam Toolset</strong>은 Lovense 오버레이를 "
            "SplitCam 안에 넣어 RTMP로 송출합니다. 모두 무료이며, 다운로드 버튼은 사용자의 "
            "시스템에 맞게 자동으로 표시됩니다.",
    "stage_word": "단계",
    "get_label": "다운로드",
    "do_label": "다음",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "캠 사이트의 팁을 읽어옵니다 — Chrome 또는 Edge에 설치됩니다.",
            "get": ["camext"],
            "steps": [
                "Cam Extension을 다운로드하고 압축을 해제하세요.",
                "<strong>chrome://extensions</strong>(또는 <strong>edge://extensions</strong>)를 "
                "열고, 오른쪽 상단의 <strong>Developer mode</strong>를 켠 다음 <strong>Load unpacked</strong>를 "
                "클릭하여 압축 해제한 <em>lovense_cam</em> 폴더를 선택하세요.",
                "툴바의 Lovense 아이콘을 클릭하고 Lovense 계정으로 로그인하세요.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Bluetooth를 통해 토이와 통신하는 브리지입니다.",
            "get": ["connect"],
            "steps": [
                "컴퓨터에서는 Lovense Connect를 설치하세요(Lovense USB Bluetooth 어댑터 사용을 "
                "권장합니다). 휴대폰에서는 Google Play 또는 App Store에서 Lovense Connect 앱을 받으세요.",
                "토이를 켜고 Connect에서 연결됨 상태가 표시될 때까지 페어링하세요. 휴대폰 앱에서는 "
                "컴퓨터에 표시된 QR 코드를 스캔하여 서로 연결하세요.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "SplitCam에 Lovense 오버레이를 표시하고 스트림을 송출합니다.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "SplitCam을 설치한 다음, Lovense SplitCam Toolset을 설치하세요 — SplitCam에 "
                "Lovense 오버레이를 추가해 주는 플러그인입니다.",
                "Cam Extension에서 <strong>+</strong>를 클릭해 캠 사이트(Chaturbate, Stripchat 등)를 "
                "추가하고 팁 메뉴를 설정한 다음, <strong>Video Feedback</strong> 탭을 열고 목록"
                "(OBS / SplitCam / Streamster)에서 <strong>SplitCam</strong>을 선택하세요.",
                "SplitCam에서 Toolset이 등록한 <strong>Lovense</strong> 소스를 추가하면 팁 메뉴 / "
                "토이 상태 오버레이가 장면에 나타납니다. 다른 레이어보다 위에 유지하세요.",
                "카메라를 추가하고, 캠 사이트의 RTMP 키를 SplitCam의 <strong>Stream Settings</strong>에 "
                "붙여넣은 다음 <strong>Go Live</strong>를 클릭하세요 — 오버레이와 토이가 팁에 반응합니다.",
            ],
        },
    ],
}
