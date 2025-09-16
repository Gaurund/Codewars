"""
Your function takes an integer (prod) and returns an array/tuple
(check the function signature/sample tests for the return type in your language):

if F(n) * F(n+1) = prod:
(F(n), F(n+1), true)
"""

import unittest


class FibTestCase(unittest.TestCase):
    def test_product_fib(self):
        self.assertEqual(product_fib(4895), [55, 89, True])
        self.assertEqual(product_fib(5895), [89, 144, False])


def product_fib(prod):
    f1, f2 = 0, 1
    while f1 * f2 < prod:
        f1, f2 = f2, f1 + f2
    return [f1, f2, f1 * f2 == prod]

unittest.main()
