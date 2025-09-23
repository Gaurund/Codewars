"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing
the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
"""

import unittest


class TestLikes(unittest.TestCase):
    def test_likes(self):
        self.assertEqual(likes([]), "no one likes this")
        self.assertEqual(likes(["Peter"]), "Peter likes this")
        self.assertEqual(likes(["Jacob", "Alex"]), "Jacob and Alex like this")
        self.assertEqual(likes(["Max", "John", "Mark"]), "Max, John and Mark like this")
        self.assertEqual(
            likes(["Alex", "Jacob", "Mark", "Max"]),
            "Alex, Jacob and 2 others like this",
        )


def likes(names):
    i = len(names)
    return {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this",
    }[min(i, 4)].format(*names[:3:], others=i - 2)


unittest.main()
