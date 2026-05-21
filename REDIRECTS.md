# 301 Redirect map — splitcam.com adult pages → new domain
*Created 2026-05-21. Goes into splitcam.com's `.htaccess` (Apache/WordPress).*

## Before using this
1. Target domain is `camstreamguide.com` (registered 2026-05). The placeholder has already been substituted below.
2. Build the consolidated pages on the new domain FIRST (one page per platform). Don't 301 to URLs that 404.
3. Each platform = ONE page on the new domain. Multiple old splitcam.com URLs (start + video-tutorials + blog) collapse into it — this also fixes the existing self-cannibalization.
4. Language preserved: EN → `/slug/`, RU → `/ru/slug/`, ES → `/es/slug/`.
5. These are cross-domain 301s — link equity flows to the new domain. Keep them permanently.
6. **streamray** carries 1008 refdomains (mostly spammy adult links). Redirecting it sends that profile to the new domain — acceptable, the new domain is the designated adult home. Do NOT point it at splitcam.com clean pages.

## `.htaccess` block (place high in splitcam.com .htaccess)

```apache
# === Adult-cam pages → migrated to camstreamguide.com (2026) ===

# Chaturbate
Redirect 301 /help/start/how-to-add-chaturbate-stream                 https://camstreamguide.com/chaturbate/
Redirect 301 /help/video-tutorials/how-to-stream-on-chaturbate        https://camstreamguide.com/chaturbate/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-chaturbate            https://camstreamguide.com/ru/chaturbate/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-dobavit-translyaciyu-na-chaturbate https://camstreamguide.com/ru/chaturbate/
Redirect 301 /es/ayuda/start/como-transmitir-en-chaturbate                                  https://camstreamguide.com/es/chaturbate/
Redirect 301 /es/ayuda/video-tutorials/transmite-en-chaturbate-en-alta-calidad-facil-paso-a-paso https://camstreamguide.com/es/chaturbate/

# CAM4
Redirect 301 /help/start/how-to-add-cam4-stream                       https://camstreamguide.com/cam4/
Redirect 301 /help/video-tutorials/how-to-stream-on-cam4              https://camstreamguide.com/cam4/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-cam4                  https://camstreamguide.com/ru/cam4/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-dobavit-translyaciyu-na-cam4       https://camstreamguide.com/ru/cam4/
Redirect 301 /es/ayuda/start/como-transmitir-en-cam4                                        https://camstreamguide.com/es/cam4/
Redirect 301 /es/ayuda/video-tutorials/transmite-en-cam4-en-alta-calidad-facil-paso-a-paso  https://camstreamguide.com/es/cam4/

# BongaCams
Redirect 301 /help/start/how-to-stream-on-bongacams                   https://camstreamguide.com/bongacams/
Redirect 301 /help/video-tutorials/how-to-stream-on-bongacams         https://camstreamguide.com/bongacams/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-bongacams             https://camstreamguide.com/ru/bongacams/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-bongacams https://camstreamguide.com/ru/bongacams/

# Stripchat
Redirect 301 /help/start/how-to-add-stripchat-stream                  https://camstreamguide.com/stripchat/
Redirect 301 /help/video-tutorials/how-to-add-stripchat-stream        https://camstreamguide.com/stripchat/
Redirect 301 /blog/2020/how-to-add-stripchat-stream.html              https://camstreamguide.com/stripchat/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-stripchat                              https://camstreamguide.com/ru/stripchat/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-v-stripchat-pri-pomoshhi-splitcam https://camstreamguide.com/ru/stripchat/

# OnlyFans
Redirect 301 /help/start/how-to-stream-on-onlyfans                    https://camstreamguide.com/onlyfans/
Redirect 301 /help/video-tutorials/how-to-stream-on-onlyfans          https://camstreamguide.com/onlyfans/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-onlyfans              https://camstreamguide.com/ru/onlyfans/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-onlyfans  https://camstreamguide.com/ru/onlyfans/

# CamPlace
Redirect 301 /help/start/how-to-stream-on-camplace                    https://camstreamguide.com/camplace/
Redirect 301 /help/start/how-to-stream-on-camplace-2                  https://camstreamguide.com/camplace/
Redirect 301 /help/video-tutorials/how-to-stream-on-camplace          https://camstreamguide.com/camplace/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-camplace              https://camstreamguide.com/ru/camplace/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-camplace  https://camstreamguide.com/ru/camplace/

# CamSoda
Redirect 301 /help/video-tutorials/how-to-stream-on-camsoda           https://camstreamguide.com/camsoda/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-camsoda                https://camstreamguide.com/ru/camsoda/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-camsoda    https://camstreamguide.com/ru/camsoda/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-camsoda-2  https://camstreamguide.com/ru/camsoda/

# Streamate
Redirect 301 /help/video-tutorials/how-to-stream-on-streamate         https://camstreamguide.com/streamate/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-streamate              https://camstreamguide.com/ru/streamate/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-streamate  https://camstreamguide.com/ru/streamate/

# StreamRay
Redirect 301 /help/start/how-to-stream-on-streamray                   https://camstreamguide.com/streamray/
Redirect 301 /help/video-tutorials/how-to-stream-on-streamray         https://camstreamguide.com/streamray/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-streamray              https://camstreamguide.com/ru/streamray/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-streamray  https://camstreamguide.com/ru/streamray/

# XLoveCam
Redirect 301 /help/start/how-to-stream-to-xlovecam                    https://camstreamguide.com/xlovecam/
Redirect 301 /help/video-tutorials/how-to-stream-on-xlovecam          https://camstreamguide.com/xlovecam/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-xlovecam               https://camstreamguide.com/ru/xlovecam/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-xlovecam   https://camstreamguide.com/ru/xlovecam/

# SoulCams
Redirect 301 /help/start/how-to-stream-to-soulcams                    https://camstreamguide.com/soulcams/
Redirect 301 /help/video-tutorials/how-to-stream-on-soulcams          https://camstreamguide.com/soulcams/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-soulcams               https://camstreamguide.com/ru/soulcams/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-soulcams   https://camstreamguide.com/ru/soulcams/

# ImLive
Redirect 301 /help/start/how-to-stream-on-imlive                      https://camstreamguide.com/imlive/
Redirect 301 /help/video-tutorials/how-to-stream-on-imlive            https://camstreamguide.com/imlive/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-imlive                 https://camstreamguide.com/ru/imlive/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-imlive     https://camstreamguide.com/ru/imlive/

# VXLive
Redirect 301 /help/video-tutorials/how-to-stream-on-vxlive            https://camstreamguide.com/vxlive/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-vxlive                 https://camstreamguide.com/ru/vxlive/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-vxlive     https://camstreamguide.com/ru/vxlive/

# Virtwish
Redirect 301 /help/start/how-to-add-virtwish-stream                   https://camstreamguide.com/virtwish/
Redirect 301 /help/video-tutorials/how-to-add-virtwish-stream         https://camstreamguide.com/virtwish/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-virtwish               https://camstreamguide.com/ru/virtwish/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-virtwish   https://camstreamguide.com/ru/virtwish/

# XModels
Redirect 301 /help/video-tutorials/how-to-stream-to-xmodels           https://camstreamguide.com/xmodels/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-xmodels    https://camstreamguide.com/ru/xmodels/

# Flirt4Free
Redirect 301 /help/video-tutorials/how-to-stream-on-flirt-4-free      https://camstreamguide.com/flirt4free/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-flirt4free https://camstreamguide.com/ru/flirt4free/

# MyFreeCams (MFC alerts)
Redirect 301 /help/start/how-to-add-mfc-alerts                        https://camstreamguide.com/mfc-alerts/
Redirect 301 /help/video-tutorials/how-to-add-mfc-alerts              https://camstreamguide.com/mfc-alerts/
Redirect 301 /blog/2020/how-to-add-mfc-alerts.html                    https://camstreamguide.com/mfc-alerts/
Redirect 301 /ru/help-ru/start/kak-dobavit-mfc-alerts                              https://camstreamguide.com/ru/mfc-alerts/
Redirect 301 /es/ayuda/start/como-agregar-mfc-alerts                               https://camstreamguide.com/es/mfc-alerts/

# Lovense (toy)
Redirect 301 /help/video-tutorials/how-to-add-a-lovense-toy-to-your-stream         https://camstreamguide.com/lovense/
Redirect 301 /ru/help-ru/start/kak-dobavit-ustrojstvo-lovense-na-translyaciyu       https://camstreamguide.com/ru/lovense/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-dobavit-ustrojstvo-lovense-na-translyaciyu https://camstreamguide.com/ru/lovense/
Redirect 301 /es/ayuda/video-tutorials/conecta-tus-juguetes-lovense-y-reacciona-a-tus-tokens-paso-a-paso https://camstreamguide.com/es/lovense/

# Multi-platform broadcast guide
Redirect 301 /help/video-tutorials/splitcam-10-how-to-broadcast-on-bongacams-chaturbate-cam4-stripchat-and-other-at-the-same-time https://camstreamguide.com/multistream-cams/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-odnovremenno-provodit-translyacii-na-bongacams-chaturbate-cam4-stripchat-i-dr      https://camstreamguide.com/ru/multistream-cams/

# === end adult migration block ===
```

## After deploying
- Submit the new domain in Google Search Console; use the "Change of Address" tool only if moving the *whole* site (not applicable here — partial migration, so just let the 301s do the work).
- Remove the migrated URLs from splitcam.com's sitemap.xml.
- Add the new domain's own sitemap.xml.
- Watch Search Console for crawl errors on both domains for 4-8 weeks.
