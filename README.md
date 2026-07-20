# image-edit-lens-paper — AAAI-27 投稿协作仓库

面向扩散图像编辑器（Qwen-Image-Edit-2511，60 块 DiT）的 layer–time lens：
固定欠指定 prompt 下，seed-conditioned 实际结果可从早层预测；Qwen 在 L52–54
附近把 target-image code 翻译成速度场。Transplant 只建立 sufficiency，steering
只建立 carrier-bounded writability；不声称不可逆早期决定、细粒度必要性或架构普适机制。
主文与补充材料均报告一个 RESTORE 启发的预注册 attention-routing audit：
内容匹配 transplant 保持自然参考路由与几何，方向 steering 只写入颜色而不
保持几何。

**接手 / 改稿唯一入口：[`AAAI_HANDOFF.md`](AAAI_HANDOFF.md)。** 本 README 只做速览。

## 投稿交付物

| 文件 | 内容 | 验收状态（2026-07-19） |
|---|---|---|
| `main_aaai.pdf` | 主论文 + references + reproducibility checklist | **10 页：技术内容止于第 7 页，references 第 8 页，checklist 随后**；Letter；0 Type 3/overfull/undefined |
| `supplement.pdf` | 匿名补充材料 | **32 页，Letter**；0 Type 3/overfull/undefined；含完整 T11 attention-routing audit 与最近邻定位 |
| `reports/aaai27_anonymous_artifact.zip`（代码仓库） | 匿名代码/数据 artifact | **103 MiB**；Python/536 JSON/ZIP/manifest/二进制敏感串扫描通过；T11 recorder tests 7/7 |

`reproducibility_checklist.pdf` 仍可单独编译作检查，但当前官网要求 checklist
放在 paper references 之后，最终上传以已合并的 `main_aaai.pdf` 为准。

截止：Abstract 注册 **2026-07-21 AoE** · Full paper **2026-07-28 AoE** · Supplementary + 可运行代码 **2026-07-31 AoE**。

## 重建与验收（改正文后必跑，缺一不可）

```bash
pdflatex main_aaai.tex && bibtex main_aaai && pdflatex main_aaai.tex && pdflatex main_aaai.tex
pdfinfo main_aaai.pdf | grep Pages     # 10：7 页内容 + refs + 2 页 checklist
grep -c "undefined" main_aaai.log      # 必须 0
pdffonts main_aaai.pdf | grep -c "Type 3"  # 必须 0
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
- `supplement.tex` — AAAI 匿名补充材料，与主稿独立编译。
- `OUTLINE.md` — claim 真值表 C1–C28，一切数字的最终真值来源。
- `provenance.md` — 图表溯源。`AAAI_SPINE.md` — 行文脊柱与取舍判据。
- `aaai_kit/` — 官方 AuthorKit 副本。**格式 / 合规规则以其中 `AAAI27-writing-skill.md` 为准**，
  拿不准就查它或标"未确认"，不要凭记忆猜（2026-07-14 复现清单 embed/standalone 之坑）。

## 协作约定

- push 前先 `git fetch` + rebase；**禁止 force-push**。
- 涉及正文的提交，信息里注明重编译后的页数（如 `[8pp ✓]`）。
