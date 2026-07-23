# Figure / table provenance

One line each: what it shows -> data source(s) -> generating script.

## Current compiled snapshot (2026-07-23, pushed paper commit `f96bf26`)

- Main PDF: 9 Letter pages; technical content and Conclusion end on page 7;
  References occupy pages 8--9.
- Supplement: 31 Letter pages. Reproducibility checklist: 2 Letter pages.
- Main figures: Fig. 1 teaser, Fig. 2 framework (only cross-column figure),
  Fig. 3 mechanism, Fig. 4 boundary, Fig. 5 tuned lens, Fig. 6 carrier crop,
  Fig. 7 differential preview.
- Main tables: Table 1 early prediction/selection; Table 2 attention-routing
  intervention audit; Table 3 cross-checkpoint translation/readout.
- The method source now contains explicit equations for the layer--time grid,
  CLIP readout, four lenses, linear probes, and three interventions. The current
  Fig. 2 PDF is an illustration asset; `fig2_method.py` is historical and does
  not reproduce it.
- Validation: zero overfull boxes, undefined references, Type 3 fonts, BibTeX
  warnings, and anonymity-string hits in the main and supplementary PDFs.
- Related Work is integrated into two Introduction paragraphs. The citation
  audit at `265a0ef` corrected or removed stale metadata; `references.bib` is
  the authoritative bibliography, not the local `allinone.md` search log.
- Current title: *Predictable Early, Translated Late: A Layer--Time Lens for
  Diffusion Image Editors*. The page-filling pass promotes routing conservation,
  rank controls, FireRed lens/preview transfer, and Rapid-AIO noise-level
  matching from the supplement without rerunning experiments.

The dated material below is an append-only historical record. Figure numbers in
old entries describe the layout at that date; use the snapshot above and each
`figs/<name>/INFO.md` for current placement.

**2026-07-16: per-figure folders are now the primary source of truth for
figure provenance.** `figs/` was restructured from a flat directory (all
image files + scripts loose together) into one subfolder per figure
(`figs/<name>/`), each containing the image file(s), the plotting script
if one is preserved, and an `INFO.md` with: intent (one-line, what the
figure demonstrates), every caption it's used under (AAAI submission /
supplement.tex, verbatim), the data sources it was built from, and --
for the figures with no preserved script (`fig12_tuned_lens`,
`fig13_transfer_onset`, `fig14_diff_lens`, `fig15_preview_lever`,
`fig16_crossmodel_lens`, `h1a_family_probes`, `h1b_steer_spectrum`,
`i1d_recompose_grid`, `i2_taxonomy_grid`) -- a note on how it was
actually produced and how to regenerate it. All `\includegraphics{figs/
NAME.ext}` references in `main_aaai.tex`/`aaai_draft/*.tex`/
`supplement.tex` were updated to `figs/NAME/NAME.ext`; recompiled 0
errors, 0 undefined refs, page counts unchanged (main_aaai.pdf 9pp,
supplement.pdf 28pp -- the 9pp is a pre-existing AAAI 7pp-body overage
from a collaborator's content edit, unrelated to this restructuring, not
yet fixed). The table below (and the v2.x notes further down) is kept
as historical narrative context; for the current, authoritative
per-figure record, read `figs/<name>/INFO.md` directly.

- **Fig. 1** (teaser, `fig:teaser`) -- source/edited images + P(red car) layer x
  time grid + five-stage editing-circuit schematic (right panel, v2.1: replaces
  the earlier two-box two-code schematic) -> `runs/wp3_car_red/{source.png,
  edited.png}`, `runs/a1_car_red/lens_grid.json` (grid) + `runs/d2_probe/
  accuracy_grid.json` (Decision box), `runs/g2_boundary/boundary_summary.json`
  (Translation box), `runs/g3_injection/summary.json` (Injection box) ->
  `paper/figs/fig1_teaser.py`
- **Fig. 2** (method diagram, `fig:method`) -- token layout / capture tap /
  depth-lens vs. time-lens / decode-then-CLIP -- illustrative diagram, no
  numeric data (conventions from `image_edit_lens/models/hooks.py`,
  `README.md`) -> `paper/figs/fig2_method.py`
- **Fig. 3** (commit-time curves, `fig:commit`) -- P(target)@L59 vs. step, 8 of
  10 battery cases -> `runs/a5_{add_boat,add_latte,bg_beach,bg_forest,
  color_car,color_cup,style_sketch,style_watercolor}/lens_grid.json` ->
  `paper/figs/fig3_commit_curves.py`
