<!-- Create a function that returns the CSV representation of a two-dimensional numeric array. -->

<?php

function toCsvText($array) {
  $lines = array();
  foreach($array as $line){
    $lines[] = implode(',',$line);
  }
  var_dump($lines);
  return implode('\n',$lines);
}