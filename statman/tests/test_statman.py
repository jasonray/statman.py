import unittest
import time
from statman import StatmanC

class TestStatman(unittest.TestCase):

    def test_create_stopwatch_directly(self):        
        from statman import StopwatchC
        sw=StopwatchC()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read() , 1, delta=0.1)

    def test_create_stopwatch_via_statman_package(self):        
        import statman
        sw=statman.StopwatchC()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read() , 1, delta=0.1)

    def test_create_stopwatch_via_statman_constructor(self):        
        sw=StatmanC.stopwatch()
        sw.start()
        time.sleep(1)
        self.assertAlmostEqual(sw.read() , 1, delta=0.1)

    def test_access_stopwatch_through_registry_get(self):        
        StatmanC.stopwatch('stopwatch-name').start()
        time.sleep(1)

        sw = StatmanC.get('stopwatch-name')
        self.assertAlmostEqual(sw.read() , 1, delta=0.1)

    def test_access_stopwatch_through_registry_stopwatch(self):        
        StatmanC.stopwatch('stopwatch-name').start()
        time.sleep(1)

        sw = StatmanC.stopwatch('stopwatch-name')
        self.assertAlmostEqual(sw.read() , 1, delta=0.1)


