$lines = Get-Content .\input.txt
$line = 0
$instruction = $null
$registerX = 1
$crtLine = New-Object string[] 6

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

    # Generate CRT output
    $pixelX = ($cycle-1)%40
    $pixelY = [math]::Floor(($cycle-1)/40)
    if( ($pixelX -ge $registerX-1) -and ($pixelX -le $registerX+1) ) { $pixel = "#" }
    else { $pixel = "." }
    $crtLine[$pixelY] += $pixel

    # Execute instruction
    $time--
    if($time -le 0) {
        if($instruction -eq "addx") {
            $registerX += $value
        }
        $instruction = $null
    }
}

# Draw CRT
$crtLine
