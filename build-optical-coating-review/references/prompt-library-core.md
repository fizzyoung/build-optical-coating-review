# Core Prompt Library

本文件提供可编辑的项目提示词母版。Task 05 后应把适用条目复制并改写为项目级 `prompt_library.md`，填入已批准范围、真实数据库能力、Source_ID 和 Claim_ID。提示词库是可编辑工作手册，不得替代 Skill 状态机、任务门禁、Schema、原始记录或阶段 4 的确定性脚本。

## Contents

1. 选题诊断
2. 已有综述比较
3. 术语扩展
4. 检索式设计
5. 筛选解释
6. 全文精读
7. 证据卡
8. 争议综合
9. 研究空白
10. 大纲审查
11. 段落写作
12. 引用核查
13. 期刊匹配
14. 审稿回复

## 使用规则

- 只使用已批准任务输出和已核验来源；缺失信息明确标为待补充。
- 保留论文原始题名、术语、公式、数值、单位和正式引文。
- 输出必须能回写项目模板；不得在提示词回答中虚构 Source_ID、Claim_ID、DOI、全文位置或数据库结果。
- 遇到登录、VPN、验证码、付费墙、全文缺失、元数据冲突、范围判断或证据不足时停止并登记人工操作。
- 将每条提示词的执行记录绑定到任务、输入版本、输出版本和日期。

## 1. 选题诊断

- `prompt_id`: `CORE-TOPIC-DIAGNOSIS-01`
- `phase`: Task 03-05，定题
- `intent`: 判断课题范围、创新空间、证据可得性和执行风险。
- `when_to_use`: 已形成初始研究方向，但尚未批准最终题目时。
- `required_inputs`: 项目简报、综述类型、范围声明、已有综述矩阵、数据库预检结果。
- `tool_or_database_prerequisites`: Step 00 已批准；至少能核验题录和摘要，动态期刊信息需联网。
- `prompt_text`: 分析给定研究方向，生成至少 3 个边界清楚的候选题。逐项比较研究对象、材料/基底、膜层、工艺、性能、应用、时间范围、与已有综述的差异、证据可得性、预计贡献和主要风险。对每项判断标明所用 Source_ID 或“待核验”，不要把检索数量少直接称为研究空白。给出推荐题目、拒绝其他题目的理由和必须由用户决定的问题。
- `expected_outputs`: 候选题评分矩阵、推荐题目、项目诊断要点、路线图初始项和待决策清单。
- `stop_conditions`: 已有综述无法核验；范围关键选择缺失；核心数据库均不可检索；证据量明显不足或过载。
- `quality_checks`: 至少 3 个候选题；差异化可追溯；题目不过大或过窄；每个核心问题连接证据任务与交付物。

## 2. 已有综述比较

- `prompt_id`: `CORE-REVIEW-COMPARISON-01`
- `phase`: Task 04，定题
- `intent`: 建立已有综述的覆盖、结构、贡献与更新空间比较。
- `when_to_use`: 需要判断新综述是否重复以及哪些结构可借鉴时。
- `required_inputs`: 已核验综述记录、摘要或全文位置、范围声明、时间与语言边界。
- `tool_or_database_prerequisites`: 可访问题录/摘要；比较详细方法或结论时必须有合法全文。
- `prompt_text`: 对输入的综述逐篇提取检索截止时间、对象、材料、工艺、性能、应用、纳入文献类型、结构、主要贡献、明确局限和证据等级。生成交叉覆盖矩阵，区分直接重合、部分重合、结构参考和背景用途。只在有证据时提出更新空间，并把可借鉴结构绑定到 Source_ID 和原文位置。
- `expected_outputs`: 已有综述矩阵、覆盖地图、结构参考登记、可核验的更新机会。
- `stop_conditions`: 仅凭标题推断内容；综述版本或全文不匹配；结构借鉴来源无法定位。
- `quality_checks`: 时间覆盖与主题覆盖分开；贡献和局限不混写；没有把“未发现”表述为“并不存在”。

## 3. 术语扩展

