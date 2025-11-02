"""
In this simple exercise, you will write a function that takes two integers;
n and limit; and returns a list of the multiples of n up to and possibly including limit.

It is guaranteed that n > 0 and limit >= n.

For example, if the parameters passed are (2, 6),
the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.

Examples
n = 2; limit = 6 --> [2, 4, 6]
n = 2; limit = 5 --> [2, 4]
"""


def find_multiples(integer, limit):
    return [integer * i for i in range(1, limit // integer + 1)]


import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(find_multiples(5, 25), [5, 10, 15, 20, 25])
        test.assert_equals(find_multiples(1, 2), [1, 2])
