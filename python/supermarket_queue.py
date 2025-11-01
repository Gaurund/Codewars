"""There is a queue for the self-checkout tills at the supermarket.
 Your task is write a function to calculate the total time required
 for all the customers to check out!

input
customers: an array of positive integers representing the queue.
Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required."""


def queue_time(customers, n):
    if len(customers) == 0:
        return 0
    tills = customers[:n:]
    for c in customers[n::]:
        index = tills.index(min(tills))
        tills[index] += c
    return max(tills)

import codewars_test as test


@test.describe("The Supermarket Queue")
def the_supermarket_queue():

    @test.it("Examples")
    def examples():
        test.assert_equals(
            queue_time([], 1), 0, "wrong answer for case with an empty queue"
        )
        test.assert_equals(
            queue_time([5], 1), 5, "wrong answer for a single person in the queue"
        )
        test.assert_equals(
            queue_time([2], 5), 2, "wrong answer for a single person in the queue"
        )
        test.assert_equals(
            queue_time([1, 2, 3, 4, 5], 1), 15, "wrong answer for a single till"
        )
        test.assert_equals(
            queue_time([1, 2, 3, 4, 5], 100),
            5,
            "wrong answer for a case with a large number of tills",
        )
        test.assert_equals(
            queue_time([2, 2, 3, 3, 4, 4], 2),
            9,
            "wrong answer for a case with two tills",
        )
        test.assert_equals(
            queue_time(
                [11, 27, 8, 28, 47, 39, 33, 35, 23, 11, 4, 12, 41, 30, 39, 35], 3
            ),
            158,
            "wrong answer for a case with two tills",
        )
        test.assert_equals(
            queue_time([15, 5, 13, 50, 21, 3, 3, 32, 27, 4, 29, 48, 30, 29], 4),
            93,
            "wrong answer for a case with two tills",
        )


# add your own test cases here

