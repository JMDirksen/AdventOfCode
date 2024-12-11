# Read notes
$monkeys = @()
foreach ($line in Get-Content .\input.txt) {
    $line = $line.Trim()
    # Monkey ID
    if ($line.StartsWith("M")) { $id = [int]$line.Split()[1].Trim(":") }
    # Item list
    if ($line.StartsWith("S")) {
        [System.Collections.ArrayList]$items = @(iex $line.Split(":")[1])
    }
    # Operation
    if ($line.StartsWith("O")) { $operation = $line.Split("=")[1].Trim() }
    # Test
    if ($line.StartsWith("T")) { $test = [int]$line.Split()[3] }
    # Actions on test true/false
    if ($line.StartsWith("If t")) { $onTrue = [int]$line.Split()[5] }
    if ($line.StartsWith("If f")) {
        $onFalse = [int]$line.Split()[5]

        # End of Monkey
        $monkey = @{}
        $monkey.id = $id
        $monkey.items = $items
        $monkey.operation = $operation
        $monkey.test = $test
        $monkey.onTrue = $onTrue
        $monkey.onFalse = $onFalse
        $monkey.inspected = 0
        $monkeys += , $monkey
    }
}

# Rounds
for ($round = 1; $round -le 20; $round++) {
    "Round $round"
    # Turns
    foreach ($monkey in $monkeys) {
        "Monkey $($monkey.id)"
        # Items
        while ($monkey.items) {
            $item = $monkey.items[0]
            "item $item"
            # Pick
            $monkey.items.RemoveAt($i)
            # Inspect
            $monkey.inspected++
            # Operation
            $item = iex $monkey.operation.Replace("old", $item)
            # Relief
            $item = [long][math]::Floor($item / 3)
            # Test
            if ( ($item % $monkey.test) -eq 0 ) { $throwTo = $monkey.onTrue }
            else { $throwTo = $monkey.onFalse }
            # Throw
            "throw $item to $throwTo"
            [void]$monkeys[$throwTo].items.Add($item)
        }
    }
    "After round $round : $($monkeys | ConvertTo-Json -Compress)"
}

$inspects = @()
$monkeys | % { $inspects += , $($_.inspected) }
$top2 = $inspects | Sort-Object -Descending | select -First 2
$monkeyBusiness = $top2[0] * $top2[1]
"Monkey business: $monkeyBusiness"
