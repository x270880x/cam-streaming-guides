# Platform logos folder

Drop a platform's official logo here and the generator (`build.py`) places it
in that platform's hero collab automatically — no code change, just rerun
`python3 build.py`.

## Naming convention

```
logos/<slug>.<ext>
```

- `<slug>` — the platform slug: `chaturbate`, `cam4`, `bongacams`, `stripchat`,
  `onlyfans`, `camplace`, `camsoda`, `streamate`, `streamray`, `xlovecam`,
  `soulcams`, `imlive`, `vxlive`, `virtwish`, `xmodels`, `flirt4free`,
  `mfc-alerts`, `lovense`, `multistream-cams`.
- `<ext>` — `svg` (best), `png` or `webp`.

## Examples

```
logos/chaturbate.svg   → shown in the Chaturbate page hero collab
logos/onlyfans.png     → shown in the OnlyFans page hero collab
```

## Notes

- Until a logo file is present, the collab shows the platform name as a clean
  wordmark in its brand colour — so the site looks finished without logos.
- The logo renders at ~21px tall; use a logo with transparent background and
  reasonable contrast against the platform's brand colour.
- These are third-party trademarks — using them is the site owner's decision.
  The generator only provides the slot.
