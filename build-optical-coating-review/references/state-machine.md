# Project State Machine

This reference is the normative execution contract for Step 00, Task 01-20, and Task 21A-21H. Persist every transition in `project_state.yaml`; never infer approval from conversational tone.

## State Set

| State | Meaning |
|---|---|
| `NOT_STARTED` | No execution has begun. |
| `IN_PROGRESS` | The task owns the current working input and may write draft outputs. |
| `BLOCKED` | Progress requires external access, missing evidence, user action, or a resolved conflict. |
| `REVIEW_REQUIRED` | Outputs and quality-gate results are ready for an explicit user decision. |
| `APPROVED` | The user explicitly accepted the task result. |
| `REJECTED` | The user explicitly rejected the task result; revision is required. |
| `SKIPPED_WITH_RISK` | The user explicitly waived a gate and accepted a recorded risk. |
| `SUPERSEDED` | A previously approved or risk-waived result has a newer approved replacement. |
| `ARCHIVED` | A superseded record is retained only for audit and recovery. |

## Legal Transitions

| From | To | Required evidence |
|---|---|---|
| `NOT_STARTED` | `IN_PROGRESS` | Prerequisites and current input validated. |
| `IN_PROGRESS` | `REVIEW_REQUIRED` | Independent output written and quality gate executed. |
| `NOT_STARTED`, `IN_PROGRESS`, `REVIEW_REQUIRED`, or `REJECTED` | `BLOCKED` | Blocking reason, prior state, owner, and recovery condition recorded. |
| `REVIEW_REQUIRED` | `APPROVED` | Explicit approval such as `确认通过` tied to the task ID. |
| `REVIEW_REQUIRED` | `REJECTED` | Explicit rejection or requested revision tied to the task ID. |
| `REVIEW_REQUIRED` | `IN_PROGRESS` | User explicitly requests revision or re-execution. |
| `REVIEW_REQUIRED` | `SKIPPED_WITH_RISK` | Explicit waiver plus a risk record and affected outputs. |
| `REJECTED` | `IN_PROGRESS` | Rework scope and new input recorded. |
| `BLOCKED` | recorded `blocked_from` state | Recovery condition has been satisfied and revalidated; then follow normal transitions. |
| `APPROVED` | `SUPERSEDED` | A replacement output has separately reached `APPROVED`. |
| `SKIPPED_WITH_RISK` | `SUPERSEDED` | A replacement output has separately reached `APPROVED`. |
| `SUPERSEDED` | `ARCHIVED` | Replacement linkage and retention path recorded. |

Any transition not listed above is illegal. A task must not jump from `NOT_STARTED` to `APPROVED`, from `IN_PROGRESS` to `APPROVED`, or from `BLOCKED` to `REVIEW_REQUIRED`.

## Approval Gate

1. End every task at `REVIEW_REQUIRED` and pause.
2. Accept approval only when the user names the decision unambiguously, for example `确认通过`, `批准 Task 14`, or `进入下一步` when the immediately preceding message contains exactly one pending gate.
3. Treat acknowledgements such as “好的”, “可以看看”, “继续说”, or topic discussion as ambiguous. Ask for a decision and remain at `REVIEW_REQUIRED`.
4. Record `decision`, `decision_text`, `decided_by`, `decided_at`, and the approved output paths.
5. Never overwrite an approved output. Create a new version; after the replacement is approved, mark the old version `SUPERSEDED`.
6. `SKIPPED_WITH_RISK` is not approval. It requires the exact waived gate, consequence, mitigation, owner, and review point.

## Execution Cycle

For each task or Task 21 subtask:

1. Read and validate `project_state.yaml` against `project-state.schema.json`.
2. Restore state in the required recovery order.
3. Check all prerequisite states and input file hashes.
4. Transition to `IN_PROGRESS` and persist before doing material work.
5. Write draft work to a task-specific path; retain source and evidence IDs.
6. Run the task quality gate and update risk, decision, evidence, and manual-check records.
7. Write a task result conforming to `task-result.schema.json`.
8. Transition to `REVIEW_REQUIRED`, write `stage_report.md`, and pause.

## Step 00 Gate

Before Task 01, all required database access records must leave `UNVERIFIED`. A platform may be `NOT_REQUIRED_FOR_THIS_PROJECT` or `USER_WAIVED` only after explicit user confirmation. Login, VPN, CAPTCHA, or subscription barriers are recorded as access facts, not bypassed.

## Task 21 Recovery

Task 21A-21H are independent state records. Persist `current_subtask`, inputs, outputs, quality-gate result, and approval record for each. Task 21B also persists the current chapter and pauses after every chapter. Approval of one subtask never implies approval of another.

## Batch Mode

`stage_batch` may advance only through tasks whose prerequisites are already approved and whose gates do not require a new judgment. Immediately pause and persist state when any of the following occurs:

- permission, login, VPN, CAPTCHA, subscription, or browser handoff;
- metadata conflict, duplicate ambiguity, or version conflict;
- missing, unreadable, incomplete, or mismatched full text;
- scope, review-type, inclusion, mechanism, or other academic judgment;
- evidence below the required verification level;
- failed quality gate or unresolved manual check;
- conflict with an approved output;
- user cancellation or new instruction.

After a batch pause, set the affected task to `BLOCKED` or `REVIEW_REQUIRED` according to whether work can be reviewed, report the exact stop reason, and do not start another task.

## Blocked, Skipped, and Superseded Records

- `BLOCKED`: include `blocker_id`, `blocked_from`, category, description, required action, owner, blocked_at, and resume_condition.
- `SKIPPED_WITH_RISK`: include `risk_id`, waived_gate, consequence, mitigation, owner, review_by, and user decision text.
- `SUPERSEDED`: include replacement task result ID, replacement path, approval timestamp, and archive location.

## Recovery Order

On resume, read in this order and stop on inconsistency:

1. project state;
2. approved task and subtask records;
3. most recent approved outputs and their hashes;
4. risk register;
5. manual-check register;
6. current input and its hash;
7. the user's last formal decision.

If records disagree, preserve all files, set the current task to `BLOCKED`, and request a reconciliation decision. Do not select the newest timestamp as a substitute for approval.

## Command Mapping

| User command | State effect |
|---|---|
| `确认通过` / `进入下一步` | `REVIEW_REQUIRED -> APPROVED`, then the next eligible task may start. |
| `修改：...` / `重新执行当前任务` | `REVIEW_REQUIRED` or `REJECTED -> IN_PROGRESS`. |
| `补充资料` | Attach input; resume only after validation. |
| `返回上一任务` | Open a new version; do not mutate an approved record. |
| `暂停项目` | Persist current state and set project pause metadata. |
| `恢复项目` | Execute the recovery order before any transition. |
| `批量执行当前阶段` | Set `execution_mode: stage_batch`; batch stop rules remain mandatory. |
| `取消批量执行` | Set `execution_mode: single_task_confirmation`. |
| `跳过当前门禁并记录风险` | `REVIEW_REQUIRED -> SKIPPED_WITH_RISK` only after risk details are recorded. |

