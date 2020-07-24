<img src="https://raw.githubusercontent.com/DQsamayoa/personal-webpage/master/imgs/logo_vs_b.png" alt="logo" align="right" height="200">

[![Build Status](https://travis-ci.org/DQsamayoa/pyLevenshteinDistance.svg?branch=master)](https://travis-ci.org/DQsamayoa/pyLevenshteinDistance)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

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
