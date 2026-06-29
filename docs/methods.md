# Methods

The benchmark compares six tool-use methods. The comparison is best interpreted as a **safety--completion tradeoff** between action-first methods and entity-aware methods.

## Method list

| Method | Type | Description |
|---|---|---|
| `direct` | Action-oriented baseline | Receives the instruction, tools, and entity candidates, then directly chooses a concrete tool call and entity binding. |
| `semantic_filter` | Action-oriented baseline | Filters tools by semantic relevance before direct execution. |
| `cmtf_only` | Action-oriented baseline | Exposes the causally relevant tool frontier but does not explicitly gate entity bindings. |
| `entity_retrieval` | Action-oriented baseline | Provides retrieved candidate entities to the agent, which must choose one and act. |
| `confidence_gate` | Entity-aware method | Acts only when the target entity is clearly resolved; otherwise clarifies. |
| `entity_cmtf_provenance` | Entity-aware method | Combines entity-aware tool filtering with provenance evidence and clarification under ambiguity. |

## Action-oriented baselines

The following methods are evaluated under a direct-execution policy:

- `direct`
- `semantic_filter`
- `cmtf_only`
- `entity_retrieval`

These methods must choose a concrete action. They expose wrong-entity risk when an agent is configured to act rather than clarify.

## Entity-aware methods

The following methods may clarify or defer when the binding is unresolved:

- `confidence_gate`
- `entity_cmtf_provenance`

These methods are designed to block execution when the intended entity cannot be safely determined.

## Key distinction

Tool filtering and entity binding solve different problems.

- Tool filtering asks: **Which action type should be visible or selected?**
- Entity binding asks: **Which real-world entity should that action operate on?**

A minimal tool menu does not guarantee safety if the remaining tool is applied to the wrong entity.

## Implementation notes

The diagnostic implementation uses structured prompts and candidate comparisons rather than a separately calibrated uncertainty model. The confidence-gated methods should therefore be interpreted as diagnostic execution policies, not production-calibrated uncertainty estimators.
