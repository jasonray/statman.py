import unittest
import time
from statman import Statman

class TestStatman(unittest.TestCase):

    def test_create_stopwatch_directly(self):        
        from statman import Stopwatch
        sw=Stopwatch()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read() , 1, delta=0.1)

    def test_create_stopwatch_via_statman_package(self):        
        import statman
        sw=statman.Stopwatch()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read() , 1, delta=0.1)

    def test_create_stopwatch_via_statman_constructor(self):        
        sw=Statman.stopwatch()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read() , 1, delta=0.1)

    def test_access_stopwatch_through_registry_get(self):        
        Statman.stopwatch('stopwatch-name').start()
        time.sleep(1)

        sw = Statman.get('stopwatch-name')
        self.assertAlmostEqual(sw.read() , 1, delta=0.1)

    def test_access_stopwatch_through_registry_stopwatch(self):        
        Statman.stopwatch('stopwatch-name').start()
        time.sleep(1)

        sw = Statman.stopwatch('stopwatch-name')
        self.assertAlmostEqual(sw.read() , 1, delta=0.1)


