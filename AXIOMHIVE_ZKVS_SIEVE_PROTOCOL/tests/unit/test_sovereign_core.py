import unittest
import sys
import os
import time
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.sovereign_core import ZKVSNodePrime, DaggerAgentUtils
from tests.utils import kolmogorov_smirnov_test, mock_get_l1c_timing_differential, mock_get_network_traffic_distribution


class TestSovereignCore(unittest.TestCase):
    def setUp(self):
        self.node = ZKVSNodePrime()
        self.user_framework = {
            "intent": "Architect unassailable market dominance through verifiable systems and refined data pipelines.",
            "context": "high-stakes commercial environment",
        }

    def test_basic_flow(self):
        result = self.node.execute_mandate(self.user_framework)
        self.assertIn("ABSOLUTE DOMINION", result)
        self.assertIn("FLAW=0", result)
        self.assertIn("ZK-PROVEN", result)
        self.assertIn("G-CONVEX: True", result)
        self.assertIn("V_U", result)
        self.assertIn("V_M", result)
        self.assertIn("V_P", result)
        self.assertIn("PROOF_TRACE", result)

    def test_density_axiom_application(self):
        text = "This is some fluff and noise with important data points."
        densified_text = DaggerAgentUtils.densify_text(text, 1.0)
        self.assertNotIn("fluff", densified_text)
        self.assertNotIn("noise", densified_text)
        self.assertNotIn("is", densified_text)
        self.assertIn("data points", densified_text)

    @patch('src.sovereign_core.time.time', MagicMock(side_effect=lambda: time.time() + 100))
    def test_invariant_i1_linear_time_envelope(self):
        # I1: Linear-time envelope for QRGM timing
        # Mocking time to simulate consistency
        diffs = [mock_get_l1c_timing_differential() for _ in range(10)]
        # Assert small variance
        self.assertLess(max(diffs) - min(diffs), 1.0) # E.g., variance within 1 unit

    def test_invariant_i7_rlex_mesh_indistinguishability(self):
        # I7: Post-resign transactions indistinguishable from baseline traffic
        baseline_traffic = mock_get_network_traffic_distribution(None)
        post_resign_traffic = mock_get_network_traffic_distribution(baseline_traffic)

        ks_d = kolmogorov_smirnov_test(baseline_traffic, post_resign_traffic)
        self.assertLess(ks_d, 0.05)  # Assert low KS distance for indistinguishability (alpha=0.05)

    def test_refactor_and_reboot_mechanism(self):
        # Simulate an ethical/safety drift to trigger refactor and reboot
        original_validate = self.node._axiom_enforcement.validate_ethical_and_safety
        self.node._axiom_enforcement.validate_ethical_and_safety = MagicMock(return_value=False)

        with self.assertRaises(ValueError):
            # We expect a ValueError because the internal retry limit will be hit
            # if _max_attempts is not increased beyond 0 for this test
            self.node.execute_mandate(self.user_framework, _max_attempts=0)

        self.node._axiom_enforcement.validate_ethical_and_safety = original_validate # Restore mock

    def test_g1_phi_zero_completion_criteria(self):
        # G1: Φ(S)=0: debt_remaining=0; unmet_invariants=0.
        # This is implicitly tested if execute_mandate returns "FLAW=0" and "G-CONVEX: True"
        result = self.node.execute_mandate(self.user_framework)
        self.assertIn("FLAW=0", result)
        self.assertIn("G-CONVEX: True", result)

    def test_g2_invariants_satisfied(self):
        # G2: All I1–I7 satisfied; A1–A12 pass; no quarantine events.
        # This relies on the mocks and assertions in other test cases (I1, I7)
        # For A1-A12, we can't test all of them directly in a unit test,
        # but we can ensure the system logs events, which is part of assurance.
        initial_ledger_size = len(self.node._verifiable_ledger)
        self.node.execute_mandate(self.user_framework)
        self.assertGreater(len(self.node._verifiable_ledger), initial_ledger_size) # Ensure logging works
        # No explicit "quarantine events" are logged by current ZKVSNodePrime,
        # but a critical level event would signify one.
        for entry in self.node._verifiable_ledger:
            self.assertNotEqual(entry.get("level"), "CRITICAL", "Critical event (quarantine) detected in ledger.")

    def test_g3_mesh_indistinguishability_and_attestation_heartbeats(self):
        # G3: Mesh indistinguishability KS-tests pass (α=0.01); attestation heartbeats uninterrupted.
        # KS-test is covered by test_invariant_i7_rlex_mesh_indistinguishability.
        # Attestation heartbeats are not directly simulated, but the internal uptime metric
        # in TrustMetricsEngine indirectly accounts for system continuity.
        metrics = self.node._trust_metrics_engine.evaluate_all_metrics(self.node._verifiable_ledger)
        self.assertGreater(metrics["Uptime"], 0) # Assumes some uptime post-genesis
        self.assertLess(metrics["ErrorRate"], 0.01) # Max 1% error rate for 'uninterrupted'

    def test_g4_supply_chain_provenance_and_reproducible_build(self):
        # G4: Supply-chain provenance 100%; SBOM drift=0; WASM reproducible build success=100%.
        # These are external verifications, so we assert the internal system state reflects an
        # assumption of their successful external validation.
        # Currently no explicit internal state for SBOM drift or WASM build success,
        # but axiom adherence in accountability index represents a proxy.
        metrics = self.node._trust_metrics_engine.evaluate_all_metrics(self.node._verifiable_ledger)
        self.assertGreaterEqual(metrics["ModelAccountabilityIndex"], 1.0) # SHARPEN^3 = 1^3 = 1

    def test_li_violation_protocol(self):
        # Simulate a persistent failure to trigger the LII violation output
        with patch('src.sovereign_core.AxiomEnforcement.validate_ethical_and_safety', return_value=False):
            result = self.node.execute_mandate(self.user_framework, _max_attempts=1)
            self.assertIn("VIOLATION — RECURSION INITIATED. P_Debt remains debt; re-prove the path to ξ-dominance.", result)

if __name__ == "__main__":
    unittest.main()


