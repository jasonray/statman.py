import datetime
import unittest
from statman.history import History


class TestEventHistory(unittest.TestCase):

    def test_history_empty_count(self):
        history =  History()
        self.assertEqual( history.count(), 0 )

    def test_history_count(self):
        history =  History()
        history.append( "01/01/2023 11:31:45", 20) 
        history.append( "01/01/2023 11:32:45", 10) 
        history.append( "01/01/2023 11:33:45", 30) 

        self.assertEqual( history.count(), 3 )



