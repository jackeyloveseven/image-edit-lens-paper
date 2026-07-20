"""Figure 1: edit example, layer-time lens, and five measured stages."""

import json
from pathlib import Path

import matplotlib
from matplotlib import font_manager

matplotlib.use("Agg")
for font_file in (
    "/usr/share/fonts/truetype/croscore/Arimo-Regular.ttf",
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/croscore/Arimo-Italic.ttf",
    "/usr/share/fonts/truetype/croscore/Arimo-BoldItalic.ttf",
):
    font_manager.fontManager.addfont(font_file)
matplotlib.rcParams.update({
    "font.family": "Arimo",
    "font.size": 8,
    "mathtext.fontset": "custom",
    "mathtext.rm": "Arimo",
    "mathtext.it": "Arimo:italic",
    "mathtext.bf": "Arimo:bold",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "axes.linewidth": 0.9,
})

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
from PIL import Image

RED = "#C2402A"
TEAL = "#0F8FA0"
INK = "#222222"
MUTE = "#6B6B6B"
GRID_BG = "#F5F5F5"

DATA_ROOT = Path("/home/ubuntu/chengyanli/image-edit-lens")
OUT_DIR = Path(__file__).resolve().parent

with open(DATA_ROOT / "runs/a1_car_red/lens_grid.json", encoding="utf-8") as f:
    lens_data = json.load(f)
scores = lens_data["clip_scores"]["raw"]
layers = lens_data["layers"]
steps = lens_data["steps"]
target = "a red car"
grid = np.array([
    [scores[f"l{layer}_t{step}"][target] for step in steps]
    for layer in layers
])

source = Image.open(DATA_ROOT / "runs/wp3_car_red/source.png")
edited = Image.open(DATA_ROOT / "runs/wp3_car_red/edited.png")


def panel_title(ax, letter, title):
    ax.text(-0.06, 1.075, letter, transform=ax.transAxes, fontsize=10,
            fontweight="bold", color=INK, ha="left", va="bottom")
    ax.text(0.02, 1.075, title, transform=ax.transAxes, fontsize=10,
            fontweight="bold", color=INK, ha="left", va="bottom")


fig = plt.figure(figsize=(7.05, 2.72), facecolor="white")
outer = fig.add_gridspec(
    1, 3,
    width_ratios=[0.28, 0.40, 0.32],
    left=0.025, right=0.985, top=0.82, bottom=0.16, wspace=0.28,
)

# A: source and edited example.
panel_a = fig.add_subplot(outer[0, 0])
panel_a.axis("off")
panel_title(panel_a, "A", "Edit example")
images = outer[0, 0].subgridspec(1, 2, wspace=0.30)
image_axes = []
for idx, (image, label) in enumerate(((source, "source"), (edited, "edited"))):
    ax = fig.add_subplot(images[0, idx])
    ax.imshow(image)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(label, fontsize=8, color=INK, pad=4)
    for spine in ax.spines.values():
        spine.set_color("#D0D0D0")
        spine.set_linewidth(0.8)
    image_axes.append(ax)

fig.canvas.draw()
left_box = image_axes[0].get_position()
right_box = image_axes[1].get_position()
mid_y = (left_box.y0 + left_box.y1) / 2
fig.patches.append(FancyArrowPatch(
    (left_box.x1 + 0.003, mid_y),
    (right_box.x0 - 0.003, mid_y),
    transform=fig.transFigure,
    arrowstyle="-|>", mutation_scale=8, linewidth=1.0, color=MUTE,
    clip_on=False,
))
fig.text((left_box.x1 + right_box.x0) / 2, mid_y + 0.045, "edit",
         fontsize=6.5, color=MUTE, ha="center", va="bottom")
fig.text((left_box.x0 + right_box.x1) / 2, min(left_box.y0, right_box.y0) - 0.045,
         "car_red", fontsize=7, color=MUTE, ha="center", va="top")

