$lines = Get-Content .\input.txt
#$lines = Get-Content .\test.txt

$disksize = 70000000
$neededspace = 30000000
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

$free = $disksize - $dirs[""]
$toRemove = $neededspace - $free
"Free: $free  To remove: $toRemove"

# Find
$smallest = @{}
$smallest["name"] = ""
$smallest["size"] = $disksize

foreach($dir in $dirs.GetEnumerator()) {
    if(($dir.Value -ge $toRemove) -and ($dir.Value -lt $smallest["size"])) {
        "Possible: $($dir.Name) $($dir.Value)"
        $smallest["name"] = $dir.Name
        $smallest["size"] = $dir.Value
    }
}
