#!/usr/bin/env python
"""
Command line utility for converting integers between bases.

Accepts an integer in [b]inary, [o]ctal, [d]ecimal, or he[x] base. 
Prints it out in all four bases. A single letter prefix specifies the 
base of the input. (Defaults to [d]ecimal if omitted.)

Accepts multiple arguments.

Example:

    $ int x10
    
    hex: 10
    dec: 16
    oct: 20
    bin: 00010000

License: This work has been placed in the public domain.

"""

__version__ = '0.4.2'


import os, sys


help_text = """usage: %s INT [INT ...]

Prints an integer in its [b]inary, [o]ctal, [d]ecimal, and he[x] bases.

Use a single letter prefix to declare the base of the input, e.g. b1010. 
The base defaults to [d]ecimal if the prefix is omitted. 

Accepts multiple arguments.""" % os.path.basename(sys.argv[0])


template = """\
hex: {0:X}
dec: {0:,d}
oct: {0:o}
bin: {1}"""


bases = {
    'b': (2, 'a binary'),
    'o': (8, 'an octal'),
    'd': (10, 'a decimal'),
    'x': (16, 'a hexadecimal'),
    'h': (16, 'a hexadecimal'),
}


def println(s=''):
    sys.stdout.write(s + '\n')


def int_to_octet(i):
    s = '' if i else '00000000'
    while i:
        for digit in range(8):
            if i & 1 == 1:
                s = '1' + s
            else:
                s = '0' + s
            i >>= 1
        s = ' ' + s
    return s.lstrip()


def parse_arg(s):
    prefix = s[0].lower()
    if prefix in bases:
        int_str = s[1:]
        base, adj = bases[prefix]
    else:
        int_str = s
        base, adj = bases['d']
    try:
        int_val = int(int_str, base)
    except ValueError:
        return 'error: "%s" cannot be parsed as %s integer' % (int_str, adj)
    if int_val < 0:
        return 'error: negative integers are not supported'
    else:
        return template.format(int_val, int_to_octet(int_val))


def main():
    if len(sys.argv) == 1:
        println(help_text)
    elif '-h' in sys.argv or '--help' in sys.argv:
        println(help_text)
    else:
        println('\n\n'.join(parse_arg(arg) for arg in sys.argv[1:]))


if __name__ == '__main__':
    main()
