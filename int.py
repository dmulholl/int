#!/usr/bin/env python
# --------------------------------------------------------------------------
# Integer conversion utility.
#
# This command line utility accepts an integer in its [b]inary, [o]ctal,
# [d]ecimal, or he[x] form, then prints it out in all four bases.
#
# Use a single letter prefix to declare the base of the input, e.g. b1010.
# (Defaults to [d]ecimal if the prefix is omitted.)
#
# Leading zeros are stripped so Python integer literals in their canonical
# form are accepted, e.g. 0x123.
#
# The user can supply multiple space-separated arguments at once.
#
# Example:
#
#     $ int x10
#     hex: 10
#     dec: 16
#     oct: 20
#     bin: 00010000
#
# Author: Darren Mulholland <dmulholland@outlook.ie>
# License: Public Domain
# --------------------------------------------------------------------------

import os
import sys
import shutil


# Application version number.
__version__ = '1.2.0'


# Command line help text.
help_text = """Usage: %s [FLAGS] INT [INT ...]

  Prints an integer in its [b]inary, [o]ctal, [d]ecimal, and he[x] bases.

  Use a single letter prefix to declare the base of the input, e.g. b1010.
  The base defaults to [d]ecimal if the prefix is omitted.

  - Accepts integer literals with a leading zero, e.g. 0x123.
  - Accepts multiple arguments.
  - Does not accept negative integers.

Flags:
  --help        Print this help text and exit.
  --version     Print the application's version number and exit.

""".strip() % os.path.basename(sys.argv[0])


# Output template.
template = """\
hex: {0:X}
dec: {0:,d}
oct: {0:o}
bin: {1}"""


# Maps single-letter prefixes to bases.
bases = {
    'b': (2, 'a binary'),
    'o': (8, 'an octal'),
    'd': (10, 'a decimal'),
    'x': (16, 'a hexadecimal'),
    'h': (16, 'a hexadecimal'),
}


# Prints to stdout, appending a newline.
def println(s=''):
    sys.stdout.write(s + '\n')


# Prints a line of dashes.
def printspacer():
    if sys.version_info < (3, 3):
        cols = 80
    else:
        cols, _ = shutil.get_terminal_size()
    println('-' * cols)


# Converts an integer into a string of binary octets.
def int_to_octets(i):
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


# Processes a single string argument.
def parse_arg(s):
    s = s.lstrip('0') or '0'
    prefix = s[0].lower()

    if prefix in bases:
        digits = s[1:]
        base, adj = bases[prefix]
    else:
        digits = s
        base, adj = bases['d']

    try:
        value = int(digits, base)
    except ValueError:
        return 'Error: "%s" cannot be parsed as %s integer.' % (digits, adj)

    if value < 0:
        return 'Error: negative integers are not supported.'
    else:
        return template.format(value, int_to_octets(value))


def main():
    if len(sys.argv) == 1 or '--help' in sys.argv:
        println(help_text)
        sys.exit()

    if '--version' in sys.argv:
        println(__version__)
        sys.exit()

    printspacer()

    for arg in sys.argv[1:]:
        println(parse_arg(arg))
        printspacer()


if __name__ == '__main__':
    main()
