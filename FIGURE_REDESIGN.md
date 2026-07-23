# 顶会级主图修改规范（除 pipeline）

面向 AAAI / CVPR 主会录用图标准。目标不是“好看一点”，而是：**扫一眼能复述 claim、版式可对齐、字体与色板可复用、打印/PDF 缩放后仍清晰**。

适用范围：`fig1_teaser`、`fig5_mechanism`、`fig10_boundary`、`fig12_tuned_lens`。  
**不含** `fig2_method`（pipeline）。

> **当前实现（2026-07-22，commit `5f917cb`）**：本文件是设计宪法和历史工单。
> 当前正文编号为 Fig1 teaser、Fig2 framework（唯一跨栏）、Fig3 mechanism、
> Fig4 boundary、Fig5 tuned lens、Fig6 carrier、Fig7 preview。本文覆盖的四张图
> 均已按单栏版式验收；技术内容与 Conclusion 止于第 7 页。

字号策略采用 **偏大气** 一档：面板标题接近正文（AAAI 正文 ≈10 pt），轴与刻度略小，避免挤爆双栏。

---

## 0. 总原则（四张图共用）

### 0.1 信息设计

- 每张图只服务 **1 个主 claim**；次要信息进 caption 或 supplement。
- 图注与图内标签 **不重复讲故事**：图内用短标签，caption 用完整句。
- 图内最小字号（热图格内数字等）≥ **7 pt**（PDF 矢量），保证双栏打印可读。

### 0.2 对称与网格

- 采用 **严格网格**：等宽面板、等边距、等圆角、等线宽。
- 标题基线、色条高度、面板字母位置 **全局对齐**。
- 禁止：半行留白、图例压数据、左右视觉重量差 > ~15%。

### 0.3 字体

- 统一嵌入 TrueType/OpenType（`pdf.fonttype = 42`，`ps.fonttype = 42`）。
- 推荐：**Source Sans 3** 或 **Helvetica Neue / Arial** 一族到底（标题 SemiBold，正文 Regular）。
- 数学符号与正文一致：`L52--54`、`v_\ell`、`\hat{x}_0` 用同一 math 风格。
- **禁止** Matplotlib 默认 DejaVu 混搭；禁止图内随意加粗/变色长标题。

#### 偏大气字号阶梯（相对 AAAI 正文 ~10 pt）

| 元素 | 字号 | 相对正文 |
|------|------|----------|
| 面板标题（`A Short title`） | **10 pt** | 与正文齐 |
| 轴标题 | **9 pt** | 略小 |
| 刻度 / 色条刻度 | **7.5–8 pt** | 明显更小 |
| 热图格内数字 / micro-label | **≥ 7 pt** | 下限 |
| 图注 caption（LaTeX） | ~9 pt | 模板默认 |

### 0.4 色板（语义色，不是装饰色）

| Token | Hex | 语义（全文固定） |
|------|-----|------------------|
| Teal | `#0F8FA0` | target-image code / early readability |
| Red | `#C2402A` | translation / velocity / snap band |
| Ink | `#222222` | 主文字 |
| Mute | `#6B6B6B` | 次要标注 |
| Band | `#C2402A` @ 12–15% alpha | L52–54 翻译带 |
| Grid bg | `#F5F5F5` | 热图低值 |

色盲友好：热图用 **单色序或 teal→red 有限两端**，避免彩虹；线型用 **实线/虚线** 双编码，不只靠颜色。

### 0.5 面板字母与标题格式

- 统一：`A` `B` `C` 粗体，放在面板外左上 **同一相对坐标**（如 `(-0.08, 1.08)`）。
- 标题格式：`A Short claim title`（名词短语，≤4 词），不要散文句。

### 0.6 导出规格

- 主文图：矢量 PDF（曲线/坐标轴）；照片网格可用 PNG@300dpi 再嵌入。
- 线宽：轴 0.8–1.0 pt；强调框 1.5–2.0 pt；尽量不用网格线。
- 整图宽度：双栏大图 `≈0.92–0.95\textwidth`，单栏 `≈0.95\columnwidth`。

---

## 1. Figure 1 — Teaser（开篇总览）

### 1.1 角色

审稿人 10 秒内应读出：**early predict → late translate → five stages**。  
视觉摘要，不是四块拼贴。

### 1.2 当前差距

