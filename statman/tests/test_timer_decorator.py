import unittest
import time
import statman
from statman import Statman
from statman.stopwatch import Stopwatch


class TestStopwatch(unittest.TestCase):

    def test_decorator_stopwatch(self):
        delay = 7
        result = self.sut('moto', delay=delay)
        self.assertEqual(result, 'hello moto')

        self.assertIsNotNone(Statman.stopwatch('sut.timer'))
        self.assertEqual(Statman.stopwatch('sut.timer').name, 'sut.timer')
        self.assertAlmostEqual(Statman.stopwatch('sut.timer').value, delay, delta=0.1)

    @statman.timer(name="sut.timer")
    def sut(self, n: str, delay: int = 1):
        msg = f'hello {n}'
        print(msg)
        time.sleep(delay)
        return msg

    def test_decorator_stopwatch_2(self):
        delay = 5
        result = self.sut('moto2', delay=delay)
        self.assertEqual(result, 'hello moto2')
        # self.assertAlmostEqual(stopwatch.read(), test_time_s, delta=self._accepted_variance)

        self.assertIsNotNone(Statman.stopwatch('sut.timer'))
        self.assertEqual(Statman.stopwatch('sut.timer').name, 'sut.timer')
        self.assertAlmostEqual(Statman.stopwatch('sut.timer').value, delay, delta=0.1)
