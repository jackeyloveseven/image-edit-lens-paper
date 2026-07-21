"""Figure 3: decode-convention reversal and early probe readability."""

import json
import os
from pathlib import Path

import matplotlib
from matplotlib import font_manager

matplotlib.use("Agg")


def resolve_font_family():
    candidates = ("Source Sans 3", "Arimo", "Arial", "Helvetica", "DejaVu Sans")
    font_files = sorted(set(
        font_manager.findSystemFonts(fontext="ttf")
        + font_manager.findSystemFonts(fontext="otf")
    ))
    by_family = {}
    for font_file in font_files:
        try:
            family = font_manager.FontProperties(fname=font_file).get_name()
        except (OSError, RuntimeError):
            continue
        by_family.setdefault(family, []).append(font_file)
    for family in candidates:
        if family in by_family:
            for font_file in by_family[family]:
                font_manager.fontManager.addfont(font_file)
            return family
    return "DejaVu Sans"


FONT_FAMILY = resolve_font_family()
print(f"font: {FONT_FAMILY}")
matplotlib.rcParams.update({
    "font.family": FONT_FAMILY,
    "font.size": 8,
    "mathtext.fontset": "custom",
    "mathtext.rm": FONT_FAMILY,
    "mathtext.it": f"{FONT_FAMILY}:italic",
    "mathtext.bf": f"{FONT_FAMILY}:bold",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "axes.linewidth": 0.9,
})

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
from PIL import Image

RED = "#C2402A"
TEAL = "#0F8FA0"
INK = "#222222"
MUTE = "#6B6B6B"
GRID_BG = "#F5F5F5"

ROOT = Path(os.environ.get(
    "IMAGE_EDIT_LENS_ROOT",
    Path(__file__).resolve().parents[3] / "image-edit-lens",
))
OUT_DIR = Path(__file__).resolve().parent
D1 = ROOT / "runs" / "d1_signflip"

with open(D1 / "d1_results.json", encoding="utf-8") as f:
    d1 = json.load(f)
scores = d1["clip_scores"]
variants = ["A_standard", "B_signflip", "C_v_as_x0", "D_neg_v_as_x0"]
variant_labels = ["A standard", "B sign-flip", "C v as x0", "D -v as x0"]
rows = [(24, "image-like"), (59, "velocity")]

fig = plt.figure(figsize=(6.9, 2.55), facecolor="white")
outer = fig.add_gridspec(
    1, 2, width_ratios=[0.55, 0.45],
    left=0.035, right=0.93, top=0.76, bottom=0.14, wspace=0.24,
)

# A: exact 2 x 4 image grid.
grid_a = outer[0, 0].subgridspec(
    2, 5, width_ratios=[0.34, 1, 1, 1, 1], wspace=0.06, hspace=0.12
)
first_ax = None
for row_idx, (layer, semantic) in enumerate(rows):
    label_ax = fig.add_subplot(grid_a[row_idx, 0])
    label_ax.axis("off")
    label_ax.text(0.95, 0.5, f"L{layer}\n{semantic}", fontsize=8,
                  color=INK, ha="right", va="center")
    for col_idx, (variant, label) in enumerate(zip(variants, variant_labels)):
        ax = fig.add_subplot(grid_a[row_idx, col_idx + 1])
        if first_ax is None:
            first_ax = ax
        ax.imshow(Image.open(D1 / f"lens_l{layer}_t4_{variant}.png"))
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color("#D0D0D0")
            spine.set_linewidth(0.6)
        if row_idx == 0:
            ax.set_title(label, fontsize=7.5, color=INK, pad=4)
        value = scores[variant][f"l{layer}_t4"]
        value_color = RED if value > 0.5 else INK
        ax.text(0.94, 0.07, f"{value:.2f}", transform=ax.transAxes,
                fontsize=7.5, fontweight="bold", color=value_color,
                ha="right", va="bottom",
                bbox=dict(boxstyle="round,pad=0.12", facecolor="white",
                          edgecolor="#D0D0D0", linewidth=0.35, alpha=0.92))

panel_a_box = outer[0, 0].get_position(fig)
fig.text((panel_a_box.x0 + panel_a_box.x1) / 2, 0.95,
         "A  Decode conventions", fontsize=10, fontweight="bold",
         color=INK, ha="center", va="top")

# B: probe-accuracy heatmap at the same total height.
with open(ROOT / "runs" / "d2_probe" / "accuracy_grid.json", encoding="utf-8") as f:
    d2 = json.load(f)
layers = d2["layers"]
steps = d2["steps"]
accuracy = d2["accuracy_grid"]
probe_grid = np.array([
    [accuracy[f"l{layer}_t{step}"] for step in steps]
    for layer in layers
])

ax_b = fig.add_subplot(outer[0, 1])
cmap = LinearSegmentedColormap.from_list(
    "probe", [GRID_BG, "#B8DDE0", TEAL, RED], N=256
)
image = ax_b.imshow(probe_grid, aspect="auto", cmap=cmap, vmin=1 / 3, vmax=0.95,
                    origin="upper", interpolation="nearest")
ax_b.set_xticks(range(len(steps)), [f"t{step}" for step in steps], fontsize=7.5)
ax_b.set_yticks(range(len(layers)), [f"L{layer}" for layer in layers], fontsize=7.5)
ax_b.set_xlabel("denoise step", fontsize=9, color=INK, labelpad=2)
ax_b.tick_params(length=2.5, width=0.8, colors=INK)
for row_idx in range(len(layers)):
    for col_idx in range(len(steps)):
        value = probe_grid[row_idx, col_idx]
        text_color = "white" if value >= 0.72 else INK
        ax_b.text(col_idx, row_idx, f"{value:.2f}", fontsize=7.5,
                  color=text_color, ha="center", va="center")

headline_row = layers.index(6)
headline_col = steps.index(4)
ax_b.add_patch(Rectangle(
    (headline_col - 0.5, headline_row - 0.5), 1, 1,
    fill=False, edgecolor=RED, linewidth=1.8,
))
panel_b_box = outer[0, 1].get_position(fig)
fig.text((panel_b_box.x0 + panel_b_box.x1) / 2, 0.95,
         "B  Early probe", fontsize=10, fontweight="bold",
         color=INK, ha="center", va="top")

position = ax_b.get_position()
cax = fig.add_axes([position.x1 + 0.009, position.y0, 0.012, position.height])
colorbar = fig.colorbar(image, cax=cax)
colorbar.set_ticks([1 / 3, 0.6, 0.9])
colorbar.ax.tick_params(labelsize=7, length=2, width=0.7)
colorbar.set_label("3-way probe acc.", fontsize=7.5, color=INK, labelpad=2)

fig.savefig(OUT_DIR / "fig5_mechanism.pdf", facecolor="white")
print("wrote fig5_mechanism.pdf")
print("L6,t4 acc =", probe_grid[headline_row, headline_col])
