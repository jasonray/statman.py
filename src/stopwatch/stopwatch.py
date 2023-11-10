import time


class Stopwatch():
    _name = None
    _start_time = None
    _stop_time = None

    def __init__(self, name=None, autostart=False):
        self._name = name
        if autostart:
            self.start()

    @property
    def name(self) -> str:
        return self._name

    def start(self):
        self._start_time = time.time()

    def stop(self) -> int:
        self._stop_time = time.time()

    def read(self):
        stop_time = None
        if self._stop_time:
            stop_time = self._stop_time
        else:
            stop_time = time.time()
        delta = stop_time - self._start_time
        return delta
