# -*- coding: utf-8 -*-
"""English content for cam-streaming-guides. One dict per platform."""

PLATFORMS_EN = [
    {
        "slug": "chaturbate", "name": "Chaturbate",
        "title": "How to Stream on Chaturbate with SplitCam — Free Guide",
        "desc": "Step-by-step guide to broadcast on Chaturbate using free SplitCam software — "
                "external RTMP encoder setup, scenes, overlays, no watermark.",
        "kw": "how to stream on chaturbate, chaturbate broadcasting software, chaturbate rtmp, "
              "chaturbate obs, stream to chaturbate",
        "h1html": 'How to stream on <span class="accent">Chaturbate</span> with SplitCam',
        "h1short": "Stream on Chaturbate",
        "card": "External encoder setup for Chaturbate broadcasts.",
        "intro": "Use free <strong style='color:var(--text)'>SplitCam</strong> as your Chaturbate "
                 "encoder — multi-camera scenes, overlays and filters that the built-in browser "
                 "broadcaster can't do. No watermark, no signup.",
        "quick": "To broadcast on Chaturbate with SplitCam: install SplitCam, build your scene, "
                 "enable external broadcasting in your Chaturbate broadcast settings, copy the RTMP "
                 "URL and stream key, paste them into SplitCam and click Go Live."
                 "<ol><li>Install SplitCam (free).</li><li>Add camera + scene.</li>"
                 "<li>Get the Chaturbate RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to Chaturbate and open your broadcast settings. Switch the broadcasting "
                   "method to <strong>external broadcaster / OBS</strong>. Chaturbate shows an "
                   "<strong>RTMP server URL</strong> and a <strong>stream key</strong> — copy both. "
                   "Keep the key private; anyone with it can stream to your room.",
        "tips": [
            ("Use a wired connection", "Ethernet beats Wi-Fi for stability. A dropped frame on a "
             "live cam stream is a dropped tip — keep the connection solid."),
            ("Layer overlays in SplitCam", "Add tip-goal text, your social handles and a logo as "
             "scene layers. The browser broadcaster can't; SplitCam can."),
            ("Run a private test first", "Do a short test broadcast to confirm camera, audio and "
             "framing before you open the room publicly."),
            ("Watch the health monitor", "SplitCam's status bar shows dropped frames and encoder "
             "load live. See red — lower the bitrate."),
        ],
        "faq": [
            ("Is SplitCam free for Chaturbate?", "Yes — 100% free, no watermark on your stream, "
             "no time limit. The full feature set is unlocked from first install."),
            ("Why use SplitCam instead of the Chaturbate browser broadcaster?",
             "The browser broadcaster is one camera, no overlays. SplitCam gives you multi-camera "
             "scenes, text overlays, filters, AI background and hardware encoding."),
            ("What bitrate should I use for Chaturbate?", "3,500–6,000 Kbps for 1080p, "
             "2,000–4,000 Kbps for 720p. Run SplitCam's speed test to confirm your upload first."),
            ("Can I stream to Chaturbate and other sites at once?", "Yes — SplitCam multistreaming "
             "sends one encode to several cam sites simultaneously. See the multi-platform guide."),
        ],
    },
    {
        "slug": "cam4", "name": "CAM4",
        "title": "How to Stream on CAM4 with SplitCam — Free Guide",
        "desc": "Broadcast on CAM4 using free SplitCam — external RTMP encoder, multi-camera "
                "scenes, overlays. Step-by-step, no watermark, no signup.",
        "kw": "how to stream on cam4, cam4 broadcasting software, cam4 rtmp, cam4 obs, stream to cam4",
        "h1html": 'How to stream on <span class="accent">CAM4</span> with SplitCam',
        "h1short": "Stream on CAM4",
        "card": "External encoder setup for CAM4 broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> works as your CAM4 "
                 "encoder — scenes, overlays, filters and hardware encoding the basic broadcaster "
                 "lacks. No watermark, no signup.",
        "quick": "To broadcast on CAM4 with SplitCam: install SplitCam, build your scene, enable "
                 "external/RTMP broadcasting in CAM4, copy the server URL and stream key, paste "
                 "them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the CAM4 RTMP key.</li><li>Paste it into SplitCam.</li><li>Go Live.</li></ol>",
        "key_how": "Sign in to CAM4 and open your broadcast / streaming settings. Choose the "
                   "<strong>external encoder (RTMP / OBS)</strong> option. CAM4 displays a "
                   "<strong>server URL</strong> and a <strong>stream key</strong> — copy both. "
                   "Treat the key like a password.",
        "tips": [
            ("Stabilise with ethernet", "A wired connection prevents the mid-show freezes that "
             "cost you viewers and tips."),
            ("Build branded overlays", "Add your name, goals and socials as SplitCam layers so "
             "every CAM4 viewer sees them."),
            ("Test before going public", "A private test broadcast catches audio and framing "
             "problems before the room is live."),
            ("Use hardware encoding", "SplitCam auto-detects NVENC / QuickSync / AMF — encoding "
             "runs on the GPU, keeping the PC responsive."),
        ],
        "faq": [
            ("Is SplitCam free for CAM4?", "Yes — fully free, no watermark, no time limit."),
            ("Does CAM4 support external broadcasting software?", "Yes — CAM4 accepts an RTMP "
             "stream key, so any RTMP encoder including SplitCam works."),
            ("What bitrate is best for CAM4?", "3,500–6,000 Kbps for 1080p. Confirm your upload "
             "with SplitCam's built-in speed test before going live."),
            ("Can I use two cameras on CAM4?", "Yes — add multiple cameras as scene sources in "
             "SplitCam and switch between them during the broadcast."),
        ],
    },
    {
        "slug": "bongacams", "name": "BongaCams",
        "title": "How to Stream on BongaCams with SplitCam — Free Guide",
        "desc": "Broadcast on BongaCams with free SplitCam — external RTMP encoder, multi-camera "
                "scenes and overlays. Step-by-step, no watermark.",
        "kw": "how to stream on bongacams, bongacams broadcasting software, bongacams rtmp, "
              "bongacams obs, stream to bongacams",
        "h1html": 'How to stream on <span class="accent">BongaCams</span> with SplitCam',
        "h1short": "Stream on BongaCams",
        "card": "External encoder setup for BongaCams broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> is your BongaCams "
                 "encoder — multi-camera scenes, overlays, AI background. No watermark, no signup.",
        "quick": "To broadcast on BongaCams with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in BongaCams, copy the server URL and stream "
                 "key, paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the BongaCams RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to BongaCams and open your broadcast settings. Select the "
                   "<strong>external software / RTMP</strong> broadcasting option. BongaCams shows "
                   "a <strong>server URL</strong> and a <strong>stream key</strong> — copy both and "
                   "keep the key private.",
        "tips": [
            ("Wired connection", "Ethernet keeps the stream stable through a long show."),
            ("Overlays viewers remember", "Tip goals, your name and socials as SplitCam layers "
             "build a recognisable channel."),
            ("Private test run", "Confirm camera, light and audio with a quick private test."),
            ("AI background", "No green screen needed — SplitCam removes or blurs your background "
             "for a cleaner shot."),
        ],
        "faq": [
            ("Is SplitCam free for BongaCams?", "Yes — fully free, no watermark, no limits."),
            ("Why not just use the BongaCams browser broadcaster?", "It is single-camera with no "
             "overlays. SplitCam adds scenes, overlays, filters and hardware encoding."),
            ("What bitrate for BongaCams?", "3,500–6,000 Kbps for 1080p; test your upload first."),
            ("Can I multistream BongaCams with other sites?", "Yes — SplitCam can broadcast to "
             "several cam sites from one encode."),
        ],
    },
    {
        "slug": "stripchat", "name": "Stripchat",
        "title": "How to Stream on Stripchat with SplitCam — Free Guide",
        "desc": "Broadcast on Stripchat with free SplitCam — external RTMP encoder, multi-camera "
                "scenes, overlays, filters. Step-by-step, no watermark.",
        "kw": "how to stream on stripchat, stripchat broadcasting software, stripchat rtmp, "
              "stripchat obs, stripchat live stream",
        "h1html": 'How to stream on <span class="accent">Stripchat</span> with SplitCam',
        "h1short": "Stream on Stripchat",
        "card": "External encoder setup for Stripchat broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> powers your Stripchat "
                 "broadcast — scenes, overlays, AI background and hardware encoding. No watermark.",
        "quick": "To broadcast on Stripchat with SplitCam: install SplitCam, build your scene, "
                 "enable external/OBS broadcasting in Stripchat, copy the RTMP URL and stream key, "
                 "paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the Stripchat RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Sign in to Stripchat and open your broadcasting settings. Choose the "
                   "<strong>OBS / external encoder</strong> method. Stripchat provides an "
                   "<strong>RTMP server URL</strong> and a <strong>stream key</strong> — copy both. "
                   "Never share the key.",
        "tips": [
            ("Ethernet over Wi-Fi", "A wired link prevents freezes during a long Stripchat show."),
            ("Layered overlays", "Add goals, name and socials as SplitCam scene layers."),
            ("Test privately", "Run a quick private broadcast to check audio and framing."),
            ("Beauty filters", "SplitCam's built-in filters and AI background sharpen the look "
             "with no extra hardware."),
        ],
        "faq": [
            ("Is SplitCam free for Stripchat?", "Yes — free, no watermark, no time limit."),
            ("Does Stripchat allow external encoders?", "Yes — Stripchat supports OBS-style RTMP "
             "broadcasting, so SplitCam works."),
            ("Best bitrate for Stripchat?", "3,500–6,000 Kbps at 1080p. Test your upload first."),
            ("Can I add a second camera on Stripchat?", "Yes — SplitCam supports multiple cameras "
             "as scene sources with hotkey switching."),
        ],
    },
    {
        "slug": "onlyfans", "name": "OnlyFans",
        "title": "How to Go Live on OnlyFans with SplitCam — Free Guide",
        "desc": "Go live on OnlyFans using free SplitCam — multi-camera scenes, overlays and "
                "filters via external encoder. Step-by-step, no watermark, no signup.",
        "kw": "how to go live on onlyfans, onlyfans live stream, onlyfans streaming software, "
              "onlyfans obs, onlyfans rtmp",
        "h1html": 'How to go live on <span class="accent">OnlyFans</span> with SplitCam',
        "h1short": "Go live on OnlyFans",
        "card": "External encoder setup for OnlyFans live streams.",
        "intro": "Use free <strong style='color:var(--text)'>SplitCam</strong> for your OnlyFans "
                 "live stream — multi-camera scenes, overlays and filters the basic in-app camera "
                 "can't match. No watermark, no signup.",
        "quick": "To go live on OnlyFans with SplitCam: install SplitCam, build your scene, start "
                 "a live stream on OnlyFans and open its streaming settings, copy the RTMP URL and "
                 "stream key, paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the OnlyFans RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "On OnlyFans, start a new live stream and open the <strong>streaming "
                   "settings</strong>. Choose the option to stream with external software — "
                   "OnlyFans shows an <strong>RTMP server URL</strong> and a <strong>stream "
                   "key</strong>. Copy both into SplitCam and keep the key private.",
        "tips": [
            ("Wired connection", "Ethernet keeps a paid OnlyFans live stream from freezing."),
            ("Brand your scene", "Add your handle and tip goals as overlays so clips of the "
             "stream stay recognisable."),
            ("Test before announcing", "Run a private test so the real live stream starts clean."),
            ("Use a second camera", "SplitCam lets you switch angles mid-stream — phone as a "
             "wireless second camera works too."),
        ],
        "faq": [
            ("Is SplitCam free for OnlyFans live streams?", "Yes — fully free, no watermark, no "
             "time limit."),
            ("Does OnlyFans support streaming software?", "Yes — OnlyFans live streaming accepts "
             "an RTMP stream key, so SplitCam and other encoders work."),
            ("What bitrate for OnlyFans?", "3,500–6,000 Kbps at 1080p. Run the speed test first."),
            ("Can I use overlays on an OnlyFans live stream?", "Yes — SplitCam applies overlays, "
             "text and filters live before the stream reaches OnlyFans."),
        ],
    },
    {
        "slug": "camplace", "name": "CamPlace",
        "title": "How to Stream on CamPlace with SplitCam — Free Guide",
        "desc": "Broadcast on CamPlace with free SplitCam — external RTMP encoder, scenes and "
                "overlays. Step-by-step, no watermark.",
        "kw": "how to stream on camplace, camplace broadcasting software, camplace rtmp, "
              "camplace obs",
        "h1html": 'How to stream on <span class="accent">CamPlace</span> with SplitCam',
        "h1short": "Stream on CamPlace",
        "card": "External encoder setup for CamPlace broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> is your CamPlace "
                 "encoder — scenes, overlays, filters and hardware encoding. No watermark.",
        "quick": "To broadcast on CamPlace with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in CamPlace, copy the server URL and stream "
                 "key, paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the CamPlace RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to CamPlace and open your broadcast settings. Select the "
                   "<strong>external encoder / RTMP</strong> option. CamPlace shows a "
                   "<strong>server URL</strong> and a <strong>stream key</strong> — copy both.",
        "tips": [
            ("Wired link", "Ethernet keeps the broadcast stable."),
            ("Overlays", "Add goals and socials as SplitCam scene layers."),
            ("Private test", "Check audio and framing before going public."),
            ("Hardware encoding", "SplitCam offloads encoding to the GPU automatically."),
        ],
        "faq": [
            ("Is SplitCam free for CamPlace?", "Yes — free, no watermark, no limits."),
            ("Does CamPlace accept external software?", "Yes — CamPlace supports RTMP encoders "
             "like SplitCam."),
            ("Bitrate for CamPlace?", "3,500–6,000 Kbps at 1080p; test your upload first."),
            ("Can I multistream CamPlace?", "Yes — SplitCam can send one encode to several sites."),
        ],
    },
    {
        "slug": "camsoda", "name": "CamSoda",
        "title": "How to Stream on CamSoda with SplitCam — Free Guide",
        "desc": "Broadcast on CamSoda with free SplitCam — external RTMP encoder, scenes, "
                "overlays, filters. Step-by-step, no watermark.",
        "kw": "how to stream on camsoda, camsoda live, camsoda broadcasting software, camsoda rtmp",
        "h1html": 'How to stream on <span class="accent">CamSoda</span> with SplitCam',
        "h1short": "Stream on CamSoda",
        "card": "External encoder setup for CamSoda broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> powers your CamSoda "
                 "broadcast — scenes, overlays, AI background. No watermark, no signup.",
        "quick": "To broadcast on CamSoda with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in CamSoda, copy the server URL and stream "
                 "key, paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the CamSoda RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Sign in to CamSoda and open your broadcast settings. Choose the "
                   "<strong>OBS / external encoder</strong> method. CamSoda shows an "
                   "<strong>RTMP URL</strong> and a <strong>stream key</strong> — copy both.",
        "tips": [
            ("Ethernet", "A wired connection prevents mid-show freezes."),
            ("Branded overlays", "Goals, name and socials as SplitCam layers."),
            ("Test privately", "Confirm camera and audio before opening the room."),
            ("Filters & AI background", "Built into SplitCam — no extra hardware."),
        ],
        "faq": [
            ("Is SplitCam free for CamSoda?", "Yes — free, no watermark, no time limit."),
            ("Does CamSoda support external encoders?", "Yes — CamSoda accepts RTMP, so SplitCam "
             "works as the encoder."),
            ("Best bitrate for CamSoda?", "3,500–6,000 Kbps at 1080p; run the speed test first."),
            ("Two cameras on CamSoda?", "Yes — add multiple cameras as scenes in SplitCam."),
        ],
    },
    {
        "slug": "streamate", "name": "Streamate",
        "title": "How to Stream on Streamate with SplitCam — Free Guide",
        "desc": "Broadcast on Streamate with free SplitCam — external RTMP encoder, scenes and "
                "overlays. Step-by-step, no watermark.",
        "kw": "how to stream on streamate, streamate broadcasting software, streamate rtmp, "
              "streamate obs",
        "h1html": 'How to stream on <span class="accent">Streamate</span> with SplitCam',
        "h1short": "Stream on Streamate",
        "card": "External encoder setup for Streamate broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> is your Streamate "
                 "encoder — multi-camera scenes, overlays and filters. No watermark.",
        "quick": "To broadcast on Streamate with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in Streamate, copy the server URL and stream "
                 "key, paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the Streamate RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to the Streamate broadcaster area and open your stream settings. Select "
                   "the <strong>external encoder / RTMP</strong> option. Streamate shows a "
                   "<strong>server URL</strong> and a <strong>stream key</strong> — copy both.",
        "tips": [
            ("Wired connection", "Ethernet keeps a Streamate show stable."),
            ("Overlays", "Add goals and socials as SplitCam scene layers."),
            ("Private test", "Catch audio and framing issues before going live."),
            ("Hardware encoding", "SplitCam uses NVENC / QuickSync / AMF automatically."),
        ],
        "faq": [
            ("Is SplitCam free for Streamate?", "Yes — free, no watermark, no limits."),
            ("Does Streamate allow external software?", "Yes — Streamate supports RTMP encoders."),
            ("Bitrate for Streamate?", "3,500–6,000 Kbps at 1080p; test upload first."),
            ("Can I multistream Streamate?", "Yes — SplitCam sends one encode to several sites."),
        ],
    },
    {
        "slug": "streamray", "name": "StreamRay",
        "title": "How to Stream on StreamRay with SplitCam — Free Guide",
        "desc": "Broadcast on StreamRay with free SplitCam — external RTMP encoder, scenes and "
                "overlays. Step-by-step, no watermark.",
        "kw": "how to stream on streamray, streamray cam, streamray broadcasting software, "
              "streamray rtmp",
        "h1html": 'How to stream on <span class="accent">StreamRay</span> with SplitCam',
        "h1short": "Stream on StreamRay",
        "card": "External encoder setup for StreamRay broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> powers your StreamRay "
                 "broadcast — scenes, overlays, filters, hardware encoding. No watermark.",
        "quick": "To broadcast on StreamRay with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in StreamRay, copy the server URL and stream "
                 "key, paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the StreamRay RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Sign in to StreamRay and open your broadcast settings. Select the "
                   "<strong>external encoder / RTMP</strong> option. StreamRay shows a "
                   "<strong>server URL</strong> and a <strong>stream key</strong> — copy both.",
        "tips": [
            ("Ethernet", "A wired link keeps the broadcast steady."),
            ("Overlays", "Goals, name and socials as SplitCam layers."),
            ("Private test", "Check the setup before opening the room."),
            ("AI background", "Clean background with no green screen."),
        ],
        "faq": [
            ("Is SplitCam free for StreamRay?", "Yes — free, no watermark, no time limit."),
            ("Does StreamRay support external encoders?", "Yes — StreamRay accepts RTMP."),
            ("Bitrate for StreamRay?", "3,500–6,000 Kbps at 1080p; test upload first."),
            ("Two cameras on StreamRay?", "Yes — SplitCam supports multiple camera sources."),
        ],
    },
    {
        "slug": "xlovecam", "name": "XLoveCam",
        "title": "How to Stream on XLoveCam with SplitCam — Free Guide",
        "desc": "Broadcast on XLoveCam with free SplitCam — external RTMP encoder, scenes and "
                "overlays. Step-by-step, no watermark.",
        "kw": "how to stream on xlovecam, xlovecam broadcasting software, xlovecam rtmp, x love cam",
        "h1html": 'How to stream on <span class="accent">XLoveCam</span> with SplitCam',
        "h1short": "Stream on XLoveCam",
        "card": "External encoder setup for XLoveCam broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> is your XLoveCam "
                 "encoder — scenes, overlays, AI background. No watermark, no signup.",
        "quick": "To broadcast on XLoveCam with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in XLoveCam, copy the server URL and stream "
                 "key, paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the XLoveCam RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to the XLoveCam model area and open your broadcast settings. Select the "
                   "<strong>external software / RTMP</strong> option. XLoveCam shows a "
                   "<strong>server URL</strong> and a <strong>stream key</strong> — copy both.",
        "tips": [
            ("Wired connection", "Ethernet keeps the stream stable."),
            ("Overlays", "Add goals and socials as SplitCam layers."),
            ("Private test", "Confirm audio and framing first."),
            ("Filters", "SplitCam's beauty filters and AI background built in."),
        ],
        "faq": [
            ("Is SplitCam free for XLoveCam?", "Yes — free, no watermark, no limits."),
            ("Does XLoveCam allow external encoders?", "Yes — XLoveCam supports RTMP broadcasting."),
            ("Bitrate for XLoveCam?", "3,500–6,000 Kbps at 1080p; test upload first."),
            ("Can I multistream XLoveCam?", "Yes — SplitCam can broadcast to several sites at once."),
        ],
    },
    {
        "slug": "soulcams", "name": "SoulCams",
        "title": "How to Stream on SoulCams with SplitCam — Free Guide",
        "desc": "Broadcast on SoulCams with free SplitCam — external RTMP encoder, scenes and "
                "overlays. Step-by-step, no watermark.",
        "kw": "how to stream on soulcams, soulcams broadcasting software, soulcams rtmp, soul cams",
        "h1html": 'How to stream on <span class="accent">SoulCams</span> with SplitCam',
        "h1short": "Stream on SoulCams",
        "card": "External encoder setup for SoulCams broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> powers your SoulCams "
                 "broadcast — scenes, overlays, filters. No watermark, no signup.",
        "quick": "To broadcast on SoulCams with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in SoulCams, copy the server URL and stream "
                 "key, paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the SoulCams RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Sign in to SoulCams and open your broadcast settings. Select the "
                   "<strong>external encoder / RTMP</strong> option. SoulCams shows a "
                   "<strong>server URL</strong> and a <strong>stream key</strong> — copy both.",
        "tips": [
            ("Ethernet", "Wired connection keeps the broadcast stable."),
            ("Overlays", "Goals and socials as SplitCam scene layers."),
            ("Private test", "Check the setup before going public."),
            ("Hardware encoding", "GPU encoding keeps the PC responsive."),
        ],
        "faq": [
            ("Is SplitCam free for SoulCams?", "Yes — free, no watermark, no limits."),
            ("Does SoulCams support external software?", "Yes — SoulCams accepts RTMP encoders."),
            ("Bitrate for SoulCams?", "3,500–6,000 Kbps at 1080p; test upload first."),
            ("Two cameras on SoulCams?", "Yes — SplitCam supports multiple camera sources."),
        ],
    },
    {
        "slug": "imlive", "name": "ImLive",
        "title": "How to Stream on ImLive with SplitCam — Free Guide",
        "desc": "Broadcast on ImLive with free SplitCam — external RTMP encoder, scenes and "
                "overlays. Step-by-step, no watermark.",
        "kw": "how to stream on imlive, imlive broadcasting software, imlive rtmp, im live stream",
        "h1html": 'How to stream on <span class="accent">ImLive</span> with SplitCam',
        "h1short": "Stream on ImLive",
        "card": "External encoder setup for ImLive broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> is your ImLive "
                 "encoder — scenes, overlays, AI background. No watermark.",
        "quick": "To broadcast on ImLive with SplitCam: install SplitCam, build your scene, enable "
                 "external/RTMP broadcasting in ImLive, copy the server URL and stream key, paste "
                 "them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the ImLive RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to the ImLive broadcaster area and open your stream settings. Select "
                   "the <strong>external encoder / RTMP</strong> option. ImLive shows a "
                   "<strong>server URL</strong> and a <strong>stream key</strong> — copy both.",
        "tips": [
            ("Wired link", "Ethernet keeps an ImLive show stable."),
            ("Overlays", "Goals and socials as SplitCam layers."),
            ("Private test", "Confirm audio and framing first."),
            ("AI background", "Clean look without a green screen."),
        ],
        "faq": [
            ("Is SplitCam free for ImLive?", "Yes — free, no watermark, no time limit."),
            ("Does ImLive support external encoders?", "Yes — ImLive accepts RTMP broadcasting."),
            ("Bitrate for ImLive?", "3,500–6,000 Kbps at 1080p; test upload first."),
            ("Can I multistream ImLive?", "Yes — SplitCam can broadcast to several sites at once."),
        ],
    },
    {
        "slug": "vxlive", "name": "VXLive",
        "title": "How to Stream on VXLive with SplitCam — Free Guide",
        "desc": "Broadcast on VXLive with free SplitCam — external RTMP encoder, scenes and "
                "overlays. Step-by-step, no watermark.",
        "kw": "how to stream on vxlive, vxlive broadcasting software, vxlive rtmp",
        "h1html": 'How to stream on <span class="accent">VXLive</span> with SplitCam',
        "h1short": "Stream on VXLive",
        "card": "External encoder setup for VXLive broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> powers your VXLive "
                 "broadcast — scenes, overlays, filters. No watermark, no signup.",
        "quick": "To broadcast on VXLive with SplitCam: install SplitCam, build your scene, enable "
                 "external/RTMP broadcasting in VXLive, copy the server URL and stream key, paste "
                 "them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the VXLive RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Sign in to VXLive and open your broadcast settings. Select the "
                   "<strong>external encoder / RTMP</strong> option. VXLive shows a "
                   "<strong>server URL</strong> and a <strong>stream key</strong> — copy both.",
        "tips": [
            ("Ethernet", "Wired connection keeps the broadcast stable."),
            ("Overlays", "Goals and socials as SplitCam scene layers."),
            ("Private test", "Check the setup before going public."),
            ("Hardware encoding", "SplitCam offloads encoding to the GPU."),
        ],
        "faq": [
            ("Is SplitCam free for VXLive?", "Yes — free, no watermark, no limits."),
            ("Does VXLive support external software?", "Yes — VXLive accepts RTMP encoders."),
            ("Bitrate for VXLive?", "3,500–6,000 Kbps at 1080p; test upload first."),
            ("Two cameras on VXLive?", "Yes — SplitCam supports multiple camera sources."),
        ],
    },
    {
        "slug": "virtwish", "name": "Virtwish",
        "title": "How to Stream on Virtwish with SplitCam — Free Guide",
        "desc": "Broadcast on Virtwish with free SplitCam — external RTMP encoder, scenes and "
                "overlays. Step-by-step, no watermark.",
        "kw": "how to stream on virtwish, virtwish broadcasting software, virtwish rtmp",
        "h1html": 'How to stream on <span class="accent">Virtwish</span> with SplitCam',
        "h1short": "Stream on Virtwish",
        "card": "External encoder setup for Virtwish broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> is your Virtwish "
                 "encoder — scenes, overlays, AI background. No watermark.",
        "quick": "To broadcast on Virtwish with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in Virtwish, copy the server URL and stream "
                 "key, paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the Virtwish RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to Virtwish and open your broadcast settings. Select the "
                   "<strong>external encoder / RTMP</strong> option. Virtwish shows a "
                   "<strong>server URL</strong> and a <strong>stream key</strong> — copy both.",
        "tips": [
            ("Wired link", "Ethernet keeps the broadcast stable."),
            ("Overlays", "Goals and socials as SplitCam layers."),
            ("Private test", "Confirm audio and framing first."),
            ("Filters", "Beauty filters and AI background built into SplitCam."),
        ],
        "faq": [
            ("Is SplitCam free for Virtwish?", "Yes — free, no watermark, no limits."),
            ("Does Virtwish support external encoders?", "Yes — Virtwish accepts RTMP."),
            ("Bitrate for Virtwish?", "3,500–6,000 Kbps at 1080p; test upload first."),
            ("Can I multistream Virtwish?", "Yes — SplitCam broadcasts to several sites at once."),
        ],
    },
    {
        "slug": "xmodels", "name": "XModels",
        "title": "How to Stream on XModels with SplitCam — Free Guide",
        "desc": "Broadcast on XModels with free SplitCam — external RTMP encoder, scenes and "
                "overlays. Step-by-step, no watermark.",
        "kw": "how to stream on xmodels, xmodels broadcasting software, xmodels rtmp",
        "h1html": 'How to stream on <span class="accent">XModels</span> with SplitCam',
        "h1short": "Stream on XModels",
        "card": "External encoder setup for XModels broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> powers your XModels "
                 "broadcast — scenes, overlays, filters. No watermark, no signup.",
        "quick": "To broadcast on XModels with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in XModels, copy the server URL and stream "
                 "key, paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the XModels RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Sign in to XModels and open your broadcast settings. Select the "
                   "<strong>external encoder / RTMP</strong> option. XModels shows a "
                   "<strong>server URL</strong> and a <strong>stream key</strong> — copy both.",
        "tips": [
            ("Ethernet", "Wired connection keeps the broadcast stable."),
            ("Overlays", "Goals and socials as SplitCam scene layers."),
            ("Private test", "Check the setup before going public."),
            ("Hardware encoding", "GPU encoding keeps the PC responsive."),
        ],
        "faq": [
            ("Is SplitCam free for XModels?", "Yes — free, no watermark, no limits."),
            ("Does XModels support external software?", "Yes — XModels accepts RTMP encoders."),
            ("Bitrate for XModels?", "3,500–6,000 Kbps at 1080p; test upload first."),
            ("Two cameras on XModels?", "Yes — SplitCam supports multiple camera sources."),
        ],
    },
    {
        "slug": "flirt4free", "name": "Flirt4Free",
        "title": "How to Stream on Flirt4Free with SplitCam — Free Guide",
        "desc": "Broadcast on Flirt4Free with free SplitCam — external RTMP encoder, scenes and "
                "overlays. Step-by-step, no watermark.",
        "kw": "how to stream on flirt4free, flirt for free cam, flirt4free broadcasting software, "
              "flirt4free rtmp",
        "h1html": 'How to stream on <span class="accent">Flirt4Free</span> with SplitCam',
        "h1short": "Stream on Flirt4Free",
        "card": "External encoder setup for Flirt4Free broadcasts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> is your Flirt4Free "
                 "encoder — scenes, overlays, AI background. No watermark.",
        "quick": "To broadcast on Flirt4Free with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in Flirt4Free, copy the server URL and stream "
                 "key, paste them into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the Flirt4Free RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to the Flirt4Free model area and open your broadcast settings. Select "
                   "the <strong>external encoder / RTMP</strong> option. Flirt4Free shows a "
                   "<strong>server URL</strong> and a <strong>stream key</strong> — copy both.",
        "tips": [
            ("Wired link", "Ethernet keeps the broadcast stable."),
            ("Overlays", "Goals and socials as SplitCam layers."),
            ("Private test", "Confirm audio and framing first."),
            ("Filters", "Beauty filters and AI background built into SplitCam."),
        ],
        "faq": [
            ("Is SplitCam free for Flirt4Free?", "Yes — free, no watermark, no limits."),
            ("Does Flirt4Free support external encoders?", "Yes — Flirt4Free accepts RTMP."),
            ("Bitrate for Flirt4Free?", "3,500–6,000 Kbps at 1080p; test upload first."),
            ("Can I multistream Flirt4Free?", "Yes — SplitCam broadcasts to several sites at once."),
        ],
    },
    {
        "slug": "mfc-alerts", "name": "MyFreeCams",
        "title": "How to Stream on MyFreeCams + Add Tip Alerts with SplitCam",
        "desc": "Broadcast on MyFreeCams with free SplitCam and show live tip alerts as an "
                "overlay. Step-by-step, no watermark.",
        "kw": "how to stream on myfreecams, mfc alerts, myfreecams broadcasting software, "
              "mfc broadcasting, myfreecams obs",
        "h1html": 'How to stream on <span class="accent">MyFreeCams</span> + tip alerts',
        "h1short": "Stream on MyFreeCams",
        "card": "Broadcast on MyFreeCams and add live tip alerts.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> is your MyFreeCams "
                 "encoder — and it can show <strong style='color:var(--text)'>live tip alerts</strong> "
                 "as a scene overlay using a Browser Source. No watermark.",
        "quick": "To broadcast on MyFreeCams with tip alerts: install SplitCam, build your scene, "
                 "add your MFC alerts page as a Browser Source overlay, get the MyFreeCams RTMP "
                 "key, paste it into SplitCam, click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Add MFC alerts as a Browser Source.</li><li>Paste the MFC RTMP key.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to MyFreeCams and open your broadcast settings. Select the "
                   "<strong>external encoder / RTMP</strong> option to get the <strong>server "
                   "URL</strong> and <strong>stream key</strong>. To show tip alerts, add your "
                   "MFC alerts/widget page as a <strong>Browser Source</strong> layer in SplitCam — "
                   "tips then pop up live on your stream.",
        "tips": [
            ("Browser Source for alerts", "Point a SplitCam Browser Source at your MFC alerts "
             "widget URL — tip notifications appear on the broadcast automatically."),
            ("Wired connection", "Ethernet keeps the show and the alert widget stable."),
            ("Position alerts carefully", "Place the alert overlay where it is visible but does "
             "not block your camera."),
            ("Private test", "Trigger a small test tip to confirm the alert overlay works."),
        ],
        "faq": [
            ("Is SplitCam free for MyFreeCams?", "Yes — free, no watermark, no limits."),
            ("How do MFC tip alerts work in SplitCam?", "Add your MFC alerts page as a Browser "
             "Source layer; SplitCam renders it live over your camera."),
            ("Does MyFreeCams support external encoders?", "Yes — MyFreeCams accepts RTMP "
             "broadcasting, so SplitCam works as the encoder."),
            ("Bitrate for MyFreeCams?", "3,500–6,000 Kbps at 1080p; test upload first."),
        ],
    },
    {
        "slug": "lovense", "name": "Lovense",
        "title": "How to Add a Lovense Toy to Your Stream with SplitCam",
        "desc": "Connect a Lovense interactive toy to your cam stream and show it on screen with "
                "free SplitCam. Step-by-step, no watermark.",
        "kw": "how to add lovense to stream, lovense cam stream, lovense splitcam, "
              "lovense interactive toy streaming",
        "h1html": 'How to add a <span class="accent">Lovense toy</span> to your stream',
        "h1short": "Add a Lovense toy",
        "card": "Connect a Lovense interactive toy to your cam stream.",
        "intro": "Run your cam stream through free <strong style='color:var(--text)'>SplitCam</strong> "
                 "and pair a <strong style='color:var(--text)'>Lovense</strong> interactive toy so it "
                 "reacts to tokens — with the connection status visible on screen.",
        "quick": "To add a Lovense toy to your stream: install SplitCam and Lovense software, pair "
                 "the toy, link Lovense to your cam platform, add the Lovense status as a Browser "
                 "Source overlay in SplitCam, then broadcast as usual."
                 "<ol><li>Install SplitCam.</li><li>Install &amp; pair Lovense software.</li>"
                 "<li>Link Lovense to your cam site.</li>"
                 "<li>Add the Lovense overlay in SplitCam.</li><li>Go Live.</li></ol>",
        "steps": [
            ("Install SplitCam",
             "SplitCam is free live-streaming software for Windows and macOS — it is the encoder "
             "that sends your video to your cam platform. Download and install it; no watermark."),
            ("Install and pair the Lovense software",
             "Install Lovense Connect / Lovense Stream (the official desktop app). Turn on your "
             "toy and pair it over Bluetooth so the app shows it connected."),
            ("Link Lovense to your cam platform",
             "In the Lovense app, connect your cam-site account so the toy reacts to tokens / tips "
             "from viewers. Most major cam platforms are supported by Lovense."),
            ("Add the Lovense overlay in SplitCam",
             "Lovense provides an overlay / widget URL. Add it as a <strong>Browser Source</strong> "
             "layer in your SplitCam scene so viewers see toy status and recent tips on screen."),
            ("Build your scene and Go Live",
             "Add your camera and any other overlays, paste your cam platform's RTMP key into "
             "SplitCam, and click <strong>Go Live</strong>. The toy reacts to tips in real time."),
        ],
        "tips": [
            ("Keep the toy charged", "A mid-show battery death kills the interactive part — "
             "charge fully before going live."),
            ("Test the token reaction", "Send a small test tip to confirm the toy reacts before "
             "the room is public."),
            ("Show the overlay", "A visible Lovense status overlay tells viewers tipping does "
             "something — it drives more tips."),
            ("Stable Bluetooth", "Keep the toy near the PC / Bluetooth adapter to avoid dropouts."),
        ],
        "faq": [
            ("Is SplitCam free for this?", "Yes — SplitCam is free with no watermark. The Lovense "
             "software is also free."),
            ("Does the toy connect to SplitCam directly?", "No — the toy pairs with the Lovense "
             "app; SplitCam just displays the Lovense overlay and broadcasts your camera."),
            ("Which cam sites support Lovense?", "Most major cam platforms integrate with Lovense "
             "for token-reactive toys — check the Lovense app for the current list."),
            ("Can I show recent tips on screen?", "Yes — add the Lovense widget URL as a Browser "
             "Source in SplitCam."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Multiple Cam Sites",
        "title": "How to Broadcast to Multiple Cam Sites at Once with SplitCam",
        "desc": "Stream to BongaCams, Chaturbate, CAM4, Stripchat and more at the same time with "
                "free SplitCam multistreaming. Step-by-step, no watermark.",
        "kw": "broadcast to multiple cam sites, multistream cam sites, stream to chaturbate and "
              "bongacams at once, cam multistreaming software",
        "h1html": 'How to broadcast to <span class="accent">multiple cam sites</span> at once',
        "h1short": "Multistream cam sites",
        "card": "Broadcast to several cam sites simultaneously.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> can broadcast one "
                 "encode to <strong style='color:var(--text)'>several cam sites at the same "
                 "time</strong> — BongaCams, Chaturbate, CAM4, Stripchat and more. No watermark.",
        "quick": "To broadcast to several cam sites at once: install SplitCam, build your scene, "
                 "get the RTMP server URL and stream key from each cam site, add them all in "
                 "SplitCam's multistream settings, click Go Live once."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get an RTMP key from each cam site.</li>"
                 "<li>Add all keys in SplitCam multistream.</li><li>Go Live once.</li></ol>",
        "steps": [
            ("Install SplitCam",
             "SplitCam is free live-streaming software for Windows and macOS with built-in "
             "multistreaming. Download and install it — no watermark, no signup."),
            ("Set up your camera and scene",
             "Open SplitCam, add your webcam and build your scene with overlays and filters. "
             "One scene feeds every destination."),
            ("Get an RTMP key from each cam site",
             "On each cam platform, enable external / RTMP broadcasting and copy its "
             "<strong>server URL</strong> and <strong>stream key</strong>. Repeat for every site "
             "you want to broadcast to."),
            ("Add every destination in SplitCam",
             "Open <strong>Stream Settings</strong> and add each cam site as a custom RTMP "
             "destination — paste its server URL and key. Tick all the ones you want live."),
            ("Click Go Live once",
             "Press <strong>Go Live</strong>. SplitCam sends your stream to every selected cam "
             "site simultaneously, peer-to-peer, from one encode — no extra fee."),
        ],
        "tips": [
            ("Mind your upload", "Multistreaming multiplies upload load. Each destination needs "
             "its own bitrate — make sure your connection can carry the total."),
            ("Wired connection", "Ethernet is essential when pushing several streams at once."),
            ("Check each platform's rules", "Some cam sites restrict simultaneous broadcasting "
             "elsewhere — confirm before you multistream."),
            ("Watch the health monitor", "SplitCam shows per-destination status — drop a site if "
             "your upload can't keep up."),
        ],
        "faq": [
            ("Is multistreaming free in SplitCam?", "Yes — multistreaming is built in and free, "
             "no per-destination fee, no watermark."),
            ("How many cam sites can I broadcast to at once?", "As many as your upload bandwidth "
             "supports — each destination consumes its own bitrate."),
            ("Does this use a cloud relay?", "No — SplitCam sends streams peer-to-peer directly "
             "from your PC to each platform's ingest server."),
            ("Will multistreaming slow my PC?", "Encoding is done once and reused; hardware "
             "encoding keeps CPU load low. Upload bandwidth is the real limit."),
        ],
    },
]
