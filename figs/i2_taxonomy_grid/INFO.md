# i2_taxonomy_grid

## Intent

(b) Direction taxonomy on the lake hull: attribute directions are steerable, object-identity directions are inert, random directions are destructive, and full-code swap is sufficient where a direction alone fails.

## Used in

- supplement.tex

Current placement: supplement Figure 22b, paired with the carrier grid in
combined Figure 22.

## Target caption

### supplement.tex

(empty -- see combined caption in the figure environment, see note below)

## Generation

- No plotting/compositing script is preserved in this repo -- see the note below for how to regenerate.

- Data sources:

  - runs/i2_mask_synthesis/{summary.json,visual_verdicts.json} (shallow L6-23)
  - runs/i2b_mask_synthesis_deep/{summary.json,visual_verdicts.json} (deep L24-47 retest)
  - runs/i2c_swap_control/{summary.json,visual_verdicts.json} (donor-boat transplant)

- Note: No compositing script preserved. Same stale-placeholder-warning correction as i1d_recompose_grid above -- confirmed real (not placeholder) as of the 2026-07-14 audit. Paired with i1d_recompose_grid as two subfigures of one figure environment (\label{fig:recomposetaxonomy}); the combined caption covers both.

## Files in this folder

- `i2_taxonomy_grid.jpg`
- `i2_taxonomy_grid.png`
