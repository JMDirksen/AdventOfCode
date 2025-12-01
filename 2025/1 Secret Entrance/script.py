import re


def main():
    inputfile = "example.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    #print(part1(input))
    print(part2(input))


def part1(input):
    position = 50
    timesatzero = 0
    lines = input.splitlines()
    for line in lines:
        direction = line[0]
        steps = int(line[1:])
        print(direction, steps, sep="", end=" ")
        if direction == "L":
            position -= steps
        elif direction == "R":
            position += steps
        # Dial goes from 0 to 99
        position = position % 100
        # Correct for negative position
        while position < 0:
            position += 100
        if position == 0:
            timesatzero += 1
        print(position)
    return timesatzero


def part2(input):
    position = 50
    timespassingzero = 0
    lines = input.splitlines()
    for line in lines:
        direction = line[0]
        steps = int(line[1:])
        print(direction, steps, sep="", end=" ")

        if direction == "L":
            position -= steps
        elif direction == "R":
            position += steps

        if position == 0:
            timespassingzero += 1

        if position > 99:
            timespassingzero -= 1
        while position > 99:
            timespassingzero += 1
            position -= 100
        if position < 0:
            timespassingzero -= 1
        while position < 0:
            timespassingzero += 1
            position += 100

        print(position, timespassingzero)
    return timespassingzero


main()
