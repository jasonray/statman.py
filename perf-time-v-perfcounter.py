import time
# from statman.stopwatch import Stopwatch
# import sys
# import statmanP.stopwatchM
# import statmanM
from statman.stopwatch import Stopwatch

for i in range(0, 2):
    iterations = 100000

    swt = Stopwatch('time.time', autostart=True)
    for i in range(0, iterations):
        time.time()
    swt.stop()
    swt.print()
    swpc = Stopwatch('time.perf_counter', autostart=True)
    for i in range(0, iterations):
        time.perf_counter()
    swpc.stop()
    swpc.print()
