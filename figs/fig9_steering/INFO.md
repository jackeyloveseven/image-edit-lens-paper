# fig9_steering

## Intent

Steering dose-response: P(red)/P(green) vs steer strength alpha, with random-direction and negated-direction controls, showing a sharp threshold between alpha=0.5 and alpha=1.

## Used in

- supplement.tex

## Target caption

### supplement.tex

Steering the same \emph{car\_green} recipient toward red by
  adding $\alpha\, d_{\text{red}}$ (the probe direction from
  \S\ref{sec:mechanism}) to car-region rows at L6--23. $P(\text{red})$
  jumps sharply between $\alpha{=}0.5$ and $\alpha{=}1$ and saturates
  thereafter; a random direction at $\alpha{=}2$ (open square) barely
  moves either score; the negated direction at $\alpha{=}2$ (triangle)
  overshoots to \emph{blue}, not back to green.

## Generation

- Script: `fig9_steering.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/g1_steer/summary.json

- Note: Script filename predates later figure insertions; renders as Figure 8, after transplant (\label{fig:steer}).

## Files in this folder

- `fig9_steering.pdf`
- `fig9_steering.py`
