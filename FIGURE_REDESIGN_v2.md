# 顶会级主图修改规范 · 第二版（在 Codex 已改基础上继续）

> **基线**：`25d8134 Redesign main paper figures` 之后的当前图。  
> **本文用途**：给 Codex / 绘图脚本的 **增量修改清单**，不是从零重画。  
> **仍不含** `fig2_method`（pipeline）。  
> **第一版全文**：见 `FIGURE_REDESIGN.md`（总原则、色板、字号阶梯仍有效；本文件只写 **v1 未落实 / 新发现** 的项）。

> **实施状态（2026-07-21）**：已完成。四图标题均按面板/行居中；Fig1 使用按物理层坐标插值的 L52--54 band；
> micro-label 下限为 7 pt；Fig5-C 自动留出 0.05 y 轴余量；四脚本均使用可移植字体 fallback，当前解析为 Arimo；
> 主稿重编译后技术内容止于第 7 页，0 overfull / undefined / Type 3。

---

## 0. 本轮必须完成（优先级从高到低）

| # | 项 | 图 | 严重度 |
|---|----|----|--------|
| 1 | **所有主图**的面板小标题（`A`/`B`/`C`…）各自相对面板 **水平居中** | Fig1 / Fig3 / Fig4 / Fig5 | P0 |
| 2 | `translation` 做成真正的 **L52–54 半透明带**，与 Fig5 几何一致 | Fig1 | P0 |
| 3 | 所有 micro-label / 箭头字 ≥ **7 pt** | Fig1（及扫一遍其余图） | P1 |
| 4 | 核对正文 PDF 中图与引用段的邻近（浮动体） | `20_experiments.tex` | P1 |
| 5 | Fig5-C y 轴略留白；Fig3-A 列标题防挤 | Fig5 / Fig3 | P2 |
| 6 | 字体路径可移植（勿写死仅 Linux Arimo 路径） | 全部脚本 | P2 |

改完后重导出 PDF/PNG，并重编译 `main_aaai.pdf`，确认技术正文仍止于第 7 页。

---

## 0.1 全局 P0 · 面板小标题各自居中（四图统一）

适用于除 pipeline 外全部主文图。**不是**只改 Fig1。

| 图 | 文件 | 须居中的面板小标题 |
|----|------|-------------------|
| Fig1 Teaser | `fig1_teaser.py` | `A Edit example` · `B Layer-time lens` · `C Measured stages` |
| Fig3 Mechanism | `fig5_mechanism.py` | `A Decode conventions` · `B Early probe` |
| Fig4 Tuned lens | `fig12_tuned_lens.py` | `A Edit enters internal image` · `B Head fails, lens succeeds`（行级标题，相对整行 3 格网格水平居中；若现为左对齐则改为居中） |
| Fig5 Boundary | `fig10_boundary.py` | `A A/C crossover` · `B Alignment to v59` · `C Probe accuracy` |

**规则（四图同一套）：**

- 每个面板（或 Fig4 的每一行）的 **字母 + 标题作为一组**，相对 **该面板/该行内容区** 水平居中（`ha="center"`，中心约 `x=0.5` in axes / row coords）。
- **禁止** 字母贴左、标题贴左的分置写法（当前若干脚本的 `letter` 在 `x≈-0.08`、`title` 在 `x≈0.02` 即属此类）。
- 同一图内各面板标题 **基线齐平**（同一 `y`）；字号 10 pt bold，Ink。
- 推荐：`ax.text(0.5, 1.08, f"{letter}  {title}", transform=ax.transAxes, ha="center", ...)` 或 `set_title(..., loc="center")`。
- **注意**：Fig3 的列小标题（`standard` / `sign-flip` / …）是格子列头，另见 §3.2；与这里的 **面板** 小标题 `A`/`B` 不是同一层。

**验收：**

- [ ] Fig1 / Fig3 / Fig5：每个 `A`/`B`/`C` 标题相对各自面板居中
- [ ] Fig4：`A`/`B` 行标题相对该行三格整体居中（或明确居中于行内容宽）
- [ ] 目检无「标题贴左、图在中间」的错位感

---

## 1. Figure 1 — Teaser（本轮重点）

文件：`figs/fig1_teaser/fig1_teaser.py` → `fig1_teaser.pdf`

### 1.1 P0 · 三栏小标题居中（用户指出；并入 §0.1）

**现状**：`A Edit example` / `B Layer-time lens` / `C Measured stages` 目前像左对齐挂在面板上方（脚本里大致是 `letter` 在 `x≈-0.06`，`title` 在 `x≈0.02`，`ha="left"`）。

