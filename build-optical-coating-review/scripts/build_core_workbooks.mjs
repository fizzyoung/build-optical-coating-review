import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { FileBlob, SpreadsheetFile, Workbook } = require("@oai/artifact-tool");

const skillRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const outputDir = path.join(skillRoot, "assets", "templates");
const qaDir = path.resolve(skillRoot, "..", "qa", "stage2", "xlsx");

const STATUS = ["NOT_STARTED", "IN_PROGRESS", "BLOCKED", "REVIEW_REQUIRED", "APPROVED", "REJECTED", "SKIPPED_WITH_RISK", "SUPERSEDED", "ARCHIVED"];
const VERIFY = ["V0", "V1", "V2", "V3", "V4", "V5"];
const HUMAN = ["UNREVIEWED", "REVIEW_REQUIRED", "ACCEPTED", "REVISE", "REJECTED"];
const STRENGTH = ["UNASSESSED", "WEAK", "MODERATE", "STRONG"];
const BOOLEAN = ["TRUE", "FALSE"];

const colors = {
  header: "#174A5B",
  headerText: "#FFFFFF",
  guideHeader: "#365B4A",
  border: "#B8C2C8",
  required: "#E8F1ED",
  optional: "#F3F5F6",
};

const databaseRows = [
  ["Web of Science Core Collection", "COMPREHENSIVE"],
  ["Scopus", "COMPREHENSIVE"],
  ["PubMed", "DISCIPLINE"],
  ["Google Scholar", "DISCOVERY"],
  ["百度学术", "DISCOVERY"],
  ["Crossref", "METADATA_VERIFICATION"],
  ["OpenAlex", "METADATA_VERIFICATION"],
  ["GeoRef", "DISCIPLINE"],
  ["Engineering Village", "DISCIPLINE"],
  ["ScienceDirect", "PUBLISHER_FULL_TEXT"],
  ["SpringerLink", "PUBLISHER_FULL_TEXT"],
  ["CNKI", "CHINESE_DATABASE"],
  ["万方", "CHINESE_DATABASE"],
].map(([database_name, database_category]) => ({ database_name, database_category, access_status: "UNVERIFIED", access_level: "L0" }));

