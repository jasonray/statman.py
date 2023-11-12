# import statmanP.stopwatchM
# import .stopwatchM
from .stopwatchM import StopwatchC

_registry = {}


class StatmanC():

    def __init__(self):
        pass

    @staticmethod
    def reset():
        '''Clears all metrics from the registry.'''
        _registry.clear()

    @staticmethod
    def count():
        '''Returns a count of the registered metrics.'''
        return len(_registry.keys())

    @staticmethod
    def stopwatch(name: str = None, autostart: bool = False, initial_delta: float = None) -> StopwatchC:
        ''' Returns a stopwatch instance.  If there is a registered stopwatch with this name, return it.  If there is no registered stopwatch with this name, create a new instance, register it, and return it. '''
        sw = StatmanC.get(name)

        if not sw:
            sw = StopwatchC(name=name, autostart=autostart, initial_delta=initial_delta)

        if not name is None:
            StatmanC.register(name, sw)

        return sw

    @staticmethod
    def register(name, metric):
        '''Manually register a new metric.'''
        _registry[name] = metric

    @staticmethod
    def get(name):
        metric = None
        if name:
            metric = _registry.get(name)
        return metric
