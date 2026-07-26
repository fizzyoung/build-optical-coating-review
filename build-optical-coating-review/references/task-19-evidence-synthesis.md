# Task 19 证据综合

## 1. 任务名称和目标
跨文献综合共识、冲突、条件、方法差异、阶段性结论和研究空白，更新文献地图的学术关系。

## 2. 适用范围
通过 Task 18 的主张与证据；Narrative Review 采用结构化叙述综合，Systematic Review 遵循预先方案。

## 3. 前置条件
Task 18 已批准，核心主张达到最低核验等级。

## 4. 必需和可选输入
必需：Claim–Evidence Matrix、证据卡、文献地图、研究问题。可选：质量评价、标准、实验设计分层和统计综合计划。

## 5. 执行步骤
按材料、工艺、结构、性能和应用聚类；比较方向与效应条件；解释样品、设备、测试和分析差异；区分共识、条件性结论、冲突和未知；为机制主张检查替代解释；从证据结构提炼空白；更新地图关系和路线图。

## 6. 应调用的 scripts、references 和 assets
读取 `literature-map.schema.json`、`optical-coating-integrated.md`、`systematic-review-branch.md`；使用 `literature_map.xlsx` 与 Claim workbook。调用 `scripts/build_literature_map.py` 和 `scripts/audit_claims.py`，不得由标题相似性推断关系。

## 7. 文件操作
创建 `19_evidence_synthesis/`；保存共识、争议、机制、条件和空白矩阵，以及地图更新前后差异。

## 8. 文献与证据追踪要求
每条综合结论连接多个 Source_ID 或明确标为单一来源；冲突关系保留双方原文位置；研究空白连接缺失节点、薄弱关系或方法偏差。

## 9. 输出文件
`consensus_matrix.xlsx`、`controversy_matrix.xlsx`、`mechanism_assessment.md`、`research_gap_matrix.xlsx` 和更新后的文献地图。

## 10. 质量检查和通过标准
综合按问题而非作者流水账组织；差异原因有证据；相关性不升级为因果；单一表征不充当完整机制；地图关系均可核验。

## 11. 阻断条件和风险
证据异质性无法解释、核心冲突缺全文、比较条件缺失、机制证据不足或空白仅凭“文献少”得出时阻断相应结论。

## 12. 用户确认问题
“请确认共识、条件性争议、机制边界和研究空白；批准后据此搭建三级大纲。”

## 13. 下一任务接口
向 Task 20 传递综合矩阵、通过的 Claim_ID、冲突、研究空白、地图和建议图表。

## 14. 最小示例
不同研究对偏压与应力关系结论相反时，先分层基底温度、氢含量、膜厚和测量方法；无法统一则保留争议，不写成单调普遍规律。
