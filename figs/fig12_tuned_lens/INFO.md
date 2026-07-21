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

- Script: `fig12_tuned_lens.py` (recomposes the preserved 512px cells into
  the symmetric 2x3 main-paper layout; no model rerun is required).
- Font: resolved at runtime in the order Source Sans 3 -> Arimo -> Arial/Helvetica -> DejaVu Sans; current build uses Arimo.

- Data sources:

  - runs/k1_tuned_lens/{tuned_grid.png,tuned_pooled_grid.png,raw_grid.png,cells/*.png}

- Layout: top row uses tuned L24/L36/L52 at t0; bottom row compares raw
  L36/t12, tuned L36/t12, and the final output.

## Files in this folder

- `fig12_tuned_lens.jpg`
- `fig12_tuned_lens.png`
- `fig12_tuned_lens.pdf`
- `fig12_tuned_lens.py`
