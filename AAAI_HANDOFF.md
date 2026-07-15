# AAAI-27 投稿交接 (START HERE)

> 给下一个从 0 接手的 agent：本文件是唯一入口。先读这一页，再按需跳转到
> `AAAI_SPINE.md`（为什么这样写）/ `OUTLINE.md`（claim 真值表 C1-C28）/
> 项目 memory（研究链全史）。真正的官方模板/规则以 `/home/ubuntu/chengyanli/AuthorKit27.zip`
> （含 `AAAI27-writing-skill.md` 权威规则说明）为准，别凭记忆造格式规则——2026-07-14 曾因此出过
> 真错（见 §4 坑 1）。最后更新 2026-07-14。

## 0. 当前状态（一眼看清）

AAAI-27 主赛道投稿稿**已定稿并编译通过**，三份独立交付物：

| 交付物 | 文件 | 状态 |
|---|---|---|
| 主论文 PDF | `main_aaai.pdf` | **8 页**（正文 7 + references 1），0 错、0 undefined ref/cite、匿名干净 ✓ |
| 复现清单 PDF | `reproducibility_checklist.pdf` | **2 页，独立提交**（不含在 main_aaai.pdf 内），匿名干净 ✓ |
| 补充材料 PDF | `supplement.pdf` | **28 页**（= 完整扩展版，含 K7-K9 配图+句级润色），已匿名 ✓ |

**合规判定：符合 AAAI-27**——正文（含全部图表）硬上限 7 页；参考文献不计入该限制、长度不限
（当前 1 页）；**Reproducibility Checklist 不计入正文页数，且 AAAI-27 明确要求单独上传，不与
主论文合并成一个 PDF**（官方模板 `ReproducibilityChecklist.tex` 本身支持 embed 或 standalone
两种编译模式，但 `AAAI27-writing-skill.md` §3/§6 对本届会议的规则写死为"单独上传"——之前版本
把它 `\input` 进了 main_aaai.tex 凑成"9 页"是**错的**，已改正，见 §4 坑 1。

## 1. 文件地图（谁是谁 / 真值来源）

**AAAI 投稿这一套（改这些）：**
- `main_aaai.tex` — **AAAI 主论文源**。AAAI 强制前导块 + title + `\author{Anonymous Submission}`
  + abstract + `\input` 9 个正文片段 + 6 个 figure 环境 + `\bibliography{references}`。
  **不再 `\input` 复现清单**（2026-07-14 起分离，见下）。**正文文字不在这个文件里改，改下面的片段。**
- `aaai_draft/*.tex` — **9 个正文片段（正文正文所在）**，按顺序：
  `00_intro` → `05_related` → `10_method` → `20_results_decided_early` →
  `30_results_translated_late` → `40_results_dissociation` →
  `45_differential_preview`（第 7 页提上来的 differential lens + 15% 预览杠杆）→
  `50_results_generalize_lever` → `60_limits_conclusion`。
- `reproducibility_checklist.tex` → `reproducibility_checklist.pdf` — **独立提交的复现性清单**
  （官方 `ReproducibilityChecklist.tex` 原文，只把 34 处 "Type your response here" 替换成 31 个
  实际答案，其余一字未改；单独 `pdflatex ×2` 编译，不 `\input` 进 main_aaai.tex——见 §4 坑 1）。
- `supplement.tex` → `supplement.pdf` — **AAAI 补充材料** = `main.tex`（arXiv 28pp）的匿名+改题副本
  （`\author`→Anonymous、删 `\thanks{Code:...}`、retitle "Supplementary Material"、6 句前言、
  8 张 PNG→JPEG）。
- `aaai2027.sty` / `aaai2027.bst` — AAAI-27 官方样式，与 `AuthorKit27.zip` 里的原文件 **md5 逐字节
  相同**（2026-07-14 核对过，别改）。
- `figs/` — 主论文用 6 图：`fig1_teaser.pdf` `fig5_mechanism.pdf` `fig10_boundary.pdf`
  `fig12_tuned_lens.jpg` `fig6_causality.pdf` `fig15_preview_lever.jpg`（全部在位）。

**权威来源（改格式规则前必查，别凭记忆）：**
- `paper/aaai_kit/AAAI-27-AuthorKit.zip`（+ 已解压的 `extracted/`）— 项目内的官方 AuthorKit 副本，
  2026-07-14 同步成与 `/home/ubuntu/chengyanli/AuthorKit27.zip` 完全一致的最新版（含
  `AAAI27-writing-skill.md`）；**旧的 2026-07-13 版本没有这份 skill.md**，这正是复现清单 embed/
  standalone 判断出错的原因（见下）——以后先查这里，不用每次找用户要新副本。
