# fig2_method

## Intent

Method/pipeline diagram: token layout, capture taps, depth-lens vs time-lens routes, decode-then-CLIP readout. Illustrative, not data-driven.

## Used in

- AAAI submission (main_aaai.tex, via aaai_draft/*.tex)
- supplement.tex

## Target caption

### AAAI submission (main_aaai.tex)

Pipeline. The image stream concatenates noisy target tokens
  with always-clean condition tokens; each block's post-block residual
  is tapped and read two ways -- the \emph{depth lens} pushes it through
  the model's own frozen output head before decoding, the \emph{time
  lens} instead reads the current step's head output combined with the
  current latent ($\hat{x}_0{=}x_t{-}\sigma_t v$). Both routes end in a
  decode-then-CLIP readout, computed identically for both true-CFG
  passes.

### supplement.tex

Method overview. The image stream concatenates noisy target
  tokens with always-clean condition tokens (\texttt{zero\_cond\_t});
  each block's post-block residual can be tapped and read two ways: the
  \emph{depth lens} pushes it through the frozen output head before
  decoding, the \emph{time lens} instead reads the current step's own
  head output and combines it with the current latent
  ($\hat{x}_0{=}x_t{-}\sigma_t v$). Both routes end in a decode-then-CLIP
  readout, computed identically for both true-CFG passes.

## Generation

- Script: `fig2_method.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - no numeric data -- conventions taken from image_edit_lens/models/hooks.py and README.md

## Files in this folder

- `fig2_method.pdf`
- `fig2_method.py`