- 四栏宽度不均，左右视觉重量失衡。
- “snap”大红框与正文 “L52–54 translation” 用语不一致。
- 右栏阶段条与中栏热图 **无几何对应**。
- 字体/标题高度不齐，像内部实验图。

### 1.3 目标版式（推荐 3 栏对称）

```
| A  Edit example | B  Layer–time lens | C  Measured stages |
|  source → edited |  heatmap + band    |  5 equal steps     |
|     ~28%         |       ~40%         |       ~32%         |
```

三栏顶边齐、底边齐；外边距左右对称；整图高约 2.6–2.8"。

### 1.4 各栏规格

**A · Edit example**

- 两张 **同尺寸正方形** 并排：`source` → `edited`。
- 中间箭头 + 极小字 `edit`（Mute）。
- 标题同色同字号（Ink），不要 edited 单独变红。
- 底栏一行 micro-label：`car_red`（与全文 running example 绑定）。

**B · Layer–time lens（主视觉）**

- `layer × denoise step` 热图，接近正方形。
- 色条贴右，高度与矩阵齐。
- **用半透明带标 L52–54**，标签写 `translation`（不要写 “snap”）。
- 在 L6 行加细标记 `probe-readable`（小三角或侧标），表达 outcome early，与 frozen-head 晚可读区分。
- 色条标题：`P(red car)`。

**C · Measured stages（与正文逐字对齐）**

五个 **等宽等高** 圆角条，间距相等，自上而下：

1. Injection — `≤ L36`
2. Outcome prediction — `L6 / t2–4`
3. Target-image code — `L6–51`
4. Translation — `L52–54`
5. Output head — `L59`

- 颜色：Teal → Red 渐进，与热图语义一致。
- 可选：从 B 的 L52–54 带到 C 的 Translation 画一条极淡引导线（0.6 pt Mute）。

### 1.5 验收标准

- [x] 缩小到半栏宽仍能读出五阶段名
- [x] 不看正文也能说出 “early / late”
- [x] 无散文式长标题、无压数据标注

---

## 2. Figure 3 — Mechanism（两码错配 + 早可读）

文件：`figs/fig5_mechanism/`（正文 Figure 3）。

### 2.1 主 claim

**Frozen-head 解码约定在 L24/L59 翻转；probe 在 L6 已可读。**

### 2.2 当前差距

- 左右不等高、不等“方”。
- 标题是解释句（`sign flips…`），不够顶会。
- 2×4 小图间距/比例不严；数字角标风格不统一。

### 2.3 目标版式（左右同高）

```
| A Decode conventions (2×4) | B Probe accuracy (heatmap) |
|         ~55%               |            ~45%            |
```

### 2.4 规格

**A**

- 8 张 **严格正方形**，行列 gap 恒定。
- 列标题短齐：`A standard` · `B sign-flip` · `C v as x₀` · `D −v as x₀`。
- 行标签水平：`L24` / `L59`（不竖排）。
- 角标：统一白底 pill；`p>0.5 → Red`，否则 Ink。
- 行侧极小语义条：`L24 image-like` / `L59 velocity`（对应正文 two codes）。

**B**

- 与 A **同总高度**；单元格尽量接近方。
- 只强调一个 headline 格：`L6, t4`（红框 1.5–2 pt）。
- 标题：`B Early probe`；色条：`3-way probe acc.`。

### 2.5 验收标准

- [x] 左右顶边齐、色条不破坏对称
- [x] 读者能指出 “哪一格是 headline”
- [x] 打印后小图仍可辨车色（必要时略放大格）

---

## 3. Figure 4 — Boundary（翻译带）

文件：`figs/fig10_boundary/`（正文 Figure 4；supplement Figure 6）。

### 3.1 主 claim

**A/C 交叉、对齐 \(v_{59}\)、probe 平坦至 L58——同在 L52–54 邻域，且 timestep 不变。**

### 3.2 当前差距

- 三栏等宽是对的，但 A 图例过大、位置不统一。
- 缺少 **共享的 L52–54 band**（正文核心几何对象）。
- y 轴标题过长，破坏三栏视觉平衡。

### 3.3 目标版式（严格 1:1:1）

```
| A A/C crossover | B cos(vℓ, v59) | C Probe accuracy |
|_________________|________________|__________________|
          shared legend strip (centered under all three)
```

### 3.4 规格

