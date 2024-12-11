function isDistinct($string) {
    for($a = 0; $a -lt $string.Length; $a++) {
        for($b = 0; $b -lt $string.Length; $b++) {
            if(($a -ne $b) -and ($string[$a] -eq $string[$b])) { return $false }
        }
    }
    return $true
}

$buffer = Get-Content .\input.txt
for($i = 13; $i -lt $buffer.Length; $i++) {
    # Get last 14 characters
    $chars = -join $buffer[$($i-13)..$i]
    if(isDistinct $chars) {
        "Found @ $($i+1) : $chars"
        break
    }
}
