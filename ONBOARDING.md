# cam-streaming-guides — Project Onboarding

*Last updated: 2026-07-19. Open this at the start of any new chat about this project.*
*Note: sections dated 2026-07 near the bottom (indexing / GSC / IndexNow) are the freshest
and were verified accurate; the counts and status flags up here were re-verified against
disk on 2026-07-19.*

## What this is
Adult-cam how-to guides — "how to stream on &lt;platform&gt; with SplitCam". Built to move the
adult-cam content **off** splitcam.com onto a separate neutral domain (brand-cleanup decision:
adult = revenue, so it gets its own domain + 301 redirects, not deletion).

- **Local folder:** `/Users/splitcam/Documents/Дизайны/SplitCam/SplitCam сайт/cam-streaming-guides/`
- **GitHub repo:** `x270880x/cam-streaming-guides`
- **Live (staging):** https://x270880x.github.io/cam-streaming-guides/
- **Production domain:** `camstreamguide.com` — **connected and live** (GitHub Pages via
  `CNAME`). The old "registered; not yet connected" note was stale and contradicted the
  Current state section right below it.
- **Local preview:** repo-local `.claude/launch.json`, profile `static`, port **8731**.
  ⚠️ Unlike the global `~/.claude/launch.json` entries (splitcam-site/buhta/kherson/
  kadastr-nr), this one runs `python3 -m http.server` **without a docroot argument** —
  it serves the current working directory, so start it from the repo root. There is no
  entry for this project in the global launch.json.
- Sister project: the main SplitCam site (`../splitcam/`).

