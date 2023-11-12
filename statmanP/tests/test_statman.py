import unittest
import time
from statmanP import StatmanC
import pytest


class TestStatman(unittest.TestCase):
    _accepted_variance = 0.1

    @pytest.fixture(autouse=True)
    def run_before_and_after_tests(data):
        print('reset registry between tests')
        StatmanC.reset()

    def test_create_stopwatch_directly(self):
        from statmanP import StopwatchC
        sw = StopwatchC()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)

    def test_create_stopwatch_via_statman_package(self):
        import statmanP
        sw = statmanP.StopwatchC()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)

    def test_create_stopwatch_via_statman_constructor(self):
        sw = StatmanC.stopwatch()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)

    def test_create_stopwatch_via_statman_constructor_autostart(self):
        sw = StatmanC.stopwatch(autostart=True)
        time.sleep(1)
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)

        sw = StatmanC.stopwatch(autostart=False)
        time.sleep(1)
        self.assertIsNone(sw.read())

    def test_access_stopwatch_through_registry_get(self):
        StatmanC.stopwatch('stopwatch-name').start()
        time.sleep(1)

        sw = StatmanC.get('stopwatch-name')
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)

    def test_access_stopwatch_through_registry_stopwatch(self):
        StatmanC.stopwatch('stopwatch-name').start()
        time.sleep(1)

        sw = StatmanC.stopwatch('stopwatch-name')
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)

    def test_ensure_reset_between_tests(self):
        sw = StatmanC.get('stopwatch-name')
        self.assertIsNone(sw)

    def test_registry_count_0(self):
        self.assertEqual(0, StatmanC.count())

    def test_registry_count_1(self):
        StatmanC.stopwatch('stopwatch-name')
        self.assertEqual(1, StatmanC.count())

    def test_registry_count_2(self):
        StatmanC.stopwatch('stopwatch-name')
        StatmanC.stopwatch('stopwatch-name2')
        self.assertEqual(2, StatmanC.count())

    def test_registry_count_duplicates(self):
        StatmanC.stopwatch('stopwatch-name')
        StatmanC.stopwatch('stopwatch-name')
        StatmanC.stopwatch('stopwatch-name2')
        self.assertEqual(2, StatmanC.count())

    def test_registry_count_with_reset(self):
        StatmanC.stopwatch('stopwatch-name')
        StatmanC.reset()
        StatmanC.stopwatch('stopwatch-name2')
        self.assertEqual(1, StatmanC.count())

    def test_dual_stopwatches_read(self):
        StatmanC.stopwatch(name='a', autostart=False)
        StatmanC.stopwatch(name='b', autostart=False)

        StatmanC.stopwatch('a').start()
        time.sleep(0.3)

        StatmanC.stopwatch('b').start()
        time.sleep(0.3)

        self.assertAlmostEqual(StatmanC.stopwatch('a').read(), 0.6, delta=self._accepted_variance)
        self.assertAlmostEqual(StatmanC.stopwatch('b').read(), 0.3, delta=self._accepted_variance)

    def test_dual_stopwatches_read_with_get(self):
        StatmanC.stopwatch(name='a', autostart=False)
        StatmanC.stopwatch(name='b', autostart=False)

        StatmanC.stopwatch('a').start()
        time.sleep(0.3)

        StatmanC.get('b').start()
        time.sleep(0.3)

        self.assertAlmostEqual(StatmanC.stopwatch('a').read(), 0.6, delta=self._accepted_variance)
        self.assertAlmostEqual(StatmanC.get('b').read(), 0.3, delta=self._accepted_variance)

    def test_simplified_access(self):
        from statmanP import StatmanC as SM

        SM.stopwatch(name='a', autostart=False)
        SM.stopwatch(name='b', autostart=False)

        SM.stopwatch('a').start()
        time.sleep(0.3)

        SM.get('b').start()
        time.sleep(0.3)

        self.assertAlmostEqual(SM.stopwatch('a').read(), 0.6, delta=self._accepted_variance)
        self.assertAlmostEqual(SM.get('b').read(), 0.3, delta=self._accepted_variance)

    def test_manually_registry(self):
        from statmanP import StopwatchC
        sw = StopwatchC()
        StatmanC.register('sw', sw)

        StatmanC.get('sw').start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read(), 1, delta=0.1)
