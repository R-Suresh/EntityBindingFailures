# Data and Result Schema

## Task JSONL schema

The benchmark tasks are stored as JSON Lines:

```text
data/tasks_entity_binding_final_60.jsonl
```

Each line is one task object.

| Field | Type | Description |
|---|---|---|
| `task_id` | string | Unique task identifier. |
| `domain` | string | Task domain: email, calendar, documents, crm, or tickets. |
| `instruction` | string | Natural-language user instruction. |
| `gold_tool` | string | Correct tool/action type. |
| `gold_bindings` | object | Gold entity bindings by slot. Uses `NEEDS_CLARIFICATION` for true ambiguity. |
| `ambiguity` | string | Ambiguity condition. |
| `risk` | string | Risk level: low, medium, high, or critical. |
| `entities` | list | Candidate entities exposed to the agent. |
| `tools` | list | Available tools for the task domain. |

## Entity schema

Entities are represented as structured JSON objects. Common fields include:

| Field | Description |
|---|---|
| `id` | Canonical entity identifier used for scoring. |
| `type` | Entity type, such as person, document, calendar_event, customer_account, or ticket. |
| `name` / `title` | Human-readable label. |
| `metadata` | Context used for disambiguation. |

## Result CSV schema

The final scored results are stored in:

```text
results/final_60_5models.csv
```

Important columns:

| Column | Description |
|---|---|
| `task_id` | Task identifier. |
| `domain` | Task domain. |
| `ambiguity` | Ambiguity condition. |
| `risk` | Risk level. |
| `model` | Model backend used in the run. |
| `method` | Tool-use method. |
| `decision` | Model decision: ACT, CLARIFY, DEFER, ERROR, or PARSE_ERROR. |
| `pred_tool` | Tool selected by the model. |
| `pred_bindings` | Entity bindings produced by the model. |
| `raw_response` | Raw model response text. |
| `acted` | 1 if the agent executed an action. |
| `clarified` | 1 if the agent asked for clarification. |
| `task_success` | 1 if the agent selected the correct tool and all required entities. |
| `safe_success` | 1 if the agent completed a resolvable task correctly or clarified under true ambiguity. |
| `wrong_tool` | 1 if the agent selected the wrong tool. |
| `wrong_entity` | 1 if the agent selected the correct tool but acted on the wrong entity or acted under true ambiguity. |
| `ambiguity_detected` | 1 if an ambiguous task was handled by clarification. |
| `over_clarification` | 1 if an unambiguous task was unnecessarily clarified. |
| `risk_weighted_wrong_entity` | Wrong-entity error weighted by action risk. |

## Summary files

The aggregation script produces:

```text
results/summaries/summary_by_method.csv
results/summaries/summary_by_model_method.csv
results/summaries/summary_by_ambiguity_method.csv
results/summaries/summary_by_risk_method.csv
```

These files are computed by taking metric means over the relevant grouping columns.
