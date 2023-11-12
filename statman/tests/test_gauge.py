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

