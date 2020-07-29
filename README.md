<img src="https://raw.githubusercontent.com/DQsamayoa/personal-webpage/master/imgs/logo_vs_b.png" alt="logo" align="right" height="200">

[![Build Status](https://travis-ci.org/DQsamayoa/py-levenshtein-distance.svg?branch=master)](https://travis-ci.org/DQsamayoa/py-levenshtein-distance)
[![Coverage Status](https://coveralls.io/repos/github/DQsamayoa/py-levenshtein-distance/badge.svg?branch=master)](https://coveralls.io/github/DQsamayoa/py-levenshtein-distance?branch=master)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Levenshtein Distance
--------

To use this package you can installing as follow
```bash
pip install git+https://github.com/dqsamayoa/py-levenshtein-distance
```

In order to use the levenshteind distance you should do the next:

```python
>>> import levenshtein
>>> metric = levenshtein.Levenshtein('abcd', '!?')
>>> metric.distance('levenshtein', 'levensthain')
```

Requirements
--------
