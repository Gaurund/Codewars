"""
Examples:
findNb(1071225) --> 45

findNb(91716553919377) --> -1
"""

import unittest

class FindNTestCase(unittest.TestCase):
    def test_find_nb(self):
        self.assertEqual(find_nb(4), -1)
        self.assertEqual(find_nb(16), -1)
        self.assertEqual(find_nb(4183059834009), 2022)
        self.assertEqual(find_nb(24723578342962), -1)
        self.assertEqual(find_nb(135440716410000), 4824)
        self.assertEqual(find_nb(40539911473216), 3568)
        self.assertEqual(find_nb(26825883955641), 3218)

def find_nb(m):
    n = 1
    v = 1
    while v <= m:
        if v == m:
            return n
        n += 1
        v += n**3
    return -1

unittest.main()