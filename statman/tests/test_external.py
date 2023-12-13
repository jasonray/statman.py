import unittest
from statman import Statman
from statman.gauge import Gauge
from statman.statman import ExternalSource


class TestExternal(unittest.TestCase):

    def test_function_return_dict(self):
        Statman.reset()
        f = lambda: {"k1": 1, "k2": 2}

        external_source = ExternalSource(function=f, name="external")
        self.assertEqual(Statman.gauge("external.k1").value, 1)
        self.assertEqual(Statman.gauge("external.k2").value, 2)

    def test_function_return_dict_with_numeric_string(self):
        Statman.reset()
        f = lambda: {"k1": "1", "k2": "2"}

        external_source = ExternalSource(function=f, name="external")
        self.assertEqual(Statman.gauge("external.k1").value, 1)
        self.assertEqual(Statman.gauge("external.k2").value, 2)

    def test_function_return_dict_with_nonnumeric_string(self):
        Statman.reset()
        f = lambda: {"k1": "1", "k2": "v2"}

        external_source = ExternalSource(function=f, name="external")
        self.assertIsNotNone(Statman.get("external.k1"))
        self.assertIsNone(Statman.get("external.k2"))

    def test_register_statman(self):
        Statman.reset()
        value = 1
        f = lambda: {"k1": value, "k2": 2}

        Statman.external_source(function=f, name="external")
        self.assertEqual(Statman.gauge("external.k1").value, 1)
        self.assertEqual(Statman.gauge("external.k2").value, 2)

    def test_statman_manual_refresh_external_source(self):
        Statman.reset()
        value = 1  # this gets hoisted into lambda
        f = lambda: {"k1": value, "k2": 2}

        Statman.external_source(function=f, name="external")
        self.assertEqual(Statman.gauge("external.k1").value, 1)
        self.assertEqual(Statman.gauge("external.k2").value, 2)

        value = 10
        Statman.external_source(name="external").refresh()
        self.assertEqual(Statman.gauge("external.k1").value, 10)
        self.assertEqual(Statman.gauge("external.k2").value, 2)

    def test_statman_auto_refresh_on_report_external_source(self):
        Statman.reset()
        value = 1  # this gets hoisted into lambda
        f = lambda: {"k1": value, "k2": 2}

        Statman.external_source(function=f, name="external")
        self.assertEqual(Statman.gauge("external.k1").value, 1)
        self.assertEqual(Statman.gauge("external.k2").value, 2)

        value = 10
        Statman.report()  # report is intended to refresh external sources
        self.assertEqual(Statman.gauge("external.k1").value, 10)
        self.assertEqual(Statman.gauge("external.k2").value, 2)
