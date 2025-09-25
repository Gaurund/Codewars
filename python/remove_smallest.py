"""
Task
Given an array of integers, remove the smallest value. 
Do not mutate the original array/list. 
If there are multiple elements with the same value, 
remove the one with the lowest index. 
If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]

"""

import unittest

class TestRemoveSmallest(unittest.TestCase):
    def test_remove_smallest(self):
        self.assertEqual(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
        self.assertEqual(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
        self.assertEqual(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
        self.assertEqual(remove_smallest([]), [], "Wrong result for []")

def remove_smallest(numbers: list):
    l =  list(numbers)
    if len(l) > 0:
        l.remove(min(numbers))
    return l

unittest.main()
