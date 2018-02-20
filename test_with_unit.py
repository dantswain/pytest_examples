'''
unittest example
'''

import unittest

# pylint: disable=missing-docstring

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        a_string = 'hello world'
        self.assertEqual(a_string.split(), ['hello', 'world'])
        # check that a_string.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            a_string.split(2)

if __name__ == '__main__':
    unittest.main()
