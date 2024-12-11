function Main {
    $head = 0,0
    $tail = 0,0
    $visits = ,"0,0"

    foreach($motion in Get-Content .\input.txt) {
        [char]$direction, [int]$distance = $motion.Split()

        "Motion: $motion"
    
        # Simulate head motion steps
        for($s = 1; $s -le $distance; $s++) {
            Switch($direction) {
                "R" { $head[0]++; Break }
                "L" { $head[0]--; Break }
                "U" { $head[1]++; Break }
                "D" { $head[1]--; Break }
            }
            "Head: $($head | ConvertTo-Json -Compress)"

            # Tail motion
            if(-not (isTouching $head $tail)) {
                # Needs diagonal move
                if($head[0] -ne $tail[0] -and $head[1] -ne $tail[1]) {
                    if($head[0] -gt $tail[0]) { $tail[0]++ }
                    else { $tail[0]-- }
                    if($head[1] -gt $tail[1]) { $tail[1]++ }
                    else { $tail[1]-- }
                }
                # R
                elseif($head[0] -gt $tail[0]) { $tail[0]++ }
                # L
                elseif($head[0] -lt $tail[0]) { $tail[0]-- }
                # U
                elseif($head[1] -gt $tail[1]) { $tail[1]++ }
                # D
                elseif($head[1] -lt $tail[1]) { $tail[1]-- }
                
                "Tail: $($tail | ConvertTo-Json -Compress)"

                # Register tail
                $visit = "$($tail[0]),$($tail[1])"
                if( -not $visits -or -not $visits.Contains($visit) ) {
                    $visits += ,$visit
                    #"Visits: $($visits | ConvertTo-Json -Compress)"
                }
            }
        }
    }

    "Visited: $($visits.Count)"
}

function isTouching([array]$a, [array]$b) {
    $xTouch = [Math]::Abs($a[0]-$b[0]) -le 1
    $yTouch = [Math]::Abs($a[1]-$b[1]) -le 1
    return $xTouch -and $yTouch
}

Main
