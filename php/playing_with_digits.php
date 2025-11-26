<?php

function digPow($n, $p)
{
    $s = 0;
    foreach (str_split($n) as $digit) {
        $s += pow($digit, $p++);
    }
    if ($s % $n == 0) {
        return $s / $n;
    }
    return ($s % $n == 0) ? ($s / $n) : -1;
}


echo digPow(46288, 3); // 51