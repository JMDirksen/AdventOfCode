$sum = 0
$elf = @()

foreach($line in Get-Content .\input.txt) {
    if($line -eq "") {
        $elf += $sum
        $sum = 0
    }
    else {
        $sum += [int]$line
    }
}

$elf | Measure-Object -Maximum
