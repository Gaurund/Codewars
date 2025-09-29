<?php
  
function dnaToRna(string $str): string {
  return str_replace("T", "U", $str);
}