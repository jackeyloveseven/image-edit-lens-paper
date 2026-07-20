import json, os, matplotlib
from pathlib import Path
matplotlib.use("Agg")
matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["ps.fonttype"] = 42
import matplotlib.pyplot as plt

RED = "#C2402A"
TEAL = "#0F8FA0"
GRAY_DARK = "#444444"
GRAY_MED = "#7A7A9A"

CASES = [
    ("add_boat", "object-addition", GRAY_DARK, "-"),
    ("add_latte", "object-addition", GRAY_DARK, "--"),
    ("bg_beach", "background-replacement", TEAL, "-"),
    ("bg_forest", "background-replacement", TEAL, "--"),
    ("color_car", "color-change", RED, "-"),
    ("color_cup", "color-change", RED, "--"),
    ("style_sketch", "style-transfer", GRAY_MED, "-"),
    ("style_watercolor", "style-transfer", GRAY_MED, "--"),
]

ROOT = Path(os.environ.get(
    "IMAGE_EDIT_LENS_ROOT",
    Path(__file__).resolve().parents[3] / "image-edit-lens",
))
OUT_DIR = Path(__file__).resolve().parent

plt.rcParams.update({
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#333333",
})

fig, ax = plt.subplots(figsize=(3.35, 2.6), constrained_layout=True)

seen_cat = set()
for case, cat, color, ls in CASES:
    d = json.load(open(ROOT / "runs" / f"a5_{case}" / "lens_grid.json"))
    cs = d["clip_scores"]
    if "raw" in cs:
        cs = cs["raw"]
    target = d["target_label"]
    steps = d["steps"]
    vals = [cs[f"l59_t{t}"][target] for t in steps]
    label = cat if cat not in seen_cat else None
    seen_cat.add(cat)
    ax.plot(steps, vals, color=color, linestyle=ls, marker="o", markersize=2.6,
            linewidth=1.4, label=label)

ax.set_xlabel("denoising step")
ax.set_ylabel("P(target) @ L59")
ax.set_ylim(-0.02, 1.02)
ax.set_xlim(-0.5, 19.5)
ax.grid(True, color="#DDDDDD", linewidth=0.6, zorder=0)
ax.set_axisbelow(True)

leg = ax.legend(loc="lower right", fontsize=6.3, frameon=False, handlelength=1.6,
                 labelspacing=0.3, borderaxespad=0.1)

ax.text(0.03, 0.06, "removal: CLIP unreliable\n(excluded)", transform=ax.transAxes,
        fontsize=6.0, color="#666666", ha="left", va="bottom")

fig.savefig(OUT_DIR / "fig3_commit_curves.pdf")
fig.savefig(OUT_DIR / "fig3_commit_curves.png", dpi=200)
print("saved fig3")
