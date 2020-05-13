# ------------------------------------------------------------------------------
# Unit tests for the int module. Run with pytest.
# ------------------------------------------------------------------------------

import textwrap
import int


# ------------------------------------------------------------------------------
# Helper functions.
# ------------------------------------------------------------------------------


def parse(s):
    out = int.parse_arg(s)
    out = textwrap.dedent(out).strip().replace('\u001B[90m \u001B[0m', ' ')
    return out


def prep(s):
    return textwrap.dedent(s).strip()


# ------------------------------------------------------------------------------
# Unprefixed (decimal) input tests.
# ------------------------------------------------------------------------------


def test_0():
    assert parse('0') == prep('''
        hex: 0
        dec: 0
        oct: 0
        bin: 0000_0000
    ''')


def test_00():
    assert parse('00') == prep('''
        hex: 0
        dec: 0
        oct: 0
        bin: 0000_0000
    ''')


def test_1():
    assert parse('1') == prep('''
        hex: 1
        dec: 1
        oct: 1
        bin: 0000_0001
    ''')


def test_2():
    assert parse('2') == prep('''
        hex: 2
        dec: 2
        oct: 2
        bin: 0000_0010
    ''')


def test_64():
    assert parse('64') == prep('''
        hex: 40
        dec: 64
        oct: 100
        bin: 0100_0000
    ''')


def test_128():
    assert parse('128') == prep('''
        hex: 80
        dec: 128
        oct: 200
        bin: 1000_0000
    ''')


def test_256():
    assert parse('256') == prep('''
        hex: 100
        dec: 256
        oct: 400
        bin: 0000_0001 0000_0000
    ''')


def test_512():
    assert parse('512') == prep('''
        hex: 200
        dec: 512
        oct: 1000
        bin: 0000_0010 0000_0000
    ''')


def test_1024():
    assert parse('1024') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 0000_0100 0000_0000
    ''')


# ------------------------------------------------------------------------------
# Hex input tests.
# ------------------------------------------------------------------------------


def test_hex_1024():
    assert parse('x400') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 0000_0100 0000_0000
    ''')


def test_zeroed_hex_1024():
    assert parse('0x400') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 0000_0100 0000_0000
    ''')


# ------------------------------------------------------------------------------
# Decimal input tests.
# ------------------------------------------------------------------------------


def test_decimal_1024():
    assert parse('d1024') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 0000_0100 0000_0000
    ''')


def test_zeroed_decimal_1024():
    assert parse('0d1024') == prep('''
            hex: 400
            dec: 1,024
            oct: 2000
            bin: 0000_0100 0000_0000
        ''')


# ------------------------------------------------------------------------------
# Octal input tests.
# ------------------------------------------------------------------------------


def test_octal_1024():
    assert parse('o2000') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 0000_0100 0000_0000
    ''')


def test_zeroed_octal_1024():
    assert parse('0o2000') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 0000_0100 0000_0000
    ''')


# ------------------------------------------------------------------------------
# Binary input tests.
# ------------------------------------------------------------------------------


def test_binary_1024():
    assert parse('b10000000000') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 0000_0100 0000_0000
    ''')


def test_zeroed_binary_1024():
    assert parse('0b10000000000') == prep('''
        hex: 400
        dec: 1,024
        oct: 2000
        bin: 0000_0100 0000_0000
    ''')


# ------------------------------------------------------------------------------
# Invalid input tests.
# ------------------------------------------------------------------------------


def test_unprefixed_error():
    assert parse('foo') == prep(
        '''Error: "foo" cannot be parsed as a decimal integer.'''
    )


def test_prefixed_error():
    assert parse('boo') == prep(
        '''Error: "oo" cannot be parsed as a binary integer.'''
    )


# ------------------------------------------------------------------------------
# Big integer tests.
# ------------------------------------------------------------------------------


def test_big_int():
    assert parse('36893488147419103233') == prep('''
        hex: 20000000000000001
        dec: 36,893,488,147,419,103,233
        oct: 4000000000000000000001
        bin: 0000_0010 0000_0000 0000_0000 0000_0000 0000_0000 0000_0000 0000_0000 0000_0000 0000_0001
    ''') # 2**65 + 1


# ------------------------------------------------------------------------------
# Negative input tests.
# ------------------------------------------------------------------------------


def test_neg_1():
    assert parse('-1') == prep('''
        hex: [8b] FF
        dec: [8b] 255
        oct: [8b] 377
        bin: [8b] 1111_1111
    ''')


def test_neg_2():
    assert parse('-2') == prep('''
        hex: [8b] FE
        dec: [8b] 254
        oct: [8b] 376
        bin: [8b] 1111_1110
    ''')


def test_neg_128():
    assert parse('-128') == prep('''
        hex: [8b] 80
        dec: [8b] 128
        oct: [8b] 200
        bin: [8b] 1000_0000
    ''')


def test_neg_129():
    assert parse('-129') == prep('''
        hex: [16b] FF7F
        dec: [16b] 65,407
        oct: [16b] 177577
        bin: [16b] 1111_1111 0111_1111
    ''')
