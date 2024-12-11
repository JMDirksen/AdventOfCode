$totalscore = 0

foreach($line in Get-Content .\input.txt) {
    $score = 0

    $them = [byte][char]$line.Substring(0,1)-64
    $need = $line.Substring(2,1).Replace("X",-1).Replace("Y",0).Replace("Z",1)
    $you = $them + $need
    if ($you -eq 0) { $you = 3 }
    if ($you -eq 4) { $you = 1 }

    $score += $you

    # win
    if ($you -eq $them+1 -or $you -eq $them-2) { $score += 6 }
    
    # draw
    if ($you -eq $them) { $score += 3 }

    $totalscore += $score
}

$totalscore
