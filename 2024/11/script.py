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
        s = 0
        while s < len(stones):
            # Apply rules
            if stones[s] == 0:
                stones[s] = 1
            elif len(str(stones[s])) % 2 == 0:
                left = int(str(stones[s])[:len(str(stones[s]))//2])
                right = int(str(stones[s])[len(str(stones[s]))//2:])
                stones[s] = left
                s += 1
                stones.insert(s, right)
            else:
                stones[s] = stones[s] * 2024
            s += 1
    return len(stones)


def part2(input):
    return


main()
