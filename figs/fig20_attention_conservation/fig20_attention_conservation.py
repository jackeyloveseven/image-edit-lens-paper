"""T11 attention-routing conservation audit for the supplement."""

import json
import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(
    os.environ.get(
        "IMAGE_EDIT_LENS_ROOT",
        Path(__file__).resolve().parents[3] / "image-edit-lens",
    )
)
OUT_DIR = Path(__file__).resolve().parent
RESULT = json.load(
    open(
        ROOT / "runs" / "t11_attention_conservation" / "detailed_analysis.json",
        encoding="utf-8",
    )
)

CONDITIONS = [
    "zero_l0_11",
    "mean_l0_11",
    "transplant_l0_23",
    "background_transplant_l0_23",
    "steer_red_alpha2_l6_23",
    "random_steer_alpha2_l6_23",
]
LABELS = {
    "zero_l0_11": "Zero",
    "mean_l0_11": "Mean",
    "transplant_l0_23": "Car donor",
    "background_transplant_l0_23": "BG donor",
    "steer_red_alpha2_l6_23": "Red steer",
    "random_steer_alpha2_l6_23": "Random steer",
}
COHERENT = {
    "zero_l0_11": False,
    "mean_l0_11": False,
    "transplant_l0_23": True,
    "background_transplant_l0_23": False,
    "steer_red_alpha2_l6_23": False,
    "random_steer_alpha2_l6_23": True,
}

plt.rcParams.update(
    {
        "font.size": 6.6,
        "axes.titlesize": 7.4,
        "axes.labelsize": 6.8,
        "xtick.labelsize": 6.2,
        "ytick.labelsize": 6.2,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
)

coherent_color = "#16837A"
incoherent_color = "#C74B3A"
neutral = "#2D3748"
grid = "#D6DADE"
summary = RESULT["condition_summary"]

figure, axes = plt.subplots(
    1,
    3,
    figsize=(7.05, 2.72),
    gridspec_kw={"width_ratios": [1.22, 1.0, 1.08]},
)

# A: registered condition-level distortion with seed replicates.
x = np.arange(len(CONDITIONS))
for index, condition in enumerate(CONDITIONS):
    values = summary[condition]["per_seed"]
    color = coherent_color if COHERENT[condition] else incoherent_color
    axes[0].scatter(
        np.full(len(values), index),
        values,
        color=color,
        s=12,
        alpha=0.65,
        edgecolor="white",
        linewidth=0.35,
        zorder=2,
    )
    axes[0].plot(
        [index - 0.27, index + 0.27],
        [np.mean(values), np.mean(values)],
        color=neutral,
        linewidth=1.5,
        zorder=3,
    )
axes[0].set_xticks(x, [LABELS[c] for c in CONDITIONS])
plt.setp(axes[0].get_xticklabels(), rotation=25, ha="right")
axes[0].set_ylabel("Reference-matched attention TV")
axes[0].set_title("A  Routing distortion and geometry", loc="left")
axes[0].grid(axis="y", color=grid, linewidth=0.5)
axes[0].set_axisbelow(True)

# B: post-hoc query-group decomposition.
query_names = ["target_region", "target_other_sample", "text"]
query_labels = ["car", "other target", "text"]
matrix = np.asarray(
    [[summary[c]["by_query"][q] for q in query_names] for c in CONDITIONS]
)
image = axes[1].imshow(matrix, cmap="magma", vmin=0, vmax=matrix.max())
axes[1].set_xticks(range(3), query_labels, rotation=25, ha="right")
axes[1].set_yticks(range(len(CONDITIONS)), [LABELS[c] for c in CONDITIONS])
axes[1].set_title("B  Distortion by query group", loc="left")
for row in range(matrix.shape[0]):
    for column in range(matrix.shape[1]):
        red, green, blue, _ = image.cmap(image.norm(matrix[row, column]))
        luminance = 0.299 * red + 0.587 * green + 0.114 * blue
        axes[1].text(
            column,
            row,
            f"{matrix[row, column]:.3f}",
            ha="center",
            va="center",
            color="black" if luminance > 0.58 else "white",
            fontsize=5.5,
        )
colorbar = figure.colorbar(image, ax=axes[1], fraction=0.045, pad=0.03)
colorbar.ax.tick_params(labelsize=5.6)

# C: post-hoc layer decomposition.
layers = [7, 12, 24, 48, 59]
for condition in CONDITIONS:
    values = [summary[condition]["by_layer"][str(layer)] for layer in layers]
    color = coherent_color if COHERENT[condition] else incoherent_color
    axes[2].plot(
        layers,
        values,
        marker="o",
        markersize=2.4,
        linewidth=1.0,
        color=color,
        linestyle="-" if "transplant" in condition else "--",
        alpha=0.9,
        label=LABELS[condition],
    )
axes[2].set_xlabel("Layer")
axes[2].set_ylabel("Mean attention TV")
axes[2].set_xticks(layers)
axes[2].set_title("C  Distortion by layer", loc="left")
axes[2].grid(color=grid, linewidth=0.5)
axes[2].legend(
    fontsize=5.0,
    frameon=False,
    ncol=3,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.22),
    columnspacing=0.8,
    handlelength=1.7,
)

figure.tight_layout(rect=(0, 0.10, 1, 1), w_pad=1.0)
figure.savefig(OUT_DIR / "fig20_attention_conservation.pdf", bbox_inches="tight")
figure.savefig(OUT_DIR / "fig20_attention_conservation.png", dpi=240, bbox_inches="tight")
print("wrote fig20_attention_conservation.{pdf,png}")
