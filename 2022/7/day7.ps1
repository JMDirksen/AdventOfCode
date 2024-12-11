$lines = Get-Content .\input.txt
#$lines = Get-Content .\test.txt

$dirs = @{}
$curDir = [System.Collections.ArrayList]@()
foreach($line in $lines) {

    # Ignore first line
    if($line -eq "$ cd /") { continue }

    # Detect directory change
    if($line -like "$ cd *") {
        # Move out
        if($line -eq "$ cd ..") {
            $curDir.RemoveAt($curDir.Count-1)
        }
        # Move in
        else {
            [void]$curDir.Add($line.Split(" ")[2])
        }
        $dirName = [string]$curDir
        $dirs[$dirName] += 0
    }

    # Files
    if(($line -notlike "$ *") -and ($line -notlike "dir *")) {
        [int]$filesize, $filename = $line.Split(" ")
        # Loop upper dirs
        for($i = 0; $i -lt $curDir.Count; $i++) {
            $dirs[[string]$curDir[0..$i]] += $filesize
        }
        $dirs[""] += $filesize
    }

}

# Filter
$filtered = @{}
foreach($dir in $dirs.GetEnumerator()) {
    if($dir.Value -le 100000) {
        $filtered.Add($dir.Name, $dir.Value)
    }
}

# Sum
$sum = 0
foreach($dir in $filtered.GetEnumerator()) {
    $sum += $dir.Value
}

$dirs | ConvertTo-Json
$filtered | ConvertTo-Json
$sum
