# Research Program

This page records the public research sequence and keeps publication status separate from work in progress.

![Research roadmap](../docs/research-roadmap.svg)

## Program thesis

AI systems should be evaluated and operated as governed systems, not only as models.

The research sequence examines four different control problems:

1. **Experimental screening:** identify influential factors without spending the largest budget on every candidate.
2. **Compute promotion:** use explicit gates to decide which experiments receive longer continuations.
3. **Final-action binding:** measure whether a model returns the exact executable action required by a harness.
4. **State-bound authorization:** distinguish a parseable proposal from one supported by current evidence and rules.

## Publication and manuscript record

### Paper 05 - Published

**Staged Factorial Screening for Budget-Constrained Micro-Pretraining**

- [arXiv:2606.05186](https://arxiv.org/abs/2606.05186)
- [DOI: 10.48550/arXiv.2606.05186](https://doi.org/10.48550/arXiv.2606.05186)
- Primary subject: Machine Learning (`cs.LG`)
- Public record: 613 experiments across designed screens, follow-ups, baselines, and bounded continuations

**Bounded contribution:** short designed screens can identify high-penalty directions and support local refinement under constrained compute.

**Not claimed:** hardware-invariant rankings, globally optimal recipes, or superiority to general hyperparameter-optimization methods.

### Paper 06 - Published

**Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining**

- [arXiv:2606.11387](https://arxiv.org/abs/2606.11387)
- [DOI: 10.48550/arXiv.2606.11387](https://doi.org/10.48550/arXiv.2606.11387)
- Primary subject: Computation and Language (`cs.CL`)
- Public record: frozen promotion rules across 2-minute, 5-minute, 10-minute, 60-minute, and 12-hour stages

**Bounded contribution:** staged promotion can make compute-allocation decisions explicit and auditable even when early rankings are unstable.

**Not claimed:** that skipped candidates could never overtake promoted candidates, or that the protocol outperforms adaptive optimization.

### Paper 07 - Submission manuscript

**Format-Bound Harnesses Repair Final-Action Failures in Controlled LLM Agent Evaluation**

**Research question:** can a model understand the decision but fail at the final binding between its reasoning and the action identifier consumed by a system?

**Bounded contribution:** evaluates strict executable-action validity separately from regret, reasoning quality, transport reliability, and deterministic controller performance in controlled expected-utility tasks.

A public arXiv link will replace this status when an identifier is available.

### Paper 08 - Research in progress

**A Valid Action Is Not Enough: Evaluating LLM Agents Against Evidence and Decision Rules**

**Research question:** when an action is syntactically executable, is it actually supported by the current state, cited evidence, and declared decision rule?

**Concept under study:** state-bound validity.

**Bounded contribution under study:** closed-world classification and deterministic enforcement relative to frozen task contracts.

**Not claimed:** open-world factual verification, complete production policy coverage, or independent proof of real-world safety.

## Public implementation

The [`state-bound-authorization`](../examples/state-bound-authorization/README.md) example demonstrates the Paper 08 mechanism with a synthetic contract:

```text
model proposal -> structural checks -> state/evidence/rule checks -> authorization
```

The separation matters because schema-valid output can still conflict with current policy state.

## Future questions

- Can automated judge panels be calibrated, replayed, and audited without treating model consensus as ground truth?
- How should evidence freshness and provenance be represented in an authorization contract?
- Which decisions require deterministic authority, human approval, or both?
- How should a governed runtime report abstention, missing evidence, and policy conflict?

Future questions are research directions, not completed papers or validated claims.
