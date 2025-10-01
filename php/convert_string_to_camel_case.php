<!-- 
 Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
 The first word within the output should be capitalized only if the original word was capitalized 
 (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"The_Stealth-Warrior" gets converted to "TheStealthWarrior" 
-->

<?php

function toCamelCase($str)
{
    $result = implode("",array_map('ucfirst', preg_split("/[_-]/", $str)));
    return ctype_upper($str[0]) ? $result : lcfirst($result);
}