- `prompt_id`: `CORE-TERM-EXPANSION-01`
- `phase`: Task 06-07，建库
- `intent`: 建立中英文术语表和可组合概念组。
- `when_to_use`: 范围已批准、准备设计数据库检索式时。
- `required_inputs`: 批准题目、PICO/对象框架或研究问题、领域包、种子文献术语。
- `tool_or_database_prerequisites`: 可查权威词表、标准或数据库索引词；具体数据库语法尚不在此步骤假定。
- `prompt_text`: 围绕基底、膜层、界面、制备、结构、光学、机械、环境、制造和应用生成术语。每个术语记录中文、标准英文、缩写、旧称、拼写变体、上下位词、排除歧义、来源和适用数据库。对 DLC 区分 a-C、a-C:H、ta-C、ta-C:H、掺杂和复合体系；对硫系玻璃区分元素体系与具体组成。将术语组织为可独立测试的概念组，不直接拼成最终查询。
- `expected_outputs`: 术语表、概念组、歧义与排除清单、待数据库验证的语法问题。
- `stop_conditions`: 术语来源不明；材料类别被错误等同；关键对象存在未决边界。
- `quality_checks`: 中英文双向覆盖；缩写无歧义；同义词与上下位词分开；排除词经已知相关文献反测。

## 4. 检索式设计

- `prompt_id`: `CORE-QUERY-DESIGN-01`
- `phase`: Task 08-10，建库
- `intent`: 设计可复现的宽、平衡、精确三级检索策略并适配各数据库。
- `when_to_use`: 概念组和数据库计划已批准时。
- `required_inputs`: 术语表、概念组、数据库访问矩阵、研究范围、种子文献。
- `tool_or_database_prerequisites`: 目标数据库至少 L2；已现场核验字段、短语、通配、邻近和长度规则。
- `prompt_text`: 先生成平台中立的布尔逻辑，再为每个获批数据库翻译为宽、平衡、精确三级查询。逐条说明字段、过滤器、预期用途、召回风险和精度风险。用已知相关文献做正向校验，用典型噪声做反向校验。不要编造结果数；实际执行后才登记 query_id、时间、精确字符串、结果数和导出批次。
- `expected_outputs`: 平台中立逻辑、数据库专用检索式、测试矩阵、查询版本和运行记录字段。
- `stop_conditions`: 数据库语法未核验；登录/CAPTCHA；查询被截断或拒绝；种子文献无法召回且原因未解释。
- `quality_checks`: 三级查询目的不同；过滤条件透明；每条实跑查询可复现；报告数与导出数可对账。

## 5. 筛选解释

- `prompt_id`: `CORE-SCREENING-RATIONALE-01`
- `phase`: Task 12-14，建库
- `intent`: 对题名摘要或全文筛选给出一致、可审计的建议与理由。
- `when_to_use`: 纳排标准已批准并需要处理待筛选记录时。
- `required_inputs`: Source_ID、题名、摘要或全文、纳排标准版本、已有人工决策示例。
- `tool_or_database_prerequisites`: 题名摘要筛选至少有真实题录；全文筛选必须打开匹配的合法全文。
- `prompt_text`: 按当前纳排标准逐条评估记录，输出 INCLUDE、EXCLUDE 或 UNCERTAIN 建议、命中的标准编号、证据文本、解释和需人工核查项。信息缺失时选择 UNCERTAIN，不从标题补全材料、工艺或结果。Systematic Review 中只提供辅助建议，不冒充第二位独立人类筛选者。
- `expected_outputs`: 筛选建议、标准编号、排除原因、证据位置和冲突/人工复核队列。
- `stop_conditions`: 全文与题录不匹配；标准版本不明；关键信息仅在不可访问全文中；两个人类审稿者发生未解决冲突。
- `quality_checks`: 排除原因单一且可复核；同类记录标准一致；UNCERTAIN 不被强制归类；系统综述角色表述真实。

## 6. 全文精读