- **Fig. 4** (depth emergence, `fig:depth`) -- layer x step decode thumbnails +
  P(red car) vs. layer curves -> `runs/a1_car_red/lens_grid.json`,
  `runs/a1_car_red/contact_sheet_raw.png` -> `paper/figs/fig4_depth.py`
- **Fig. 5** (mechanism, `fig:mechanism`) -- four-variant decode row (L24/L59,
  t4) + rebuilt D2 cross-seed probe heatmap -> `runs/d1_signflip/d1_results.json`
  + `runs/d1_signflip/lens_l{24,59}_t4_{A_standard,B_signflip,C_v_as_x0,
  D_neg_v_as_x0}.png`, `runs/d2_probe/accuracy_grid.json` ->
  `paper/figs/fig5_mechanism.py`
- **Fig. 6** (dense boundary sweep, `fig:boundary`, v2.1 new) -- A/C decode
  crossover, cos($v_\ell$,$v_{59}$), and dense cross-seed probe accuracy, all
  vs. layer (L44-59, t=4/16) -> `runs/g2_boundary/boundary_summary.json`
  (also cross-checked against `sweep.json` and `dense_probe_accuracy.json`,
  same numbers) -> `paper/figs/fig10_boundary.py` (script kept its build-order
  name; renders as Figure 6, in §5.3)
- **Table 2** (`tab:injection`, v2.1 new) -- text-stream (encoder_hidden_states)
  zero-ablation by layer band, car_red -> `runs/g3_injection/summary.json`
  (hand-transcribed into `main.tex`, no separate script)
- **Fig. 7** (causality, `fig:causal`) -- layer-band ablation (A), step-window
  ablation (B), transplant (C) -> `runs/a3_summary.json` (layerwindow +
  stepwindow scans), `runs/a4_summary.json` -> `paper/figs/fig6_causality.py`
  (script name predates later insertions; renders as Figure 7)
- **Table 3** (`tab:condtok`) -- condition-token ablation, car\_red ->
  `runs/a3_summary.json` (`condtokens` scan; hand-transcribed into
  `main.tex`, no separate script)
- **Fig. 8** (steering dose-response, `fig:steer`) -- P(red)/P(green) vs.
  steer strength alpha, random-dir and negated-dir controls ->
  `runs/g1_steer/summary.json` -> `paper/figs/fig9_steering.py` (script kept
  its build-order name; renders as Figure 8, in §5.7 after transplant)
- **Fig. 9** (applications, `fig:apps`) -- decision-saliency comparison,
  step-budget prediction, mid-stack rescue -> `runs/e1_saliency/summary.json`
  (+ `saliency_L12_t4.png`, `red_edited_reference.png`),
  `runs/e3_earlyexit/summary.json`, `runs/e3_rescue/summary.json` ->
  `paper/figs/fig7_applications.py` (script name predates later insertions;
  renders as Figure 9)
- **Fig. 10** (cross-model replication, `fig:replication`, v2.1 new) -- A/C
  crossover layer across Qwen-Image-Edit-2511 / FireRed-Image-Edit-1.1 /
  Rapid-AIO (A), layer-band ablation edit success Qwen vs. FireRed (B) ->
  `runs/g4_summary.json` -> `paper/figs/fig11_replication.py` (renders as
  Figure 10, in new §5.10 "Does this generalize?")
- **Fig. 11** (appendix self-correction, `fig:onset`) -- IoU-vs-final onset
  curves + add-boat storyboard -> `runs/e2_revision/summary.json`,
  `runs/e2_revision/boat_storyboard.png` -> `paper/figs/fig8_appendix.py`
  (script name predates later insertions; renders as Figure 11, in
  Appendix A). The 20-case onset-vs-novelty/area extension (`runs/
  g5_onset_law/summary.json`) is reported as prose + exact numbers in the
  revised §5.1 rather than as a separate figure: a standalone scatter-plot
  figure was tried and pushed the paper to 14pp, so it was cut in favor of
  §5.1's prose, which states the same rho/p values and case-level numbers
  exactly.
- **Table 1** (`tab:battery`) -- commit step / first readable layer, all 10
  battery cases -> `runs/a5_aggregate.json` (hand-transcribed into
  `main.tex`, no separate script)

## Numbers cited in prose but not tied to a specific figure/table

