import time

class Stopwatch():
    _name = None
    _start_time = None

    def __init__(self, name=None):
        self._name = name

    def read(self) -> int:
        return 0
    
    @property
    def name(self) -> str:
        return self._name
    
    def start(self):
        self._start_time = time.time()

    def read(self):
        now = time.time()
        delta = now - self._start_time
        return delta