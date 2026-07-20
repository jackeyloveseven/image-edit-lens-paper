"""Fig 5: mechanism. Panel A: D1 four-variant decode (L24 vs L59, at t4) showing
the sign of v only matters in the last ~6 blocks. Panel B: D2 cross-seed probe
accuracy heatmap (layer x step), rebuilt from raw numbers, headline L6/t4 cell
highlighted."""
import json
import os
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["ps.fonttype"] = 42
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
from PIL import Image

RED = "#C2402A"
TEAL = "#0F8FA0"
GRAY_D = "#444444"
GRAY_M = "#888888"

ROOT = Path(os.environ.get(
    "IMAGE_EDIT_LENS_ROOT",
    Path(__file__).resolve().parents[3] / "image-edit-lens",
))
OUT_DIR = Path(__file__).resolve().parent
D1 = ROOT / "runs" / "d1_signflip"

d1 = json.load(open(D1 / "d1_results.json"))
cs = d1["clip_scores"]
target = d1["target_label"]

variants = ["A_standard", "B_signflip", "C_v_as_x0", "D_neg_v_as_x0"]
vlabels = ["A: standard", "B: sign-flip", "C: v-as-x0", "D: neg-v-as-x0"]
rows = [24, 59]

fig = plt.figure(figsize=(7.05, 3.3))
gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1.0], wspace=0.32,
                       left=0.04, right=0.99, top=0.82, bottom=0.13)

# ---- Panel A ----
gsA = gs[0, 0].subgridspec(len(rows), len(variants), wspace=0.06, hspace=0.16)
for ridx, layer in enumerate(rows):
    for cidx, (v, vlab) in enumerate(zip(variants, vlabels)):
        ax = fig.add_subplot(gsA[ridx, cidx])
        img = Image.open(D1 / f"lens_l{layer}_t4_{v}.png")
        ax.imshow(img)
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        if ridx == 0:
            ax.set_title(vlab, fontsize=6.6, color=GRAY_D)
        if cidx == 0:
            ax.set_ylabel(f"L{layer}", fontsize=8, color=GRAY_D)
        p = cs[v][f"l{layer}_t4"]
        color = RED if p > 0.5 else GRAY_D
        ax.text(0.97, 0.05, f"{p:.2f}", transform=ax.transAxes, fontsize=6.3,
                color=color, ha="right", va="bottom",
                bbox=dict(boxstyle="round,pad=0.12", facecolor="white", edgecolor="none", alpha=0.8))
fig.text(0.235, 0.90, "sign flips near L59", fontsize=8.6, ha="center", color=GRAY_D)

# ---- Panel B: D2 heatmap ----
d2 = json.load(open(ROOT / "runs" / "d2_probe" / "accuracy_grid.json"))
layers = d2["layers"]
steps = d2["steps"]
acc = d2["accuracy_grid"]
grid = np.array([[acc[f"l{l}_t{t}"] for t in steps] for l in layers])

cmap = LinearSegmentedColormap.from_list("acc", ["#F2F2F2", TEAL, RED], N=256)
axB = fig.add_subplot(gs[0, 1])
im = axB.imshow(grid, aspect="auto", cmap=cmap, vmin=0.33, vmax=0.95, origin="upper")
axB.set_xticks(range(len(steps)))
axB.set_xticklabels([f"t{t}" for t in steps], fontsize=7.5)
axB.set_yticks(range(len(layers)))
axB.set_yticklabels([f"L{l}" for l in layers], fontsize=7.2)
axB.set_xlabel("denoising step", fontsize=8.5)
axB.set_ylabel("layer (of 59)", fontsize=8.5)
for i in range(len(layers)):
    for j in range(len(steps)):
        val = grid[i, j]
        tcolor = "white" if val > 0.75 else GRAY_D
        axB.text(j, i, f"{val:.2f}", ha="center", va="center", fontsize=5.4, color=tcolor)

# highlight headline cell L6, t4
li = layers.index(6)
sj = steps.index(4)
axB.add_patch(Rectangle((sj - 0.5, li - 0.5), 1, 1, fill=False, edgecolor=RED, linewidth=2.0))

cbar = fig.colorbar(im, ax=axB, fraction=0.055, pad=0.03)
cbar.ax.tick_params(labelsize=6.5)
cbar.set_label("3-way probe acc.", fontsize=7)
fig.text(0.735, 0.90, "decision readable early", fontsize=8.6, ha="center", color=GRAY_D)

fig.savefig(OUT_DIR / "fig5_mechanism.pdf", bbox_inches="tight")
print("wrote fig5_mechanism.pdf")
print("L6,t4 acc =", grid[li, sj])
