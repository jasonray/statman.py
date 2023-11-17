import time
import datetime


class History():
    _data = []

    def __init__(self):
        _data = []

    def __str__(self):
        pass

    def append(self, dt:datetime=None , value:float = None) -> str:
        event = self.create_event(dt=dt, value=value)
        self._data.append(event)

    def create_event(self, dt, value):
        event = {}
        if isinstance(dt, str):
            dt = datetime.datetime.strptime(dt, '%m/%d/%Y %H:%M:%S')
        event['dt'] = dt
        event['value'] = value

    def count(self):
        return len(self._data)
