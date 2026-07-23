# AAAI-27 handoff: start here

This file is the self-contained entry point for an agent with no conversation
history. Last updated 2026-07-22.

## 1. Current state

Repository:

```text
/home/ubuntu/chengyanli/image-edit-lens-paper-t3-review
remote: https://github.com/jackeyloveseven/image-edit-lens-paper.git
branch: main
remote baseline before this documentation pass: 5f917cb
```

Commit `5f917cb` is pushed to `origin/main`. The working tree for this pass
contains documentation synchronization only (and may include regenerated PDFs
after validation); do not discard it before reviewing the scoped diff.

Validated deliverables:

| File | Validation |
|---|---|
| `main_aaai.pdf` | 8 pages; all technical content including Conclusion ends on page 7; References occupy the remaining space through page 8; Letter; 0 overfull / undefined / Type 3 |
| `supplement.pdf` | 31 pages; Letter; 0 overfull / undefined / Type 3 |
| `reproducibility_checklist.pdf` | 2 pages; standalone upload |
| `main_aaai_non_input.tex` | flattened copy generated from the authoritative modular source |

AAAI-27 permits 7 technical pages plus at most 2 reference pages in the main
PDF. The reproducibility checklist is a separate OpenReview upload and must not
be `\input` into `main_aaai.tex`.

## 2. Current implementation and recent changes

### Figures

Updated these scripts and regenerated their assets:

- `figs/fig1_teaser/fig1_teaser.py`
- `figs/fig5_mechanism/fig5_mechanism.py`
- `figs/fig10_boundary/fig10_boundary.py`
- `figs/fig12_tuned_lens/fig12_tuned_lens.py`

Implemented behavior:

- Every panel/row title is centered over its own content region.
- Fig. 1 maps L52--54 into the coarse heatmap using physical-layer
  interpolation instead of highlighting the entire L54 row.
- All micro-labels are at least 7 pt.
- Fig. 4-C leaves 0.05 headroom above the observed maximum.
- Font lookup order is Source Sans 3, Arimo, Arial/Helvetica, DejaVu Sans.
  Current builds resolve to Arimo and embed TrueType fonts.

### Main paper

`aaai_draft/20_experiments.tex` now contains:

- `tab:early`: fixed-prompt prediction, continuous hue, and best-of-five
  selection across Qwen and Boogu.
- `tab:generalize`: same-lineage A/C bands, early-to-terminal probe behavior,
  and Qwen/FireRed transfer.
- Mechanism, boundary, and tuned-lens floats placed beside or one page from
  their first discussion, instead of being grouped after Setup.
- All main-paper figures use single-column layout except the layer--time method
  framework, which remains cross-column.
- Added compact carrier-mask evidence and the 15\%-NFE differential preview
  from the supplement, directly supporting writability and practical use.
- Shortened prose and captions to keep Conclusion on page 7.

Figure numbering in the main paper is now fixed as: Fig. 1 teaser, Fig. 2
framework, Fig. 3 mechanism, Fig. 4 boundary, Fig. 5 tuned lens, Fig. 6
carrier, and Fig. 7 differential preview. Only Fig. 2 spans both columns.

### Method formalization

The latest method pass adds explicit definitions for the layer--time score
grid, crop-level CLIP readout, time/depth/tuned/differential lenses, linear
probes, and ablate/transplant/steer interventions in
`aaai_draft/10_method.tex`. The revised Fig. 2 summarizes the same pipeline.

No experiment was rerun. Table values were cross-checked against existing prose,
`OUTLINE.md`, and `supplement.tex`.

### Build and documentation

- Removed `\input{reproducibility_checklist}` from `main_aaai.tex`.
- Added `scripts/flatten_tex.py` to regenerate `main_aaai_non_input.tex`.
- Updated per-figure `INFO.md`, `provenance.md`, `AAAI_SPINE.md`, design plans,
  README, and the local AAAI rule summary.
- Rebuilt `supplement.pdf` after the revised Fig. 2/caption landed, keeping the
  current source and 32-page artifact synchronized.

## 3. Sources of truth

Use this precedence order:

