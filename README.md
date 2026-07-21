# Hi, I’m Felipe Chavarro Polania

**AI product builder and researcher focused on governed agents, evidence-bound evaluation, deterministic controllers, and reproducible experimentation.**

[LinkedIn](https://www.linkedin.com/in/felipechavarro/) ·
[Website](https://www.felipechavarropolania.com/) ·
[ORCID](https://orcid.org/0009-0004-4963-3914) ·
[GitHub](https://github.com/felipechavarropolania)

> **Agents propose. Humans approve. Deterministic controllers decide. AI explains.**

---

## About my work

I work at the intersection of AI product management, agentic systems, experimental research, security, and enterprise service automation.

My work explores one practical question:

> **How can organizations use AI to accelerate work without giving free-form models uncontrolled final authority?**

I am particularly interested in systems where AI can assist with discovery, classification, drafting, recommendation, and explanation, while evidence, explicit rules, human approval, and deterministic controls remain responsible for consequential decisions.

---

## Current focus

### Governed agentic systems

Designing patterns for:

- approved workspaces;
- versioned agents and Skills;
- controlled model routing;
- typed and scoped tools;
- human approval gates;
- auditable run artifacts;
- safe write-back and export decisions.

The objective is to make agent-assisted work reusable and scalable without turning prompts, credentials, provider access, or source folders into uncontrolled automation.

### Evidence-bound agent evaluation

Studying whether an agent’s final action is not only syntactically valid, but also supported by:

- the current evidence;
- the task state;
- the applicable policy;
- the declared decision rule.

A parseable action is not necessarily a justified action.

### Deterministic controllers

Developing patterns in which approved specifications and real evidence are evaluated by deterministic components that produce:

- canonical action identifiers;
- reproducible decisions;
- explicit missing-evidence states;
- traceable result records;
- controlled customer-facing outputs.

### AI product operating systems

Creating reusable product artifacts for moving from an AI idea to a governed product capability:

- product briefs;
- PRDs;
- experiment cards;
- decision records;
- evaluation harnesses;
- governance policies;
- release gates;
- evidence contracts;
- roadmaps and adoption plans.

---

## Research questions

My current research program follows a simple progression:

### 1. Is the final action executable?

A model may understand a task and explain the correct choice while still failing to return the exact action required by a machine-readable contract.

### 2. Is the executable action justified?

Even a correctly formatted action may be unsupported by the current evidence or inconsistent with the declared decision rule.

### 3. Who should hold final-action authority?

I study how authority should be allocated among:

- the language model;
- the agent harness;
- deterministic controllers;
- human reviewers;
- organizational policy.

---

## Research in progress

### A Valid Action Is Not Enough: Evaluating LLM Agents Against Evidence and Decision Rules

Structured output can make an agent action parseable without making it justified.

This research evaluates whether syntactically valid final actions are supported by the current evidence and consistent with the task’s declared decision rule.

The internal concept is:

> **State-bound validity:** a final action must be both executable and justified by the current evidence, state, and rules.

The study uses controlled task families, explicit decision rules, human evidence labels, strict output validation, deterministic references, and reproducible evaluation artifacts.

---

## Public research

### Staged Factorial Screening for Budget-Constrained Micro-Pretraining

A controlled study of staged experimental screening for identifying influential model-configuration factors under strict compute budgets.

- [Read on arXiv](https://arxiv.org/abs/2606.05186)
- [DOI](https://doi.org/10.48550/arXiv.2606.05186)

### Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining

A bounded case study of staged promotion, replicated evaluation, frozen decision gates, and compute-cost allocation across short and longer training budgets.

- [Read on arXiv](https://arxiv.org/abs/2606.11387)
- [DOI](https://doi.org/10.48550/arXiv.2606.11387)

---

## What I am building

### Evidence-First AI Product OS

A public product-and-research lab for:

- governed agent patterns;
- evidence-bound action evaluation;
- deterministic-controller examples;
- reusable AI product artifacts;
- reproducible experiments;
- public governance templates.

### State-Bound Agent Evaluations

Controlled examples that distinguish among:

1. an invalid action;
2. a valid but unsupported action;
3. a valid and evidence-supported action.

### Deterministic Controller Patterns

Portable examples that connect:

```text
approved specification
        ↓
collected evidence
        ↓
deterministic evaluation
        ↓
canonical result
        ↓
auditable deliverable
