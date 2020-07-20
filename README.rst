[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Levenshtein Distance
--------

To use this package you can installing as follow
::
    pip install git+https://github.com/dqsamayoa/pyLevenshteinDistance

Y en python se ejecuta lo siguiente:
::
    >>> import levenshtein
    >>> metric = levenshtein.Levenshtein('abcd', '!?')
    >>> metric.distance('levenshtein', 'levensthain')

Requirements
--------

The libraries need for this are:

- json
- cython 

Cythons is only for compile purposes.