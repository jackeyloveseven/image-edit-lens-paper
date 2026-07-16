"""Fig 17 (K7): Rapid-AIO L52 decode ladder under the sigma-matched
three-rung translator dictionary. Rows = which dictionary rung produced
the decode (L0 frozen Qwen-Image-Edit-2511 / L1 recalibrated / L2
Rapid-AIO-native refit); columns = Rapid-AIO's four sampling steps
t0-t3. Panel a: car_red. Panel b: style_ink. Per-cell text is the
held-out velocity-space R^2 for that rung/step; red flags a negative
score. Both panels only fail visually and numerically in the
coverage-edge final column (t3, sigma=0.02) -- the sigma-keying law's
boundary made visible, not just tabulated."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

RED = "#C2402A"
GRAY_D = "#444444"

ROOT = "/home/ubuntu/chengyanli/image-edit-lens"
RUN = f"{ROOT}/runs/k7_rapid_ladder"

d = json.load(open(f"{RUN}/summary.json"))
cases = d["cases"]

rungs = ["L0_sigma", "L1", "L2"]
rung_labels = ["L0 frozen", "L1 recal.", "L2 native"]
steps = [0, 1, 2, 3]

fig = plt.figure(figsize=(7.0, 3.15))
gs = fig.add_gridspec(1, 2, wspace=0.11, left=0.05, right=0.985,
                       top=0.84, bottom=0.02)

for panel_idx, (case, letter, title) in enumerate(
        zip(["car_red", "style_ink"], "ab", ["car_red", "style_ink"])):
    r2 = cases[case]["test_r2"]
    gsP = gs[0, panel_idx].subgridspec(len(rungs), len(steps),
                                        wspace=0.04, hspace=0.07)
    for ridx, rung in enumerate(rungs):
        for cidx, step in enumerate(steps):
            ax = fig.add_subplot(gsP[ridx, cidx])
            img = Image.open(f"{RUN}/cells/{case}_{rung}_L52_t{step}.png")
            ax.imshow(img)
            ax.set_xticks([]); ax.set_yticks([])
            flagged = cidx == len(steps) - 1
            for s in ax.spines.values():
                s.set_visible(flagged)
                s.set_color(RED)
                s.set_linewidth(1.3)
            val = r2[rung][f"L52_t{step}"]
            color = RED if val < 0 else "white"
            ax.text(0.96, 0.05, f"{val:.2f}", transform=ax.transAxes,
                     fontsize=6.0, color=color, ha="right", va="bottom",
                     fontweight="bold" if val < 0 else "normal",
                     bbox=dict(boxstyle="round,pad=0.10", facecolor="black",
                               edgecolor="none", alpha=0.55))
            if ridx == 0:
                ax.set_title(f"t{step}", fontsize=8, color=GRAY_D, pad=3)
            if cidx == 0:
                ax.set_ylabel(rung_labels[ridx], fontsize=7.0, color=GRAY_D)
    fig.text(0.255 + panel_idx * 0.495, 0.965, title, fontsize=9.5,
              ha="center", style="italic", color=GRAY_D)
    fig.text(0.045 + panel_idx * 0.495, 0.985, letter, fontsize=10.5,
              fontweight="bold")

fig.text(0.5, 0.905,
          "coverage-edge column (t3, σ=0.02) outlined in red — "
          "the only column where decode and R² both degrade",
          fontsize=7.0, color=RED, ha="center")

out = f"{ROOT}/paper/figs/fig17_k7_ladder.png"
fig.savefig(out, dpi=420, bbox_inches="tight")
plt.close(fig)
print("wrote", out)
