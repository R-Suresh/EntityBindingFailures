# Reproduction Guide

This guide describes two reproduction modes.

## Mode A: reproduce tables from saved results

This mode does not require AWS access. It regenerates summary CSVs from the saved final run.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python code/aggregate_results.py \
  --input results/final_60_5models.csv \
  --outdir results/summaries
```

Expected output files:

```text
results/summaries/summary_by_method.csv
results/summaries/summary_by_model_method.csv
results/summaries/summary_by_ambiguity_method.csv
results/summaries/summary_by_risk_method.csv
```

The final run should match:

```text
Rows: 1800
Models: 5
Methods: 6
Tasks: 60
Error rows: 0
Wrong entity rows: 305
Wrong tool rows: 0
Over-clarification rows: 0
```

## Mode B: regenerate the task suite

```bash
python code/generate_final_60_tasks.py
```

This writes:

```text
data/tasks_entity_binding_final_60.jsonl
```

## Mode C: rerun the full model experiment

This mode requires AWS Bedrock credentials and access to the target model IDs.

```bash
python code/run_entity_binding_experiment.py \
  --tasks data/tasks_entity_binding_final_60.jsonl \
  --out results/final_60_5models.csv \
  --region us-east-1 \
  --models <MODEL_ID_1> <MODEL_ID_2> \
  --methods direct semantic_filter cmtf_only entity_retrieval confidence_gate entity_cmtf_provenance
```

The full run evaluates every combination of task, model, and method. For the final paper run, this produced 60 tasks x 5 models x 6 methods = 1,800 rows.

## Notes

- Model outputs may vary across model versions, provider updates, decoding behavior, and runtime configuration.
- The saved result files should be used to reproduce the paper tables exactly.
- The full experiment requires cloud model access and may incur provider costs.
