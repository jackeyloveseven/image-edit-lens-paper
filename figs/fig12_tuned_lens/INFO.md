# fig12_tuned_lens

## Intent

Tuned lens (K1) renders a coherent internal image at every depth from t=0 on held-out car_red (zero-shot ridge translators fit on remove/background/addition), vs the frozen head's color-inverted 'anti-image' ghost at t=12 for the same L36 state.

## Used in

- AAAI submission (main_aaai.tex, via aaai_draft/*.tex)
- supplement.tex

## Target caption

### AAAI submission (aaai_draft/20_experiments.tex)

A tuned lens renders the internal image the frozen head
  cannot read. Top: per-(layer, timestep) ridge translators, fit on
  \emph{remove}/\emph{background}/\emph{addition} edits and evaluated
  zero-shot on the held-out \emph{car\_red} color edit, decode a
  coherent scene at every depth at $t{=}0$, watching the edit enter the
  internal image layer by layer. Bottom: at $t{=}12$ the raw frozen
  head renders the identical L36 hidden state as a color-inverted
  ghost -- the complement of the true scene -- while the tuned lens at
  the same cell is already coherent.

### supplement.tex

A tuned lens renders the internal image the frozen head
  cannot read. Top: per-(layer, timestep) ridge translators, fit on
  \emph{remove}/\emph{background}/\emph{addition} edits and evaluated
  zero-shot on the held-out \emph{car\_red} color edit, decode a
  coherent scene at every depth at $t{=}0$ -- pixels here are pure
  noise, so every pixel of the decode comes from the velocity code
  alone. The source's blue car (L12--L24) turns orange-red (L36), the
  scene composes fully (L44), and the car is fully red by L52: the
  edit entering the internal image, watched layer by layer. Bottom: at
  $t{=}12$ the raw frozen head (\S\ref{sec:depthlens}) renders the
  identical L36 hidden state as a color-inverted ghost -- a cyan car
  under a red-brown sky, the complement of the true scene -- while the
  tuned lens at the same cell is already coherent; the model's actual
  final output is shown for reference.

## Generation

- No plotting/compositing script is preserved in this repo -- see the note below for how to regenerate.

- Data sources:

  - runs/k1_tuned_lens/{tuned_grid.png,tuned_pooled_grid.png,raw_grid.png,cells/*.png}

- Note: No plotting/compositing script preserved in this repo (same convention as fig13/14/16 -- raw PNG from the runs/ folder was used directly, per provenance.md's fig12-fig16/K1-K6 note). See project memory 'K1 tuned lens (2026-07-11, C21)' / 'K1b transfer battery' for the full experimental narrative behind this figure. To regenerate or re-derive: re-run the K1 tuned-lens fit and re-render `runs/k1_tuned_lens/tuned_grid.png` (or `tuned_pooled_grid.png`), then re-crop/relabel to match the current caption.

## Files in this folder

- `fig12_tuned_lens.jpg`
- `fig12_tuned_lens.png`