const specs = [
  {
    file: "preflight_and_roadmap.xlsx",
    sheets: [
      {
        name: "Database Access",
        fields: [
          ["database_name", "string", true, "平台名称"], ["database_category", "enum", true, "平台类别"], ["access_status", "enum", true, "访问状态"], ["access_level", "enum", true, "L0-L5 能力等级"],
          ["access_route", "string", false, "机构、VPN 或公开访问路径"], ["test_date", "date", false, "ISO 日期"], ["institutional_login", "boolean", true, "是否使用机构登录"], ["vpn_required", "boolean", true, "是否需要 VPN"],
          ["search_available", "boolean", true, "是否可检索"], ["record_page_available", "boolean", true, "是否可查看题录页"], ["abstract_available", "boolean", true, "是否可查看摘要"], ["full_text_available", "boolean", true, "是否可合法访问全文"],
          ["citation_export_available", "boolean", true, "是否可导出引文"], ["supported_export_formats", "array<string>", true, "分号分隔"], ["test_query", "string", false, "实际测试检索式"], ["test_result_count", "integer", false, "真实结果数量"],
          ["automation_restrictions", "string", false, "验证码、速率或条款限制"], ["known_limitations", "string", false, "已知限制"], ["user_confirmed", "boolean", true, "用户是否确认"], ["notes", "string", false, "补充说明"]
        ],
        rows: databaseRows,
        validations: { access_status: ["ACCESSIBLE", "PARTIALLY_ACCESSIBLE", "VPN_REQUIRED", "LOGIN_REQUIRED", "NO_SUBSCRIPTION", "CAPTCHA_OR_MANUAL_OPERATION_REQUIRED", "TEMPORARILY_UNAVAILABLE", "REGION_RESTRICTED", "NOT_REQUIRED_FOR_THIS_PROJECT", "USER_WAIVED", "UNVERIFIED"], access_level: ["L0", "L1", "L2", "L3", "L4", "L5"], institutional_login: BOOLEAN, vpn_required: BOOLEAN, search_available: BOOLEAN, record_page_available: BOOLEAN, abstract_available: BOOLEAN, full_text_available: BOOLEAN, citation_export_available: BOOLEAN, user_confirmed: BOOLEAN }
      },
      {
        name: "Research Roadmap",
        fields: [
          ["schema_version", "string", true, "固定为 1.0.0"], ["roadmap_item_id", "id", true, "RM-000 格式稳定 ID"], ["research_question", "string", true, "核心研究问题"], ["stage", "enum", true, "STEP_00 或 STAGE_1-4"],
          ["task", "task_id", true, "STEP-00 或 TASK-01...TASK-21H"], ["prerequisites", "array<string>", true, "分号分隔"], ["evidence_needed", "array<string>", true, "至少一项，分号分隔"], ["preferred_sources", "array<string>", true, "分号分隔"],
          ["planned_deliverable", "string", true, "计划交付物"], ["decision_gate", "string", true, "批准条件"], ["risk", "string|null", false, "主要风险"], ["status", "enum", true, "任务状态"], ["owner", "string|null", false, "责任人"], ["last_updated", "date|null", false, "ISO 日期"]
        ],
        validations: { stage: ["STEP_00", "STAGE_1", "STAGE_2", "STAGE_3", "STAGE_4"], status: STATUS }
      }
    ]
  },
  {
    file: "literature_registry.xlsx",
    sheets: [
      {
        name: "Master Literature",
        fields: [
          ["schema_version", "string", true, "固定为 1.0.0"], ["source_id", "id", true, "SRC- 前缀稳定 ID"], ["title", "string|null", true, "原文题名"], ["authors", "array<string>", true, "分号分隔"], ["year", "integer|null", true, "出版年份"],
          ["journal", "string|null", true, "期刊或来源"], ["document_type", "enum", true, "文献类型"], ["doi", "string|null", false, "规范化 DOI"], ["url", "uri|null", false, "记录页或全文 URL"], ["language", "string|null", false, "语言"],
          ["database_sources", "array<string>", true, "分号分隔"], ["record_version", "string", true, "题录版本"], ["supersedes_source_id", "source_id|null", false, "被替代版本"], ["verification_level", "enum", true, "V0-V5"], ["verification_date", "date|null", false, "ISO 日期"],
          ["full_text_status", "enum", true, "全文状态"], ["screening_decision", "enum", true, "筛选决定"], ["screening_reason", "string|null", false, "筛选理由"], ["materials", "array<string>", true, "分号分隔"], ["substrates", "array<string>", true, "分号分隔"],
          ["coatings", "array<string>", true, "分号分隔"], ["deposition_routes", "array<string>", true, "分号分隔"], ["interface_strategies", "array<string>", true, "分号分隔"], ["optical_properties", "array<string>", true, "分号分隔"], ["mechanical_properties", "array<string>", true, "分号分隔"],
          ["environmental_properties", "array<string>", true, "分号分隔"], ["manufacturing_properties", "array<string>", true, "分号分隔"], ["characterization_methods", "array<string>", true, "分号分隔"], ["themes", "array<string>", true, "分号分隔"], ["research_stage", "string|null", false, "研究阶段"],
          ["intended_uses", "array<enum>", true, "CORE/SUPPORTING/BACKGROUND/METHOD/CONFLICT"], ["evidence_strength", "enum", true, "证据强度"], ["notes", "string|null", false, "补充说明"]
        ],
        validations: { document_type: ["JOURNAL_ARTICLE", "REVIEW", "CONFERENCE_PAPER", "BOOK_CHAPTER", "STANDARD", "PATENT", "THESIS", "PREPRINT", "REPORT", "OTHER"], verification_level: VERIFY, full_text_status: ["NOT_REQUESTED", "MISSING", "PARTIAL", "AVAILABLE", "UNREADABLE", "MISMATCHED"], screening_decision: ["UNSCREENED", "INCLUDE", "EXCLUDE", "UNCERTAIN", "BACKGROUND_ONLY", "METHOD_ONLY"], evidence_strength: STRENGTH },
        wholeNumbers: { year: [1600, 2200] }
      },
      {
        name: "Screening",
        fields: [["screening_id", "id", true, "筛选记录 ID"], ["source_id", "source_id", true, "稳定来源 ID"], ["screening_stage", "enum", true, "筛选阶段"], ["decision", "enum", true, "决定"], ["exclusion_reason", "string|null", false, "排除理由"], ["uncertainty", "enum", true, "不确定性"], ["full_text_used", "boolean", true, "是否实际使用全文"], ["reviewer", "string|null", false, "筛选者"], ["reviewed_at", "date|null", false, "ISO 日期"], ["notes", "string|null", false, "补充说明"]],
        validations: { screening_stage: ["TITLE", "ABSTRACT", "FULL_TEXT"], decision: ["INCLUDE", "EXCLUDE", "UNCERTAIN", "BACKGROUND_ONLY", "METHOD_ONLY"], uncertainty: ["LOW", "MEDIUM", "HIGH"], full_text_used: BOOLEAN }
      },
      {
        name: "Source Registry",
        fields: [["source_id", "source_id", true, "稳定来源 ID"], ["canonical_title", "string|null", true, "规范题名"], ["doi", "string|null", false, "规范化 DOI"], ["record_version", "string", true, "记录版本"], ["supersedes_source_id", "source_id|null", false, "替代关系"], ["verification_level", "enum", true, "V0-V5"], ["metadata_sources", "array<string>", true, "分号分隔"], ["pdf_path", "string|null", false, "项目内 PDF 路径"], ["pdf_sha256", "sha256|null", false, "PDF 哈希"], ["attachment_status", "enum", true, "附件状态"], ["manual_check_status", "enum", true, "人工核查状态"], ["notes", "string|null", false, "补充说明"]],
        validations: { verification_level: VERIFY, attachment_status: ["NONE", "AVAILABLE", "MISSING", "MISMATCHED", "UNREADABLE"], manual_check_status: HUMAN }
      }
    ]
  },
  {
    file: "evidence_and_claims.xlsx",
    sheets: [
      {
        name: "Claims",
        fields: [["schema_version", "string", true, "固定为 1.0.0"], ["claim_id", "claim_id", true, "CLM-章节-序号"], ["claim_text_zh", "string|null", true, "中文主张"], ["claim_text_en", "string|null", true, "英文主张"], ["claim_type", "enum", true, "主张类型"], ["source_ids", "array<source_id>", true, "分号分隔"], ["original_locations", "array<string>", true, "与来源顺序对应"], ["relations", "array<enum>", true, "SUPPORTS/CONTRADICTS/QUALIFIES/BACKGROUND_ONLY"], ["evidence_type", "enum", true, "证据类型"], ["evidence_strength", "enum", true, "证据强度"], ["consistency", "enum", true, "一致性"], ["applicability_conditions", "array<string>", true, "分号分隔"], ["limitations", "array<string>", true, "分号分隔"], ["intended_section", "string|null", false, "计划章节"], ["human_status", "enum", true, "人工状态"], ["minimum_verification_level", "enum", true, "最低核验等级"], ["notes", "string|null", false, "补充说明"]],
        validations: { claim_type: ["BACKGROUND", "DESCRIPTIVE", "COMPARATIVE", "QUANTITATIVE", "MECHANISTIC", "CAUSAL", "METHOD", "CONSENSUS", "CONTROVERSY", "RESEARCH_GAP", "APPLICATION"], evidence_type: ["METADATA", "ABSTRACT", "FULL_TEXT_STATEMENT", "TABLE", "FIGURE", "SUPPLEMENT", "STANDARD", "DERIVED_CALCULATION", "SYNTHESIS"], evidence_strength: STRENGTH, consistency: ["UNASSESSED", "CONSISTENT", "MIXED", "CONTRADICTORY", "SINGLE_SOURCE"], human_status: HUMAN, minimum_verification_level: VERIFY }
      },
      {
        name: "Evidence Cards",
        fields: [["schema_version", "string", true, "固定为 1.0.0"], ["evidence_card_id", "id", true, "EC- 前缀稳定 ID"], ["source_id", "source_id", true, "稳定来源 ID"], ["citation", "string|null", false, "规范引文"], ["research_question", "string|null", false, "对应研究问题"], ["material_system", "string|null", false, "材料体系"], ["substrate", "string|null", false, "基底"], ["coating", "string|null", false, "膜层"], ["deposition_method", "string|null", false, "沉积方法"], ["interface_strategy", "string|null", false, "界面策略"], ["process_conditions", "array<string>", true, "分号分隔"], ["characterization_methods", "array<string>", true, "分号分隔"], ["key_results", "array<structured>", true, "指标|值|单位|条件|位置，多条用分号"], ["author_interpretation", "array<string>", true, "分号分隔"], ["skill_assessment", "array<string>", true, "分号分隔"], ["supported_claim_ids", "array<claim_id>", true, "分号分隔"], ["comparison_uses", "array<string>", true, "分号分隔"], ["figure_table_uses", "array<string>", true, "分号分隔"], ["original_locations", "array<string>", true, "分号分隔"], ["verification_level", "enum", true, "V0-V5"], ["evidence_strength", "enum", true, "证据强度"], ["limitations", "array<string>", true, "分号分隔"], ["citation_risks", "array<string>", true, "分号分隔"], ["human_status", "enum", true, "人工状态"]],
        validations: { verification_level: VERIFY, evidence_strength: STRENGTH, human_status: HUMAN }
      },
      {
        name: "Figure-Table Trace",
        fields: [["schema_version", "string", true, "固定为 1.0.0"], ["trace_id", "id", true, "TRC- 前缀稳定 ID"], ["artifact_id", "id", true, "FIG- 或 TAB- 前缀"], ["artifact_type", "enum", true, "图、图元素、表或单元格"], ["element_id", "string|null", false, "元素 ID"], ["target_location", "string|null", false, "稿件位置"], ["source_id", "source_id", true, "稳定来源 ID"], ["original_location", "string", true, "页码、章节、图或表"], ["transformation", "enum", true, "转换方式"], ["calculation", "string|null", false, "计算过程"], ["copyright_status", "enum", true, "版权状态"], ["permission_reference", "string|null", false, "许可记录"], ["verification_level", "enum", true, "V0-V5"], ["human_status", "enum", true, "人工状态"], ["notes", "string|null", false, "补充说明"]],
        validations: { artifact_type: ["FIGURE", "FIGURE_ELEMENT", "TABLE", "TABLE_CELL"], transformation: ["DIRECT_REUSE", "REDRAWN", "ADAPTED", "DIGITIZED", "CALCULATED", "SYNTHESIZED"], copyright_status: ["UNASSESSED", "ORIGINAL", "LICENSED", "PERMISSION_REQUIRED", "PERMISSION_OBTAINED", "FAIR_USE_ASSESSED", "NOT_REUSABLE"], verification_level: VERIFY, human_status: HUMAN }
      }
    ]
  },
  {
    file: "literature_map.xlsx",
    sheets: [
      {
        name: "Nodes",
        fields: [["source_id", "source_id", true, "稳定来源 ID"], ["title", "string|null", true, "题名"], ["year", "integer|null", true, "年份"], ["journal", "string|null", true, "期刊"], ["document_type", "string|null", true, "文献类型"], ["materials", "array<string>", true, "分号分隔"], ["substrates", "array<string>", true, "分号分隔"], ["coatings", "array<string>", true, "分号分隔"], ["deposition_routes", "array<string>", true, "分号分隔"], ["interface_strategies", "array<string>", true, "分号分隔"], ["optical_properties", "array<string>", true, "分号分隔"], ["mechanical_properties", "array<string>", true, "分号分隔"], ["environmental_properties", "array<string>", true, "分号分隔"], ["manufacturing_properties", "array<string>", true, "分号分隔"], ["characterization_methods", "array<string>", true, "分号分隔"], ["evidence_types", "array<string>", true, "分号分隔"], ["verification_level", "enum", true, "V0-V5"], ["themes", "array<string>", true, "分号分隔"], ["research_stage", "string|null", false, "研究阶段"], ["intended_uses", "array<enum>", true, "CORE/SUPPORTING/BACKGROUND/METHOD/CONFLICT"], ["evidence_strength", "enum", true, "证据强度"]],
        validations: { verification_level: VERIFY, evidence_strength: STRENGTH },
        wholeNumbers: { year: [1600, 2200] }
      },
      {
        name: "Edges",
        fields: [["edge_id", "id", true, "EDGE- 前缀稳定 ID"], ["from_source_id", "source_id", true, "起点 Source_ID"], ["to_source_id", "source_id", true, "终点 Source_ID"], ["relation", "enum", true, "学术关系"], ["basis", "string", true, "关系依据，禁止仅凭标题相似"], ["original_locations", "array<string>", true, "原文位置，分号分隔"], ["verification_level", "enum", true, "V0-V5"], ["human_status", "enum", true, "人工状态"]],
        validations: { relation: ["SUPPORTS", "CONTRADICTS", "EXTENDS", "USES_METHOD_FROM", "SHARES_MATERIAL_SYSTEM", "SHARES_DEPOSITION_ROUTE", "REPORTS_COMPARABLE_METRIC", "STRUCTURAL_REFERENCE", "BACKGROUND_ONLY"], verification_level: VERIFY, human_status: ["UNREVIEWED", "REVIEW_REQUIRED", "ACCEPTED", "REJECTED"] }
      },
      {
        name: "Views",
        fields: [["view_type", "enum", true, "必需视图"], ["status", "enum", true, "构建状态"], ["scope", "string|null", false, "视图范围"], ["output_path", "string|null", false, "导出路径"], ["last_updated", "date|null", false, "ISO 日期"], ["notes", "string|null", false, "补充说明"]],
        rows: ["TIME_EVOLUTION", "MATERIAL_PROCESS_STRUCTURE_PERFORMANCE", "THEME_CLUSTER", "METHOD_CHARACTERIZATION_MATRIX", "CONSENSUS_CONTROVERSY", "EVIDENCE_LAYER"].map((view_type) => ({ view_type, status: "NOT_STARTED" })),
        validations: { view_type: ["TIME_EVOLUTION", "MATERIAL_PROCESS_STRUCTURE_PERFORMANCE", "THEME_CLUSTER", "METHOD_CHARACTERIZATION_MATRIX", "CONSENSUS_CONTROVERSY", "EVIDENCE_LAYER"], status: STATUS }
      }
    ]
  }
];