- `/home/ubuntu/chengyanli/AuthorKit27.zip` — 用户主目录下的原始来源，解压得
  `AnonymousSubmission2027.tex/.pdf`（投稿模板范例，10pp）、`CameraReady2027.tex/.pdf`、
  `ReproducibilityChecklist.tex/.pdf`（清单原文，standalone 编译 2pp）、`aaai2027.sty/.bst`
  （我们在用的这两个文件的官方源）、**`AAAI27-writing-skill.md`**（本届会议规则的中文摘要：
  时间节点/模板选择/页数与格式硬性要求/双盲要求/Supplementary 规则/复现清单规则/投稿数量限制/
  自查清单，比这份 HANDOFF 更权威，冲突时以它为准）。

**参考/别动：**
- `main.tex` — **arXiv 预印本原稿（现 28pp）**，不是 AAAI 投稿件，**别在改 AAAI 稿时顺手改它**（两条轨独立维护）。
  它自己有独立的、持续在动的维护轨（K7-K9 配图补齐 + `research-paper-writing` skill 句级润色，均已完成，
  详见 `provenance.md`），editing main.tex 不影响 `main_aaai.tex`/`aaai_draft/*.tex` 的任何内容。
- `AAAI_SPINE.md` — 脊柱锁定（为什么留正文/下沉补充的判据 + abstract v1）。
- `OUTLINE.md` — **claim 真值表 C1-C28，所有数字的最终真值来源**。
- `provenance.md` — 图表溯源。

## 2. 如何重建 PDF（pdflatex + bibtex，无 latexmk）

```bash
cd /home/ubuntu/chengyanli/image-edit-lens/paper
pdflatex main_aaai.tex && bibtex main_aaai && pdflatex main_aaai.tex && pdflatex main_aaai.tex
# 补充材料同理：
pdflatex supplement.tex && bibtex supplement && pdflatex supplement.tex && pdflatex supplement.tex
# 复现清单是独立文档，不吃 bibtex（无引用），standalone 编译两遍即可：
pdflatex reproducibility_checklist.tex && pdflatex reproducibility_checklist.tex
```
验收：`pdfinfo main_aaai.pdf | grep Pages` 应为 **8**（7 正文 + 1 refs）；
`pdfinfo reproducibility_checklist.pdf | grep Pages` 应为 **2**；
`grep -c "undefined" main_aaai.log` 应为 0。

## 3. 合规 & 匿名（**阻塞项，改任何东西后必复核**）

- **双盲**：`main_aaai.tex` 用 `\usepackage[submission]{aaai2027}`（加行号、隐作者块），
  `\author{Anonymous Submission}`。改完跑：
  `strings main_aaai.pdf | grep -icE "chengyanli|image-edit-lens|flowgpt|yata|github"` **必须 =0**。
  supplement / reproducibility_checklist 同样已 byte-grep 干净、`pdfinfo` Author 空。
- **AAAI 禁用包/命令**（会硬报错）：hyperref/geometry/titlesec/setspace/wrapfig/ulem 等；
  `\clearpage \newpage \pagebreak \columnsep \addtolength \tiny`、caption/float/heading 附近的负
  `\vspace`。别加 times/helvet/courier/mathptmx（sty 已自动载）。xcolor 安全（清单蓝字要用）。
- **页数**：正文（含全部图表）硬上限 7 页；references 不计入、长度不限（当前 1 页）；
  **复现清单完全不占 main_aaai.pdf 的页数——它根本不在这个 PDF 里**，是单独一份 2 页 PDF。
  当前正文正好卡在 7 页。

## 4. 关键坑（已记 algo-log pitfall，别重踩）

