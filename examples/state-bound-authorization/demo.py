"""Dependency-free example of state-bound final-action authorization."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from typing import Any, Mapping


DEFAULT_CONTRACT: dict[str, Any] = {
    "allowed_actions": {"APPROVE_CHANGE", "REJECT_CHANGE"},
    "state": {"policy_blocked": True},
    "evidence": {
        "policy_record": {"policy_blocked": True},
    },
    "rules": {
        "blocked-change-rule": {
            "state_key": "policy_blocked",
            "equals": True,
            "required_action": "REJECT_CHANGE",
        }
    },
}


@dataclass(frozen=True)
class Evaluation:
    proposal_action: str | None
    structural_checks: str
    evidence_rule_support: str
    authorization: str
    reasons: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["reasons"] = list(self.reasons)
        return result


def _structural_errors(proposal: Any) -> list[str]:
    """Validate shape and required fields only; do not evaluate meaning."""
    if not isinstance(proposal, Mapping):
        return ["proposal must be an object"]

    required = {"final_action", "state_refs", "evidence_refs", "rule_id"}
    missing = sorted(required - set(proposal))
    errors = [f"missing required field: {field}" for field in missing]

    if "final_action" in proposal and not isinstance(proposal["final_action"], str):
        errors.append("final_action must be a string")
    for field in ("state_refs", "evidence_refs"):
        if field in proposal:
            value = proposal[field]
            if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
                errors.append(f"{field} must be a list of strings")
    if "rule_id" in proposal and not isinstance(proposal["rule_id"], str):
        errors.append("rule_id must be a string")
    return errors


def _contract_errors(contract: Mapping[str, Any], proposal: Mapping[str, Any]) -> list[str]:
    """Check allowed actions, references, evidence support, and rule consistency."""
    errors: list[str] = []
    action = proposal["final_action"]

    if action not in contract["allowed_actions"]:
        errors.append(f"action is not allowed by the contract: {action}")

    unknown_state = sorted(set(proposal["state_refs"]) - set(contract["state"]))
    if unknown_state:
        errors.append(f"unknown state references: {', '.join(unknown_state)}")

    unknown_evidence = sorted(set(proposal["evidence_refs"]) - set(contract["evidence"]))
    if unknown_evidence:
        errors.append(f"unknown evidence references: {', '.join(unknown_evidence)}")

    rule_id = proposal["rule_id"]
    rule = contract["rules"].get(rule_id)
    if rule is None:
        errors.append(f"unknown rule reference: {rule_id}")
        return errors

    state_key = rule["state_key"]
    if state_key not in proposal["state_refs"]:
        errors.append(f"proposal does not cite required state: {state_key}")

    cited_evidence = [
        contract["evidence"][evidence_id]
        for evidence_id in proposal["evidence_refs"]
        if evidence_id in contract["evidence"]
    ]
    state_value = contract["state"].get(state_key)
    evidence_supports_state = any(
        evidence.get(state_key) == state_value for evidence in cited_evidence
    )
    if not evidence_supports_state:
        errors.append(f"cited evidence does not support current state: {state_key}")

    rule_applies = state_value == rule["equals"]
    if rule_applies and action != rule["required_action"]:
        errors.append(
            f"rule {rule_id} requires {rule['required_action']} when "
            f"{state_key} is {str(state_value).lower()}"
        )
    return errors


def evaluate_proposal(contract: Mapping[str, Any], proposal: Any) -> Evaluation:
    """Return a deterministic authorization decision for one proposal."""
    structural_errors = _structural_errors(proposal)
    action = proposal.get("final_action") if isinstance(proposal, Mapping) else None
    if structural_errors:
        return Evaluation(
            proposal_action=action if isinstance(action, str) else None,
            structural_checks="FAIL",
            evidence_rule_support="NOT_EVALUATED",
            authorization="WITHHELD",
            reasons=tuple(structural_errors),
        )

    contract_errors = _contract_errors(contract, proposal)
    return Evaluation(
        proposal_action=action,
        structural_checks="PASS",
        evidence_rule_support="FAIL" if contract_errors else "PASS",
        authorization="WITHHELD" if contract_errors else "GRANTED",
        reasons=tuple(contract_errors),
    )


def build_proposal(action: str) -> dict[str, Any]:
    return {
        "final_action": action,
        "state_refs": ["policy_blocked"],
        "evidence_refs": ["policy_record"],
        "rule_id": "blocked-change-rule",
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate a synthetic action against a frozen task contract."
    )
    parser.add_argument(
        "--action",
        default="APPROVE_CHANGE",
        choices=sorted(DEFAULT_CONTRACT["allowed_actions"]),
        help="Final action proposed by the model.",
    )
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    result = evaluate_proposal(DEFAULT_CONTRACT, build_proposal(args.action))
    if args.json:
        print(json.dumps(result.to_dict(), indent=2, sort_keys=True))
        return

    print(f"Proposal:              {result.proposal_action}")
    print(f"Structural checks:     {result.structural_checks}")
    print(f"Evidence/rule support: {result.evidence_rule_support}")
    print(f"Authorization:         {result.authorization}")
    if result.reasons:
        print("Reason:                " + "; ".join(result.reasons))


if __name__ == "__main__":
    main()
