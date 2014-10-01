#!/usr/bin/env python3
"""
Command line utility for converting integers between bases.

Accepts an integer in [b]inary, [o]ctal, [d]ecimal, or he[x] base. 
Prints it in all four bases. A single letter prefix declares the base 
of the input. (Defaults to decimal if no prefix is present.)

Accepts multiple arguments.

Example:

    $ int x10
    
    hex: 10
    dec: 16
    oct: 20
    bin: 00010000

License: This work has been placed in the public domain.

"""

__version__ = '0.2.0'


import os, sys


help_text = """usage: %s INT [INT ...]

Prints an integer in its [b]inary, [o]ctal, [d]ecimal, and he[x] bases.

Use a single letter prefix to declare the base of the input, e.g. b1010. 
The base defaults to decimal if no prefix is supplied. Multiple arguments 
are accepted.""" % os.path.basename(__file__)


template = """
hex: {0:X}
dec: {0:,d}
oct: {0:o}
bin: \
"""


bases = {
    'b': (2, 'a binary'),
    'o': (8, 'an octal'),
    'd': (10, 'a decimal'),
    'x': (16, 'a hexadecimal'),
    'h': (16, 'a hexadecimal'),
}


def binary_string(i):
    s = ''
    while i:
        for digit in range(8):
            if i & 1 == 1:
                s = '1' + s
            else:
                s = '0' + s
            i >>= 1
        s = ' ' + s
    return s.lstrip()


def print_ints(args):
    for argstr in args:
        prefix = argstr[0].lower()
        if prefix in bases:
            inp_str = argstr[1:]
            base, adj = bases[prefix]
        else:
            inp_str = argstr
            base, adj = bases['d']
        try:
            inp_int = int(inp_str, base)
        except ValueError:
            sys.exit(
                '\nerror: "%s" cannot be parsed as %s integer' % (inp_str, adj)
            )
        print(template.format(inp_int) + binary_string(inp_int))


def main():
    if len(sys.argv) == 1:
        print(help_text)
    elif '-h' in sys.argv or '--help' in sys.argv:
        print(help_text)
    else:
        print_ints(sys.argv[1:])


if __name__ == '__main__':
    main()
