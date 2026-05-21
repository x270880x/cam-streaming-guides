# Adult-page inventory — splitcam.com → migration to new domain
*Created 2026-05-21. Source: splitcam.com/page-sitemap.xml (260 URLs) + Ahrefs weights (seo/data, US market).*

## Scope
73 adult-cam pages to migrate off splitcam.com: **32 EN + 35 RU + 6 ES**.
(2 RU "crowdcast" pages excluded — Crowdcast is a webinar platform, not adult; those stay on splitcam.com.)

## Important caveats
- **Weights are US-market.** Adult traffic is heavily non-US, so real traffic is *higher* than the numbers below. Refdomains (rd) are global and accurate.
- **Heavy duplication.** Most platforms have BOTH a `/help/start/how-to-...` and a `/help/video-tutorials/how-to-...` page — they cannibalize each other. **Migration = consolidate to ONE page per platform** on the new domain; all old variants 301 to it.
- traffic = monthly organic visits (US) · value = traffic $ value · kw = ranking keywords · rd = referring domains.

---

## TIER A — pages with real weight (migrate carefully, preserve)

| splitcam.com URL | traffic | value | kw | rd | top keyword |
|---|--:|--:|--:|--:|---|
| /help/start/how-to-stream-on-streamray | 4 | 232 | 13 | **1008** | streamray (vol 2800) |
| /help/start/how-to-stream-on-onlyfans | 22 | 1808 | 9 | 138 | how to go live on onlyfans |
| /ru/help-ru/start/kak-provodit-translyaciyu-na-bongacams | — | — | — | 109 | (RU) |
| /ru/help-ru/start/kak-provodit-translyaciyu-na-stripchat | — | — | — | 100 | (RU) |
| /help/video-tutorials/how-to-stream-on-flirt-4-free | 17 | 4290 | 8 | — | flirt for free cam |
| /help/start/how-to-stream-on-camplace-2 | 10 | 1261 | 12 | — | streamate login |
| /help/video-tutorials/how-to-stream-on-camsoda | 9 | 765 | 3 | 11 | camsoda live (vol 250) |
| /help/start/how-to-stream-to-xlovecam | 11 | 596 | 5 | 16 | x love cam |
| /help/start/how-to-add-stripchat-stream | 9 | 0 | 3 | 5 | stripchat live stream |
| /blog/2020/how-to-add-stripchat-stream.html | 9 | 929 | 2 | 6 | strip cam (vol 3600) |
| /help/start/how-to-add-cam4-stream | 0 | 0 | 1 | 30 | cam4.com |
| /help/start/how-to-stream-on-bongacams | 0 | 0 | 1 | 14 | bongcams |
| /help/start/how-to-stream-on-imlive | 5 | 73 | 6 | — | im live stream |
| /help/video-tutorials/how-to-stream-on-xlovecam | 0 | 0 | 2 | — | xlovecam (vol **1900**) |
| /help/start/how-to-stream-to-soulcams | 2 | 110 | 1 | — | soul cams |
| /help/video-tutorials/how-to-stream-on-streamate | 0 | 0 | 3 | — | streamate |
| /help/start/how-to-add-virtwish-stream | — | — | — | 5 | — |
| /help/video-tutorials/how-to-stream-on-streamray | 1 | 105 | 2 | — | streamray cam |
| /help/video-tutorials/splitcam-10-...broadcast-on-bongacams-chaturbate-cam4-stripchat... | 1 | — | 1 | — | stripchat chaturbate |
| /blog/2020/how-to-add-mfc-alerts.html | 0 | — | 1 | — | mfc alerts |

**Note on streamray (1008 rd):** almost certainly spammy adult backlinks. High count, low real quality — see seo/REDIRECTS.md adult-content note.

---

## TIER B — low / zero weight (migrate, but no special care)

**EN — /help/start/:** how-to-add-chaturbate-stream · how-to-add-mfc-alerts · how-to-stream-on-camplace
**EN — /help/video-tutorials/:** how-to-add-a-lovense-toy-to-your-stream · how-to-add-mfc-alerts · how-to-add-stripchat-stream · how-to-add-virtwish-stream · how-to-stream-on-bongacams · how-to-stream-on-cam4 · how-to-stream-on-camplace · how-to-stream-on-chaturbate · how-to-stream-on-imlive · how-to-stream-on-onlyfans · how-to-stream-on-soulcams · how-to-stream-on-vxlive · how-to-stream-to-xmodels

---

## Platforms covered (consolidation targets — one page each on new domain)

| Platform | EN pages | RU pages | ES pages | → new slug |
|---|--:|--:|--:|---|
| Chaturbate | 2 | 2 | 2 | /chaturbate/ |
| CAM4 | 2 | 2 | 2 | /cam4/ |
| BongaCams | 2 | 2 | — | /bongacams/ |
| Stripchat | 3 | 2 | — | /stripchat/ |
| OnlyFans | 2 | 2 | — | /onlyfans/ |
| CamPlace | 3 | 2 | — | /camplace/ |
| CamSoda | 1 | 2 | — | /camsoda/ |
| Streamate | 1 | 2 | — | /streamate/ |
| StreamRay | 2 | 2 | — | /streamray/ |
| XLoveCam | 2 | 2 | — | /xlovecam/ |
| SoulCams | 2 | 2 | — | /soulcams/ |
| ImLive | 2 | 2 | — | /imlive/ |
| VXLive | 1 | 2 | — | /vxlive/ |
| Virtwish | 2 | 2 | — | /virtwish/ |
| XModels | 1 | 1 | — | /xmodels/ |
| Flirt4Free | 1 | 1 | — | /flirt4free/ |
| MyFreeCams (MFC alerts) | 2 + 1 blog | 1 | 1 | /mfc-alerts/ |
| Lovense (toy) | 1 | 2 | 1 | /lovense/ |
| Multi-broadcast guide | 1 | 1 | — | /multistream-cams/ |

**~19 consolidated pages per language.** Recommended: build EN first (19 pages), then RU (19), then ES (6 — or drop ES, lowest priority).

## Full URL list
See `seo/data/` after rerunning, or `/tmp/sc-all-urls.txt`. Raw adult URL list is in this repo's git history of this commit.
