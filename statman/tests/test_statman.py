import unittest
import time
from statman import Statman
import pytest


class TestStatman(unittest.TestCase):
    _accepted_variance = 0.1

    @pytest.fixture(autouse=True)
    def run_before_and_after_tests(data):
        print('reset registry between tests')
        Statman.reset()

    def log(self, message):
        print(f'{TestStatman} {message}')

class TestGaugeViaStatman(TestStatman):
    def test_create_gauge_via_statman_package(self):
        import statman
        gauge = statman.Gauge()
        gauge.value = 1
        self.assertEqual(gauge.value, 1)

    def test_access_gauge_through_registry(self):
        g1 = Statman.gauge('g1')
        g1.value = 1

        Statman.gauge(name='g2', value=2).increment()

        Statman.gauge('g3')
        Statman.gauge('g3').value = 20
        Statman.gauge('g3').increment(10)

        self.assertEqual(Statman.gauge('g1').name, 'g1')
        self.assertEqual(Statman.gauge('g1').value, 1)
        self.assertEqual(Statman.gauge('g2').value, 3)
        self.assertEqual(Statman.gauge('g3').value, 30)

    def test_report(self):
        Statman.gauge('g1').value = 1
        Statman.gauge('g2').value = 2
        Statman.gauge('g3')
        Statman.gauge('g4').increment()
        Statman.stopwatch('sw1', autostart=True, enable_history=True)
        time.sleep(1)
        Statman.stopwatch('sw1').stop()
        Statman.stopwatch('sw1', autostart=True, enable_history=True)
        Statman.stopwatch('sw2', autostart=True, enable_history=True)
        Statman.stopwatch('sw3', autostart=False, enable_history=True)
        Statman.stopwatch('sw4', autostart=True, enable_history=True)
        time.sleep(2)
        Statman.stopwatch('sw1').stop()
        Statman.stopwatch('sw4').stop()

        message = Statman.report(output_stdout=False, log_method=self.log)
        print('raw message:', message)

class TestStopwatchViaStatman(TestStatman):
    def test_create_stopwatch_via_statman_package(self):
        import statman
        sw = statman.Stopwatch()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)

    def test_create_stopwatch_directly(self):
        from statman import Stopwatch
        sw = Stopwatch()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)


    def test_create_stopwatch_via_statman_constructor(self):
        sw = Statman.stopwatch()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)

    def test_create_stopwatch_via_statman_constructor_autostart(self):
        sw = Statman.stopwatch(autostart=True)
        time.sleep(1)
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)

        sw = Statman.stopwatch(autostart=False)
        time.sleep(1)
        self.assertIsNone(sw.read())

    def test_access_stopwatch_through_registry_get(self):
        Statman.stopwatch('stopwatch-name').start()
        time.sleep(1)

        sw = Statman.get('stopwatch-name')
        Statman.report(output_stdout=True)
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)

    def test_access_stopwatch_through_registry_stopwatch(self):
        Statman.stopwatch('stopwatch-name').start()
        time.sleep(1)

        sw = Statman.stopwatch('stopwatch-name')
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)

    def test_ensure_reset_between_tests(self):
        sw = Statman.get('stopwatch-name')
        self.assertIsNone(sw)

    def test_registry_count_0(self):
        self.assertEqual(0, Statman.count())

    def test_registry_count_1(self):
        Statman.stopwatch('stopwatch-name')
        self.assertEqual(1, Statman.count())

    def test_registry_count_2(self):
        Statman.stopwatch('stopwatch-name')
        Statman.stopwatch('stopwatch-name2')
        self.assertEqual(2, Statman.count())

    def test_registry_count_duplicates(self):
        Statman.stopwatch('stopwatch-name')
        Statman.stopwatch('stopwatch-name')
        Statman.stopwatch('stopwatch-name2')
        self.assertEqual(2, Statman.count())

    def test_registry_count_with_reset(self):
        Statman.stopwatch('stopwatch-name')
        Statman.reset()
        Statman.stopwatch('stopwatch-name2')
        self.assertEqual(1, Statman.count())

    def test_dual_stopwatches_read(self):
        Statman.stopwatch(name='a', autostart=False)
        Statman.stopwatch(name='b', autostart=False)

        Statman.stopwatch('a').start()
        time.sleep(0.3)

        Statman.stopwatch('b').start()
        time.sleep(0.3)

        self.assertAlmostEqual(Statman.stopwatch('a').read(), 0.6, delta=self._accepted_variance)
        self.assertAlmostEqual(Statman.stopwatch('b').read(), 0.3, delta=self._accepted_variance)

    def test_dual_stopwatches_read_with_get(self):
        Statman.stopwatch(name='a', autostart=False)
        Statman.stopwatch(name='b', autostart=False)

        Statman.stopwatch('a').start()
        time.sleep(0.3)

        Statman.get('b').start()
        time.sleep(0.3)

        self.assertAlmostEqual(Statman.stopwatch('a').read(), 0.6, delta=self._accepted_variance)
        self.assertAlmostEqual(Statman.get('b').read(), 0.3, delta=self._accepted_variance)

    def test_simplified_access(self):
        from statman import Statman as SM

        SM.stopwatch(name='a', autostart=False)
        SM.stopwatch(name='b', autostart=False)

        SM.stopwatch('a').start()
        time.sleep(0.3)

        SM.get('b').start()
        time.sleep(0.3)

        self.assertAlmostEqual(SM.stopwatch('a').read(), 0.6, delta=self._accepted_variance)
        self.assertAlmostEqual(SM.get('b').read(), 0.3, delta=self._accepted_variance)

    def test_manually_registry(self):
        from statman import Stopwatch
        sw = Stopwatch()
        Statman.register('sw', sw)

        Statman.get('sw').start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)


class TestCalculationViaStatman(TestStatman):
    def test_calculation_metric(self):
        Statman.stopwatch('sw').start()
        time.sleep(0.5)
        Statman.stopwatch('sw').stop()

        Statman.gauge('messages_processed').value = 100

        Statman.calculation(
            'messages_per_second').calculation_function = lambda: (Statman.gauge('messages_processed').value / Statman.stopwatch('sw').value)
        Statman.calculation('messages_per_millisecond').calculation_function = lambda: (Statman.get('messages_per_second').value / 1000)

        self.assertAlmostEqual(Statman.calculation('messages_per_second').value, 200, delta=5)
        self.assertAlmostEqual(Statman.calculation('messages_per_millisecond').value, 0.2, places=1)

    def test_calculation_metric_invalid_functions(self):
        Statman.stopwatch('sw')

        Statman.gauge('messages_processed').value = 100

        Statman.calculation(
            'messages_per_second').calculation_function = lambda: (Statman.gauge('messages_processed').value / Statman.stopwatch('sw').value)
        Statman.calculation('messages_per_millisecond').calculation_function = lambda: (Statman.get('messages_per_second').value / 1000)

        self.assertIsNone(Statman.calculation('messages_per_second').value)
        self.assertIsNone(Statman.calculation('messages_per_millisecond').value)

    def test_mutated_registry_during_reporting(self):
        Statman.stopwatch('sw')
        Statman.calculation(
            'messages_per_second').calculation_function = lambda: (Statman.gauge('messages_processed').value / Statman.stopwatch('sw').value)
        Statman.report(output_stdout=True)