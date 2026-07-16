# fig17_k7_ladder

## Intent

Rapid-AIO L52 decode ladder (K7) under the sigma-matched three-rung translator dictionary: decode quality visibly degrades only in the coverage-edge final column (sigma=0.02).

## Used in

- supplement.tex

## Target caption

### supplement.tex

\textbf{Rapid-AIO L52 decode ladder under the $\sigma$-matched
  three-rung translator dictionary (K7).} Rows: L0 frozen \model{}
  dictionary, L1 recalibrated, L2 Rapid-AIO-native refit. Columns:
  Rapid-AIO's four sampling steps $t{=}0$--$3$. \textbf{(a)}
  \emph{car\_red}. \textbf{(b)} \emph{style\_ink}. Per-cell numbers are
  the held-out velocity-space $R^2$ for that rung/step. Decode quality
  visibly degrades only in the coverage-edge final column
  ($\sigma{=}0.02$, red outline); the $R^2$ there is negative for
  \emph{style\_ink} L1 even though the pixel decode is a clean ink
  painting, the pixel-invisible failure mode described in prose. Data:
  \texttt{runs/k7\_rapid\_ladder/}.

## Generation

- Script: `fig17_k7_ladder.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/k7_rapid_ladder/cells/ (per-cell PNGs, not the pre-assembled contact sheets)
  - runs/k7_rapid_ladder/summary.json (cases.{case}.test_r2, annotated in-frame)

- Note: Redrawn 2026-07-14 from raw runs/ data to house style (RED/TEAL/GRAY_D palette); replaced an earlier raw-PNG-verbatim pass. See paper/provenance.md 'K7/K8/K9 figures added' section.

## Files in this folder

- `fig17_k7_ladder.jpg`
- `fig17_k7_ladder.png`
- `fig17_k7_ladder.py`