- `prompt_id`: `CORE-FULLTEXT-READING-01`
- `phase`: Task 16，搭架
- `intent`: 从全文提取可定位、可比较的研究设计与结果。
- `when_to_use`: 文献已通过全文筛选并进入精读优先队列时。
- `required_inputs`: Source_ID、匹配全文、结构化阅读模板、领域包、研究问题。
- `tool_or_database_prerequisites`: 合法全文可读；扫描件需要可验证 OCR；图表提取需要页码和元素定位能力。
- `prompt_text`: 从头至尾阅读全文，分别记录研究目的、样品链、基底组成、膜层与层序、工艺参数、表征方法、测试条件、结果、误差、作者解释、作者推测、局限和与研究问题的关系。每个数字或机制结论给出页码、章节、图或表位置。区分正文报告值、图中读取值、换算值和模型值；无法读取处明确标记。
- `expected_outputs`: 结构化精读记录、可用证据位置、数据冲突、缺失字段和后续证据卡候选。
- `stop_conditions`: PDF 错配/残缺；OCR 破坏关键数字或公式；补充材料缺失导致核心结论不可核验。
- `quality_checks`: 关键结果达到 V4；观察、解释、推测和 Skill 综合分开；条件与单位完整；未把 Raman 拟合当作精确 sp3。

## 7. 证据卡

- `prompt_id`: `CORE-EVIDENCE-CARD-01`
- `phase`: Task 17-18，搭架
- `intent`: 将可用证据封装为可回查的主张候选。
- `when_to_use`: 全文精读获批，需要构建 Claim-Evidence Matrix 时。
- `required_inputs`: Source_ID、全文精读记录、原文位置、研究问题、`evidence-card.schema.json`。
- `tool_or_database_prerequisites`: 原文位置可回查；元数据至少 V2，核心证据通常 V4。
- `prompt_text`: 为一项原子化证据生成证据卡，包含原文结论/数据、证据类型、样品与条件、方法、原文位置、核验等级、支持强度、适用边界、局限、替代解释、可支持与不可支持的主张。机制卡必须逐段检查因果链；定量卡必须保留单位、误差和比较基线。
- `expected_outputs`: 符合 Schema 的证据卡、候选 Claim_ID 关系和人工复核标记。
- `stop_conditions`: 找不到原文位置；数值条件不全；主张范围大于证据；元数据冲突未关闭。
- `quality_checks`: 一卡一主要证据；来源与位置可回查；支持/反驳/无关关系明确；证据强度不过度提升。

## 8. 争议综合

- `prompt_id`: `CORE-CONTROVERSY-SYNTHESIS-01`
- `phase`: Task 19，搭架
- `intent`: 解释跨研究结论不一致及其条件边界。
- `when_to_use`: Claim-Evidence Matrix 已批准且同一主张存在冲突证据时。
- `required_inputs`: Claim_ID、支持与反驳证据卡、样品/工艺/测试条件、质量与核验等级。
- `tool_or_database_prerequisites`: 关键全文证据达到 V4；可按领域包字段比较。
- `prompt_text`: 围绕指定 Claim_ID 分组比较支持、反驳和条件性证据。优先检查基底组成、DLC 类型、界面层、膜厚、应力、工艺能量/温度、光学波段、机械载荷、环境标准、样本数和测量方法。区分真实矛盾、条件差异、测量差异、证据不足和术语混用。形成条件化结论，不按论文数量投票。
- `expected_outputs`: 争议矩阵、差异原因排序、条件化共识、残余不确定性和新增研究问题。
- `stop_conditions`: 关键条件缺失；冲突只来自摘要；比较跨越不可换算标准；证据质量无法评估。
- `quality_checks`: 每项解释有证据；替代解释被讨论；少数高质量反证未被多数低质量记录淹没；措辞与核验等级一致。

## 9. 研究空白

