# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_KO = {
    "common": [
        (
            "{name}에서 모델은 얼마나 벌 수 있나요?",
            "{name}에서의 수입은 시청자 규모, 방송 시간, 팁 문화에 따라 달라집니다. "
            "활발한 방송인은 보통 월 $200~$3,000을 가져가며, 상위권은 $10,000 이상을 "
            "벌기도 합니다. 수익 배분은 {name}의 수수료 구조를 따르므로, 라이브 시작 "
            "전에 모델 계약서를 반드시 확인하세요."
        ),
        (
            "{name}은(는) 방송인에게 안전한가요?",
            "{name}은(는) 지급 전에 연령 및 신분 확인을 요구하므로 모델을 사기로부터 "
            "보호합니다. 활동명을 사용하고, 카메라 앞에서 개인 정보를 절대 공유하지 말며, "
            "지역 차단을 활성화해 본인이 거주하는 지역에서 방송이 보이지 않도록 하고, "
            "모든 시청자 요청을 거래로 다루세요. SplitCam의 오버레이와 AI 배경 기능을 "
            "사용하면 실제 주변 환경을 가리거나 교체할 수도 있습니다."
        ),
        (
            "{name}에서 모델이 되려면 어떤 서류가 필요한가요?",
            "{name}은(는) 일반적으로 정부 발급 사진 신분증(여권, 운전면허증 또는 신분증), "
            "신분증을 들고 찍은 셀카, 그리고 세금/지급 양식(미국은 W-9, 미국 외 지역은 "
            "W-8BEN)을 요구합니다. 승인까지 보통 24~72시간이 걸리며, 승인되면 당일에 "
            "바로 라이브를 시작할 수 있습니다."
        ),
        (
            "휴대폰으로 {name}에 방송할 수 있나요?",
            "{name}은(는) 보통 모바일 방송 앱이나 모바일 웹 방송 기능을 제공하지만, "
            "오버레이, 보조 카메라, AI 배경이 없는 등 기능이 제한적입니다. 완전한 "
            "제작 품질을 원한다면 컴퓨터에서 SplitCam으로 방송하고, 휴대폰을 보조 "
            "카메라로 사용하세요(SplitCam은 휴대폰에서 IP 카메라 입력을 받을 수 있습니다)."
        ),
    ],
    "stream": (
        "{name}은(는) OBS나 외부 인코더를 지원하나요?",
        "네 — {name}은(는) 방송인 패널에서 RTMP 서버 URL과 스트림 키를 제공합니다. "
        "둘 다 SplitCam의 <strong>Stream Settings → Custom RTMP</strong>에 붙여 넣고, "
        "1920×1080, 30fps, 4,000~5,000 Kbps 비트레이트로 설정한 뒤 <strong>Go Live</strong>를 "
        "클릭하세요. Custom RTMP 경로를 사용하면 SplitCam의 모든 장면 구성 기능"
        "(멀티 카메라, 오버레이, 필터)을 그대로 활용할 수 있습니다."
    ),
    "vcam": (
        "{name}에서 SplitCam을 가상 카메라로 사용할 수 있나요?",
        "네 — {name}의 라이브는 브라우저에서 실행되므로, SplitCam은 "
        "<strong>\"SplitCam Video Driver\"</strong>라는 이름의 웹캠으로 인식됩니다. "
        "{name} 방송인 패널을 열고 브라우저의 카메라 선택기를 클릭한 뒤 SplitCam을 "
        "고르세요. 구성한 장면(오버레이, 보조 카메라, 필터, AI 배경)이 하나의 웹캠 "
        "피드로 시청자에게 전달됩니다."
    ),
}
