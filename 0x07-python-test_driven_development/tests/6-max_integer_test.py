#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([100, 10, 12]), 100)
        self.assertEqual(max_integer([10, 100, 12]), 100)
        self.assertEqual(max_integer([10, 12, 100]), 100)
        self.assertEqual(max_integer([-15, 100, 12]), 100)
        self.assertEqual(max_integer([-10, -5, -15]), -5)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([]), None)
