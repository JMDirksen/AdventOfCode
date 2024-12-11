$lines = Get-Content .\input.txt

# Iterate 1st Elf in ElfGroups
$prioSum = 0
for($i=0; $i -lt $lines.Length; $i+=3) {
    # Compare all items of 1st Elf to 2nd and 3th Elf
    foreach($char in [char[]]$lines[$i]) {
        if($lines[$i+1].Contains($char) -and $lines[$i+2].Contains($char)) {
            $found = $char
            break
        }
    }

    # Character value
    $ascii = [byte][char]$found
    # Upper case prio
    if($ascii -ge 65 -and $ascii -le 90) {
        $prio = $ascii-38
    }
    # Lower case prio
    else {
        $prio = $ascii-96
    }

    $prioSum += $prio
}

$prioSum