function columnLetter(index) {
  let n = index + 1;
  let out = "";
  while (n > 0) {
    const r = (n - 1) % 26;
    out = String.fromCharCode(65 + r) + out;
    n = Math.floor((n - 1) / 26);
  }
  return out;
}

function rowsToMatrix(fields, rows = []) {
  return rows.map((record) => fields.map(([name]) => Object.hasOwn(record, name) ? record[name] : null));
}

function defaultWidth(name, type) {
  if (name.includes("title") || name.includes("question") || name.includes("basis") || name.includes("reason") || name.includes("notes")) return 30;
  if (type.startsWith("array") || name.includes("conditions") || name.includes("limitations")) return 24;
  if (type.includes("date") || name.includes("status") || name.includes("level")) return 18;
  if (name.includes("id")) return 20;
  return 17;
}

function writeDataSheet(workbook, spec) {
  const sheet = workbook.worksheets.add(spec.name);
  const headers = spec.fields.map(([name]) => name);
  const end = columnLetter(headers.length - 1);
  sheet.getRange(`A1:${end}1`).values = [headers];
  const matrix = rowsToMatrix(spec.fields, spec.rows);
  if (matrix.length) sheet.getRange(`A2:${end}${matrix.length + 1}`).values = matrix;
  const header = sheet.getRange(`A1:${end}1`);
  header.format = { fill: colors.header, font: { bold: true, color: colors.headerText }, wrapText: true, verticalAlignment: "center", horizontalAlignment: "center", borders: { preset: "all", style: "thin", color: colors.border } };
  header.format.rowHeight = 34;
  spec.fields.forEach(([name, type], i) => {
    sheet.getRange(`${columnLetter(i)}:${columnLetter(i)}`).format.columnWidth = defaultWidth(name, type);
  });
  sheet.freezePanes.freezeRows(1);
  for (const [field, values] of Object.entries(spec.validations || {})) {
    const idx = headers.indexOf(field);
    if (idx >= 0) sheet.getRange(`${columnLetter(idx)}2:${columnLetter(idx)}500`).dataValidation = { rule: { type: "list", values } };
  }
  for (const [field, [min, max]] of Object.entries(spec.wholeNumbers || {})) {
    const idx = headers.indexOf(field);
    if (idx >= 0) sheet.dataValidations.add({ range: `${columnLetter(idx)}2:${columnLetter(idx)}500`, rule: { type: "whole", operator: "between", formula1: min, formula2: max } });
  }
  if (matrix.length) {
    const body = sheet.getRange(`A2:${end}${matrix.length + 1}`);
    body.format = { wrapText: true, verticalAlignment: "top", borders: { preset: "all", style: "thin", color: colors.border } };
    body.format.rowHeight = 28;
  }
  return sheet;
}

