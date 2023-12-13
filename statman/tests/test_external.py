import unittest
from statman import Statman
from statman.external_source import ExternalSource
from statman.gauge import Gauge


class TestExternal(unittest.TestCase):

    def test_function_return_dict(self):
        Statman.reset()
        f = lambda : {"k1":1, "k2":2}

        external_source =ExternalSource (function=f, name="external")
        self.assertEqual( Statman.gauge("external.k1").value , 1  )
        self.assertEqual( Statman.gauge("external.k2").value , 2  )

    def test_function_return_dict_with_numeric_string(self):
        Statman.reset()
        f = lambda : {"k1":"1", "k2":"2"}

        external_source =ExternalSource (function=f, name="external")
        self.assertEqual( Statman.gauge("external.k1").value , 1  )
        self.assertEqual( Statman.gauge("external.k2").value , 2  )

    def test_function_return_dict_with_nonnumeric_string(self):
        Statman.reset()
        f = lambda : {"k1":"1", "k2":"v2"}

        external_source =ExternalSource (function=f, name="external")
        self.assertIsNotNone( Statman.get("external.k1")  )
        self.assertIsNone( Statman.get("external.k2")  )
