function test($array) {
    $array = $array | % { $_ }
    $array[0] = "!"
}

$test = @("a", "b")
$test
test $test
$test
