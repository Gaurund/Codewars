"""
The number
89
89 is the first integer with more than one digit that fulfills
the property partially introduced in the title of this kata.
What's the use of saying "Eureka"? Because this sum gives the same number:

Task
We need a function to collect these numbers, that may receive two integers a, b that defines the range
[a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Examples
Let's see some cases (input -> output):

1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range
[a,b] the function should output an empty list.

90, 100 --> []
Enjoy it!!
"""


def int_to_list(n: int) -> list:
    res_list = []
    while n > 0:
        res_list.insert(0, n % 10)
        n = n // 10
    return res_list


def sum_pow(lst: list) -> int:
    res_sum = 0
    for i, num in enumerate(lst, start=1):
        res_sum = res_sum + pow(num, i)
    return res_sum


def sum_dig_pow(a: int, b: int) -> list:
    result = []
    for num in range(a, b + 1):
        summ = sum_pow(int_to_list(num)) # One could use a casting to string type here, but I wanted do it only with numbers
        if num == summ:
            result.append(num)
    return result


import codewars_test as test


@test.describe(
    "Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!"
)
def desc1():
    @test.it("Sample tests")
    def it1():
        test.assert_equals(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.assert_equals(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
        test.assert_equals(sum_dig_pow(10, 89), [89])
        test.assert_equals(sum_dig_pow(10, 100), [89])
        test.assert_equals(sum_dig_pow(90, 100), [])
        test.assert_equals(sum_dig_pow(89, 135), [89, 135])
