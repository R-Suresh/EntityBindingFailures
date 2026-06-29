# Code

This directory contains scripts for generating tasks, running the model experiment, and aggregating scored results.

## Files

| File | Purpose |
|---|---|
| `generate_final_60_tasks.py` | Generates the final 60-task diagnostic benchmark as JSONL. |
| `run_entity_binding_experiment.py` | Runs the model-method-task evaluation using AWS Bedrock. |
| `aggregate_results.py` | Aggregates the final scored CSV into summary tables. |

## Typical commands

Generate tasks:

```bash
python code/generate_final_60_tasks.py
```

Aggregate saved results:

```bash
python code/aggregate_results.py \
  --input results/final_60_5models.csv \
  --outdir results/summaries
```

Run the experiment with AWS Bedrock access:

```bash
python code/run_entity_binding_experiment.py \
  --tasks data/tasks_entity_binding_final_60.jsonl \
  --out results/final_60_5models.csv \
  --region us-east-1 \
  --models <MODEL_ID_1> <MODEL_ID_2> \
  --methods direct semantic_filter cmtf_only entity_retrieval confidence_gate entity_cmtf_provenance
```
