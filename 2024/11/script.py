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
        output = array.array("Q", [])
        for s in range(len(stones)):
            # Apply rules
            if stones[s] == 0:
                output.append(1)
            elif len(str(stones[s])) % 2 == 0:
                output.append(int(str(stones[s])[:len(str(stones[s]))//2]))
                output.append(int(str(stones[s])[len(str(stones[s]))//2:]))
            else:
                output.append(stones[s] * 2024)
        stones = output
    return len(stones)


def part2(input):
    return


main()
