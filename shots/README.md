# Screenshots folder

Drop platform screenshots here. The generator (`build.py`) picks them up
automatically by filename — no code change needed, just rerun `python3 build.py`.

## Naming convention

```
shots/<slug>-<step-number>.<ext>
```

- `<slug>` — the platform slug: `onlyfans`, `chaturbate`, `cam4`, `bongacams`,
  `stripchat`, `camplace`, `camsoda`, `streamate`, `streamray`, `xlovecam`,
  `soulcams`, `imlive`, `vxlive`, `virtwish`, `xmodels`, `flirt4free`,
  `mfc-alerts`, `lovense`, `multistream-cams`.
- `<step-number>` — which guide step the screenshot illustrates (1–5).
  - Step 3 = the platform's broadcast/RTMP settings → `onlyfans-3.png`
  - Step 4 = SplitCam stream settings → `onlyfans-4.png`
- `<ext>` — png, jpg, jpeg or webp.

## Examples

```
shots/onlyfans-3.png      → shown under step 3 of /onlyfans/
shots/onlyfans-4.png      → shown under step 4 of /onlyfans/
shots/chaturbate-3.png    → shown under step 3 of /chaturbate/
```

## Notes

- Screenshots are shared across all languages (EN/RU/ES) — the SplitCam UI
  is the same. One file per platform-step covers all three locale pages.
- Annotate the screenshots (red boxes / arrows for "click here") **before**
  dropping them here — the generator places them as-is.
- The figure caption is auto-set to the step heading.