- bf16 necessity, absmax ~3e9, mean |x| ~1e5-1e7, fp16 overflow 80-98%:
  `image_edit_lens/models/hooks.py` docstring.
- Depth-lens self-consistency gate (raw vs. rescaled, `max_rel_diff=0`,
  max pixel diff 11/255, max CLIP diff 0.038): `runs/a1_car_red/lens_grid.json`
  (`self_consistency_gate`, `max_raw_vs_rescale_pixel_diff`,
  `max_raw_vs_rescale_clip_diff`).
- Spatial-locality ratio ("in/out 26x") and massive-activation channel index
  (~ch673) and L59 absmax (~2.6e9): reported in `paper/OUTLINE.md` (C3, C5)
  from WP4/WP5 exploration; the underlying stdout logs were not retained on
  disk at paper-writing time, so these are cited as previously-verified
  facts per OUTLINE.md rather than re-derived from a JSON in this pass.
- Reproducibility / runtime numbers (Appendix A): `runs/*/summary.json`
  `load_time_s`/`peak_vram_gib` fields across `a3`, `a4`, `d1`, `d2`, `e1`,
  `e3_earlyexit`, `e3_rescue`; `experiments/README.md` (~11s load, ~27s
  denoising, 57.93 GiB peak, no capture hooks).
- Cross-model replication numbers (§5.10, `sec:generalize`): all from
  `runs/g4_summary.json` (`findings` list F1-F5 + `transfer` block); the
  zero_cond_t / self-consistency-gate note for FireRed and Rapid-AIO is
  `g4_summary.json`'s own `zero_cond_t_note` field, quoted near-verbatim.
- 20-case onset-vs-novelty/area extension (§5.1): all from
  `runs/g5_onset_law/summary.json` (`spearman_onset_vs_novelty`,
  `spearman_onset_vs_area`, per-case `onset_step`/`final_area_frac`
  fields); cross-checked against the human-readable `runs/g5_onset_law/
  table.md`.

## K7/K8/K9 figures added (2026-07-14), then redrawn from source data (2026-07-14)

Prose/numbers for K7 (C26, sigma-keying law), K8 (C27, terminal-step
collapse decomposition), and K9 (C28, nested learning curve) were
backfilled into `main.tex`/`supplement.tex` \S\ref{sec:generalize} on
an earlier pass, but the actual result plots generated in `runs/`
were never copied into `paper/figs/` or wired up via
`\includegraphics` -- these three subsections had numbers but no
figure. First fix pass added the raw `runs/` PNGs verbatim (no
plotting script, same as the fig12-fig16/K1-K6 convention); a same-day
follow-up pass replaced all three with purpose-built figures generated
directly from each run's `summary.json`/`cells/`, styled to match this
paper's house convention (`RED`/`TEAL`/`GRAY_D` palette, matplotlib
default sans-serif, panel-label letters baked into the raster --
see `fig11_replication.py`/`fig4_depth.py` for the house style this
follows). Each is now a single combined image (no LaTeX `subfigure`
split), directly after its paragraph (before the next
`\textbf{...}` paragraph / before `\subsection{Across edit
families...}` for K9):

- **Figure 16** (`fig:k7ladder`) -- `paper/figs/fig17_k7_ladder.py`.
  Image-plate + quant archetype: 3-rung (L0 frozen / L1 recal. / L2
  native-refit) x 4-step (t0-t3) decode grid at L52, car_red (a) and
  style_ink (b), rebuilt from the per-cell PNGs in
  `runs/k7_rapid_ladder/cells/` (not the pre-assembled contact-sheet
  PNGs) with each cell's held-out $R^2$ from `summary.json`
  (`cases.{case}.test_r2`) annotated in-frame and the coverage-edge
  t3 column outlined in red -> `paper/figs/fig17_k7_ladder.{png,jpg}`.
- **Figure 17** (`fig:k8decompose`) -- `paper/figs/fig18_k8_decompose.py`.
  Quantitative-grid archetype: Q1 dose-response (a) and Q2 native
  held-out collapse (b), redrawn from `runs/k8_sigma_coverage/
  summary.json` (`t3_scoring_table`, `q2_native_heldout_r2`) with a
  car_red/style_ink x L52/L56/L59 color+marker encoding (tonal
  red/teal families) shared across both panels via one figure-level
  legend -> `paper/figs/fig18_k8_decompose.{png,jpg}`.
