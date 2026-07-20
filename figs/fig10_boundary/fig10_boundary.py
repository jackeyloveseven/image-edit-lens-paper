"""Figure 5: timestep-stable translation band in a dense layer sweep."""

import json
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
    "mathtext.fontset": "custom",
    "mathtext.rm": "Arimo",
    "mathtext.it": "Arimo:italic",
    "mathtext.bf": "Arimo:bold",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "axes.linewidth": 0.9,
})

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

RED = "#C2402A"
TEAL = "#0F8FA0"
INK = "#222222"
MUTE = "#6B6B6B"

ROOT = Path(os.environ.get(
    "IMAGE_EDIT_LENS_ROOT",
    Path(__file__).resolve().parents[3] / "image-edit-lens",
))
OUT_DIR = Path(__file__).resolve().parent
with open(ROOT / "runs" / "g2_boundary" / "boundary_summary.json", encoding="utf-8") as f:
    boundary = json.load(f)

layers = boundary["layers"]
steps = ["4", "16"]
colors = {"4": TEAL, "16": RED}

fig, axes = plt.subplots(
    1, 3, figsize=(6.9, 2.48), sharex=True,
    gridspec_kw={"left": 0.07, "right": 0.985, "top": 0.82,
                 "bottom": 0.28, "wspace": 0.30},
)

for ax in axes:
    ax.axvspan(52, 54, facecolor=RED, alpha=0.13, edgecolor="none", zorder=0)
    ax.set_xlim(44, 59)
    ax.set_xticks([44, 48, 52, 54, 56, 59])
    ax.set_xlabel("layer", fontsize=9, color=INK, labelpad=2)
    ax.tick_params(labelsize=7.5, length=3, width=0.8, colors=INK)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.text(53, 1.015, "translation", transform=ax.get_xaxis_transform(),
            fontsize=7, fontweight="bold", color=RED, ha="center", va="bottom")

# A: standard and direct-v decode crossover.
ax_a = axes[0]
for step in steps:
    values = boundary["per_step"][step]
    ax_a.plot(layers, values["P_A"], color=colors[step], marker="o",
              markersize=3.2, linewidth=1.5, linestyle="-", zorder=2)
    ax_a.plot(layers, values["P_C"], color=colors[step], marker="o",
              markersize=3.2, linewidth=1.35, linestyle="--", zorder=2)
ax_a.set_ylabel("CLIP P(red)", fontsize=9, color=INK, labelpad=3)
ax_a.set_ylim(0, 1.02)

# B: alignment to terminal velocity.
ax_b = axes[1]
for step in steps:
    values = boundary["per_step"][step]
    ax_b.plot(layers, values["cos_v59"], color=colors[step], marker="o",
              markersize=3.2, linewidth=1.5, zorder=2)
ax_b.set_ylabel(r"cos($v_\ell$, $v_{59}$)", fontsize=9, color=INK, labelpad=3)
ax_b.set_ylim(0.45, 1.02)

# C: probe remains readable through L58, then drops at L59.
ax_c = axes[2]
for step in steps:
    values = boundary["per_step"][step]
    ax_c.plot(layers, values["probe_accuracy"], color=colors[step], marker="o",
              markersize=3.2, linewidth=1.5, zorder=2)
ax_c.axhline(1 / 3, color=MUTE, linewidth=1.0, linestyle=(0, (3, 2)), zorder=1)
ax_c.set_ylabel("probe accuracy", fontsize=9, color=INK, labelpad=3)
ax_c.set_ylim(0.30, 0.95)

titles = ["A  A/C crossover", "B  Alignment to v59", "C  Probe accuracy"]
for ax, title in zip(axes, titles):
    letter, text = title.split("  ", 1)
    ax.text(-0.08, 1.12, letter, transform=ax.transAxes, fontsize=10,
            fontweight="bold", color=INK, ha="left", va="bottom")
    ax.text(0.05, 1.12, text, transform=ax.transAxes, fontsize=10,
            fontweight="bold", color=INK, ha="left", va="bottom")

legend_handles = [
    Line2D([0], [0], color=TEAL, marker="o", linewidth=1.5, markersize=3.2,
           label="t=4"),
    Line2D([0], [0], color=RED, marker="o", linewidth=1.5, markersize=3.2,
           label="t=16"),
    Line2D([0], [0], color=INK, linewidth=1.5, linestyle="-", label="A standard"),
    Line2D([0], [0], color=INK, linewidth=1.35, linestyle="--", label="C direct-v"),
    Line2D([0], [0], color=MUTE, linewidth=1.0, linestyle=(0, (3, 2)), label="chance"),
]
fig.legend(handles=legend_handles, loc="lower center", bbox_to_anchor=(0.5, 0.045),
           ncol=5, frameon=False, fontsize=7.5, handlelength=2.0,
           columnspacing=1.4, handletextpad=0.45)

fig.savefig(OUT_DIR / "fig10_boundary.pdf", facecolor="white")
print("wrote fig10_boundary.pdf")
print("midpoints:", {
    step: boundary["per_step"][step]["crossover_midpoint_layer"]
    for step in steps
})
