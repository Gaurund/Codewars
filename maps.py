"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
"""

import unittest

class MapsTest(unittest.TestCase):
    def test_maps(self):
        self.assertEqual(maps([1, 2, 3]), [2, 4, 6])
        self.assertEqual(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
        self.assertEqual(maps([]), [])

def maps(a):
    return [e*2 for e in a]

unittest.main()