import re
import json


def main():
    # inputfile = "example1.txt"
    inputfile = "example2.txt"
    # inputfile = "input.txt"
    with open(inputfile) as f:
        input = f.read()

    print(part2(input))


def part1(input):
    input = input.splitlines()
    parts_sum = 0
    for line_nr in range(len(input)):
        line = input[line_nr]
        numbers = re.finditer(r"\d+", line)
        for number in numbers:
            is_part_nr = search_parts(line_nr, number.span(), input) > 0
            if is_part_nr:
                parts_sum += int(number.group())
    return parts_sum


def part2(input):
    input = input.splitlines()
    parts_sum = 0
    for line_nr in range(len(input)):
        line = input[line_nr]
    return


def search_parts(line_nr, span, input):

    if line_nr > 0:
        top = input[line_nr-1]
        top = top[max(0, span[0]-1):span[1]+1]
    else:
        top = ""

    if line_nr < len(input)-1:
        bottom = input[line_nr+1]
        bottom = bottom[max(0, span[0]-1):span[1]+1]
    else:
        bottom = ""

    if span[0] > 0:
        left = input[line_nr][span[0]-1]
    else:
        left = ""

    if span[1] < len(input[line_nr]):
        right = input[line_nr][span[1]]
    else:
        right = ""

    parts = (len(re.sub(r"\d+|\.", "", top))
             + len(re.sub(r"\d+|\.", "", bottom))
             + len(re.sub(r"\d+|\.", "", left))
             + len(re.sub(r"\d+|\.", "", right))
             )

    return parts


main()
