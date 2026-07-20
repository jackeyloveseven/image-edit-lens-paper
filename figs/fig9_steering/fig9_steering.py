"""Fig 9 (G-phase): activation steering dose-response. Adding the probe
direction d_red at L6-23 (all steps) to a car_green recipient's car-region
rows flips the output to red above a sharp alpha~1 threshold; a random
direction at the same alpha does not; the negative direction overshoots
to blue, not back to green."""
import json
import os
from pathlib import Path
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
g1 = json.load(open(ROOT / "runs" / "g1_steer" / "summary.json"))

by_cond = {r["condition"]: r for r in g1["results"]}
alphas = [0.0, 0.5, 1.0, 2.0, 4.0, 8.0]
conds = ["control_no_steer", "alpha_0.5", "alpha_1", "alpha_2", "alpha_4", "alpha_8"]
p_red = [by_cond[c]["scores"]["a red car"] for c in conds]
p_green = [by_cond[c]["scores"]["a green car"] for c in conds]

fig, ax = plt.subplots(figsize=(3.35, 2.65))
ax.plot(alphas, p_red, color=RED, marker="o", markersize=4.5, linewidth=1.8, label="P(red)")
ax.plot(alphas, p_green, color=GRAY_M, marker="o", markersize=4.5, linewidth=1.4,
        linestyle="--", label="P(green)")

rd = by_cond["random_dir_alpha2"]
ax.scatter([2.0], [rd["scores"]["a red car"]], marker="s", s=42, facecolor="none",
           edgecolor=TEAL, linewidth=1.4, zorder=5, label="random dir")
nd = by_cond["neg_dir_alpha2"]
ax.scatter([2.0], [nd["scores"]["a blue car"]], marker="v", s=42, color=TEAL,
           zorder=5, label="-dir: P(blue)")

ax.set_xlabel(r"steer strength $\alpha$", fontsize=9.5)
ax.set_ylabel("CLIP probability", fontsize=9.5)
ax.set_ylim(-0.03, 1.05)
ax.tick_params(labelsize=8.5)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.legend(fontsize=6.6, frameon=False, loc="center right", handlelength=1.5, labelspacing=0.35)
ax.set_title("steering dose-response", fontsize=9.3, color=GRAY_D)

fig.savefig(OUT_DIR / "fig9_steering.pdf", bbox_inches="tight")
print("wrote fig9_steering.pdf")
