# AAAI-27 投稿脊柱决策 (spine lock)

目标: AAAI-27 主赛道, double-blind, 正文 7 页硬上限 (references 不计入、可另起页数不限长度,
当前 1 页, 现总 8pp), supplementary 独立 PDF (审稿人无义务读 → 主线每个数字必须正文自证)。
Reproducibility Checklist 不计入正文页数且需**独立提交**(不合并进 main PDF, 2026-07-14 修正,
见 AAAI_HANDOFF.md §4 坑 1)。
截止: abstract 2026-07-21 AoE / full paper 2026-07-28 AoE。

## 单一最强贡献 (the one line reviewers should remember)
**"我们造了第一个面向扩散图像编辑器的 tuned-lens,用它证明:编辑不是逐步显影,而是
*决定得早、翻译得晚*——在靠近栈顶一条锐利(~1 层)、时间步不变、且跨模型通用的
L52-54 带里,才把内部目标图像码翻译成绘制用的速度场。因为读数是因果的,它们直接
变成免训练杠杆。"**

## 脊柱 (spine) — 决定谁留正文的判据: 对头条 claim 是否 load-bearing
1. **Instrument**: layer-time tuned-lens + 冻结头 logit-lens 类比 + 三因果原语
   (ablation / transplant / steer)。这是使一切可见的仪器。[method, ~1.5pp]
2. **When — decided early**: 编辑 L6 即线性可读 (cross-seed probe 0.88),
   而冻结头到 L48-54 才可读。头号反直觉。[result, 脊柱]
3. **Translate late — two codes**: 大半栈携带线性可读的目标图像码,在 L52-54
   锐带 (transition width ≤1 层, 四变体解码确认) 翻译成速度码。[result, 脊柱]
4. **三解离 (深化脊柱, 很可能是最新颖点)**: 可读 ≠ 因果必要 ≠ 线性可写——
   三种不同的解离,各自定位。[result, 深化]
5. **普适 (回应最大质疑=外部效度)**: L52-54 边界 edit-family 通用 + 独立
   fine-tune (FireRed) + 4 步蒸馏 (Rapid-AIO) 复现。压成 2 段 + 1 图。[defense]
6. **应用 (so-what)**: 只留最干净的一个——CFG 截断 step 2 后省 45% forward passes,
   四类编辑视觉完好 (CFG 真作用=范围解析非决定编辑)。其余杠杆进 supp。[so-what]

## 下沉 supplementary (独立 PDF)
tuned-lens 完整推导 · differential lens · 15%-NFE preview · **C21-C28 迁移梯/
σ-索引/非线性容量曲线全链** · recompose (masks are the carrier) · rank-ladder
物体身份 shells · 全 20-case battery · massive-activations 方法学警示 ·
mask-steer 免 donor 杠杆 · saliency 修复 · 4 处自纠错完整叙事。

## Blocking pass: DEANONYMIZE
scrub 掉: yata-image-publics.flowgpt.com / R2 bucket 名 / 任何 GitHub / "we release
at <url>" / showcase 页引用 → 全部 "anonymized" 或 "released upon acceptance"。
确认 AAAI-27 主赛道 double-blind (提交说明) + [submission] 模式加行号/隐作者块。

## 图预算 (正文最多 4-5 张; 选进正文的 2-3MB PNG 转 PDF/压 JPEG)
- Fig1 teaser (layer-time grid + 五阶段回路)
- Fig2 method (lens + 三原语 schematic)
- Fig3 tuned-lens 渲染内部图像 + L52-54 边界 (可能合并 depth/mechanism)
- Fig4 三解离 or 跨模型边界一致
- (应用小图可并入或进 supp)

---

## AAAI 摘要 draft v1 (~185 词, 一条脊柱)

Between reading "turn the car red" and painting it, what does a diffusion image
editor do? The mechanics suggest gradual development -- sixty transformer blocks
times twenty denoising steps, the edit surfacing progressively like a photograph
in developer fluid. We show this picture is wrong in a measurable way. We build
the first tuned lens for a diffusion-transformer (DiT) image editor, decoding
intermediate residual streams through the model's own frozen output head, and
pair every passive reading with causal interventions -- ablation, transplant,
and steering. The editor thinks with an internal image: the edit is *decided
early* -- linearly readable by layer 6, where the frozen head still reads
noise -- and only *translated late*, in a sharp, timestep-invariant band
(layers 52--54 of 60, transition width as narrow as one layer) from an internal
target-image code into the flow field that paints it. This translation boundary
is edit-family universal and survives an independently fine-tuned checkpoint and
a four-step distilled model. Readability, causal necessity, and linear
writability dissociate three distinct ways, and we map exactly where. Because the
readings are causal, they convert into training-free levers -- including
truncating classifier-free guidance after step two for a 45% compute saving with
all edit families visually intact.
