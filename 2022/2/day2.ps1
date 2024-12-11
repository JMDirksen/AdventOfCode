$totalscore = 0

foreach($line in Get-Content .\input.txt) {
    $score = 0

    $them = [byte][char]$line.Substring(0,1)-64
    $you = [byte][char]$line.Substring(2,1)-87

    $score += $you

    # win
    if ($you -eq $them+1 -or $you -eq $them-2) { $score += 6 }
    
    # draw
    if ($you -eq $them) { $score += 3 }

    $totalscore += $score
}

$totalscore
