# Step 00 数据库与运行环境预检

## 1. 任务名称和目标
在 Task 01 前核验数据库访问能力、本地文件与工具能力，形成真实能力边界，禁止把“网页可打开”当成“可检索、可导出或可访问全文”。

## 2. 适用范围
所有 Narrative Review 与 Systematic Review 项目；数据库清单和状态定义以 v2 规格及 `optical-coating-integrated` 的学科需求为准。

## 3. 前置条件
项目目录可写；用户已说明可能使用的机构账号、VPN 和本地软件。无前置任务，但状态必须从 `NOT_STARTED` 合法转换。

## 4. 必需和可选输入
必需：课题、可用数据库、机构权限、浏览器状态、本地文件格式需求。可选：已有 PDF、RIS/BibTeX/EndNote/Zotero 导出、OCR 和版本控制环境。

## 5. 执行步骤
逐项测试 WoS、Scopus、PubMed、Google Scholar、百度学术、Crossref、OpenAlex、GeoRef、Engineering Village、ScienceDirect、SpringerLink、CNKI、万方；登记 L0–L5、访问状态、测试日期、真实测试式和限制。随后检查 Markdown、CSV/XLSX、DOCX、JSON/YAML、PDF、OCR、脚本、联网、浏览器、持久目录、临时目录、版本控制和断点恢复。

## 6. 应调用的 scripts、references 和 assets
读取 `state-machine.md`、`database-access-and-search.md`；复制 `assets/templates/preflight_and_roadmap.xlsx`。使用 `scripts/init_project.py` 进行无覆盖初始化，并用 `scripts/validate_project.py` 检查持久状态、目录、输出哈希和恢复约束。

## 7. 文件操作
创建 `00_preflight/`，保存数据库访问表、环境检查表和受限能力说明。登录信息、Cookie、令牌和密码不得写入项目或日志。

## 8. 文献与证据追踪要求
本步骤不创建虚假 Source_ID。测试检索若保留记录，标明仅为能力测试并登记真实来源、日期和结果数。

## 9. 输出文件
`database_access_check.xlsx`、`environment_preflight.md`、风险与人工操作清单，以及更新后的 `project_state.yaml`。

## 10. 质量检查和通过标准
进入 Task 01 前，必需平台不得保留 `UNVERIFIED`；每个平台记录字段完整；L4/L5 仅在实际导出/全文访问成功后赋值；项目需要的文件能力至少有一条可行路径。

## 11. 阻断条件和风险
登录、VPN、验证码、订阅、地区限制或浏览器权限立即暂停；不得规避访问控制。项目关键平台不可用时设 `BLOCKED`，或由用户明确批准 `USER_WAIVED`/`NOT_REQUIRED_FOR_THIS_PROJECT`。

## 12. 用户确认问题
“以上数据库与本地能力状态是否准确？请回复‘确认通过’，或指出需要重测、豁免或补充的平台。”

## 13. 下一任务接口
向 Task 01 传递已批准的访问矩阵、环境能力、风险和人工操作要求；未获批准不得初始化正式项目。

## 14. 最小示例
对 DLC—硫系玻璃课题实际测试 WoS、OpenAlex、CNKI 与 ScienceDirect；若 CNKI 需机构登录，则记录 `LOGIN_REQUIRED` 和当前 L1，而不是宣称已获得中文核心文献。
