import unittest
from statman.gauge import Gauge


class TestGauge(unittest.TestCase):
    def test_create_with_no_params(self):
        g = Gauge()
        self.assertIsNotNone(g)
        self.assertEqual(g.name, None)

    def test_create_with_name(self):
        g = Gauge('g')
        self.assertIsNotNone(g)
        self.assertEqual(g.name, 'g')