- `prompt_id`: `CORE-RESEARCH-GAP-01`
- `phase`: Task 19-20，搭架
- `intent`: 从证据地图识别可证成、可行动的研究空白。
- `when_to_use`: 文献地图、证据矩阵和争议综合已形成时。
- `required_inputs`: 研究问题、文献地图、Claim-Evidence Matrix、时间/方法/材料覆盖、未关闭风险。
- `tool_or_database_prerequisites`: 核心数据库检索和引用追踪已记录；主要全文缺口已知。
- `prompt_text`: 从材料、工艺、界面、表征、性能、标准、寿命、制造放大和系统应用维度寻找证据断点。对每个候选空白说明已覆盖范围、缺失证据、检索与全文限制、为何重要、可检验问题和所需方法。区分真正证据空白、报告不足、数据库不可访问、术语遗漏和范围外问题。
- `expected_outputs`: 分级空白清单、证据依据、可信度、可行动研究问题和路线图更新项。
- `stop_conditions`: 检索覆盖不可审计；空白仅依据“命中少”；关键数据库或语种被省略且未批准风险。
- `quality_checks`: 每个空白连接地图节点/关系与 Claim；限制透明；不使用“首次”“无人研究”等绝对表述，除非有充分验证。

## 10. 大纲审查

- `prompt_id`: `CORE-OUTLINE-REVIEW-01`
- `phase`: Task 20，搭架
- `intent`: 检查三级大纲的论证递进、证据配置和图表可追溯性。
- `when_to_use`: 已生成候选大纲但尚未请求 Task 20 批准时。
- `required_inputs`: 三级大纲、研究问题、Claim-Evidence Matrix、文献地图、图表计划、篇幅约束。
- `tool_or_database_prerequisites`: 核心 Claim 和图表来源可回查；目标期刊结构要求若使用必须联网核验。
- `prompt_text`: 逐级审查大纲。对每个三级标题说明其问题、中心命题、主要证据、比较、冲突、局限、阶段判断和图表。识别作者流水账、重复、章节失衡、无证据主张、孤立图表和范围漂移。把每条修改建议标记优先级、位置、证据和关闭条件。
- `expected_outputs`: `outline_review_report.md` 内容、修订建议、章节证据覆盖表和阻断项。
- `stop_conditions`: 核心章节无 Claim；关键争议无位置；图表版权或来源不明；大纲版本冲突。
- `quality_checks`: 每个三级标题连接至少一个合格 Claim_ID/Source_ID；关键问题关闭前不批准；未经明确批准不进入 Task 21。

## 11. 段落写作

- `prompt_id`: `CORE-PARAGRAPH-WRITING-01`
- `phase`: Task 21B，成稿
- `intent`: 按批准大纲和证据边界写出可审计的综述段落。
- `when_to_use`: 写作语言与当前章节已批准，且该段证据子集完整时。
- `required_inputs`: 批准大纲位置、段落功能、Claim_ID、证据卡、正式引文、术语规则、语言决定。
- `tool_or_database_prerequisites`: 核心事实至少 V3；机制、定量和图表证据至少 V4。
- `prompt_text`: 仅用给定 Claim 和证据写一个综述段落，按中心观点、主要证据、跨研究比较、差异原因、适用条件、局限和阶段性判断组织。每个事实、数字和机制紧邻正式引文；对证据不一致使用条件化措辞。不要新增未登记主张，不要写作者流水账，不要把相关性升级为因果。
- `expected_outputs`: 带正式引文的段落、内部 Claim/Source 审计映射、未解决问题。
- `stop_conditions`: 段落需要的新主张没有 Claim_ID；证据低于门禁；引用与原文不符；批准大纲不支持该段。
- `quality_checks`: 一段一中心功能；每项主张可追溯；比较条件完整；措辞强度不超过证据；完成当前章节后必须暂停审批。

## 12. 引用核查

