# import re
from time import time
import array


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part1(input))


def part1(input):
    start = time()
    stones = list(map(int, input.split()))
    stones = array.array("Q", stones)
    for i in range(75):
        print(f"Blink {i+1} at {int(time()-start)} sec.")
        print(f"Len: {len(stones)}")
        output = array.array("Q", [])
        for s, stone in enumerate(stones):
            # Apply rules
            if stone == 0:
                output.append(1)
            elif len(str(stone)) % 2 == 0:
                output.append(int(str(stone)[:len(str(stone))//2]))
                output.append(int(str(stone)[len(str(stone))//2:]))
            else:
                output.append(stone * 2024)
        stones = output
    return len(stones)


def part2(input):
    return


main()