function writeFieldGuide(workbook, sheetSpecs) {
  const sheet = workbook.worksheets.add("Field Guide");
  const rows = [["sheet", "field", "type", "required", "description", "allowed_values"]];
  for (const spec of sheetSpecs) {
    for (const [field, type, required, description] of spec.fields) {
      rows.push([spec.name, field, type, required ? "YES" : "NO", description, (spec.validations?.[field] || []).join(";")]);
    }
  }
  sheet.getRange(`A1:F${rows.length}`).values = rows;
  sheet.getRange("A1:F1").format = { fill: colors.guideHeader, font: { bold: true, color: colors.headerText }, wrapText: true, horizontalAlignment: "center", borders: { preset: "all", style: "thin", color: colors.border } };
  sheet.getRange(`A2:F${rows.length}`).format = { wrapText: true, verticalAlignment: "top", borders: { preset: "all", style: "thin", color: colors.border } };
  [18, 28, 18, 12, 36, 42].forEach((width, i) => { sheet.getRange(`${columnLetter(i)}:${columnLetter(i)}`).format.columnWidth = width; });
  sheet.freezePanes.freezeRows(1);
  return sheet;
}

function safeName(name) {
  return name.replace(/[^A-Za-z0-9_-]+/g, "_");
}

async function buildWorkbook(spec) {
  const workbook = Workbook.create();
  for (const sheetSpec of spec.sheets) writeDataSheet(workbook, sheetSpec);
  writeFieldGuide(workbook, spec.sheets);

  const workbookQaDir = path.join(qaDir, path.basename(spec.file, ".xlsx"));
  await fs.mkdir(workbookQaDir, { recursive: true });
  const inspections = [];
  for (const sheetSpec of [...spec.sheets, { name: "Field Guide" }]) {
    const inspected = await workbook.inspect({ kind: "table", sheetId: sheetSpec.name, range: "A1:Z20", include: "values,formulas", tableMaxRows: 20, tableMaxCols: 26, maxChars: 6000 });
    inspections.push({ sheet: sheetSpec.name, inspect: inspected.ndjson ?? String(inspected) });
    const preview = await workbook.render({ sheetName: sheetSpec.name, autoCrop: "all", scale: 1, format: "png" });
    await fs.writeFile(path.join(workbookQaDir, `${safeName(sheetSpec.name)}.png`), new Uint8Array(await preview.arrayBuffer()));
  }
  const errors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "formula error scan" });
  await fs.writeFile(path.join(workbookQaDir, "inspection.json"), JSON.stringify({ workbook: spec.file, inspections, formula_errors: errors.ndjson ?? String(errors) }, null, 2), "utf8");
  const outputPath = path.join(outputDir, spec.file);
  const out = await SpreadsheetFile.exportXlsx(workbook);
  await out.save(outputPath);
  const reopened = await SpreadsheetFile.importXlsx(await FileBlob.load(outputPath));
  for (const sheetSpec of spec.sheets) {
    const expected = sheetSpec.fields.map(([name]) => name);
    const end = columnLetter(expected.length - 1);
    const actual = reopened.worksheets.getItem(sheetSpec.name).getRange(`A1:${end}1`).values[0];
    if (JSON.stringify(actual) !== JSON.stringify(expected)) {
      throw new Error(`Exported header mismatch in ${spec.file}/${sheetSpec.name}`);
    }
  }
}

await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(qaDir, { recursive: true });
for (const spec of specs) await buildWorkbook(spec);
console.log(JSON.stringify({ outputDir, qaDir, workbooks: specs.map((s) => s.file) }, null, 2));
