# Task 11 元数据清洗

## 1. 任务名称和目标
规范 DOI、题名、作者、年份、期刊和版本关系，合并重复记录但保留来源、异常和决策链。

## 2. 适用范围
Task 10 的全部原始导出及用户补充记录；支持 CSV、XLSX、RIS、BibTeX、EndNote XML、Zotero 映射和 JSON。

## 3. 前置条件
Task 10 已批准，原始导出只读保存且平台/查询标签完整。

## 4. 必需和可选输入
必需：全部原始记录、来源平台、查询 ID。可选：Crossref/OpenAlex 核验结果、Zotero 库、PDF 文件名和已有 DOI 清单。

## 5. 执行步骤
解析格式并保留原始字段；规范空白、大小写、DOI URL 和作者；按 DOI、规范题名、作者年份和版本关系分层判重；区分预印本、会议文与正式版本；核验冲突；分配稳定 Source_ID；输出合并和异常决策。

## 6. 应调用的 scripts、references 和 assets
读取 `source-record.schema.json`、`database-access-and-search.md`；使用 `literature_registry.xlsx`。依次调用 `scripts/import_records.py`、`scripts/deduplicate_records.py`、`scripts/validate_metadata.py`，保留导入、决策、冲突和外部核验状态。

## 7. 文件操作
创建 `11_metadata_cleaning/working|outputs|qa|logs`；原始记录不改；规范库和决策日志版本化；被替代记录通过 `supersedes_source_id` 连接。

## 8. 文献与证据追踪要求
Source_ID 一旦被引用不得重分配；V2 仅在题录和 DOI 已核验后赋值；元数据来源和核验日期必须保留。

## 9. 输出文件
主文献库、Source Registry、重复决策日志、元数据异常清单和导入统计。

## 10. 质量检查和通过标准
每条记录有唯一 Source_ID；重复决策可逆追踪；DOI 冲突未被静默覆盖；缺失字段明确为空；导入数、合并数、排除数和输出数守恒。

## 11. 阻断条件和风险
同 DOI 不同题名、同题名不同版本、解析失败、编码损坏或计数不守恒时阻断；不得凭相似题名自动永久合并。

## 12. 用户确认问题
“请确认重复与版本关系处理，特别是预印本/正式版和 DOI 冲突记录。”

## 13. 下一任务接口
向 Task 12 传递规范主库、稳定 Source_ID、异常和未决版本关系。

## 14. 最小示例
同一 DLC 论文的会议摘要与期刊全文分别保留 Source_ID，并用版本关系连接；期刊版作为主要证据，但不删除会议记录的来源轨迹。
