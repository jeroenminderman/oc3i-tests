import unittest
from pathlib import Path

import pandas as pd

from src.oc3i_tests import summarise_output

CURRENT_DIR = Path(__file__).resolve().parent


class TestSummariseOutput(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        test_file = (
            CURRENT_DIR.parent / "data/tests_data/test_summarise_output.csv"
        )
        cls.test_data = pd.read_csv(test_file, dtype=str).fillna("")

    def test_full_data(self):
        result = summarise_output(
            self.test_data,
            given_code="input",
            prediction1="pred1",
            prediction2="pred2",
            prediction3="pred3"
        )
        self.assertEqual(result["total_cases"], 10)
        self.assertEqual(result["match1"], 4)
        self.assertEqual(result["match123"], 7)

    def test_type_a(self):
        result = summarise_output(
            self.test_data,
            given_code="input",
            prediction1="pred1",
            prediction2="pred2",
            prediction3="pred3",
            filter_col="type",
            filter_value="A"
        )
        self.assertEqual(result["total_cases"], 5)
        self.assertEqual(result["match1"], 2)
        self.assertEqual(result["match123"], 4)

    def test_type_b(self):
        result = summarise_output(
            self.test_data,
            given_code="input",
            prediction1="pred1",
            prediction2="pred2",
            prediction3="pred3",
            filter_col="type",
            filter_value="B"
        )
        self.assertEqual(result["total_cases"], 5)
        self.assertEqual(result["match1"], 2)
        self.assertEqual(result["match123"], 3)
