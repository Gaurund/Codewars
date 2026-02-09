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

function numbers_to_array($n)
{
    $arr = array();
    while ($n > 0) {
        $arr[] = $n % 10;
        $n = intdiv($n, 10);
    }
    return $arr;
}

function nextBigger($n)
{
    $init_arr = numbers_to_array($n);
    var_dump($init_arr);
    echo '<br/>--- ';
    $buff_arr = [$init_arr[0]];
    var_dump($buff_arr);
    echo '<br/>+++ ';
    $i = 1;
    while ($i < count($init_arr)) {
        $buff_arr[$i] = $init_arr[$i];
        if ($buff_arr[$i] < $buff_arr[$i - 1]) {
            // Если число полученное меньше предыдущего, то надо начать перестановку
            // Надо запомнить последнее полученное число
            $last = $buff_arr[$i];
            // Надо отсортировать весь массив по убыванию
            sort($buff_arr);
            $buff_arr = array_reverse($buff_arr);
            // Надо найти то последнее полученное число в массиве.
            $needle_key = array_search($last, $buff_arr);
            // Извлечь число перед ним
            // Ещё раз отсортировать массив по убыванию
            $needle = array_splice($buff_arr, $needle_key - 1, 1);
            // Добавить в конец массива извлечённое ранее число
            $buff_arr[] = $needle;
            // Заменить в исходном массиве поиндексно значения взяв новые из буфферного массива
            array_splice($init_arr, 0, count($buff_arr), $buff_arr);
            $i = count($init_arr);
        }
        $i++;
    }

    return $n;
}
