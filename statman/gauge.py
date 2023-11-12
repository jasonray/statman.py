class Gauge():
    _name = None
    _value = None

    def __init__(self, name=None):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value) -> float:
        self._value=float(value)
