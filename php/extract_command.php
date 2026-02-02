    <?php
    $size = "large";
    $var_array = array(
        "color" => "blue",
        "size"  => "medium",
        "shape" => "sphere"
    );

    extract($var_array, EXTR_PREFIX_SAME, "w");

    echo "$color, $size, $shape, $w_size\n";
