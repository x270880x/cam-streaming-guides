# -*- coding: utf-8 -*-
"""English content for cam-streaming-guides. One dict per platform.

Content is genuinely per-platform (real in-platform paths, platform quirks,
distinct intros/FAQ) so each page is unique — not a name-swapped duplicate.
Sources: original splitcam.com help pages + platform specifics.
"""

# shared general tips/faq reused sparingly (most content is per-platform)
_T_ETH = ("Use a wired connection", "Ethernet beats Wi-Fi for a long live show — a dropped "
          "frame is a dropped tip. Run a cable to the streaming PC.")
_T_TEST = ("Run a private test first", "Do a short test broadcast to check camera, audio, "
           "framing and overlays before you open the room publicly.")

PLATFORMS_EN = [
    {
        "slug": "chaturbate", "name": "Chaturbate",
        "title": "How to Stream on Chaturbate with SplitCam — Token & RTMP Setup",
        "desc": "Broadcast on Chaturbate with free SplitCam. Find your broadcast token via "
                "Broadcast Yourself, route the external encoder through SplitCam — scenes, "
                "overlays, no watermark.",
        "kw": "how to stream on chaturbate, chaturbate broadcast token, chaturbate rtmp obs, "
              "chaturbate external encoder, stream to chaturbate",
        "h1html": 'How to stream on <span class="accent">Chaturbate</span> with SplitCam',
        "h1short": "Stream on Chaturbate",
        "card": "Token-based external encoder setup for Chaturbate.",
        "intro": "Chaturbate is one of the biggest cam platforms, built on a token economy. Its "
                 "browser broadcaster is a single plain camera — routing through the "
                 "<strong style='color:var(--text)'>external encoder</strong> option with free "
                 "<strong style='color:var(--text)'>SplitCam</strong> unlocks multi-camera "
                 "scenes, overlays and filters on the same token-based stream.",
        "quick": "Broadcast on Chaturbate with SplitCam: install SplitCam, build your scene, open "
                 "<em>Broadcast Yourself → My Broadcast</em> on Chaturbate, copy your broadcast "
                 "token, paste it into SplitCam and click Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Copy your Chaturbate broadcast token.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "On Chaturbate, click <strong>Broadcast Yourself</strong> to open the "
                   "<strong>My Broadcast</strong> page, then click <strong>View RTMP/OBS "
                   "broadcast information and stream key</strong>. Your key is shown as your "
                   "<strong>broadcast token</strong> — copy it. It works like a password; never "
                   "post it publicly.",
        "tips": [
            ("Your token is the key", "Chaturbate uses your broadcast token in place of a "
             "generic stream key. Treat it like a password — reset it if it ever leaks."),
            ("Use SplitCam's recommended preset", "Chaturbate's guide points at a recommended "
             "preset — SplitCam's auto settings match it, so you rarely need to tune manually."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Does Chaturbate allow OBS / external encoders?", "Yes — Chaturbate exposes RTMP/OBS "
             "broadcast info and a token under Broadcast Yourself, so SplitCam works as the "
             "encoder."),
            ("Where is my Chaturbate stream key?", "Broadcast Yourself → My Broadcast → View "
             "RTMP/OBS broadcast information and stream key. The key is your broadcast token."),
            ("Is SplitCam free for Chaturbate?", "Yes — 100% free, no watermark on the stream, "
             "no time limit."),
            ("What bitrate for Chaturbate?", "3,500–6,000 Kbps at 1080p. Run SplitCam's speed "
             "test to confirm your upload first."),
        ],
    },
    {
        "slug": "cam4", "name": "CAM4",
        "title": "How to Stream on CAM4 with SplitCam — External Encoder Setup",
        "desc": "Broadcast on CAM4 with free SplitCam. Open Broadcast & Earn Money, use the "
                "External Encoder, Get Stream Key, set geo-restrictions — scenes and overlays, "
                "no watermark.",
        "kw": "how to stream on cam4, cam4 external encoder, cam4 get stream key, cam4 rtmp obs, "
              "cam4 broadcast",
        "h1html": 'How to stream on <span class="accent">CAM4</span> with SplitCam',
        "h1short": "Stream on CAM4",
        "card": "External Encoder setup for CAM4, with geo-controls.",
        "intro": "CAM4 is a global cam-and-earn platform with built-in geo-controls — you can "
                 "hide your broadcast in chosen countries. Streaming through free "
                 "<strong style='color:var(--text)'>SplitCam</strong> as the external encoder "
                 "adds scene switching and overlays the basic broadcaster can't do.",
        "quick": "Broadcast on CAM4 with SplitCam: install SplitCam, build your scene, on CAM4 "
                 "open <em>Broadcast &amp; Earn Money → Start Broadcast → External Encoder</em>, "
                 "Get Stream Key, paste it into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the CAM4 stream key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "On CAM4, click <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn "
                   "Money</strong> → <strong>Start Broadcast</strong>, then click "
                   "<strong>External Encoder</strong> at the top. Fill in date of birth, gender "
                   "and country, then use <strong>Get Stream Key</strong> and copy it. A green "
                   "slider in SplitCam's Stream Settings confirms the connection.",
        "tips": [
            ("Set your geo-restrictions", "CAM4 lets you hide your broadcast in specific "
             "countries and regions — set this on CAM4's side before going live if you need it."),
            ("Watch for the green slider", "CAM4's setup shows a green slider in SplitCam Stream "
             "Settings when the key is accepted — red means re-check the key."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Can I geo-block my CAM4 broadcast?", "Yes — CAM4 has built-in geo-restriction to "
             "hide your broadcast in certain countries. It's set on CAM4, not in SplitCam."),
            ("Where is the CAM4 stream key?", "Broadcast → Broadcast & Earn Money → Start "
             "Broadcast → External Encoder → Get Stream Key."),
            ("Is SplitCam free for CAM4?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for CAM4?", "3,500–6,000 Kbps at 1080p; test your upload first."),
        ],
    },
    {
        "slug": "bongacams", "name": "BongaCams",
        "title": "How to Stream on BongaCams with SplitCam — External Encoder",
        "desc": "Broadcast on BongaCams with free SplitCam. Open Broadcast settings → Select "
                "Encoder → External Encoder. If the button is missing, support enables it.",
        "kw": "how to stream on bongacams, bongacams external encoder, bongacams rtmp obs, "
              "bongacams broadcast settings",
        "h1html": 'How to stream on <span class="accent">BongaCams</span> with SplitCam',
        "h1short": "Stream on BongaCams",
        "card": "External Encoder setup for BongaCams.",
        "intro": "BongaCams is a global cam platform. External-encoder streaming there isn't "
                 "always on by default — once it's enabled, free "
                 "<strong style='color:var(--text)'>SplitCam</strong> drives the broadcast with "
                 "multi-camera scenes, overlays and AI background.",
        "quick": "Broadcast on BongaCams with SplitCam: install SplitCam, build your scene, on "
                 "BongaCams open <em>Options → Broadcast settings → Select Encoder → External "
                 "Encoder</em>, copy the URL and key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the BongaCams encoder URL + key.</li><li>Paste into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "On BongaCams, open <strong>Options</strong> → <strong>Broadcast "
                   "settings</strong> → <strong>Select Encoder</strong> → <strong>External "
                   "Encoder</strong>, and copy the server URL and stream key shown. "
                   "<strong>If the External Encoder button isn't there</strong>, contact "
                   "BongaCams support and ask them to enable external encoding for your account.",
        "tips": [
            ("No External Encoder button? Ask support", "BongaCams gates external encoding — if "
             "the option is missing in Broadcast settings, support has to switch it on for you."),
            ("Match your resolution", "BongaCams recommends your webcam resolution and stream "
             "resolution match — e.g. set both to 1280×720."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Why is the External Encoder button missing on BongaCams?", "External encoding is "
             "not enabled by default for every account — contact BongaCams support to activate "
             "it, then the button appears in Broadcast settings."),
            ("Does BongaCams support OBS-style streaming?", "Yes — via the External Encoder "
             "option, so SplitCam works once it's enabled."),
            ("Is SplitCam free for BongaCams?", "Yes — free, no watermark, no limits."),
            ("What bitrate for BongaCams?", "3,500–6,000 Kbps at 1080p; test upload first."),
        ],
    },
    {
        "slug": "stripchat", "name": "Stripchat",
        "title": "How to Stream on Stripchat with SplitCam — External Software Setup",
        "desc": "Broadcast on Stripchat with free SplitCam. Switch to external software, copy "
                "the token-based stream key, run scenes and overlays. No watermark.",
        "kw": "how to stream on stripchat, stripchat external software, stripchat stream key, "
              "stripchat rtmp obs, stripchat live stream",
        "h1html": 'How to stream on <span class="accent">Stripchat</span> with SplitCam',
        "h1short": "Stream on Stripchat",
        "card": "External-software setup for Stripchat broadcasts.",
        "intro": "Stripchat is a large, interactivity-focused cam platform. Its <em>external "
                 "software</em> mode hands you a token-based key — feed it into free "
                 "<strong style='color:var(--text)'>SplitCam</strong> to broadcast with scenes, "
                 "overlays and filters instead of a single flat camera.",
        "quick": "Broadcast on Stripchat with SplitCam: install SplitCam, build your scene, on "
                 "Stripchat choose <em>Switch to external software</em>, copy the stream key, "
                 "paste it into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the Stripchat stream key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "On Stripchat, choose <strong>Switch to external software</strong>, then open "
                   "<strong>Show external software settings for the stream</strong>. Copy the "
                   "stream key — Stripchat shows it as a token. Keep it private.",
        "tips": [
            ("The key is a token", "Stripchat's stream key is a token — copy it exactly and "
             "never share it; reset it if it leaks."),
            ("Match your resolution", "Stripchat recommends webcam and stream resolution match — "
             "e.g. both at 1280×720."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("How do I switch Stripchat to external software?", "In your broadcast view choose "
             "Switch to external software, then open the external software settings to reveal "
             "the stream key."),
            ("Does Stripchat allow OBS / SplitCam?", "Yes — the external-software mode accepts "
             "any RTMP encoder, SplitCam included."),
            ("Is SplitCam free for Stripchat?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for Stripchat?", "3,500–6,000 Kbps at 1080p; test upload first."),
        ],
    },
    {
        "slug": "onlyfans", "name": "OnlyFans",
        "title": "How to Go Live on OnlyFans with SplitCam — OBS Key Setup",
        "desc": "Go live on OnlyFans with free SplitCam. Find the OBS Key under Settings → "
                "Other, route it through SplitCam for multi-camera scenes and overlays.",
        "kw": "how to go live on onlyfans, onlyfans obs key, onlyfans live stream, "
              "onlyfans streaming software, onlyfans rtmp",
        "h1html": 'How to go live on <span class="accent">OnlyFans</span> with SplitCam',
        "h1short": "Go live on OnlyFans",
        "card": "OBS Key setup for OnlyFans live streams.",
        "intro": "OnlyFans live streaming runs for your subscribers, and the platform exposes a "
                 "single <strong style='color:var(--text)'>OBS Key</strong> — no separate server "
                 "URL. Free <strong style='color:var(--text)'>SplitCam</strong> turns that key "
                 "into a real production: multi-camera scenes, overlays and filters.",
        "quick": "Go live on OnlyFans with SplitCam: install SplitCam, build your scene, on "
                 "OnlyFans open <em>Profile → Settings → Other</em>, copy the OBS Key, paste it "
                 "into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Copy your OnlyFans OBS Key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "On OnlyFans, go to <strong>Profile</strong> → <strong>Settings</strong> → the "
                   "<strong>Other</strong> section. Copy the value in the <strong>OBS Key</strong> "
                   "field. OnlyFans gives only this key — there is no separate RTMP server URL to "
                   "copy, so leave the SplitCam server field as its default if no URL is needed.",
        "tips": [
            ("Only an OBS Key, no server URL", "Unlike most cam sites, OnlyFans exposes just an "
             "OBS Key under Settings → Other — don't go hunting for a server URL."),
            ("Brand the stream for clips", "Add your handle and goals as overlays — clips of an "
             "OnlyFans live stream stay recognisable when reshared."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Where is the OnlyFans OBS Key?", "Profile → Settings → the Other section — the "
             "field is labelled OBS Key."),
            ("Does OnlyFans support streaming software?", "Yes — OnlyFans live streaming accepts "
             "an OBS-style key, so SplitCam works as the encoder."),
            ("Is SplitCam free for OnlyFans live streams?", "Yes — free, no watermark, no limit."),
            ("What bitrate for OnlyFans?", "3,500–6,000 Kbps at 1080p; run the speed test first."),
        ],
    },
    {
        "slug": "camplace", "name": "CamPlace",
        "title": "How to Stream on CamPlace with SplitCam — Free Setup Guide",
        "desc": "Broadcast on CamPlace with free SplitCam — external encoder, multi-camera "
                "scenes, overlays and filters. Step-by-step, no watermark.",
        "kw": "how to stream on camplace, camplace broadcasting software, camplace rtmp, "
              "camplace external encoder",
        "h1html": 'How to stream on <span class="accent">CamPlace</span> with SplitCam',
        "h1short": "Stream on CamPlace",
        "card": "External encoder setup for CamPlace broadcasts.",
        "intro": "CamPlace is a cam-streaming platform. Routing your broadcast through free "
                 "<strong style='color:var(--text)'>SplitCam</strong> adds multi-camera scenes, "
                 "overlays, filters and AI background that a basic browser camera can't manage.",
        "quick": "Broadcast on CamPlace with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in CamPlace, copy the server URL and stream "
                 "key, paste them into SplitCam, Go Live. The video guide above walks it through."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the CamPlace RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to CamPlace and open your broadcast settings. Switch to the external "
                   "encoder / RTMP / OBS option to reveal the <strong>server URL</strong> and "
                   "<strong>stream key</strong>, and copy both. The video guide above shows the "
                   "exact path on CamPlace's current interface.",
        "tips": [
            ("Follow the video guide", "CamPlace's interface changes over time — the video guide "
             "above shows the current path to the encoder settings."),
            ("Layer your overlays in SplitCam", "Tip goals, your name and socials as scene "
             "layers — CamPlace's basic camera can't add them."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Does CamPlace support external encoders?", "Yes — CamPlace accepts an RTMP stream "
             "key, so SplitCam works as the encoder."),
            ("Is SplitCam free for CamPlace?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for CamPlace?", "3,500–6,000 Kbps at 1080p; test your upload first."),
            ("Can I use two cameras on CamPlace?", "Yes — add multiple cameras as scene sources "
             "in SplitCam and switch with hotkeys."),
        ],
    },
    {
        "slug": "camsoda", "name": "CamSoda",
        "title": "How to Stream on CamSoda with SplitCam — Free Setup Guide",
        "desc": "Broadcast on CamSoda with free SplitCam — external encoder, scenes, overlays "
                "and filters. Video guide included, no watermark.",
        "kw": "how to stream on camsoda, camsoda live, camsoda broadcasting software, "
              "camsoda rtmp obs",
        "h1html": 'How to stream on <span class="accent">CamSoda</span> with SplitCam',
        "h1short": "Stream on CamSoda",
        "card": "External encoder setup for CamSoda broadcasts.",
        "intro": "CamSoda is a US cam platform known for novel, interactive show formats. Free "
                 "<strong style='color:var(--text)'>SplitCam</strong> works as its encoder — "
                 "scenes, overlays, filters and hardware encoding for a cleaner, more produced "
                 "broadcast than the basic camera.",
        "quick": "Broadcast on CamSoda with SplitCam: install SplitCam, build your scene, enable "
                 "the OBS / external encoder in CamSoda, copy the server URL and stream key, "
                 "paste them into SplitCam, Go Live. Watch the video guide above for the exact "
                 "path."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the CamSoda RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Sign in to CamSoda and open your broadcast settings. Choose the <strong>OBS / "
                   "external encoder</strong> option to get the RTMP server URL and stream key, "
                   "and copy both. The video guide above shows CamSoda's exact menu path.",
        "tips": [
            ("Watch the video guide", "CamSoda's broadcast UI is best followed visually — the "
             "video guide above shows the current encoder path."),
            ("Produce, don't just point a camera", "CamSoda rewards distinctive shows — use "
             "SplitCam scenes and overlays to make yours stand out."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Does CamSoda support external encoders?", "Yes — CamSoda accepts an RTMP/OBS "
             "stream, so SplitCam works as the encoder."),
            ("Is SplitCam free for CamSoda?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for CamSoda?", "3,500–6,000 Kbps at 1080p; test your upload first."),
            ("Can I multistream CamSoda with other sites?", "Yes — SplitCam can broadcast to "
             "several cam sites from one encode."),
        ],
    },
    {
        "slug": "streamate", "name": "Streamate",
        "title": "How to Stream on Streamate with SplitCam — Built-in Channel Setup",
        "desc": "Broadcast on Streamate with free SplitCam. Streamate is a built-in channel in "
                "SplitCam — use SM Connect, copy the key, Add Channel → Streamate.",
        "kw": "how to stream on streamate, streamate sm connect, streamate broadcasting "
              "software, streamate rtmp, streamate add channel",
        "h1html": 'How to stream on <span class="accent">Streamate</span> with SplitCam',
        "h1short": "Stream on Streamate",
        "card": "Streamate is a built-in SplitCam channel — quick setup.",
        "intro": "Streamate is an established cam platform — and it's one of the destinations "
                 "<strong style='color:var(--text)'>pre-configured inside SplitCam</strong>'s "
                 "channel list, so setup is quicker than a manual RTMP entry: pick Streamate, "
                 "paste the key, done.",
        "quick": "Broadcast on Streamate with SplitCam: install SplitCam, build your scene, on "
                 "Streamate use <em>SM Connect → Start Show</em> and copy the key, then in "
                 "SplitCam open <em>Stream Settings → Add Channel → Streamate</em> and paste it."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the Streamate key via SM Connect.</li>"
                 "<li>Add Channel → Streamate in SplitCam.</li><li>Go Live.</li></ol>",
        "key_how": "On Streamate, open <strong>SM Connect</strong>, accept the terms, click "
                   "<strong>Start Show</strong> on the left and close the window that opens — "
                   "then copy your streaming key. In SplitCam, open <strong>Stream "
                   "Settings</strong> → <strong>Add Channel</strong>, pick <strong>Streamate</strong> "
                   "from the list and paste the key. A green slider confirms the connection.",
        "tips": [
            ("Streamate is a built-in channel", "You don't need a manual RTMP URL — SplitCam has "
             "Streamate in its Add Channel list, so just select it and paste the key."),
            ("Close the SM Connect pop-up", "After Start Show, Streamate opens a window — close "
             "it; you only needed it to reveal the streaming key."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Is Streamate built into SplitCam?", "Yes — Streamate appears in SplitCam's Add "
             "Channel list, so you select it instead of entering an RTMP URL by hand."),
            ("Where is the Streamate streaming key?", "SM Connect → accept terms → Start Show → "
             "close the pop-up window → copy the key."),
            ("Is SplitCam free for Streamate?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for Streamate?", "3,500–6,000 Kbps at 1080p; test upload first."),
        ],
    },
    {
        "slug": "streamray", "name": "StreamRay",
        "title": "How to Stream on StreamRay with SplitCam — URL-from-Chat Setup",
        "desc": "Broadcast on StreamRay with free SplitCam. StreamRay posts the stream URL in "
                "the chat window and uses no stream key — SplitCam handles the URL-only flow.",
        "kw": "how to stream on streamray, streamray obs broadcaster, streamray cam, "
              "streamray rtmp, streamray broadcast",
        "h1html": 'How to stream on <span class="accent">StreamRay</span> with SplitCam',
        "h1short": "Stream on StreamRay",
        "card": "URL-from-chat external encoder setup for StreamRay.",
        "intro": "StreamRay has an unusual external-encoder setup — it hands you the stream URL "
                 "inside the <strong style='color:var(--text)'>broadcast chat window</strong> "
                 "and uses no separate stream key. Free "
                 "<strong style='color:var(--text)'>SplitCam</strong> handles that URL-only flow "
                 "fine.",
        "quick": "Broadcast on StreamRay with SplitCam: install SplitCam, build your scene, on "
                 "StreamRay enable the OBS Broadcaster, copy the stream URL from the chat window, "
                 "paste it into SplitCam (leave the key field empty), Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Copy the StreamRay URL from chat.</li>"
                 "<li>Paste the URL into SplitCam.</li><li>Go Live.</li></ol>",
        "key_how": "On StreamRay, click <strong>Broadcast Now</strong> twice, open the "
                   "<strong>Other</strong> menu, choose <strong>OBS Broadcaster</strong> and "
                   "<strong>Save and Close</strong>. StreamRay then posts your <strong>stream URL "
                   "in the chat window</strong> — copy it from there. Leave SplitCam's stream-key "
                   "field <strong>empty</strong>; StreamRay authenticates by URL only.",
        "tips": [
            ("The URL is in the chat", "StreamRay doesn't show the stream URL in a settings "
             "box — it posts it into your broadcast chat window. Copy it from there."),
            ("Leave the stream key empty", "StreamRay uses no separate key — only the URL. Don't "
             "try to fill the key field in SplitCam."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Where is the StreamRay stream URL?", "After enabling OBS Broadcaster, StreamRay "
             "posts the stream URL into the chat window — copy it from chat."),
            ("Why is there no StreamRay stream key?", "StreamRay authenticates by URL only — "
             "leave SplitCam's stream-key field empty."),
            ("Is SplitCam free for StreamRay?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for StreamRay?", "3,500–6,000 Kbps at 1080p; test upload first."),
        ],
    },
    {
        "slug": "xlovecam", "name": "XLoveCam",
        "title": "How to Stream on XLoveCam with SplitCam — RTMP Link & Key Setup",
        "desc": "Broadcast on XLoveCam with free SplitCam. Find the RTMP link and stream key "
                "under My Account → settings, run scenes and overlays. No watermark.",
        "kw": "how to stream on xlovecam, xlovecam rtmp link, xlovecam stream key, "
              "x love cam, xlovecam broadcast",
        "h1html": 'How to stream on <span class="accent">XLoveCam</span> with SplitCam',
        "h1short": "Stream on XLoveCam",
        "card": "RTMP link + key setup for XLoveCam broadcasts.",
        "intro": "XLoveCam is a European, multilingual cam platform. Its account settings expose "
                 "both an <strong style='color:var(--text)'>RTMP link</strong> and a "
                 "<strong style='color:var(--text)'>stream key</strong> — free "
                 "<strong style='color:var(--text)'>SplitCam</strong> takes both and broadcasts "
                 "with full scenes and overlays.",
        "quick": "Broadcast on XLoveCam with SplitCam: install SplitCam, build your scene, on "
                 "XLoveCam open <em>My Account → settings</em>, copy the RTMP link and stream "
                 "key, paste both into SplitCam, start your show."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Copy the XLoveCam RTMP link + key.</li><li>Paste both into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "On XLoveCam, open <strong>My Account</strong> → <strong>settings</strong>. "
                   "The settings contain both an <strong>RTMP link</strong> and a "
                   "<strong>stream key</strong> — copy both into SplitCam's server URL and key "
                   "fields, then use <strong>Start your show</strong> on XLoveCam.",
        "tips": [
            ("Copy both link and key", "XLoveCam gives you an RTMP link AND a separate stream "
             "key — you need both in SplitCam, not just one."),
            ("Multilingual audience", "XLoveCam is European and multilingual — a clear text "
             "overlay with your language helps viewers find you."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Where are the XLoveCam RTMP details?", "My Account → settings — it shows both the "
             "RTMP link and the stream key."),
            ("Does XLoveCam support external encoders?", "Yes — it provides an RTMP link and "
             "key, so SplitCam works as the encoder."),
            ("Is SplitCam free for XLoveCam?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for XLoveCam?", "3,500–6,000 Kbps at 1080p; test upload first."),
        ],
    },
    {
        "slug": "soulcams", "name": "SoulCams",
        "title": "How to Stream on SoulCams with SplitCam — OBS Settings Setup",
        "desc": "Broadcast on SoulCams with free SplitCam. Go Online → Settings → OBS shows the "
                "RTMP server and key together. Scenes, overlays, no watermark.",
        "kw": "how to stream on soulcams, soulcams obs, soul cams, soulcams rtmp, "
              "soulcams broadcast",
        "h1html": 'How to stream on <span class="accent">SoulCams</span> with SplitCam',
        "h1short": "Stream on SoulCams",
        "card": "OBS-settings setup for SoulCams broadcasts.",
        "intro": "SoulCams is a cam platform whose OBS settings show the "
                 "<strong style='color:var(--text)'>RTMP server and stream key together</strong> "
                 "in one window. Drop both into free "
                 "<strong style='color:var(--text)'>SplitCam</strong> to broadcast with "
                 "multi-camera scenes and overlays.",
        "quick": "Broadcast on SoulCams with SplitCam: install SplitCam, build your scene, on "
                 "SoulCams click Go Online → Settings → OBS, copy the server and key, paste both "
                 "into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Open SoulCams Settings → OBS.</li><li>Paste server + key into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "On SoulCams, log in and click <strong>Go Online</strong>, then open "
                   "<strong>Settings</strong> → <strong>OBS</strong>. The OBS window shows the "
                   "<strong>RTMP server</strong> and <strong>stream key</strong> together — copy "
                   "both into SplitCam.",
        "tips": [
            ("Server and key are side by side", "SoulCams shows both the RTMP server and the "
             "key in the same OBS window — grab both in one go."),
            ("Go Online first", "The OBS settings only appear after you click Go Online on "
             "SoulCams — do that before looking for the encoder details."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Where are the SoulCams OBS settings?", "Log in, click Go Online, then Settings → "
             "OBS — the RTMP server and stream key are shown together."),
            ("Does SoulCams support external encoders?", "Yes — its OBS settings provide an RTMP "
             "server and key, so SplitCam works."),
            ("Is SplitCam free for SoulCams?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for SoulCams?", "3,500–6,000 Kbps at 1080p; test upload first."),
        ],
    },
    {
        "slug": "imlive", "name": "ImLive",
        "title": "How to Use SplitCam on ImLive — Virtual Camera Setup",
        "desc": "ImLive uses your webcam directly — no RTMP. Connect SplitCam as a virtual "
                "camera so your scenes, overlays and filters show in ImLive video chat.",
        "kw": "how to stream on imlive, imlive splitcam, imlive virtual camera, imlive webcam, "
              "im live stream",
        "h1html": 'How to use <span class="accent">ImLive</span> with SplitCam',
        "h1short": "Use SplitCam on ImLive",
        "card": "Virtual-camera setup for ImLive — no RTMP needed.",
        "intro": "ImLive uses your webcam directly in the browser — there is "
                 "<strong style='color:var(--text)'>no RTMP and no stream key</strong>. Free "
                 "<strong style='color:var(--text)'>SplitCam</strong> connects as a "
                 "<strong style='color:var(--text)'>virtual camera</strong> instead: build your "
                 "scene in SplitCam, then pick SplitCam as the camera inside ImLive.",
        "quick": "Use SplitCam on ImLive: install SplitCam, build your scene with media layers, "
                 "open ImLive and start a video chat, then in ImLive's settings select SplitCam "
                 "as your webcam and microphone."
                 "<ol><li>Install SplitCam.</li><li>Build your scene in SplitCam.</li>"
                 "<li>Start a video chat on ImLive.</li>"
                 "<li>Pick SplitCam as the ImLive camera.</li><li>Start the chat.</li></ol>",
        "steps": [
            ("Install SplitCam",
             "SplitCam is free software for Windows and macOS. Install it — no watermark, no "
             "signup. On ImLive it works as a <strong>virtual camera</strong>, not an RTMP "
             "encoder."),
            ("Build your scene in SplitCam",
             "Open SplitCam and use <strong>Media Layers +</strong> to add your webcam plus any "
             "overlays, text, filters or AI background. This composed scene is what ImLive will "
             "see as your camera."),
            ("Start a video chat on ImLive",
             "Go to the ImLive site and click <strong>Start Video Chat</strong>, then open "
             "<strong>Go To Settings</strong> to reach the camera and microphone options."),
            ("Select SplitCam as your camera",
             "In ImLive's settings, choose <strong>SplitCam</strong> as both the webcam and the "
             "microphone. ImLive now shows your full SplitCam scene instead of a plain webcam."),
            ("Start your Free Live Chat",
             "Click <strong>Free Live Chat</strong> on ImLive to go live. To change your look "
             "mid-session, edit the scene in SplitCam — it updates in ImLive instantly."),
        ],
        "tips": [
            ("No stream key needed", "ImLive has no RTMP — don't look for a server URL or key. "
             "SplitCam is just selected as the camera device."),
            ("Set SplitCam as mic too", "Pick SplitCam for the microphone as well as the camera "
             "so your audio mix and noise suppression carry through."),
            ("Build the scene before going live", "ImLive shows whatever SplitCam outputs — "
             "arrange your layers before starting the chat."),
            _T_TEST,
        ],
        "faq": [
            ("Does ImLive use RTMP or a stream key?", "No — ImLive uses your webcam directly. "
             "SplitCam connects as a virtual camera, so there's no key to copy."),
            ("How do I pick SplitCam on ImLive?", "Start Video Chat → Go To Settings → choose "
             "SplitCam as the webcam and microphone."),
            ("Is SplitCam free for ImLive?", "Yes — free, no watermark, no time limit."),
            ("Can I use overlays on ImLive?", "Yes — build them into the SplitCam scene; ImLive "
             "shows the composed result."),
        ],
    },
    {
        "slug": "vxlive", "name": "VXLive",
        "title": "How to Stream on VXLive with SplitCam — Free Setup Guide",
        "desc": "Broadcast on VXLive with free SplitCam — external encoder, scenes, overlays and "
                "filters. Video guide included, no watermark.",
        "kw": "how to stream on vxlive, vxlive broadcasting software, vxlive rtmp, "
              "vxlive external encoder",
        "h1html": 'How to stream on <span class="accent">VXLive</span> with SplitCam',
        "h1short": "Stream on VXLive",
        "card": "External encoder setup for VXLive broadcasts.",
        "intro": "VXLive is a German-market cam platform. Free "
                 "<strong style='color:var(--text)'>SplitCam</strong> works as its encoder — "
                 "multi-camera scenes, overlays, filters and hardware encoding for a cleaner "
                 "broadcast than the basic camera.",
        "quick": "Broadcast on VXLive with SplitCam: install SplitCam, build your scene, enable "
                 "the external encoder in VXLive, copy the server URL and stream key, paste them "
                 "into SplitCam, Go Live. The video guide above shows the path."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the VXLive RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Sign in to VXLive and open your broadcast settings. Choose the <strong>"
                   "external encoder / RTMP</strong> option to get the server URL and stream "
                   "key, and copy both. The video guide above shows VXLive's exact path.",
        "tips": [
            ("German-market platform", "VXLive's audience is largely German-speaking — a German "
             "text overlay or title can help you connect with viewers."),
            ("Follow the video guide", "VXLive's broadcast UI is best followed visually — the "
             "video above shows the current encoder path."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Does VXLive support external encoders?", "Yes — VXLive accepts an RTMP/OBS stream, "
             "so SplitCam works as the encoder."),
            ("Is SplitCam free for VXLive?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for VXLive?", "3,500–6,000 Kbps at 1080p; test your upload first."),
            ("Can I multistream VXLive?", "Yes — SplitCam can broadcast to several cam sites at "
             "once from one encode."),
        ],
    },
    {
        "slug": "virtwish", "name": "VirtWish",
        "title": "How to Stream on VirtWish with SplitCam — Stream URL & Key Setup",
        "desc": "Broadcast on VirtWish with free SplitCam. Profile → Start Broadcast → OBS "
                "section gives the stream URL and key. Scenes, overlays, no watermark.",
        "kw": "how to stream on virtwish, virtwish broadcasting software, virtwish rtmp, "
              "virtwish stream key, virtwish obs",
        "h1html": 'How to stream on <span class="accent">VirtWish</span> with SplitCam',
        "h1short": "Stream on VirtWish",
        "card": "Stream URL + key setup for VirtWish broadcasts.",
        "intro": "VirtWish is an interactive cam platform. Its broadcast settings give you a "
                 "<strong style='color:var(--text)'>stream URL and a separate stream key</strong> "
                 "in an OBS section — free <strong style='color:var(--text)'>SplitCam</strong> "
                 "takes both and runs the show with scenes and overlays.",
        "quick": "Broadcast on VirtWish with SplitCam: install SplitCam, build your scene, on "
                 "VirtWish open <em>Profile → Start Broadcast</em> to reach the OBS section, copy "
                 "the link and key, paste both into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the VirtWish URL + key.</li><li>Paste both into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "On VirtWish, click the icon at the top right → <strong>Profile</strong> → "
                   "<strong>Start Broadcast</strong>, then <strong>Start Broadcast</strong> again "
                   "to reach the OBS section. <strong>Copy the link in the first line</strong> "
                   "into SplitCam's Stream URL field, and copy the <strong>Stream Key</strong> "
                   "separately into the key field.",
        "tips": [
            ("Link is in the first line", "VirtWish's OBS section puts the stream URL on the "
             "first line — copy that into SplitCam's Stream URL, then the key separately."),
            ("Two clicks of Start Broadcast", "You click Start Broadcast twice on VirtWish to "
             "reach the OBS section — that's expected, not a glitch."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Where are the VirtWish RTMP details?", "Top-right icon → Profile → Start Broadcast "
             "twice → the OBS section shows the link and stream key."),
            ("Does VirtWish support external encoders?", "Yes — its OBS section provides a "
             "stream URL and key, so SplitCam works."),
            ("Is SplitCam free for VirtWish?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for VirtWish?", "3,500–6,000 Kbps at 1080p; test upload first."),
        ],
    },
    {
        "slug": "xmodels", "name": "XModels",
        "title": "How to Stream on XModels with SplitCam — Free Setup Guide",
        "desc": "Broadcast on XModels with free SplitCam — external encoder, scenes, overlays "
                "and filters. Video guide included, no watermark.",
        "kw": "how to stream on xmodels, xmodels broadcasting software, xmodels rtmp, "
              "xmodels external encoder",
        "h1html": 'How to stream on <span class="accent">XModels</span> with SplitCam',
        "h1short": "Stream on XModels",
        "card": "External encoder setup for XModels broadcasts.",
        "intro": "XModels is a cam-streaming platform. Through free "
                 "<strong style='color:var(--text)'>SplitCam</strong> you broadcast with "
                 "multi-camera scenes, overlays, filters and AI background instead of a single "
                 "plain camera.",
        "quick": "Broadcast on XModels with SplitCam: install SplitCam, build your scene, enable "
                 "the external encoder in XModels, copy the server URL and stream key, paste "
                 "them into SplitCam, Go Live. See the video guide above for the path."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the XModels RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to XModels and open your broadcast settings. Switch to the "
                   "<strong>external encoder / RTMP</strong> option to reveal the server URL and "
                   "stream key, and copy both. The video guide above walks through XModels' "
                   "current path.",
        "tips": [
            ("Follow the video guide", "The video above shows the current path to XModels' "
             "encoder settings — interfaces shift over time."),
            ("Layer overlays in SplitCam", "Tip goals, your name and socials as scene layers — "
             "XModels' basic camera can't add them."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Does XModels support external encoders?", "Yes — XModels accepts an RTMP/OBS "
             "stream, so SplitCam works as the encoder."),
            ("Is SplitCam free for XModels?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for XModels?", "3,500–6,000 Kbps at 1080p; test your upload first."),
            ("Can I use two cameras on XModels?", "Yes — add multiple cameras as scene sources "
             "in SplitCam."),
        ],
    },
    {
        "slug": "flirt4free", "name": "Flirt4Free",
        "title": "How to Stream on Flirt4Free with SplitCam — Free Setup Guide",
        "desc": "Broadcast on Flirt4Free with free SplitCam — external encoder, scenes, overlays "
                "and filters. Video guide included, no watermark.",
        "kw": "how to stream on flirt4free, flirt for free cam, flirt4free broadcasting "
              "software, flirt4free rtmp",
        "h1html": 'How to stream on <span class="accent">Flirt4Free</span> with SplitCam',
        "h1short": "Stream on Flirt4Free",
        "card": "External encoder setup for Flirt4Free broadcasts.",
        "intro": "Flirt4Free is one of the longest-running cam platforms, online since the "
                 "1990s. Free <strong style='color:var(--text)'>SplitCam</strong> works as its "
                 "encoder — scenes, overlays and filters for a polished, modern-looking "
                 "broadcast.",
        "quick": "Broadcast on Flirt4Free with SplitCam: install SplitCam, build your scene, "
                 "enable the external encoder in the Flirt4Free model area, copy the server URL "
                 "and stream key, paste them into SplitCam, Go Live. The video guide above shows "
                 "the path."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the Flirt4Free RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to the Flirt4Free model area and open your broadcast settings. Choose "
                   "the <strong>external encoder / RTMP</strong> option to get the server URL and "
                   "stream key, and copy both. The video guide above shows the exact steps.",
        "tips": [
            ("An established platform", "Flirt4Free has run since the 1990s — its model tools "
             "are mature; the external-encoder option is in the model broadcast settings."),
            ("Follow the video guide", "The video above shows Flirt4Free's current encoder "
             "path."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Does Flirt4Free support external encoders?", "Yes — Flirt4Free accepts an RTMP/OBS "
             "stream, so SplitCam works as the encoder."),
            ("Is SplitCam free for Flirt4Free?", "Yes — free, no watermark, no time limit."),
            ("What bitrate for Flirt4Free?", "3,500–6,000 Kbps at 1080p; test upload first."),
            ("Can I multistream Flirt4Free?", "Yes — SplitCam can broadcast to several cam sites "
             "at once."),
        ],
    },
    {
        "slug": "mfc-alerts", "name": "MFC Alerts",
        "title": "How to Add MFC Alerts to Your Stream with SplitCam",
        "desc": "Show animated tip alerts on your MyFreeCams stream. Add your mfcalerts.com URL "
                "as a Browser layer in free SplitCam — keep it above the webcam.",
        "kw": "mfc alerts, how to add mfc alerts, myfreecams tip alerts, mfcalerts splitcam, "
              "myfreecams alerts overlay",
        "h1html": 'How to add <span class="accent">MFC Alerts</span> to your stream',
        "h1short": "Add MFC Alerts",
        "card": "Show animated tip alerts on your MyFreeCams stream.",
        "intro": "MFC Alerts shows animated effects on your MyFreeCams stream whenever a viewer "
                 "tips. It runs as a <strong style='color:var(--text)'>Browser layer</strong> "
                 "inside free <strong style='color:var(--text)'>SplitCam</strong> — set it up "
                 "once and tips trigger on-screen reactions live.",
        "quick": "Add MFC Alerts with SplitCam: install SplitCam, add your webcam, open the "
                 "Browser tab and load mfcalerts.com, copy your alerts URL, add it as a Browser "
                 "layer above the webcam, then test with a test tip."
                 "<ol><li>Install SplitCam.</li><li>Add your webcam.</li>"
                 "<li>Get your URL from mfcalerts.com.</li>"
                 "<li>Add it as a Browser layer above the webcam.</li><li>Send a test tip.</li></ol>",
        "steps": [
            ("Install SplitCam and add your webcam",
             "Install free SplitCam for Windows or macOS, then add your <strong>webcam</strong> "
             "as a source. MFC Alerts will sit as a layer on top of this camera."),
            ("Open the Browser tab and go to mfcalerts.com",
             "In SplitCam, open the <strong>Browser</strong> tab and navigate to "
             "<strong>www.mfcalerts.com</strong>. Log in, or register if you don't have an "
             "mfcalerts.com account yet."),
            ("Copy your alerts URL",
             "On mfcalerts.com, use <strong>Copy to clipboard</strong> to copy your personal "
             "alerts URL — this is the page that renders the tip animations."),
            ("Add the URL as a Browser layer — above the webcam",
             "Paste the URL into SplitCam's Browser window and click <strong>Add</strong>. Then "
             "reorder the source list so <strong>MFC Alerts sits above your webcam</strong> "
             "(3-dot menu → Move Up). If it's below the webcam, the effects won't show."),
            ("Test with a test tip",
             "Open <strong>Settings → Send test tip</strong> and confirm the alert effect "
             "appears over your camera. Then stream to MyFreeCams as usual — real tips now "
             "trigger the animations."),
        ],
        "tips": [
            ("Keep MFC Alerts above the webcam", "The single most common mistake: if the MFC "
             "Alerts layer is below the webcam in the source list, the effects are hidden. Move "
             "it up."),
            ("You need an mfcalerts.com account", "The alerts URL is personal to your account — "
             "register on mfcalerts.com first if you don't have one."),
            ("Send a test tip before going live", "Use Settings → Send test tip to confirm the "
             "overlay works — don't discover it's broken mid-show."),
            _T_ETH,
        ],
        "faq": [
            ("What is MFC Alerts?", "A notification system for MyFreeCams that shows video "
             "effects on your stream when viewers tip — added as a Browser overlay in SplitCam."),
            ("Why don't my MFC Alerts show?", "Almost always layer order — the MFC Alerts "
             "Browser layer must sit above the webcam in SplitCam's source list."),
            ("Do I need an account for MFC Alerts?", "Yes — register on mfcalerts.com to get "
             "your personal alerts URL."),
            ("Is SplitCam free for this?", "Yes — SplitCam is free, no watermark, no limits."),
        ],
    },
    {
        "slug": "lovense", "name": "Lovense",
        "title": "How to Add a Lovense Toy to Your Stream with SplitCam",
        "desc": "Connect a Lovense interactive toy to your cam stream and show its status "
                "on screen with free SplitCam. Step-by-step, no watermark.",
        "kw": "how to add lovense to stream, lovense cam stream, lovense splitcam, "
              "lovense interactive toy streaming",
        "h1html": 'How to add a <span class="accent">Lovense toy</span> to your stream',
        "h1short": "Add a Lovense toy",
        "card": "Connect a Lovense interactive toy to your cam stream.",
        "intro": "Run your cam stream through free <strong style='color:var(--text)'>SplitCam</strong> "
                 "and pair a <strong style='color:var(--text)'>Lovense</strong> interactive toy "
                 "so it reacts to tokens — with the connection status visible on screen.",
        "quick": "To add a Lovense toy to your stream: install SplitCam and Lovense software, "
                 "pair the toy, link Lovense to your cam platform, add the Lovense status as a "
                 "Browser layer in SplitCam, then broadcast as usual."
                 "<ol><li>Install SplitCam.</li><li>Install &amp; pair Lovense software.</li>"
                 "<li>Link Lovense to your cam site.</li>"
                 "<li>Add the Lovense overlay in SplitCam.</li><li>Go Live.</li></ol>",
        "steps": [
            ("Install SplitCam",
             "SplitCam is free live-streaming software for Windows and macOS — the encoder that "
             "sends your video to your cam platform. Install it; no watermark."),
            ("Install and pair the Lovense software",
             "Install Lovense Connect / Lovense Stream (the official desktop app). Turn on your "
             "toy and pair it over Bluetooth so the app shows it connected."),
            ("Link Lovense to your cam platform",
             "In the Lovense app, connect your cam-site account so the toy reacts to tokens / "
             "tips from viewers. Most major cam platforms are supported by Lovense."),
            ("Add the Lovense overlay in SplitCam",
             "Lovense provides an overlay / widget URL. Add it as a <strong>Browser</strong> "
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
            ("Is SplitCam free for this?", "Yes — SplitCam is free with no watermark. The "
             "Lovense software is also free."),
            ("Does the toy connect to SplitCam directly?", "No — the toy pairs with the Lovense "
             "app; SplitCam displays the Lovense overlay and broadcasts your camera."),
            ("Which cam sites support Lovense?", "Most major cam platforms integrate with "
             "Lovense for token-reactive toys — check the Lovense app for the current list."),
            ("Can I show recent tips on screen?", "Yes — add the Lovense widget URL as a Browser "
             "layer in SplitCam."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Multiple Cam Sites",
        "title": "How to Broadcast to Multiple Cam Sites at Once with SplitCam",
        "desc": "Stream to MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat and more at the "
                "same time with free SplitCam multistreaming. Step-by-step, no watermark.",
        "kw": "broadcast to multiple cam sites, multistream cam sites, stream to chaturbate and "
              "bongacams at once, cam multistreaming software",
        "h1html": 'How to broadcast to <span class="accent">multiple cam sites</span> at once',
        "h1short": "Multistream cam sites",
        "card": "Broadcast to several cam sites simultaneously.",
        "intro": "Free <strong style='color:var(--text)'>SplitCam</strong> can broadcast one "
                 "encode to <strong style='color:var(--text)'>several cam sites at the same "
                 "time</strong> — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat and more. "
                 "No watermark, one click.",
        "quick": "To broadcast to several cam sites at once: install SplitCam, build your scene, "
                 "get the RTMP server URL and stream key from each cam site, add them all in "
                 "SplitCam's multistream settings, click Go Live once."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get an RTMP key from each cam site.</li>"
                 "<li>Add all keys in SplitCam multistream.</li><li>Go Live once.</li></ol>",
        "steps": [
            ("Install SplitCam",
             "SplitCam is free live-streaming software for Windows and macOS with built-in "
             "multistreaming. Install it — no watermark, no signup."),
            ("Set up your camera and scene",
             "Open SplitCam, add your webcam and build your scene with overlays and filters. "
             "One scene feeds every destination."),
            ("Get an RTMP key from each cam site",
             "On each cam platform, enable external / RTMP broadcasting and copy its "
             "<strong>server URL</strong> and <strong>stream key</strong>. Repeat for every site "
             "you want to broadcast to — see the individual platform guides for exact paths."),
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
            ("Check each platform's rules", "Some cam sites restrict simultaneous broadcasting "
             "elsewhere — confirm before you multistream."),
            _T_ETH,
            ("Watch the health monitor", "SplitCam shows per-destination status — drop a site "
             "if your upload can't keep up."),
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
