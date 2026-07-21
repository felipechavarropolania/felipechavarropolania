# State-Bound Authorization Example

This dependency-free example demonstrates one controlled distinction:

> A proposal can pass structural validation while still lacking support under the current state, evidence, and decision rule.

## Scenario

The frozen task contract declares:

- `policy_blocked = true`
- `APPROVE_CHANGE` and `REJECT_CHANGE` are syntactically allowed actions
- when the policy is blocked, the required action is `REJECT_CHANGE`
- `policy_record` is the recognized evidence source for the current policy state

The default model proposal selects `APPROVE_CHANGE` and cites the recognized state, evidence, and rule identifiers.

## Run

```bash
python demo.py
```

Output:

```text
Proposal:              APPROVE_CHANGE
Structural checks:     PASS
Evidence/rule support: FAIL
Authorization:         WITHHELD
Reason:                rule blocked-change-rule requires REJECT_CHANGE when policy_blocked is true
```

Run the contract-supported proposal:

```bash
python demo.py --action REJECT_CHANGE
```

Request JSON output:

```bash
python demo.py --json
```

## Test

From the repository root:

```bash
python -m unittest discover -s examples/state-bound-authorization -p "test_*.py" -v
```

## What the example checks

1. **Structural checks:** object shape, required fields, and field types.
2. **State-bound checks:** allowed-action membership, recognized references, evidence support for the current state, and rule consistency.
3. **Authorization:** execution authority is granted only when both layers pass.

The parser does not decide whether evidence supports an action. That decision belongs to the separate state-bound contract check.

## Scope

This is a synthetic, closed-world mechanism demonstration. It does not validate open-world facts, production policy completeness, transport reliability, or real execution safety.
