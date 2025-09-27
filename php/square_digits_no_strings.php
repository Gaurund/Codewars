<?php

function square_digits(int $num): int
{
  $result = 0;
  $length = 0;
  while ($num > 0) {
    $digit = $num % 10;
    $num = ($num - $digit) / 10;
    $result += $digit * $digit * 10 ** $length;
    $length++;
    if ($digit > 3) {
      $length++;
    }
  }

  return $result;
}
