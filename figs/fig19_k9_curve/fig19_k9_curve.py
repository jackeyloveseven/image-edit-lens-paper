"""Fig 19 (K9): a nested learning curve isolates intrinsic nonlinearity
from fit capacity. Panel a: held-out R^2 at the terminal, collapsed
step (t19, solid) vs. nested training-case count N, the step16 healthy
control at the same N (dashed, same case/layer colors), and the t19
train-val R^2 (dash-dot, layer-aggregate, no case split) -- train-val
plateaus at ~0.80 (L52) / ~0.90 (L56) invariant to N, an expressivity
ceiling rather than undersampling, while step16 stays uniformly high
and flat, showing the collapse is step-specific. Panel b:
composition-swap control -- held-out R^2 under two independent case
orderings at matched N (N6 vs. N6', N9 vs. N9') agree closely,
confirming the N=3->6 rise tracks case count, not which cases were
added."""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RED_D, RED_M, RED_L = "#8E2A18", "#C2402A", "#E2967F"
TEAL_D, TEAL_M, TEAL_L = "#0A5A66", "#0F8FA0", "#7FC3CC"
GRAY_D = "#444444"
GRAY_M = "#999999"

ROOT = "/home/ubuntu/chengyanli/image-edit-lens"
RUN = f"{ROOT}/runs/k9_capacity_curve"
d = json.load(open(f"{RUN}/summary.json"))
rpc = d["results_per_config"]

deep_layers = [52, 56, 59]
cases = ["car_red", "style_ink"]
case_colors = {"car_red": (RED_L, RED_M, RED_D), "style_ink": (TEAL_L, TEAL_M, TEAL_D)}
markers = {52: "o", 56: "s", 59: "^"}
layer_gray = {52: "#B8B8B8", 56: "#8A8A8A", 59: "#4D4D4D"}

fig = plt.figure(figsize=(7.0, 2.75))
gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1.0], wspace=0.30,
                       left=0.07, right=0.99, top=0.82, bottom=0.20)
axA = fig.add_subplot(gs[0, 0])
gsB = gs[0, 1].subgridspec(1, 2, wspace=0.08)
axB1 = fig.add_subplot(gsB[0, 0])
axB2 = fig.add_subplot(gsB[0, 1], sharey=axB1)

# ---- Panel a: nested learning curve, t19 held-out + train-val ceiling ----
main_cfgs = ["N3", "N6", "N9", "N12"]
Ns = [d["main_curve_n"][c] for c in main_cfgs]

for case in cases:
    colors = case_colors[case]
    for li, layer in enumerate(deep_layers):
        ys19 = [rpc[c]["held_out_r2"][case][f"L{layer}_t19"] for c in main_cfgs]
        axA.plot(Ns, ys19, color=colors[li], marker=markers[layer], markersize=4.3,
                  linewidth=1.3, zorder=3)
        ys16 = [rpc[c]["held_out_r2"][case][f"L{layer}_t16"] for c in main_cfgs]
        axA.plot(Ns, ys16, color=colors[li], marker=markers[layer], markersize=3.2,
                  linewidth=0.9, linestyle="--", alpha=0.55, zorder=1)

for li, layer in enumerate(deep_layers):
    ys = [rpc[c]["train_val_r2"][f"L{layer}_t19"] for c in main_cfgs]
    axA.plot(Ns, ys, color=layer_gray[layer], marker=markers[layer], markersize=3.0,
              linewidth=1.0, linestyle="-.", alpha=0.85, zorder=2)

axA.set_xticks(Ns)
axA.set_xlabel("N (nested training-case count)", fontsize=8.3)
axA.set_ylabel(r"$R^2$ at the terminal step ($t{=}19$)", fontsize=8.3)
axA.tick_params(labelsize=7.5)
axA.set_ylim(0.15, 1.02)
for spine in ["top", "right"]:
    axA.spines[spine].set_visible(False)
axA.axhspan(0.79, 0.83, color=GRAY_M, alpha=0.14, zorder=0)
axA.text(Ns[0], 0.185,
          "solid = t19 held-out   dashed = t16 control   dash-dot = t19 train-val (layer only)",
          fontsize=5.5, color=GRAY_D, ha="left", va="bottom")
axA.annotate("train-val ceiling\n≈0.80 (L52), flat in N", xy=(12, 0.805), xytext=(4.6, 0.34),
              fontsize=6.4, color=GRAY_D, ha="left",
              arrowprops=dict(arrowstyle="-|>", color=GRAY_D, linewidth=0.8))
axA.annotate("t16 control:\nhigh, flat in N", xy=(6, 0.965), xytext=(7.0, 0.63),
              fontsize=6.2, color=GRAY_D, ha="left", alpha=0.85,
              arrowprops=dict(arrowstyle="-|>", color=GRAY_D, linewidth=0.7, alpha=0.7))
axA.set_title("held-out (t19 vs. t16) vs. train-val ceiling", fontsize=8.2, color=GRAY_D)

# ---- Panel b: composition-swap control, two mini bar charts ----
cats = []
bar_colors = []
for case in cases:
    colors = case_colors[case]
    for li, layer in enumerate(deep_layers):
        cats.append(f"{'car' if case == 'car_red' else 'ink'}\nL{layer}")
        bar_colors.append(colors[li])
x = np.arange(len(cats))
w = 0.36

for ax, (cfg, cfgp), title in zip([axB1, axB2], [("N6", "N6p"), ("N9", "N9p")],
                                     ["N=6", "N=9"]):
    vals_a, vals_b = [], []
    for case in cases:
        for layer in deep_layers:
            vals_a.append(rpc[cfg]["held_out_r2"][case][f"L{layer}_t19"])
            vals_b.append(rpc[cfgp]["held_out_r2"][case][f"L{layer}_t19"])
    ax.bar(x - w / 2, vals_a, width=w, color=bar_colors, edgecolor="none", label="original order")
    ax.bar(x + w / 2, vals_b, width=w, color=bar_colors, edgecolor="white",
            linewidth=0.6, hatch="////", label="swapped order")
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=5.9)
    ax.set_ylim(0, 1.05)
    ax.tick_params(labelsize=7.2)
    ax.set_title(title, fontsize=7.6, color=GRAY_D)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

axB2.tick_params(labelleft=False)
axB1.set_ylabel(r"held-out $R^2$ ($t{=}19$)", fontsize=8.0)
handles = [plt.Rectangle((0, 0), 1, 1, facecolor=GRAY_M, edgecolor="none"),
           plt.Rectangle((0, 0), 1, 1, facecolor=GRAY_M, edgecolor="white", hatch="////")]
axB1.legend(handles, ["case order A", "case order B"], fontsize=5.8, frameon=False,
             loc="lower left", handlelength=1.3)
fig.text(0.735, 0.895, "composition swap (same N, different case order)",
          fontsize=8.5, color=GRAY_D, ha="center")

for ax, letter, xoff in zip([axA, axB1], "ab", [-0.13, -0.30]):
    ax.text(xoff, 1.08, letter, transform=ax.transAxes, fontsize=10, fontweight="bold")

out = f"{ROOT}/paper/figs/fig19_k9_curve.png"
fig.savefig(out, dpi=400, bbox_inches="tight")
plt.close(fig)
print("wrote", out)
