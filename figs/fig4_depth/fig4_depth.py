"""Fig 4: depth emergence. Panel A: contact-sheet excerpt (rows=layer, cols=step)
for car_red, showing complementary-color mid-stack renderings snapping to red at
L48-54. Panel B: P(red car) vs layer curves at 5 timesteps, snap zone shaded."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

RED = "#C2402A"
TEAL = "#0F8FA0"
GRAY_D = "#444444"

ROOT = "/home/ubuntu/chengyanli/image-edit-lens"
RUN = f"{ROOT}/runs/a1_car_red"

excerpt_layers = [0, 24, 48, 54, 59]
excerpt_steps = [0, 4, 19]

d = json.load(open(f"{RUN}/lens_grid.json"))
cs_raw = d["clip_scores"]["raw"]
target = "a red car"

fig = plt.figure(figsize=(7.0, 3.35))
gs = fig.add_gridspec(1, 2, width_ratios=[1.05, 1.0], wspace=0.28,
                       left=0.045, right=0.98, top=0.80, bottom=0.14)

# ---- Panel A: contact-sheet excerpt ----
gsA = gs[0, 0].subgridspec(len(excerpt_layers), len(excerpt_steps), wspace=0.05, hspace=0.12)
for ridx, layer in enumerate(excerpt_layers):
    for cidx, step in enumerate(excerpt_steps):
        ax = fig.add_subplot(gsA[ridx, cidx])
        img = Image.open(f"{RUN}/lens_l{layer}_t{step}_raw.png")
        ax.imshow(img)
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        if ridx == 0:
            ax.set_title(f"t{step}", fontsize=8, color=GRAY_D)
        if cidx == 0:
            ax.set_ylabel(f"L{layer}", fontsize=8, color=GRAY_D)
        p = cs_raw[f"l{layer}_t{step}"][target]
        color = RED if p > 0.5 else GRAY_D
        ax.text(0.97, 0.05, f"{p:.2f}", transform=ax.transAxes, fontsize=6.3,
                color=color, ha="right", va="bottom",
                bbox=dict(boxstyle="round,pad=0.12", facecolor="white", edgecolor="none", alpha=0.75))
fig.text(0.24, 0.93, "layer x step decode", fontsize=9.5, ha="center", color=GRAY_D)

# ---- Panel B: P(red car) vs layer curves ----
axB = fig.add_subplot(gs[0, 1])
layers = d["layers"]
steps5 = [0, 4, 10, 16, 19]
grays = ["#CFCFCF", "#9A9A9A", "#6B6B6B", "#3E3E3E", "#111111"]
axB.axvspan(48, 54, color=RED, alpha=0.12, zorder=0)
for t, color in zip(steps5, grays):
    vals = [cs_raw[f"l{l}_t{t}"][target] for l in layers]
    axB.plot(layers, vals, color=color, marker="o", markersize=2.8, linewidth=1.4, label=f"t{t}")
axB.text(51, 1.0, "snap", fontsize=7.5, color=RED, ha="center", va="top", fontweight="bold")
axB.set_xlabel("layer (of 59)", fontsize=9.5)
axB.set_ylabel("P(red car)", fontsize=9.5)
axB.set_ylim(-0.02, 1.05)
axB.set_xlim(-2, 61)
axB.tick_params(labelsize=8.5)
for spine in ["top", "right"]:
    axB.spines[spine].set_visible(False)
axB.legend(loc="center left", fontsize=7, frameon=False, handlelength=1.6, labelspacing=0.3)
fig.text(0.74, 0.93, "P(red) vs layer", fontsize=9.5, ha="center", color=GRAY_D)

fig.savefig(f"{ROOT}/paper/figs/fig4_depth.pdf", bbox_inches="tight")
print("wrote fig4_depth.pdf")
