$input = ".\input.txt"

# Generate map
$map = [System.Collections.ArrayList]@()
foreach($line in Get-Content $input) {
    [void]$map.Add([System.Collections.ArrayList]$line.ToCharArray())
}

$visibleTrees = 2*$map[0].Count + 2*($map.Count-2)

# Iterate inner trees
for($r = 1; $r -lt $map.Count-1; $r++) {
    for($c = 1; $c -lt $map[$r].Count-1; $c++) {
        # Test tree
        $tree = $map[$r][$c]
        $visible = $false

        # Look west
        $west = $map[$r][0..$($c-1)]
        if( $($west | Measure-Object -Maximum).Maximum -lt $tree ) { $visible = $true }
        
        # Look east
        $east = $map[$r][$($c+1)..$($map[$r].Count-1)]
        if( $($east | Measure-Object -Maximum).Maximum -lt $tree ) { $visible = $true }
        
        # Look north
        $north = [System.Collections.ArrayList]@()
        0..$($r-1) | % { [void]$north.Add($map[$_][$c]) }
        if( $($north | Measure-Object -Maximum).Maximum -lt $tree ) { $visible = $true }
        
        # Look south
        $south = [System.Collections.ArrayList]@()
        $($r+1)..$($map.Count-1) | % { [void]$south.Add($map[$_][$c]) }
        if( $($south | Measure-Object -Maximum).Maximum -lt $tree ) { $visible = $true }

        "row $r col $c tree $tree visible $visible"
        if($visible) { $visibleTrees++ }
    }
}

$visibleTrees
