# fig15_preview_lever

## Intent

Differential lens as a ~15%-NFE (t=2) preview lever: 3 of a 10-case battery, each showing the final edited output alongside the L52/t2 differential D with the true edit region outlined in red (object-removal ghost, keep-vs-replace background segmentation, tiny recolor glow).

## Used in

- AAAI submission (main_aaai.tex, via aaai_draft/*.tex)
- supplement.tex

## Target caption

### AAAI submission (aaai_draft/20_experiments.tex)

\textbf{Differential preview at 15\% NFE.} Final edits (left) and
$D_{\mathrm{L52},t2}$ previews (right, true edit boundary in red): removal,
keep-vs-replace background structure, and a tiny recolor are visible after
only three of twenty denoising steps.

Current placement: main Figure 7; supplement Figure 10.

### supplement.tex

The differential lens as a $t{=}2$ ($\approx$15\% NFE)
  preview lever: three of the ten-case battery
  (\S\ref{sec:previewlever}). Left: each case's final edited output.
  Right: $D_{\text{L52},t2}$ (grayscale) with the ground-truth edit
  region $R$'s boundary overlaid in red. \emph{remove\_duckfloat}: the
  whole object slated for removal lights up as a duck-shaped ghost (IoU
  $0.81$, AUROC $0.995$). \emph{bg\_tatami}: a keep-vs-replace
  segmentation emerges unsupervised -- the three food bowls the prompt
  asks to preserve stay dark against a bright to-be-replaced background.
  \emph{color\_eyes}: two glowing eyes again, at only 15\% of the
  denoising trajectory -- visually the sharpest preview in the battery
  despite the lowest IoU/AUROC, because the fixed top-10\%
  ground-truth mask $R$ is padded roughly $10\times$ by collateral fur
  divergence around this tiny true edit (a metric artifact, not a
  preview failure).

## Generation

- No plotting/compositing script is preserved in this repo -- see the note below for how to regenerate.

- Data sources:

  - runs/k4_preview_lever/ (per-case *_preview_L52_t2.png, *_editregion.png, *_unchanged_edited.png, *_edit_edited.png)
  - underlying K4 experiment driver: experiments/k4_preview_lever.py (generates the runs/k4_preview_lever/ data this figure panels are drawn from; this script lives in the main project's experiments/, not in paper/figs/)

- Note: No plotting/compositing script for the assembled 3-case panel image itself is preserved in this repo. See project memory 'K4 t2 早览杠杆' for the experimental narrative. To regenerate: re-run experiments/k4_preview_lever.py, then re-assemble the 3-case panel (final output + red-outlined D at L52/t2) for the same three battery cases (remove_duckfloat, bg_tatami, color_eyes per the supplement caption).

## Files in this folder

- `fig15_preview_lever.jpg`
- `fig15_preview_lever.png`
