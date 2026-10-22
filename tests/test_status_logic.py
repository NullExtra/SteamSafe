import sys
import unittest
from pathlib import Path

# Menambahkan folder src agar fungsi dapat ditemukan saat pengujian.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from status_logic import determine_water_status


class TestWaterStatus(unittest.TestCase):

    def test_dry_returns_normal(self):
        self.assertEqual(
            determine_water_status("DRY"),
            "NORMAL"
        )

    def test_wet_returns_overflow_detected(self):
        self.assertEqual(
            determine_water_status("WET"),
            "OVERFLOW_DETECTED"
        )

    def test_missing_reading_returns_no_data(self):
        self.assertEqual(
            determine_water_status(None),
            "NO_DATA"
        )

    def test_lowercase_is_accepted(self):
        self.assertEqual(
            determine_water_status("wet"),
            "OVERFLOW_DETECTED"
        )

    def test_invalid_value_returns_no_data(self):
        self.assertEqual(
            determine_water_status("UNKNOWN"),
            "NO_DATA"
        )


if __name__ == "__main__":
    unittest.main()