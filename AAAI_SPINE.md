# AAAI-27 投稿脊柱决策 (spine lock)

目标: AAAI-27 主赛道, double-blind, 正文 7 页硬上限，主 PDF 最多另含 2 页 references。
当前 `main_aaai.pdf` 共 8 页，技术内容与 Conclusion 均止于第 7 页，References 从第 7 页底部延续至第 8 页。
Supplementary 独立 PDF (审稿人无义务读 → 主线每个数字必须正文自证)。
Reproducibility Checklist 不计入正文页数且需**独立提交**(不合并进 main PDF, 2026-07-14 修正,
见 `AAAI_HANDOFF.md` §1/§5)。
时间状态（2026-07-22）: abstract 截止 2026-07-21 AoE 已过；full paper 截止
2026-07-28 AoE；supplement/code 截止 2026-07-31 AoE。

## 单一最强贡献 (the one line reviewers should remember)
**"我们造了面向扩散图像编辑器的 layer--time / tuned lens,并发现:编辑不是逐步显影,而是
*结果早可预测、代码晚翻译*——在靠近栈顶一条锐利(~1 层)、时间步不变、且在测试的
Qwen 谱系 checkpoint 中复现的
L52-54 带里,才把内部目标图像码翻译成绘制用的速度场。读数与 transplant / steer
干预相互校验，并导出免训练杠杆。"**

## 脊柱 (spine) — 决定谁留正文的判据: 对头条 claim 是否 load-bearing
1. **Instrument**: layer-time tuned-lens + 冻结头 logit-lens 类比 + 三因果原语
   (ablation / transplant / steer)。这是使一切可见的仪器。[method, ~1.5pp]
2. **When — predictable early**: 编辑结果 L6 即线性可读 (cross-seed probe 0.88),
   而冻结头到 L48-54 才可读。头号反直觉。[result, 脊柱]
3. **Translate late — two codes**: 大半栈携带线性可读的目标图像码,在 L52-54
   锐带 (transition width ≤1 层, 四变体解码确认) 翻译成速度码。[result, 脊柱]
4. **三解离 (深化脊柱, 很可能是最新颖点)**: 可读 ≠ 因果必要 ≠ 线性可写——
   三种不同的解离,各自定位。[result, 深化]
5. **测试范围内的外部效度**: L52-54 邻域在测试 edit families、独立 fine-tune
   (FireRed) 与 4 步蒸馏 (Rapid-AIO) 中复现；不外推到无关架构。[defense]
6. **应用 (so-what)**: CFG 截断 step 2 后省 45% forward passes；另以单栏图保留
   15%-NFE differential preview，展示机制可直接用于候选编辑预览。[so-what]

## 下沉 supplementary (独立 PDF)
tuned-lens 完整推导 · differential lens 全量电池 · **C21-C28 迁移梯/
σ-索引/非线性容量曲线全链** · recompose 完整剂量梯 · rank-ladder
物体身份 shells · 全 20-case battery · massive-activations 方法学警示 ·
mask-steer 免 donor 杠杆 · saliency 修复 · 4 处自纠错完整叙事。

## Blocking pass: DEANONYMIZE
scrub 掉: yata-image-publics.flowgpt.com / R2 bucket 名 / 任何 GitHub / "we release
at <url>" / showcase 页引用 → 全部 "anonymized" 或 "released upon acceptance"。
确认 AAAI-27 主赛道 double-blind (提交说明) + [submission] 模式加行号/隐作者块。

## 图预算（当前 7 张；仅 method framework 跨栏）
- Fig1 teaser：单栏，五阶段主线
- Fig2 method：唯一跨栏图，lens + 三原语 schematic
- Fig3 mechanism：单栏，早期 probe 与 decode convention
- Fig4 boundary：单栏，L52--54 锐边界
- Fig5 tuned lens：单栏，内部图像与 anti-image
- Fig6 carrier：单栏，bbox 失败 vs silhouette 成功
- Fig7 preview：单栏，15%-NFE differential preview

---

## 当前摘要口径

以下不再维护独立 draft；权威文本是 `main_aaai.tex` 的 `abstract`。摘要必须使用
“predictable early”，不能写成 irreversible decision/commitment；Boogu 只支持
prediction/selection，不支持 Qwen 的 translation mechanism。

## 历史 AAAI 摘要 draft v1（仅留档）

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
