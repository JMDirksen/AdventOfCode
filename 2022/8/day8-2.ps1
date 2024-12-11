$input = ".\input.txt"

# Generate map
$map = [System.Collections.ArrayList]@()
foreach($line in Get-Content $input) {
    [void]$map.Add([System.Collections.ArrayList]$line.ToCharArray())
}

$highScore = 0

# Iterate trees
for($r = 0; $r -lt $map.Count; $r++) {
    for($c = 0; $c -lt $map[$r].Count; $c++) {
        # Consider tree
        $tree = $map[$r][$c]
        $score = $scoreWest = $scoreEast = $scoreNorth = $scoreSouth = 0

        # Look west
        #$($c-1)..0 | % 
        for($t = $c-1; $t -ge 0; $t--) {
            $scoreWest++
            if($map[$r][$t] -ge $tree) { break }
        }
        
        # Look east
        for($t = $c+1; $t -lt $map[$r].Count; $t++) {
            $scoreEast++
            if($map[$r][$t] -ge $tree) { break }
        }

        # Look north
        for($t = $r-1; $t -ge 0; $t--) {
            $scoreNorth++
            if($map[$t][$c] -ge $tree) { break }
        }

        # Look south
        for($t = $r+1; $t -lt $map.Count; $t++) {
            $scoreSouth++
            if($map[$t][$c] -ge $tree) { break }
        }

        $score = $scoreWest * $scoreEast * $scoreNorth * $scoreSouth
        "$r $c $tree $scoreWest $scoreEast $scoreNorth $scoreSouth $score"
        if($score -gt $highScore) { 
            $highScore = $score
            "!"
        }
    }
}

$highScore
