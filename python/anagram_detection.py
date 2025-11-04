"""
An anagram is the result of rearranging the letters of
a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments
given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"
"""


def is_anagram(test, original):
    return sorted(test.lower())==sorted(original.lower())


import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            is_anagram("foefet", "toffee"),
            True,
            "The word foefet is an anagram of toffee",
        )
        test.assert_equals(
            is_anagram("Buckethead", "DeathCubeK"),
            True,
            "The word Buckethead is an anagram of DeathCubeK",
        )
        test.assert_equals(
            is_anagram("Twoo", "WooT"), True, "The word Twoo is an anagram of WooT"
        )
        test.assert_equals(
            is_anagram("dumble", "bumble"),
            False,
            "Characters do not match for test case dumble, bumble",
        )
        test.assert_equals(
            is_anagram("ound", "round"),
            False,
            "Missing characters for test case ound, round",
        )
        test.assert_equals(
            is_anagram("apple", "pale"), False, "Same letters, but different count"
        )
