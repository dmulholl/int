
# Int

Int is a handy command line utility for converting integers between bases.
It accepts an integer in its [b]inary, [o]ctal, [d]ecimal, or he[x] form,
then prints it out in all four bases.

Output:

    $ int 64 128
    ────────────────────────────────────────────────────────────────────────────────
    hex: 40
    dec: 64
    oct: 100
    bin: 01000000
    ────────────────────────────────────────────────────────────────────────────────
    hex: 80
    dec: 128
    oct: 200
    bin: 10000000
    ────────────────────────────────────────────────────────────────────────────────

Interface:

    $ int --help

    Usage: int [FLAGS] INT [INT ...]

      Integer conversion utility. Prints an integer in [b]inary, [o]ctal,
      [d]ecimal, and he[x] bases.

      Use a single letter prefix to declare the base of the input, e.g. b1010.
      The base defaults to [d]ecimal if the prefix is omitted.

      This utility:

      - Accepts integer literals with a leading zero, e.g. 0x123.
      - Accepts multiple arguments.
      - Does not accept negative integers.

    Flags:
      --help        Print this help text and exit.
      --version     Print the application's version number and exit.

Install:

    $ pip install int

Int requires Python 3.
