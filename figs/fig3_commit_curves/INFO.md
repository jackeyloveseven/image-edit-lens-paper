# fig3_commit_curves

## Intent

Time-lens P(target)@L59 vs denoising step for 8 of 10 battery cases: most edits commit near step 0, the one novel-object-insertion case rises late.

## Used in

- supplement.tex

## Target caption

### supplement.tex

Time-lens $P(\text{target})$ at the final readable layer
  (L59) across the denoising trajectory, for 8 of our 10 battery cases
  (\S\ref{sec:when}), colored by edit category. Preserving edits
  (color-change, most background-replacement) print near their final
  value from step 0; \emph{add\_boat}, the one novel-object insertion,
  only rises after step $\sim$4. Object-removal cases (2 of 10) are
  excluded here and shown separately in Table~\ref{tab:battery}: their
  target label ("an empty desk with no cup") is not a CLIP-friendly
  category and the readout is flat/noisy regardless of the true edit
  outcome (\S\ref{sec:limits}).

## Generation

- Script: `fig3_commit_curves.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/a5_{add_boat,add_latte,bg_beach,bg_forest,color_car,color_cup,style_sketch,style_watercolor}/lens_grid.json

## Files in this folder

- `fig3_commit_curves.pdf`
- `fig3_commit_curves.png`
- `fig3_commit_curves.py`
