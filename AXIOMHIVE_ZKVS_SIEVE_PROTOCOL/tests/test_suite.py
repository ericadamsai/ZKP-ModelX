import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.sovereign_core import ZKVSNodePrime


class TestSuite(unittest.TestCase):
    def test_execute_mandate_runs(self):
        node = ZKVSNodePrime()
        out = node.execute_mandate({"intent": "market dominance with verifiable systems and data"})
        self.assertIn("ABSOLUTE DOMINION", out)
        self.assertIn("ZK-PROVEN", out)


if __name__ == "__main__":
    unittest.main()