## Current state
- **54 platforms × 35 languages** (**2 135 pages** on disk = 2 135 `<loc>` in
  `sitemap.xml`, verified 2026-07-19) + per-language hubs, legal, OBS-alternative,
  become-a-cam-model, Lovense and the SEO-grouped category hub.
  (Earlier figures of "44 platforms" / "≈1 800+ pages" were stale; the file also carried
  "40 of 54" and "all 60 EN platform pages" elsewhere — 54 is the real platform count in
  `PLATFORMS_EN`, 60 counts content directories per locale.)
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
3. ~~Apply the `.htaccess` 301 block from `REDIRECTS.md` on splitcam.com~~ — **done.**
   All **75** redirect directives are live in `../splitcam/seo/redirects.htaccess`
   (0 missing, 0 extra — verified on disk 2026-07-19). The "still pending" flag here was
   stale and contradicted the verification section further down this same file.
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
c0f7fc81e 2026-07-19 docs: submit the whole sitemap to IndexNow, not a curated subset
dbb266e3c 2026-07-19 docs: kill two plausible theories with data, and start using IndexNow
6149b066b 2026-07-19 docs: record why the traffic never arrived — it is indexing, not redirects
f96e0c0c2 2026-07-08 lovense: rebuild page as Lovense's official 3-step setup, localized ×35
f265dc36a 2026-07-08 lovense: rebuild HTML with Windows Toolset button
c43c07d8e 2026-07-08 lovense downloads: add Windows Toolset (.exe v1.0.30), drop 'Mac only'
54ef72a8d 2026-07-08 lovense downloads: add Lovense Stream Master
58382df09 2026-07-08 lovense downloads: add Lovense SplitCam Toolset (Mac .dmg direct)
8648e8154 2026-07-07 lovense downloads: Mac SplitCam → direct .dmg from splitcam.com
1a48ff078 2026-07-07 lovense: correct install facts across all 35 languages
2af8335f7 2026-07-07 lovense: auto-link tool mentions in body text (35 langs)
1295163e0 2026-07-07 lovense downloads: clarify Cam Extension IS the plugin
9bd289461 2026-07-07 lovense downloads: fix 3 dead links
9d45391d6 2026-07-07 lovense: add 'What to install' downloads section (35 langs)
61a6c1ca1 2026-07-07 lovense: rewrite guide with accurate 2026 Lovense setup, 35 langs
--- (everything below predates 2026-06-10) ---
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
cd "/Users/splitcam/Documents/Дизайны/SplitCam/SplitCam сайт/cam-streaming-guides"
python3 build.py
git add . && git commit -m "..." && git push origin main
```
GitHub Pages auto-deploys in 30–90 sec. Hard-refresh the browser (`Cmd+Shift+R`) — it caches.

## Indexing reality check — 2026-07-19 (first direct GSC read)

**The redirects are not the problem — they are perfect.** All 75 rules in splitcam.com's
`.htaccess` were tested live end-to-end: every one lands on its correct thematic page here,
**in a single hop, HTTP 200**. The map in `REDIRECTS.md` is implemented with zero drift
(diffed: 0 missing, 0 extra). Do not re-audit this; check something else first.

**The problem is that Google will not index this site.** As of 2026-07-19:

| | |
|---|---|
| Indexed | **16 pages** |
| Not indexed | 211 — of which **156 "crawled — currently not indexed"** |
| Clicks, 10–17 July | **0** (6 impressions) |
| Clicks, 3 months | 30 (2 520 impressions) |
| Sitemap | 2 135 URLs, submitted 2026-06-10, processed 2026-07-15, **Успешно** |

**Everything technical checks out** — verified, so don't go looking for a bug: self-canonical
per locale, 36 hreflang entries, `index, follow`, robots.txt open, 1 160–1 280 words per page,
all 60 EN platform pages linked from the homepage (relative `href="slug/"`, resolves correctly),
no orphans, **no manual actions**, redirect targets all 200.

`/cam4/` was crawled on 2026-07-18 at 19:47 and still not indexed. That is the whole story:
Google sees the pages and declines them. This is a **domain-trust** problem on a 5.5-week-old
site with **zero external links** — splitcam.com sends only 301s, not a single ordinary link
(checked: 0 files in the splitcam repo link here).

⚠️ **Request Indexing quota is per Google ACCOUNT, not per property.** Spending it on
splitcam.com uses up camstreamguide's allowance the same day. On 2026-07-19 only
`/bongacams/` got through before the quota hit; `/cam4/` was refused. Plan the day's ~10-12
requests across both properties.

**Owner decisions (2026-07-19), do not relitigate without asking:**
- **No direct links from splitcam.com.** The whole point of the split was to get adult
  content away from the brand; a link partially undoes that. 301s only.
- **Sitemap stays at all 2 135 URLs.** Not narrowed to EN + top languages.

What that leaves as the working lever: **make the top platform pages genuinely
differentiated.** Sampled pages share ~30 % of their 8-word phrases and every one of the 44
platforms runs the identical 5-step skeleton. For a new domain in this niche that reads as a
template farm, which is exactly the profile behind "crawled — currently not indexed".
Real bitrate limits, RTMP quirks, actual dashboard steps and payout specifics per platform
are what earn the index slot.

**Worth being honest about the ceiling:** of the 131 758 weekly impressions this cluster used
to draw on splitcam.com, ~106 000 were navigational (`cam4`, `бонга камс`, `bongacams`) —
people wanting the platform itself, who converted at 0.2 % even from position 6. A guide site
will not convert them either. The winnable slice is informational, and there this site already
ranks where it is indexed: `how to go live on stripchat` sits at 6.5 with 5.1 % CTR.

### Two theories tested and rejected — 2026-07-19

**1. "The spammy backlinks are poisoning the domain." — NO.** `INVENTORY.md` records 1008
refdomains on the streamray page, characterised there as *"mostly spammy adult links"*, and
the obvious move looked like cutting that redirect so the profile doesn't reach a young
domain. Checked it against **Google's own Links report for splitcam.com** first: 3 333
external links, top donors **reddit.com 487, microsoft.com 153, begindot.com 146,
google.com 110, ambercutie.com 88**, anchors all brand ("splitcam", "www splitcamera com").
No spam cluster, and the streamray page is not even among the top linked pages. The 1008
figure is a May Ahrefs snapshot, and Ahrefs API is at 0 units so it cannot be re-checked.
**Do not break the streamray redirect** — it would discard real equity on an unverified
hunch.

**2. "The money pages are too templated to index." — NO.** `build_steps()` lets a platform
pass `None` for a step and inherit `STEP_TMPL`. Measured: 28 of 270 EN steps are inherited
(10 %), and they sit on exactly the 14 platforms that carry the demand — chaturbate,
bongacams, cam4, stripchat, camsoda, streamate, xlovecam, streamray, flirt4free, camplace,
soulcams, vxlive, virtwish, xmodels — always steps **1 and 3**. Those 14 average **385
characters** of unique step text against **825** for the other 40. So the money pages really
are the thinnest on the site.

But that does not explain the indexing, and the arithmetic says so: **40 of 54 EN platforms
have fully custom steps, and only 16 pages are indexed site-wide.** If templating were the
blocker, those 40 would be in. The ~0.7 % index rate is uniform regardless of page quality.
Rewriting steps 1 and 3 is worth doing on its own merits — they are the pages with demand —
but **do not expect it to move indexing.**

### IndexNow — wired all along, first actually used 2026-07-19

Key `1dce1f527c611c22daebaf1b00b0649a` is served at
`https://camstreamguide.com/1dce1f527c611c22daebaf1b00b0649a.txt` (verified 200, content
matches filename), and Bing (`msvalidate.01`) + Yandex verification meta tags are live on
every page. None of it had ever been submitted — `site:camstreamguide.com` on Bing returns
essentially nothing.

**Submit the WHOLE sitemap, not a hand-picked subset.** IndexNow takes up to 10 000 URLs per
request and has **no daily quota** — the GSC habit of rationing does not apply here and
picking "money pages" only leaves the rest undiscovered for no reason. On 2026-07-19 all
**2 135** URLs went out in 5 chunks of 500: api.indexnow.org 200×5, bing.com/indexnow 200×5,
yandex.com/indexnow 202×5. (An earlier attempt the same day sent only 21 pages — that was
Google-thinking applied where it does not belong.)

Bing and Yandex index young domains far more readily than Google, so this is the one route
that can produce traffic here without waiting on Google's trust. **Re-ping the full sitemap
after every `build.py` run.**
