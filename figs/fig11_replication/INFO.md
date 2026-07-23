# fig11_replication

## Intent

Cross-model replication: A/C decode-crossover layer across
Qwen-Image-Edit-2511, FireRed-Image-Edit-1.1, and Rapid-AIO (all cluster
L52--56), plus the checkpoint-specific behavior of an off-manifold
layer-band ablation stress test.

## Used in

- supplement.tex

Current placement: supplement Figure 15.

## Target caption

### supplement.tex

Cross-model replication of the core measurements.
  \textbf{A}: the A/C decode-crossover layer (\S\ref{sec:mechanism}) for
  \model{} (reference), an independently fine-tuned checkpoint
  (FireRed-Image-Edit-1.1), and a 4-step distilled merge (Rapid-AIO), all
  clustered within L52--56. \textbf{B}: layer-band zero-ablation edit
  success for \emph{car\_red}, \model{} vs.\ FireRed -- the two replicate
  at L0--11 and diverge sharply at L48--59, the one genuine
  training-specific finding in this section.

## Generation

- Script: `fig11_replication.py` (run from this folder; regenerates the image from the data sources below)

- Data sources:

  - runs/g4_summary.json

- Note: Current placement is supplement Figure 15
  (`\label{fig:replication}`).

## Files in this folder

- `fig11_replication.pdf`
- `fig11_replication.py`
