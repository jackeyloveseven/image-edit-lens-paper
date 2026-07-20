"""Fig 7: applications. Panel A: decision-saliency heatmap (naive magnitude vs
probe saliency) fraction of top-10% patches inside car bbox. Panel B: step-budget
prediction (target score vs #steps run, 3 cases). Panel C: mid-stack transplant
rescue vs global CFG bump."""
import json
import os
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["ps.fonttype"] = 42
import matplotlib.pyplot as plt
from PIL import Image

RED = "#C2402A"
TEAL = "#0F8FA0"
GRAY_D = "#444444"
GRAY_M = "#888888"
GRAY_L = "#BBBBBB"

ROOT = Path(os.environ.get(
    "IMAGE_EDIT_LENS_ROOT",
    Path(__file__).resolve().parents[3] / "image-edit-lens",
))
OUT_DIR = Path(__file__).resolve().parent

fig, axes = plt.subplots(1, 3, figsize=(6.9, 2.55))

# ---- Panel A: saliency before/after (crop out baked-in title banner) ----
img = Image.open(ROOT / "runs" / "e1_saliency" / "before_after_L12_t4.png")
w, h = img.size
crop = img.crop((0, int(h * 0.135), w, h))
axes[0].imshow(crop)
axes[0].set_xticks([]); axes[0].set_yticks([])
for s in axes[0].spines.values():
    s.set_visible(False)
cw, ch = crop.size
axes[0].text(cw * 0.25, ch * 0.06, "38% in car", fontsize=8, color="white", ha="center",
             va="top", fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.2", facecolor=GRAY_M, edgecolor="none", alpha=0.85))
axes[0].text(cw * 0.75, ch * 0.06, "99% in car", fontsize=8, color="white", ha="center",
             va="top", fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.2", facecolor=RED, edgecolor="none", alpha=0.9))
axes[0].set_title("decision saliency", fontsize=9, color=GRAY_D)

# ---- Panel B: step-budget prediction ----
e3 = json.load(open(ROOT / "runs" / "e3_earlyexit" / "summary.json"))
cases = ["color_car", "style_watercolor", "add_boat"]
clabels = {"color_car": "car (color)", "style_watercolor": "watercolor", "add_boat": "add boat"}
colors = {"color_car": TEAL, "style_watercolor": GRAY_D, "add_boat": RED}
for c in cases:
    r = e3["results"][c]
    xs = [4, 8, 20]
    ys = [r["steps"]["4"]["target_score"], r["steps"]["8"]["target_score"], r["ref20_target_score"]]
    lw = 2.4 if c == "add_boat" else 1.3
    axes[1].plot(xs, ys, marker="o", markersize=4, linewidth=lw, color=colors[c], label=clabels[c])
axes[1].set_xlabel("steps run", fontsize=9)
axes[1].set_ylabel("target score", fontsize=9)
axes[1].set_xticks([4, 8, 20])
axes[1].set_ylim(0.85, 1.02)
axes[1].legend(fontsize=6.6, frameon=False, loc="lower right", handlelength=1.5, labelspacing=0.3)
axes[1].set_title("step-budget prediction", fontsize=9, color=GRAY_D)
for spine in ["top", "right"]:
    axes[1].spines[spine].set_visible(False)
axes[1].tick_params(labelsize=8)

# ---- Panel C: rescue ----
e3r = json.load(open(ROOT / "runs" / "e3_rescue" / "summary.json"))
labels = ["original", "transplant", "global CFG"]
vals = [e3r["original_cropped_P_black_cup"], e3r["R2"]["P_black_cup_cropped"], e3r["R1"]["P_black_cup_cropped"]]
bar_colors = [GRAY_M, RED, TEAL]
x = np.arange(3)
bars = axes[2].bar(x, vals, width=0.55, color=bar_colors)
for xi, v in zip(x, vals):
    axes[2].text(xi, v + 0.02, f"{v:.2f}", ha="center", fontsize=7.6, color=GRAY_D)
axes[2].set_xticks(x)
axes[2].set_xticklabels(labels, fontsize=7.6)
axes[2].set_ylim(0, 1.02)
axes[2].set_ylabel("P(black cup)", fontsize=9)
axes[2].set_title("mid-stack rescue", fontsize=9, color=GRAY_D)
for spine in ["top", "right"]:
    axes[2].spines[spine].set_visible(False)
axes[2].tick_params(labelsize=8)

fig.tight_layout()
fig.savefig(OUT_DIR / "fig7_applications.pdf", bbox_inches="tight")
print("wrote fig7_applications.pdf")
print("rescue vals", vals)
