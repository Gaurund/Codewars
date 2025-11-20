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
    if (empty($a1) || empty($a2)) {
        return -1;
    }
    $a1 = array_map("strlen", $a1);
    $a2 = array_map("strlen", $a2);
    return max((max($a1) - min($a2)), max($a2) - min($a1));
}

$s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"];
$s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"];

echo mxdiflg($s1, $s2);
