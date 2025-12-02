import re


def main():
    inputfile = "input.txt"  # example.txt / input.txt
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

        # Full turns
        fts = steps // 100
        # Remaining steps
        steps = steps % 100

        # Move dial
        oldPosition = position
        if direction == "L":
            position -= steps
        elif direction == "R":
            position += steps

        # Correct position not to exceed 99 or go below 0
        while position > 99:
            position -= 100
        while position < 0:
            position += 100

        # Count zero position and passing zero
        timespassingzero += fts
        if position == 0:
            timespassingzero += 1
        elif oldPosition == 0:
            pass
        elif direction == "L" and position > oldPosition:
            timespassingzero += 1
        elif direction == "R" and position < oldPosition:
            timespassingzero += 1

        print(position, timespassingzero)
    return timespassingzero


main()
