#!/usr/bin/python3
"""
a test file for the reverse string function
"""
import unittest
reverse_string = __import__('reverse_string').reverse_string

class TestReverseString(unittest.TestCase):

    def testReverse(self):
        self.assertEqual(reverse_string("Hello"), "olleH")
        self.assertEqual(reverse_string("H"), "H")
        self.assertEqual(reverse_string("123"), "321")
        self.assertEqual(reverse_string(""), "")

        with self.assertRaises(TypeError):
            reverse_string(123)
            reverse_string([])
            reverse_string(None)
            reverse_string(1.4)
            reverse_string([1.3, 2])


