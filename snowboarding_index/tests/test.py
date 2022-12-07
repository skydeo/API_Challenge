import unittest

from snowboarding_index.app import beautify_name, index_to_eng
from snowboarding_index.data_structures.period_data_frame import PeriodDataFrame


class TestBeautifyName(unittest.TestCase):
    def test_name_formatting(self):
        """Test beautify_name()

        Given a correctly formatted dict, the function
        properly formats the resulting string.
        """
        data = {"name": "minneapolis", "state": "mn", "country": "us"}
        result = beautify_name(data)
        self.assertEqual(result, "Minneapolis, MN, US")


class TestIndexToEng(unittest.TestCase):
    def test_valid_index_to_eng(self):
        """Test index_to_eng() with valid input"""
        data = 3
        result = index_to_eng(data)
        self.assertEqual(result, "good")

    def test_invalid_index_to_eng(self):
        """Test index_to_end() with invalid input"""
        data = 8
        result = index_to_eng(data)
        self.assertEqual(result, "Unavailable")


class TestPeriodDataFrame(unittest.TestCase):
    def test_pdf_initialization(self):
        """Test proper initialization of PeriodDataFrame"""
        result = PeriodDataFrame(
            snowIN=1.0, snowRateIN=1.0, tempC=-2, feelslikeC=2, windSpeedMPH=0
        )
        self.assertIsInstance(result, PeriodDataFrame)
        self.assertEqual(result.feelslikeC, 2)

    def test_pdf_methods_perfect_conditions(self):
        """Test methods in the PeriodDataFrame return correct values
        when using ideal conditions."""
        result = PeriodDataFrame(
            snowIN=1.0, snowRateIN=1.0, tempC=-2, feelslikeC=2, windSpeedMPH=0
        )
        self.assertEqual(result.score_tempC(), 1)
        self.assertEqual(result.score_snowIN(), 2)
        self.assertEqual(result.score_feelslikeC(), 0.5)
        self.assertEqual(result.calculate_sbi_score(), 5)

    def test_pdf_methods_real_conditions(self):
        """Test methods in the PeriodDataFrame return correct values
        when using more real-world conditions."""
        result = PeriodDataFrame(
            snowIN=0.3, snowRateIN=0.1, tempC=1, feelslikeC=-4, windSpeedMPH=10
        )
        self.assertAlmostEqual(result.score_snowIN(), 1.5)
        self.assertAlmostEqual(result.score_snowRateIN(), 0.5)
        self.assertEqual(result.score_tempC(), 0)
        self.assertAlmostEqual(result.score_feelslikeC(), 0.25)
        self.assertAlmostEqual(result.score_windSpeedMPH(), 0.5)
        self.assertAlmostEqual(result.calculate_sbi_score(), 2.75)


if __name__ == "__main__":
    unittest.main()
