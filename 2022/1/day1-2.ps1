$elf = [System.Collections.ArrayList]@()
$sum = 0

foreach($line in Get-Content .\input.txt) {
    if($line -eq "") {
        [void]$elf.Add($sum)
        $sum = 0
    }
    else {
        $sum += [int]$line
    }
}

$highElf = [System.Collections.ArrayList]@()
1..3 | % {
    $max = [int]($elf | Measure-Object -Maximum).Maximum
    [void]$highElf.Add($max)
    $elf.Remove($max)
}

$highElf | Measure-Object -Sum
