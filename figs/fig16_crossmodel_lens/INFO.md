# fig16_crossmodel_lens

## Intent

Lens toolchain transfer to FireRed-Image-Edit-1.1 (K6): 3-rung transfer ladder R^2 (L0 frozen / L1 recalibrated / L2 native-refit) across probed layers, plus the anti-image replicating on FireRed (raw vs tuned decode at L24, t12).

## Used in

- supplement.tex

Current placement: supplement Figure 16.

## Target caption

### supplement.tex

The lens toolchain transfers to FireRed-Image-Edit-1.1.
  \textbf{A}: test $R^2$ at $t{=}2$ across the 9 probed layers for the
  three-rung transfer ladder on held-out \emph{car\_red} -- L0 (\model{}
  translator dictionary $W$, fully frozen), L1 (same $W$, FireRed's own
  recalibration), L2 (FireRed-native refit of $W$ and calibration). At
  deep layers all three converge with L1$\approx$L2, showing $W$ itself
  needs no refitting; the shaded band marks L6/L12, the one region where
  L1 can dip below L0 (data: \texttt{ladder\_r2.json}). \textbf{B}: the
  anti-image replicates -- the same cell (L24, $t{=}12$) decoded by the
  raw frozen head (left) versus the native tuned lens (right): a cyan
  car under a red-brown sky versus the correct red car under blue sky,
  pixel-Pearson-vs-final $-0.36$ vs.\ $+0.98$ (data:
  \texttt{cells/\{raw,tuned\}\_L24\_t12.png}, \texttt{summary.json}).

## Generation

- No plotting/compositing script is preserved in this repo -- see the note below for how to regenerate.

- Data sources:

  - runs/k6_firered_lens/{tuned_grid.png,ladder_L0_grid.png,ladder_L2_grid.png,ladder_r2.json}
  - runs/k6_firered_lens/cells/{raw,tuned}_L24_t12.png, summary.json

- Note: No plotting/compositing script preserved in this repo. See project memory 'K6 跨模型 (2026-07-11, C25)' / 'K6b 电池级封口' for the experimental narrative. To regenerate: re-run the K6 FireRed transfer ladder and re-render the R^2-vs-layer curve (ladder_r2.json) plus the raw-vs-tuned L24/t12 decode pair.

## Files in this folder

- `fig16_crossmodel_lens.jpg`
- `fig16_crossmodel_lens.png`
