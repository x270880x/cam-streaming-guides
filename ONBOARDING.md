# cam-streaming-guides — Project Onboarding

*Last updated: 2026-05-21. Open this at the start of any new chat about this project.*

## What this is
Adult-cam how-to guides — "how to stream on &lt;platform&gt; with SplitCam". Built to move the
adult-cam content **off** splitcam.com onto a separate neutral domain (brand-cleanup decision:
adult = revenue, so it gets its own domain + 301 redirects, not deletion).

- **Local folder:** `/Users/splitcam/Documents/Дизайны/SplitCam/SPLITCAM DEV./cam-streaming-guides/`
- **GitHub repo:** `x270880x/cam-streaming-guides`
- **Live (staging):** https://x270880x.github.io/cam-streaming-guides/
- Sister project: the main SplitCam site (`../splitcam/`).

## Current state
- **60 pages**: 19 platforms × EN/RU/ES + 3 language hubs.
- All pages are `noindex` — this is staging, not the production domain yet.
- Platforms: chaturbate, cam4, bongacams, stripchat, onlyfans, camplace, camsoda, streamate,
  streamray, xlovecam, soulcams, imlive, vxlive, virtwish, xmodels, flirt4free, mfc-alerts,
  lovense, multistream-cams.

## How it's built — STATIC GENERATOR
Do not hand-edit the HTML. Edit data, then regenerate.

- `build.py` — the generator (shared dark-theme template, all CSS, page render).
- `platforms_en.py` / `platforms_ru.py` / `platforms_es.py` — per-platform content, one dict each.
- Run: `python3 build.py` → writes `<slug>/index.html`, `ru/<slug>/`, `es/<slug>/` + 3 hubs.

Each generated page: hero with platform×SplitCam collab logo (variant C, animated dot flowing
SplitCam→platform), quick answer, YouTube video guide, 5-step guide, pro tips, FAQ,
Schema.org (BreadcrumbList + HowTo + FAQPage + SoftwareApplication), EN/RU/ES switcher,
full meta (OG + Twitter cards).

## Asset slots (drop a file, rerun build.py)
- `logos/<slug>.svg` (or png/webp) — official platform logo for the hero collab. Until present,
  a brand-colour wordmark is shown. See `logos/README.md`.
- `shots/<slug>-<n>.png` — screenshot for guide step `<n>`. See `shots/README.md`.
- `assets/splitcam.png` — the official SplitCam logo (already present).

## Rules
- **Multi-language sync:** any content added/changed in one language must be replicated to
  all three — keep `platforms_en/ru/es.py` in sync, regenerate, verify counts match.
- **Uniqueness:** pages must stay genuinely distinct (target: no EN pair >65% body similarity)
  so Google indexes each. Current: EN max ~58%, RU ~68%, ES ~53%.
- After meaningful edits: commit + push immediately (GitHub Pages auto-deploys).

## Reference docs in this repo
- `INVENTORY.md` — the 73 source adult pages on splitcam.com (with Ahrefs weights).
- `REDIRECTS.md` — the `.htaccess` 301 map, old splitcam.com URL → new domain
  (uses `NEWDOMAIN.com` as a placeholder).

## Pending before launch
1. Register a neutral adult domain (not brand-associated). Then replace `NEWDOMAIN.com`
   everywhere (canonical, og:url, schema, REDIRECTS.md).
2. Connect the domain to hosting/Pages; remove `noindex`.
3. Apply the `.htaccess` 301 block on splitcam.com **after** the new site is live.
4. Optional: official platform logos → `logos/`, screenshots → `shots/`, Android SplitCam
   Remote link.

## Deploy
```bash
cd "/Users/splitcam/Documents/Дизайны/SplitCam/SPLITCAM DEV./cam-streaming-guides"
python3 build.py
git add . && git commit -m "..." && git push origin main
```
GitHub Pages auto-deploys in 30–90 sec. Hard-refresh the browser (`Cmd+Shift+R`) — it caches.
