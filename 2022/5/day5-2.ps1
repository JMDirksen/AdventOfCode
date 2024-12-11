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
    $amount = [int]$split[1]
    $from = [int]$split[3]-1
    $to = [int]$split[5]-1
    
    # Move from > to
    # Get crates
    $crates = $stack[$from][$($stack[$from].Count-$amount)..$($stack[$from].Count-1)]
    "Move $crates from $from to $to"
    # Remove/Add crates
    $crates | % {
        $stack[$from].RemoveAt($($stack[$from].Count-1))
        [void]$stack[$to].Add($_)
    }
}

"", "End:"
1..9 | % {
    "Stack $_ : $($stack[$_-1] | ConvertTo-Json -Compress)"
}
