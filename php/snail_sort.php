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
        var_dump($array[$i][$j]);
        echo '<br>';
        if (($j >= $i && ($j != $x - 1 ))) {
            $j++;
        } elseif ($i < $j && $i != $y - 1) {
            $i++;
        } elseif ($j <= $i && $j > 0) {
            $j--;
        } elseif ($i > $j + 1) {
            $i--;
        }
    }

    // for ($k = 0; $k < $limit; $k++) {
    //     if ($i < $y && $j < $x) {
    //         $snail[] = $array[$i][$j];
    //         var_dump($array[$i][$j]);
    //         echo '<br>';
    //         // echo 'First IF<br/>';
    //         if ($j >= $i && $j != $x) {
    //             $j++;
    //         } elseif ( $j >= $i && $i != $y){
    //             $i++;
    //         }
    //     } else {
    //         $i = 0;
    //         // $j = 0;
    //         // echo 'First ELSE<br/>';
    //     }
    // }

    return $snail;
}
