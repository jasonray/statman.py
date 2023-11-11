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

## Registry
* `register(name, metric)` => manually register a new metric
* `get(name)` => get a metric by name
* `count()` => returns a count of the registered metrics.
* `stopwatch(name)` => returns a stopwatch instance.  If there is a registered stopwatch with this name, return it.  If there is no registered stopwatch with this name, create a new instance, register it, and return it.
* `reset()` => clears all metrics from the registry.

## Stopwatch Example
### Direct Usage (no registry)
```
from statman import Stopwatch
sw = Stopwatch()
sw.start()

# do some expensive operation that you want to measure

delta = sw.stop()
print(f'event took {sw.read(precision=1)}s to execute')  # event took 1.0s to execute
```
