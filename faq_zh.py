# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_ZH = {
    "common": [
        (
            "模特在 {name} 上能赚多少钱？",
            "在 {name} 上的收入取决于观众规模、直播时长和打赏情况。"
            "活跃的主播每月通常能拿到 $200–$3,000；顶级主播可达 "
            "$10,000 以上。你的分成比例遵循 {name} 的佣金政策——开播前"
            "请仔细查看模特协议。"
        ),
        (
            "{name} 对主播来说安全吗？",
            "{name} 在结算前会要求年龄和身份验证，这能保护模特免受"
            "欺诈。建议使用艺名，绝不在镜头前透露个人信息，开启地区屏蔽"
            "以隐藏所在地，并把每一位观众的请求都视为交易行为。SplitCam 的"
            "叠加层和 AI 背景也可以遮挡或替换你的真实环境。"
        ),
        (
            "在 {name} 注册模特需要哪些证件？",
            "{name} 通常需要政府签发的带照片身份证件（护照、驾照"
            "或身份证）、手持证件的自拍，以及税务/结算表格（美国用户 W-9，"
            "非美国用户 W-8BEN）。审核一般需要 24–72 小时；通过后当天即可开播。"
        ),
        (
            "我可以用手机在 {name} 上直播吗？",
            "{name} 通常提供手机主播 App 或移动网页版主播界面，但"
            "功能有限——没有叠加层、没有第二路摄像头、没有 AI 背景。如需"
            "完整的制作品质，请使用电脑配合 SplitCam 直播，并把手机作为"
            "第二路摄像头使用（SplitCam 支持来自手机的 IP 摄像头输入）。"
        ),
    ],
    "stream": (
        "{name} 支持 OBS 或外部编码器吗？",
        "支持——{name} 会在主播面板中提供 RTMP 服务器地址和推流密钥。"
        "把它们粘贴到 SplitCam 的 <strong>Stream Settings → Custom RTMP</strong>，"
        "设置 1920×1080、30 fps、4,000–5,000 Kbps 码率，然后点击 <strong>Go Live</strong>。"
        "通过 Custom RTMP 通道，你可以充分利用 SplitCam 的场景合成（多摄像头、叠加层、滤镜）。"
    ),
    "vcam": (
        "可以把 SplitCam 当作 {name} 的虚拟摄像头吗？",
        "可以——{name} 的直播在浏览器中运行，因此 SplitCam 会被识别为名为 "
        "<strong>\"SplitCam Video Driver\"</strong> 的网络摄像头。打开 {name} 主播页面，"
        "点击浏览器中的摄像头选择器，选择 SplitCam。你合成好的画面（叠加层、第二路摄像头、"
        "滤镜、AI 背景）会作为一路网络摄像头信号送达观众。"
    ),
}
