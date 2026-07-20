# fig1_teaser

## Intent

Teaser: layer x time P(red car) decode grid plus a five-stage measured
layer--time schematic. It distinguishes early outcome prediction from late
frozen-head translation.

## Used in

- AAAI submission (main_aaai.tex, via aaai_draft/*.tex)
- supplement.tex

## Target caption

### AAAI submission (main_aaai.tex)

A layer--time lens for a DiT image editor. Decoding the
  frozen output head at intermediate layers of \emph{car\_red} gives a
  $P(\text{red car})$ grid across layer and denoising step (center); a
  sharp snap between layers 48 and 54 is where the head-readable
  signal first appears, but a linear probe shows the edit is already
  linearly decodable from layer 6. We read this as a five-stage
  five-stage picture (right): the instruction is injected early,
  the realized outcome is predictable from layer 6, most of the stack
  then carries a target-image code, a narrow band (L52--54) translates
  it into the velocity code, and layer 59's frozen head reads it out.

### supplement.tex

A layer--time lens for a DiT image editor. Decoding the
  frozen output head at intermediate layers of \emph{car\_red} gives a
  $P(\text{red car})$ grid across layer and denoising step (center); a
  sharp "snap" between layers 48 and 54 (\S\ref{sec:depth}) is where the
  head-readable signal first appears, but a linear probe shows the edit
  is already linearly decodable from layer 6 (\S\ref{sec:mechanism}). A
  denser sweep (\S\ref{sec:mechanism}) resolves this snap to a sharp,
  timestep-invariant crossover centered at layer $\approx$53. We read
  this as five measured stages (right): the instruction is injected
  early, the realized outcome is predictable from layer 6, most of the stack
  then carries a target-image code, a narrow band (L52--54) translates
  it into the velocity code, and layer 59's frozen head reads it out.

## Generation

- Script: `fig1_teaser.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/wp3_car_red/{source.png,edited.png}
  - runs/a1_car_red/lens_grid.json (grid)
  - runs/t3_implicit_choice/continuous_hue_analysis.json (outcome-prediction box)
  - runs/g2_boundary/boundary_summary.json (Translation box)
  - runs/g3_injection/summary.json (Injection box)

## Files in this folder

- `fig1_teaser.pdf`
- `fig1_teaser.png`
- `fig1_teaser.py`
