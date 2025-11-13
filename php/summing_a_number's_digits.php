<!-- Write a function which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

For example: (Input -> Output)

10 => 1
99 => 18
-32 => 5
Let's assume that all numbers in the input will be integer values. -->

<?php

function sumDigits(int $number): int{
  $res = 0;
  $number = abs($number);
  while ($number > 0 ){
    $res += $number % 10;
    $number = (int)($number / 10);
  }
  return $res;
}