#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test for max_integer"""

    def text_max(self):
        """Tests for valid integers"""
        self.assertEqual(max_integer([2, 4, 1, 9]), 9)

    def text_max(self):
        """Tests for valid integers"""
        self.assertEqual(max_integer([9, 1, 4, 2]), 9)

    def text_max(self):
        """Tests for valid integers"""
        self.assertEqual(max_integer([-2, -4, -1, -9]), -1)

    def text_max(self):
        """Tests for valid integers"""
        self.assertEqual(max_integer([25]), 25)

    def text_max(self):
        """Tests for valid integers"""
        self.assertEqual(max_integer([2, 4, -9, 1]), 4)

    def text_max(self):
        """Tests for valid integers"""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
