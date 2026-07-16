import json, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

root = "/home/ubuntu/chengyanli/image-edit-lens"
RED = "#C2402A"
TEAL = "#0F8FA0"

plt.rcParams.update({
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#333333",
})

a3 = json.load(open(f"{root}/runs/a3_summary.json"))["results"]
a4 = json.load(open(f"{root}/runs/a4_summary.json"))["results"]

def get(scan, case, cond):
    for r in a3:
        if r["scan"] == scan and r["case"] == case and r["condition"] == cond:
            return r["edit_success"]
    raise KeyError((scan, case, cond))

layer_bands = ["L0_11", "L12_23", "L24_35", "L36_47", "L48_59"]
layer_labels = ["0-11", "12-23", "24-35", "36-47", "48-59"]
car_layer = [get("layerwindow", "car_red", c) for c in layer_bands]
beach_layer = [get("layerwindow", "beach_background", c) for c in layer_bands]

step_conds = ["steps_0_3", "steps_4_9", "steps_10_15", "steps_16_19", "steps_0_19"]
step_labels = ["0-3", "4-9", "10-15", "16-19", "all"]
car_step = [get("stepwindow", "car_red", c) for c in step_conds]
beach_step = [get("stepwindow", "beach_background", c) for c in step_conds]

swap_conds = ["control_no_swap", "swap_L0_11", "swap_L12_23", "swap_L0_23", "swap_L48_59"]
swap_labels = ["ctrl", "L0-11", "L12-23", "L0-23", "L48-59"]
swap_vals = []
for r in a4:
    if r["condition"] in swap_conds:
        swap_vals.append((r["condition"], r["scores"]["a red car"]))
swap_vals = [dict(swap_vals)[c] for c in swap_conds]

fig, axes = plt.subplots(1, 3, figsize=(6.9, 2.3), constrained_layout=True)

def grouped_bars(ax, labels, v1, v2, ylabel, xlab):
    x = np.arange(len(labels))
    w = 0.36
    ax.bar(x - w/2, v1, width=w, color=RED, label="car")
    ax.bar(x + w/2, v2, width=w, color=TEAL, label="beach")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=7, rotation=35, ha="right")
    ax.set_ylim(0, 1.05)
    ax.axhline(0.5, color="#CCCCCC", linewidth=0.7, zorder=0)
    ax.set_ylabel(ylabel, fontsize=8)
    ax.set_xlabel(xlab, fontsize=8)
    ax.set_axisbelow(True)

grouped_bars(axes[0], layer_labels, car_layer, beach_layer, "edit success", "layer band ablated")
axes[0].legend(loc="upper left", fontsize=6.5, frameon=False, handlelength=1.2)

grouped_bars(axes[1], step_labels, car_step, beach_step, "edit success", "step window ablated")

x = np.arange(len(swap_labels))
axes[2].bar(x, swap_vals, width=0.55, color=RED)
axes[2].set_xticks(x)
axes[2].set_xticklabels(swap_labels, fontsize=7, rotation=35, ha="right")
axes[2].set_ylim(0, 1.05)
axes[2].axhline(0.5, color="#CCCCCC", linewidth=0.7, zorder=0)
axes[2].set_ylabel("P(red car)", fontsize=8)
axes[2].set_xlabel("donor layers transplanted", fontsize=8)
axes[2].set_axisbelow(True)

for ax, letter in zip(axes, "ABC"):
    ax.text(-0.12, 1.05, letter, transform=ax.transAxes, fontsize=10, fontweight="bold")

fig.savefig(f"{root}/paper/figs/fig6_causality.pdf")
fig.savefig(f"{root}/paper/figs/fig6_causality.png", dpi=200)
print("saved fig6")
