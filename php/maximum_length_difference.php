<!-- You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

Example:
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) -> 13

Bash note:
input : 2 strings with substrings separated by ,
output: number as a string -->

<?php

function cmp($a, $b)
{
    if (strlen($a) == strlen($b)) {
        return 0;
    }
    return (strlen($a) < strlen($b)) ? -1 : 1;
}

function mxdiflg($a1, $a2)
{
    $size_of_a1 = count($a1);
    $size_of_a2 = count($a2);
    if ($size_of_a1 == 0 || $size_of_a2 == 0) {
        return -1;
    }
    usort($a1, "cmp");
    usort($a2, "cmp");

    $a1_first = $a1[0];
    $a2_first = $a2[0];
    $a1_last = $a1[$size_of_a1 - 1];
    $a2_last = $a2[$size_of_a2 - 1];

    $max = max((strlen($a1_last) - strlen($a2_first)), (strlen($a2_last) - strlen($a1_first)));
    return $max;
}

$s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"];
$s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"];

echo mxdiflg($s1, $s2);
