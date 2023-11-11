# statman

[![Python package](https://github.com/jasonray/statman-stopwatch.py/actions/workflows/python-package.yml/badge.svg)](https://github.com/jasonray/statman-stopwatch.py/actions/workflows/python-package.yml)
[![PyPI version](https://badge.fury.io/py/statman.svg)](https://badge.fury.io/py/statman)
[![Known Vulnerabilities](https://snyk.io/test/github/jasonray/statman.py/badge.svg)](https://snyk.io/test/github/jasonray/statman.py)

# Overview

Statman is a collection of metric collectors to embed within your python application.  It includes a registry to easily access your metrics.

`Statman` => registry
`Metric` => set of classes that can perform metric collection
`Stopwatch` => a metric class responsible for tracking time delta

# Install it!

Statman is availble from [pypi](https://pypi.org/project/statman/).

It can be manually installed by:
```
pip install statman
```

or by adding the following to your `requirements.txt`:
```
statman=*
```

# Use it

## Statman (Registry)

`Statman` offers a registery to make it easily to globally access metrics.  Perhaps you will create and register a stopwatch in the depths of your codebase to measure the time to write to a database, and then want to access that result in some other part of your application.

### Register
* `register(name, metric)` => manually register a new metric

### Get
* `get(name)` => get a metric by name

### Count
* `count()` => returns a count of the registered metrics.

### Reset
* `reset()` => clears all metrics from the registry.

### Specialized register / get
* `stopwatch(name)` => returns a stopwatch instance.  If there is a registered stopwatch with this name, return it.  If there is no registered stopwatch with this name, create a new instance, register it, and return it.

## Stopwatch

`Statman-Stopwatch` is for timing operations within your system.  Suppose that you are trying to track down where the system is slow.  Put a stopwatch around certain critical areas, time those operations, and compare.

### Constructor
* `Stopwatch(name=None, autostart=False, initial_delta=None)` => create an instance of a stopwatch.
  * If `autostart` set to true, the stopwatch will automatically start
  * If `initial_delta` is set to a value, and `read` of the stopwatch is incremented by this amount.  This can be helpful if you adding timings together.
 
### Start
* `start()` => starts the stopwatch, let the timing begin!

### Read
* `read(precision)` => reads the stopwatch to determine how much time has elapsed.  Returns the time elapsed in seconds.
  * If precision is provided, `read()` will round to the number of decimals places based on precision.
  * Note: `read` does NOT stop the stopwatch - if the stopwatch is runnning, it will continues to run.
* `time(precision)` => alias for `read()`

### Stop
* `stop()` => stops the stopwatch, and returns the time elapsed in seconds

### Reset
* `reset()` => restores the stopwatch back to init state and clears start and stop times

### Restart
* `restart()` => `reset`s the stopwatch, then `start`s it

## Examples

### Maually Register Metric
``` python
from statman import Statman
Statman.register('expensive-operation-timing',Stopwatch())

stopwatch = Statman.get('expensive-operation-timing')
```

### Stopwatch via Registry
``` python
from statman import Statman

Statman.stopwatch('stopwatch-name').start()
# do some expensive operation that you want to measure
Statman.stopwatch('stopwatch-name').read()

print(f'event took {Statman.stopwatch('stopwatch-name').read(precision=1)}s to execute')  # event took 1.0s to execute
```


### Stopwatch: Direct Usage (no registry)
``` python
from statman import Stopwatch
sw = Stopwatch()
sw.start()

# do some expensive operation that you want to measure

delta = sw.stop()
print(f'event took {sw.read(precision=1)}s to execute')  # event took 1.0s to execute
```