- 三图共用 x：`layer ∈ [44, 59]`，相同 tick、spine、字体。
- **三图叠加同一浅 Red band：L52–54**（比多条竖虚线更干净、更对称）。
- 图例 **移出图外**：底部一条 `t=4` / `t=16` / `A solid` / `C dashed` / `chance`。
- A 的 y 轴缩短为 `CLIP P(red)`。
- 线宽统一；marker 统一圆点；C 用虚线区分约定。
- 面板题短齐：`A A/C crossover` · `B Alignment to v59` · `C Probe accuracy`。

### 3.5 验收标准

- [x] 三栏真正镜像对称（含标题/字母位置）
- [x] 不看 legend 位置也知道 band 是 translation
- [x] A 图数据区无大块遮挡

---

## 4. Figure 5 — Tuned lens（内部图像）

文件：`figs/fig12_tuned_lens/`（正文 Figure 5；supplement Figure 7）。

### 4.1 主 claim

**Mid-stack 是可读图像；frozen head 在同状态上读成 anti-image；tuned 还原 coherent scene。**

### 4.2 当前差距（相对顶会最严重）

- 上 5 下 3 + 右下空白：**不合格的非对称拼贴**。
- 像 raw dump，不像设计过的 figure。
- 标签弱，与 “anti-image / tuned / final” 叙事绑定不够。

### 4.3 目标版式（推荐 2×3，完全对称）

```
Row 1 (t = 0):   tuned L24 | tuned L36 | tuned L52
                 ← edit enters internal image →

Row 2 (t = 12):  raw L36 (anti-image) | tuned L36 | final output
                 ← head fails | lens succeeds | painted →
```

六格 **等大正方形**，等 gap，细灰边；标签统一在 **图上方**：`tuned · L36 · t0`。

- `raw L36`：细红框 + 角标 `anti-image`
- `tuned L36`：细 teal 框 + `tuned`
- `final`：Mute 框或无框

若必须保留更多深度，用 **2×4**（两端对称），**禁止 5+3 留白**。

### 4.4 验收标准

- [x] 无大块空白
- [x] 两行叙事与正文两句一一对应
- [x] 缩放后标签仍清晰；输出用 PNG@300dpi 或 PDF 嵌入无损图

---

## 5. 与正文的强制对应表

| 正文表述 | 必须出现在 |
|---------|-----------|
| predictable early / L6 | Fig1-B 侧标 + Fig3-B 红框 |
| translated late / L52–54 | Fig1-B band + Fig1-C Translation + Fig4 三图 band |
| target-image vs velocity | Fig3-A 两行语义 + Fig5 下行 raw vs tuned |
| five stages 名称 | Fig1-C 与 Intro/Experiments **逐字一致** |
| probe flat, drop at L59 | Fig4-C |

Fig1-C 五阶段名称（与正文一致）：

1. Injection (`≤ L36`)
2. Outcome prediction (`L6 / t2–4`)
3. Target-image code (`L6–51`)
4. Translation (`L52–54`)
5. Output head (`L59`)

---

## 6. 实施优先级（按收益）

1. **Fig5 Tuned lens** — 对称性一票否决级
2. **Fig1 Teaser** — 第一印象与五阶段对齐
3. **Fig4 Boundary** — 共享 legend + L52–54 band（改动小、很顶会）
4. **Fig3 Mechanism** — 网格与短标题精修

对应脚本（改图时优先动这些）：

- `figs/fig12_tuned_lens/`（需重排脚本或新 compositing）
- `figs/fig1_teaser/fig1_teaser.py`
- `figs/fig10_boundary/fig10_boundary.py`
- `figs/fig5_mechanism/fig5_mechanism.py`

---

## 7. 最终 checklist（AAAI / CVPR 级别）

- [x] 四图同一字体、色板、字母规范
- [x] 偏大气字号阶梯已落实（面板标题 10 pt，轴 9 pt，刻度 7.5–8 pt，格内 ≥7 pt）
- [x] 每图一个主 claim，标题 ≤4 词
- [x] 网格对称，无半行留白、无 legend 压曲线
- [x] L52–54 / L6 在相关图上几何一致
- [x] 矢量 PDF + 必要位图 300dpi；`pdffonts` 无 Type 3
- [x] 打印灰度仍可区分实线/虚线与 band
- [x] 重导出后重编译 `main_aaai.pdf`，确认正文仍 ≤7 页技术内容
