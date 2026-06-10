# cam-streaming-guides — Project Onboarding

*Last updated: 2026-06-09. Open this at the start of any new chat about this project.*

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
- **44 platforms × 35 languages** (≈ 1 800+ pages) + per-language hubs, legal,
  OBS-alternative, become-a-cam-model and the new SEO-grouped category hub.
- Production domain **`camstreamguide.com` is connected** — `noindex` has been
  removed from all content pages; Google can index. Bing + Yandex webmaster
  verification slots wired in `build.py`; GSC verification meta tag in place.
- Platform set: original 19 + 14-parent expansion (livejasmin, myfreecams,
  cherry-tv, amateurtv, camster, camversity, skyprivate, manyvids, fansly,
  ifriends, babestation, adultwork, jerkmate, justforfans) **+11 added in
  2026-06 batches:** 5 cam-model platforms, 4 regional cam platforms,
  MyFans.jp + Privacy.com.br (Brazil/Japan).
- New SEO topology: category-grouped hub (live-cam / cam-model / regional
  / virtual-camera / OBS-alt) with anchor TOC, cross-refs, 3-level
  breadcrumbs and method-aware "related-cards" + autolinked brand mentions
  in body copy.
- FAQ depth: **5 universal FAQ entries per platform × 35 langs** added
  (≈ 9 450 Q&A pairs) so every page hits Schema FAQPage threshold.
- Brand: redesigned to a signal-broadcast / signal-waves icon, matching
  favicon, white wordmark with colored 'Stream'. Language switcher reordered
  by popularity. CJK titles trimmed to ≤34 chars for zh/ko on a few slugs.

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
- **SEO meta (per platform, all langs):** `title` front-loaded "how to broadcast/stream/go live
  on {Brand} with SplitCam", ≤60 chars (≤34 CJK); `desc` ≤155 chars, compelling, complete
  sentence; `kw` = native intent + brand + modifier long-tail ({brand} obs/external encoder/
  rtmp/stream key) — brands are unwinnable head terms (KD 67-71), so target the long-tail.
  Keep verbs truthful to each page's real broadcast mechanism.
- After meaningful edits: commit + push immediately (GitHub Pages auto-deploys).

## Reference docs in this repo
- `INVENTORY.md` — the 73 source adult pages on splitcam.com (with Ahrefs weights).
- `REDIRECTS.md` — the `.htaccess` 301 map, old splitcam.com URL → new domain
  (uses `camstreamguide.com` as a placeholder).

## Pending before launch
1. ~~Register a neutral domain~~ — **done: `camstreamguide.com`**.
2. ~~Connect domain + remove `noindex`~~ — **done.** Live, indexable.
3. Apply the `.htaccess` 301 block from `REDIRECTS.md` on splitcam.com **after** the new
   site is live on `camstreamguide.com` — never 301 to URLs that 404. **← still pending.**
4. Optional: official platform logos → `logos/`, screenshots → `shots/`, Android SplitCam
   Remote link.

## Session log — 2026-06-09 (June launch push)

The site went **live on `camstreamguide.com`** this iteration. Big swing:

- **Launch:** removed `noindex` from all content pages (`build.py`), wired
  Google / Bing / Yandex Search Console verification slots, regenerated.
- **+11 new platforms × 35 langs (≈ 385 new pages):** 5 cam-model
  platforms, 4 regional cam platforms, MyFans.jp + Privacy.com.br. Each
  passes the multi-language sync rule (all 35 `platforms_<lang>.py` files).
- **SEO topology overhaul:** category-grouped hub (live-cam / cam-model /
  regional / virtual-camera / OBS-alt) with anchor-link TOC,
  method-aware related-cards, autolinked brand mentions in body, and
  3-level breadcrumbs on every page.
- **FAQ depth:** added 5 universal FAQ entries per platform × 35 langs
  → ≈ 9 450 new Q&A pairs, every page now meets FAQPage Schema threshold.
- **Brand:** redesigned logo (signal-waves / signal-broadcast icon),
  matching favicon, colored 'Stream' wordmark; language switcher
  reordered by usage. CJK titles trimmed to ≤34 chars on a few slugs
  (zh/ko fc2-live, mym-fans, boosty, amateurcommunity).
- **Hub polish:** MyFreeCams pinned 3rd, MFC moved to 2nd in right col,
  added Stream / Virtual-camera filter.

Still pending: `.htaccess` 301 block on splitcam.com (item 3 above).

## Recent commits — main cam-streaming-guides repo (most recent first)
```
ebb02ed68 SEO topology: category-grouped hub + anchor TOC + cross-refs + 3-level breadcrumbs
6959caa22 verify: enable Bing + Yandex webmaster tools
997d1e114 internal linking: method-aware related-cards + autolinked brand mentions
c0710f315 SEO: add 5 universal FAQ entries per platform × 35 langs (+9 450 Q&A pairs)
220e651c0 launch: add GSC / Bing / Yandex verification slots in build.py
94bc4c644 launch: remove noindex from content pages (domain connected, Google can index now)
35c40206a Add MyFans.jp + Privacy.com.br × 35 languages (70 new pages)
3418d9dbc qc: trim 6 CJK titles to ≤34 chars (zh/ko fc2-live, mym-fans, boosty, amateurcommunity)
5c223f101 Add 4 regional cam platforms × 35 languages (140 new pages)
2c14bbc29 Add 5 cam-model platforms × 35 languages (175 new pages)
2890fdb2b brand: signal-waves logo + language switcher ordered by popularity
c7047c5db Redesign brand logo to signal-broadcast icon
fadb3306b Hub: pin MyFreeCams to 3rd, shift the rest down by one
5be96c7f3 Hub: move MFC to 2nd in right column + add Stream/Virtual-camera filter
d13326d3f Brand polish: camera-lens logo, white wordmark with colored 'Stream', matching favicon
```

## Deploy
```bash
cd "/Users/splitcam/Documents/Дизайны/SplitCam/SPLITCAM DEV./cam-streaming-guides"
python3 build.py
git add . && git commit -m "..." && git push origin main
```
GitHub Pages auto-deploys in 30–90 sec. Hard-refresh the browser (`Cmd+Shift+R`) — it caches.
