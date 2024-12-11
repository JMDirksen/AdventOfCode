$count = 0
foreach($line in Get-Content .\input.txt) {
    $a, $b = $line.Split(",")
    [int]$a1, [int]$a2 = $a.Split("-")
    [int]$b1, [int]$b2 = $b.Split("-")

    # A in B or B in A
    if (($a1 -ge $b1 -and $a2 -le $b2) -or ($b1 -ge $a1 -and $b2 -le $a2)) {
        $count++
    }

}
$count
