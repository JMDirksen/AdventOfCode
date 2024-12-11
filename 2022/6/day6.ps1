function isMark($string) {
    for($a = 0; $a -lt 4; $a++) {
        for($b = 0; $b -lt 4; $b++) {
            if(($a -ne $b) -and ($string[$a] -eq $string[$b])) { return $false }
        }
    }
    return $true
}

$buffer = Get-Content .\input.txt
for($i = 3; $i -lt $buffer.Length; $i++) {
    # Get last 4 characters
    $chars = -join $buffer[$($i-3)..$i]
    if(isMark $chars) {
        "Found @ $($i+1) : $chars"
        break
    }
}
