# cam-streaming-guides — Project Onboarding

*Last updated: 2026-06-07. Open this at the start of any new chat about this project.*

## What this is
Adult-cam how-to guides — "how to stream on &lt;platform&gt; with SplitCam". Built to move the
adult-cam content **off** splitcam.com onto a separate neutral domain (brand-cleanup decision:
adult = revenue, so it gets its own domain + 301 redirects, not deletion).

- **Local folder:** `/Users/splitcam/Documents/Дизайны/SplitCam/SPLITCAM DEV./cam-streaming-guides/`
- **GitHub repo:** `x270880x/cam-streaming-guides`
- **Live (staging):** https://x270880x.github.io/cam-streaming-guides/
- **Production domain:** `camstreamguide.com` (registered; not yet connected to hosting).
- Sister project: the main SplitCam site (`../splitcam/`).

## Current state
- **1400 pages**: 33 platforms × 35 languages + per-language hubs, legal, OBS-alternative
  and become-a-cam-model pages.
- All pages are `noindex` — this is staging, not the production domain yet.
- Platforms = the original 19 plus the now-complete "14 parent expansion": livejasmin,
  myfreecams, cherry-tv, amateurtv, camster, camversity, skyprivate, manyvids, fansly (1-9),
  ifriends, babestation, adultwork (10-12), jerkmate, justforfans (13-14). All live across
  all 35 languages. Note: jerkmate broadcasts via the Streamate network (reuses the streamate
  flow); justforfans is browser-live so SplitCam connects as a virtual camera.

## How it's built — STATIC GENERATOR
Do not hand-edit the HTML. Edit data, then regenerate.

- `build.py` — the generator (shared dark-theme template, all CSS, page render). `main()`
  imports every `platforms_<code>.py` (35 of them) and merges by slug; a platform is rendered
  for a language only if it exists in that language's file.
- `platforms_<lang>.py` — one file per language (35 total: en, ru, es, de, fr, it, … ja, ar, th,
  he, fa, hi). Each holds a `PLATFORMS_<LANG>` list, one dict per platform. Some files use a
  `_p(...)` helper-constructor style instead of raw dicts — match whatever the file already uses.
- Run: `python3 build.py` → writes `<slug>/index.html` (EN) + `<lang>/<slug>/` for every language,
  plus per-language hubs, legal, OBS-alt and cam-model pages, sitemap.xml, robots.txt.

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
- **Multi-language sync:** any platform added/changed must be replicated to **all 35**
  `platforms_<lang>.py` files (not just en/ru/es), regenerate, verify each platform has 35 dirs.
- **Uniqueness:** pages must stay genuinely distinct (target: no EN pair >65% body similarity)
  so Google indexes each. Current: EN max ~58%, RU ~68%, ES ~53%.
- After meaningful edits: commit + push immediately (GitHub Pages auto-deploys).

## Reference docs in this repo
- `INVENTORY.md` — the 73 source adult pages on splitcam.com (with Ahrefs weights).
- `REDIRECTS.md` — the `.htaccess` 301 map, old splitcam.com URL → new domain
  (uses `camstreamguide.com` as a placeholder).

## Pending before launch
1. ~~Register a neutral domain~~ — **done: `camstreamguide.com`**. Placeholder `NEWDOMAIN.com`
   has been replaced everywhere (canonical, og:url, schema in `build.py`, `REDIRECTS.md`).
2. Connect `camstreamguide.com` to hosting/Pages; then remove `noindex` (in `build.py`,
   two `<meta name="robots">` lines) and rebuild.
3. Apply the `.htaccess` 301 block from `REDIRECTS.md` on splitcam.com **after** the new
   site is live on `camstreamguide.com` — never 301 to URLs that 404.
4. Optional: official platform logos → `logos/`, screenshots → `shots/`, Android SplitCam
   Remote link.

## Deploy
```bash
cd "/Users/splitcam/Documents/Дизайны/SplitCam/SPLITCAM DEV./cam-streaming-guides"
python3 build.py
git add . && git commit -m "..." && git push origin main
```
GitHub Pages auto-deploys in 30–90 sec. Hard-refresh the browser (`Cmd+Shift+R`) — it caches.
