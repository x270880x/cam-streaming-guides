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
        "desc": "How to stream on Chaturbate with free SplitCam — broadcast token, RTMP setup, multi-camera scenes and overlays. No watermark, no signup.",
        "kw": "how to stream on chaturbate, chaturbate broadcast token, chaturbate rtmp obs, chaturbate external encoder, chaturbate live stream",
        "h1html": 'How to stream on <span class="accent">Chaturbate</span> with SplitCam',
        "h1short": "Stream on Chaturbate",
        "card": "Token-based external encoder setup for Chaturbate.",
        "steps": [
            None,
            ("Build a multi-camera scene", "Add your webcam in SplitCam, then layer in a "
             "second camera or your phone, overlays and beauty or AI-background filters. "
             "Chaturbate's broadcaster shows one flat camera — your composed scene replaces "
             "it."),
            None,
            ("Paste the token into SplitCam", "Open Stream Settings and paste the broadcast "
             "token into the custom RTMP key field. Chaturbate has huge headroom — set 1080p "
             "at 3,500–6,000 Kbps with a 2-second keyframe."),
            ("Go Live", "Press Go Live in SplitCam — your scene reaches the room in about 10 "
             "seconds. Chaturbate's low-latency delivery keeps tips and reactions in sync "
             "with what you do."),
        ],
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
        "desc": "How to stream on CAM4 with free SplitCam — External Encoder, stream key, geo-blocking and scene overlays. No watermark, free guide.",
        "kw": "how to stream on cam4, cam4.com, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
        "h1html": 'How to stream on <span class="accent">CAM4</span> with SplitCam',
        "h1short": "Stream on CAM4",
        "card": "External Encoder setup for CAM4, with geo-controls.",
        "steps": [
            None,
            ("Set up your scene and geo-blocking", "Add your webcam and overlays in SplitCam, "
             "and decide on CAM4 which countries to hide your show from before you start."),
            None,
            ("Paste the CAM4 stream key", "Paste the key into SplitCam's Stream Settings — a "
             "green slider confirms it. Keep the bitrate near 3,000 Kbps; CAM4's ingest caps "
             "lower than most sites."),
            ("Go Live", "Press Go Live in SplitCam, then start the broadcast on CAM4. Watch "
             "that the slider stays green — red means re-check the key."),
        ],
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
        "desc": "How to stream on BongaCams with free SplitCam — External Encoder setup, multi-camera scenes, overlays and AI background. No watermark.",
        "kw": "bongacams, bongcams, how to stream on bongacams, bongacams external encoder, bongacams rtmp obs, bongacams broadcast settings",
        "h1html": 'How to stream on <span class="accent">BongaCams</span> with SplitCam',
        "h1short": "Stream on BongaCams",
        "card": "External Encoder setup for BongaCams.",
        "steps": [
            None,
            ("Match the scene resolution", "Add your webcam and overlays in SplitCam, and set "
             "the same resolution BongaCams uses — e.g. 1280×720 on both sides — so the "
             "picture isn't rescaled."),
            None,
            ("Paste the BongaCams URL and key", "Paste the server URL and stream key into "
             "SplitCam's custom RTMP fields. If BongaCams never showed an External Encoder "
             "button, contact support to enable it first."),
            ("Go Live", "Press Go Live in SplitCam to start broadcasting to BongaCams. Do a "
             "short private test first to confirm camera and audio."),
        ],
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
        "title": "How to Stream on Stripchat with SplitCam — Strip Cam Setup",
        "desc": "How to stream on Stripchat — the strip cam platform — with free SplitCam. External software setup, token key, scenes and overlays.",
        "kw": "strip cam, stripchat live stream, how to stream on stripchat, stripchat external software, stripchat stream key, stripchat rtmp obs",
        "h1html": 'How to stream on <span class="accent">Stripchat</span> with SplitCam',
        "h1short": "Stream on Stripchat",
        "card": "External-software setup for Stripchat broadcasts.",
        "steps": [
            None,
            ("Build your scene at the site resolution", "Add your webcam, overlays and "
             "filters in SplitCam. Set SplitCam's resolution to exactly match the one chosen "
             "on Stripchat, or the video pixelates."),
            None,
            ("Paste the Stripchat token", "Paste the token-based stream key into SplitCam's "
             "RTMP key field. Stay well above Stripchat's 2 Mbps minimum — aim for "
             "3,500–6,000 Kbps at 1080p."),
            ("Go Live", "Press Go Live in SplitCam, then click Start Show on Stripchat — "
             "switching to external software alone doesn't make you public."),
        ],
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
        "desc": "How to go live on OnlyFans with free SplitCam — Authorization sign-in or OBS Key, multi-camera scenes and overlays. No watermark.",
        "kw": "how to go live on onlyfans, onlyfans live stream, onlyfans authorization splitcam, onlyfans obs key, onlyfans streaming software",
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
        "desc": "How to stream on CamPlace with free SplitCam — external encoder, RTMP key, scenes and overlays. Step-by-step guide, no watermark.",
        "kw": "how to stream on camplace, camplace broadcasting software, camplace rtmp, camplace external encoder, camplace stream key",
        "h1html": 'How to stream on <span class="accent">CamPlace</span> with SplitCam',
        "h1short": "Stream on CamPlace",
        "card": "External encoder setup for CamPlace broadcasts.",
        "steps": [
            None,
            ("Build your scene", "Add your webcam in SplitCam and layer in overlays, a second "
             "camera and filters — extras CamPlace's basic broadcaster can't produce."),
            None,
            ("Paste the CamPlace server URL and key", "Paste both into SplitCam's custom RTMP "
             "fields. CamPlace publishes no encoder specs, so follow the video guide above "
             "and let the speed test set your bitrate."),
            ("Go Live", "Press Go Live in SplitCam to start the CamPlace broadcast. Run a "
             "short private test first, since there are no official docs to fall back on."),
        ],
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
        "title": "How to Stream on CamSoda Live with SplitCam — Free Setup",
        "desc": "How to go CamSoda live with free SplitCam — Use OBS Broadcaster, regional servers, scenes and overlays. No watermark, free guide.",
        "kw": "camsoda live, how to stream on camsoda, camsoda obs broadcaster, camsoda rtmp obs, camsoda live broadcast",
        "h1html": 'How to stream on <span class="accent">CamSoda</span> with SplitCam',
        "h1short": "Stream on CamSoda",
        "card": "External encoder setup for CamSoda broadcasts.",
        "steps": [
            None,
            ("Build your scene", "Add your webcam, overlays and filters in SplitCam. CamSoda "
             "is known for interactive show formats — overlays for goals and games fit well "
             "here."),
            None,
            ("Paste the CamSoda server URL and key", "Paste both into SplitCam, choosing the "
             "regional CamSoda server (NA, Europe, Asia, etc.) nearest you. Cap quality at "
             "1080p/30 fps, ~6,000 Kbps."),
            ("Go Live", "Press Go Live in SplitCam to broadcast to CamSoda. Note you must "
             "finish CamSoda's verification before you can receive tips."),
        ],
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
        "desc": "How to stream on Streamate with free SplitCam — built-in channel, SM Connect key, scenes and overlays. No watermark, quick setup.",
        "kw": "streamate, streamate sm connect, how to stream on streamate, streamate broadcasting software, streamate rtmp",
        "h1html": 'How to stream on <span class="accent">Streamate</span> with SplitCam',
        "h1short": "Stream on Streamate",
        "card": "Streamate is a built-in SplitCam channel — quick setup.",
        "steps": [
            None,
            ("Build your scene", "Add your webcam, overlays and filters in SplitCam before "
             "you fetch the key."),
            None,
            ("Add Streamate as a channel", "In SplitCam open Stream Settings → Add Channel, "
             "pick Streamate from the built-in list and paste the SM Connect key — no manual "
             "RTMP URL needed. Lock the resolution to 1080p."),
            ("Go Live", "Press Go Live in SplitCam — a green slider confirms the connection. "
             "The feed is adaptive, so a lower bitrate on a still shot is normal."),
        ],
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
        "desc": "How to stream on StreamRay cam with free SplitCam — URL from chat window, OBS Broadcaster mode, scenes and overlays. No watermark.",
        "kw": "streamray, streamray cam, how to stream on streamray, streamray obs broadcaster, streamray rtmp",
        "h1html": 'How to stream on <span class="accent">StreamRay</span> with SplitCam',
        "h1short": "Stream on StreamRay",
        "card": "URL-from-chat external encoder setup for StreamRay.",
        "steps": [
            None,
            ("Build your scene", "Add your webcam and overlays in SplitCam before you enable "
             "StreamRay's OBS Broadcaster."),
            None,
            ("Paste the StreamRay URL — leave the key empty", "Copy the stream URL StreamRay "
             "posts in the chat window into SplitCam's server field. StreamRay authenticates "
             "by URL only, so leave the stream-key field empty."),
            ("Go Live", "Press Go Live in SplitCam to start broadcasting to StreamRay. Test "
             "privately first to confirm the URL pasted correctly."),
        ],
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
        "desc": "How to stream on XLoveCam with free SplitCam — RTMP link and key, regional servers, scenes and overlays. No watermark, free guide.",
        "kw": "xlovecam, x love cam, how to stream on xlovecam, xlovecam rtmp link, xlovecam stream key",
        "h1html": 'How to stream on <span class="accent">XLoveCam</span> with SplitCam',
        "h1short": "Stream on XLoveCam",
        "card": "RTMP link + key setup for XLoveCam broadcasts.",
        "steps": [
            None,
            ("Build your scene", "Add your webcam, overlays and a clear text overlay in your "
             "language — XLoveCam's audience is European and multilingual."),
            None,
            ("Paste the XLoveCam link and key", "Copy both the RTMP link and the separate "
             "stream key from My Account → settings into SplitCam. Pick the regional server "
             "nearest you to cut latency."),
            ("Go Live", "Press Go Live in SplitCam, then use Start your show on XLoveCam."),
        ],
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
        "desc": "How to stream on SoulCams with free SplitCam — OBS-settings setup, RTMP server and key, multi-camera scenes and overlays.",
        "kw": "soul cams, soulcams, how to stream on soulcams, soulcams obs, soulcams rtmp, soulcams broadcast",
        "h1html": 'How to stream on <span class="accent">SoulCams</span> with SplitCam',
        "h1short": "Stream on SoulCams",
        "card": "RTMP setup for SoulCams broadcasts.",
        "steps": [
            None,
            ("Build your scene", "Add your webcam, overlays and filters in SplitCam, and "
             "decide on SoulCams which countries to block before going online."),
            None,
            ("Paste the SoulCams server and key", "From SoulCams' OBS settings, copy the "
             "RTMP server and key — shown together — into SplitCam's custom RTMP fields."),
            ("Go Live", "Press Go Live in SplitCam to broadcast to SoulCams. The OBS details "
             "only appear after Go Online, so do that first."),
        ],
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
        "title": "How to Stream on ImLive with SplitCam — Im Live Stream Setup",
        "desc": "Im Live stream setup with free SplitCam — ImLive uses webcam directly (no RTMP), connect SplitCam as virtual camera with scenes.",
        "kw": "im live stream, imlive splitcam, how to stream on imlive, imlive virtual camera, imlive webcam, im live cam",
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
        "desc": "How to stream on VXLive (VXModels / VISIT-X) with free SplitCam — official VISIT-X preset, server and key, scenes. No watermark.",
        "kw": "vxlive, visit-x, vxmodels splitcam, how to stream on vxlive, visit-x stream, vxlive rtmp",
        "h1html": 'How to stream on <span class="accent">VXLive</span> with SplitCam',
        "h1short": "Stream on VXLive",
        "card": "External encoder setup for VXLive broadcasts.",
        "steps": [
            None,
            ("Build your scene", "Add your webcam and overlays in SplitCam — a German title "
             "or text overlay suits VXLive's largely German-speaking audience."),
            None,
            ("Use the VISIT-X preset", "In SplitCam pick VISIT-X from the platform list and "
             "paste the server URL and key VXLive gives you under \"Stream with third-party "
             "software\"."),
            ("Go Live in two steps", "Press Go Live in SplitCam first, then click GO ONLINE "
             "in VXLive — both, in that order."),
        ],
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
        "desc": "How to stream on VirtWish with free SplitCam — Profile → Start Broadcast OBS section, stream URL and key, scenes and overlays.",
        "kw": "virtwish, how to stream on virtwish, virtwish broadcasting software, virtwish rtmp, virtwish stream key, virtwish obs",
        "h1html": 'How to stream on <span class="accent">VirtWish</span> with SplitCam',
        "h1short": "Stream on VirtWish",
        "card": "Stream URL + key setup for VirtWish broadcasts.",
        "steps": [
            None,
            ("Build your scene", "Add your webcam, overlays and filters in SplitCam before "
             "opening VirtWish's broadcast settings."),
            None,
            ("Paste the VirtWish URL and key", "Copy the link from the first line of "
             "VirtWish's OBS section into SplitCam's Stream URL field, and the Stream Key "
             "into the key field separately."),
            ("Go Live", "Press Go Live in SplitCam to start the VirtWish broadcast. Test "
             "privately first to confirm the URL and key landed correctly."),
        ],
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
        "desc": "How to stream on XModels with free SplitCam — external encoder option in model account settings, RTMP key, scenes and overlays.",
        "kw": "xmodels, how to stream on xmodels, xmodels broadcasting software, xmodels rtmp, xmodels external encoder",
        "h1html": 'How to stream on <span class="accent">XModels</span> with SplitCam',
        "h1short": "Stream on XModels",
        "card": "External encoder setup for XModels broadcasts.",
        "steps": [
            None,
            ("Build your scene", "Add your webcam, overlays and filters in SplitCam — extras "
             "XModels' basic camera can't add."),
            None,
            ("Paste the XModels key", "Enable the external-encoder option in your XModels "
             "model account settings and paste the stream key into SplitCam. If the option "
             "isn't where expected, XModels' FAQ chat and info@xmodels.com can help."),
            ("Go Live", "Press Go Live in SplitCam, then start the broadcast in your XModels "
             "account."),
        ],
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
        "desc": "How to stream on Flirt for Free cam with free SplitCam — External Broadcast Form, RTMP URL and Stream Name, scenes and overlays.",
        "kw": "flirt for free cam, flirt 4 free cam, flirt4free, how to stream on flirt4free, flirt4free external broadcast, flirt4free rtmp",
        "h1html": 'How to stream on <span class="accent">Flirt4Free</span> with SplitCam',
        "h1short": "Stream on Flirt4Free",
        "card": "External encoder setup for Flirt4Free broadcasts.",
        "steps": [
            None,
            ("Build your scene", "Add your webcam, overlays and filters in SplitCam."),
            None,
            ("Paste the Flirt4Free URL and Stream Name", "From the External Broadcast Form, "
             "copy the RTMP URL and the Stream Name into SplitCam's server and key fields, "
             "and set the same resolution and bitrate on the form as in SplitCam."),
            ("Go Live", "Press Go Live in SplitCam, then start your show from the Flirt4Free "
             "model area."),
        ],
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
        "desc": "Add MFC Alerts (MyFreeCams tip alerts) to your stream with free SplitCam — Browser layer setup, animated effects on viewer tips.",
        "kw": "mfc alerts, myfreecams alerts, how to add mfc alerts, mfcalerts splitcam, myfreecams tip alerts, myfreecams alerts overlay",
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
        "desc": "How to add a Lovense interactive toy to your stream with free SplitCam — Lovense SplitCam Toolset, on-screen tip alerts and reactions.",
        "kw": "how to add lovense to stream, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense interactive toy streaming",
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
        "desc": "Broadcast to multiple cam sites at once with free SplitCam — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat. One click, no watermark.",
        "kw": "broadcast to multiple cam sites, multistream cam sites, stream to chaturbate and bongacams at once, cam multistreaming software",
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
    {
        "slug": "livejasmin", "name": "LiveJasmin",
        "title": "How to Broadcast on LiveJasmin with SplitCam — HD External Encoder",
        "desc": "Broadcast on LiveJasmin with free SplitCam — Model Center external encoder, HD 1080p setup, multi-camera scenes and overlays. No watermark, no signup.",
        "kw": "livejasmin broadcast, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key, livejasmin model setup, jasmin live",
        "h1html": 'How to broadcast on <span class="accent">LiveJasmin</span> with SplitCam',
        "h1short": "Broadcast on LiveJasmin",
        "card": "External encoder setup for LiveJasmin's HD-only Model Center.",
        "intro": "LiveJasmin is the flagship of Docler Holding — one of the largest cam networks in the world and an HD-only platform. Its preferred broadcaster is the proprietary <strong>JasminCAM</strong> client, but the Model Center also exposes a standard <strong>external encoder</strong> path that free <strong style='color:var(--text)'>SplitCam</strong> connects to — letting you stream with multi-camera scenes, beauty filters and overlays on the same HD stream.",
        "quick": "Broadcast on LiveJasmin with SplitCam: install SplitCam, build your HD scene, in the Model Center go to <em>Settings → Broadcast → External Encoder</em>, copy the server URL and stream key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + HD scene.</li><li>Get URL and stream key from the Model Center.</li><li>Paste into SplitCam.</li><li>Press Go Live.</li></ol>",
        "key_how": "Log in to <strong>modelcenter.livejasmin.com</strong>, open <strong>Settings → Broadcast → External Encoder</strong>. The Model Center reveals a <strong>server URL</strong> and <strong>stream key</strong> tied to your account — copy both into SplitCam's custom RTMP fields. <strong>Note:</strong> new accounts must be approved (48–72 hours) before the external encoder option appears, and the platform enforces HD-only output.",
        "tips": [
            ("HD or you get de-ranked", "LiveJasmin is HD-only — anything under 1280×720 risks being shown only on lower-paying lists, anything under 1080p loses 'Premium' eligibility. Push 1920×1080 at 30 fps, 4,000–6,000 Kbps."),
            ("JasminCAM vs external encoder", "Docler's own JasminCAM client gives the cleanest HD compliance, but external encoders (OBS, SplitCam, vMix) are officially supported once your account is approved — they unlock multi-camera scenes and overlays JasminCAM can't do."),
            ("Free chat ≠ private show", "Free chat is preview-only — no nudity. Private and Gold shows are where the model earns. Plan your scene to look strong dressed AND in show mode."),
            _T_ETH,
        ],
        "faq": [
            ("Does LiveJasmin officially support external encoders like SplitCam?", "Yes — the Model Center includes an External Encoder option in Settings → Broadcast. JasminCAM is the recommended client, but OBS, SplitCam and other RTMP encoders are explicitly listed as supported once your model account is approved."),
            ("Where do I get my LiveJasmin stream key?", "Inside the Model Center: Settings → Broadcast → External Encoder. Both the server URL and the unique stream key appear there — copy both into SplitCam's custom RTMP fields. The key is tied to your account; treat it like a password."),
            ("What bitrate should I use for LiveJasmin?", "LiveJasmin is HD-only — target 1920×1080 at 30 fps, 4,000–6,000 Kbps with a 2-second keyframe interval. Anything noticeably under that loses the Premium label and gets de-ranked."),
            ("Is SplitCam free to use with LiveJasmin?", "Yes — SplitCam is free, no watermark and no time limit. The only cost is hitting LiveJasmin's HD requirements, which SplitCam handles natively with its 1080p scene composition and beauty filters."),
        ],
        "steps": [
            ("Download and install SplitCam", "SplitCam is free live-streaming software for Windows and macOS — no signup, no card, no watermark. It's the encoder that sends your HD video to LiveJasmin."),
            ("Build your HD scene", "Open SplitCam and add your webcam in 1080p mode. Layer in overlays, text, a second camera or your phone, beauty filters or an AI background — LiveJasmin requires HD quality and your composed scene needs to look premium throughout free chat AND private shows."),
            ("Get your LiveJasmin URL and stream key", "Log in to <strong>modelcenter.livejasmin.com</strong> (your account must be approved first — typically 48–72 hours after signup). Open <strong>Settings → Broadcast → External Encoder</strong>. The page reveals a <strong>server URL</strong> and unique <strong>stream key</strong>. Copy both."),
            ("Connect SplitCam to LiveJasmin", "In SplitCam open <strong>Stream Settings</strong>, paste the LiveJasmin server URL and stream key into the custom RTMP fields. Set bitrate to 4,000–6,000 Kbps at 1920×1080, 30 fps, with a 2-second keyframe. Run the built-in speed test first — HD streams are demanding."),
            ("Click Go Live", "Press <strong>Go Live</strong> in SplitCam, then go online in the LiveJasmin Model Center. Within ~10 seconds your HD feed reaches LiveJasmin's network. Subsequent broadcasts are one click — open SplitCam, Go Live, then go online on LiveJasmin."),
        ],
    },
    {
        "slug": "myfreecams", "name": "MyFreeCams",
        "title": "How to Broadcast on MyFreeCams (MFC) with SplitCam — Model Web Broadcaster Bypass",
        "desc": "Broadcast on MyFreeCams with free SplitCam — Model Admin external broadcaster, MFC token economy, multi-camera scenes, overlays. No watermark, no signup.",
        "kw": "myfreecams broadcast, mfc external broadcaster, myfreecams obs, mfc rtmp, mfc stream key, model admin, mfc token",
        "h1html": 'How to broadcast on <span class="accent">MyFreeCams</span> with SplitCam',
        "h1short": "Broadcast on MyFreeCams",
        "card": "External broadcaster setup for MFC's token-based Model Admin.",
        "intro": "MyFreeCams (MFC) is one of the oldest cam platforms — pure token economy, no model approval gauntlet, and a loyal Premium-member base. Its default <em>Model Web Broadcaster</em> is a single-camera browser tool, but Model Admin also exposes an <strong>External Broadcaster</strong> option that free <strong style='color:var(--text)'>SplitCam</strong> connects to — unlocking multi-camera scenes, overlays and filters on the same token stream.",
        "quick": "Broadcast on MyFreeCams with SplitCam: install SplitCam, build your scene, in <em>Model Admin → Broadcaster</em> switch from Web Broadcaster to External Broadcaster, copy the server URL and stream key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li><li>Get URL and stream key from Model Admin.</li><li>Paste into SplitCam.</li><li>Press Go Live.</li></ol>",
        "key_how": "Log in to MyFreeCams, open <strong>Model Admin → Broadcaster</strong>, and switch from <em>Web Broadcaster</em> to <strong>External Broadcaster</strong>. The page reveals a <strong>server URL</strong> (rtmp://publish.myfreecams.com…) and a <strong>stream key</strong> tied to your model account — copy both into SplitCam's custom RTMP fields. The key is account-bound; treat it like a password and reset if it leaks.",
        "tips": [
            ("MFC tokens, not subscriptions", "MFC is pure tipping/token economy — Premium members can private, but the bread-and-butter income is free chat tips. Plan a scene that earns dressed and casual, not just nude shows."),
            ("Web Broadcaster vs External — choose once", "The default Web Broadcaster is single-camera, single-source. External Broadcaster unlocks multi-scene, overlays, beauty filters via SplitCam/OBS. Switch in Model Admin → Broadcaster before going live."),
            ("MFC Alerts integration", "Animated tip alerts on screen come from mfcalerts.com — add the alert URL as a Browser layer in SplitCam, above the camera. See our MFC Alerts guide for the full overlay setup."),
            _T_ETH,
        ],
        "faq": [
            ("Does MyFreeCams officially support external broadcasters like SplitCam?", "Yes — Model Admin has an External Broadcaster option that exposes a standard RTMP server URL and stream key. OBS, SplitCam, vMix and other RTMP encoders all work; MFC explicitly supports the option in its model documentation."),
            ("Where do I find my MFC stream key?", "Model Admin → Broadcaster → switch to External Broadcaster. Both the server URL (rtmp://publish.myfreecams.com…) and the stream key appear there. Copy both into SplitCam's custom RTMP fields."),
            ("What bitrate should I use for MyFreeCams?", "MFC accepts up to ~6,000 Kbps with a 2-second keyframe interval. Push 1920×1080 at 30 fps, 3,500–6,000 Kbps — your upload is the real limit. Run SplitCam's speed test first."),
            ("Is SplitCam free to use with MyFreeCams?", "Yes — SplitCam is free, no watermark and no time limit. The External Broadcaster option itself is free in Model Admin. Total broadcaster cost: zero."),
        ],
        "steps": [
            ("Download and install SplitCam", "SplitCam is free live-streaming software for Windows and macOS — no signup, no card, no watermark. It's the encoder that sends your video to MyFreeCams."),
            ("Build your scene", "Open SplitCam and add your webcam. Layer in overlays, text, a second camera or your phone, beauty filters or an AI background — all applied live before the stream leaves your PC. Consider adding the mfcalerts.com URL as a Browser layer for animated tip alerts."),
            ("Switch to External Broadcaster in Model Admin", "Log in to MyFreeCams. Open <strong>Model Admin → Broadcaster</strong>. Switch from <em>Web Broadcaster</em> to <strong>External Broadcaster</strong>. The page reveals a <strong>server URL</strong> and unique <strong>stream key</strong>. Copy both."),
            ("Connect SplitCam to MyFreeCams", "In SplitCam open <strong>Stream Settings</strong>, paste the MFC server URL and stream key into the custom RTMP fields. Set bitrate to 3,500–6,000 Kbps at 1920×1080, 30 fps, with a 2-second keyframe interval. Run the built-in speed test first."),
            ("Click Go Live", "Press <strong>Go Live</strong> in SplitCam. Within ~10 seconds your stream reaches MyFreeCams. Subsequent broadcasts are one click — open SplitCam, Go Live."),
        ],
    },
    {
        "slug": "cherry-tv", "name": "Cherry.tv",
        "title": "How to Broadcast on Cherry.tv with SplitCam — Web3-Friendly External Encoder",
        "desc": "Broadcast on Cherry.tv with free SplitCam — Streamer Dashboard external encoder, crypto-friendly cam platform, multi-camera scenes. No watermark, no signup.",
        "kw": "cherry tv broadcast, cherry.tv obs, cherry tv external encoder, cherry.tv rtmp, cherry.tv stream key, cherry tv streamer, web3 cam",
        "h1html": 'How to broadcast on <span class="accent">Cherry.tv</span> with SplitCam',
        "h1short": "Broadcast on Cherry.tv",
        "card": "External encoder setup for Cherry.tv's Streamer Dashboard.",
        "intro": "Cherry.tv is a newer, fast-growing cam platform with a Web3 angle — crypto-friendly payouts and lower entry barriers than legacy networks like LiveJasmin. The default broadcaster is browser-based, but the <strong>Streamer Dashboard</strong> also exposes a standard <strong>external encoder</strong> path that free <strong style='color:var(--text)'>SplitCam</strong> connects to — letting you stream with multi-camera scenes, overlays and filters.",
        "quick": "Broadcast on Cherry.tv with SplitCam: install SplitCam, build your scene, in the Streamer Dashboard open <em>Broadcast Settings → External Encoder</em>, copy the server URL and stream key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li><li>Get URL and stream key from the Streamer Dashboard.</li><li>Paste into SplitCam.</li><li>Press Go Live.</li></ol>",
        "key_how": "Log in to your Cherry.tv streamer account, open the <strong>Streamer Dashboard</strong> and navigate to <strong>Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and <strong>stream key</strong> tied to your account — copy both into SplitCam's custom RTMP fields. New streamer accounts need to complete basic verification (usually fast — Cherry.tv has a lighter onboarding than legacy cam networks) before the external encoder option is fully active.",
        "tips": [
            ("Lighter entry, growing traffic", "Cherry.tv's onboarding is faster than legacy platforms (no 72-hour Docler-style review). Combined with growing traffic, it's a good early-mover spot to build a follower base before competition tightens."),
            ("Crypto payouts available", "Cherry.tv supports crypto withdrawal alongside standard fiat — useful if you're in a region where traditional cam-network payouts are slow or restricted."),
            ("Browser broadcaster vs external", "The default browser broadcaster is convenient but single-source. SplitCam via External Encoder unlocks multi-camera scenes, overlays, beauty filters and AI background that the browser tool can't do."),
            _T_ETH,
        ],
        "faq": [
            ("Does Cherry.tv officially support external encoders like SplitCam?", "Yes — the Streamer Dashboard includes External Encoder under Broadcast Settings. The platform provides a standard RTMP server URL and stream key; OBS, SplitCam and other RTMP encoders all connect."),
            ("Where do I get my Cherry.tv stream key?", "Streamer Dashboard → Broadcast Settings → External Encoder. Both the server URL and the stream key appear there — copy both into SplitCam's custom RTMP fields. The key is account-bound; treat it like a password."),
            ("What bitrate should I use for Cherry.tv?", "Cherry.tv accepts standard cam-quality settings — push 1920×1080 at 30 fps, 3,500–6,000 Kbps with a 2-second keyframe. Run SplitCam's built-in speed test first."),
            ("Is SplitCam free to use with Cherry.tv?", "Yes — SplitCam is free, no watermark and no time limit. Cherry.tv's external encoder option is free to enable. Total broadcaster cost: zero."),
        ],
        "steps": [
            ("Download and install SplitCam", "SplitCam is free live-streaming software for Windows and macOS — no signup, no card, no watermark. It's the encoder that sends your video to Cherry.tv."),
            ("Build your scene", "Open SplitCam and add your webcam. Layer in overlays, text, a second camera or your phone, beauty filters or an AI background — all applied live. Cherry.tv's audience is younger and platform-savvy, so a polished scene helps stand out."),
            ("Get your Cherry.tv URL and stream key", "Log in to your Cherry.tv streamer account, open the <strong>Streamer Dashboard</strong>, navigate to <strong>Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and unique <strong>stream key</strong>. Copy both."),
            ("Connect SplitCam to Cherry.tv", "In SplitCam open <strong>Stream Settings</strong>, paste the Cherry.tv server URL and stream key into the custom RTMP fields. Set bitrate to 3,500–6,000 Kbps at 1920×1080, 30 fps, with a 2-second keyframe. Run the built-in speed test first."),
            ("Click Go Live", "Press <strong>Go Live</strong> in SplitCam, then go online from the Streamer Dashboard on Cherry.tv. Within ~10 seconds your stream reaches Cherry.tv. Subsequent broadcasts are one click — open SplitCam, Go Live, then go online on Cherry.tv."),
        ],
    },
    {
        "slug": "amateurtv", "name": "AmateurTV",
        "title": "How to Broadcast on AmateurTV with SplitCam — Spanish-Speaking Cam Network",
        "desc": "Broadcast on AmateurTV with free SplitCam — Model Panel external encoder, Spanish/Latin American cam network, multi-camera scenes. No watermark, no signup.",
        "kw": "amateurtv broadcast, amateur.tv obs, amateurtv external encoder, amateurtv rtmp, amateurtv stream key, modelos amateur tv",
        "h1html": 'How to broadcast on <span class="accent">AmateurTV</span> with SplitCam',
        "h1short": "Broadcast on AmateurTV",
        "card": "External encoder setup for AmateurTV's Spanish-speaking network.",
        "intro": "AmateurTV is the leading Spanish-speaking cam network — strong audience in Spain, Mexico, Argentina and across LatAm. The default Model Panel broadcaster works in-browser, but it also exposes a standard <strong>external encoder</strong> path that free <strong style='color:var(--text)'>SplitCam</strong> connects to — letting you stream with multi-camera scenes, beauty filters and overlays to a hispanophone audience that doesn't get well served on US-centric networks.",
        "quick": "Broadcast on AmateurTV with SplitCam: install SplitCam, build your scene, in the Model Panel open <em>Broadcast Settings → External Encoder</em>, copy the server URL and stream key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li><li>Get URL and stream key from the Model Panel.</li><li>Paste into SplitCam.</li><li>Press Go Live.</li></ol>",
        "key_how": "Log in to your AmateurTV model account, open the <strong>Model Panel</strong> and navigate to <strong>Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and <strong>stream key</strong> tied to your account — copy both into SplitCam's custom RTMP fields. New model accounts need ID verification before going live.",
        "tips": [
            ("Hispanophone audience first", "AmateurTV's traffic is overwhelmingly Spanish-speaking — Spain by daytime, LatAm in evening US hours. Stream titles, scene text and overlays in Spanish dramatically out-perform English-only on this network."),
            ("LatAm timezone is your prime", "Peak traffic correlates with LatAm evening hours (UTC-3 to UTC-6). If you're flexible, broadcasting late-evening CET / early-morning Asian hours hits both Spain and LatAm peaks."),
            ("Solid mid-tier payouts", "Not the highest RPM in the industry, but stable — AmateurTV pays consistently and the hispanophone niche has less competition than top US networks."),
            _T_ETH,
        ],
        "faq": [
            ("Does AmateurTV officially support external encoders like SplitCam?", "Yes — the Model Panel includes an External Encoder option under Broadcast Settings. AmateurTV provides a standard RTMP server URL and stream key; OBS, SplitCam, vMix and other RTMP encoders all connect."),
            ("Where do I get my AmateurTV stream key?", "Model Panel → Broadcast Settings → External Encoder. Both the server URL and stream key appear there. Copy both into SplitCam's custom RTMP fields. The key is account-bound."),
            ("What bitrate should I use for AmateurTV?", "Standard cam-quality settings — push 1920×1080 at 30 fps, 3,500–6,000 Kbps with a 2-second keyframe interval. Run SplitCam's built-in speed test first."),
            ("Is SplitCam free to use with AmateurTV?", "Yes — SplitCam is free, no watermark and no time limit. AmateurTV's external encoder option is free to enable."),
        ],
        "steps": [
            ("Download and install SplitCam", "SplitCam is free live-streaming software for Windows and macOS — no signup, no card, no watermark. It's the encoder that sends your video to AmateurTV."),
            ("Build your scene", "Open SplitCam and add your webcam. Layer in overlays, text, a second camera or your phone, beauty filters or an AI background. Use Spanish text on overlays for AmateurTV's hispanophone audience."),
            ("Get your AmateurTV URL and stream key", "Log in to your AmateurTV model account, open the <strong>Model Panel</strong>, navigate to <strong>Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and unique <strong>stream key</strong>. Copy both."),
            ("Connect SplitCam to AmateurTV", "In SplitCam open <strong>Stream Settings</strong>, paste the AmateurTV server URL and stream key into the custom RTMP fields. Set bitrate to 3,500–6,000 Kbps at 1920×1080, 30 fps, with a 2-second keyframe. Run the built-in speed test first."),
            ("Click Go Live", "Press <strong>Go Live</strong> in SplitCam, then go online from the Model Panel on AmateurTV. Within ~10 seconds your stream reaches the network. Subsequent broadcasts are one click — open SplitCam, Go Live."),
        ],
    },
    {
        "slug": "camster", "name": "Camster",
        "title": "How to Broadcast on Camster with SplitCam — Model Hub External Encoder",
        "desc": "Broadcast on Camster with free SplitCam — Model Hub external encoder, established mid-tier cam platform, multi-camera scenes and overlays. No watermark, no signup.",
        "kw": "camster broadcast, camster.com obs, camster external encoder, camster rtmp, camster stream key, camster model hub",
        "h1html": 'How to broadcast on <span class="accent">Camster</span> with SplitCam',
        "h1short": "Broadcast on Camster",
        "card": "External encoder setup for Camster's Model Hub.",
        "intro": "Camster is an established mid-tier cam platform — smaller than Chaturbate or LiveJasmin but with a loyal user base and fair payouts. The default Model Hub broadcaster works in-browser, but it also exposes a standard <strong>external encoder</strong> path that free <strong style='color:var(--text)'>SplitCam</strong> connects to — letting you stream with multi-camera scenes, overlays and filters that the built-in broadcaster can't deliver.",
        "quick": "Broadcast on Camster with SplitCam: install SplitCam, build your scene, in the Model Hub open <em>Broadcast Settings → External Encoder</em>, copy the server URL and stream key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li><li>Get URL and stream key from the Model Hub.</li><li>Paste into SplitCam.</li><li>Press Go Live.</li></ol>",
        "key_how": "Log in to your Camster model account, open the <strong>Model Hub</strong> and navigate to <strong>Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and <strong>stream key</strong> tied to your account — copy both into SplitCam's custom RTMP fields. The key is account-bound; treat it like a password.",
        "tips": [
            ("Mid-tier means less competition", "Camster has steady traffic but fewer broadcasters than top-tier networks — easier to land on the front page with a polished scene and consistent schedule."),
            ("Browser broadcaster vs external", "The default browser broadcaster is single-source. SplitCam via External Encoder unlocks multi-camera scenes, overlays, beauty filters and AI background."),
            ("Stable payouts, fair splits", "Camster's revenue split is fair for the mid-tier — not the highest in the industry, but reliable monthly payouts and few model complaints about payment delays."),
            _T_ETH,
        ],
        "faq": [
            ("Does Camster officially support external encoders like SplitCam?", "Yes — the Model Hub includes an External Encoder option under Broadcast Settings. Standard RTMP server URL and stream key; OBS, SplitCam and other RTMP encoders all connect."),
            ("Where do I get my Camster stream key?", "Model Hub → Broadcast Settings → External Encoder. Both the server URL and stream key appear there. Copy both into SplitCam's custom RTMP fields."),
            ("What bitrate should I use for Camster?", "Standard cam-quality settings — push 1920×1080 at 30 fps, 3,500–6,000 Kbps with a 2-second keyframe interval. Run SplitCam's built-in speed test first."),
            ("Is SplitCam free to use with Camster?", "Yes — SplitCam is free, no watermark and no time limit. Camster's external encoder option is free."),
        ],
        "steps": [
            ("Download and install SplitCam", "SplitCam is free live-streaming software for Windows and macOS — no signup, no card, no watermark."),
            ("Build your scene", "Open SplitCam and add your webcam. Layer in overlays, text, a second camera or your phone, beauty filters or an AI background — all applied live."),
            ("Get your Camster URL and stream key", "Log in to your Camster model account, open the <strong>Model Hub</strong>, navigate to <strong>Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and unique <strong>stream key</strong>. Copy both."),
            ("Connect SplitCam to Camster", "In SplitCam open <strong>Stream Settings</strong>, paste the Camster server URL and stream key into the custom RTMP fields. Set bitrate to 3,500–6,000 Kbps at 1920×1080, 30 fps, with a 2-second keyframe. Run the built-in speed test first."),
            ("Click Go Live", "Press <strong>Go Live</strong> in SplitCam, then go online from the Model Hub on Camster. Within ~10 seconds your stream reaches Camster."),
        ],
    },
    {
        "slug": "camversity", "name": "Camversity",
        "title": "How to Broadcast on Camversity with SplitCam — Performer Dashboard External Encoder",
        "desc": "Broadcast on Camversity with free SplitCam — Performer Dashboard external encoder, growing independent cam platform, multi-camera scenes. No watermark, no signup.",
        "kw": "camversity broadcast, camversity obs, camversity external encoder, camversity rtmp, camversity stream key, camversity performer",
        "h1html": 'How to broadcast on <span class="accent">Camversity</span> with SplitCam',
        "h1short": "Broadcast on Camversity",
        "card": "External encoder setup for Camversity's Performer Dashboard.",
        "intro": "Camversity is a growing independent cam platform with a focus on performer-friendly tools and lower commission rates than legacy networks. The default Performer Dashboard broadcaster works in-browser, but it also exposes a standard <strong>external encoder</strong> path that free <strong style='color:var(--text)'>SplitCam</strong> connects to — letting you stream with multi-camera scenes, overlays and filters.",
        "quick": "Broadcast on Camversity with SplitCam: install SplitCam, build your scene, in the Performer Dashboard open <em>Stream Settings → External Encoder</em>, copy the server URL and stream key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li><li>Get URL and stream key from the Performer Dashboard.</li><li>Paste into SplitCam.</li><li>Press Go Live.</li></ol>",
        "key_how": "Log in to your Camversity performer account, open the <strong>Performer Dashboard</strong> and navigate to <strong>Stream Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and <strong>stream key</strong> tied to your account — copy both into SplitCam's custom RTMP fields. New accounts need standard ID verification before going live.",
        "tips": [
            ("Performer-friendly splits", "Camversity's revenue split is more favorable for performers than legacy networks — worth comparing against your current main platform if you're early in your cam career."),
            ("Lighter onboarding than Docler", "Camversity's verification is faster than LiveJasmin's 48–72 hour approval, while still being legitimate (no random / unverified models). Good middle ground."),
            ("Build a scene, not just a webcam", "Camversity's default Performer Dashboard broadcaster is single-source. SplitCam via External Encoder unlocks multi-camera, overlays, beauty filters."),
            _T_ETH,
        ],
        "faq": [
            ("Does Camversity officially support external encoders like SplitCam?", "Yes — the Performer Dashboard includes an External Encoder option under Stream Settings. Standard RTMP server URL and stream key; OBS, SplitCam, vMix all connect."),
            ("Where do I get my Camversity stream key?", "Performer Dashboard → Stream Settings → External Encoder. Both the server URL and stream key appear there."),
            ("What bitrate should I use for Camversity?", "Push 1920×1080 at 30 fps, 3,500–6,000 Kbps with a 2-second keyframe interval. Run SplitCam's built-in speed test first."),
            ("Is SplitCam free to use with Camversity?", "Yes — SplitCam is free, no watermark and no time limit. Camversity's external encoder option is free."),
        ],
        "steps": [
            ("Download and install SplitCam", "SplitCam is free live-streaming software for Windows and macOS — no signup, no card, no watermark."),
            ("Build your scene", "Open SplitCam and add your webcam. Layer in overlays, text, a second camera or your phone, beauty filters or an AI background."),
            ("Get your Camversity URL and stream key", "Log in to your Camversity performer account, open the <strong>Performer Dashboard</strong>, navigate to <strong>Stream Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and unique <strong>stream key</strong>. Copy both."),
            ("Connect SplitCam to Camversity", "In SplitCam open <strong>Stream Settings</strong>, paste the Camversity server URL and stream key into the custom RTMP fields. Set bitrate to 3,500–6,000 Kbps at 1920×1080, 30 fps, with a 2-second keyframe."),
            ("Click Go Live", "Press <strong>Go Live</strong> in SplitCam, then go online from the Performer Dashboard. Within ~10 seconds your stream reaches Camversity."),
        ],
    },
    {
        "slug": "skyprivate", "name": "SkyPrivate",
        "title": "How to Use SkyPrivate with SplitCam — Skype-Based Private Cam Calls",
        "desc": "Use SkyPrivate with free SplitCam as virtual camera — pay-per-minute private Skype cam calls, multi-camera scenes, beauty filters. No watermark, no signup.",
        "kw": "skyprivate, sky private cam, skype cam private, skyprivate splitcam, skyprivate virtual camera, pay-per-minute cam",
        "h1html": 'How to use <span class="accent">SkyPrivate</span> with SplitCam',
        "h1short": "SplitCam on SkyPrivate",
        "card": "Virtual-camera setup for SkyPrivate's Skype-based cam calls.",
        "intro": "SkyPrivate is a unique cam platform — instead of RTMP broadcast, it monetizes <strong>pay-per-minute private cam calls via Skype</strong>. Clients book and pay per minute through the SkyPrivate marketplace, then the actual video call runs over Skype. Free <strong style='color:var(--text)'>SplitCam</strong> connects as a <strong>virtual camera</strong>: build your scene in SplitCam, then pick SplitCam as the camera inside Skype before answering a SkyPrivate-booked call.",
        "quick": "Use SkyPrivate with SplitCam: install SplitCam, build your scene, install Skype with the SkyPrivate add-on, in Skype's <em>Video Settings</em> select SplitCam as camera and microphone, then answer SkyPrivate-booked calls — Skype delivers your composed scene to the client."
                 "<ol><li>Install SplitCam.</li><li>Build scene in SplitCam.</li><li>Install Skype + SkyPrivate add-on.</li><li>Select SplitCam as camera in Skype.</li><li>Take calls.</li></ol>",
        "key_how": "SkyPrivate doesn't use RTMP or a stream key — it uses Skype as the video transport with a per-minute billing add-on. Install Skype, install the SkyPrivate browser/desktop add-on, then in Skype open <strong>Settings → Audio &amp; Video → Camera</strong> and select <strong>SplitCam</strong> instead of your webcam. SplitCam's composed scene (overlays, multi-camera, beauty filters) becomes what the SkyPrivate client sees through Skype.",
        "tips": [
            ("No RTMP — virtual camera flow", "Don't look for a server URL or stream key. SkyPrivate runs over Skype, and Skype just sees SplitCam as a webcam device. Build your scene in SplitCam, then pick SplitCam in Skype's camera settings."),
            ("Set SplitCam as the microphone too", "In Skype's Audio settings select SplitCam as the microphone in addition to camera — that way noise-suppression, mixed audio and intro music all reach the client."),
            ("Add a Skype outgoing-call test", "Before your first paid SkyPrivate call, do a free Skype test call (Echo / Sound Test Service) to confirm SplitCam is the active camera and your scene is composed correctly."),
            _T_TEST,
        ],
        "faq": [
            ("Does SkyPrivate use RTMP or a stream key?", "Neither. SkyPrivate handles billing and booking; the actual video runs over Skype. You don't need an RTMP server URL or stream key — just configure SplitCam as your camera inside Skype."),
            ("How do I select SplitCam in Skype for SkyPrivate?", "Open Skype Settings → Audio &amp; Video → Camera, choose SplitCam from the list. Do the same for Microphone. SkyPrivate calls then arrive as normal Skype calls with your SplitCam scene as the camera feed."),
            ("Can I use overlays and beauty filters with SkyPrivate?", "Yes — build them inside your SplitCam scene. Skype just receives the composed result as one camera feed, so anything SplitCam composes (overlays, beauty filters, AI background, multi-camera scenes) is visible to the SkyPrivate client."),
            ("Is SplitCam free for SkyPrivate?", "Yes — SplitCam is free, no watermark and no time limit. As a virtual camera for Skype-based SkyPrivate calls, it adds no cost or branding to the call."),
        ],
        "steps": [
            ("Install SplitCam", "SplitCam is free for Windows and macOS — no signup, no card, no watermark. For SkyPrivate it acts as a <strong>virtual camera</strong> that Skype picks up like any webcam."),
            ("Build your scene in SplitCam", "Open SplitCam and use <strong>Media Layers +</strong> to add your webcam plus any overlays, text, beauty filters or AI background. This composed scene is what Skype will deliver to the SkyPrivate client."),
            ("Install Skype and the SkyPrivate add-on", "Install Skype on the same PC, sign in, then install the SkyPrivate add-on / desktop app following SkyPrivate's onboarding. The add-on handles per-minute billing on the SkyPrivate side."),
            ("Select SplitCam as camera and mic in Skype", "In Skype open <strong>Settings → Audio &amp; Video</strong>. Set <strong>Camera = SplitCam</strong> and <strong>Microphone = SplitCam</strong>. Run a quick Skype test call (Echo / Sound Test Service) to confirm your scene looks and sounds right."),
            ("Take SkyPrivate calls", "When a SkyPrivate client books a paid call it arrives as a Skype call — answer it. They see your composed SplitCam scene; SkyPrivate bills per minute. Adjust the scene mid-call by editing it in SplitCam — Skype updates instantly."),
        ],
    },
    {
        "slug": "manyvids", "name": "ManyVids",
        "title": "How to Stream on MV Live (ManyVids) with SplitCam — Creator Studio Setup",
        "desc": "Stream on ManyVids' MV Live with free SplitCam — Creator Studio external encoder, OnlyFans-style creator economy, multi-camera scenes. No watermark, no signup.",
        "kw": "manyvids stream, mv live, manyvids live broadcast, manyvids obs, mv live external encoder, manyvids stream key, manyvids creator",
        "h1html": 'How to stream on <span class="accent">MV Live</span> with SplitCam',
        "h1short": "Stream on MV Live",
        "card": "External encoder setup for ManyVids' MV Live Creator Studio.",
        "intro": "ManyVids is a creator-economy platform — clip sales, custom videos, fan club subscriptions and the live-streaming product <strong>MV Live</strong>. The default Creator Studio broadcaster runs in-browser, but it also exposes a standard <strong>external encoder</strong> path that free <strong style='color:var(--text)'>SplitCam</strong> connects to — letting you stream with multi-camera scenes, overlays and filters on the same creator-friendly platform.",
        "quick": "Stream on MV Live with SplitCam: install SplitCam, build your scene, in the Creator Studio open <em>MV Live → Broadcast Settings → External Encoder</em>, copy the server URL and stream key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li><li>Get URL and stream key from Creator Studio.</li><li>Paste into SplitCam.</li><li>Press Go Live.</li></ol>",
        "key_how": "Log in to your ManyVids creator account, open the <strong>Creator Studio</strong> and go to <strong>MV Live → Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and <strong>stream key</strong> tied to your account — copy both into SplitCam's custom RTMP fields. Creator accounts must be fully verified (ID + tax) before MV Live is available.",
        "tips": [
            ("Creator-economy, not just live", "ManyVids isn't a pure cam platform — MV Live is one revenue stream alongside clip sales, custom videos and fan club subscriptions. Use live streams to drive viewers toward your other monetization."),
            ("Token tipping inside MV Live", "MV Live has its own token-tipping system inside the live room. Plan goal menus and reward triggers similar to Chaturbate / Stripchat — they convert well with the existing ManyVids audience."),
            ("Browser vs external encoder", "Creator Studio's built-in browser broadcaster is single-camera. SplitCam via External Encoder unlocks multi-camera scenes, overlays and filters."),
            _T_ETH,
        ],
        "faq": [
            ("Does MV Live (ManyVids) support external encoders like SplitCam?", "Yes — Creator Studio's MV Live section includes an External Encoder option under Broadcast Settings. Standard RTMP server URL and stream key; OBS, SplitCam, vMix all connect."),
            ("Where do I get my MV Live stream key?", "Creator Studio → MV Live → Broadcast Settings → External Encoder. Both the server URL and stream key appear there — copy both into SplitCam's custom RTMP fields."),
            ("What bitrate should I use for MV Live?", "Push 1920×1080 at 30 fps, 3,500–6,000 Kbps with a 2-second keyframe interval. Run SplitCam's built-in speed test first."),
            ("Is SplitCam free to use with MV Live?", "Yes — SplitCam is free, no watermark and no time limit. ManyVids' external encoder option is free in Creator Studio."),
        ],
        "steps": [
            ("Download and install SplitCam", "SplitCam is free live-streaming software for Windows and macOS — no signup, no card, no watermark."),
            ("Build your scene", "Open SplitCam and add your webcam. Layer in overlays, text, a second camera or your phone, beauty filters or an AI background — perfect for MV Live goal-reveal builds and reward triggers."),
            ("Get your MV Live URL and stream key", "Log in to your ManyVids creator account, open the <strong>Creator Studio</strong>, navigate to <strong>MV Live → Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and unique <strong>stream key</strong>. Copy both."),
            ("Connect SplitCam to MV Live", "In SplitCam open <strong>Stream Settings</strong>, paste the MV Live server URL and stream key into the custom RTMP fields. Set bitrate to 3,500–6,000 Kbps at 1920×1080, 30 fps, with a 2-second keyframe interval."),
            ("Click Go Live", "Press <strong>Go Live</strong> in SplitCam, then start the MV Live broadcast from Creator Studio. Within ~10 seconds your stream reaches MV Live's audience."),
        ],
    },
    {
        "slug": "fansly", "name": "Fansly",
        "title": "How to Stream on Fansly Live with SplitCam — Creator Dashboard External Encoder",
        "desc": "Stream on Fansly Live with free SplitCam — Creator Dashboard external encoder, OnlyFans competitor, multi-camera scenes, beauty filters. No watermark, no signup.",
        "kw": "fansly stream, fansly live, fansly broadcast, fansly obs, fansly external encoder, fansly rtmp, fansly stream key, fansly creator",
        "h1html": 'How to stream on <span class="accent">Fansly Live</span> with SplitCam',
        "h1short": "Stream on Fansly",
        "card": "External encoder setup for Fansly's Creator Dashboard.",
        "intro": "Fansly is a direct OnlyFans competitor with looser content rules and a growing creator base — subscriptions, pay-per-view content and the live-streaming product <strong>Fansly Live</strong>. The default broadcaster works in-browser, but the <strong>Creator Dashboard</strong> also exposes a standard <strong>external encoder</strong> path that free <strong style='color:var(--text)'>SplitCam</strong> connects to — letting you stream with multi-camera scenes, overlays and filters to your subscriber base.",
        "quick": "Stream on Fansly Live with SplitCam: install SplitCam, build your scene, in the Creator Dashboard open <em>Live → Broadcast Settings → External Encoder</em>, copy the server URL and stream key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li><li>Get URL and stream key from Creator Dashboard.</li><li>Paste into SplitCam.</li><li>Press Go Live.</li></ol>",
        "key_how": "Log in to your Fansly creator account, open the <strong>Creator Dashboard</strong> and navigate to <strong>Live → Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and <strong>stream key</strong> tied to your account — copy both into SplitCam's custom RTMP fields. Creator accounts need ID verification before Fansly Live is enabled.",
        "tips": [
            ("Subscriber-first audience", "Fansly's audience is subscription-based — your live stream reaches people who already pay you monthly. Plan content that rewards loyalty (exclusive Q&amp;A, behind-the-scenes, custom tip goals) rather than chasing public-room metrics."),
            ("Tips alongside subscriptions", "Fansly Live supports in-stream tipping in addition to base subscriptions. Combined revenue can outpace pure cam-platform tipping for established creators."),
            ("Browser broadcaster vs external", "The default browser broadcaster is single-source. SplitCam via External Encoder unlocks multi-camera, overlays, beauty filters and AI background that match the polish of paid subscriber content."),
            _T_ETH,
        ],
        "faq": [
            ("Does Fansly Live support external encoders like SplitCam?", "Yes — the Creator Dashboard's Live section includes an External Encoder option under Broadcast Settings. Standard RTMP server URL and stream key; OBS, SplitCam, vMix all connect."),
            ("Where do I get my Fansly stream key?", "Creator Dashboard → Live → Broadcast Settings → External Encoder. Both the server URL and stream key appear there. Copy both into SplitCam's custom RTMP fields."),
            ("What bitrate should I use for Fansly Live?", "Push 1920×1080 at 30 fps, 3,500–6,000 Kbps with a 2-second keyframe interval. Run SplitCam's built-in speed test first."),
            ("Is SplitCam free to use with Fansly?", "Yes — SplitCam is free, no watermark and no time limit. Fansly's external encoder option is free in Creator Dashboard."),
        ],
        "steps": [
            ("Download and install SplitCam", "SplitCam is free live-streaming software for Windows and macOS — no signup, no card, no watermark."),
            ("Build your scene", "Open SplitCam and add your webcam. Layer in overlays, text, a second camera or your phone, beauty filters or an AI background — polished scenes match the premium expectation of paying subscribers."),
            ("Get your Fansly URL and stream key", "Log in to your Fansly creator account, open the <strong>Creator Dashboard</strong>, navigate to <strong>Live → Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and unique <strong>stream key</strong>. Copy both."),
            ("Connect SplitCam to Fansly", "In SplitCam open <strong>Stream Settings</strong>, paste the Fansly server URL and stream key into the custom RTMP fields. Set bitrate to 3,500–6,000 Kbps at 1920×1080, 30 fps, with a 2-second keyframe interval."),
            ("Click Go Live", "Press <strong>Go Live</strong> in SplitCam, then start the Fansly Live broadcast from Creator Dashboard. Within ~10 seconds your stream reaches your Fansly subscribers."),
        ],
    },
    {
        "slug": "ifriends", "name": "iFriends",
        "title": "How to Broadcast on iFriends with SplitCam — Model Center External Encoder",
        "desc": "Broadcast on iFriends with free SplitCam — Model Center external encoder, long-running independent cam network, multi-camera scenes. No watermark, no signup.",
        "kw": "ifriends broadcast, ifriends obs, ifriends external encoder, ifriends rtmp, ifriends stream key, ifriends model center, ifriends.net",
        "h1html": 'How to broadcast on <span class="accent">iFriends</span> with SplitCam',
        "h1short": "Broadcast on iFriends",
        "card": "External encoder setup for iFriends' mature Model Center.",
        "intro": "iFriends (WebPower) is one of the longest-running independent cam networks — quietly profitable, loyal user base, and a mature Model Center built before browser broadcasters were common. The platform supports a standard <strong>external encoder</strong> path from the Model Center that free <strong style='color:var(--text)'>SplitCam</strong> connects to — letting you stream with modern multi-camera scenes, overlays and filters on this established network.",
        "quick": "Broadcast on iFriends with SplitCam: install SplitCam, build your scene, in the Model Center open <em>Broadcast Settings → External Encoder</em>, copy the server URL and stream key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li><li>Get URL and stream key from Model Center.</li><li>Paste into SplitCam.</li><li>Press Go Live.</li></ol>",
        "key_how": "Log in to your iFriends model account, open the <strong>Model Center</strong> and navigate to <strong>Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and <strong>stream key</strong> tied to your account — copy both into SplitCam's custom RTMP fields. iFriends approval for new model accounts is rigorous but legitimate; once verified, the external encoder option stays available indefinitely.",
        "tips": [
            ("Long-tail audience, mature network", "iFriends has run since the late '90s with a loyal user base — many users are long-term subscribers, not first-time visitors. Stable income for established models, slower growth for newcomers."),
            ("Browser broadcaster vs external", "iFriends' legacy broadcaster was built before modern multi-camera UX. Switching to SplitCam via External Encoder is a noticeable upgrade — multi-camera scenes, overlays and beauty filters that the older tool can't deliver."),
            ("Steady payouts, fewer surprises", "iFriends' parent (WebPower) has paid models reliably for decades — slower payout schedules than newer crypto-friendly platforms, but very few horror stories."),
            _T_ETH,
        ],
        "faq": [
            ("Does iFriends officially support external encoders like SplitCam?", "Yes — the Model Center includes an External Encoder option under Broadcast Settings. Standard RTMP server URL and stream key; OBS, SplitCam, vMix all connect once your account is approved."),
            ("Where do I get my iFriends stream key?", "Model Center → Broadcast Settings → External Encoder. Both the server URL and stream key appear there — copy both into SplitCam's custom RTMP fields."),
            ("What bitrate should I use for iFriends?", "Push 1920×1080 at 30 fps, 3,500–6,000 Kbps with a 2-second keyframe interval. Run SplitCam's built-in speed test first."),
            ("Is SplitCam free to use with iFriends?", "Yes — SplitCam is free, no watermark and no time limit. iFriends' external encoder option is free in the Model Center."),
        ],
        "steps": [
            ("Download and install SplitCam", "SplitCam is free live-streaming software for Windows and macOS — no signup, no card, no watermark."),
            ("Build your scene", "Open SplitCam and add your webcam. Layer in overlays, text, a second camera or your phone, beauty filters or an AI background — polished modern scenes stand out on this mature network."),
            ("Get your iFriends URL and stream key", "Log in to your iFriends model account, open the <strong>Model Center</strong>, navigate to <strong>Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and unique <strong>stream key</strong>. Copy both."),
            ("Connect SplitCam to iFriends", "In SplitCam open <strong>Stream Settings</strong>, paste the iFriends server URL and stream key into the custom RTMP fields. Set bitrate to 3,500–6,000 Kbps at 1920×1080, 30 fps, with a 2-second keyframe."),
            ("Click Go Live", "Press <strong>Go Live</strong> in SplitCam, then go online from the iFriends Model Center. Within ~10 seconds your stream reaches the network."),
        ],
    },
    {
        "slug": "babestation", "name": "Babestation",
        "title": "How to Broadcast on Babestation with SplitCam — UK Cam Network Setup",
        "desc": "Broadcast on Babestation with free SplitCam — Performer Hub external encoder, UK adult TV / cam network, multi-camera scenes, overlays. No watermark, no signup.",
        "kw": "babestation broadcast, babestation cam, babestation obs, babestation external encoder, babestation rtmp, babestation performer, uk cam network",
        "h1html": 'How to broadcast on <span class="accent">Babestation</span> with SplitCam',
        "h1short": "Broadcast on Babestation",
        "card": "External encoder setup for Babestation's UK Performer Hub.",
        "intro": "Babestation is the leading UK adult TV / cam network — a hybrid of broadcast TV channels and a live cam product fed by performers logged into the Performer Hub. The platform supports a standard <strong>external encoder</strong> path from the Performer Hub that free <strong style='color:var(--text)'>SplitCam</strong> connects to — letting independent UK performers stream with multi-camera scenes, overlays and beauty filters that go beyond Babestation's TV-studio-style default broadcaster.",
        "quick": "Broadcast on Babestation with SplitCam: install SplitCam, build your scene, in the Performer Hub open <em>Broadcast Settings → External Encoder</em>, copy the server URL and stream key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li><li>Get URL and stream key from Performer Hub.</li><li>Paste into SplitCam.</li><li>Press Go Live.</li></ol>",
        "key_how": "Log in to your Babestation performer account, open the <strong>Performer Hub</strong> and navigate to <strong>Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and <strong>stream key</strong> tied to your account — copy both into SplitCam's custom RTMP fields. Babestation's UK performer onboarding includes ID verification under UK age-verification regulations.",
        "tips": [
            ("UK-first audience and timing", "Babestation's prime traffic is UK evening / overnight (GMT/BST). If you're in another time zone, broadcasting late-night UK hours significantly out-performs local-prime timing on this network."),
            ("TV-studio polish expected", "Babestation's brand is tied to its TV channels — viewers expect more produced-looking sets and lighting than a typical webcam stream. SplitCam scenes (overlays, branded text, AI background) help match the platform's polished aesthetic."),
            ("Independent vs studio performers", "Babestation works with both UK studios and independent performers. Independent broadcasters connecting via External Encoder get the same payout model as studio-fed cameras."),
            _T_ETH,
        ],
        "faq": [
            ("Does Babestation support external encoders like SplitCam?", "Yes — the Performer Hub includes an External Encoder option under Broadcast Settings. Standard RTMP server URL and stream key; OBS, SplitCam, vMix all connect after performer verification is complete."),
            ("Where do I get my Babestation stream key?", "Performer Hub → Broadcast Settings → External Encoder. Both the server URL and stream key appear there — copy both into SplitCam's custom RTMP fields."),
            ("What bitrate should I use for Babestation?", "Push 1920×1080 at 30 fps, 3,500–6,000 Kbps with a 2-second keyframe interval. UK upload bandwidth is generally strong, but run SplitCam's speed test first."),
            ("Is SplitCam free to use with Babestation?", "Yes — SplitCam is free, no watermark and no time limit. Babestation's external encoder option is free in the Performer Hub."),
        ],
        "steps": [
            ("Download and install SplitCam", "SplitCam is free live-streaming software for Windows and macOS — no signup, no card, no watermark."),
            ("Build your scene", "Open SplitCam and add your webcam. Layer in overlays, text, a second camera or your phone, beauty filters or an AI background — match Babestation's TV-studio production polish to stand out."),
            ("Get your Babestation URL and stream key", "Log in to your Babestation performer account, open the <strong>Performer Hub</strong>, navigate to <strong>Broadcast Settings → External Encoder</strong>. The page reveals a <strong>server URL</strong> and unique <strong>stream key</strong>. Copy both."),
            ("Connect SplitCam to Babestation", "In SplitCam open <strong>Stream Settings</strong>, paste the Babestation server URL and stream key into the custom RTMP fields. Set bitrate to 3,500–6,000 Kbps at 1920×1080, 30 fps, with a 2-second keyframe."),
            ("Click Go Live", "Press <strong>Go Live</strong> in SplitCam, then go online from the Performer Hub. Within ~10 seconds your stream reaches Babestation's UK audience."),
        ],
    },
    {
        "slug": "adultwork", "name": "AdultWork",
        "title": "How to Broadcast on AdultWork with SplitCam — Members Area External Encoder",
        "desc": "Broadcast on AdultWork with free SplitCam — Members Area external encoder, UK adult-service marketplace with cam feature, multi-camera scenes. No watermark, no signup.",
        "kw": "adultwork broadcast, adultwork cam, adultwork obs, adultwork external encoder, adultwork rtmp, adultwork webcam, uk cam",
        "h1html": 'How to broadcast on <span class="accent">AdultWork</span> with SplitCam',
        "h1short": "Broadcast on AdultWork",
        "card": "External encoder setup for AdultWork's UK Members Area cam feature.",
        "intro": "AdultWork is the established UK adult-service marketplace — primarily known for escort bookings, photo / video sales and phone services, with a live <strong>webcam feature</strong> alongside. The platform supports a standard <strong>external encoder</strong> path from the Members Area that free <strong style='color:var(--text)'>SplitCam</strong> connects to — letting independent UK performers add live cam revenue with multi-camera scenes, overlays and filters.",
        "quick": "Broadcast on AdultWork with SplitCam: install SplitCam, build your scene, in the Members Area open <em>Members → Broadcasting → External Encoder</em>, copy the server URL and stream key, paste into SplitCam, Go Live."
                 "<ol><li>Install SplitCam.</li><li>Add camera + scene.</li><li>Get URL and stream key from the Members Area.</li><li>Paste into SplitCam.</li><li>Press Go Live.</li></ol>",
        "key_how": "Log in to your AdultWork performer account, open the <strong>Members Area</strong> and navigate to <strong>Members → Broadcasting → External Encoder</strong>. The page reveals a <strong>server URL</strong> and <strong>stream key</strong> tied to your account — copy both into SplitCam's custom RTMP fields. AdultWork verification is mandatory for the live cam feature and covers UK age-verification compliance.",
        "tips": [
            ("Cross-sell from other AdultWork services", "AdultWork's strength is its existing customer base — viewers may already book your photo / video / phone services. Use live cam streams to cross-sell to clients who haven't tried your cam yet, not to chase strangers."),
            ("Members Area is the entry point", "Don't look for the broadcaster in the public-facing site — everything performer-side is inside the Members Area. Broadcasting settings, payouts, content management all sit there."),
            ("UK-centric but international payouts", "Most traffic is UK/EU. Payouts work internationally via standard bank transfer / e-wallet, with weekly schedules common on the platform."),
            _T_ETH,
        ],
        "faq": [
            ("Does AdultWork support external encoders like SplitCam?", "Yes — the Members Area includes an External Encoder option under Broadcasting. Standard RTMP server URL and stream key; OBS, SplitCam, vMix all connect after performer verification."),
            ("Where do I get my AdultWork stream key?", "Members Area → Members → Broadcasting → External Encoder. Both the server URL and stream key appear there — copy both into SplitCam's custom RTMP fields."),
            ("What bitrate should I use for AdultWork?", "Push 1920×1080 at 30 fps, 3,500–6,000 Kbps with a 2-second keyframe interval. Run SplitCam's built-in speed test first."),
            ("Is SplitCam free to use with AdultWork?", "Yes — SplitCam is free, no watermark and no time limit. AdultWork's external encoder option is free in the Members Area."),
        ],
        "steps": [
            ("Download and install SplitCam", "SplitCam is free live-streaming software for Windows and macOS — no signup, no card, no watermark."),
            ("Build your scene", "Open SplitCam and add your webcam. Layer in overlays, text, a second camera or your phone, beauty filters or an AI background — use overlays to advertise your AdultWork content / phone services and cross-sell during the live."),
            ("Get your AdultWork URL and stream key", "Log in to your AdultWork performer account, open the <strong>Members Area</strong>, navigate to <strong>Members → Broadcasting → External Encoder</strong>. The page reveals a <strong>server URL</strong> and unique <strong>stream key</strong>. Copy both."),
            ("Connect SplitCam to AdultWork", "In SplitCam open <strong>Stream Settings</strong>, paste the AdultWork server URL and stream key into the custom RTMP fields. Set bitrate to 3,500–6,000 Kbps at 1920×1080, 30 fps, with a 2-second keyframe."),
            ("Click Go Live", "Press <strong>Go Live</strong> in SplitCam, then go online from the Members Area. Within ~10 seconds your stream reaches AdultWork's audience."),
        ],
    },
]
