#!/usr/bin/env python3
# ------------------------------------------------------------------------------
# Integer conversion utility.
# ------------------------------------------------------------------------------

import os
import sys
import shutil
import math


__version__ = '3.0.0'


help_text = """
Usage: %s [FLAGS] INT [INT ...]

  Integer conversion utility. Prints an integer in [b]inary, [o]ctal,
  [d]ecimal, and he[x]adecimal bases.

  Use a single letter prefix to declare the base of the input, e.g. b1010.
  The base defaults to decimal if the prefix is omitted.

  This utility:

  - Accepts integer literals with a leading zero, e.g. 0x123.
  - Accepts multiple arguments.
  - Prints negative binary integers in two's complement.

Flags:
  -h, --help        Print this help text.
  -v, --version     Print the application's version number.

""".strip() % os.path.basename(sys.argv[0])


# Output template.
template = """\
 hex: {0:X}
 dec: {0:,d}
 oct: {0:o}
 bin: {1}"""


# Map single-letter prefixes to bases and adjectives.
bases = {
    'b': (2, 'a binary'),
    'o': (8, 'an octal'),
    'd': (10, 'a decimal'),
    'x': (16, 'a hexadecimal'),
    'h': (16, 'a hexadecimal'),
}


# Print a line of dashes.
def printline():
    cols, _ = shutil.get_terminal_size()
    print('\u001B[90m' + '─' * cols + '\u001B[0m')


# Convert an integer into a string of binary octets.
def binary_string(value):
    if value == 0:
        return '0000_0000'
    elif value < 0:
        bits = math.log2(-value) + 1
        if bits > 64:
            return '<unsupported>'
        elif bits > 32:
            bits = 64
        elif bits > 16:
            bits = 32
        elif bits > 8:
            bits = 16
        else:
            bits = 8
        value = 2**bits + value

    binstring = ''
    while value:
        for i in range(8):
            binstring = '1' + binstring if value & 1 else '0' + binstring
            value >>= 1
            if i == 3: binstring = '_' + binstring
            if i == 7: binstring = ' ' + binstring
    return binstring.strip()


# Process a single string argument.
def parse_arg(arg):
    arg = arg.lstrip('0') or '0'
    prefixchar = arg[0].lower()

    if prefixchar in bases:
        digits = arg[1:]
        base, adj = bases[prefixchar]
    else:
        digits = arg
        base, adj = bases['d']

    try:
        value = int(digits, base)
    except ValueError:
        return f'Error: "{digits}" cannot be parsed as {adj} integer.'

    return template.format(value, binary_string(value))


def main():
    if len(sys.argv) == 1 or '--help' in sys.argv or '-h' in sys.argv:
        print(help_text)
        sys.exit()

    if '--version' in sys.argv or '-v' in sys.argv:
        print(__version__)
        sys.exit()

    printline()
    for arg in sys.argv[1:]:
        print(parse_arg(arg))
        printline()


if __name__ == '__main__':
    main()