- **Figure 18** (`fig:k9curve`) -- `paper/figs/fig19_k9_curve.py`.
  Quantitative-grid archetype: nested learning curve with train-val
  ceiling band (a) and a two-mini-panel composition-swap bar check
  (b, hatch-encoded case order), redrawn from `runs/k9_capacity_curve/
  summary.json` (`results_per_config.*.held_out_r2`/`train_val_r2`)
  -> `paper/figs/fig19_k9_curve.{png,jpg}`.

`main.tex` uses the `.png` originals; `supplement.tex` uses `.jpg`
(PIL `quality=88`, same convention as the other late-added figures).
main.pdf 26pp -> 27pp (raw-PNG pass) -> 28pp (redrawn pass);
supplement.pdf 26pp -> 28pp -> 28pp (bibtex+2x pdflatex each pass, 0
errors, 0 undefined refs, anonymity byte-grep on supplement.pdf still
0 hits). Not touched: `main_aaai.tex` (AAAI 8pp submission does not
cover K7-K9 at all, per `AAAI_SPINE.md`).

## v2.1 revision note

This revision folds in four experiment batches that landed after v2's final
compile (previously tracked in this file as the "G-phase note", now resolved):
`runs/g2_boundary/` (dense L44-59 boundary sweep, now Fig. 6/§5.3),
`runs/g3_injection/` (text-stream injection ablation, now Table 2/§5.4, and
the Injection/Decision boxes of Fig. 1's circuit panel), `runs/g4_summary.json`
(cross-model replication, now Fig. 10/§5.10), and `runs/g5_onset_law/`
(20-case onset-timing extension, now folded into the revised §5.1, which
softens the original 10-case "layout-novelty gradient" reading to the
honest categorical finding). No G-phase data remains unincorporated.

## Figure 11 (figs/h1a_family_probes.png) — v2.2
- Source: verbatim copy of `runs/h1a/family_probe_heatmaps.png` (generated by `experiments/h1a_probe.py`, 2026-07-09).
- Data: cross-seed 3-class probe accuracy per family, 5 layers (L6/12/36/53/59) × 3 steps (t0/4/16); train seed 0 / test seed 1. NOTE: `runs/h1a/probe_grids.json` has an empty `families` dict (save bug); the annotated numbers on the PNG are the ground truth, cross-checked manually against the boundary/steer analyses.
- Boundary numbers quoted in §families text: recomputed 2026-07-09 from `runs/h1a/boundary_by_family.json` via linear interpolation of the A−C CLIP margin (style 53.0/53.1, background 52.1@t16, removal/addition nominal 53.4–55.9 with margins too small to localize).

## Figure 12 (figs/h1b_steer_spectrum.png) — v2.2
- Generated by `experiments/h1b_spectrum_fig.py` from `runs/h1b_steer/summary.json` + `runs/h1b_steer/visual_verdicts.json`; steered images from `experiments/h1b_steer.py` (13 GPU runs, 2026-07-09); color row from `runs/g1_steer/summary.json` (alpha_2 vs control_no_steer).
- Verdict badges = human visual inspection of every output vs its H1a neutral baseline (rationale logged: CLIP forced-choice/region readouts cannot distinguish clean edits from flat-patch overwrites — this audit is what downgraded G1's color "flip" to crude and triggered the §steer self-correction paragraph).

## v2.3 revision (§recompose, §cfgfreelunch) — 2026-07-09

New subsection `\subsection{Recomposing edits in place: masks are the carrier}`
(`sec:recompose`, after §families) and `\subsection{A mechanism-derived free
lunch: truncating classifier-free guidance}` (`sec:cfgfreelunch`), plus
abstract/contributions/conclusion/limitations edits. All numbers transcribed
directly from the `summary.json` + `visual_verdicts.json` pairs below; no
number in this revision comes from OUTLINE.md prose alone.

- **Erasure separability + write self-cancellation** (rank-2 QR strip,
  $1.2\%$ row norm, F0/F1 desaturation and push-fails-to-redden numbers):
  `runs/i1_recompose/summary.json` (`F0_strip_only`, `F1_strip_plus_red_a1/a2`
  results + `qr_basis`), `runs/i1_recompose/visual_verdicts.json`.
- **Rank-1 strip-only reproduction** (in-diff $14.9$): `runs/i1b_write_fix/
  summary.json` (`R1_rank1_strip_only`), `.../visual_verdicts.json`.
- **Clamp fix, $\alpha{=}8$ clean recolor, $\alpha{=}16$ overdose, matched-dose
  push flood**: `runs/i1b_write_fix/summary.json` (`C8_clamp_a8`,
  `C16_clamp_a16`, `S1_striponce_push_a1/a2`), `.../visual_verdicts.json`
  (`CLEAN_RECOLOR_SUCCESS` verdict text, incl. the "CLIP fails in reverse"
  note quoted near-verbatim in the CLIP-failure-mode-iv limitation).
- **Dose ladder ($\alpha$=4/6/8/10/12), bbox-shaped overshoot, direction-
  dependent gain (FLIP red→green), matched-dose push control**:
  `runs/i1c_dose_window/summary.json` + `.../visual_verdicts.json`
  (`dose_window_law_v2`, `C4/C6/C10/C12_clamp_a*`, `FLIP_red2green_a8`,
  `P8_push_a8_control`).
- **Silhouette-mask perfect recolor at every dose/semantics** (n=371 of 792
  in-bbox patches, out-diff $0.46$–$0.57$): `runs/i1d_silhouette/summary.json`
  + `.../visual_verdicts.json` (`membership_law_CONFIRMED`, `law_v3_final` —
  this is the source of the "carrier is the spatial support you steer" /
  "G1/H1b steering failures were mask failures" claim and the paper's fourth
  self-correction).
- **Direction taxonomy (boat/swan/random/swap on the 61-patch lake hull)**:
  `runs/i2_mask_synthesis/summary.json` + `.../visual_verdicts.json` (shallow
  L6–23, `BOAT_*`/`SWAN_clamp_a8`/`RAND_clamp_a8`), `runs/
  i2b_mask_synthesis_deep/summary.json` + `.../visual_verdicts.json` (deep
  L24–47 retest, `depth_excuse_removed`, `taxonomy_law`), `runs/
  i2c_swap_control/summary.json` + `.../visual_verdicts.json` (donor-boat
  transplant, `SWAP_L0_23/L24_47/L0_47`, `taxonomy_law_COMPLETE`,
  `family_depth_confirmed`). Table 4 (`tab:taxonomy`) and Figure 13
  (`figs/i1d_recompose_grid/` + `figs/i2_taxonomy_grid/`, combined as two
  subfigures) were originally **placeholders** at v2.3 write time: the PNGs
  were generator-script boxes stating what was to be rendered
  (`/tmp/.../scratchpad/make_placeholders.py`, since deleted), not the
  actual `intervened.png` grids. **Superseded 2026-07-14** (confirmed
  during the K7/K8/K9 provenance audit): both are now real image grids
  assembled from the `runs/i1*`/`runs/i2*` directories listed above — see
  `figs/i1d_recompose_grid/INFO.md` / `figs/i2_taxonomy_grid/INFO.md` for
  the current record. This paragraph is left as historical context for why
  the caption cites so many `runs/` subdirectories.
- **CFG truncation (`cfg_until`=4/8 vs full)**: `runs/x1_cfg_truncation/
  summary.json` (`nfe_note`: full=40, cfg4=24/40% saving, cfg8=28/30%
  saving; per-case `wall_time_s`, `diff_vs_full`, `target_score`) +
  `.../visual_verdicts.json` (`law_update`, add\_boat identity-drift note).
- **CFG floor (`cfg_until`=2/0)**: `runs/x1b_cfg_floor/summary.json`
  (45% NFE saving at cfg_until=2 computed as $22/40$; $2.0\times$ speedup at
  cfg_until=0 from `color_car` wall times $9.66$s vs.\ x1's $19.33$s full) +
  `.../visual_verdicts.json` (`cfg_law_final`, `bg_beach_cfg0`
  `HALF_synthesis_without_erase` verdict — source of the "erase-without-
  synthesis / synthesize-without-erase" complementarity framing).
  `runs/x1c_cfg2_battery/` (20-case generalization check) has no
  `summary.json`/`visual_verdicts.json` yet at write time — mentioned in
  prose as "in progress" with no numbers cited, per instruction not to
  invent battery figures.
- **CLIP failure-mode (iv), under-scoring a genuine success**: same
  `runs/i1b_write_fix/visual_verdicts.json` `C8_clamp_a8` entry as above
  (haze causes $P(\text{red})=0.091$ despite a visually clean red car); the
  paired overshoot mis-scoring ($0.70$–$0.84$ for a fake patch) is from
  `runs/i1c_dose_window/visual_verdicts.json` (`C10_clamp_a10`,
  `C12_clamp_a12`).
- Placement note: a `\FloatBarrier` (package `placeins`) was added before
  `sec:recompose` to keep §families' own floats (Fig. 10/11/12) from
  drifting into the new subsections' pages; this changed pagination but no
  numbers. Two placeholder figures were merged into one `figure` float with
  two `subcaption` panels (rather than two separate figures) purely to fit
  the page-count constraint (v2.2 was 15pp; this revision is 17pp, within
  the requested ≤2pp increase) — content is unaffected, only float layout.

## Sentence-level clarity pass (2026-07-14)

Applied the `research-paper-writing` skill (methodology from
github.com/Master-cai/Research-Paper-Writing-Skills, based on Peng Sida's
`learning_research` notes) as a prose-only polish pass over `main.tex`,
propagated identically to `supplement.tex`. Scope was restricted to
**sentence boundaries only** — no claim, number, or citation was added,
removed, or reworded; every edit was a pure split/re-punctuation of an
existing long/compound sentence into two or more shorter ones.

- First batch (interactive, user-confirmed): Abstract's "Translated late"
  sentence (one ~115-word sentence carrying both the L52-54 boundary claim
  and the depth-non-universality caveat) split into three; a matching
  Introduction/Contributions split.
- Second batch (user confirmed to continue across the whole paper): a
  programmatic long-sentence scan (regex over `.`-delimited spans, sorted
  by word count) was used to prioritize genuine run-ons rather than manually
  re-reading all 28pp; surgical splits applied across §depth, §tunedlens,
  §previewlever, §swap, §steer, §massive, §generalize (cross-model),
  §families, §recompose, §injection, Limitations, and Conclusion. ~23
  sentence-splits total across both batches.
- Third batch (final review pass, same request): re-ran the long-sentence
  scan against the then-current `main.tex`, cross-read the
  previously-unreviewed Method (`§capture`/`§timelens`/`§depthlens`/
  `§readout`/`§interventions`/`§protocol`) and Experiments (`§injection`/
  `§causal`/`§applications`/`§cfgfreelunch`) sections by hand. Found one
  genuine 91-word run-on in `§injection` (the "Cutting text access at
  L0--11 or at L24--35 is destructive in a qualitatively different way..."
  sentence, which fused the L0-11-destructive-mode claim with the
  $P(\text{red})=0.321$ evidence into a single clause) and split it in two;
  everything else in those sections was judged already clause-clean and
  left untouched, as was a terminology-consistency grep spot-check
  (no inconsistent term usage found).
- Verification after each batch: full `pdflatex`+`bibtex`+`pdflatex`x2
  recompile of both `main.tex` and `supplement.tex` (0 errors, 0 undefined
  refs/cites, 0 new overfull hboxes each time), plus the standard anonymity
  byte-grep on `supplement.pdf` (`chengyanli|image-edit-lens|flowgpt|yata|
  github`, 0 hits throughout). Page count unaffected by this pass — both
  PDFs stayed at 28pp (the count set by the K7/K8/K9 redraw above); the
  polish pass only ever changed sentence boundaries, never total wordcount
  enough to shift pagination.
- Not touched: `main_aaai.tex` (AAAI 8pp submission has its own separate
  prose in `aaai_draft/*.tex`, out of scope for this pass).

## Reproducibility checklist decoupled from main_aaai.pdf (2026-07-14)

Found and fixed a real compliance bug (user-flagged, verified against the
official `/home/ubuntu/chengyanli/AuthorKit27.zip`): `main_aaai.tex` had
`\input{repro_checklist_filled}` right before `\end{document}`, merging the
reproducibility checklist into the same PDF as the main paper (9pp total =
7pp body + refs/checklist crammed onto pages 8-9). The AuthorKit's own
`AAAI27-writing-skill.md` states the checklist "不计入正文页数，单独上传"
(does not count toward the body limit, uploaded **separately**) for AAAI-27
specifically -- the official `ReproducibilityChecklist.tex` template does
support an embedded `\input` mode (via an `isChecklistMainFile` guard), but
that mode is opt-in per-conference and AAAI-27's own instructions call for
a standalone submission, not embedding.

Fix: removed the `\input{repro_checklist_filled}` line from `main_aaai.tex`
(now 8pp: 7pp body + 1pp references, 0 errors, 0 undefined refs, anonymity
byte-grep 0 hits). Replaced `repro_checklist_filled.tex` (a hand-stripped
fragment) with `reproducibility_checklist.tex` -- the official
`ReproducibilityChecklist.tex` copied verbatim, with only the 31 real
"Type your response here" answer placeholders substituted (the other 3
occurrences of that phrase, in the template's own instructions text, were
left untouched) -- compiled standalone (`pdflatex` x2, no bibtex, no
citations) into its own `reproducibility_checklist.pdf` (2pp, matching the
official example `ReproducibilityChecklist.pdf`'s page count exactly;
anonymity byte-grep 0 hits). Also verified in the same pass: `aaai2027.sty`
and `aaai2027.bst` are byte-identical (md5sum) to the copies in
`AuthorKit27.zip` -- not modified/hallucinated, no replacement needed;
the `\twocolumn` layout was rendering correctly all along (checked via
`pdftoppm` page-1 render), so the only real defect was the checklist
merge, not the template files themselves.

## Per-figure folder restructuring (2026-07-16)

`figs/` was flat (23 figures' worth of `.pdf`/`.png`/`.jpg`/`.py` files all
loose in one directory) with no per-image record of intent or provenance
beyond this file's terse one-liners -- and several figures (the K1/K6
family: `fig12_tuned_lens`, `fig13_transfer_onset`, `fig14_diff_lens`,
`fig15_preview_lever`, `fig16_crossmodel_lens`, plus `h1a_family_probes`,
`h1b_steer_spectrum`) had no entry here at all, or only an entry with no
generation script. Restructured into `figs/<name>/` per figure, each
holding the image file(s), the `.py` script if one exists, and an
`INFO.md` (intent, every caption the figure is used under verbatim, data
sources, and a regeneration note for the ~9 script-less figures --
including tracing `fig14_diff_lens.png` to a byte-identical md5 match
against `runs/k3b_diff_lens_colorcases/color_eyes_strip.png`, and pointing
the others at their likely `runs/` source folders since no exact-match
compositing script survives). All 23 `\includegraphics{figs/NAME.ext}`
call sites across `main_aaai.tex`, `aaai_draft/*.tex` (7 references), and
`supplement.tex` (23 references) were rewritten to
`figs/NAME/NAME.ext`; full clean recompile of both documents (0 errors, 0
undefined refs) confirmed the new paths resolve and pages render
correctly (spot-checked via `pdftoppm`). Page counts unchanged:
main_aaai.pdf 9pp (unrelated pre-existing overage, see next paragraph),
supplement.pdf 28pp. Also used this pass to correct two stale notes above:
the i1d/i2 "placeholder" warning (superseded 2026-07-14, text hadn't been
updated) and this file's own top note pointing future readers at
`figs/<name>/INFO.md` as the current source of truth rather than this
table.

**Known open issue, not fixed by this pass**: `main_aaai.pdf` is
currently 9pp (8pp body + 1pp refs), one page over the AAAI-27 7pp-body
limit verified compliant on 2026-07-14 (8pp = 7+1). Root cause: a
collaborator's edit expanded `aaai_draft/20_experiments.tex` (merged 5
old result subsections into one 370-line file) after that verification.
Not touched here -- deciding what to cut is an editorial call, not a
provenance-tooling one.

**Side fix, mechanical not editorial**: doing a truly clean rebuild (full
delete of `.aux/.bbl/.blg/.log` before `pdflatex`+`bibtex`+`pdflatex`x2,
rather than reusing whatever was already on disk) for this restructuring
surfaced that `supplement.tex` \S\ref{sec:related} cites
`ho2020ddpm,song2021ddim,rombach2022ldm` (line ~327, the "Diffusion
models are most commonly studied through their sampling process..."
sentence) but all three keys were missing from `references.bib` --
`bibtex` silently dropped them and `pdflatex` reported "Citation ...
undefined" (this had been masked because the previously-committed
`supplement.bbl` was stale: it still had all 3 formatted entries from
before they were removed from `references.bib`, so anyone reusing that
`.bbl` instead of rebuilding it from scratch would never see the break).
Root cause: the collaborator's `references.bib` restructuring (git commit
`aa1fffa`, net -22 lines) dropped these 3 entries while trimming/
deduplicating, without touching `supplement.tex` (only `main_aaai.tex`/
`aaai_draft/` were edited that commit) or regenerating `supplement.bbl`
to catch the break. Restored verbatim from the pre-restructuring
`references.bib` (git commit `87d6b75`) -- same title/author/venue/year/
eprint fields, nothing invented. Recompiled both `main_aaai.pdf` (9pp,
unaffected -- doesn't cite these 3 keys) and `supplement.pdf` (28pp): 0
errors, 0 undefined refs/cites, anonymity byte-grep 0 hits on both.
Treated as a mechanical repair (restoring a dropped, verifiable,
standard citation) rather than an editorial call, unlike the 9pp overage
above -- flagging here in case the collaborator meant to drop the
sentence rather than just the bib entries.

## T11 attention-routing conservation audit (2026-07-19)

Added `figs/fig20_attention_conservation/` for the preregistered T11 audit.
The figure is regenerated by `fig20_attention_conservation.py` from
`runs/t11_attention_conservation/detailed_analysis.json` in the adjacent code
repository (or the path named by `IMAGE_EDIT_LENS_ROOT`). Panel A reports the
registered five-seed condition statistic; panels B--C are explicitly post-hoc
query-group and layer decompositions. The embedded PDF uses TrueType fonts and
has zero Type 3 entries.

The supplement text and caption are grounded in:

- `runs/t11_attention_conservation/analysis.json` for the registered
  destructive-minus-on-manifold contrast (5/5 positive, mean 0.0355812,
  exact one-sided sign-flip p=0.03125);
- `runs/t11_attention_conservation/detailed_analysis.json` for condition means
  and the post-hoc geometry separation;
- `runs/t11_attention_conservation/vqa_results.json` and
  `blind_geometry_verdicts.json` for the 40/40 agreement audit;
- `experiments/AAAI_T11_ATTENTION_CONSERVATION_UPDATE.md` for integrity checks
  and claim boundaries.

The figure and prose support only the tested Qwen car-setting explanation that
content-matched transplant conserves natural-reference routing and geometry,
whereas destructive/content-mismatched replacement and geometry-breaking
steering do not. They do not claim token reduction, speedup, causal necessity,
architecture universality, or transfer of RESTORE calibration.

The registered scalar result and controls are also summarized without a figure
in the seven-page main paper's final experiments page. The full decomposition
remains supplementary. A 2026 nearest-neighbor pass additionally added direct
positioning against Breaking the Lock-in, DreamReader, Look But Don't Touch,
multiple-mediator patching, Concept Spaces, and the ICLR massive-activation
study; no visual data were changed by that citation/claim audit.

## Main-figure v2 and compact summary tables (2026-07-21)

Applied `FIGURE_REDESIGN_v2.md` to the four main-paper figures. All panel or row
titles are centered over their own content regions; Fig. 1 now maps the dense
L52--54 translation interval into the coarse heatmap by interpolating physical
layer values rather than highlighting the full L54 row; Fig. 5 leaves 0.05
headroom above the maximum probe accuracy. All four scripts resolve fonts in
the order Source Sans 3, Arimo, Arial/Helvetica, DejaVu Sans and print the
selected family; the current build selected Arimo and embeds CID TrueType fonts.

Added two booktabs tables to `aaai_draft/20_experiments.tex`: `tab:early`
summarizes fixed-prompt prediction, continuous hue, and held-out selection;
`tab:generalize` summarizes same-lineage translation bands, early-to-terminal
probe behavior, and cross-checkpoint transfer. Every value was transcribed from
the pre-existing main text, supplement, and `OUTLINE.md`; no experiment was
rerun and no result was inferred. The mechanism, boundary, and tuned-lens floats
were moved from the Setup block to the same or adjacent page as first use.

Final build state for this pass: `main_aaai.pdf` 9 pages with technical content
ending on page 7 and references continuing through page 9; `supplement.pdf` 32
pages; standalone `reproducibility_checklist.pdf` 2 pages. Main and supplement
have zero overfull boxes, undefined references, and Type 3 fonts. The checklist
remains a separate upload and is no longer input into `main_aaai.tex`.

## Main-paper single-column layout and evidence promotion (2026-07-21)

Converted every main-paper figure except the layer--time method framework to a
single-column float. Promoted two load-bearing supplementary visuals into the
main paper without rerunning experiments: a four-panel crop of
`i1d_recompose_grid.jpg` for the carrier-bound writability claim, and
`fig15_preview_lever.jpg` for the differential preview at 15% NFE. The full
dose ladders, batteries, and diagnostic chains remain supplementary.

The rebuilt `main_aaai.pdf` is 8 pages: technical content and Conclusion end on
page 7, and References continue through page 8. Validation reports zero
overfull boxes, undefined references, and Type 3 fonts. Visual inspection
covered all seven figures at page scale; only the method framework spans both
columns.
