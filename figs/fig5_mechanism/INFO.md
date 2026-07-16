# fig5_mechanism

## Intent

Four ways to decode a layer's frozen-head output (standard/sign-flip/direct-v/neg-v) at L24 vs L59, plus cross-seed linear-probe accuracy heatmap: shows readability (probe, L6) and frozen-head legibility dissociate.

## Used in

- AAAI submission (main_aaai.tex, via aaai_draft/*.tex)
- supplement.tex

## Target caption

### AAAI submission (aaai_draft/20_experiments.tex)

Left: four ways of turning an intermediate layer's
  frozen-head output into an image for \emph{car\_red} at $t{=}4$ (A:
  standard $\hat{x}_0{=}x_t{-}\sigma_t v_\ell$; B: sign-flipped; C:
  $v_\ell$ decoded directly; D: $-v_\ell$ decoded directly) -- at L24
  the standard decode is wrong-colored while the sign-flipped/direct
  decodes already look red, and at L59 this reverses. Right: cross-seed
  3-way probe accuracy (chance $=0.33$) by layer/step; the headline
  cell L6/$t$4 ($0.883$) is far above the frozen-head reading at the
  same cell, and probe accuracy drops at L59 relative to L48--L54.

### supplement.tex

Left: four ways of turning an intermediate layer's frozen-head
  output into an image for \emph{car\_red} at $t{=}4$ (A: standard
  $\hat{x}_0{=}x_t{-}\sigma_t v_\ell$; B: sign-flipped
  $x_t{+}\sigma_t v_\ell$; C: $v_\ell$ decoded directly; D: $-v_\ell$
  decoded directly). At L24 the standard decode (A) is wrong-colored
  while the sign-flipped/direct-$v$ decodes (B, C) already look red; at
  L59 this reverses. Right: cross-seed 3-way probe accuracy (chance
  $=0.33$) by layer/step; the headline cell L6/$t$4 (red outline,
  $0.883$) is far above the frozen-head reading at the same cell
  (\S\ref{sec:depth}), and probe accuracy \emph{drops} at L59 relative
  to L48--L54.

## Generation

- Script: `fig5_mechanism.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/d1_signflip/d1_results.json
  - runs/d1_signflip/lens_l{24,59}_t4_{A_standard,B_signflip,C_v_as_x0,D_neg_v_as_x0}.png
  - runs/d2_probe/accuracy_grid.json

## Files in this folder

- `fig5_mechanism.pdf`
- `fig5_mechanism.py`
