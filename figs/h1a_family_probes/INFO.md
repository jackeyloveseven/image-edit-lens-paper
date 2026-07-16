# h1a_family_probes

## Intent

Cross-seed 3-class probe accuracy per edit family (5 layers x 3 steps): appearance families (style/background) readable almost immediately in depth, structure families (removal/addition) crystallize only mid-stack or never cleanly.

## Used in

- supplement.tex

## Target caption

### supplement.tex

Cross-seed probe accuracy per edit family (chance $=0.33$),
  the identical protocol behind Figure~\ref{fig:mechanism} (right):
  three prompts per family (two real edits plus one neutral), probe
  trained on seed 0 and tested on seed 1, on region-appropriate token
  rows (whole frame for style, background complement of the subject box
  for background, the object box for removal and addition). Appearance
  families (left two) are readable almost immediately in depth;
  structure families (right two) crystallize only mid-stack (removal
  crosses $0.88$ at L36) or never cleanly at $t\ge4$ (addition).

## Generation

- No plotting/compositing script is preserved in this repo -- see the note below for how to regenerate.

- Data sources:

  - runs/h1a/family_probe_heatmaps.png (verbatim copy)
  - runs/h1a/probe_grids.json (NOTE: has an empty families dict, save bug -- the annotated numbers on the PNG are ground truth, cross-checked manually)
  - runs/h1a/boundary_by_family.json

- Note: Generation script exists in the main project (NOT in paper/figs/): experiments/h1a_probe.py. This figure is a verbatim copy of that script's output, added v2.2 (2026-07-09).

## Files in this folder

- `h1a_family_probes.png`
