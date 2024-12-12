# import re
from time import time
import array


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part2(input))


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
    start = time()
    stones = list(map(int, input.split()))

    # List with nr counts
    for s, stone in enumerate(stones):
        stones[s] = [stone, 1]

    # Blinks
    for b in range(75):
        print(f"Blink {b+1} at {int(time()-start)} sec.")
        output = []
        for s, stone in enumerate(stones):
            # Apply rules
            if stone[0] == 0:
                add_value(output, 1, stone[1])
            elif len(str(stone[0])) % 2 == 0:
                add_value(output, int(str(stone[0])[:len(str(stone[0]))//2]), stone[1])
                add_value(output, int(str(stone[0])[len(str(stone[0]))//2:]), stone[1])
            else:
                add_value(output, stone[0]*2024, stone[1])
        stones = output

    count = 0
    for stone in stones:
        count += stone[1]
    return count


def add_value(stonesList, value, count):
    found = False
    for s, stone in enumerate(stonesList):
        if stone[0] == value:
            stonesList[s][1] += count
            found = True
            break
    if not found:
        stonesList.append([value, count])
        

main()