1. **【已修复的真错，2026-07-14】复现清单不该合进 main_aaai.pdf**：早前版本把
   `ReproducibilityChecklist.tex` 剥壳成 `repro_checklist_filled.tex` 再 `\input` 进
   main_aaai.tex，凑成"9 页 = 7 正文 + 2 refs/清单"——**这是错的**。官方模板本身确实同时支持
   embed 和 standalone 两种编译路径（`\@ifundefined{isChecklistMainFile}` 守卫是给 embed 用的
   合法开关，不是"陷阱"，之前的坑记录把这点说反了），但具体选哪种要看会议官网说明；
   `AAAI27-writing-skill.md` §3/§6 对 AAAI-27 写得很明确：**"Reproducibility Checklist 不计入
   正文页数，单独上传"**——即必须是独立 PDF，不能和主论文合并。用户在 2026-07-14 发现这个问题
   （连带怀疑模板本身是不是错的——查证后 `aaai2027.sty`/`.bst` 其实和
   `/home/ubuntu/chengyanli/AuthorKit27.zip` 里的官方文件逐字节相同，双栏渲染也正常，问题只出
   在清单该不该合并这一点上）。修法：删掉 `main_aaai.tex` 里的 `\input{repro_checklist_filled}`，
   main_aaai.pdf 从 9pp 变回 8pp（7 正文 + 1 refs）；把官方 `ReproducibilityChecklist.tex`
   原文整份复制过来（连指令/示例文字都不动，只替换 34 处 "Type your response here" 里真正对应
   问题的 31 处）存成 `reproducibility_checklist.tex`，standalone 编译成独立的
   `reproducibility_checklist.pdf`（2 页，与官方范例 `ReproducibilityChecklist.pdf` 页数一致）。
   **教训（精确版，别过度归因）**：`paper/aaai_kit/` 里其实早就有一份真的官方 AuthorKit（2026-07-13
   存的，`aaai2027.sty`/`.bst`/`ReproducibilityChecklist.tex` 当时就已经是从这份真实材料原样抄的，
   不是凭空编的——sty/bst 序号证明没抄错）；但那份旧 kit **没有** `AAAI27-writing-skill.md`，即没有
   "AAAI-27 这一届具体要不要分开提交"这条会议特定指令，官方模板自己的注释原话是"Check the
   instructions on your conference's website"——没有联网查会议官网的条件下，只能二选一猜，猜错了选
   embed。**真正的教训是：模板明确写了"这是 per-conference 决定，需要外部确认"的地方，不能拿
   "两种方式都技术合法"当理由随便选一个了事，要么找到会议官网原话，要么标成"未确认/待用户核实"
   而不是直接定稿宣称"已定稿并编译通过"。** 2026-07-14 用户给的新 `AuthorKit27.zip` 多带了这份
   `AAAI27-writing-skill.md`，才把这个悬而未决的选择点坐实。
2. **参考文献不计入 7 页正文**：一度按 refs 也占页保守排版白丢一页，纠正后才把
   differential lens 从补充提回正文第 7 页。
3. 环境无 `convert`/`magick`：PNG→JPEG 用 Python PIL
   `Image.open(p).convert('RGB').save(q, quality=88)`。

## 5. 待办 / 开放项（都非阻塞，等用户拍板）

- **[美观] 页 7 留白**：`fig:mechanism`(fig5) + `fig:previewlever`(fig15) 两张浮动图下方留空。
  合规但不好看，可微调图序/尺寸或 `[t]`→`[b]` 消除。
- **[打包] 投稿包**：三份各自独立上传的 PDF——`main_aaai.pdf`（主论文）、
  `reproducibility_checklist.pdf`（复现清单，独立字段/独立上传，不合并进主 PDF，见 §4 坑 1）、
  `supplement.pdf`（Supplementary，据 `AAAI27-writing-skill.md` §5 截止比正文晚 3 天即
  2026-07-31 AoE，且**不接受"录用后公开代码"的承诺**——投稿时就要给可运行代码/数据，这条待办：
  supplementary 阶段需要额外准备代码仓库，不只是 PDF）。走 OpenReview 还是 CMT 待投稿系统开放
  （2026-06-30，已过）后到入口确认；不用 zip 打包，各自以独立文件上传。
- ~~**[非 AAAI 关键路径] arXiv 版 K9/C28 回填**~~：**已完成 (2026-07-14)**。审计发现不止 K9，
  K7/K8 的结果图也一样只有数字没配图；三组都已配图补齐（Figure 16-18，`fig:k7ladder`/
  `fig:k8decompose`/`fig:k9curve`，先原始 PNG 直搬后用 `nature-figure` skill 重做成投稿级配图），
  `main.tex`/`supplement.tex` 均定格 **28pp**，重编译 0 错 0 undefined ref，匿名 byte-grep 仍 0
  命中。详见 `provenance.md` "K7/K8/K9 figures added" 节。这仍是 arXiv/展示页轨，与 AAAI 稿独立，
  AAAI 稿不含 K7-K9。
