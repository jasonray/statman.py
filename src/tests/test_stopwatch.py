import unittest
from src.stopwatch.stopwatch import Stopwatch


class TestStopwatch(unittest.TestCase):

    def test_create_with_no_params(self):
        stopwatch = Stopwatch()
        self.assertIsNotNone(stopwatch)
        self.assertEquals(stopwatch.name(),None)
