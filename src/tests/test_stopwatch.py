import unittest
from src.stopwatch.stopwatch import Stopwatch


class TestStopwatch(unittest.TestCase):

    def test_create_with_no_params(self):
        stopwatch = Stopwatch()
        self.assertIsNotNone(stopwatch)
        self.assertEqual(stopwatch.name,None)

    def test_create_with_empty_string(self):
        stopwatch = Stopwatch("")
        self.assertIsNotNone(stopwatch)
        self.assertEqual(stopwatch.name,"")

    def test_create_with_name(self):
        stopwatch = Stopwatch('sw')
        self.assertIsNotNone(stopwatch)
        self.assertEqual(stopwatch.name,'sw')

    def test_create_with_name_by_label(self):
        stopwatch = Stopwatch(name='sw')
        self.assertIsNotNone(stopwatch)
        self.assertEqual(stopwatch.name,'sw')
