"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""


def triangle(n):
    for i in range(1, n):
        for j in range(i * (i - 1) + 1, i * i + i, 2):
            print(j, end=" ")
        print()


def row_sum_odd_numbers(n):
    return pow(n,3)
