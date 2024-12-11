$lines = Get-Content .\input.txt

# Build virtual stacks
$stack = [System.Collections.ArrayList]@()
# Iterate stacks
0..8 | % {
    $stackId = $stack.Add([System.Collections.ArrayList]@())
    # Iterate stack layers
    0..7 | % {
        $layerId = $_
        $lineNr = 7-$layerId
        $charNr = $stackId*4+1
        $crate = $lines[$lineNr][$charNr]
        if($crate -ne " ") {
            [void]$stack[$stackId].Add($crate)
        }
    }
}

"Start:"
1..9 | % {
    "Stack $_ : $($stack[$_-1] | ConvertTo-Json -Compress)"
}

# Iterate steps
for($l = 10; $l -lt $lines.Count; $l++) {
    $step = $l-9
    $split = $lines[$l].Split(" ")
    $times = [int]$split[1]
    $from = [int]$split[3]-1
    $to = [int]$split[5]-1
    # Run x times
    for($t = 1; $t -le $times; $t++) {
        # Move from > to
        # Get crate
        $crate = $stack[$from][$stack[$from].Count-1]
        # Remove crate
        $stack[$from].RemoveAt($stack[$from].Count-1)
        # Add crate
        [void]$stack[$to].Add($crate)
    }
}

"", "End:"
1..9 | % {
    "Stack $_ : $($stack[$_-1] | ConvertTo-Json -Compress)"
}
