import re


def main():
    # inputfile = "example2.txt"
    inputfile = "input.txt"
    with open(inputfile) as f:
        input = f.read()

    print(part2(input))


def part1(input):
    instructions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", input)
    sum = 0
    for i in instructions:
        x, y = i.replace("mul(", "").replace(")", "").split(",")
        sum += int(x) * int(y)
        print(x, y, sum)
    return sum


def part2(input):
    instructions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", input)
    instructions = apply_conditions(instructions)
    sum = 0
    for i in instructions:
        x, y = i.replace("mul(", "").replace(")", "").split(",")
        sum += int(x) * int(y)
        print(x, y, sum)
    return sum


def apply_conditions(instructions):
    do_condition = True
    resulting_instructions = []
    for i in instructions:
        if i == "don't()":
            do_condition = False
            continue
        if i == "do()":
            do_condition = True
            continue
        if do_condition:
            resulting_instructions += [i]
    return resulting_instructions


main()
