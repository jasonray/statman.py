import unittest
import time
from statman import Statman
from statman.statman import Rate
from statman.calculation import Calculation


class TestRate(unittest.TestCase):
    _accepted_variance = 0.1

    def test_create(self):
        rate = Rate()
        self.assertIsNotNone(rate)
        self.assertEqual(rate.name, None)

    def test_rate(self):
        Statman.stopwatch('sw').start()
        time.sleep(0.5)
        Statman.stopwatch('sw').stop()

        Statman.gauge('messages_processed').value = 100

        messages_per_second = Rate(name='messages_per_second', numerator_metric_name='messages_processed', denominator_metric_name='sw')
        self.assertAlmostEqual(messages_per_second.value, 200, delta=5)

    def test_rate_via_statman(self):
        Statman.stopwatch('sw').start()
        time.sleep(0.5)
        Statman.stopwatch('sw').stop()

        Statman.gauge('messages_processed').value = 100

        Statman.rate(name='messages_per_second', numerator_metric_name='messages_processed', denominator_metric_name='sw')
        self.assertAlmostEqual(Statman.rate('messages_per_second').value, 200, delta=5)

    # def test_rate_report(self):
    #     Statman.stopwatch('sw').start()
    #     time.sleep(0.5)
    #     Statman.stopwatch('sw').stop()
    #     Statman.gauge('messages_processed').value = 100
    #     messages_per_second = Rate(name='messages_per_second', numerator_metric_name='messages_processed', denominator_metric_name='sw')
    #     messages_per_second.report(output_stdout=True)
