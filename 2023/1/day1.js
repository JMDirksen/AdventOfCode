function go() {
    var input = document.getElementById('input').value
    var lines = input.split('\n')
    var sum = 0
    for(var i = 0; i < lines.length; i++) {
        var digits = lines[i].replace(/\D/g, '')
        var digit1 = digits[0]
        var digit2 = digits[digits.length-1]
        var concat = parseInt(digit1 + digit2)
        sum += concat
        console.log(digit1, digit2, concat, sum)
    }
    alert(sum)
}

function go2() {
    var input = document.getElementById('input').value
    var lines = input.split('\n')
    var sum = 0
    for(var i = 0; i < lines.length; i++) {
        var digits = lines[i].replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9').replace(/\D/g, '')
        var digit1 = digits[0]
        var digit2 = digits[digits.length-1]
        var concat = parseInt(digit1 + digit2)
        sum += concat
        console.log(digit1, digit2, concat, sum)
    }
    alert(sum)
}
