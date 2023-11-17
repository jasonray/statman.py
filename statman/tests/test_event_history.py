import time
import datetime
import unittest
import random
from statman import Statman
from statman.history import History


class TestEventHistory(unittest.TestCase):

    def test_history_empty_count(self):
        history = History()
        self.assertEqual(history.count(), 0)

    def test_history_count(self):
        history = History()
        history.append("01/01/2023 11:31:45", 20)
        history.append("01/01/2023 11:32:45", 10)
        history.append("01/01/2023 11:33:45", 30)

        self.assertEqual(history.count(), 3)

    def test_history_get_events(self):
        history = History()
        history.append("01/01/2023 11:31:45", 20)
        history.append("01/01/2023 11:32:45", 10)
        history.append("01/01/2023 11:33:45", 30)

        events = history.events()
        self.assertEqual(events[0].dt.year, 2023)

    def test_history_get_values(self):
        history = History()
        history.append("01/01/2023 11:31:45", 20)
        history.append("01/01/2023 11:32:45", 10)
        history.append("01/01/2023 11:33:45", 30)

        self.assertEqual(history.values()[1], 10)

    def test_history_get_max_value(self):
        history = History()
        history.append("01/01/2023 11:31:45", 20)
        history.append("01/01/2023 11:32:45", 10)
        history.append("01/01/2023 11:33:45", 30)

        self.assertEqual(history.max_value(), 30)

    def test_history_get_min_value(self):
        history = History()
        history.append("01/01/2023 11:31:45", 20)
        history.append("01/01/2023 11:32:45", 10)
        history.append("01/01/2023 11:33:45", 30)

        self.assertEqual(history.min_value(), 10)

    def test_history_get_sum_value(self):
        history = History()
        history.append("01/01/2023 11:31:45", 20)
        history.append("01/01/2023 11:32:45", 10)
        history.append("01/01/2023 11:33:45", 30)

        self.assertEqual(history.sum_value(), 60)

    def test_history_get_ave_value(self):
        history = History()
        history.append("01/01/2023 11:31:45", 20)
        history.append("01/01/2023 11:32:45", 10)
        history.append("01/01/2023 11:33:45", 60)

        self.assertEqual(history.average_value(), 30)

    def test_history_get_median_value(self):
        history = History()
        history.append("01/01/2023 11:31:45", 20)
        history.append("01/01/2023 11:32:45", 10)
        history.append("01/01/2023 11:33:45", 60)

        self.assertEqual(history.median_value(), 20)



    # def test_perf(self):
    #     history = History()

    #     number_of_events = 1000000
    #     min_value = 1000
    #     max_value = 2000
    #     expected_ave = min_value+ ((max_value-min_value) / 2)

    #     sw = Statman.stopwatch(autostart=True)
    #     for i in range(0 , number_of_events):
    #         value = random.randint(min_value,max_value)
    #         history.append("01/01/2023 11:31:45", value)
    #     sw.stop()

    #     print('time:', sw.value)
    #     sw.print()
    #     self.assertEqual(history.count() , number_of_events)
    #     self.assertAlmostEqual(history.average_value(), expected_ave,0)
