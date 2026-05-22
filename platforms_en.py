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
            ("Lots of headroom", "Chaturbate's own RTMP ingest accepts up to 4K, 60 fps and a "
             "very high bitrate ceiling — quality is limited by your upload, not the platform. "
             "Use a 2-second keyframe interval."),
            ("Low latency by design", "Chaturbate delivers your stream over low-latency HLS — "
             "roughly 2–4 seconds glass-to-glass — so viewer tips and reactions stay in step "
             "with what you do on cam."),
            ("Wire up for the 4K headroom", "Chaturbate accepts very high bitrates, so you'll "
             "be pushing a lot of data — a wired Ethernet link keeps that stream stable where "
             "Wi-Fi would drop frames."),
            ("Test the room privately first", "Chaturbate lets you broadcast before going "
             "public — do a short private check of camera, audio and overlays first."),
        ],
        "faq": [
            ("Does Chaturbate allow OBS / external encoders?", "Yes — Chaturbate officially "
             "supports external encoders and has its own \"How do I set up OBS?\" support "
             "article. Activate it with \"Use External Encoder to Broadcast\" in your broadcast "
             "settings."),
            ("Where is my Chaturbate stream key?", "Broadcast Yourself → My Broadcast → View "
             "RTMP/OBS broadcast information and stream key. The key is your broadcast token."),
            ("What resolution and fps does Chaturbate support?", "Chaturbate's RTMP ingest "
             "accepts up to 3840×2160 (4K) and 60 fps with a 2-second keyframe interval — far "
             "more headroom than most cam platforms."),
            ("What bitrate for Chaturbate?", "3,500–6,000 Kbps at 1080p is plenty. Chaturbate's "
             "ceiling is very high, so your upload speed is the real limit — run SplitCam's "
             "speed test first."),
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
            ("Use CAM4's official encoder preset", "CAM4's OBS Guide specifies CBR, a 1-second "
             "keyframe interval and the x264 veryfast/superfast preset with tune=zerolatency and "
             "B-frames at 0 — and recommends enabling \"dynamically change bitrate\". Run the "
             "connection test at speedtest.xcdnpro.com first."),
            ("Cable beats Wi-Fi on CAM4", "CAM4's ingest is bandwidth-tiered — a wired "
             "connection holds a steady tier instead of bouncing your resolution down on "
             "every Wi-Fi dip."),
            ("Test camera and geo-settings", "Run a short private CAM4 broadcast to check "
             "your camera, audio and geo-restrictions before opening the room."),
        ],
        "faq": [
            ("Does CAM4 officially support OBS / external encoders?", "Yes — CAM4 has an "
             "official OBS Guide on its support site and recommends the External Encoder option "
             "for the best experience. SplitCam uses the same RTMP path."),
            ("Can I geo-block my CAM4 broadcast?", "Yes — CAM4 has built-in geo-restriction to "
             "hide your broadcast in certain countries. It's set on CAM4, not in SplitCam."),
            ("Where is the CAM4 stream key?", "Broadcast → Broadcast & Earn Money → Start "
             "Broadcast → External Encoder → Get Stream Key."),
            ("What bitrate for CAM4?", "Lower than most cam sites — CAM4's ingest caps the "
             "video bitrate around 3,000 Kbps at 30 fps with a 1-second keyframe interval. "
             "CAM4's official OBS Guide has a speed-test-based table; don't push past ~3,000."),
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
            ("A dropped frame is a dropped token", "On a long BongaCams show, Wi-Fi instability "
             "costs you tips — run an Ethernet cable to the streaming PC."),
            ("Test once support enables encoding", "After BongaCams switches on external "
             "encoding, do a short private broadcast to confirm camera, audio and overlays."),
        ],
        "faq": [
            ("Why is the External Encoder button missing on BongaCams?", "External encoding is "
             "not enabled by default for every account — contact BongaCams support to activate "
             "it, then the button appears in Broadcast settings."),
            ("Do I need to verify my account on BongaCams?", "Yes — broadcasting requires being "
             "18+ with a valid government ID for age verification, and account approval before "
             "you can go live."),
            ("What bitrate for BongaCams?", "BongaCams' RTMP ingest caps the video bitrate "
             "around 6,000 Kbps with a 2-second keyframe interval — 3,500–6,000 at 1080p is the "
             "sweet spot; test your upload first."),
            ("Is SplitCam free for BongaCams?", "Yes — fully free, with no watermark and no "
             "time limit, so the encoder never eats into your BongaCams token earnings or "
             "caps how long you can broadcast."),
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
            ("Match the site resolution exactly", "Stripchat's FAQ warns that the resolution in "
             "your software must exactly match the resolution set on the site, or the video "
             "pixelates. Set both the same."),
            ("Mind the 2 Mbps floor", "Stripchat states 2 Mbps upload is the minimum — and is "
             "explicitly not enough for OBS-style streaming or simultaneous multi-platform "
             "streaming. Aim well above it."),
            ("The key is a token", "Stripchat's stream key is a token — copy it exactly and "
             "never share it; reset it if it leaks."),
            ("Wired, and well above 2 Mbps", "Stripchat's 2 Mbps floor isn't enough for "
             "encoder streaming — a wired link plus real headroom above that minimum keeps "
             "the show smooth."),
        ],
        "faq": [
            ("Does Stripchat recommend OBS / external software?", "Yes — Stripchat's own FAQ "
             "advises using external broadcast software like OBS \"to achieve better video and "
             "audio quality.\" SplitCam works the same way."),
            ("How do I switch Stripchat to external software?", "In the Broadcast Center choose "
             "Switch to External Broadcast Software (OBS), then open the external software "
             "settings to reveal the stream key (token)."),
            ("What bitrate for Stripchat?", "Its RTMP ingest accepts up to ~6,000 Kbps with a "
             "2-second keyframe interval. 3,500–6,000 at 1080p is ideal — but you need well "
             "above the 2 Mbps minimum, especially with OBS-style streaming."),
            ("Is SplitCam free for Stripchat?", "Yes — no licence fee, watermark or time "
             "limit, so even long interactive Stripchat shows cost nothing on the encoder "
             "side."),
        ],
    },
    {
        "slug": "onlyfans", "name": "OnlyFans",
        "title": "How to Go Live on OnlyFans with SplitCam — Authorization or Stream Key",
        "desc": "Go live on OnlyFans with free SplitCam. Connect by Authorization (log in once "
                "and the stream key syncs automatically) or paste the OBS Key by hand — scenes, "
                "overlays, no watermark.",
        "kw": "how to go live on onlyfans, onlyfans authorization splitcam, onlyfans obs key, "
              "onlyfans live stream, onlyfans streaming software",
        "h1html": 'How to go live on <span class="accent">OnlyFans</span> with SplitCam',
        "h1short": "Go live on OnlyFans",
        "card": "Authorize once or paste the key — go live on OnlyFans.",
        "intro": "OnlyFans live streaming runs for your subscribers. SplitCam connects in "
                 "<strong style='color:var(--text)'>two ways</strong> — sign in once with your "
                 "OnlyFans login and SplitCam fetches and keeps the stream key synced "
                 "automatically, or paste the OBS Key by hand. Either way you stream with "
                 "multi-camera scenes, overlays and filters.",
        "quick": "Go live on OnlyFans with SplitCam: install SplitCam, build your scene, open "
                 "Stream Settings &rarr; Add Channel &rarr; OnlyFans and choose "
                 "<em>Authorization</em> — sign in with your OnlyFans login and SplitCam pulls "
                 "your stream key automatically — then click Go Live. With the account "
                 "connected you can change the OnlyFans stream settings inside SplitCam, "
                 "without opening the OnlyFans site.",
        "steps": [
            ("Download and install SplitCam",
             "SplitCam is free live-streaming software for Windows and macOS — no signup, no "
             "card, no watermark. It is the encoder that sends your video to OnlyFans."),
            ("Set up your camera and scene",
             "Open SplitCam and add your webcam. Build the scene viewers will see — overlays, "
             "text, a second camera, beauty filters or an AI background, applied live."),
            ("Connect — Method 1: Authorization (recommended)",
             "In SplitCam open <strong>Stream Settings</strong> &rarr; <strong>Add "
             "Channel</strong> &rarr; <strong>OnlyFans</strong> and choose "
             "<strong>Authorization</strong>. Sign in with your OnlyFans email and password. "
             "SplitCam connects to your account, fetches the stream key automatically and "
             "keeps it synced — and lets you manage the OnlyFans stream settings inside "
             "SplitCam, changing them during or after the stream without opening the OnlyFans "
             "site."),
            ("Connect — Method 2: Stream Key (manual)",
             "Prefer not to sign in? Use the key instead. On OnlyFans go to "
             "<strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; the "
             "<strong>Other</strong> section and copy the <strong>OBS Key</strong>. In "
             "SplitCam, Add Channel &rarr; OnlyFans, paste it into the stream-key field. This "
             "key is static — to change settings later you go back to the OnlyFans site."),
            ("Go Live",
             "Whichever method you used, click <strong>Go Live</strong> in SplitCam. With "
             "Method 1 you can keep adjusting the OnlyFans settings from SplitCam on the fly; "
             "with Method 2 the key stays exactly as you set it."),
        ],
        "tips": [
            ("Authorization vs Stream Key", "Two ways to connect: <strong>Authorization</strong> "
             "(sign in once, the key is fetched and kept synced — easiest) or <strong>Stream "
             "Key</strong> (copy the OBS Key from OnlyFans → Profile → Settings → Other and "
             "paste it). Authorization needs no manual copying."),
            ("Change settings without leaving SplitCam", "With Authorization the account stays "
             "connected, so you can adjust the OnlyFans stream settings inside SplitCam mid-"
             "stream or afterwards — no trip to the OnlyFans website."),
            ("Keep the bitrate modest", "OnlyFans' RTMP ingest caps the video bitrate around "
             "2,500 Kbps — stricter than most cam sites. Aim for 720p–1080p at ~2,000–2,500."),
            _T_ETH,
        ],
        "faq": [
            ("How do I connect OnlyFans to SplitCam?", "Two ways. <strong>Authorization</strong> "
             "— Stream Settings → Add Channel → OnlyFans → sign in with your OnlyFans login, and "
             "SplitCam fetches the stream key automatically. Or <strong>Stream Key</strong> — "
             "copy the OBS Key from OnlyFans → Profile → Settings → Other and paste it in."),
            ("Can I change OnlyFans stream settings without opening the site?", "Yes — with the "
             "Authorization method SplitCam stays connected to your OnlyFans account, so the "
             "key and settings sync automatically. You can change them inside SplitCam during "
             "the stream or after it, without visiting onlyfans.com."),
            ("What bitrate for OnlyFans?", "Keep it modest — OnlyFans' RTMP ingest caps the "
             "video bitrate around 2,500 Kbps, much stricter than most cam platforms. Aim for "
             "720p–1080p at roughly 2,000–2,500 Kbps."),
            ("Is SplitCam free for OnlyFans live streams?", "Yes — free, no watermark, no limit."),
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
        "intro": "CamPlace is a cam-streaming platform. It has no public OBS help article, so "
                 "the <strong style='color:var(--text)'>video guide above</strong> is the "
                 "reference — free <strong style='color:var(--text)'>SplitCam</strong> connects "
                 "via standard RTMP and adds scenes, overlays and AI background a basic camera "
                 "can't.",
        "quick": "Broadcast on CamPlace with SplitCam: install SplitCam, build your scene, "
                 "enable external/RTMP broadcasting in CamPlace, copy the server URL and stream "
                 "key, paste them into SplitCam, Go Live. Follow the video guide above for the "
                 "current path."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the CamPlace RTMP key.</li><li>Paste it into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "Log in to CamPlace and open your broadcast settings. Switch to the external "
                   "encoder / RTMP / OBS option to reveal the <strong>server URL</strong> and "
                   "<strong>stream key</strong>, and copy both. CamPlace publishes no official "
                   "OBS documentation, so the <strong>video guide above</strong> is the most "
                   "reliable walkthrough of the current interface.",
        "tips": [
            ("No official OBS guide — use the video", "CamPlace has no public help-center "
             "article on external encoders; the video guide above is the reference for the "
             "current path."),
            ("Standard RTMP works", "Even without docs, CamPlace accepts a standard RTMP server "
             "URL and key — SplitCam connects as a normal custom RTMP destination."),
            ("Layer your overlays in SplitCam", "Tip goals, your name and socials as scene "
             "layers — CamPlace's basic camera can't add them."),
            ("Run a wired connection", "With no official CamPlace encoder docs to fall back "
             "on, a stable Ethernet link removes connection drops as a variable while you "
             "follow the video guide."),
        ],
        "faq": [
            ("Does CamPlace have an official OBS guide?", "No public help-center article on "
             "external encoders was found. CamPlace does accept a standard RTMP URL and key, so "
             "SplitCam works — follow the video guide above for the current path."),
            ("Does CamPlace support external encoders?", "Yes — it accepts a standard RTMP "
             "stream key, so SplitCam connects as a custom RTMP destination."),
            ("Is SplitCam free for CamPlace?", "Yes — free, no watermark, no time cap. Since "
             "CamPlace ships no encoder of its own, a free RTMP tool is all the setup needs."),
            ("What bitrate for CamPlace?", "CamPlace publishes no official figure — treat "
             "3,500–6,000 Kbps at 1080p as a safe range and let SplitCam's speed test set "
             "your real ceiling."),
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
        "intro": "CamSoda is a US cam platform known for novel, interactive show formats. It "
                 "officially supports OBS-style broadcasting — there's a "
                 "<strong style='color:var(--text)'>Use OBS Broadcaster</strong> button on the "
                 "Go Live page and an official OBS guide on the CamSoda wiki. Free "
                 "<strong style='color:var(--text)'>SplitCam</strong> works the same way.",
        "quick": "Broadcast on CamSoda with SplitCam: install SplitCam, build your scene, click "
                 "Use OBS Broadcaster on CamSoda's Go Live page, copy the server URL and stream "
                 "key, paste them into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Click Use OBS Broadcaster on CamSoda.</li>"
                 "<li>Paste server URL + key into SplitCam.</li><li>Go Live.</li></ol>",
        "key_how": "On CamSoda's <strong>Go Live</strong> page, click <strong>Use OBS "
                   "Broadcaster</strong>. CamSoda shows the RTMP server URL and stream key — "
                   "copy both. Pick the regional server (North America, Europe, Asia, etc.) "
                   "nearest to you. CamSoda's own wiki has a full OBS guide if you need the "
                   "detail.",
        "tips": [
            ("Get verified to receive tips", "On CamSoda anyone can broadcast, but you must "
             "complete CamSoda's verification application before you can receive tips."),
            ("Pick the nearest regional server", "CamSoda offers regional ingest servers — "
             "choosing the closest one (NA / Europe / Asia / South America / Oceania) reduces "
             "lag and dropped frames."),
            ("Cap at 1080p / 30 fps", "CamSoda's ingest tops out around 1080p, 30 fps and "
             "~6,000 Kbps — no need to push higher."),
            ("Wire up to your regional server", "Pair a wired connection with the nearest "
             "CamSoda regional ingest server — together they keep latency and dropped frames "
             "low."),
        ],
        "faq": [
            ("Does CamSoda support OBS / external encoders?", "Yes — officially. There's a Use "
             "OBS Broadcaster button on the Go Live page and an OBS guide on the CamSoda wiki, "
             "so SplitCam works."),
            ("Do I need to verify on CamSoda?", "To broadcast, no. To receive tips, yes — "
             "CamSoda requires you to complete its verification application first."),
            ("What resolution does CamSoda support?", "Up to 1920×1080 at 30 fps, roughly "
             "6,000 Kbps maximum on its RTMP ingest."),
            ("Is SplitCam free for CamSoda?", "Yes — free, no watermark, no time limit. It "
             "works alongside CamSoda's own free OBS-broadcaster mode, so the whole chain "
             "costs nothing."),
            ("What audio and encoder settings does CamSoda use?", "CamSoda's ingest takes AAC "
             "audio up to 160 Kbps and H.264 video with a tune=zerolatency preset. CamSoda is "
             "also a built-in service in OBS, so it behaves as a standard RTMP target in "
             "SplitCam."),
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
            ("Lock the resolution to 1080p", "SM Connect's Video Resolution field can jump to "
             "1440, which isn't actually delivered and quietly drops your quality — set it to "
             "1080p by hand. A bitrate that falls on a still shot is normal: Streamate's feed "
             "is adaptive."),
            ("Use a wired connection", "Streamate's feed already drops bitrate under strain "
             "— don't add Wi-Fi instability on top; run an Ethernet cable."),
            ("Test via SM Connect first", "Start a short private show through SM Connect to "
             "confirm the green slider and your scene before going public."),
        ],
        "faq": [
            ("Is Streamate built into SplitCam?", "Yes — Streamate appears in SplitCam's Add "
             "Channel list, so you select it instead of entering an RTMP URL by hand."),
            ("Where is the Streamate streaming key?", "SM Connect → accept terms → Start Show → "
             "close the pop-up window → copy the key."),
            ("Is SplitCam free for Streamate?", "Yes — free, no watermark, no time limit; and "
             "as Streamate is a built-in SplitCam channel there's no separate encoder cost "
             "either."),
            ("What bitrate for Streamate?", "Streamate sets no hard cap — 3,500–6,000 Kbps at "
             "1080p works well. The feed is adaptive, so a lower bitrate on a still shot is "
             "normal, not a fault."),
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
            ("Wired connection for the URL flow", "StreamRay authenticates by URL only — a "
             "wired link avoids a mid-show reconnect that would send you back to the chat "
             "window for the URL."),
            ("Test before broadcasting", "Do a short private StreamRay test to confirm the "
             "URL pasted correctly and the scene looks right."),
        ],
        "faq": [
            ("Where is the StreamRay stream URL?", "After enabling OBS Broadcaster, StreamRay "
             "posts the stream URL into the chat window — copy it from chat."),
            ("Why is there no StreamRay stream key?", "StreamRay authenticates by URL only — "
             "leave SplitCam's stream-key field empty."),
            ("Is SplitCam free for StreamRay?", "Yes — free, no watermark, no time limit, "
             "which suits StreamRay's URL-only flow where you just paste one link and "
             "broadcast."),
            ("What bitrate for StreamRay?", "StreamRay states no official ceiling — aim for "
             "3,500–6,000 Kbps at 1080p and run SplitCam's speed test, since the URL-only "
             "setup gives no bitrate feedback."),
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
            ("Pick the closest server", "XLoveCam runs regional RTMP servers — Europe (including "
             "Russia), North America (including Canada), South America and Asia. Choose the one "
             "nearest you to cut latency and dropped frames."),
            ("Wired beats Wi-Fi", "After picking the closest XLoveCam server, a wired "
             "connection is the other half of a stable stream — it keeps frames from dropping "
             "on a long show."),
            ("Run a private test", "Do a short test broadcast to check camera, audio and your "
             "language overlay before XLoveCam viewers arrive."),
        ],
        "faq": [
            ("Where are the XLoveCam RTMP details?", "My Account → settings — it shows both the "
             "RTMP link and the stream key."),
            ("Does XLoveCam support external encoders?", "Yes — it provides an RTMP link and "
             "key, so SplitCam works as the encoder."),
            ("Is SplitCam free for XLoveCam?", "Yes — free, no watermark, no time limit, so "
             "reaching XLoveCam's multilingual European audience carries no software cost."),
            ("What bitrate for XLoveCam?", "XLoveCam publishes no fixed limit; 3,500–6,000 "
             "Kbps at 1080p is ideal. Choosing the closest regional server matters as much — "
             "it cuts dropped frames."),
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
            ("Block regions you don't want", "SoulCams supports model-side country blocking — "
             "choose which countries can't see your broadcast before you click Go Online."),
            ("Use a wired connection", "SoulCams shows server and key together for a quick "
             "start — keep the stream itself just as solid with an Ethernet cable."),
            ("Test after Go Online", "The OBS settings appear only after Go Online — once "
             "connected, run a short private test before taking the room public."),
        ],
        "faq": [
            ("Where are the SoulCams OBS settings?", "Log in, click Go Online, then Settings → "
             "OBS — the RTMP server and stream key are shown together."),
            ("Does SoulCams support external encoders?", "Yes — its OBS settings provide an RTMP "
             "server and key, so SplitCam works."),
            ("Is SplitCam free for SoulCams?", "Yes — free, no watermark, no time limit, so a "
             "full SoulCams show with multi-camera scenes and overlays costs nothing to "
             "encode."),
            ("What bitrate for SoulCams?", "SoulCams gives no official figure — target "
             "3,500–6,000 Kbps at 1080p and test your upload first, as its OBS window shows "
             "no bitrate guidance."),
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
            ("Test the virtual camera first", "Before starting an ImLive chat, confirm the "
             "SplitCam virtual camera works — check it in ImLive's settings preview."),
        ],
        "faq": [
            ("Does ImLive use RTMP or a stream key?", "No — ImLive uses your webcam directly. "
             "SplitCam connects as a virtual camera, so there's no key to copy."),
            ("How do I pick SplitCam on ImLive?", "Start Video Chat → Go To Settings → choose "
             "SplitCam as the webcam and microphone."),
            ("Is SplitCam free for ImLive?", "Yes — free, no watermark, no time limit. As a "
             "virtual camera for ImLive it adds no cost and no branding to your video chat."),
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
        "intro": "VXLive (VXModels / VISIT-X) is a German-market cam platform — and one of the "
                 "few that <strong style='color:var(--text)'>officially supports SplitCam by "
                 "name</strong>. VXModels has a dedicated help article on connecting "
                 "<strong style='color:var(--text)'>SplitCam</strong> to VXLive, and SplitCam "
                 "ships VISIT-X as a ready-made channel preset.",
        "quick": "Broadcast on VXLive with SplitCam: install SplitCam, build your scene, in "
                 "VXLive choose \"Stream with third-party software\", copy the server URL and "
                 "key, in SplitCam pick the VISIT-X preset and paste them, Go Live in SplitCam, "
                 "then GO ONLINE in VXLive."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Get the VXLive server URL + key.</li>"
                 "<li>Pick the VISIT-X preset in SplitCam, paste.</li>"
                 "<li>Go Live, then GO ONLINE in VXLive.</li></ol>",
        "key_how": "In VXLive, choose <strong>Stream with third-party software</strong> and "
                   "select the option for <strong>OBS, SplitCam or XSplit</strong>. VXLive "
                   "supplies a <strong>server URL</strong> and a <strong>stream key</strong>. In "
                   "SplitCam, select <strong>VISIT-X</strong> as the streaming platform, paste "
                   "both, press <strong>Go Live</strong> in SplitCam, then <strong>GO "
                   "ONLINE</strong> in VXLive.",
        "tips": [
            ("VISIT-X is a built-in preset", "You don't enter a raw RTMP URL — SplitCam has "
             "VISIT-X in its platform list, so select it and just paste the server URL and key."),
            ("Two-step go-live", "On VXLive you press Go Live in SplitCam first, then GO ONLINE "
             "in VXLive — both, in that order."),
            ("German-market platform", "VXLive's audience is largely German-speaking — a German "
             "text overlay or title helps you connect with viewers."),
            ("Use a wired connection", "VXLive's two-step go-live means a mid-show drop costs "
             "you both reconnections — a wired link makes that far less likely."),
        ],
        "faq": [
            ("Does VXLive officially support SplitCam?", "Yes — VXModels (VXLive) has a "
             "dedicated official help article on setting up SplitCam, and lists SplitCam "
             "alongside OBS and XSplit as supported broadcasting software."),
            ("How do I connect SplitCam to VXLive?", "In VXLive choose \"Stream with "
             "third-party software\", then in SplitCam select the VISIT-X preset and paste the "
             "server URL and stream key VXLive gives you."),
            ("Do I go live in SplitCam or VXLive?", "Both — press Go Live in SplitCam first, "
             "then GO ONLINE in VXLive."),
            ("Is SplitCam free for VXLive?", "Yes — free, no watermark, no time limit. "
             "VXModels lists SplitCam as supported software, so it is both free and "
             "officially recognised."),
            ("Why does VXModels recommend SplitCam?", "VXModels' official help article "
             "recommends SplitCam specifically to clear up webcam image artifacts and "
             "pixelation and to stabilise the connection — not just as a generic encoder."),
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
            ("Use a wired connection", "VirtWish gives a separate URL and key — a wired link "
             "avoids a reconnect that would send you back through the two Start Broadcast "
             "clicks."),
            ("Test before going live", "Run a short private VirtWish broadcast to confirm the "
             "URL and key landed in the right SplitCam fields."),
        ],
        "faq": [
            ("Where are the VirtWish RTMP details?", "Top-right icon → Profile → Start Broadcast "
             "twice → the OBS section shows the link and stream key."),
            ("Does VirtWish support external encoders?", "Yes — its OBS section provides a "
             "stream URL and key, so SplitCam works."),
            ("Is SplitCam free for VirtWish?", "Yes — free, no watermark, no time limit, so "
             "VirtWish's stream-URL-and-key setup costs nothing beyond the few minutes it "
             "takes."),
            ("What bitrate for VirtWish?", "VirtWish publishes no official cap; 3,500–6,000 "
             "Kbps at 1080p is a safe range. Match SplitCam's resolution to the one set on "
             "VirtWish to avoid rescaling."),
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
        "intro": "XModels is a cam-streaming platform with an in-product "
                 "<strong style='color:var(--text)'>external-encoder option</strong> in the "
                 "model account settings. Free <strong style='color:var(--text)'>SplitCam</strong> "
                 "broadcasts to it with multi-camera scenes, overlays and filters instead of a "
                 "single plain camera.",
        "quick": "Broadcast on XModels with SplitCam: install SplitCam, build your scene, in "
                 "your XModels model account enable the external-encoder option, copy the "
                 "server URL and stream key, paste them into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Enable the external encoder in XModels account settings.</li>"
                 "<li>Paste server URL + key into SplitCam.</li><li>Go Live.</li></ol>",
        "key_how": "In your XModels <strong>model account settings</strong>, enable the "
                   "<strong>broadcast-from-external-encoder</strong> option. XModels supplies a "
                   "<strong>stream key</strong> — copy it into SplitCam. If the option or path "
                   "isn't where you expect, XModels support runs through in-site FAQ chat and "
                   "<strong>info@xmodels.com</strong>; the video guide above also shows it.",
        "tips": [
            ("It's in the account settings", "XModels puts the external-encoder option inside "
             "the model account settings, not a separate broadcast screen."),
            ("Support is chat + email", "XModels has no large public help center — its FAQ chat "
             "on-site and info@xmodels.com are the official support routes."),
            ("Layer overlays in SplitCam", "Tip goals, your name and socials as scene layers — "
             "XModels' basic camera can't add them."),
            ("Run a wired connection", "XModels support is chat-and-email only — a stable "
             "Ethernet link spares you a slow support round-trip if the stream drops."),
        ],
        "faq": [
            ("Does XModels support external encoders?", "Yes — the model account settings "
             "include a broadcast-from-external-encoder option that supplies a stream key, so "
             "SplitCam works."),
            ("Where do I get help with XModels?", "XModels support is via its in-site FAQ chat "
             "and email at info@xmodels.com — there is no large public help center."),
            ("Is SplitCam free for XModels?", "Yes — free, no watermark, no time limit, so "
             "broadcasting to XModels' European network adds no software cost."),
            ("What bitrate for XModels?", "XModels documents no official figure — use "
             "3,500–6,000 Kbps at 1080p and run SplitCam's speed test, since XModels' support "
             "is chat and email only."),
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
                 "1990s. It officially supports external broadcasting through an "
                 "<strong style='color:var(--text)'>External Broadcast Form</strong> — free "
                 "<strong style='color:var(--text)'>SplitCam</strong> sends the stream while the "
                 "form sets your resolution and bitrate.",
        "quick": "Broadcast on Flirt4Free with SplitCam: install SplitCam, build your scene, "
                 "open Flirt4Free's External Broadcast Form, copy the RTMP URL and Stream Name "
                 "and set resolution/bitrate, paste them into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li>"
                 "<li>Open Flirt4Free's External Broadcast Form.</li>"
                 "<li>Paste the RTMP URL + Stream Name into SplitCam.</li>"
                 "<li>Go Live.</li></ol>",
        "key_how": "In the Flirt4Free model area, open the <strong>External Broadcast Form</strong>. "
                   "Unlike most cam sites, Flirt4Free gives you an <strong>RTMP URL</strong> and "
                   "a <strong>Stream Name</strong> (not a \"key\"), plus resolution and bitrate "
                   "fields you fill in on the form itself. Copy the URL and Stream Name into "
                   "SplitCam's server and key fields.",
        "tips": [
            ("It's a Stream Name, not a key", "Flirt4Free labels the credential a Stream Name. "
             "Paste it into SplitCam's stream-key field — it serves the same role."),
            ("Set resolution/bitrate on the form", "Flirt4Free's External Broadcast Form has "
             "its own resolution and bitrate fields — match them to your SplitCam settings so "
             "the picture isn't rescaled."),
            ("An established platform", "Flirt4Free has run since the 1990s — its model tools "
             "are mature and the External Broadcast Form is a documented part of them."),
            ("Use a wired connection", "Flirt4Free's External Broadcast Form fixes your "
             "resolution and bitrate — a wired link keeps the stream matching those values "
             "without Wi-Fi dips."),
        ],
        "faq": [
            ("Does Flirt4Free support external encoders?", "Yes — officially, through its "
             "External Broadcast Form, which provides an RTMP URL and Stream Name. SplitCam "
             "works as the encoder."),
            ("Where do I get the Flirt4Free RTMP details?", "From the External Broadcast Form "
             "in the model area — it shows the RTMP URL, the Stream Name and resolution/bitrate "
             "fields."),
            ("Is SplitCam free for Flirt4Free?", "Yes — free, no watermark, no time limit, "
             "which suits a long-established platform like Flirt4Free where shows can run "
             "long."),
            ("What bitrate for Flirt4Free?", "3,500–6,000 Kbps at 1080p — set the same value in "
             "the External Broadcast Form and in SplitCam."),
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
            ("Alerts stuck? Refresh the cache", "If the alert effects stop appearing, "
             "right-click the MFC Alerts Browser layer and choose \"Refresh cache of current "
             "page\" — that clears a stale overlay."),
            ("Use a wired connection", "MFC Alerts is a live browser overlay reacting to "
             "tips — a wired link keeps both the camera and the alert animations from "
             "stuttering."),
        ],
        "faq": [
            ("What is MFC Alerts?", "A notification system for MyFreeCams that shows video "
             "effects on your stream when viewers tip — added as a Browser overlay in SplitCam."),
            ("Why don't my MFC Alerts show?", "Almost always layer order — the MFC Alerts "
             "Browser layer must sit above the webcam in SplitCam's source list."),
            ("Do I need an account for MFC Alerts?", "Yes — register on mfcalerts.com to get "
             "your personal alerts URL."),
            ("Is SplitCam free for this?", "Yes — SplitCam is free with no watermark or time "
             "limit, and the MFC Alerts browser overlay runs inside it at no extra cost."),
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
                 "so it reacts to tokens. Lovense officially documents a dedicated "
                 "<strong style='color:var(--text)'>Lovense SplitCam Toolset</strong>, and "
                 "SplitCam ships an official Lovense plugin — the integration is supported on "
                 "both sides.",
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
            ("Use the official Lovense SplitCam Toolset", "Lovense publishes a SplitCam-specific "
             "toolset with its own install guide — it adds the toy-activity and tip-alert "
             "overlay built for SplitCam."),
            ("Update the Lovense Cam Extension", "The toolset needs a recent Lovense Cam "
             "Extension (30.1.4 or newer) — update it before going live."),
            ("Keep the toy charged", "A mid-show battery death kills the interactive part — "
             "charge fully before going live."),
            ("Test the token reaction", "Send a small test tip to confirm the toy reacts before "
             "the room is public."),
            ("Mind the version requirements", "The Lovense SplitCam Toolset needs SplitCam "
             "10.4.5 or newer. The Lovense Cam Extension officially covers Chaturbate, "
             "Stripchat, BongaCams, MyFreeCams and CamSoda — for any other site, use Lovense's "
             "Generic URL integration instead."),
        ],
        "faq": [
            ("Does Lovense officially support SplitCam?", "Yes — Lovense documents an official "
             "\"Lovense SplitCam Toolset\" with its own install guide, and SplitCam ships an "
             "official Lovense plugin. The integration is supported on both sides."),
            ("Does the toy connect to SplitCam directly?", "No — the toy pairs with the Lovense "
             "app; SplitCam displays the Lovense overlay and broadcasts your camera."),
            ("Which cam sites support Lovense?", "Lovense's Cam Extension officially supports "
             "Chaturbate, Stripchat, BongaCams, MyFreeCams and CamSoda, with varying support "
             "for others — check the Lovense app for the current list."),
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
            ("Wire up — you can't afford a drop", "Multistreaming multiplies upload load, so "
             "a single Wi-Fi dip can stall every destination at once. A wired connection is "
             "not optional here."),
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
