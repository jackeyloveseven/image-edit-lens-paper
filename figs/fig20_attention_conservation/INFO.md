# fig20_attention_conservation

## Intent

RESTORE-inspired T11 audit comparing reference-matched joint-attention routing
distortion with blinded rendered geometry. Panel A shows five seed replicates
and condition means; panels B and C are explicitly post-hoc decompositions by
query group and layer.

## Used in

- `supplement.tex`

## Generation

- Script: `fig20_attention_conservation.py`
- Data source: `runs/t11_attention_conservation/detailed_analysis.json`
- Set `IMAGE_EDIT_LENS_ROOT` when the code repository is not adjacent to the
  paper repository.

## Claim boundary

The figure supports an attention-routing distortion explanation for the tested
Qwen car interventions. It does not establish token reduction, speedup, causal
necessity, architecture universality, or transfer of RESTORE calibration.
