"""Fig 10 (G2): dense L44-59 sweep sharpening the depth-lens snap zone
(Fig 4/5) to a timestep-invariant crossover. Panel A: standard decode (A,
solid) vs. v-as-x0 decode (C, dashed) CLIP score by layer, t=4 and t=16 --
the crossover. Panel B: cosine similarity of the intermediate pseudo-
velocity to the terminal v_59, same layers/steps. Panel C: dense cross-seed
probe accuracy by layer -- flat through L58, drops only at L59."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RED = "#C2402A"
TEAL = "#0F8FA0"
GRAY_D = "#444444"
GRAY_M = "#999999"

ROOT = "/home/ubuntu/chengyanli/image-edit-lens"
b = json.load(open(f"{ROOT}/runs/g2_boundary/boundary_summary.json"))
layers = b["layers"]
steps = ["4", "16"]
colors = {"4": TEAL, "16": RED}

fig, axes = plt.subplots(1, 3, figsize=(6.9, 2.35))

# ---- Panel A: A-vs-C crossover ----
axA = axes[0]
for t in steps:
    d = b["per_step"][t]
    axA.plot(layers, d["P_A"], color=colors[t], marker="o", markersize=3.4,
              linewidth=1.5, label=f"A ($x_0{{=}}x_t{{-}}\\sigma v_\\ell$), t{t}")
    axA.plot(layers, d["P_C"], color=colors[t], marker="s", markersize=3.4,
              linewidth=1.3, linestyle="--", alpha=0.75,
              label=f"C ($v_\\ell$ as $x_0$), t{t}")
    axA.axvline(d["crossover_midpoint_layer"], color=colors[t], linewidth=0.9,
                linestyle=":", alpha=0.8)
axA.set_xlabel("layer", fontsize=8.5)
axA.set_ylabel("CLIP P(\"a red car\"), car bbox", fontsize=8)
axA.legend(fontsize=5.4, frameon=False, loc="center left", handlelength=1.5, labelspacing=0.25)
axA.set_title("A/C crossover", fontsize=9, color=GRAY_D)
axA.tick_params(labelsize=7.5)
for spine in ["top", "right"]:
    axA.spines[spine].set_visible(False)

# ---- Panel B: cosine to v59 ----
axB = axes[1]
for t in steps:
    d = b["per_step"][t]
    axB.plot(layers, d["cos_v59"], color=colors[t], marker="o", markersize=3.4,
              linewidth=1.6, label=f"t={t}")
axB.set_xlabel("layer", fontsize=8.5)
axB.set_ylabel(r"cos($v_\ell$, $v_{59}$)", fontsize=8.5)
axB.legend(fontsize=7, frameon=False, loc="lower right", handlelength=1.5)
axB.set_title(r"cos($v_\ell$, $v_{59}$)", fontsize=9, color=GRAY_D)
axB.tick_params(labelsize=7.5)
for spine in ["top", "right"]:
    axB.spines[spine].set_visible(False)

# ---- Panel C: dense probe accuracy ----
axC = axes[2]
for t in steps:
    d = b["per_step"][t]
    axC.plot(layers, d["probe_accuracy"], color=colors[t], marker="o",
              markersize=3.4, linewidth=1.6, label=f"t={t}")
axC.axhline(1.0 / 3, color=GRAY_M, linewidth=0.9, linestyle="--", label="chance")
axC.set_xlabel("layer", fontsize=8.5)
axC.set_ylabel("cross-seed probe acc.", fontsize=8.5)
axC.set_ylim(0.3, 0.95)
axC.legend(fontsize=7, frameon=False, loc="lower left", handlelength=1.5)
axC.set_title("probe accuracy", fontsize=9, color=GRAY_D)
axC.tick_params(labelsize=7.5)
for spine in ["top", "right"]:
    axC.spines[spine].set_visible(False)

for ax, letter in zip(axes, "ABC"):
    ax.text(-0.15, 1.05, letter, transform=ax.transAxes, fontsize=10, fontweight="bold")

fig.tight_layout()
fig.savefig(f"{ROOT}/paper/figs/fig10_boundary.pdf", bbox_inches="tight")
print("wrote fig10_boundary.pdf")
print("midpoints:", {t: b["per_step"][t]["crossover_midpoint_layer"] for t in steps})
print("shift:", b["midpoint_shift_t4_to_t16"])
