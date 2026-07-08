# -*- coding: utf-8 -*-
LOVENSE_METHODS_ZH = {
    "heading": "在 SplitCam 上配置 Lovense — 3 步搞定",
    "lead": "这与 Lovense 官方的三步配置完全一致。<strong>Cam Extension</strong> 读取你直播平台上的"
            "打赏，<strong>Lovense Connect</strong> 是连接你玩具的蓝牙桥梁，而 "
            "<strong>SplitCam Toolset</strong> 会把 Lovense 叠加层放进 SplitCam，再通过 RTMP 推流。"
            "全部免费；下载按钮会自动匹配你的系统。",
    "stage_word": "第",
    "get_label": "下载",
    "do_label": "然后",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "读取你直播平台上的打赏 — 安装到 Chrome 或 Edge。",
            "get": ["camext"],
            "steps": [
                "下载 Cam Extension 并解压。",
                "打开 <strong>chrome://extensions</strong>（或 <strong>edge://extensions</strong>），"
                "在右上角开启 <strong>Developer mode</strong>，点击 <strong>Load unpacked</strong>，"
                "然后选择解压出的 <em>lovense_cam</em> 文件夹。",
                "点击工具栏中的 Lovense 图标，用你的 Lovense 账号登录。",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "通过蓝牙与你玩具通讯的桥梁。",
            "get": ["connect"],
            "steps": [
                "在电脑上：安装 Lovense Connect（推荐搭配 Lovense USB 蓝牙适配器）。在手机上："
                "从 Google Play 或 App Store 获取 Lovense Connect 应用。",
                "打开你的玩具并在 Connect 中配对，直到显示已连接。在手机应用上扫描电脑上显示的 "
                "QR 码即可将两者关联。",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "在 SplitCam 中显示 Lovense 叠加层并推送你的直播。",
            "get": ["splitcam", "toolset"],
            "steps": [
                "安装 SplitCam，然后安装 Lovense SplitCam Toolset —— 这个插件会把 Lovense 叠加层"
                "添加到 SplitCam 中。",
                "在 Cam Extension 中，点击 <strong>+</strong> 添加你的直播平台（Chaturbate、"
                "Stripchat 等）并设置打赏菜单，然后打开 <strong>Video Feedback</strong> 标签页，"
                "从列表（OBS / SplitCam / Streamster）中选择 <strong>SplitCam</strong>。",
                "在 SplitCam 中，添加 Toolset 注册的 <strong>Lovense</strong> 源 —— 打赏菜单／"
                "玩具状态叠加层就会出现在你的场景中。把它放在其他图层之上。",
                "添加你的摄像头，把直播平台的 RTMP 密钥粘贴到 SplitCam 的 <strong>Stream "
                "Settings</strong> 里，然后点击 <strong>Go Live</strong> —— 叠加层和玩具会随打赏做出反应。",
            ],
        },
    ],
}
