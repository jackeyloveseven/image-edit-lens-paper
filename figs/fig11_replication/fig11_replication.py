"""Fig 11 (G4): cross-model replication. Panel A: the A/C crossover layer
(where the two-code translation completes) across three checkpoints --
Qwen-Image-Edit-2511 (reference), FireRed-Image-Edit-1.1 (independent
fine-tune), and a 4-step distilled merge (Rapid-AIO) -- all cluster at
L52-56. Panel B: layer-band zero-ablation edit success, Qwen vs. FireRed,
showing the one genuine divergence: FireRed's late band (L48-59) is
catastrophic where Qwen's is harmless."""
import json
import os
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["ps.fonttype"] = 42
import matplotlib.pyplot as plt

RED = "#C2402A"
TEAL = "#0F8FA0"
GRAY_D = "#444444"
GRAY_M = "#999999"

ROOT = Path(os.environ.get(
    "IMAGE_EDIT_LENS_ROOT",
    Path(__file__).resolve().parents[3] / "image-edit-lens",
))
OUT_DIR = Path(__file__).resolve().parent
g4 = json.load(open(ROOT / "runs" / "g4_summary.json"))
f1 = g4["findings"][0]
f4 = g4["findings"][3]

fig, axes = plt.subplots(1, 2, figsize=(6.9, 2.35))

# ---- Panel A: crossover-layer replication across models ----
axA = axes[0]

def scatter_series(d, color, label, marker):
    xs = sorted((int(k) for k, v in d.items() if v is not None))
    ys = [d[str(x)] for x in xs]
    axA.plot(xs, ys, color=color, marker=marker, markersize=5.5, linewidth=1.2,
              linestyle="--", label=label)

scatter_series(f1["qwen"], TEAL, "Qwen (ref)", "o")
scatter_series(f1["firered_car"], RED, "FireRed (fine-tune)", "s")
scatter_series(f1["rapidaio_4step"], GRAY_D, "Rapid-AIO (4-step distill)", "^")
axA.set_xlabel("denoising step", fontsize=8.5)
axA.set_ylabel("A/C crossover layer", fontsize=8.5)
axA.set_ylim(51, 57)
axA.legend(fontsize=6.2, frameon=False, loc="upper left", handlelength=1.5, labelspacing=0.3)
axA.set_title("translation boundary replicates", fontsize=9, color=GRAY_D)
axA.tick_params(labelsize=7.5)
for spine in ["top", "right"]:
    axA.spines[spine].set_visible(False)

# ---- Panel B: layer-band ablation, Qwen vs FireRed ----
axB = axes[1]
bands = ["L0_11", "L24_35", "L48_59"]
band_labels = ["0-11", "24-35", "48-59"]
qwen_vals = [f4["qwen"][b]["edit_success"] for b in bands]
fr_vals = [f4["firered"][b]["edit_success"] for b in bands]
x = np.arange(len(bands))
w = 0.36
axB.bar(x - w / 2, qwen_vals, width=w, color=TEAL, label="Qwen")
axB.bar(x + w / 2, fr_vals, width=w, color=RED, label="FireRed")
axB.set_xticks(x)
axB.set_xticklabels(band_labels, fontsize=7.8)
axB.set_ylim(0, 1.02)
axB.set_ylabel("edit success (car_red)", fontsize=8.5)
axB.set_xlabel("layer band ablated", fontsize=8.5)
axB.legend(fontsize=7, frameon=False, loc="upper right", handlelength=1.5)
axB.set_title("late-band divergence", fontsize=9, color=GRAY_D)
axB.tick_params(labelsize=7.5)
for spine in ["top", "right"]:
    axB.spines[spine].set_visible(False)
axB.annotate("catastrophic\nfor FireRed only", xy=(2 + w / 2, fr_vals[2] + 0.02),
             xytext=(1.05, 0.55), fontsize=6.6, color=RED, ha="center",
             arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=0.9))

for ax, letter in zip(axes, "AB"):
    ax.text(-0.14, 1.06, letter, transform=ax.transAxes, fontsize=10, fontweight="bold")

fig.tight_layout()
fig.savefig(OUT_DIR / "fig11_replication.pdf", bbox_inches="tight")
print("wrote fig11_replication.pdf")
print("qwen L48_59:", f4["qwen"]["L48_59"]["edit_success"], "firered L48_59:", f4["firered"]["L48_59"]["edit_success"])
