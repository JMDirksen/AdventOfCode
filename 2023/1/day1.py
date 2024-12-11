import re


def main():
    # inputfile = "example1.txt"
    inputfile = "example2.txt"
    inputfile = "input.txt"
    with open(inputfile) as f:
        input = f.read()

    print(part2(input))


def part1(input):
    sum = 0
    for line in input.splitlines():
        digits = "".join(re.findall(r'\d+', line))
        firstdigit = digits[0]
        lastdigit = digits[-1]
        concat = firstdigit + lastdigit
        sum += int(concat)
        print(line, digits, firstdigit, lastdigit, concat, sum)
    return sum


def part2(input):
    sum = 0
    for line in input.splitlines():
        r = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
        leftnumber = re.search(r, line).group()
        r = r'(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)'
        rightnumber = re.search(r, line[::-1]).group()[::-1]
        leftnumber = replace_numbers(leftnumber)
        rightnumber = replace_numbers(rightnumber)
        concat = leftnumber + rightnumber
        sum += int(concat)
        print(line, leftnumber, rightnumber, concat, sum)
    return sum


def replace_numbers(string):
    string = string.replace("one", "1")
    string = string.replace("two", "2")
    string = string.replace("three", "3")
    string = string.replace("four", "4")
    string = string.replace("five", "5")
    string = string.replace("six", "6")
    string = string.replace("seven", "7")
    string = string.replace("eight", "8")
    string = string.replace("nine", "9")
    return string


main()
