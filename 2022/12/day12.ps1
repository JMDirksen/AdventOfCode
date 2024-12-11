function Main {
    "$(Get-Date) Start"
    # Read map
    $map = @()
    foreach ($line in Get-Content .\input.txt) { $map += , $line.ToCharArray() }
    $start = findStart $map
    $Global:bestSolve = 0
    solve $map $start 0
    "$(Get-Date) Best solve: $bestSolve"
}

function solve($map, $pos, $steps) {
    $hight = [string]$map[$pos[0]][$pos[1]]
    #"Steps $steps, pos $pos, hight $hight"
    #printMap $map

    if ($hight -ceq "E") {
        "$(Get-Date) Solved in $steps steps!"
        if($bestSolve -eq 0 -or $steps -lt $bestSolve) {
            $Global:bestSolve = $steps
        }
    }

    # Check right
    if ($pos[1] -lt $map[$pos[0]].Count - 1) {
        $targetPos = $pos[0], ($pos[1] + 1)
        $targetHight = $map[$targetPos[0]][$targetPos[1]]
        if (isValid $hight $targetHight) {
            $newMap = deepCopy $map
            $newMap[$pos[0]][$pos[1]] = ">"
            #"Go right"
            solve $newMap $targetPos ($steps + 1)
        }
    }
    # Check up
    if ($pos[0] -gt 0) {
        $targetPos = ($pos[0] - 1), $pos[1]
        $targetHight = $map[$targetPos[0]][$targetPos[1]]
        if (isValid $hight $targetHight) {
            $newMap = deepCopy $map
            $newMap[$pos[0]][$pos[1]] = "^"
            #"Go up"
            solve $newMap $targetPos ($steps + 1)
        }
    }
    # Check down
    if ($pos[0] -lt $map.Count - 1) {
        $targetPos = ($pos[0] + 1), $pos[1]
        $targetHight = $map[$targetPos[0]][$targetPos[1]]
        if (isValid $hight $targetHight) {
            $newMap = deepCopy $map
            $newMap[$pos[0]][$pos[1]] = "V"
            #"Go down"
            solve $newMap $targetPos ($steps + 1)
        }
    }
    # Check left
    if ($pos[1] -gt 0) {
        $targetPos = $pos[0], ($pos[1] - 1)
        $targetHight = $map[$targetPos[0]][$targetPos[1]]
        if (isValid $hight $targetHight) {
            $newMap = deepCopy $map
            $newMap[$pos[0]][$pos[1]] = "<"
            #"Go left"
            solve $newMap $targetPos ($steps + 1)
        }
    }

    #"Nothing, back to step $($steps - 1)"
}

function isValid($curHight, $target) {
    $curHight = ([string]$curHight).Replace("S", "a")
    $target = ([string]$target).Replace("E", "z")
    if ($target -cnotmatch "[a-z]") { return $false }
    #if (([byte][char]$target - [byte][char]$curHight) -le 1) {
    $elevation = [byte][char]$target - [byte][char]$curHight
    if ($elevation -ge 0 -and $elevation -le 1) { return $true }
    else { return $false }
}

function findStart($map) {
    for ($r = 0; $r -lt $map.Count; $r++) {
        for ($c = 0; $c -lt $map[$r].Count; $c++) {
            if ($map[$r][$c] -ceq "S") {
                return $r, $c
            }
        }
    }
}

function printMap($map) {
    " + " + 0..($map[0].Count - 1) -join " "
    for ($r = 0; $r -lt $map.Count; $r++) {
        " $r " + $map[$r] -join " "
    }
}

function deepCopy($2dArray) {
    $clone = [System.Collections.ArrayList]@()
    for ($x = 0; $x -lt $2dArray.Count; $x++ ) {
        $clone2 = [System.Collections.ArrayList]@()
        for ($y = 0; $y -lt $2dArray[$x].Count; $y++) {
            [void]$clone2.Add($2dArray[$x][$y])
        }
        [void]$clone.Add([array]$clone2)
    }
    return [array]$clone
}

Main
