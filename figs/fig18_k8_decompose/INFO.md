# fig18_k8_decompose

## Intent

Decomposing K7's terminal-step collapse (K8): (a) Q1 dose-response as borrowed-dictionary sigma approaches the terminal value -- a coverage gap, not a transfer breakdown; (b) Q2 native held-out collapse at the same terminal step -- a model-independent decodability loss.

## Used in

- supplement.tex

Current placement: supplement Figure 18.

## Target caption

### supplement.tex

\textbf{Decomposing K7's terminal-step collapse into
  coverage and intrinsic-decodability causes (K8).} \textbf{(a)} Q1:
  as the borrowed \model{} dictionary entry's $\sigma$ closes in on
  Rapid-AIO's terminal $\sigma{=}0.02$ (left to right), zero-shot
  transfer $R^2$ at Rapid $t{=}3$ rises monotonically toward each
  cell's native-refit ceiling (dotted) on 5/6 deep curves -- a
  coverage gap, not a terminal-step transfer breakdown. \textbf{(b)}
  Q2: \model{}'s own held-out native refit, with zero cross-model
  shift, collapses at the same terminal step for L52/L56 while L59
  stays at $0.99$ -- a model-independent loss of decodability. Data:
  \texttt{runs/k8\_sigma\_coverage/}.

## Generation

- Script: `fig18_k8_decompose.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/k8_sigma_coverage/summary.json (t3_scoring_table, q2_native_heldout_r2)

- Note: Redrawn 2026-07-14 from raw runs/ data to house style. See paper/provenance.md 'K7/K8/K9 figures added' section.

## Files in this folder

- `fig18_k8_decompose.jpg`
- `fig18_k8_decompose.png`
- `fig18_k8_decompose.py`
