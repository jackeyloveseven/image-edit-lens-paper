# fig8_appendix

## Intent

Appendix self-correction case: IoU-vs-final onset curves for 6 non-global-edit cases, plus the add_boat storyboard showing in-place growth (not relocation of an earlier draft).

## Used in

- supplement.tex

## Target caption

### supplement.tex

The self-correction case from \S\ref{sec:limits}. Top: IoU
  of the per-step edit mask against its final mask, for the 6
  non-global-edit battery cases. Five cases ("printing") are already
  $\ge0.67$ IoU at step 0; \emph{add\_boat} ("thinking") is entirely
  absent until step 4 and then grows to IoU $1.00$ by step 19. Bottom:
  the \emph{add\_boat} storyboard showing this growth happens
  \emph{in place}, not via relocation of an earlier draft.

## Generation

- Script: `fig8_appendix.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/e2_revision/summary.json
  - runs/e2_revision/boat_storyboard.png

- Note: Script filename predates later figure insertions; renders in Appendix A (\label{fig:onset}). The 20-case onset-vs-novelty/area extension (runs/g5_onset_law/summary.json) is reported as prose in \S5.1 rather than a separate figure -- a standalone scatter was tried and cost 1pp, cut in favor of prose stating the same numbers.

## Files in this folder

- `fig8_appendix.pdf`
- `fig8_appendix.py`
