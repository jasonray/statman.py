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
    def value(self, value: float) -> float:
        self._value = float(value)

    def increment(self, amount: int = 1) -> float:
        if self._value:
            self._value += amount
        else:
            self._value = amount


    def decrement(self, amount: int = 1) -> float:
        if self._value:
            self._value -= amount
        else:
            self._value = amount
