# fig14_diff_lens

## Intent

Differential lens (K3) on color_eyes: edit run's internal image already red at t=0 (early commitment) vs the 'keep unchanged' control's faithful no-op; the differential D condenses from a diffuse gray field (t=0, sig=0.70) to two glowing eyes (t=8, sig=7.76).

## Used in

- supplement.tex

Current placement: supplement Figure 9.

## Target caption

### supplement.tex

A differential lens applied to \emph{color\_eyes} (``change
  the cat's green eyes to red eyes''), decoded at L52 through the
  frozen K1 dictionaries of Figure~\ref{fig:tunedlens}. Top: the edit
  run's internal image already shows red eyes at $t{=}0$ and stays red
  throughout -- commitment is early. Middle: the ``keep the image
  unchanged'' control's internal image keeps the source's green eyes at
  every step -- a faithful no-op. Bottom: the differential
  $D=|\text{edit}-\text{unchanged}|$ is a diffuse gray field over the
  whole face at $t{=}0$ ($\mathrm{sig}=0.70$, at the chance floor), and
  condenses monotonically into two glowing eyes in the dark by $t{=}8$
  ($\mathrm{sig}=7.76$, the sharpest concentration measured anywhere in
  this paper) -- commitment and separation are two different
  quantities.

## Generation

- No plotting/compositing script is preserved in this repo -- see the note below for how to regenerate.

- Data sources:

  - runs/k3b_diff_lens_colorcases/color_eyes_strip.png (byte-identical match confirmed via md5sum against figs/fig14_diff_lens.png)

- Note: No plotting/compositing script preserved in this repo -- the figure IS the raw run output `color_eyes_strip.png`, copied verbatim. See project memory 'K3+K3b 差分透镜' for the experimental narrative and the 'unchanged' no-op prior finding.

## Files in this folder

- `fig14_diff_lens.jpg`
- `fig14_diff_lens.png`
