<!-- mplement a function that receives two IPv4 addresses, 
 and returns the number of addresses between them 
 (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. 
The last address will always be greater than the first one.

Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246 -->

<?php

function ips_between($start, $end)
{
    $s_arr = array_reverse(array_map('intval', explode(".", $start)));
    $e_arr = array_reverse(array_map('intval', explode(".", $end)));
    $result = 0;
    for ($i = 0; $i < 4; $i++) {
        $e_arr[$i] -= $s_arr[$i];
        if ($e_arr[$i] < 0) {
            $e_arr[$i + 1] -= 1;
            $e_arr[$i] += 256;
        }
        $result += pow(256, $i) * $e_arr[$i];
    }
    return $result;
}
