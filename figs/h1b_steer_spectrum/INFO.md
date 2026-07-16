# h1b_steer_spectrum

## Intent

Steering each edit family's own probe direction into a neutral recipient at shallow (L6-23) and, for structure families, deep (L24-47) bands: only removal (the one target state with no geometry) steers cleanly.

## Used in

- supplement.tex

## Target caption

### supplement.tex

Steering each family's own probe direction ($\alpha{=}2$)
  into a neutral-prompt recipient, at the shallow band L6--23 (middle
  column) and, for the structure families, with a direction re-trained
  at L36 and applied at L24--47 (right column). Verdict badges are from
  visual inspection of every output against its baseline; CLIP gains
  corroborate but do not decide (by CLIP alone the crude L12 removal,
  $+0.89$, would outrank the clean L36 one, $+0.76$). Only removal --
  the one edit whose target state has no geometry -- steers cleanly.

## Generation

- No plotting/compositing script is preserved in this repo -- see the note below for how to regenerate.

- Data sources:

  - runs/h1b_steer/{summary.json,visual_verdicts.json}
  - runs/g1_steer/summary.json (color row: alpha_2 vs control_no_steer)

- Note: Generation scripts exist in the main project (NOT in paper/figs/): experiments/h1b_spectrum_fig.py (assembles this figure), experiments/h1b_steer.py (generates the 13 steered-image GPU runs it's built from). Verdict badges are human visual inspection (CLIP forced-choice cannot distinguish clean edits from flat-patch overwrites -- this audit is what downgraded an earlier K/G1 'clean flip' claim to 'crude'). Added v2.2 (2026-07-09).

## Files in this folder

- `h1b_steer_spectrum.jpg`
- `h1b_steer_spectrum.png`
