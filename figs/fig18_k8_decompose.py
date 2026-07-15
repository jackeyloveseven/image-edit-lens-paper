"""Fig 18 (K8): decomposing K7's terminal-step collapse into a coverage
cause and an intrinsic-decodability cause. Panel a (Q1): as the
borrowed frozen Qwen-Image-Edit-2511 dictionary entry's sigma closes in
on Rapid-AIO's terminal sigma=0.02, zero-shot R^2 at Rapid t3 rises
monotonically toward each case/layer's native-refit ceiling (dotted) --
a coverage gap, not a transfer breakdown. Panel b (Q2): Qwen's own
held-out native refit, with zero cross-model shift, collapses at the
same terminal step for L52/L56 while L59 stays at ~0.99 -- a
model-independent loss of decodability."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RED_D, RED_M, RED_L = "#8E2A18", "#C2402A", "#E2967F"     # car_red, L52/L56/L59
TEAL_D, TEAL_M, TEAL_L = "#0A5A66", "#0F8FA0", "#7FC3CC"   # style_ink, L52/L56/L59
GRAY_D = "#444444"
GRAY_M = "#999999"

ROOT = "/home/ubuntu/chengyanli/image-edit-lens"
RUN = f"{ROOT}/runs/k8_sigma_coverage"
d = json.load(open(f"{RUN}/summary.json"))

deep_layers = [52, 56, 59]
cases = ["car_red", "style_ink"]
case_colors = {"car_red": (RED_L, RED_M, RED_D), "style_ink": (TEAL_L, TEAL_M, TEAL_D)}
markers = {52: "o", 56: "s", 59: "^"}

fig, (axA, axB) = plt.subplots(1, 2, figsize=(7.0, 2.55))

# ---- Panel a: Q1 dose-response ----
dict_steps = [16, 17, 18, 19]
sigma_gap = {16: 0.26, 17: 0.18, 18: 0.09, 19: 0.00}
xs = list(range(len(dict_steps)))
for case in cases:
    tbl = d["t3_scoring_table"][case]
    colors = case_colors[case]
    for li, layer in enumerate(deep_layers):
        key = f"L{layer}_t3"
        row = tbl["scores"][key]
        ys = [row["L0_old16"], row["L0_new17"], row["L0_new18"], row["L0_new19"]]
        ceiling = row["L2_rapid"]
        axA.plot(xs, ys, color=colors[li], marker=markers[layer], markersize=4.2,
                  linewidth=1.3, label=f"{case} L{layer}")
        axA.axhline(ceiling, color=colors[li], linestyle=":", linewidth=0.9, alpha=0.75,
                     xmin=0.86, xmax=1.0)
axA.axhline(0, color=GRAY_M, linewidth=0.7, zorder=0)
axA.set_xticks(xs)
axA.set_xticklabels([f"t{s}\n(Δσ≈{sigma_gap[s]:.2f})" for s in dict_steps], fontsize=6.6)
axA.set_ylabel(r"$R^2$ at Rapid $t{=}3$", fontsize=8.5)
axA.set_title("Q1: dose-response as coverage gap closes", fontsize=8.3, color=GRAY_D)
axA.tick_params(labelsize=7.5)
for spine in ["top", "right"]:
    axA.spines[spine].set_visible(False)

# ---- Panel b: Q2 native held-out collapse ----
steps16_19 = [16, 17, 18, 19]
xsB = list(range(len(steps16_19)))
for case in cases:
    q2 = d["q2_native_heldout_r2"][case]
    colors = case_colors[case]
    for li, layer in enumerate(deep_layers):
        ys = [q2[f"L{layer}_t{s}"] for s in steps16_19]
        axB.plot(xsB, ys, color=colors[li], marker=markers[layer], markersize=4.2,
                  linewidth=1.3, label=f"L{layer}")
axB.set_xticks(xsB)
axB.set_xticklabels([f"t{s}" for s in steps16_19], fontsize=7.5)
axB.set_ylabel(r"native held-out $R^2$", fontsize=8.5)
axB.set_title("Q2: Qwen-native collapse, zero cross-model shift", fontsize=8.3, color=GRAY_D)
axB.tick_params(labelsize=7.5)
axB.set_ylim(-0.05, 1.05)
for spine in ["top", "right"]:
    axB.spines[spine].set_visible(False)
axB.annotate("L59 stays\nnear-perfect", xy=(3, 0.99), xytext=(1.3, 0.55),
              fontsize=6.6, color=GRAY_D, ha="center",
              arrowprops=dict(arrowstyle="-|>", color=GRAY_D, linewidth=0.8))
axB.annotate("L52/L56 collapse\nat the terminal step",
              xy=(3, 0.63), xytext=(1.3, 0.18),
              fontsize=6.6, color=RED_M, ha="center",
              arrowprops=dict(arrowstyle="-|>", color=RED_M, linewidth=0.8))

# ---- shared legend (case x layer, 6 entries) ----
handles = []
labels = []
for case in cases:
    colors = case_colors[case]
    for li, layer in enumerate(deep_layers):
        h, = axA.plot([], [], color=colors[li], marker=markers[layer], markersize=4.2, linewidth=1.3)
        handles.append(h)
        labels.append(f"{case} L{layer}")
fig.legend(handles, labels, ncol=6, fontsize=6.3, frameon=False,
           loc="lower center", bbox_to_anchor=(0.5, -0.03), handlelength=1.6,
           columnspacing=0.9, handletextpad=0.4)

for ax, letter in zip([axA, axB], "ab"):
    ax.text(-0.13, 1.10, letter, transform=ax.transAxes, fontsize=10, fontweight="bold")

fig.tight_layout(rect=[0, 0.06, 1, 1])
out = f"{ROOT}/paper/figs/fig18_k8_decompose.png"
fig.savefig(out, dpi=400, bbox_inches="tight")
plt.close(fig)
print("wrote", out)
