import unittest
import time
from statman import Statman
from statman.calculation import Calculation


class TestCalculation(unittest.TestCase):
    _accepted_variance = 0.1

    def test_create(self):
        calc = Calculation()
        self.assertIsNotNone(calc)
        self.assertEqual(calc.name, None)
        self.assertEqual(calc.calculation_function, None)

    def test_create_with_name(self):
        f = lambda: 1
        calc = Calculation(function=f, name='n')
        self.assertEqual(calc.name, 'n')

    def test_static_function(self):
        f = lambda: 1
        calc = Calculation(function=f, name='n')
        self.assertEqual(calc.read(), 1)

    def test_static_function_using_gauge_ref(self):
        Statman.gauge('temp_f').value = 32

        f_to_c = lambda: (Statman.gauge('temp_f').value - 32) * 5 / 9
        calc = Calculation(function=f_to_c, name='temp_c')
        self.assertEqual(calc.value, 0)

        Statman.gauge('temp_f').value = 212
        self.assertEqual(calc.value, 100)

    def test_round(self):
        Statman.gauge('temp_f').value = 0

        f_to_c = lambda: (Statman.gauge('temp_f').value - 32) * 5 / 9
        calc = Calculation(function=f_to_c, name='temp_c')
        self.assertEqual(calc.read(1), -17.8)

    def test_static_function_using_stopwatch_ref(self):
        Statman.stopwatch('sw').start()
        time.sleep(1)
        Statman.stopwatch('sw').stop()

        f = lambda: (Statman.stopwatch('sw').value * 2)
        calc = Calculation(function=f, name='f')
        self.assertAlmostEqual(calc.value, 2, 1)

    def test_function_use_two_metrics(self):
        Statman.stopwatch('sw').start()
        time.sleep(0.5)
        Statman.stopwatch('sw').stop()

        Statman.gauge('messages_processed').value = 100

        f_messages_per_second = lambda: (Statman.gauge('messages_processed').value / Statman.stopwatch('sw').value)
        messages_per_second = Calculation(function=f_messages_per_second, name='messages_per_second')
        self.assertAlmostEqual(messages_per_second.value, 200, delta=5)

    def test_invalid_state_on_sw(self):
        Statman.stopwatch('sw').start()
        Statman.gauge('messages_processed').value = 100

        f_messages_per_second = lambda: (Statman.gauge('messages_processed').value / Statman.stopwatch('sw').value)
        messages_per_second = Calculation(function=f_messages_per_second, name='messages_per_second')
        self.assertIsNone(messages_per_second.value)
        self.assertIsNone(messages_per_second.read())

    def test_div_by_zero(self):
        f_div_zero = lambda: (1 / 0)
        dev_zero = Calculation(function=f_div_zero, name='div_zero')
        self.assertIsNone(dev_zero.value)
        self.assertIsNone(dev_zero.read())
