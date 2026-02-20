<!-- https://www.codewars.com/kata/550f22f4d758534c1100025a/train/php
 
Task
Write a function dirReduc which will take an array of strings 
and returns an array of strings with the needless 
directions removed (W<->E or S<->N side by side).

Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] 
is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" 
are not directly opposite of each other and can't become such. 
Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
-->

<?php

function dirReduc($arr) {
    for ($i = 0; $i < count($arr); $i++){
        if ($i < count($arr) -2 && (($arr[$i] = "NORTH" && $arr[$i+1]="SOUTH") || ($arr[$i] = "WEST" && $arr[$i+1])="EAST"))
    }

    return $arr
}