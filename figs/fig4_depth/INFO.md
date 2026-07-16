# fig4_depth

## Intent

Depth-lens decode thumbnails + P(red car) vs layer curves: flat/wrong-colored decode through L42-48, then a sharp snap to red between L48-54.

## Used in

- supplement.tex

## Target caption

### supplement.tex

Depth lens on \emph{car\_red}. Left: decoded depth-lens
  preview at 5 layers $\times$ 3 steps, with the frozen head's
  $P(\text{red car})$ overlaid (red text $>0.5$); L0--L48 renders a
  \emph{blue/tan car} (source color or its complement), not red, despite
  the final output being red. Right: $P(\text{red car})$ vs.\ layer for
  5 timesteps -- flat and low through L42, then a sharp rise
  ("snap", shaded) between L48 and L54 that lands within a few points of
  the L59 value.

## Generation

- Script: `fig4_depth.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/a1_car_red/lens_grid.json
  - runs/a1_car_red/contact_sheet_raw.png

## Files in this folder

- `fig4_depth.pdf`
- `fig4_depth.py`
