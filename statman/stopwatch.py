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

    def stop(self, units: str = 's', precision: int = None) -> float:
        self._stop_time = time.time()
        return self.read(units=units , precision=precision)

    def read(self, units: str = 's', precision: int = None) -> float:
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

            if not units is None:
                if units == 's':
                    # no conversion, already in seconds
                    pass
                elif units == 'ms':
                    delta = delta * 1000
                elif units == 'm':
                    delta = delta / 60
                else:
                    raise Exception(f'Invalid units {units}')

            if not precision is None:
                delta = round(delta, precision)
        return delta

    def time(self, units: str = 's', precision: int = None) -> float:
        return self.read(units=units , precision=precision)
