import time


class Stopwatch():
    _name = None
    _start_time = None
    _stop_time = None
    _initial_delta = None

    def __init__(self, name=None, autostart=False, initial_delta=None):
        self._name = name
        self._initial_delta = initial_delta
        if autostart:
            self.start()

    @property
    def name(self) -> str:
        return self._name

    def start(self):
        self._start_time = time.time()

    def stop(self, precision=None) -> float:
        self._stop_time = time.time()
        return self.read(precision=precision)

    def read(self, precision=None) -> float:
        delta = None
        if self._start_time:
            stop_time = None
            if self._stop_time:
                stop_time = self._stop_time
            else:
                stop_time = time.time()
            delta = stop_time - self._start_time

            if self._initial_delta:
                delta += self._initial_delta

            if not precision is None:
                delta = round(delta, precision)
        return delta

    def time(self, precision=None) -> float:
        return self.read(precision=precision)
