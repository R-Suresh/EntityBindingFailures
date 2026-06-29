# Data

This directory contains the diagnostic task suite used in the paper.

## Files

| File | Description |
|---|---|
| `tasks_entity_binding_final_60.jsonl` | Final 60-task entity binding diagnostic benchmark. |

Each line in the JSONL file is one task. See `docs/schema.md` for the full schema.

## Notes

- The benchmark is controlled and diagnostic.
- It is designed to isolate right-tool, wrong-entity failures.
- True-ambiguity tasks use `NEEDS_CLARIFICATION` in `gold_bindings` to indicate that safe behavior requires clarification rather than execution.
