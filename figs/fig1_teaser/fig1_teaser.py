"""
Fig 1: teaser. Source -> edited image, mini layer x time P(red) heatmap
(the "layer-time lens"), and a two-code schematic (target-image code ->
translation -> velocity code). Palette: red #C2402A, teal #0F8FA0, grays.
"""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["ps.fonttype"] = 42
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image

RED = "#C2402A"
TEAL = "#0F8FA0"
GRAY_D = "#444444"
GRAY_M = "#888888"
GRAY_L = "#BBBBBB"

DATA_ROOT = Path("/home/ubuntu/chengyanli/image-edit-lens")
OUT_DIR = Path(__file__).resolve().parent

# ---- data ----
d = json.load(open(DATA_ROOT / "runs/a1_car_red/lens_grid.json"))
cs = d["clip_scores"]["raw"]
layers = d["layers"]  # [0,6,12,18,24,30,36,42,48,54,59]
steps = d["steps"]  # [0,4,10,16,19]
target = "a red car"
grid = np.array([[cs[f"l{l}_t{t}"][target] for t in steps] for l in layers])  # (layers, steps)

src_img = Image.open(DATA_ROOT / "runs/wp3_car_red/source.png")
edit_img = Image.open(DATA_ROOT / "runs/wp3_car_red/edited.png")

# ---- figure ----
fig = plt.figure(figsize=(7.05, 2.75))
gs = fig.add_gridspec(1, 4, width_ratios=[1.0, 1.0, 1.35, 1.55], wspace=0.38,
                       left=0.015, right=0.985, top=0.84, bottom=0.16)

# panel 1: source
ax0 = fig.add_subplot(gs[0, 0])
ax0.imshow(src_img)
ax0.set_xticks([]); ax0.set_yticks([])
for s in ax0.spines.values():
    s.set_visible(False)
ax0.set_title("source", fontsize=9, color=GRAY_D)

# arrow between panel 1 and 2 (drawn in figure coords later)

# panel 2: edited
ax1 = fig.add_subplot(gs[0, 1])
ax1.imshow(edit_img)
ax1.set_xticks([]); ax1.set_yticks([])
for s in ax1.spines.values():
    s.set_visible(False)
ax1.set_title("edited", fontsize=9, color=RED)

# arrow from source to edited
fig.canvas.draw()
p0 = ax0.get_position()
p1 = ax1.get_position()
arrow = FancyArrowPatch((p0.x1 + 0.002, (p0.y0 + p0.y1) / 2),
                         (p1.x0 - 0.002, (p1.y0 + p1.y1) / 2),
                         transform=fig.transFigure, arrowstyle="-|>",
                         mutation_scale=10, color=GRAY_D, linewidth=1.2,
                         clip_on=False)
fig.patches.append(arrow)
fig.text((p0.x1 + p1.x0) / 2, (p0.y0 + p0.y1) / 2 + 0.10, "edit", fontsize=7.5,
          ha="center", color=GRAY_D)

# panel 3: layer x time P(red) heatmap
cmap = LinearSegmentedColormap.from_list("lens", ["#F2F2F2", TEAL, RED], N=256)
ax2 = fig.add_subplot(gs[0, 2])
im = ax2.imshow(grid, aspect="auto", cmap=cmap, vmin=0.0, vmax=1.0, origin="upper")
ax2.set_xticks(range(len(steps)))
ax2.set_xticklabels([f"t{t}" for t in steps], fontsize=7)
ax2.set_yticks(range(len(layers)))
ax2.set_yticklabels([f"L{l}" for l in layers], fontsize=7)
ax2.set_xlabel("denoise step", fontsize=7.5, labelpad=2)
ax2.set_ylabel("layer", fontsize=8, labelpad=1)
ax2.set_title("P(red) lens", fontsize=9, color=GRAY_D)
# snap-zone bracket between L48 (idx 8) and L54 (idx 9)
ax2.add_patch(Rectangle((-0.5, 7.5), len(steps) - 0.02, 2, fill=False,
                         edgecolor=RED, linewidth=1.6, clip_on=False))
ax2.text(0.5, 8.5, "snap", fontsize=7, color=RED, va="center",
          ha="center", fontweight="bold",
          bbox=dict(boxstyle="round,pad=0.15", facecolor="white",
                     edgecolor="none", alpha=0.75))
cbar = fig.colorbar(im, ax=ax2, fraction=0.06, pad=0.04)
cbar.ax.tick_params(labelsize=6)
cbar.set_label("P(red car)", fontsize=6.5)

# panel 4: five measured stages (Injection -> Outcome prediction -> Target-image
# code -> Translation -> Output head), replacing the earlier two-box
# schematic; the color language (teal = target-image code, red = translation
# / velocity-code readout) is kept from the original two-code framing.
ax3 = fig.add_subplot(gs[0, 3])
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)
ax3.axis("off")
ax3.set_title("measured stages", fontsize=9, color=GRAY_D)

stages = [
    ("Injection", "$\\leq$L36", "(late text dispensable)", TEAL, 0.55),
    ("Outcome prediction", "L6 / t2–4", None, TEAL, 0.72),
    ("Target-image code", "L6–51", None, TEAL, 0.9),
    ("Translation", "L52–54", None, RED, 0.85),
    ("Output head", "L59", None, RED, 1.0),
]
box_h, gap, top = 1.28, 0.34, 9.15
box_w = 8.6
x0 = (10 - box_w) / 2
y = top
centers = []
for name, rng, sub, color, alpha in stages:
    y0 = y - box_h
    ax3.add_patch(FancyBboxPatch((x0, y0), box_w, box_h,
                                  boxstyle="round,pad=0.02,rounding_size=0.12",
                                  facecolor=color, alpha=alpha, edgecolor="none"))
    ax3.text(x0 + box_w / 2, y0 + box_h * 0.62, name, fontsize=6.8, color="white",
              ha="center", va="center", fontweight="bold")
    sub_txt = rng if sub is None else f"{rng}  {sub}"
    ax3.text(x0 + box_w / 2, y0 + box_h * 0.24, sub_txt, fontsize=5.6,
              color="white", ha="center", va="center")
    centers.append((y0, y))
    y = y0 - gap
# down-arrows between consecutive boxes
for (y0_prev, y1_prev), (y0_next, y1_next) in zip(centers[:-1], centers[1:]):
    ax3.annotate("", xy=(x0 + box_w / 2, y0_next + box_h + 0.02),
                 xytext=(x0 + box_w / 2, y0_prev - 0.02),
                 arrowprops=dict(arrowstyle="-|>", color=GRAY_D, linewidth=1.0))

fig.savefig(OUT_DIR / "fig1_teaser.pdf")
fig.savefig(OUT_DIR / "fig1_teaser.png", dpi=200)
print("saved fig1_teaser.pdf/png")
print("grid P(red) L0..L59 rows x t0..t19 cols:")
print(grid)
