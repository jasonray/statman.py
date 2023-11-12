import time
# from statman.stopwatch import Stopwatch
# import sys
# import statmanP.stopwatchM
# import statmanM
from statmanP.stopwatchM import StopwatchC

for i in range(0, 2):
    iterations = 100000000

    swt = StopwatchC('time.time', autostart=True)
    for i in range(0, iterations):
        time.time()
    swt.stop()
    swt.print()
    swpc = StopwatchC('time.perf_counter', autostart=True)
    for i in range(0, iterations):
        time.perf_counter()
    swpc.stop()
    swpc.print()
