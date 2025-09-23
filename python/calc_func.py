"""
This time we want to write calculations using functions and get the results.
Let's have a look at some examples:

seven(times(five()))    #  must return 35
four(plus(nine()))      #  must return 13
eight(minus(three()))   #  must return 5
six(divided_by(two()))  #  must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")

There must be a function for each of the following mathematical
operations: plus, minus, times, divided_by

Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand,
the most inner function represents the right operand

Division should be integer division. For example,
this should return 2, not 2.666666...:

eight(divided_by(three()))
"""


def default(a):
    return a


def zero(func=default):
    return func(0)


def one(func=default):
    return func(1)


def two(func=default):
    return func(2)


def three(func=default):
    return func(3)


def four(func=default):
    return func(4)


def five(func=default):
    return func(5)


def six(func=default):
    return func(6)


def seven(func=default):
    return func(7)


def eight(func=default):
    return func(8)


def nine(func=default):
    return func(9)


def plus(n):
    return lambda a: a + n


def minus(n):
    return lambda a: a - n


def times(n):
    return lambda a: a * n


def divided_by(n):
    return lambda a: a // n


# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it("Basic Test Cases")
#     def basic_test_cases():
#         test.assert_equals(seven(times(five())), 35)
#         test.assert_equals(four(plus(nine())), 13)
#         test.assert_equals(eight(minus(three())), 5)
#         test.assert_equals(six(divided_by(two())), 3)

print(seven(times(five())))
