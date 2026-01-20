<!-- A bookseller has lots of books classified in 26 categories labeled A, B, C, ..., Z. 
 Each book has a code of at least 3 characters. The 1st character of a code is a capital letter which defines the book category.

In the bookseller's stocklist each code is followed by a space and by a positive integer, which indicates the quantity of books of this code in stock.

Task
You will receive the bookseller's stocklist and a list of categories. Your task is to find the total number of books in the bookseller's stocklist,
with the category codes in the list of categories. Note: the codes are in the same order in both lists.

Return the result as a string described in the example below, or as a list of pairs (Haskell/Clojure/Racket/Prolog).

If any of the input lists is empty, return an empty string, or an empty array/list (Clojure/Racket/Prolog). -->
<?php
function stockList($listOfArt, $listOfCat)
{
    $arr = array();
    foreach ($listOfCat as $key) {
        $arr[$key] = 0;
    }
    foreach ($listOfArt as $value) {
        if (key_exists($value[0], $arr)) {
            $arr[$value[0]] += explode(' ', $value)[1];
        }
    }
    if (array_sum($arr) == 0) {
        return '';
    }
    foreach ($arr as $key => $value) {
        $arr[$key] = '(' . $key . ' : ' . $value . ')';
    }
    return implode(' - ', $arr);
}