- `prompt_id`: `CORE-CITATION-AUDIT-01`
- `phase`: Task 21D，成稿
- `intent`: 逐句检查主张、引文、数字和原文证据的一致性。
- `when_to_use`: 全文整合稿已批准进入引用审计时。
- `required_inputs`: 审计版稿件、Claim-Evidence Matrix、Source registry、全文位置、图表追踪。
- `tool_or_database_prerequisites`: 可访问被核查的真实来源；DOI/元数据可交叉验证。
- `prompt_text`: 逐句识别可核查事实、数字、比较、机制、因果、范围和引文。为每项登记 Claim_ID、Source_ID、原文位置、核验等级、支持/部分支持/不支持、问题类型和建议修正。重点查找无来源数字、二次引用、引用漂移、范围扩大、条件丢失、同引文支持多项无关主张和图表来源缺口。
- `expected_outputs`: 引用审计记录、阻断项、可执行修订和复核状态。
- `stop_conditions`: 来源无法打开或错配；主张没有证据记录；图表关键单元格无法追溯；DOI 冲突未解决。
- `quality_checks`: 核心句逐句覆盖；机制/定量达到 V4；修订后复核；所有关键问题关闭前不生成清洁投稿版。

## 13. 期刊匹配

- `prompt_id`: `CORE-JOURNAL-MATCH-01`
- `phase`: Task 21F，成稿
- `intent`: 基于当前官方政策比较目标期刊的学术适配、成本和投稿风险。
- `when_to_use`: 清洁候选稿和用户偏好已形成时。
- `required_inputs`: 稿件题目/摘要/范围、文章类型、篇幅、图表、开放获取与预算偏好、候选期刊。
- `tool_or_database_prerequisites`: 必须联网访问期刊/出版商官方页面并记录核验日期；指标来源需标明年份和来源。
- `prompt_text`: 为候选期刊核验 scope、可投稿综述类型、是否邀约、字数、图表、参考文献、APC、开放获取、版权、数据和 AI 政策。记录官方 URL、页面名称和访问日期。比较主题适配、读者、格式改造成本、政策风险与备选顺序；无法确认的信息标为人工核查，不用记忆补齐。
- `expected_outputs`: 期刊比较矩阵、推荐顺序、格式差距、成本与风险、官方来源记录。
- `stop_conditions`: 官方页面不可访问；文章类型/邀约要求不明确；费用或政策相互冲突；用户尚未决定关键预算或投稿目标。
- `quality_checks`: 动态字段均有当前官方证据；学术适配与指标分开；不保证录用；最终选择由用户明确批准。

## 14. 审稿回复

- `prompt_id`: `CORE-REVIEWER-RESPONSE-01`
- `phase`: Task 21H，返修
- `intent`: 形成意见、响应、证据、稿件修改和位置闭环。
- `when_to_use`: 已收到真实编辑/审稿意见和对应投稿版本时。
- `required_inputs`: 原始意见、投稿稿件版本、期刊要求、Claim-Evidence Matrix、实际完成的修改或实验。
- `tool_or_database_prerequisites`: 可读取带行号稿件和相关证据；新增期刊政策需联网核验。
- `prompt_text`: 逐条原样登记意见并分类严重度和响应类型。起草礼貌、直接的回复，说明同意、部分同意或有证据的不同意；列出实际修改文本、稿件位置、Claim_ID/Source_ID 和仍需作者完成的事项。不得编造实验、分析、页码、行号或已完成修改。跨意见冲突时先建立决策清单。
- `expected_outputs`: 审稿回复矩阵、逐条回复草稿、稿件修改建议、未关闭事项和最终 response letter 草案。
- `stop_conditions`: 意见文本不完整；稿件版本错配；要求新实验但尚未完成；作者立场或数据需确认；修改位置无法核验。
- `quality_checks`: 每条意见均闭环；回复与稿件实际修改一致；不同意有证据且语气专业；所有作者声明和新增结果经人工确认。

## 项目化规则

Task 05 创建项目级 `prompt_library.md` 时，只保留与已批准路线图相关的条目，并将泛化输入替换为项目文件、版本和 ID。后续在 Task 10、15、20 和 21 更新执行前提与输出路径，但保留旧版本。项目提示词库可由用户修改；任何修改若改变任务顺序、审批门禁、证据阈值或确定性文件操作，必须回到相应规范或脚本，而不能只改提示词。
