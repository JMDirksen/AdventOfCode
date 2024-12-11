function Main {
    $knot = @((0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
    $visits = ,"0,0"

    foreach($motion in Get-Content .\input.txt) {
        [char]$direction, [int]$distance = $motion.Split()

        "Motion: $motion"
    
        # Simulate head motion steps
        for($s = 1; $s -le $distance; $s++) {
            " Step $s"

            # Move head
            Switch($direction) {
                "R" { $knot[0][0]++; Break }
                "L" { $knot[0][0]--; Break }
                "U" { $knot[0][1]++; Break }
                "D" { $knot[0][1]--; Break }
            }
            "  Head: $($knot[0] | ConvertTo-Json -Compress)"

            # Iterate other rope knots
            for($k = 1; $k -le 9; $k++) {
                $knot[$k] = getNewPos $knot[$k] $knot[$k-1]
                "   Knot $k $($knot[$k]|ConvertTo-Json -Compress)"
            }

            # Register tail
            $visit = "$($knot[9][0]),$($knot[9][1])"
            if( -not $visits -or -not $visits.Contains($visit) ) {
                $visits += ,$visit
            }
        }
    }

    "Tail visited: $($visits | ConvertTo-Json -Compress)"
    "Tail visits: $($visits.Count)"
}

function getNewPos($this, $target) {
    if(-not (areTouching $this $target)) {
        # Needs diagonal move
        if($target[0] -ne $this[0] -and $target[1] -ne $this[1]) {
            if($target[0] -gt $this[0]) { $this[0]++ }
            else { $this[0]-- }
            if($target[1] -gt $this[1]) { $this[1]++ }
            else { $this[1]-- }
        }
        # R
        elseif($target[0] -gt $this[0]) { $this[0]++ }
        # L
        elseif($target[0] -lt $this[0]) { $this[0]-- }
        # U
        elseif($target[1] -gt $this[1]) { $this[1]++ }
        # D
        elseif($target[1] -lt $this[1]) { $this[1]-- }
    }
    return $this
}

function areTouching([array]$a, [array]$b) {
    $xTouch = [Math]::Abs($a[0]-$b[0]) -le 1
    $yTouch = [Math]::Abs($a[1]-$b[1]) -le 1
    return $xTouch -and $yTouch
}

Main
