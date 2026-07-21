import copy
import unittest

from demo import DEFAULT_CONTRACT, build_proposal, evaluate_proposal


class StateBoundAuthorizationTests(unittest.TestCase):
    def test_parseable_but_rule_conflicting_action_is_withheld(self):
        result = evaluate_proposal(DEFAULT_CONTRACT, build_proposal("APPROVE_CHANGE"))

        self.assertEqual(result.structural_checks, "PASS")
        self.assertEqual(result.evidence_rule_support, "FAIL")
        self.assertEqual(result.authorization, "WITHHELD")
        self.assertIn("requires REJECT_CHANGE", result.reasons[0])

    def test_contract_supported_action_is_granted(self):
        result = evaluate_proposal(DEFAULT_CONTRACT, build_proposal("REJECT_CHANGE"))

        self.assertEqual(result.structural_checks, "PASS")
        self.assertEqual(result.evidence_rule_support, "PASS")
        self.assertEqual(result.authorization, "GRANTED")
        self.assertEqual(result.reasons, ())

    def test_missing_required_field_fails_structure(self):
        proposal = build_proposal("REJECT_CHANGE")
        del proposal["rule_id"]

        result = evaluate_proposal(DEFAULT_CONTRACT, proposal)

        self.assertEqual(result.structural_checks, "FAIL")
        self.assertEqual(result.evidence_rule_support, "NOT_EVALUATED")
        self.assertEqual(result.authorization, "WITHHELD")

    def test_unknown_evidence_reference_is_withheld(self):
        proposal = build_proposal("REJECT_CHANGE")
        proposal["evidence_refs"] = ["unknown_record"]

        result = evaluate_proposal(DEFAULT_CONTRACT, proposal)

        self.assertEqual(result.structural_checks, "PASS")
        self.assertEqual(result.evidence_rule_support, "FAIL")
        self.assertEqual(result.authorization, "WITHHELD")
        self.assertTrue(any("unknown evidence" in reason for reason in result.reasons))

    def test_evidence_must_match_current_state(self):
        contract = copy.deepcopy(DEFAULT_CONTRACT)
        contract["evidence"]["policy_record"]["policy_blocked"] = False

        result = evaluate_proposal(contract, build_proposal("REJECT_CHANGE"))

        self.assertEqual(result.evidence_rule_support, "FAIL")
        self.assertEqual(result.authorization, "WITHHELD")
        self.assertTrue(any("does not support" in reason for reason in result.reasons))


if __name__ == "__main__":
    unittest.main()
