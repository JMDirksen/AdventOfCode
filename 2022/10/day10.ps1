$lines = Get-Content .\input.txt
$line = 0
$instruction = $null
$registerX = 1
$sum = 0

for($cycle = 1; $cycle -le 250; $cycle++) {
    # Check for instruction
    if(-not $instruction) {
        # Read new instruction
        if($line -ge $lines.Count) { break }
        $instruction, $value = $lines[$line].Split()
        $line++
        if($instruction -eq "addx") { $time = 2 }
        else { $time = 1 }
    }

    if( (($cycle+20)%40 -eq 0) -and ($cycle -le 220) ) {
        $signalStrength = $($cycle*$registerX)
        $sum += $signalStrength
        "cycle $cycle x $registerX ss $signalStrength sum $sum"
    }

    # Execute instruction
    $time--
    if($time -le 0) {
        if($instruction -eq "addx") {
            $registerX += $value
        }
        $instruction = $null
    }
}
