import unittest
from unittest.mock import patch
from pathlib import Path
from datetime import datetime
import numpy as np

from ausdex.dates import convert_date


class TestDates(unittest.TestCase):
    def test_str(self):
        result = convert_date("2006")
        self.assertIsInstance(result, np.ndarray)
        np.testing.assert_equal(result, np.array("2006-01-01", dtype="datetime64[D]"))

    def test_int(self):
        np.testing.assert_equal(
            convert_date(2006), np.array("2006-01-01", dtype="datetime64[D]")
        )

    def test_float(self):
        np.testing.assert_equal(
            convert_date(2006.5), np.array("2006-07-02", dtype="datetime64[D]")
        )

    def test_numpy_ints(self):
        dates = np.array([2006, 2007], dtype=np.int32)
        np.testing.assert_equal(
            convert_date(dates),
            np.array(["2006-01-01", "2007-01-01"], dtype="datetime64[D]"),
        )
