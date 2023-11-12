import unittest
from statman.gauge import Gauge


class TestGauge(unittest.TestCase):

    def test_create_with_no_params(self):
        gauge = Gauge()
        self.assertIsNotNone(gauge)
        self.assertEqual(gauge.name, None)

    def test_create_with_name(self):
        gauge = Gauge('g')
        self.assertEqual(gauge.name, 'g')

    def test_create_with_name(self):
        gauge = Gauge('g')
        gauge.value = 5
        self.assertEqual(gauge.value, 5)

    def test_increment(self):
        gauge = Gauge('g')
        gauge.value = 5
        gauge.increment()
        self.assertEqual(gauge.value, 6)

    def test_increment_2(self):
        gauge = Gauge('g')
        gauge.value = 5
        gauge.increment(2)
        self.assertEqual(gauge.value, 7)

    def test_decrement(self):
        gauge = Gauge('g')
        gauge.value = 5
        gauge.decrement()
        self.assertEqual(gauge.value, 4)

    def test_decrement_2(self):
        gauge = Gauge('g')
        gauge.value = 5
        gauge.decrement(2)
        self.assertEqual(gauge.value, 3)
