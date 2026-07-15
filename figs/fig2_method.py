"""Fig 2: method / anatomy diagram. Token layout -> 60-block stack with a
post-block capture tap -> two lens branches (depth lens: frozen head;
time lens: x0 decode) -> decode-then-CLIP readout. On-figure labels kept
short; full explanation lives in the caption."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from matplotlib.path import Path
import matplotlib.patches as mpatches

RED = "#C2402A"
TEAL = "#0F8FA0"
GRAY_D = "#444444"
GRAY_M = "#8A8A8A"
GRAY_L = "#DDDDDD"

ROOT = "/home/ubuntu/chengyanli/image-edit-lens"

fig, ax = plt.subplots(figsize=(7.05, 3.0))
ax.set_xlim(0, 100)
ax.set_ylim(0, 42)
ax.axis("off")


def box(x, y, w, h, text, fc="white", ec=GRAY_D, tcolor=GRAY_D, fs=7.6, lw=1.1, bold=False):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.35,rounding_size=1.2",
                        linewidth=lw, edgecolor=ec, facecolor=fc, zorder=3)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            color=tcolor, zorder=4, fontweight="bold" if bold else "normal")
    return p


def arrow(xy0, xy1, color=GRAY_D, lw=1.1, style="-|>", ls="-"):
    a = FancyArrowPatch(xy0, xy1, arrowstyle=style, mutation_scale=9,
                         color=color, linewidth=lw, linestyle=ls, zorder=2, clip_on=False)
    ax.add_patch(a)


# ---- 1. token layout (top strip) ----
ax.text(11, 39.5, "token layout", fontsize=8.6, ha="center", color=GRAY_D, fontweight="bold")
box(1, 33.5, 13, 4.6, "target\n(noisy)", fc=TEAL, tcolor="white", fs=7.2)
box(14.3, 33.5, 8, 4.6, "condition\n(t=0)", fc=GRAY_M, tcolor="white", fs=7.0)
ax.text(19.5, 31.4, "zero_cond_t", fontsize=6.2, color=GRAY_M, ha="center", style="italic")

arrow((9, 33.3), (9, 30.3), color=GRAY_D)

# ---- 2. block stack ----
stack_x, stack_w = 3, 17
stack_y0, stack_h = 3, 21
ax.add_patch(Rectangle((stack_x, stack_y0), stack_w, stack_h, facecolor="#F2F2F2",
                        edgecolor=GRAY_D, linewidth=1.1, zorder=1))
n_ticks = 6
for i in range(n_ticks):
    yy = stack_y0 + stack_h * i / (n_ticks - 1)
    ax.plot([stack_x, stack_x + stack_w], [yy, yy], color="white", linewidth=0.8, zorder=1.5)
ax.text(stack_x + stack_w / 2, stack_y0 + stack_h + 3.4, "60 blocks", fontsize=7.6,
        color=GRAY_D, ha="center")
ax.text(stack_x + stack_w / 2, stack_y0 - 1.6, "L0", fontsize=6.6, color=GRAY_M, ha="center")
ax.text(stack_x + stack_w / 2, stack_y0 + stack_h + 1.4, "L59", fontsize=6.6, color=GRAY_M, ha="center")

# tap point at a representative mid layer
tap_y = stack_y0 + stack_h * 0.42
ax.plot([stack_x + stack_w], [tap_y], marker="o", color=RED, markersize=5, zorder=5)
ax.text(stack_x + stack_w / 2, tap_y, "tap", fontsize=6.6, color=RED, ha="center", va="center",
        fontweight="bold", zorder=5,
        bbox=dict(boxstyle="round,pad=0.12", facecolor="white", edgecolor=RED, linewidth=0.8))
ax.text(stack_x + stack_w / 2, stack_y0 + 2.0, "post-block\nresidual", fontsize=6.0,
        color=GRAY_M, ha="center", style="italic")

# ---- 3. two lens branches ----
branch_x0 = stack_x + stack_w
depth_y = tap_y + 7.5
time_y = tap_y - 7.5

arrow((branch_x0, tap_y), (branch_x0 + 6, depth_y), color=TEAL)
arrow((branch_x0, tap_y), (branch_x0 + 6, time_y), color=GRAY_D)

box(branch_x0 + 6.3, depth_y - 2.2, 14, 4.4, "frozen head\n(depth lens)", fc=TEAL, tcolor="white", fs=6.8)
box(branch_x0 + 6.3, time_y - 2.2, 14, 4.4, "x0 = xt - sigma*v\n(time lens)", fc="white",
    ec=GRAY_D, tcolor=GRAY_D, fs=6.5)

arrow((branch_x0 + 20.3, depth_y), (branch_x0 + 27, depth_y), color=TEAL)
arrow((branch_x0 + 20.3, time_y), (branch_x0 + 27, time_y), color=GRAY_D)

decode_x = branch_x0 + 27.3
box(decode_x, depth_y - 2.2, 12.5, 4.4, "decode", fc="white", ec=TEAL, tcolor=GRAY_D, fs=7.0)
box(decode_x, time_y - 2.2, 12.5, 4.4, "decode", fc="white", ec=GRAY_D, tcolor=GRAY_D, fs=7.0)

arrow((decode_x + 12.5, depth_y), (decode_x + 12.5 + 6.2, (depth_y + time_y) / 2 + 1.2), color=TEAL)
arrow((decode_x + 12.5, time_y), (decode_x + 12.5 + 6.2, (depth_y + time_y) / 2 - 1.2), color=GRAY_D)

readout_x = decode_x + 12.5 + 6.5
box(readout_x, (depth_y + time_y) / 2 - 3.0, 14, 6.0, "CLIP\nreadout", fc=RED, tcolor="white", fs=8.0, bold=True)

ax.text((branch_x0 + readout_x) / 2 + 7, depth_y + 4.6, "semantic readout", fontsize=8.0,
        color=GRAY_D, ha="center", fontweight="bold")

# ---- 4. CFG note (bottom-right small annotation) ----
ax.text(readout_x + 7, 6.0, "true CFG:\n2 passes", fontsize=6.4, color=GRAY_M,
        ha="center", style="italic",
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#F7F7F7", edgecolor=GRAY_L, linewidth=0.7))

fig.savefig(f"{ROOT}/paper/figs/fig2_method.pdf", bbox_inches="tight")
print("wrote fig2_method.pdf")
