import re


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part1(input))


def part1(input):

    # Uncompress
    print("Uncompressing...")
    file = True
    id = 0
    disk_map = []
    for i in input:
        if file:
            for x in range(int(i)):
                disk_map += [id]
            id += 1
        else:
            for x in range(int(i)):
                disk_map += [None]
        file = not file

    # Defragment
    print("Defragmenting...")
    while True:
        # First block with data from right
        for br in range(len(disk_map)-1, -1, -1):
            if disk_map[br] != None:
                break
        # First free space from left
        for bl in range(0, br):
            if disk_map[bl] == None:
                break
        if bl == br-1:
            break
        # Move block
        disk_map[bl] = disk_map[br]
        disk_map[br] = None

    # Calculate checksum
    print("Calculating checksum...")
    checksum = 0
    for i in range(len(disk_map)):
        if disk_map[i] == None:
            break
        checksum += i * disk_map[i]
    return checksum


def part2(input):
    return


main()