**目标**：按 §0.1，每个面板的 **字母 + 标题作为一组，相对该面板内容区水平居中**。

推荐实现见 §0.1；Fig1 额外验收：

- [ ] 三栏标题的视觉中心与各自面板（A 双图块 / B 热图+色条整体 / C 阶段条）水平中轴对齐
- [ ] 三栏标题 **基线齐平**（同一 `y`）
- [ ] 字母仍为粗体 10 pt；标题同字号，Ink 色

### 1.2 P0 · Translation 带与 Fig5 一致

**现状**：脚本对 `layers.index(54)` 画约一行高的强调，标签 `translation`；**不是** L52–54 跨层 band。

**目标**（对齐 `FIGURE_REDESIGN.md` §1.4 与 Fig5）：

- 在热图上画半透明带，覆盖 **L52 与 L54 之间的行**（含两端；与 Fig5 的 `axvspan(52, 54)` 语义一致）。
- 色：`Red @ 12–15% alpha`（或与 Fig5 同源常量）。
- 标签写在带内或带旁：`translation`，白字或 Red 字，**≥7 pt**，勿遮住过多格子。
- 删除“只框 L54 一行”的旧逻辑。

**验收**：

- [ ] 带的垂直范围对应 L52–54（在离散 layer 轴上覆盖正确行）
- [ ] Fig1-B 与 Fig5 三图的 translation 区间读感一致
- [ ] 与右侧 C 栏 **Translation / L52–54** 盒子仍语义对齐（引导线可选保留）

### 1.3 P1 · 字号下限

- `edit` 箭头字、一切 micro-label：从 6.5 → **≥7 pt**。
- `car_red`、色条刻度、热图侧标保持 ≥7 pt。

### 1.4 本轮不要改动的（已达标）

- 三栏结构 A/B/C、五阶段文案与顺序、Teal→Red 语义色、`probe-readable` 侧标、色条 `P(red car)`。

---

## 2. Figure 5 — Boundary（小修）

文件：`figs/fig10_boundary/fig10_boundary.py`

### 2.1 P0 · 三栏面板小标题各自居中（并入 §0.1）

- 现状：若仍为 `letter` 左、`title` 左分置，改为每栏 `A …` / `B …` / `C …` **相对该 axes 水平居中**。
- 三栏标题基线齐平。

### 2.2 已达标（保持）

- 1:1:1 三栏、共享底栏 legend、三图同一 translation 浅带、短标题文案、y 轴 `CLIP P(red)`。

### 2.3 P2 · Panel C 留白

- 现状：probe 曲线贴着 y 轴上沿。
- 改为：`ylim` 略高于数据 max（例如 max+0.05，或固定 `0.30–0.95`），避免贴顶。

### 2.4 与 Fig1 联动

- Fig1 改 band 时，**复用同一常量**（如 `TRANSLATION_LO, TRANSLATION_HI = 52, 54` 与同一 `BAND_ALPHA`），避免两图 band 宽窄/颜色不一致。

---

## 3. Figure 3 — Mechanism（小修）

文件：`figs/fig5_mechanism/fig5_mechanism.py`

### 3.1 P0 · 面板小标题各自居中（并入 §0.1）

- `A Decode conventions` 相对左侧 2×4 内容区水平居中。
- `B Early probe` 相对右侧热图（含色条整体或主热图区，与实现一致即可）水平居中。
- 两标题基线齐平；勿用左贴边分置。

### 3.2 已达标（保持）

- L24 image-like / L59 velocity、L6/t4 红框、角标 pill 规则、短标题文案。

### 3.3 P2 · 列标题防挤

- 四列标题若换行或互相碰撞：略减字号至 7–7.5 pt，或缩短为  
  `standard` / `sign-flip` / `v as x0` / `−v as x0`（面板字母 A–D 可保留在标题或仅留在 caption）。
- 保持四列等宽、**列头**水平居中于各列（此为格子列头，与 §3.1 面板标题分层）。

### 3.4 P2 · 热图数字对比度（可选）

- 深红格上白字若发灰：按亮度自动选白/Ink（已有则保持）。

---

## 4. Figure 4 — Tuned lens

文件：`figs/fig12_tuned_lens/fig12_tuned_lens.py`

### 4.1 P0 · 行级小标题居中（并入 §0.1）

- `A Edit enters internal image`、`B Head fails, lens succeeds`：相对 **该行三格整体宽度** 水平居中（不要贴左）。
- 两行标题左端不必互相对齐到纸张左边；以各自行内容中轴为准，或两行共用同一居中规则但相对网格居中。

