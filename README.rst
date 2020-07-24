|LOGO| |LICENSE|

Levenshtein Distance
--------

To use this package you can installing as follow
::
	pip install git+https://github.com/dqsamayoa/pyLevenshteinDistance


In order to use the levenshteind distance you should do the next:

.. code-block:: python

  >>> import levenshtein
  >>> metric = levenshtein.Levenshtein('abcd', '!?')
  >>> metric.distance('levenshtein', 'levensthain')


Requirements
--------

The libraries need for this are:

- json
- cython 

Cythons is only for compile purposes.




.. |LOGO| image:: https://raw.githubusercontent.com/DQsamayoa/personal-webpage/master/imgs/logo_vs_b.png
	:align: right
	:height: 200px
	:alt: logo

.. |LICENSE| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
	:target: https://opensource.org/licenses/Apache-2.0
	:alt: License Apache 2.0