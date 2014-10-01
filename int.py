#!/usr/bin/env python3
"""
Command line utility for converting integers between bases.

Accepts an integer in [b]inary, [o]ctal, [d]ecimal, or he[x] base. 
Prints it in all four bases. A single letter prefix declares the base 
of the input. (Defaults to decimal if no prefix is present.)

Accepts multiple arguments.

Example:

    $ int x10
    
    bin: 10000
    oct: 20
    dec: 16
    hex: 10

License: This work has been placed in the public domain.

"""

__version__ = '0.1.0'


import os, sys


help_text = """usage: %s INT [INT ...]

Print an integer in its [b]inary, [o]ctal, [d]ecimal, and he[x] bases.

Use a single letter prefix to declare the base of the input, e.g. b1010. 
The base defaults to decimal if no prefix is supplied. Multiple arguments 
are accepted.""" % os.path.basename(__file__)


template = """
bin: {0:b}
oct: {0:o}
dec: {0:d}
hex: {0:X}\
"""


bases = {
    'b': (2, 'a binary'),
    'o': (8, 'an octal'),
    'd': (10, 'a decimal'),
    'x': (16, 'a hexadecimal'),
}


def print_ints(args):
    for argstr in args:
        prefix = argstr[0].lower()
        if prefix in bases:
            intstr = argstr[1:]
            base, adj = bases[prefix]
        else:
            intstr = argstr
            base, adj = bases['d']
        try:
            print(template.format(int(intstr, base)))
        except ValueError:
            print("\nerror: [%s] cannot be parsed as %s integer" % (intstr, adj))


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] in ('-h', '--help'):
        print(help_text)
    else:
        print_ints(sys.argv[1:])

