# Task 02 综述类型判定

## 1. 任务名称和目标
区分 Narrative Review 与 Systematic Review，避免因检索较广就错误使用“系统综述”名称。

## 2. 适用范围
所有项目；选择 Systematic Review 时必须同时加载 `systematic-review-branch.md`。

## 3. 前置条件
Task 01 已批准，项目目标、期限、资源和数据库能力明确。

## 4. 必需和可选输入
必需：研究目的、问题类型、预期透明度、数据库能力、人力和期限。可选：注册平台、协议模板、双人筛选资源和偏倚评价工具。

## 5. 执行步骤
比较两类综述在问题结构、协议、检索复现、筛选、偏倚风险和综合方法上的要求；评估项目是否能满足 Systematic Review 的最低条件；形成推荐与备选方案。

## 6. 应调用的 scripts、references 和 assets
读取 `systematic-review-branch.md`、`state-machine.md`。输出使用项目 Markdown；用 `scripts/validate_project.py` 检查 review_type、状态与项目记录的一致性，Systematic Review 的学术合规仍按严格分支人工门禁。

## 7. 文件操作
创建 `02_review_type/`，保存类型评估和用户决策；更新 `project_state.yaml.review_type`，保留变更历史。

## 8. 文献与证据追踪要求
用于判断的同类综述或指南分配 Source_ID；政策和方法指南记录版本与访问日期。

## 9. 输出文件
`review_type_assessment.md`、类型决策记录，以及 Systematic 分支所需的初始合规缺口清单。

## 10. 质量检查和通过标准
推荐理由连接项目能力；若选 Systematic，协议、双人筛选、分歧处理、PRISMA、偏倚风险和标准化提取均有可行方案；否则明确采用 Narrative Review。

## 11. 阻断条件和风险
用户坚持 Systematic 名称但资源无法满足最低要求时阻断；不得伪装注册、双人筛选或 Meta-analysis。

## 12. 用户确认问题
“请明确批准 Narrative Review 或 Systematic Review；若批准后者，请同时确认协议和双人筛选安排。”

## 13. 下一任务接口
向 Task 03 传递已批准类型、方法学义务和未解决风险。

## 14. 最小示例
DLC—硫系玻璃主题若目标是材料与工艺进展综合、没有双人筛选资源，推荐 Narrative Review，并承诺公开检索式和筛选理由但不宣称 PRISMA 系统综述。
