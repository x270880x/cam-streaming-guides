# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_FIL = {
    "common": [
        (
            "Magkano ang kita ng mga model sa {name}?",
            "Ang kita sa {name} ay nakadepende sa laki ng audience, oras ng pag-stream at "
            "pag-uugali sa pagbibigay ng tip. Ang aktibong broadcaster ay karaniwang kumikita ng "
            "$200–$3,000 kada buwan; ang mga top performer ay umaabot sa $10,000+. Sumusunod ang "
            "iyong revenue share sa istruktura ng komisyon ng {name} — tingnan ang model "
            "agreement bago mag-live."
        ),
        (
            "Ligtas ba ang {name} para sa mga broadcaster?",
            "Nangangailangan ang {name} ng age at ID verification bago ang payout, na "
            "nagpoprotekta sa mga model laban sa fraud. Gumamit ng stage name, huwag kailanman "
            "ibahagi ang personal na datos sa camera, i-enable ang geo-blocks para itago ang "
            "iyong stream mula sa iyong home region, at ituring na transactional ang bawat "
            "kahilingan ng viewer. Maaari ring itago o palitan ng overlays at AI background ng "
            "SplitCam ang iyong tunay na paligid."
        ),
        (
            "Anong mga dokumento ang kailangan ko para maging model sa {name}?",
            "Karaniwang nangangailangan ang {name} ng government-issued photo ID (pasaporte, "
            "lisensya sa pagmamaneho o ID card), selfie habang hawak ang ID, at tax/payout form "
            "(W-9 para sa US, W-8BEN para sa hindi US). Karaniwang tumatagal ang approval ng "
            "24–72 oras; kapag naaprubahan ay maaari kang mag-live sa parehong araw."
        ),
        (
            "Maaari ba akong mag-stream sa {name} mula sa aking telepono?",
            "Karaniwang nag-aalok ang {name} ng mobile broadcaster app o mobile-web broadcaster, "
            "ngunit limitado ang karanasan — walang overlays, walang second camera, walang AI "
            "background. Para sa buong production quality, mag-broadcast mula sa computer gamit "
            "ang SplitCam at gamitin ang iyong telepono bilang second camera (tinatanggap ng "
            "SplitCam ang IP-camera input mula sa mga telepono)."
        ),
    ],
    "stream": (
        "Sinusuportahan ba ng {name} ang OBS o panlabas na encoder?",
        "Oo — nagbibigay ang {name} ng RTMP server URL at stream key sa broadcaster panel. "
        "I-paste ang dalawa sa <strong>Stream Settings → Custom RTMP</strong> ng SplitCam, "
        "itakda sa 1920×1080 sa 30 fps na may 4,000–5,000 Kbps bitrate, at i-click ang "
        "<strong>Go Live</strong>. Ang Custom RTMP route ay nagbibigay sa iyo ng buong SplitCam "
        "scene composition (multi-camera, overlays, filters)."
    ),
    "vcam": (
        "Maaari ko bang gamitin ang SplitCam bilang virtual camera sa {name}?",
        "Oo — ang live ng {name} ay tumatakbo sa browser, kaya nagrerehistro ang SplitCam "
        "bilang webcam na tinatawag na <strong>\"SplitCam Video Driver\"</strong>. Buksan ang "
        "{name} broadcaster, i-click ang camera selector sa browser, at piliin ang SplitCam. "
        "Ang iyong composed scene (overlays, second camera, filters, AI background) ay "
        "umaabot sa mga viewer bilang isang webcam feed."
    ),
}
