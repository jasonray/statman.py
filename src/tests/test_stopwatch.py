import unittest
import time
from src.stopwatch.stopwatch import Stopwatch


class TestStopwatch(unittest.TestCase):
    _accepted_variance = 0.1

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

    def test_start_read_100ms(self):
        test_time_s = 0.100
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        self.assertAlmostEqual(stopwatch.read(), test_time_s, delta=self._accepted_variance)
        
    def test_start_read_1s(self):
        test_time_s = 1
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        self.assertAlmostEqual(stopwatch.read(), test_time_s, delta=self._accepted_variance)