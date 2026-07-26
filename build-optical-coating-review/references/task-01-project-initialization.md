# Task 01 项目初始化

## 1. 任务名称和目标
把用户课题、用途、期限、资源和 Step 00 能力固化为可恢复项目，分配稳定项目 ID 和控制文件。

## 2. 适用范围
所有新项目；恢复既有项目时使用 `state-machine.md` 的恢复顺序，不重复初始化。

## 3. 前置条件
Step 00 为 `APPROVED` 或 `SKIPPED_WITH_RISK`，且所有未核验平台已处理。

## 4. 必需和可选输入
必需：题目、综述用途、目标读者、截止日期、可用人力和已批准预检。可选：目标期刊、已有大纲、文献库、团队分工和写作语言偏好。

## 5. 执行步骤
生成项目 ID；复制状态和清单模板；建立 00–21 任务目录；记录研究目标、成功标准、范围假设、数据库能力、交付格式、时间约束和风险；将 Task 01 设为 `REVIEW_REQUIRED`。

## 6. 应调用的 scripts、references 和 assets
读取 `state-machine.md`、`schema-and-template-map.md`；由 `scripts/init_project.py` 复制 `project_state.yaml`、`project_manifest.json`、`task_status.yaml`、`stage_report.md` 并执行确定性、无覆盖初始化。

## 7. 文件操作
创建 `01_project_initialization/working|outputs|qa|logs` 及项目级 `working/outputs/qa/logs`；计算输入哈希；批准版本采用新文件名，不覆盖。

## 8. 文献与证据追踪要求
导入的已有记录只登记原始文件和格式，不在本任务生成未经核验的 DOI、Source_ID 或全文状态。

## 9. 输出文件
`project_brief.md`、`project_state.yaml`、`project_manifest.json`、任务登记、决策日志、风险清单和人工核查清单。

## 10. 质量检查和通过标准
工作目录可写；项目 ID 唯一；题目、用途、期限、责任人和能力边界明确；控制文件可解析并符合 Schema；恢复入口明确。

## 11. 阻断条件和风险
项目目标或交付物不明确、目录不可持久化、输入版本冲突或关键期限缺失时阻断。不得在临时目录中建立唯一项目副本。

## 12. 用户确认问题
“请确认项目目标、截止日期、目录和能力边界是否正确；确认后进入综述类型判定。”

## 13. 下一任务接口
向 Task 02 传递项目简报、资源边界和用户正式决策。

## 14. 最小示例
项目题目登记为“红外硫系玻璃基底 DLC 薄膜：材料基础、制备技术与应用进展”，用途为中文学术综述，过程报告默认中文，但写作语言仍留待 Task 21A 决定。
