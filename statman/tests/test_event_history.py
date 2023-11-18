import datetime
import unittest
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

    def test_history_string_date(self):
        date_string = "01/01/2023 11:31:45"
        expected_dt = datetime.datetime.strptime(date_string, '%m/%d/%Y %H:%M:%S')

        history = History()
        history.append(value=20)
        history.append(dt=date_string, value=10)
        history.append(value=30)

        self.assertEqual(history.events()[1].dt, expected_dt)

    def test_history_date(self):
        date_string = "01/01/2023 11:31:45"
        dt = datetime.datetime.strptime(date_string, '%m/%d/%Y %H:%M:%S')

        history = History()
        history.append(value=20)
        history.append(dt=dt, value=10)
        history.append(value=30)

        self.assertEqual(history.events()[1].dt, dt)

    def test_history_default_date(self):
        history = History()
        history.append(value=20)
        history.append(value=10)
        history.append(value=30)

        self.assertTrue(isinstance(history.events()[1].dt, datetime.date))

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

    # def test_variance(self):
    #     history = History()

    #     number_of_events = 1000000

    #     for i in range(0 , number_of_events):
    #         sw = Statman.stopwatch()
    #         sw.start()
    #         sw.stop()
    #         history.append("01/01/2023 11:31:45", sw.read(units='ms')  )
    #     sw.stop()

    #     print( 'number of measurements:', history.count() )
    #     print( 'min:', history.min_value() )
    #     print( 'max:', history.max_value() )
    #     print( 'ave:', history.average_value() )
    #     print( 'mode:', history.mode_value() )

    #     # min:  0.0
    #     # max:  0.019124941900372505 ms
    #     # ave:  0.000089719530893489 ms
    #     # mode: 0.000082887709140777 ms

    #     1/0
