import unittest
import time
from src.stopwatch.stopwatch import Stopwatch


class TestStopwatch(unittest.TestCase):
    _accepted_variance = 0.1

    def test_create_with_no_params(self):
        stopwatch = Stopwatch()
        self.assertIsNotNone(stopwatch)
        self.assertEqual(stopwatch.name, None)

    def test_create_with_empty_string(self):
        stopwatch = Stopwatch("")
        self.assertIsNotNone(stopwatch)
        self.assertEqual(stopwatch.name, "")

    def test_create_with_name(self):
        stopwatch = Stopwatch('sw')
        self.assertIsNotNone(stopwatch)
        self.assertEqual(stopwatch.name, 'sw')

    def test_create_with_name_by_label(self):
        stopwatch = Stopwatch(name='sw')
        self.assertIsNotNone(stopwatch)
        self.assertEqual(stopwatch.name, 'sw')

    def test_start_read_250ms(self):
        test_time_s = 0.250
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

    def test_autostart_read_250ms(self):
        test_time_s = 0.25
        stopwatch = Stopwatch(name='sw', autostart=True)
        time.sleep(test_time_s)
        self.assertAlmostEqual(stopwatch.read(), test_time_s, delta=self._accepted_variance)

    def test_stop_returns_time(self):
        test_time_s = 0.25
        stopwatch = Stopwatch(name='sw', autostart=True)
        time.sleep(test_time_s)
        self.assertAlmostEqual(stopwatch.stop(), test_time_s, delta=self._accepted_variance)

    def test_dual_stopwatches_names(self):
        stopwatchA = Stopwatch(name='a', autostart=False)
        stopwatchB = Stopwatch(name='b', autostart=False)

        self.assertEqual(stopwatchA.name, 'a')
        self.assertEqual(stopwatchB.name, 'b')

    def test_dual_stopwatches_read(self):
        stopwatchA = Stopwatch(name='a', autostart=False)
        stopwatchB = Stopwatch(name='b', autostart=False)

        stopwatchA.start()
        time.sleep(0.3)

        stopwatchB.start()
        time.sleep(0.3)

        self.assertAlmostEqual(stopwatchA.read(), 0.6, delta=self._accepted_variance)
        self.assertAlmostEqual(stopwatchB.read(), 0.3, delta=self._accepted_variance)

    def test_start_stop_read(self):
        test_time_s = 0.25
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        stopwatch.stop()
        time.sleep(test_time_s)
        self.assertAlmostEqual(stopwatch.read(), test_time_s, delta=self._accepted_variance)

    def test_read_without_start_return_none(self):
        stopwatch = Stopwatch(name='sw')
        self.assertIsNone(stopwatch.read())

    def test_two_stops_second_time(self):
        test_time_s = 0.25
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        stopwatch.stop()
        time.sleep(test_time_s)
        stopwatch.stop()
        self.assertAlmostEqual(stopwatch.read(), test_time_s * 2, delta=self._accepted_variance)

    def test_start_delta(self):
        test_time_s = 0.250
        stopwatch = Stopwatch(name='sw', initial_delta=1)
        stopwatch.start()
        time.sleep(test_time_s)
        self.assertAlmostEqual(stopwatch.read(), test_time_s + 1, delta=self._accepted_variance)

    def test_start_read_with_precision(self):
        test_time_s = 0.3
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        self.assertAlmostEqual(stopwatch.read(precision=1), test_time_s, delta=self._accepted_variance)

    def test_start_read_with_precision_1s(self):
        test_time_s = 1.1
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        self.assertAlmostEqual(stopwatch.read(precision=0), 1, delta=self._accepted_variance)
        self.assertAlmostEqual(stopwatch.read(precision=1), 1.1, delta=self._accepted_variance)

    def test_start_stop_with_precision(self):
        test_time_s = 0.3
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        self.assertAlmostEqual(stopwatch.stop(precision=1), test_time_s, delta=self._accepted_variance)

    def test_start_time(self):
        test_time_s = 1.1
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        self.assertAlmostEqual(stopwatch.time(precision=0), 1, delta=self._accepted_variance)
        self.assertAlmostEqual(stopwatch.time(precision=1), 1.1, delta=self._accepted_variance)
