# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_EN = {
    "common": [
        (
            "How much can models earn on {name}?",
            "Earnings on {name} depend on audience size, hours streamed and tipping behaviour. "
            "Active broadcasters typically take home $200–$3,000 per month; top performers reach "
            "$10,000+. Your revenue share follows {name}'s commission structure — check the model "
            "agreement before going live."
        ),
        (
            "Is {name} safe for broadcasters?",
            "{name} requires age and ID verification before payout, which protects models from "
            "fraud. Use a stage name, never share personal data on camera, enable geo-blocks to "
            "hide your stream from your home region, and treat every viewer request as "
            "transactional. SplitCam's overlays and AI background can also hide or replace your "
            "real surroundings."
        ),
        (
            "What documents do I need to become a model on {name}?",
            "{name} typically requires a government-issued photo ID (passport, driver's license "
            "or ID card), a selfie holding the ID, and a tax/payout form (W-9 for US, W-8BEN for "
            "non-US). Approval usually takes 24–72 hours; once approved you can go live the same day."
        ),
        (
            "Can I stream on {name} from my phone?",
            "{name} usually offers a mobile broadcaster app or a mobile-web broadcaster, but the "
            "experience is limited — no overlays, no second camera, no AI background. For full "
            "production quality, broadcast from a computer with SplitCam and use your phone as a "
            "second camera (SplitCam accepts IP-camera input from phones)."
        ),
    ],
    "stream": (
        "Does {name} support OBS or an external encoder?",
        "Yes — {name} provides an RTMP server URL and a stream key in the broadcaster panel. "
        "Paste both into SplitCam's <strong>Stream Settings → Custom RTMP</strong>, set "
        "1920×1080 at 30 fps with a 4,000–5,000 Kbps bitrate, and click <strong>Go Live</strong>. "
        "The Custom RTMP route gives you full SplitCam scene composition (multi-camera, overlays, filters)."
    ),
    "vcam": (
        "Can I use SplitCam as a virtual camera on {name}?",
        "Yes — {name}'s live runs in the browser, so SplitCam registers as a webcam called "
        "<strong>\"SplitCam Video Driver\"</strong>. Open the {name} broadcaster, click the camera "
        "selector in the browser, and pick SplitCam. Your composed scene (overlays, second camera, "
        "filters, AI background) reaches viewers as a single webcam feed."
    ),
}
