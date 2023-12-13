from .metric import Metric
from statman import Statman
import re


class ExternalSource():
    _function = None
    _name = None

    def __init__(self, name:str,  function  ):
        self._function = function
        self._name = name
        self.refresh()

    def refresh(self) :
        try:
            f = self.refresh_function
            result = f()

            if isinstance(result, dict):
                for key in result:
                    value = result.get(key)
                    statman_key = f'{self._name}.{key}'
                    if isinstance(value, int) or isinstance(value, float):
                        print(f'setting gauge {key=} {value=} {statman_key=}')
                        Statman.gauge(statman_key).value = value
                    elif isinstance(value, str) and ExternalSource.is_numeric(value):
                        value = float(value)
                        print(f'setting gauge {key=} {value=} {statman_key=}')
                        Statman.gauge(statman_key).value = value
                    else:
                        print(f'skipping non-numeric value {key=} {value=} {statman_key=}')
            else:
                if isinstance(value, int) or isinstance(value, float):
                    print(f'skipping non-dictionary, numeric {result=}')
                else:
                    print(f'skipping non-dictionary {result=}')

        except Exception as e:
            print(f'failed to execute refresh method [{self._name}][{e}]')
            raise e

    @property
    def refresh_function(self):
        return self._function

    @staticmethod    
    def is_numeric(value):
        if isinstance(value, (int, float)):
            return True
        if isinstance(value, str):
            return bool(re.match(r"^-?\d+(\.\d+)?$", value))
        return False    

    # @refresh_function.setter
    # def refresh_function(self, function):
    #     self._function = function
