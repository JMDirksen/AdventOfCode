import re


def main():
    inputfile = "example.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part1(input))


def part1(input):

    # Uncompress
    file = True
    id = 0
    disk_map = ""
    for i in input:
        if file:
            for x in range(int(i)):
                disk_map += str(id)
            id += 1
        else:
            for x in range(int(i)):
                disk_map += "."
        file = not file
    print("Uncompressed:", disk_map)

    # Defragment
    while True:
        # First digit from right
        block_r = len(disk_map)-1-re.search("\d", disk_map[::-1]).start()
        # First free space from left
        search_space = re.search("\.", disk_map[0:block_r+1])
        if not search_space:
            break
        space_l = search_space.start()
        # Move block
        disk_map = list(disk_map)
        disk_map[space_l] = disk_map[block_r]
        disk_map[block_r] = "."
        disk_map = "".join(disk_map)
    
    # Calculate checksum
    files_map = disk_map.replace(".", "")
    checksum = 0
    for pos in range(len(files_map)):
        checksum += pos * int(files_map[pos])
    
    return checksum


def part2(input):
    return


main()
