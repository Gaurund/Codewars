<!-- Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

uniqueInOrder("AAAABBBCCDAABBB") == {'A', 'B', 'C', 'D', 'A', 'B'}
uniqueInOrder("ABBCcAD")         == {'A', 'B', 'C', 'c', 'A', 'D'}
uniqueInOrder([1,2,2,3,3])       == {1,2,3} -->

<?php

function uniqueInOrder($iterable)
{
    if ($iterable == '') return array();
    if (is_string($iterable)){
        $iterable = str_split($iterable);
    }
    $ret = array($iterable[0]);
    for ($i = 0; $i < count($iterable) - 1; $i++) {
        if ($iterable[$i] != $iterable[$i + 1]){
            $ret[] = $iterable[$i + 1];
        }
    }
    return $ret;
}
