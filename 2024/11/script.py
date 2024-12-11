#import re


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part1(input))


def part1(input):
    stones = list(map(int, input.split()))
    for i in range(75):
        print("Blink", i+1)
        #print(stones, "-> ", end="")
        output = []
        for s in range(len(stones)):
            stone = stones[s]
            # Apply rules
            if stone == 0:
                output += [1]
            elif len(str(stone)) % 2 == 0:
                output += [int(str(stone)[:int(len(str(stone))/2)])]
                output += [int(str(stone)[int(len(str(stone))/2):])]
            else:
                output += [(stone*2024)]
        #print(output)
        stones = output
    return len(output)


def part2(input):
    return


main()
