# fig6_causality

## Intent

Causal ablation (layer-band A, step-window B) + transplant (C), car_red vs beach_background: necessity and sufficiency dissociate by edit family.

## Used in

- supplement.tex only (the main paper retains transplant results in prose)

## Target caption

### supplement.tex

Historical whole-token stress tests and transplant. \textbf{A--B}:
zero-overwrite scores are retained as a methodological negative; exact-region
re-audit shows the edited tokens are driven off-manifold, so these panels
cannot localize fine-grained necessity. \textbf{C}: transplanting a donor
\emph{car\_red} state into a \emph{car\_green} recipient at any tested band
is sufficient to move the output toward red.

## Generation

- Script: `fig6_causality.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/a3_summary.json (layerwindow + stepwindow scans)
  - runs/a4_summary.json

- Note: Current placement is supplement Figure 11 (`\label{fig:causal}`).

## Files in this folder

- `fig6_causality.pdf`
- `fig6_causality.png`
- `fig6_causality.py`
