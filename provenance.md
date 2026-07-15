# Figure / table provenance

One line each: what it shows -> data source(s) -> generating script.

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
  (`figs/i1d_recompose_grid.png` + `figs/i2_taxonomy_grid.png`, combined as
  two subfigures) are **placeholders**: the PNGs are generator-script boxes
  stating what is to be rendered (`/tmp/.../scratchpad/make_placeholders.py`
  at write time), not the actual `intervened.png` grids — a follow-up pass
  must replace them with real image grids assembled from the `runs/i1*` and
  `runs/i2*` directories listed in the caption/table.
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
