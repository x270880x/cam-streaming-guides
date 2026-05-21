# 301 Redirect map — splitcam.com adult pages → new domain
*Created 2026-05-21. Goes into splitcam.com's `.htaccess` (Apache/WordPress).*

## Before using this
1. Replace `NEWDOMAIN.com` everywhere with the real domain once registered.
2. Build the consolidated pages on the new domain FIRST (one page per platform). Don't 301 to URLs that 404.
3. Each platform = ONE page on the new domain. Multiple old splitcam.com URLs (start + video-tutorials + blog) collapse into it — this also fixes the existing self-cannibalization.
4. Language preserved: EN → `/slug/`, RU → `/ru/slug/`, ES → `/es/slug/`.
5. These are cross-domain 301s — link equity flows to the new domain. Keep them permanently.
6. **streamray** carries 1008 refdomains (mostly spammy adult links). Redirecting it sends that profile to the new domain — acceptable, the new domain is the designated adult home. Do NOT point it at splitcam.com clean pages.

## `.htaccess` block (place high in splitcam.com .htaccess)

```apache
# === Adult-cam pages → migrated to NEWDOMAIN.com (2026) ===

# Chaturbate
Redirect 301 /help/start/how-to-add-chaturbate-stream                 https://NEWDOMAIN.com/chaturbate/
Redirect 301 /help/video-tutorials/how-to-stream-on-chaturbate        https://NEWDOMAIN.com/chaturbate/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-chaturbate            https://NEWDOMAIN.com/ru/chaturbate/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-dobavit-translyaciyu-na-chaturbate https://NEWDOMAIN.com/ru/chaturbate/
Redirect 301 /es/ayuda/start/como-transmitir-en-chaturbate                                  https://NEWDOMAIN.com/es/chaturbate/
Redirect 301 /es/ayuda/video-tutorials/transmite-en-chaturbate-en-alta-calidad-facil-paso-a-paso https://NEWDOMAIN.com/es/chaturbate/

# CAM4
Redirect 301 /help/start/how-to-add-cam4-stream                       https://NEWDOMAIN.com/cam4/
Redirect 301 /help/video-tutorials/how-to-stream-on-cam4              https://NEWDOMAIN.com/cam4/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-cam4                  https://NEWDOMAIN.com/ru/cam4/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-dobavit-translyaciyu-na-cam4       https://NEWDOMAIN.com/ru/cam4/
Redirect 301 /es/ayuda/start/como-transmitir-en-cam4                                        https://NEWDOMAIN.com/es/cam4/
Redirect 301 /es/ayuda/video-tutorials/transmite-en-cam4-en-alta-calidad-facil-paso-a-paso  https://NEWDOMAIN.com/es/cam4/

# BongaCams
Redirect 301 /help/start/how-to-stream-on-bongacams                   https://NEWDOMAIN.com/bongacams/
Redirect 301 /help/video-tutorials/how-to-stream-on-bongacams         https://NEWDOMAIN.com/bongacams/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-bongacams             https://NEWDOMAIN.com/ru/bongacams/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-bongacams https://NEWDOMAIN.com/ru/bongacams/

# Stripchat
Redirect 301 /help/start/how-to-add-stripchat-stream                  https://NEWDOMAIN.com/stripchat/
Redirect 301 /help/video-tutorials/how-to-add-stripchat-stream        https://NEWDOMAIN.com/stripchat/
Redirect 301 /blog/2020/how-to-add-stripchat-stream.html              https://NEWDOMAIN.com/stripchat/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-stripchat                              https://NEWDOMAIN.com/ru/stripchat/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-v-stripchat-pri-pomoshhi-splitcam https://NEWDOMAIN.com/ru/stripchat/

# OnlyFans
Redirect 301 /help/start/how-to-stream-on-onlyfans                    https://NEWDOMAIN.com/onlyfans/
Redirect 301 /help/video-tutorials/how-to-stream-on-onlyfans          https://NEWDOMAIN.com/onlyfans/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-onlyfans              https://NEWDOMAIN.com/ru/onlyfans/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-onlyfans  https://NEWDOMAIN.com/ru/onlyfans/

# CamPlace
Redirect 301 /help/start/how-to-stream-on-camplace                    https://NEWDOMAIN.com/camplace/
Redirect 301 /help/start/how-to-stream-on-camplace-2                  https://NEWDOMAIN.com/camplace/
Redirect 301 /help/video-tutorials/how-to-stream-on-camplace          https://NEWDOMAIN.com/camplace/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-camplace              https://NEWDOMAIN.com/ru/camplace/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-camplace  https://NEWDOMAIN.com/ru/camplace/

# CamSoda
Redirect 301 /help/video-tutorials/how-to-stream-on-camsoda           https://NEWDOMAIN.com/camsoda/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-camsoda                https://NEWDOMAIN.com/ru/camsoda/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-camsoda    https://NEWDOMAIN.com/ru/camsoda/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-camsoda-2  https://NEWDOMAIN.com/ru/camsoda/

# Streamate
Redirect 301 /help/video-tutorials/how-to-stream-on-streamate         https://NEWDOMAIN.com/streamate/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-streamate              https://NEWDOMAIN.com/ru/streamate/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-streamate  https://NEWDOMAIN.com/ru/streamate/

# StreamRay
Redirect 301 /help/start/how-to-stream-on-streamray                   https://NEWDOMAIN.com/streamray/
Redirect 301 /help/video-tutorials/how-to-stream-on-streamray         https://NEWDOMAIN.com/streamray/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-streamray              https://NEWDOMAIN.com/ru/streamray/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-streamray  https://NEWDOMAIN.com/ru/streamray/

# XLoveCam
Redirect 301 /help/start/how-to-stream-to-xlovecam                    https://NEWDOMAIN.com/xlovecam/
Redirect 301 /help/video-tutorials/how-to-stream-on-xlovecam          https://NEWDOMAIN.com/xlovecam/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-xlovecam               https://NEWDOMAIN.com/ru/xlovecam/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-xlovecam   https://NEWDOMAIN.com/ru/xlovecam/

# SoulCams
Redirect 301 /help/start/how-to-stream-to-soulcams                    https://NEWDOMAIN.com/soulcams/
Redirect 301 /help/video-tutorials/how-to-stream-on-soulcams          https://NEWDOMAIN.com/soulcams/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-soulcams               https://NEWDOMAIN.com/ru/soulcams/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-soulcams   https://NEWDOMAIN.com/ru/soulcams/

# ImLive
Redirect 301 /help/start/how-to-stream-on-imlive                      https://NEWDOMAIN.com/imlive/
Redirect 301 /help/video-tutorials/how-to-stream-on-imlive            https://NEWDOMAIN.com/imlive/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-imlive                 https://NEWDOMAIN.com/ru/imlive/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-imlive     https://NEWDOMAIN.com/ru/imlive/

# VXLive
Redirect 301 /help/video-tutorials/how-to-stream-on-vxlive            https://NEWDOMAIN.com/vxlive/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-vxlive                 https://NEWDOMAIN.com/ru/vxlive/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-vxlive     https://NEWDOMAIN.com/ru/vxlive/

# Virtwish
Redirect 301 /help/start/how-to-add-virtwish-stream                   https://NEWDOMAIN.com/virtwish/
Redirect 301 /help/video-tutorials/how-to-add-virtwish-stream         https://NEWDOMAIN.com/virtwish/
Redirect 301 /ru/help-ru/start/kak-provodit-translyaciyu-na-virtwish               https://NEWDOMAIN.com/ru/virtwish/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-virtwish   https://NEWDOMAIN.com/ru/virtwish/

# XModels
Redirect 301 /help/video-tutorials/how-to-stream-to-xmodels           https://NEWDOMAIN.com/xmodels/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-xmodels    https://NEWDOMAIN.com/ru/xmodels/

# Flirt4Free
Redirect 301 /help/video-tutorials/how-to-stream-on-flirt-4-free      https://NEWDOMAIN.com/flirt4free/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-provodit-translyaciyu-na-flirt4free https://NEWDOMAIN.com/ru/flirt4free/

# MyFreeCams (MFC alerts)
Redirect 301 /help/start/how-to-add-mfc-alerts                        https://NEWDOMAIN.com/mfc-alerts/
Redirect 301 /help/video-tutorials/how-to-add-mfc-alerts              https://NEWDOMAIN.com/mfc-alerts/
Redirect 301 /blog/2020/how-to-add-mfc-alerts.html                    https://NEWDOMAIN.com/mfc-alerts/
Redirect 301 /ru/help-ru/start/kak-dobavit-mfc-alerts                              https://NEWDOMAIN.com/ru/mfc-alerts/
Redirect 301 /es/ayuda/start/como-agregar-mfc-alerts                               https://NEWDOMAIN.com/es/mfc-alerts/

# Lovense (toy)
Redirect 301 /help/video-tutorials/how-to-add-a-lovense-toy-to-your-stream         https://NEWDOMAIN.com/lovense/
Redirect 301 /ru/help-ru/start/kak-dobavit-ustrojstvo-lovense-na-translyaciyu       https://NEWDOMAIN.com/ru/lovense/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-dobavit-ustrojstvo-lovense-na-translyaciyu https://NEWDOMAIN.com/ru/lovense/
Redirect 301 /es/ayuda/video-tutorials/conecta-tus-juguetes-lovense-y-reacciona-a-tus-tokens-paso-a-paso https://NEWDOMAIN.com/es/lovense/

# Multi-platform broadcast guide
Redirect 301 /help/video-tutorials/splitcam-10-how-to-broadcast-on-bongacams-chaturbate-cam4-stripchat-and-other-at-the-same-time https://NEWDOMAIN.com/multistream-cams/
Redirect 301 /ru/help-ru/video-rukovodstva/kak-odnovremenno-provodit-translyacii-na-bongacams-chaturbate-cam4-stripchat-i-dr      https://NEWDOMAIN.com/ru/multistream-cams/

# === end adult migration block ===
```

## After deploying
- Submit the new domain in Google Search Console; use the "Change of Address" tool only if moving the *whole* site (not applicable here — partial migration, so just let the 301s do the work).
- Remove the migrated URLs from splitcam.com's sitemap.xml.
- Add the new domain's own sitemap.xml.
- Watch Search Console for crawl errors on both domains for 4-8 weeks.
