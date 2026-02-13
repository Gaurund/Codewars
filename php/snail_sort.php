<!-- Given an n x n array, return the array elements arranged 
 from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers 
of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9] -->

<?php

function snail(array $array): array
{
    $i = $j = 0;
    $snail = [];
    $y = count($array);
    $x = count($array[0]);
    $limit = $y * $x;

    for ($k = 0; $k < $limit; $k++) {
        $snail[] = $array[$i][$j];
        if ($i <= $j + 1 && $i + $j < $x - 1) {
            $j++;
        } elseif ($i < $j && $i + $j >= $y - 1) {
            $i++;
        } elseif ($i >= $j && $i + $j > $x - 1) {
            $j--;
        } else {
            $i--;
        }
    }

    return $snail;
}
