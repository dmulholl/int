# --------------------------------------------------------------------------
# Unit tests for the int module.
# --------------------------------------------------------------------------

import textwrap
import int


# --------------------------------------------------------------------------
# Helper functions.
# --------------------------------------------------------------------------


def parse(s):
    return int.parse_arg(s).strip()


def prep(s):
    return textwrap.dedent(s).strip()


# --------------------------------------------------------------------------
# Unprefixed (decimal) input tests.
# --------------------------------------------------------------------------


def test_0():
    assert parse('0') == prep('''
        hex: 0
        dec: 0
        oct: 0
        bin: 00000000
    ''')


def test_00():
    assert parse('00') == prep('''
        hex: 0
        dec: 0
        oct: 0
        bin: 00000000
    ''')


def test_1():
    assert parse('1') == prep('''
        hex: 1
        dec: 1
        oct: 1
        bin: 00000001
    ''')


def test_2():
    assert parse('2') == prep('''
        hex: 2
        dec: 2
        oct: 2
        bin: 00000010
    ''')


def test_64():
    assert parse('64') == prep('''
        hex: 40
        dec: 64
        oct: 100
        bin: 01000000
    ''')


def test_128():
    assert parse('128') == prep('''
        hex: 80
        dec: 128
        oct: 200
        bin: 10000000
    ''')


def test_256():
    assert parse('256') == prep('''
        hex: 100
        dec: 256
        oct: 400
        bin: 00000001 00000000
    ''')


def test_512():
    assert parse('512') == prep('''
        hex: 200
        dec: 512
        oct: 1000
        bin: 00000010 00000000
    ''')


def test_1024():
    assert parse('1024') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 00000100 00000000
    ''')


# --------------------------------------------------------------------------
# Hex input tests.
# --------------------------------------------------------------------------


def test_hex_1024():
    assert parse('x400') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 00000100 00000000
    ''')


def test_zeroed_hex_1024():
    assert parse('0x400') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 00000100 00000000
    ''')


# --------------------------------------------------------------------------
# Decimal input tests.
# --------------------------------------------------------------------------


def test_decimal_1024():
    assert parse('d1024') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 00000100 00000000
    ''')


def test_zeroed_decimal_1024():
    assert parse('0d1024') == prep('''
            hex: 400
            dec: 1,024
            oct: 2000
            bin: 00000100 00000000
        ''')


# --------------------------------------------------------------------------
# Octal input tests.
# --------------------------------------------------------------------------


def test_octal_1024():
    assert parse('o2000') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 00000100 00000000
    ''')


def test_zeroed_octal_1024():
    assert parse('0o2000') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 00000100 00000000
    ''')


# --------------------------------------------------------------------------
# Binary input tests.
# --------------------------------------------------------------------------


def test_binary_1024():
    assert parse('b10000000000') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 00000100 00000000
    ''')


def test_zeroed_binary_1024():
    assert parse('0b10000000000') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 00000100 00000000
    ''')


# --------------------------------------------------------------------------
# Invalid input tests.
# --------------------------------------------------------------------------


def test_unprefixed_error():
    assert parse('foo') == prep(
        '''Error: "foo" cannot be parsed as a decimal integer.'''
    )


def test_prefixed_error():
    assert parse('boo') == prep(
        '''Error: "oo" cannot be parsed as a binary integer.'''
    )


# --------------------------------------------------------------------------
# Big integer tests.
# --------------------------------------------------------------------------


def test_big_int():
    assert parse('36893488147419103233') == prep('''
        hex: 20000000000000001
        dec: 36,893,488,147,419,103,233
        oct: 4000000000000000000001
        bin: 00000010 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000001
    ''') # 2**65 + 1
