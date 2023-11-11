import statman.stopwatch

_registry = {}

class Statman():

    def __init__(self):
        pass

    @staticmethod    
    def stopwatch(name=None) -> statman.Stopwatch:
        print('get/create sw', name)
        sw=None
        if name:
            sw=_registry.get(name)
        
        if not sw:
            sw = statman.Stopwatch()

        if not name is None:
            _registry[name] = sw

        return sw

    @staticmethod    
    def get(name):
        print('get by name', name)
        return _registry[name]
