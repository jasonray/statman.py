class Stopwatch():
    _name = None

    def __init__(self, name=None):
        self._name = name

    def read(self) -> int:
        return 0
    
    @property
    def name(self) -> str:
        return self._name
    
