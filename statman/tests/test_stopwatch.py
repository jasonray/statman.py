import unittest
import time
import statman
from statman.stopwatch import Stopwatch


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

    def test_start_read_units_s(self):
        test_time_s = 1
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        delta = stopwatch.read(units='s', precision=1)
        self.assertAlmostEqual(delta, 1, delta=self._accepted_variance)

    def test_start_read_units_ms(self):
        test_time_s = 1
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        delta = stopwatch.read(units='ms', precision=1)
        self.assertTrue(990 <= delta <= 1010)

    # too expensive, need to look for mock time increment
    # def test_start_read_units_min(self):
    #     test_time_s = 3 * 60
    #     stopwatch = Stopwatch(name='sw')
    #     stopwatch.start()
    #     time.sleep(test_time_s)
    #     delta = stopwatch.read(units='m', precision=1)
    #     self.assertAlmostEqual(delta, 3, delta=self._accepted_variance)

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
        self.assertEqual(stopwatch.read(precision=1), test_time_s)

    def test_start_read_with_precision_1s(self):
        test_time_s = 1.1
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        self.assertEqual(stopwatch.read(precision=0), 1)
        self.assertEqual(stopwatch.read(precision=1), 1.1)

    def test_start_stop_with_precision(self):
        test_time_s = 0.3
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        self.assertEqual(stopwatch.stop(precision=1), test_time_s)

    def test_access_through_statman(self):
        stopwatch = statman.Stopwatch()
        self.assertIsNotNone(stopwatch)
        self.assertEqual(stopwatch.name, None)

    def test_start_then_restart(self):
        test_time_s = 0.250
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)

        stopwatch.restart()
        time.sleep(test_time_s)

        self.assertAlmostEqual(stopwatch.read(), test_time_s, delta=self._accepted_variance)

    def test_start_stop_then_restart(self):
        test_time_s = 0.250
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        stopwatch.stop()
        time.sleep(test_time_s)

        stopwatch.restart()
        time.sleep(test_time_s)

        self.assertAlmostEqual(stopwatch.read(), test_time_s, delta=self._accepted_variance)

    def test_reset(self):
        test_time_s = 0.250
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        stopwatch.reset()
        self.assertIsNone(stopwatch.read())

    # re-enable after mock of time increment
    # def test_stopped_to_string(self):
    #     test_time_s = 0.2
    #     stopwatch = StopwatchC(name='sw')
    #     stopwatch.start()
    #     time.sleep(test_time_s)
    #     stopwatch.stop()
    #     expected = '[sw => state:None; elapsed:200ms]'
    #     self.assertEqual(str(stopwatch), expected)

    # re-enable after mock of time increment
    # def test_stopped_no_name_to_string(self):
    #     test_time_s = 0.2
    #     stopwatch = StopwatchC()
    #     stopwatch.start()
    #     time.sleep(test_time_s)
    #     stopwatch.stop()
    #     expected = '[(Stopwatch) => state:None; elapsed:200ms]'
    #     self.assertEqual(str(stopwatch), expected)

    def test_value(self):
        test_time_s = 0.250
        stopwatch = Stopwatch(name='sw')
        stopwatch.start()
        time.sleep(test_time_s)
        self.assertIsNone(stopwatch.value())
        stopwatch.stop()
        self.assertAlmostEqual(stopwatch.value(), test_time_s, delta=self._accepted_variance)
