"""Fig 8 (appendix): Panel A onset curves (IoU vs final mask) for the 6
non-global-edit E2 cases, add_boat highlighted as the one delayed-onset case.
Panel B: cropped boat storyboard (existing rendered reference figure, title
banner trimmed)."""
import json
import os
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["ps.fonttype"] = 42
import matplotlib.pyplot as plt
from PIL import Image

RED = "#C2402A"
GRAY_D = "#444444"
GRAY_M = "#999999"

ROOT = Path(os.environ.get(
    "IMAGE_EDIT_LENS_ROOT",
    Path(__file__).resolve().parents[3] / "image-edit-lens",
))
OUT_DIR = Path(__file__).resolve().parent
e2 = json.load(open(ROOT / "runs" / "e2_revision" / "summary.json"))

non_global = ["add_boat", "add_latte", "color_car", "color_cup", "remove_cup", "remove_laptop"]

fig = plt.figure(figsize=(6.9, 5.1))
gs = fig.add_gridspec(2, 1, height_ratios=[1.05, 1.0], hspace=0.42,
                       left=0.09, right=0.99, top=0.94, bottom=0.06)

axA = fig.add_subplot(gs[0, 0])
for c in non_global:
    v = e2["cases"][c]
    steps = [p["t"] for p in v["per_step"]]
    ious = [p["iou_vs_final"] for p in v["per_step"]]
    if c == "add_boat":
        axA.plot(steps, ious, color=RED, linewidth=2.4, marker="o", markersize=4, label="add boat", zorder=10)
    else:
        axA.plot(steps, ious, color=GRAY_M, linewidth=1.1, marker="o", markersize=2.6, zorder=3,
                  label=c.replace("_", " "))
axA.set_xlabel("denoising step", fontsize=9.5)
axA.set_ylabel("IoU vs final mask", fontsize=9.5)
axA.set_ylim(-0.03, 1.05)
axA.legend(fontsize=6.8, frameon=False, loc="lower right", ncol=2, handlelength=1.5, labelspacing=0.3)
axA.set_title("onset curves", fontsize=9.5, color=GRAY_D)
for spine in ["top", "right"]:
    axA.spines[spine].set_visible(False)
axA.tick_params(labelsize=8.5)

axB = fig.add_subplot(gs[1, 0])
img = Image.open(ROOT / "runs" / "e2_revision" / "boat_storyboard.png")
w, h = img.size
crop = img.crop((0, int(h * 0.135), w, h))
axB.imshow(crop)
axB.set_xticks([]); axB.set_yticks([])
for s in axB.spines.values():
    s.set_visible(False)
axB.set_title("add-boat storyboard", fontsize=9.5,
               color=GRAY_D, pad=8)

fig.savefig(OUT_DIR / "fig8_appendix.pdf", bbox_inches="tight")
print("wrote fig8_appendix.pdf")
