NumeralRu - Convert numbers to russian words
============================================

``numeralru`` provides gender and case aware conversion of numbers
to russian words. E.g.: 1034 in feminine gender and genitive case 
becomes: "одной тысячи тридцати четырёх".

Installation
------------

Download source from and install using::

    python setup.py install

Tests can be run with::

    python setup.py test

Usage
-----

    >>> from numeralru import numeralize, Gender, Case
    >>> numeralize(14, Gender.neuter, Case.instrumental)
    'четырнадцатью'
    >>> numeralize(123, Gender.feminine, Case.accusative, animate=True)
    'сто двадцать трёх'
    >>> numeralize(1337, long=False)
    'тысяча триста тридцать семь'

A detailed funciton documentation can be found by calling::

    >>> help(numeralize)

Acknowledgements
----------------

The package is a python implementation of JavaScript library
``numeralize-ru`` https://github.com/anotherpit/numeralize-ru

