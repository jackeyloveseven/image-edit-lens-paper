# 主文加表计划：Table A + Table B

> 目标：在 AAAI 主文（技术内容 ≤7 页）增加 **两张** 紧凑表，缓解“全文无表、数字挤在段落里”的问题。  
> 画法遵循 [nature-skills](https://github.com/Yuan1z0825/nature-skills) 中 `nature-writing/references/experiments.md` 的表格规则，并适配 AAAI 双栏版式。  
> 不含 Table C（levers）与 taxonomy 上提；那些仍留 supplement 或后续可选。

> **实施状态（2026-07-21）**：已完成。`tab:early` 与 `tab:generalize` 已加入
> `aaai_draft/20_experiments.tex`，caption 在上、booktabs、无竖线；重复数字已压缩。
> Table B 为适配单栏改成四列紧凑版，但保留计划中的 boundary、early/L59 probe、transfer 和 direction cosine。
> 主稿技术内容仍止于第 7 页，0 overfull / undefined。

> **当前状态（2026-07-22）**：两表仍为正文 Table 1/2。主文图号已重排，
> boundary 是 Figure 4；15%-NFE preview 已作为 Figure 7 进入正文，不再只是
> “正文一句或日后 Table C”。本文件以下主体保留为实施历史。

---

## 0. 总规则（nature-skills × AAAI）

### 硬规则

1. `\usepackage{booktabs}`（主文已有则可复用）。
2. 只用 `\toprule` / `\midrule` / `\bottomrule`；**禁止竖线** `|` 与密 `\hline`。
3. **caption 在表上方**；`\caption` 后接 `\label`。
4. **一张表一个主信息**；不要把 early probe 与 CFG 杠杆混在一张表。
5. 同列小数位统一；需要时在表头标方向：`↑` / `↓`。
6. 关键格可用极淡底色（`colortbl` + `\cellcolor{...!12}`）；最多高亮 1–2 个 headline 格，勿整表染色。
7. 可选：`siunitx` 做小数对齐；若引入新包，确认不与 `aaai2027.sty` 冲突。

### AAAI 版式

- 优先 **`table` 单栏**（`\small` 或 `\footnotesize`）。
- 列太多再改 `table*`；先尝试单栏。
- 加表后必须 **删掉正文里已被表格覆盖的数字串**，避免重复占页。
- 编译验收：`sec:limits` / `sec:conclusion` 仍在第 **7** 页；`Overfull \hbox` 尽量为 0。

### Caption 风格

- 名词短语总题 + 一句协议说明（设定 / \(n\) / 指标含义）。
- 示例格式：`Early outcome probes and held-out selection. ...`
- 长讨论、失败 case（eyes null 等）放正文一句或表注 \(^\dagger\)，不要把 caption 写成段落。

---

## 1. Table A — Early prediction & held-out selection

### 1.1 主信息

在固定欠指定（或目标）设定下，**早层状态可预测最终结果**，且 held-out **best-of-five selection** 在 Qwen 与独立架构 Boogu 上成立。

### 1.2 建议位置

- 文件：`aaai_draft/20_experiments.tex`
- 小节：`\subsection{The Realized Edit Is Predictable Early}`（`sec:early`）
- 锚点：在报完 car 固定 prompt probe（0.667）与 tree/Boogu/selection 叙述的 **中段或段末** 插入；首次引用 `\ref{tab:early}`。
- 插入后：压缩该段中与表重复的数字列举（保留 1–2 个 headline 口头点题即可）。

### 1.3 建议表头（单栏）

```latex
\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3.5pt}
\begin{tabular}{@{}lllccl@{}}
\toprule
Setting & Model & Readout & Metric & Result & $p$ \\
\midrule
...
\bottomrule
\end{tabular}
\caption{Early outcome probes and held-out selection.
Fixed underspecified or target-color protocols as in \S\ref{sec:early};
chance or random-selection baselines in parentheses where applicable.}
\label{tab:early}
\end{table}
```

列含义：

| 列 | 内容 |
|----|------|
| Setting | 任务简称（car fixed-prompt / tree hue / Boogu select / …） |
| Model | Qwen-Image-Edit-2511 / Boogu-40 |
| Readout | 层·步，如 L6/t4 |
| Metric | 带方向，如 bal.\ acc.\ ↑、MAE (°)\ ↓、success ↑、mean rank ↓ |
| Result | 主结果（可括号写 baseline/chance） |
| \(p\) | 置换 / exact 检验；不显著可写 n.s.\ 或省略行 |

### 1.4 建议行（与当前正文数字对齐；以 `OUTLINE.md` / 正文为准逐格核对）

| Setting | Model | Readout | Metric | Result | \(p\) |
|---------|-------|---------|--------|--------|-------|
| Car, fixed prompt (3-way) | Qwen | L6/t4 | bal.\ acc.\ ↑ | 0.667 (chance 0.333) | 0.002 |
| Car hue (continuous) | Qwen | L6/t2 | MAE (°)\ ↓ | 22.3 → 8.3 | — (\(R^2{=}0.815\)) |
| Tree hue | Qwen | L6 | MAE (°)\ ↓ | 55.9 → 11.4 | 0.005 |
| Mug hue | Qwen | L6 | MAE (°)\ ↓ | 17.0 → 10.7 | 0.005 |
| Boogu hue | Boogu | L4/t2 | MAE (°)\ ↓ | 39.9 → 6.9 | 0.005 |
| Boogu recolor select | Boogu | L4 best-of-5 | success ↑ | 8/12 (rand.\ 20%) | \(4.1{\times}10^{-5}\) |
| Tree select | Qwen | L6/t2 best-of-5 | MAE (°)\ ↓ | 95.2 → 46.5 (rank 1.17) | \(3.7{\times}10^{-7}\) |
| Car select (env.) | Qwen | best-of-5 | MAE (°)\ ↓ | 25.7 → 11.1 (rank 2.00) | 0.0086 |

可选表注：

- \(^\dagger\) Eyes discrete / continuous null（\(p{=}0.796\)）不列入主表，正文一句带过。
- \(^\ddagger\) Selection 只选 closest candidate；部分 group 无 target-like hue。
- 高亮建议：car fixed-prompt 0.667 行、Boogu 8/12 行、tree select 行（三选一或两选）。

### 1.5 数据来源（核对用）

- 正文：`aaai_draft/20_experiments.tex`（`sec:early`）
- Claim 真值：`OUTLINE.md`（C9 及 selection 相关）
- 原始 runs（若需重算）：`runs/d2_probe/`、tree/mug/Boogu/selection 对应目录（以 provenance / 正文脚注为准）

### 1.6 正文改写要点

加表后删除或缩短：

- 连续堆叠的 `0.667` / `55.9→11.4` / `8/12` / `46.5` / `p=…` 串读。
- 改为：`Table~\ref{tab:early} summarizes ...` + 1–2 句机制解读（basis mismatch、不宣称 irreversible commitment）。

---

## 2. Table B — Cross-checkpoint translation & early readout

### 2.1 主信息

**Translation band（A/C crossover）** 与 **早层 probe 可读** 在同谱系 checkpoint（独立 fine-tune / 蒸馏）上复现；可读方向可跨模型转移。

### 2.2 建议位置

- 文件：`aaai_draft/20_experiments.tex`
- 小节：`\subsection{Generalization Across Checkpoints}`（`sec:generalize`）
- 锚点：段首 claim 后立刻给表，再留 2–3 句解释 cosine / toolchain。
- 与 Fig4（单模型 dense sweep）分工：**图 = 曲线形状；表 = 跨模型汇总**。

### 2.3 建议表头（单栏）

```latex
\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3.5pt}
\begin{tabular}{@{}lcccc@{}}
\toprule
Checkpoint & A/C band & Early probe & Probe @ L59 & Transfer \\
\midrule
...
\bottomrule
\end{tabular}
\caption{Translation boundary and early readout across checkpoints.
All models share Qwen-Image-Edit-2511 transformer classes unless noted.
Early probe is explicit-prompt 3-way accuracy unless noted.}
\label{tab:generalize}
\end{table}
```

列含义：

| 列 | 内容 |
|----|------|
| Checkpoint | Qwen-2511 / FireRed-1.1 / Rapid-AIO |
| A/C band | 交叉所在层带（如 L52–54） |
| Early probe | 早层准确率（标明层·步） |
| Probe @ L59 | 末端跌落（与 “flat-then-dip” 一致） |
| Transfer | 跨模型 probe 准确率或方向 cosine（仅适用行填） |

### 2.4 建议行（与当前正文对齐；逐格核对）

| Checkpoint | A/C band | Early probe | Probe @ L59 | Transfer |
|------------|----------|-------------|-------------|----------|
| Qwen-Image-Edit-2511 | L52–54 | 0.883 @ L6/t4 | 0.68–0.70 | — (source) |
| FireRed-Image-Edit-1.1 | L53–56 | 0.852 @ L6 | 0.69 | vs Qwen: 0.84 / 0.92 |
| Rapid-AIO (4-step) | L52–54 | (若正文有单独数则填；否则写 “boundary replicates”) | — | — |
| Direction align (L12) | — | — | — | cosine 0.833 |

表注建议：

- FireRed / Rapid 与主模型 **同架构谱系**；Boogu 的 prediction/selection 见 Table A，不进本表（避免与 limitations 矛盾）。
- Tuned-lens \(R^2\) 深度范围（0.97–0.999）可放表注一句，不必另开列。
- 高亮：三行的 A/C band 列（强调落在同一邻域）。

### 2.5 数据来源

- 正文：`aaai_draft/20_experiments.tex`（`sec:generalize`）
- Claim：`OUTLINE.md` C25 及相关；`runs/k6_*` / `g2_boundary` 等（以 provenance 为准）

### 2.6 正文改写要点

- 用表替换 FireRed/Rapid 层带与 0.852 / 0.84/0.92 / 0.833 的口头罗列。
- 保留一句：boundary 是架构邻域属性；Boogu 不宣称 translation 复现。

---

## 3. 不放进 A/B 的内容（避免表膨胀）

| 内容 | 去向 |
|------|------|
| CFG until-2、45% NFE | 正文 prose（不另建 Table C） |
| diff preview IoU / qualitative preview | 正文 prose + Figure 7；完整 battery 留 supplement |
| 10-case saturation battery | supplement `tab:battery` |
| Text-injection bands | supplement `tab:injection` |
| Steer / rank / Jacobian taxonomy | supplement `tab:taxonomy` |
| 逐层 A/C 曲线点 | Figure 4（boundary） |

---

## 4. 实施清单（给人 / Codex）

1. 在 `main_aaai.tex` 确认 `booktabs`；若用底色再加 `xcolor`/`colortbl`（检查 AAAI 模板兼容）。
2. 在 `20_experiments.tex` 写入 `tab:early`、`tab:generalize`。
3. 逐格对照正文与 `OUTLINE.md`，**禁止臆造数字**。
4. 压缩对应散文；增加 `\ref{tab:early}` / `\ref{tab:generalize}`。
5. 全量编译：

```bash
pdflatex main_aaai.tex && bibtex main_aaai && pdflatex main_aaai.tex && pdflatex main_aaai.tex
```

6. 验收：

- [x] 主文恰好两张新表（A+B），caption 在上、无竖线
- [x] 技术正文 ≤7 页
- [x] 表中数字与正文/OUTLINE 一致
- [x] 无 undefined ref；尽量无 overfull
- [x] Abstract / Intro 若点到这些结果，仍与表一致（不必在 abstract 里引用表号）

---

## 5. 与图表的分工（写给审稿人视角）

| 载体 | 职责 |
|------|------|
| Fig1 / Fig3 / Fig4 / Fig5 | 机制形状（early vs late、两码、band、internal image） |
| **Table A** | 跨任务/跨架构的 **可预测性与 selection** 汇总 + \(p\) |
| **Table B** | 跨 checkpoint 的 **边界与 probe** 汇总 |
| Supplement tables | 完整电池、ablation 细表、taxonomy |

---

## 6. 文件命名

- 本计划：`TABLE_PLAN.md`（本文件）
- 实现落点：`aaai_draft/20_experiments.tex`（主），必要时 `main_aaai.tex` 宏包行
