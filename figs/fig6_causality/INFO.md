# fig6_causality

## Intent

Causal ablation (layer-band A, step-window B) + transplant (C), car_red vs beach_background: necessity and sufficiency dissociate by edit family.

## Used in

- AAAI submission (main_aaai.tex, via aaai_draft/*.tex)
- supplement.tex

## Target caption

### AAAI submission (aaai_draft/20_experiments.tex)

Causal ablation and transplant, \emph{car\_red} vs.\
  \emph{beach\_background}. \textbf{A}: ablating a band of layers shows
  opposite profiles -- car needs its \emph{early} layers, beach needs
  its \emph{late} ones. \textbf{B}: ablating a window of steps shows
  car tolerates any single window, beach is destroyed by ablating the
  earliest one. \textbf{C}: transplanting a donor \emph{car\_red} run's
  hidden state into a \emph{car\_green} recipient, at any of four layer
  bands, is \emph{sufficient} to flip the output back to red --
  including the L48--59 band, which panel A shows is \emph{not
  necessary} for the car edit at all.

### supplement.tex

Causal ablation and transplant, \emph{car\_red} vs.\
  \emph{beach\_background}. \textbf{A}: ablating a band of layers (all
  20 steps) shows opposite profiles -- car needs its \emph{early} layers,
  beach needs its \emph{late} ones. \textbf{B}: ablating a window of
  steps (4 mid layers, [12,24,36,48]) shows car tolerates any single
  window, beach is destroyed by ablating the earliest one. \textbf{C}:
  transplanting a donor \emph{car\_red} run's hidden state into a
  \emph{car\_green} recipient, at any of four layer bands, is
  \emph{sufficient} to flip the output back to red -- including the
  L48--59 band, which panel A shows is \emph{not necessary} for the
  car edit at all.

## Generation

- Script: `fig6_causality.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/a3_summary.json (layerwindow + stepwindow scans)
  - runs/a4_summary.json

- Note: Script filename predates later figure insertions; renders as a later-numbered figure in the compiled PDF (see \label{fig:causal}).

## Files in this folder

- `fig6_causality.pdf`
- `fig6_causality.png`
- `fig6_causality.py`
