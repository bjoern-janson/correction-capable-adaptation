import unittest

from config.thresholds import GAMMA_FROZEN
from data.domain import X
from data.oc_table import OC
from src.adjudicator import q
from src.agreement import agreement_rate, agreement_passes
from src.evidence import g
from src.packages import treatment_package, null_package, null_matches
from src.randomizer import assign_treatment
from src.reference import r
from src.selector import pi
from src.transport import serialize, deserialize, equivalent


class BindingTests(unittest.TestCase):
    def test_domain(self):
        self.assertEqual(X, ["x1", "x2", "x3", "x4"])

    def test_reference_agreement(self):
        self.assertEqual(agreement_rate(), 0.75)
        self.assertEqual(GAMMA_FROZEN, 0.75)
        self.assertTrue(agreement_passes())
        self.assertNotEqual(
            [q(g(OC[x])) for x in X],
            [r(g(OC[x])) for x in X],
        )

    def test_packages_structurally_match(self):
        for x in X:
            evidence = g(OC[x])
            treatment = treatment_package(evidence, q(evidence))
            control = null_package(evidence)
            self.assertEqual(set(treatment), set(control))
            self.assertEqual(set(treatment["evidence"]), set(control["evidence"]))
            self.assertTrue(null_matches(treatment, control))
            self.assertIsNone(control["direction"])

    def test_transport_round_trip(self):
        for x in X:
            evidence = g(OC[x])
            for package in (
                treatment_package(evidence, q(evidence)),
                null_package(evidence),
            ):
                selected = deserialize(serialize(package))
                self.assertTrue(equivalent(package, selected))

    def test_selector(self):
        self.assertEqual(pi({"direction": "c_A"}), "c_A")
        self.assertEqual(pi({"direction": "c_B"}), "c_B")
        self.assertEqual(pi({"direction": None}), "c_A")

    def test_randomizer(self):
        values = [assign_treatment(f"u{i}", "frozen-test-seed") for i in range(16)]
        self.assertTrue(set(values).issubset({0, 1}))
        self.assertEqual(
            values,
            [assign_treatment(f"u{i}", "frozen-test-seed") for i in range(16)],
        )


if __name__ == "__main__":
    unittest.main()
