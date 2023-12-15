from .statman import Statman


def timer(name):

    def timer_inner_decorator(func):

        def timer_wrapper(*args, **kwargs):
            sw = Statman.stopwatch(name=name, enable_history=True, thread_safe=True)
            sw.start()
            result = func(*args, **kwargs)
            sw.stop()
            return result

        return timer_wrapper

    return timer_inner_decorator
