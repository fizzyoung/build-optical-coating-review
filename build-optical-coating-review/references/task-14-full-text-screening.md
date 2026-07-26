# Task 14 全文筛选分类

## 1. 任务名称和目标
基于实际全文完成最终纳入、排除和二三级主题分类，并生成文献地图初版。

## 2. 适用范围
Task 13 的 `INCLUDE` 与 `UNCERTAIN` 记录；无全文记录不得伪装全文筛选。

## 3. 前置条件
Task 13 已批准；全文文件与 Source_ID 的初步映射可用。

## 4. 必需和可选输入
必需：筛选协议、Source_ID、全文或明确缺失状态。可选：OCR 文本、补充材料、标准、专利和第二审阅者判断。

## 5. 执行步骤
核对全文与题录；定位研究对象、材料、基底、膜层、工艺和结果；应用全文排除码；为纳入文献分配二三级主题和用途层级；记录边界与冲突；基于真实 Source_ID 建立文献地图节点和经证据支持的关系初版。

## 6. 应调用的 scripts、references 和 assets
读取 `literature-map.schema.json`、`optical-coating-integrated.md`；使用 `literature_registry.xlsx` 和 `literature_map.xlsx`。调用 `scripts/build_literature_map.py` 生成仅含显式 Source_ID 和已核验关系的地图。

## 7. 文件操作
创建 `14_full_text_screening/`；保存最终筛选表、排除日志、主题分类和地图初版；PDF 本体不移动时保存稳定相对路径与哈希。

## 8. 文献与证据追踪要求
全文决定记录页码或章节；地图关系必须连接真实 Source_ID 和依据；不能凭题名相似创建 `SUPPORTS`、`CONTRADICTS` 或方法继承关系。

## 9. 输出文件
最终纳入库、`full_text_exclusion_log.xlsx`、主题分类、`literature_map.xlsx/.md/.json` 初版。

## 10. 质量检查和通过标准
每个决定说明是否实际读到全文；排除理由可定位；主题层级与研究问题相连；地图节点与 Source Registry 一致，关系有依据和核验等级。

## 11. 阻断条件和风险
全文缺失、错配、扫描不可读、页码不稳定、协议无法处理新类型或关系证据不足时阻断或保留 `UNCERTAIN`。

## 12. 用户确认问题
“请确认最终纳入排除、主题分类和文献地图初版；缺失全文如何处理也需明确决定。”

## 13. 下一任务接口
向 Task 15 传递最终纳入库、全文映射、排除日志、主题和地图初版。

## 14. 最小示例
全文确认使用 Ge-As-Se 基底和 DLC 过渡层后纳入界面工程主题；若 PDF 实际是同题名会议摘要，则标记 `MISMATCHED` 并阻断，不按全文纳入。
