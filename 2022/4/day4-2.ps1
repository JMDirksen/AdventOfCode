$count = 0
foreach($line in Get-Content .\input.txt) {
    $a, $b = $line.Split(",")
    $a = @(IEX $a.Replace("-",".."))
    $b = @(IEX $b.Replace("-",".."))
    foreach($section in $a) {
        if($b.Contains($section)) {
            $count++
            break
        }
    }
}
$count