- ~~**[非 AAAI 关键路径] arXiv 版全文句级润色**~~：**已完成 (2026-07-14)**。用
  `research-paper-writing` skill（github.com/Master-cai/Research-Paper-Writing-Skills）对
  `main.tex`（同步 `supplement.tex`）做纯句子边界层面的润色——只拆长句/改标点，不动任何数字、
  claim、引用。覆盖 Abstract/Introduction 到 Method/Experiments/Limitations/Conclusion 全篇，
  详见 `provenance.md` "Sentence-level clarity pass" 节。页数不受影响（仍 28pp）。
- ~~**[非 AAAI 关键路径] 展示页 + 打包下载链接**~~：**已完成 (2026-07-14)**。展示页
  `image-edit-lens-showcase/index.html`（挂在 R2，公网
  `yata-image-publics.flowgpt.com/image-edit-lens-showcase/`，现 v7.1）新增撰写指南小节
  （含论文行文逻辑说明 + README.md 工具背景 + Future-work→实际实验映射表）与一键下载按钮，
  链接到同域名下的 `downloads/image-edit-lens-paper.zip`（35MB，`main.tex`/`main.pdf`/`figs/`/
  `provenance.md`/`OUTLINE.md`）。**打包范围刻意排除全部 AAAI 投稿专属文件**
  （`main_aaai.tex`/`main_aaai.pdf`/`supplement.tex`/`supplement.pdf`/`aaai_draft/`/`aaai_kit/`/
  `AAAI_HANDOFF.md`/`AAAI_SPINE.md`/`reproducibility_checklist.tex`/`reproducibility_checklist.pdf`），
  且打包用的 `provenance.md` 副本额外剥离了所有 AAAI/supplement 字样——理由见 §3 双盲约束：
  `supplement.pdf` 是 `main.pdf` 的匿名改题副本，若与实名展示页打包在一起会构成自我去匿名化证据链。
  **任何人未来再次打包 `paper/` 给展示页/公网下载，必须延续这条排除清单**，不要因为 `paper/`
  目录下新增了文件就无脑全打包。
- ~~**[AAAI 合规修复] 复现清单从 main_aaai.pdf 中拆分为独立提交**~~：**已完成 (2026-07-14)**，
  详见 §4 坑 1。`main_aaai.pdf` 9pp→**8pp**（7 正文+1 refs），新增独立的
  `reproducibility_checklist.pdf`（2pp），两份 PDF 均已重编译验证（0 错、0 undefined ref、
  匿名 byte-grep 0 命中）。用户提供了官方 `/home/ubuntu/chengyanli/AuthorKit27.zip` 核对，
  `aaai2027.sty`/`.bst` 确认与官方逐字节相同（无需替换），双栏渲染也确认正常——问题只在
  复现清单的提交方式上。
- **[非关键] K7/K8/K9 微日志**曾发现漏记，权威记录在 `runs/*/visual_verdicts.json`，
  已不影响 AAAI。

## 6. 硬约束 / 纪律（贯穿全项目，务必遵守）

- **不 git commit**（本项目既有约定，从未 commit）。
- **/mnt/local 只读**取模型，产物一律写 /home；模型真身在 `/mnt/local/yzh/models/Qwen-Image-Edit-2511`。
- 不动他人 GPU 进程、不 `pkill -f`。
- **回复用中文**。
- **分工**：Fable 做计划/审读/目检 verdicts；sonnet 子代理写代码（脚本/论文回填/展示页），
  默认 `model:"sonnet"`。
- 生图/批量任务默认 ≤10/批停等用户说继续。
- 需要任何数据集直接问用户要。

## 7. 截止日期

- Abstract 注册：**2026-07-21 AoE**
- Full paper（main_aaai.pdf + reproducibility_checklist.pdf）：**2026-07-28 AoE**
- Supplementary / Code（supplement.pdf + 可运行代码仓库）：**2026-07-31 AoE**（比正文晚 3 天，
  据 `AAAI27-writing-skill.md` §5；不接受"录用后公开代码"的承诺，投稿时必须给可运行代码）

## 8. 论文脊柱（一句话，细节见 `AAAI_SPINE.md`）

第一个面向扩散图像编辑器的 tuned-lens，证明编辑**决定得早**（L6 即线性可读，cross-seed
probe 0.88，而冻结头到 L48-54 才可读）、**翻译得晚**（L52-54 锐带把内部目标图像码翻译成速度场，
时间步不变、跨模型通用）；可读≠因果必要≠线性可写三向解离；读数因果 → 免训练杠杆（CFG 截断
step 2 省 45% 算力，四族编辑视觉完好）。