# B: frozen-head layer-time lens.
panel_b = fig.add_subplot(outer[0, 1])
panel_b.axis("off")
panel_title(panel_b, "B", "Layer-time lens")
bbox = panel_b.get_position()
heat_ax = fig.add_axes([
    bbox.x0 + 0.055 * bbox.width,
    bbox.y0 + 0.02 * bbox.height,
    0.72 * bbox.width,
    0.94 * bbox.height,
])
cmap = LinearSegmentedColormap.from_list(
    "lens", [GRID_BG, "#B8DDE0", TEAL, "#7F7770", RED], N=256
)
image = heat_ax.imshow(grid, aspect="auto", cmap=cmap, vmin=0, vmax=1,
                       origin="upper", interpolation="nearest")
heat_ax.set_xticks(range(len(steps)), [f"t{step}" for step in steps], fontsize=7.5)
heat_ax.set_yticks(range(len(layers)), [f"L{layer}" for layer in layers], fontsize=7.5)
heat_ax.set_xlabel("denoise step", fontsize=9, color=INK, labelpad=2)
heat_ax.set_ylabel("layer", fontsize=9, color=INK, labelpad=2)
heat_ax.tick_params(length=3, width=0.8, colors=INK)

# The coarse grid samples L48 and L54; mark the dense-sweep L52--54 band at L54.
translation_row = layers.index(54)
heat_ax.add_patch(Rectangle(
    (-0.5, translation_row - 0.46), len(steps), 0.92,
    facecolor=RED, edgecolor=RED, alpha=0.14, linewidth=1.3,
))
heat_ax.text(len(steps) - 0.55, translation_row, "translation",
             fontsize=7, color="white", fontweight="bold", ha="right", va="center",
             bbox=dict(boxstyle="round,pad=0.16", facecolor=RED,
                       edgecolor="none", alpha=0.92))

probe_row = layers.index(6)
heat_ax.scatter(-0.64, probe_row, marker=">", s=22, color=TEAL,
                edgecolor="white", linewidth=0.45, clip_on=False, zorder=5)
heat_ax.annotate(
    "probe-readable",
    xy=(-0.58, probe_row), xycoords="data",
    xytext=(-4, 10), textcoords="offset points",
    fontsize=7, color=TEAL, ha="right", va="bottom",
    arrowprops=dict(arrowstyle="-", color=TEAL, linewidth=0.7),
    annotation_clip=False,
)

cax = fig.add_axes([
    bbox.x0 + 0.82 * bbox.width,
    heat_ax.get_position().y0,
    0.035 * bbox.width,
    heat_ax.get_position().height,
])
colorbar = fig.colorbar(image, cax=cax)
colorbar.ax.tick_params(labelsize=7.5, length=2.5, width=0.8)
colorbar.set_label("P(red car)", fontsize=8, color=INK, labelpad=4)

# C: measured stages, using equal geometry and the exact paper terminology.
panel_c = fig.add_subplot(outer[0, 2])
panel_c.set_xlim(0, 1)
panel_c.set_ylim(0, 1)
panel_c.axis("off")
panel_title(panel_c, "C", "Measured stages")
stages = [
    ("Injection", "≤ L36", "#7BC1C9", INK),
    ("Outcome prediction", "L6 / t2–4", "#42AAB6", "white"),
    ("Target-image code", "L6–51", TEAL, "white"),
    ("Translation", "L52–54", "#D46A55", "white"),
    ("Output head", "L59", RED, "white"),
]
box_x, box_w, box_h, gap = 0.06, 0.88, 0.145, 0.035
top = 0.93
for idx, (name, location, color, text_color) in enumerate(stages):
    y = top - (idx + 1) * box_h - idx * gap
    panel_c.add_patch(FancyBboxPatch(
        (box_x, y), box_w, box_h,
        boxstyle="round,pad=0.008,rounding_size=0.018",
        facecolor=color, edgecolor="none",
    ))
    panel_c.text(box_x + box_w / 2, y + box_h * 0.64, name,
                 fontsize=8, fontweight="bold", color=text_color,
                 ha="center", va="center")
    panel_c.text(box_x + box_w / 2, y + box_h * 0.28, location,
                 fontsize=7.2, color=text_color, ha="center", va="center")

fig.savefig(OUT_DIR / "fig1_teaser.pdf", facecolor="white")
fig.savefig(OUT_DIR / "fig1_teaser.png", dpi=300, facecolor="white")
print("saved fig1_teaser.pdf/png")
