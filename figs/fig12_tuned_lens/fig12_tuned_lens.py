"""Figure 4: symmetric 2x3 tuned-lens comparison for one-column use."""

import os
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
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

import matplotlib.pyplot as plt
from PIL import Image

RED = "#C2402A"
TEAL = "#0F8FA0"
INK = "#222222"
LIGHT_BORDER = "#C8C8C8"

ROOT = Path(os.environ.get(
    "IMAGE_EDIT_LENS_ROOT",
    Path(__file__).resolve().parents[3] / "image-edit-lens",
))
RUN = ROOT / "runs" / "k1_tuned_lens"
OUT_DIR = Path(__file__).resolve().parent

rows = [
    [
        (RUN / "cells/tuned_L24_t0.png", "tuned · L24 · t0", LIGHT_BORDER, None),
        (RUN / "cells/tuned_L36_t0.png", "tuned · L36 · t0", LIGHT_BORDER, None),
        (RUN / "cells/tuned_L52_t0.png", "tuned · L52 · t0", LIGHT_BORDER, None),
    ],
    [
        (RUN / "cells/raw_L36_t12.png", "raw · L36 · t12", RED, "anti-image"),
        (RUN / "cells/tuned_L36_t12.png", "tuned · L36 · t12", TEAL, "tuned"),
        (RUN / "test_car_red_edited.png", "final output · t19", LIGHT_BORDER, None),
    ],
]

fig = plt.figure(figsize=(3.28, 2.34), facecolor="white")
grid = fig.add_gridspec(
    4, 3,
    height_ratios=[0.13, 1.0, 0.13, 1.0],
    left=0.025, right=0.985, top=0.985, bottom=0.025,
    wspace=0.055, hspace=0.17,
)

for row_idx, (letter, heading) in enumerate((
    ("A", "Edit enters internal image"),
    ("B", "Head fails, lens succeeds"),
)):
    header = fig.add_subplot(grid[row_idx * 2, :])
    header.axis("off")
    header.text(0.0, 0.55, letter, fontsize=10, fontweight="bold",
                color=INK, ha="left", va="center")
    header.text(0.075, 0.55, heading, fontsize=10, fontweight="bold",
                color=INK, ha="left", va="center")

    for col_idx, (path, label, border, badge) in enumerate(rows[row_idx]):
        ax = fig.add_subplot(grid[row_idx * 2 + 1, col_idx])
        ax.imshow(Image.open(path))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(label, fontsize=7.2, fontweight="bold", color=INK, pad=2)
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color(border)
            spine.set_linewidth(1.5 if border in (RED, TEAL) else 0.7)
        if badge:
            ax.text(0.04, 0.94, badge, transform=ax.transAxes, fontsize=7,
                    fontweight="bold", color="white", ha="left", va="top",
                    bbox=dict(boxstyle="round,pad=0.18", facecolor=border,
                              edgecolor="none", alpha=0.95))

fig.savefig(OUT_DIR / "fig12_tuned_lens.pdf", facecolor="white")
fig.savefig(OUT_DIR / "fig12_tuned_lens.png", dpi=300, facecolor="white")
fig.savefig(OUT_DIR / "fig12_tuned_lens.jpg", dpi=300, facecolor="white",
            pil_kwargs={"quality": 95})
print("wrote fig12_tuned_lens.pdf/png/jpg")
