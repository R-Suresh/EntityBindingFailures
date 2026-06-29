# Results

This directory contains scored outputs and summary tables for the final diagnostic evaluation.

## Files

- `final_60_5models.csv`: full scored output for the final run.
- `summaries/summary_by_method.csv`: aggregate metrics by method.
- `summaries/summary_by_model_method.csv`: aggregate metrics by model and method.
- `summaries/summary_by_ambiguity_method.csv`: aggregate metrics by ambiguity condition and method.
- `summaries/summary_by_risk_method.csv`: aggregate metrics by risk level and method.

## Final run counts

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

## Recompute summaries

```bash
python code/aggregate_results.py --input results/final_60_5models.csv --outdir results/summaries
```
