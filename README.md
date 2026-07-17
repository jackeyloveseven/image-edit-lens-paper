# image-edit-lens-paper — AAAI-27 投稿协作仓库

第一个面向扩散图像编辑器（Qwen-Image-Edit-2511，60 块 DiT）的 layer–time lens：
编辑**决定得早**（L6 线性可读，cross-seed probe 0.88）、**翻译得晚**（L52–54 窄带把内部目标图像码
翻译成速度场）；可读 ≠ 因果必要 ≠ 线性可写三向解离；读数因果化为免训练加速杠杆（CFG 截断省 45% 算力）。

**接手 / 改稿唯一入口：[`AAAI_HANDOFF.md`](AAAI_HANDOFF.md)。** 本 README 只做速览。

## 三份交付物（各自独立上传，不打包）

| 文件 | 内容 | 验收状态（2026-07-17） |
|---|---|---|
| `main_aaai.pdf` | 主论文 | **8 页：正文于第 7 页内结束（合规），refs 第 7–8 页**；0 错、0 undefined ref、匿名 byte-grep 0 命中 |
| `reproducibility_checklist.pdf` | 复现清单（**独立提交，不合并进主论文**） | 2 页 |
| `supplement.pdf` | 补充材料（arXiv 28pp 的匿名改题副本） | 28 页 |

截止：Abstract 注册 **2026-07-21 AoE** · Full paper **2026-07-28 AoE** · Supplementary + 可运行代码 **2026-07-31 AoE**。

## 重建与验收（改正文后必跑，缺一不可）

```bash
pdflatex main_aaai.tex && bibtex main_aaai && pdflatex main_aaai.tex && pdflatex main_aaai.tex
pdfinfo main_aaai.pdf | grep Pages     # 正文（含全部图表）必须在第 7 页内结束；refs 不计入限制
grep -c "undefined" main_aaai.log      # 必须 0
strings main_aaai.pdf | grep -icE "chengyanli|image-edit-lens|flowgpt|yata|github"   # 必须 0（双盲）
```

**页数红线**：2026-07-16 曾发生合并改稿把 PDF 悄悄顶到 9 页（正文 8 页，超限）而无人察觉的事故，
07-17 已通过全文编辑级压缩修复。教训：**"编译 0 错" 不等于合规**——任何涉及正文的改动，push 前
必须重编译并核对上面三条。

## 目录速览

- `main_aaai.tex` + `aaai_draft/*.tex` — AAAI 主论文。**正文文字在 `aaai_draft/` 片段里改**，
  `main_aaai.tex` 只管前导块 / 图环境 / 装配。
- `figs/` — 主论文 6 图：teaser、method、mechanism、causality、boundary、tuned-lens
  （fig15 预览杠杆图 2026-07-17 起下沉 supplement，正文靠文字引用）。
- `main.tex` / `supplement.tex` — arXiv 28pp 轨 / AAAI 补充材料轨，与 AAAI 主稿**独立维护，别顺手混改**。
- `OUTLINE.md` — claim 真值表 C1–C28，一切数字的最终真值来源。
- `provenance.md` — 图表溯源。`AAAI_SPINE.md` — 行文脊柱与取舍判据。
- `aaai_kit/` — 官方 AuthorKit 副本。**格式 / 合规规则以其中 `AAAI27-writing-skill.md` 为准**，
  拿不准就查它或标"未确认"，不要凭记忆猜（2026-07-14 复现清单 embed/standalone 之坑）。

## 协作约定

- push 前先 `git fetch` + rebase；**禁止 force-push**。
- 涉及正文的提交，信息里注明重编译后的页数（如 `[8pp ✓]`）。
