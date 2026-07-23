# fig7_applications

## Intent

Three practical applications of the lens: decision-saliency map beats raw magnitude heatmap, step-budget prediction from early commitment, mid-stack transplant rescue of under-strength edits.

## Used in

- supplement.tex

Current placement: supplement Figure 14.

## Target caption

### supplement.tex

Three practical uses of the lens. Left: a saliency map built
  from the trained linear probe at the L12/$t$4 hero cell puts $99\%$ of
  its top-decile mass inside the car region, vs.\ $38\%$ for a raw
  magnitude heatmap at the same cell (chance level $19\%$). Center: three
  cases run at genuinely reduced step budgets (4, 8, 20 steps); the two
  early-committing cases are already near their 20-step target score at
  4 steps, the delayed-onset case needs slightly more. Right: transplanting
  L6--23 hidden states from a stronger (CFG 7) run into a weaker (CFG 4)
  recipient rescues an under-strength edit about as well as simply
  raising the recipient's own guidance scale.

## Generation

- Script: `fig7_applications.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/e1_saliency/summary.json
  - runs/e1_saliency/saliency_L12_t4.png
  - runs/e1_saliency/red_edited_reference.png
  - runs/e3_earlyexit/summary.json
  - runs/e3_rescue/summary.json

- Note: Script filename predates later figure insertions; current label is
  supplement Figure 14 (`\label{fig:apps}`).

## Files in this folder

- `fig7_applications.pdf`
- `fig7_applications.py`
