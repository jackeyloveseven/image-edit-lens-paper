# AAAI-27 论文写作 Skill

用于指导 AAAI-27 投稿论文的写作、排版与检查，避免因格式或流程问题被 desk reject。

> 项目状态（2026-07-22）：Abstract 截止已过；Full Paper（2026-07-28 AoE）
> 与 Supplementary/Code（2026-07-31 AoE）尚未到期。当前仓库使用
> `main_aaai.tex` + `aaai2027.sty` + `aaai2027.bst`，不是下文模板示例名。

---

## 1. 关键时间节点

| 事项 | 截止时间（均为 UTC-12） |
|---|---|
| OpenReview 作者注册开放 | 2026-06-17 |
| 投稿系统开放 | 2026-06-30 |
| Abstract 提交 | 2026-07-21 |
| 全文（Full Paper）提交 | 2026-07-28 |
| Supplementary / Code 提交 | 2026-07-31 |
| Phase 1 拒稿通知 | 2026-09-24 |
| Author feedback 窗口 | 2026-10-19 ~ 10-25 |
| 最终录用通知 | 2026-11-30 |
| Camera-ready 提交 | 2026-12-14 |
| 会议召开 | 2027-02-16 ~ 02-23（蒙特利尔） |

> 标题/摘要在 Full Paper 截止前可修改，之后不可再改动标题与作者。

---

## 2. 模板与文件选择

- **本仓库投稿入口**：`main_aaai.tex`，加载 `\usepackage[submission]{aaai2027}`。
- **录用后**：切换为 `CameraReady2027.tex`，补充作者、单位、邮箱、ORCID、Acknowledgements。
- 本仓库配套文件：`aaai2027.sty`、`aaai2027.bst`、`references.bib`。
- **禁止修改**模板的页边距、字号、行距、字体、双栏结构。

写作全程建议只用 Anonymous 版本，录用后再切换，不要中途混用。

---

## 3. 页面与格式硬性要求

- 版式：双栏（two-column），US Letter（8.5 × 11 inch），PDF，Type 1 / TrueType 字体。
- **正文（技术内容）最多 7 页**，包含：Abstract、Introduction、Related Work、Method、Experiments、Conclusion 及其中所有图表。
- **参考文献（References）不计入 7 页技术内容**，但主 PDF 总长最多 9 页，即 references 最多额外 2 页。
- **Reproducibility Checklist 不计入正文页数**，单独上传。
- Acknowledgements 投稿版必须删除，仅 Camera-ready 版可加入。

写作时的页数分配建议：
- Introduction + Related Work：控制在 1~1.5 页
- Method：2~2.5 页
- Experiments：2.5~3 页
- Conclusion：≤0.5 页
- 消融实验、更多细节 → 放入 Supplementary，不占正文页数

---

## 4. 双盲匿名要求（Double-Blind）

投稿版本中**必须删除或避免**：
- 作者姓名、单位、邮箱、ORCID
- 可识别身份的致谢
- 可识别身份的项目名称/资助编号
- 指向自己 GitHub 账号 / 个人主页的链接
- 行文中出现"我们之前的工作 [X]"这种暴露身份的自引表述，应改为第三人称中性表述

可用占位符：paper number、keywords 替代作者信息。

---

## 5. Supplementary Material 规则

- 可提交：Supplementary Document、Code、Data、更多实验、证明、算法细节。
- 截止时间比正文晚 3 天（2026-07-31）。
- **不接受"代码录用后公开"的承诺**：审稿人会将其视为"没有代码"处理，务必在投稿时就提供可运行的代码/数据。
- 复现所需信息（数据集处理、超参数、训练细节等）应写入正文或 Code and Data Supplement；证明、假设、伪代码等技术细节可放入 Supplementary Document。

---

## 6. Reproducibility Checklist

- AAAI-27 强制要求，单独上传，不占正文页数。
- 审稿人会参考此 checklist 评估论文，并计入最终决定。
- 写作时应对照 checklist 逐条核实，提前准备，避免临时补充。

---

## 7. 投稿数量与一稿多投

- 每位作者最多 10 篇投稿（Technical Track，不含 AI Alignment / AI for Social Impact track）。
- 投稿后作者名单不可增删。
- **禁止**同时投稿其他 archival 会议/期刊（如 CVPR、ICCV、ECCV、NeurIPS、ICML、ICLR、TPAMI、TNNLS、TIP 等）。
- arXiv 预印本、非 archival workshop 允许。
- 若已有稿件在其他 venue 审稿，须在 AAAI-27 投稿前撤回。
- 投稿后到收到 AAAI-27 决定前，不可将同一或高度相似工作投往其他 archival venue。

### 重复/拆分投稿禁忌
- 同一工作做"化妆式"修改后拆分多投
- 将本应是一篇的贡献拆成数据集/方法/领域不同的多篇"薄切片"论文
- 提交经过混淆处理的"平行宇宙"版本

---

## 8. 引用与对比要求

- 应引用与内容最相关的已发表文献；对未发表的 arXiv 工作可不强制引用，但若该工作在领域内广为人知，评审仍可能据此评估新颖性。
- 全文截止日（2026-07-28）前 2 个月内发表的论文视为"同期工作"，不强制要求对比，但 camera-ready 阶段建议补充讨论。

---

## 9. 写作时自查清单（Checklist）

写作/定稿前逐项确认：

- [ ] 使用 `main_aaai.tex` 的 `[submission]` 模式，而非 CameraReady 模板
- [ ] 双栏、US Letter、PDF、Type 1/TrueType 字体，未改动模板样式
- [ ] 正文（含图表）≤ 7 页
- [ ] 技术内容在第 7 页内结束；References 可紧随其后，主 PDF 总长 ≤9 页
- [ ] 已删除作者信息、单位、邮箱、ORCID、致谢
- [ ] 全文无暴露身份的自引表述或个人链接
- [ ] Method、Experiments 是重点，Related Work / Conclusion 精简
- [ ] 消融实验等次要内容移至 Supplementary
- [ ] 代码、数据已准备好，将随 Supplementary 一起提交（而非"录用后公开"）
- [ ] Reproducibility Checklist 已逐条填写并单独上传
- [ ] 确认未与其他 archival 会议/期刊重复投稿
- [ ] 确认作者总投稿数未超过 10 篇上限
- [ ] Abstract 与最终全文内容一致，未大幅改动

---

## 10. 使用建议（写作流程）

1. 先用 Anonymous 模板起草全文框架，实时统计页数，控制在 7 页以内。
2. 图片尽量精简、适当缩小分辨率/尺寸，避免因图占用过多版面。
3. Method 与 Experiments 部分优先保证完整性和清晰度。
4. 消融实验、额外可视化、证明细节放入 Supplementary Document。
5. 提前（而非最后一天）准备好代码仓库、数据说明、Reproducibility Checklist。
6. 定稿前用上方 Checklist 逐条核对一遍，确认无匿名性/页数/格式问题后再提交。
7. 录用后再切换 `CameraReady2027.tex`，补全作者信息与致谢。