1. Official AAAI-27 instructions and Author Kit for submission rules.
2. `OUTLINE.md` for claim wording and exact experimental numbers.
3. `aaai_draft/*.tex` and `main_aaai.tex` for the main paper.
4. `supplement.tex` for extended evidence.
5. `figs/<name>/INFO.md` and `provenance.md` for asset lineage.
6. `FIGURE_REDESIGN_v2.md` and `TABLE_PLAN.md` for this pass's acceptance
   criteria.

Do not use `main_aaai_non_input.tex` as an editing source. It is generated.

## 4. Data and environment

The plotting scripts consume preserved outputs from:

```text
/home/ubuntu/chengyanli/image-edit-lens/runs/
```

Most scripts infer the sibling repository or accept `IMAGE_EDIT_LENS_ROOT`.
Fig. 1 currently uses `/home/ubuntu/chengyanli/image-edit-lens` directly.
Required files were verified present on 2026-07-22. The update does not require
GPU work, model loading, or new experiments.

Never terminate unfamiliar GPU/model processes. Do not modify the sibling data
repository while editing the paper.

## 5. Rebuild from scratch

From the paper repository root:

```bash
python figs/fig1_teaser/fig1_teaser.py
python figs/fig5_mechanism/fig5_mechanism.py
python figs/fig10_boundary/fig10_boundary.py
python figs/fig12_tuned_lens/fig12_tuned_lens.py

pdflatex main_aaai.tex
bibtex main_aaai
pdflatex main_aaai.tex
pdflatex main_aaai.tex

pdflatex supplement.tex
bibtex supplement
pdflatex supplement.tex
pdflatex supplement.tex

pdflatex reproducibility_checklist.tex
pdflatex reproducibility_checklist.tex

python scripts/flatten_tex.py main_aaai.tex main_aaai_non_input.tex
```

The checklist template emits a longstanding standalone `\iftrue` warning while
still producing the expected 2-page PDF. Treat new hard errors, undefined
references, overfull boxes, or changed page counts as regressions.

## 6. Acceptance checks

Run:

```bash
pdfinfo main_aaai.pdf | grep -E 'Pages|Page size'
pdfinfo supplement.pdf | grep -E 'Pages|Page size'
pdfinfo reproducibility_checklist.pdf | grep -E 'Pages|Page size'
grep -c 'Overfull' main_aaai.log
grep -c 'undefined' main_aaai.log
grep -c 'Overfull' supplement.log
grep -c 'undefined' supplement.log
pdffonts main_aaai.pdf | grep -c 'Type 3'
pdffonts supplement.pdf | grep -c 'Type 3'
strings main_aaai.pdf supplement.pdf reproducibility_checklist.pdf \
  | grep -icE 'chengyanli|image-edit-lens|flowgpt|yata|github'
```

Expected:

- Main 8 pages, supplement 31, checklist 2, all Letter.
- All count checks above return zero.
- Page 7 visibly contains the end of Limitations, all of Conclusion, then the
  start of References.
- Fig. 3 is adjacent to the early-probe discussion; Figs. 4 and 5 are on the
  same page as the translation/tuned-lens discussion; the carrier and preview
  figures are adjacent to their claims; Table 2 is one page from Generalization.

## 7. Scientific boundaries

Allowed claims:

- The realized outcome is predictable early in the tested fixed-prompt tasks.
- Qwen-lineage checkpoints show an L52--54-neighborhood translation from an
  image-like code to the velocity convention.
- Boogu independently supports early outcome prediction and selection.
- Transplant establishes tested sufficiency.
- Steering demonstrates carrier-bounded writability.
- CFG truncation and best-of-five selection are tested existence proofs.

Do not claim:

- Irreversible early commitment.
- Fine-grained causal necessity from destructive ablation.
- A universal translation boundary for unrelated architectures.
- Boogu replication of Qwen's translation or terminal probe drop.
- That a readable linear direction is generally writable without a spatial
  carrier.

## 8. Git and next action

The last pushed paper commit is `5f917cb`. This documentation synchronization
is a new local pass. Before its next push:

1. Run `git fetch origin` and verify the remote has not advanced.
2. Review `git diff --check` and the full scoped diff.
3. Rebuild and rerun every acceptance check above.
4. Commit with a concise message describing figures, tables, and submission
   docs.
5. Push normally; never force-push.

Do not place credentials in remotes, files, command history, or documentation.
