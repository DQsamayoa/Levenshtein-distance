[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Levenshtein Distance
--------

To use this package you can installing as follow
```bash
pip install git+https://github.com/dqsamayoa/pyLevenshteinDistance
```

In order to use the levenshteind distance you should do the next:

```python
>>> import levenshtein
>>> metric = levenshtein.Levenshtein('abcd', '!?')
>>> metric.distance('levenshtein', 'levensthain')
```

Requirements
--------

The libraries need for this are:

- json
- cython 

Cythons is only for compile purposes.