#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer([..])."""

    def test_ol(self):
        """Test ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unol(self):
        """Test unordered list of integers."""
        unordered = [2, 1, 6, 19]
        self.assertEqual(max_integer(unordered), 19)

    def test_eml(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_oel(self):
        """Test single element list."""
        one_element = [11]
        self.assertEqual(max_integer(one_element), 11)

    def test_fl(self):
        """Test a list of floats."""
        floats = [0.237, 109.2, -99.4, 78.3, 9.1211]
        self.assertEqual(max_integer(floats), 109.2)

    def test_inf(self):
        """Test a list of combos."""
        ints_and_floats = [1.34, -89, 11.78, 8.53, 0, 111]
        self.assertEqual(max_integer(ints_and_floats), 111)

    def test_sr(self):
        """Test string."""
        string = "Xyler"
        self.assertEqual(max_integer(string), 'y')

    def test_lsr(self):
        """Test list of strings."""
        strings = ["ab", "cd", "ef"]
        self.assertEqual(max_integer(strings), "ef")

    def test_emsr(self):
        """Test empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
