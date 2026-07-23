# fig13_transfer_onset

## Intent

Zero-retrain transfer to held-out add_runner edit, decoded through the same K1 translators: empty path at t=0, blurred figure by t=2, clear runner by t=4 -- the invention-class delayed onset watched directly on the internal image's time axis.

## Used in

- supplement.tex

Current placement: supplement Figure 8.

## Target caption

### supplement.tex

Zero-retrain transfer to a held-out \emph{add\_runner} edit
  (\S\ref{sec:tunedlens}), decoded at L52 through the same translators
  fit for Figure~\ref{fig:tunedlens}. At $t{=}0$ the internal image
  shows an empty path; a blurred figure appears by $t{=}2$; a clear
  blue-shirted runner is rendered by $t{=}4$ -- the invention-class
  delayed onset of \S\ref{sec:when}, watched directly on the internal
  image's time axis rather than inferred from a probe score. Final
  output shown for reference.

## Generation

- No plotting/compositing script is preserved in this repo -- see the note below for how to regenerate.

- Data sources:

  - runs/k1b_transfer_battery/{add_runner_grid.png,add_runner_edited.png}

- Note: No plotting/compositing script preserved in this repo. See project memory 'K1b 迁移电池' for the experimental narrative. To regenerate: re-run the K1b zero-shot transfer battery on add_runner and re-render `runs/k1b_transfer_battery/add_runner_grid.png`.

## Files in this folder

- `fig13_transfer_onset.jpg`
- `fig13_transfer_onset.png`
