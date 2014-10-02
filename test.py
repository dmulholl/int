#!/usr/bin/env python

""" Unit tests for the int module. """


import unittest
import textwrap
import int


def parse(s):
    return int.parse_arg(s).strip()


def prep(s):
    return textwrap.dedent(s).strip()


class IntegerConversionTests(unittest.TestCase):

    def test_0(self):
        self.assertEqual(
            parse('0'),
            prep('''
                hex: 0
                dec: 0
                oct: 0
                bin: 00000000
            ''')
        )

    def test_1(self):
        self.assertEqual(
            parse('1'),
            prep('''
                hex: 1
                dec: 1
                oct: 1
                bin: 00000001
            ''')
        )

    def test_2(self):
        self.assertEqual(
            parse('2'),
            prep('''
                hex: 2
                dec: 2
                oct: 2
                bin: 00000010
            ''')
        )

    def test_64(self):
        self.assertEqual(
            parse('64'),
            prep('''
                hex: 40
                dec: 64
                oct: 100
                bin: 01000000
            ''')
        )

    def test_128(self):
        self.assertEqual(
            parse('128'),
            prep('''
                hex: 80
                dec: 128
                oct: 200
                bin: 10000000
            ''')
        )

    def test_256(self):
        self.assertEqual(
            parse('256'),
            prep('''
                hex: 100
                dec: 256
                oct: 400
                bin: 00000001 00000000
            ''')
        )

    def test_512(self):
        self.assertEqual(
            parse('512'),
            prep('''
                hex: 200
                dec: 512
                oct: 1000
                bin: 00000010 00000000
            ''')
        )

    def test_1024(self):
        self.assertEqual(
            parse('1024'),
            prep('''
                hex: 400
                dec: 1,024
                oct: 2000
                bin: 00000100 00000000
            ''')
        )

    def test_hex_1024(self):
        self.assertEqual(
            parse('x400'),
            prep('''
                hex: 400
                dec: 1,024
                oct: 2000
                bin: 00000100 00000000
            ''')
        )

    def test_decimal_1024(self):
        self.assertEqual(
            parse('d1024'),
            prep('''
                hex: 400
                dec: 1,024
                oct: 2000
                bin: 00000100 00000000
            ''')
        )

    def test_octal_1024(self):
        self.assertEqual(
            parse('o2000'),
            prep('''
                hex: 400
                dec: 1,024
                oct: 2000
                bin: 00000100 00000000
            ''')
        )

    def test_binary_1024(self):
        self.assertEqual(
            parse('b10000000000'),
            prep('''
                hex: 400
                dec: 1,024
                oct: 2000
                bin: 00000100 00000000
            ''')
        )

    def test_unprefixed_error(self):
        self.assertEqual(
            parse('foo'),
            prep('''error: "foo" cannot be parsed as a decimal integer''')
        )

    def test_prefixed_error(self):
        self.assertEqual(
            parse('boo'),
            prep('''error: "oo" cannot be parsed as a binary integer''')
        )


if __name__ == '__main__':
    unittest.main()
