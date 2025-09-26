<?php

function square_digits(int $num): int
{
  $result = "";
  $string = strval($num);
  for ($i = 0; $i < strlen($string); $i++)
  {
    $digit = intval($string[$i]);
    $result .= $digit ** 2;
  }

  return intval($result);
}
