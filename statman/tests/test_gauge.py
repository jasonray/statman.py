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

    def test_value(self):
        gauge = Gauge('g')
        gauge.value = 5
        self.assertEqual(gauge.value, 5)

    def test_value_init_0(self):
        gauge = Gauge('g')
        self.assertEqual(gauge.value, 0)

    def test_value_multiple(self):
        gauge = Gauge('g')
        gauge.value = 5
        self.assertEqual(gauge.value, 5)
        gauge.value = 6
        self.assertEqual(gauge.value, 6)

    def test_set_value_to_none_resets_to_0(self):
        gauge = Gauge('g')
        gauge.value = 5
        self.assertEqual(gauge.value, 5)
        gauge.value = None
        self.assertEqual(gauge.value, 0)

    def test_increment(self):
        gauge = Gauge('g')
        gauge.value = 5
        gauge.increment()
        self.assertEqual(gauge.value, 6)

    def test_increment_none_value(self):
        gauge = Gauge('g')
        gauge.value = 5
        gauge.increment(amount=None)
        self.assertEqual(gauge.value, 6)

    def test_increment_zero_value(self):
        gauge = Gauge('g')
        gauge.value = 5
        gauge.increment(amount=0)
        self.assertEqual(gauge.value, 5)

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

    def test_decrement_none_value(self):
        gauge = Gauge('g')
        gauge.value = 5
        gauge.decrement(amount=None)
        self.assertEqual(gauge.value, 4)

    def test_decrement_zero_value(self):
        gauge = Gauge('g')
        gauge.value = 5
        gauge.decrement(amount=0)
        self.assertEqual(gauge.value, 5)

    def test_decrement_2(self):
        gauge = Gauge('g')
        gauge.value = 5
        gauge.decrement(2)
        self.assertEqual(gauge.value, 3)

    def test_increment_against_none(self):
        gauge = Gauge('g')
        gauge.increment()
        self.assertEqual(gauge.value, 1)

    def test_decrement_against_none(self):
        gauge = Gauge('g')
        gauge.increment()
        self.assertEqual(gauge.value, 1)

    def test_to_string(self):
        gauge = Gauge('g')
        gauge.value = 5
        expected = '[g => value=5]'
        self.assertEqual(str(gauge), expected)
