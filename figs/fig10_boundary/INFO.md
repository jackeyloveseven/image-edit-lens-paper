# fig10_boundary

## Intent

Dense every-layer L44-59 sweep of car_red sharpening the coarse L48/L54 snap to a precise crossover boundary (A: decode crossover, B: cosine similarity to terminal v, C: probe accuracy).

## Used in

- AAAI submission (main_aaai.tex, via aaai_draft/*.tex)
- supplement.tex

## Target caption

### AAAI submission (aaai_draft/20_experiments.tex)

A dense, every-layer sweep of \emph{car\_red} over L44--L59
  sharpens the coarse L48/L54 snap to a precise boundary.
  \textbf{A}: the standard decode and the direct-$v$ decode cross
  between L52 and L54 at both steps shown. \textbf{B}: cosine
  similarity of the intermediate pseudo-velocity to the terminal
  $v_{59}$ rises sharply in the same band. \textbf{C}: cross-seed probe
  accuracy is flat from L44 through L58 and drops only at the terminal
  layer.

### supplement.tex

A dense, every-layer sweep of \emph{car\_red} over L44--L59
  sharpens the coarse L48/L54 snap of Figure~\ref{fig:depth} to a precise
  boundary. \textbf{A}: the standard decode (A) and the direct-$v$ decode
  (C) cross between L52 and L54 at both steps shown. \textbf{B}: cosine
  similarity of the intermediate pseudo-velocity to the terminal $v_{59}$
  rises sharply in the same band. \textbf{C}: cross-seed probe accuracy is
  flat from L44 through L58 and drops only at the terminal layer.

## Generation

- Script: `fig10_boundary.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/g2_boundary/boundary_summary.json (cross-checked against sweep.json and dense_probe_accuracy.json, same numbers)

- Note: Script kept its build-order name; renders as Figure 6 in \S5.3 (\label{fig:boundary}), v2.1 addition.

## Files in this folder

- `fig10_boundary.pdf`
- `fig10_boundary.py`
