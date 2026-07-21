# image-edit-lens-paper: AAAI-27 submission repository

AAAI-27 double-blind paper for a layer--time lens of diffusion image editors.
The central result is deliberately narrow: under fixed underspecified prompts,
the realized edit is predictable from early states; in the tested Qwen lineage,
an image-like code is translated to the velocity convention near L52--54.
Transplant supports sufficiency and steering supports carrier-bounded
writability. The paper does not claim irreversible commitment, fine-grained
necessity, or architecture-wide universality.

Start with [`AAAI_HANDOFF.md`](AAAI_HANDOFF.md) when taking over the project.

## Current deliverables

Validated on 2026-07-21:

| Deliverable | State |
|---|---|
| `main_aaai.pdf` | 9 pages, Letter; technical content and Conclusion end on page 7; References continue through page 9; 0 overfull, undefined refs, or Type 3 fonts |
| `supplement.pdf` | 32 pages, Letter; regenerated with the v2 main figures; 0 overfull, undefined refs, or Type 3 fonts |
| `reproducibility_checklist.pdf` | 2-page standalone checklist; upload separately from the main paper |
| `main_aaai_non_input.tex` | flattened main source, regenerated with `scripts/flatten_tex.py` |

The main paper now contains five figures and two compact result tables.
`tab:early` summarizes prediction/selection; `tab:generalize` summarizes
same-lineage translation and probe transfer.

## Repository layout

- `main_aaai.tex` and `aaai_draft/*.tex`: authoritative main-paper source.
- `supplement.tex`: authoritative supplementary source.
- `figs/<figure>/`: generated assets, plotting script when available, and
  per-figure `INFO.md` provenance.
- `OUTLINE.md`: claim and number ledger. Check it before changing results.
- `provenance.md`: figure/table data lineage and historical build notes.
- `FIGURE_REDESIGN*.md`, `TABLE_PLAN.md`: design requirements and implemented
  status for the current figure/table pass.
- `aaai_kit/AAAI27-writing-skill.md`: local summary of AAAI-27 constraints.
- `AAAI_HANDOFF.md`: operational state for a new agent.

## External data dependency

Figure scripts read preserved experiment outputs from the sibling repository:

```text
/home/ubuntu/chengyanli/image-edit-lens
```

Scripts that support relocation read `IMAGE_EDIT_LENS_ROOT`; Fig. 1 currently
uses the path above directly. No model rerun is needed for the current figures.

## Rebuild

Run from this repository root:

```bash
python figs/fig1_teaser/fig1_teaser.py
python figs/fig5_mechanism/fig5_mechanism.py
python figs/fig10_boundary/fig10_boundary.py
python figs/fig12_tuned_lens/fig12_tuned_lens.py

pdflatex main_aaai.tex && bibtex main_aaai \
  && pdflatex main_aaai.tex && pdflatex main_aaai.tex
pdflatex supplement.tex && bibtex supplement \
  && pdflatex supplement.tex && pdflatex supplement.tex
pdflatex reproducibility_checklist.tex \
  && pdflatex reproducibility_checklist.tex
python scripts/flatten_tex.py main_aaai.tex main_aaai_non_input.tex
```

## Validation

```bash
pdfinfo main_aaai.pdf | grep -E 'Pages|Page size'
pdfinfo supplement.pdf | grep -E 'Pages|Page size'
grep -c 'Overfull' main_aaai.log
grep -c 'undefined' main_aaai.log
pdffonts main_aaai.pdf | grep -c 'Type 3'
strings main_aaai.pdf | grep -icE \
  'chengyanli|image-edit-lens|flowgpt|yata|github'
```

Expected counts for the final four greps are zero. Page count alone is not
enough: visually confirm that Conclusion ends on page 7 and References begins
after it.

## Submission split and dates

- Abstract registration: 2026-07-21 AoE.
- Full paper: 2026-07-28 AoE.
- Supplementary material and code: 2026-07-31 AoE.
- Upload `main_aaai.pdf`, `supplement.pdf`, and
  `reproducibility_checklist.pdf` as separate artifacts in their designated
  fields.

Do not commit or push automatically. Before a requested push, fetch the remote,
review the diff, rebuild all deliverables, and never force-push.
