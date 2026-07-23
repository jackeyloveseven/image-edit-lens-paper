# fig19_k9_curve

## Intent

Nested learning curve (K9) isolating nonlinearity from fit capacity: (a) held-out and train-val R^2 vs nested training-case count N, train-val plateaus regardless of N (expressivity ceiling); (b) composition-swap control confirming the N=3->6 rise is a true N effect.

## Used in

- supplement.tex

Current placement: supplement Figure 19.

## Target caption

### supplement.tex

\textbf{Nested learning curve isolates nonlinearity from
  fit capacity (K9).} \textbf{(a)} Held-out $R^2$ (solid, by
  case$\times$layer) and train--val $R^2$ (dash-dot, layer only) at
  the terminal step ($t{=}19$) vs.\ nested training-case count $N$.
  Train--val plateaus at $\approx0.80$ (L52) / $\approx0.90$ (L56),
  invariant to $N$ -- an expressivity ceiling, not undersampling.
  \textbf{(b)} Composition-swap control: held-out $R^2$ under two
  independent case orderings at matched $N$ (N6 vs.\ N6$'$, N9 vs.\
  N9$'$) agree to within $0.055$, confirming the $N{=}3{\to}6$ rise
  tracks case count, not which cases were added. Data:
  \texttt{runs/k9\_capacity\_curve/}.

## Generation

- Script: `fig19_k9_curve.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/k9_capacity_curve/summary.json (results_per_config.*.held_out_r2 / train_val_r2)

- Note: Redrawn 2026-07-14 from raw runs/ data to house style. See paper/provenance.md 'K7/K8/K9 figures added' section.

## Files in this folder

- `fig19_k9_curve.jpg`
- `fig19_k9_curve.png`
- `fig19_k9_curve.py`
