<!-- Create a function that takes a positive integer 
 and returns the next bigger number that can be formed 
 by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1 -->

<?php

function number_to_array($n)
{
    $arr = array();
    while ($n > 0) {
        $arr[] = $n % 10;
        $n = intdiv($n, 10);
    }
    return $arr;
}

function array_to_number($arr)
{
    $n = 0;
    for ($i = 0; $i < count($arr); $i++) {
        $n += pow(10, $i) * $arr[$i];
    }
    return $n;
}

function nextBigger($n)
{
    $init_arr = number_to_array($n);
    $buff_arr = [$init_arr[0]];
    for ($i = 1; $i < count($init_arr); $i++) {
        $buff_arr[$i] = $init_arr[$i];
        if ($buff_arr[$i] < $buff_arr[$i - 1]) {
            $last = $buff_arr[$i];
            rsort($buff_arr);
            $needle_key = array_search($last, $buff_arr);
            $needle = array_splice($buff_arr, $needle_key - 1, 1);
            $buff_arr[] = $needle[0];
            array_splice($init_arr, 0, count($buff_arr), $buff_arr);
            $i = count($init_arr);
        }
    }
    $final_num = array_to_number($init_arr);

    return $n != $final_num ? $final_num : -1;
}
