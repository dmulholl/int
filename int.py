#!/usr/bin/env python3
# ------------------------------------------------------------------------------
# Integer conversion utility.
# ------------------------------------------------------------------------------

import os
import sys
import shutil
import math


__version__ = '3.1.0'


help_text = """
Usage: %s [FLAGS] INT [INT ...]

  Integer conversion utility. Accepts input in [b]inary, [o]ctal, [d]ecimal,
  or he[x]adecimal base, then prints the integer out in all four bases.

  Use a single letter prefix to declare the base of the input, e.g. b1010.
  The base defaults to decimal if the prefix is omitted.

  This utility:

  - Accepts integer literals with a leading zero, e.g. 0x123.
  - Accepts multiple arguments.
  - Displays the two's complement for negative integers.

Flags:
  -h, --help        Print this help text.
  -v, --version     Print the application's version number.

""".strip() % os.path.basename(sys.argv[0])


pos_template = """\
 hex: {0:X}
 dec: {0:,d}
 oct: {0:o}
 bin: {1}"""


neg_template = """\
 hex: [{0}b] {1:X}
 dec: [{0}b] {1:,d}
 oct: [{0}b] {1:o}
 bin: [{0}b] {2}"""


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


# Convert a positive integer into a string of binary octets.
def binary_string(value):
    binstring = '' if value else '0000_0000'
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

    if value >= 0:
        return pos_template.format(value, binary_string(value))
    else:
        num_bits = math.ceil(math.log2(-value) + 1)
        for size in (8, 16, 32, 64):
            if num_bits <= size:
                num_bits = size
                break
        tc_value = 2**num_bits + value
        return neg_template.format(num_bits, tc_value, binary_string(tc_value))


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