### 4.2 已达标（保持）

- 2×3 对称、anti-image / tuned 框与 badge、行标题 claim 文案。

### 4.3 可选增强（P3，时间不够可跳过）

- 正文现为单栏 `0.98\columnwidth`：若双栏打印偏小，可改为 `figure*` + `0.92\textwidth`（需重编译确认不超页）。
- B 行 `tuned L36` 与 `final` 几乎相同：可不改图；若改，仅微调 final 的标注或 crop，**不要**破坏 2×3。

---

## 5. 正文浮动体（P1）

文件：`aaai_draft/20_experiments.tex`

**现状**：`fig:mechanism` / `fig:tunedlens` / `fig:boundary` 环境集中在 Setup 之后、Early 小节正文之前，易导致图出现在首次引用之前较远。

**目标**：

- 每个 `figure`/`figure*` 尽量紧挨 **首次 `\ref{...}` 的段落**（引用后或段末）。
- 不要用 AAAI 禁用的 `\clearpage` / `\newpage` / 负 `\vspace`。
- 用 `[t]` / `[b]` 等标准浮动选项微调即可。

**验收**：翻 `main_aaai.pdf`，Fig3/4/5 与讨论它们的段落同页或邻页，而不是整块堆在 Setup 后。

---

## 6. 工程 / 可移植性（P2）

四份绘图脚本目前硬编码：

```text
/usr/share/fonts/truetype/croscore/Arimo-*.ttf
```

**目标**：

- 按顺序 fallback：Source Sans 3 → Arimo → Arial/Helvetica → DejaVu Sans（最后手段）。
- macOS / Linux 都能找到至少一种；在脚本开头打印实际选用的字体名。
- 保持 `pdf.fonttype=42`。

在各图 `INFO.md` 补一行：`font: <resolved family>`。

---

## 7. 字号与色板（沿用 v1，提醒）

| 元素 | 字号 |
|------|------|
| 面板标题 | 10 pt |
| 轴标题 | 9 pt |
| 刻度 | 7.5–8 pt |
| 格内 / micro-label | **≥ 7 pt** |

| Token | Hex | 语义 |
|------|-----|------|
| Teal | `#0F8FA0` | target-image / early |
| Red | `#C2402A` | translation / velocity |
| Ink | `#222222` | 主文字 |
| Mute | `#6B6B6B` | 次要 |
| Band | Red @ 12–15% α | L52–54 |

---

## 8. Codex 执行清单（建议顺序）

1. **四图面板/行标题居中**（§0.1）：`fig1_teaser.py`、`fig5_mechanism.py`、`fig10_boundary.py`、`fig12_tuned_lens.py`。
2. 修 `fig1_teaser.py`：L52–54 band + micro-label ≥7pt → 重导出。
3. 抽公共 band 常量，同步确认 `fig10_boundary.py` 一致；微调 C 的 `ylim`。
4. 轻修 `fig5_mechanism.py` 列标题（若挤）。
5. 调整 `aaai_draft/20_experiments.tex` 中三个 figure 环境位置。
6. 字体 fallback（四脚本）。
7. 编译：

```bash
pdflatex main_aaai.tex && bibtex main_aaai && pdflatex main_aaai.tex && pdflatex main_aaai.tex
```

确认：`sec:limits` / `sec:conclusion` 仍在第 7 页；目检 **四图** 面板/行标题各自居中，以及 Fig1 translation 带。

---

## 9. 本轮完成定义（DoD）

- [ ] Fig1 / Fig3 / Fig5 面板小标题相对各面板 **居中**；Fig4 行标题相对各行 **居中**；同图基线齐
- [ ] Fig1 热图为 **L52–54 band**，标签 `translation`，与 Fig5 一致
- [ ] 图内无 <7 pt 的说明文字
- [ ] 正文图浮动不再整块堆在 Setup 后（目检通过）
- [ ] 重编译通过，正文技术内容 ≤7 页
- [ ] （可选）字体 fallback + Fig5-C ylim + Fig3 列标题

---

## 10. 与第一版的关系

- `FIGURE_REDESIGN.md` = 完整设计宪法（仍有效）。
- **本文件 `FIGURE_REDESIGN_v2.md`** = 基于当前仓库实拍效果的 **第二轮增量工单**。  
Codex 应落实本文件缺口；**面板/行标题居中是四图统一 P0**，不要只改 Fig1。Fig4 的 2×3 网格与 Fig5 共享 legend **不要无关重排**，只改标题对齐等列出项。
