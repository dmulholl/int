
Integer Conversion Utility
==========================

A tiny command line utility for converting integers between bases.

`int` accepts an integer in its [b]inary, [o]ctal, [d]ecimal, or he[x] form, then prints it out in all four bases:

    $ int 64

    hex: 40
    dec: 64
    oct: 100
    bin: 01000000

You can specify the base of the input using a single letter prefix. (Defaults to [d]ecimal if omitted.) `int` also accepts multiple arguments:

    $ int b1001 o777 d256 x1EA


Installation
------------

Install directly from the Python Package Index using `pip`:

    $ pip install int


Requirements
------------

Requires Python 2.7 or 3+.


License
-------

This work has been placed in the public domain.
