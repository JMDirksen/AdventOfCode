$prioSum = 0
foreach($line in Get-Content .\input.txt) {
    $compartment1 = $line.Substring(0,$line.Length/2)
    $compartment2 = $line.Substring($line.Length/2)

    foreach($char in [char[]]$compartment1) {
        if($compartment2.Contains($char)) {
            $found = $char
        }
    }

    # Character value
    $ascii = [byte][char]$found

    # Upper case
    if($ascii -ge 65 -and $ascii -le 90) {
        $prio = $ascii-38
    }
    # Lower case
    else {
        $prio = $ascii-96
    }


    #$line, $c1, $c2, $found, $prio
    $prioSum += $prio
}

$prioSum
