<!-- Create a parser to interpret and execute the Deadfish language.

Deadfish operates on a single value in memory, which is initially set to 0.

It uses four single-character commands:

i: Increment the value
d: Decrement the value
s: Square the value
o: Output the value to a result array
All other instructions are no-ops and have no effect.

Examples
Program "iiisdoso" should return numbers [8, 64].
Program "iiisdosodddddiso" should return numbers [8, 64, 3600]. -->

<?php

function parse($data)
{
    $arr = array();
    $num = 0;

  for ($i = 0; $i < strlen($data); $i++) {
    if ($data[$i] == "i") {
      $num += 1;
    } elseif ($data[$i] == "d") {
      $num -= 1;
    } elseif ($data[$i] == "s") {
      $num *= $num;
    } elseif ($data[$i] == "o") {
      array_push($arr, $num);
    }
  }
  return $arr;
}
