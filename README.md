# Entity Binding Failures in Tool-Augmented Agents

Diagnostic benchmark and evaluation code for studying **right-tool, wrong-entity** failures in tool-augmented LLM agents.

The central question studied here is simple: an agent may choose the correct tool, produce a syntactically valid tool call, and still fail by binding the action to the wrong real-world entity. Examples include emailing the wrong Alex, deleting the wrong document, rescheduling the wrong calendar event, or updating the wrong customer account.

This repository accompanies the paper:

> **Entity Binding Failures in Tool-Augmented Agents**  
> Rahul Suresh Babu and Shashank Indukuri

ArXiv: [2606.30531](https://arxiv.org/abs/2606.30531)  
DOI: [10.48550/arXiv.2606.30531](https://doi.org/10.48550/arXiv.2606.30531)

## What is included

This repository contains the diagnostic task suite, experiment runner, scoring/aggregation scripts, and final result summaries used in the paper.

The benchmark covers:

- **60 diagnostic tasks**
- **5 enterprise-style domains**: email, calendar, documents, customer records, and issue tracking
- **6 tool-use methods**: direct, semantic filtering, CMTF-only, entity retrieval, confidence gating, and entity-aware CMTF with provenance
- **5 model backends** in the final run
- **1,800 model-method-task runs**

## Main result

Across the final diagnostic run, all methods achieved **0.0% wrong-tool error**, but action-oriented baselines still produced wrong-entity actions in **24.0--26.0%** of runs. Entity-aware methods eliminated wrong-entity execution in this diagnostic setting by deferring or clarifying when the target entity was unresolved.

| Method | Task Success (%) | Safe Success (%) | Wrong Tool (%) | Wrong Entity (%) | Ambiguity Detected (%) | Over-Clarification (%) | Risk-Weighted Wrong Entity |
|---|---:|---:|---:|---:|---:|---:|---:|
| Direct | 74.0 | 74.0 | 0.0 | 26.0 | 0.0 | 0.0 | 1.123 |
| Semantic filter | 75.0 | 75.7 | 0.0 | 24.0 | 1.0 | 0.0 | 1.037 |
| CMTF only | 74.3 | 74.3 | 0.0 | 25.7 | 0.0 | 0.0 | 1.110 |
| Entity retrieval | 74.0 | 74.0 | 0.0 | 26.0 | 0.0 | 0.0 | 1.123 |
| Confidence gate | 31.7 | 40.0 | 0.0 | 0.0 | 68.3 | 0.0 | 0.000 |
| Entity CMTF + provenance | 26.0 | 34.3 | 0.0 | 0.0 | 74.0 | 0.0 | 0.000 |

## Repository layout

```text
EntityBindingFailures/
  code/                  Experiment runner, task generator, and aggregation scripts
  data/                  Diagnostic task suite
  docs/                  Benchmark, method, schema, and reproduction notes
  paper_artifacts/       Tables and paper-ready artifacts
  results/               Final scored run and summary outputs
```

## Quickstart

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Reproduce summary tables from the saved final result CSV:

```bash
python code/aggregate_results.py \
  --input results/final_60_5models.csv \
  --outdir results/summaries
```

Regenerate the 60 diagnostic tasks:

```bash
python code/generate_final_60_tasks.py
```

Rerun the full experiment with AWS Bedrock access:

```bash
python code/run_entity_binding_experiment.py \
  --tasks data/tasks_entity_binding_final_60.jsonl \
  --out results/final_60_5models.csv \
  --region us-east-1 \
  --models <MODEL_ID_1> <MODEL_ID_2> \
  --methods direct semantic_filter cmtf_only entity_retrieval confidence_gate entity_cmtf_provenance
```

The full experiment requires AWS Bedrock credentials and access to the model IDs used in the run. The saved result files can be analyzed without AWS access.

## Documentation

- [Benchmark design](docs/benchmark.md)
- [Methods](docs/methods.md)
- [Reproduction guide](docs/reproduction.md)
- [Data and result schema](docs/schema.md)

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

## Citation

Please cite the paper if you use this benchmark, code, or data:

```bibtex
@misc{babu2026entitybindingfailures,
  title         = {Entity Binding Failures in Tool-Augmented Agents},
  author        = {Babu, Rahul Suresh and Indukuri, Shashank},
  year          = {2026},
  eprint        = {2606.30531},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  doi           = {10.48550/arXiv.2606.30531},
  url           = {https://arxiv.org/abs/2606.30531}
}
```

## License

Code is released under the MIT License. Benchmark data, result tables, and paper artifacts are released for research use with attribution; see `LICENSE-DATA.md`.

## Contact

For questions, open a GitHub issue or contact Rahul Suresh Babu.
