import re


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part2(input))


def part1(input):
    # Setup grids
    antenna_grid = list(map(list, input.splitlines()))
    antinode_grid = [len(antenna_grid[0])*["."] for _ in range(len(antenna_grid))]
    print_grid(antenna_grid, antinode_grid)

    # Iterate posible antenna frequencies
    for f in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":

        # Get list of antennas
        antenna_list = []
        for r in range(len(antenna_grid)):
            for c in range(len(antenna_grid[r])):
                if antenna_grid[r][c] == f:
                    antenna_list += [[r, c]]
        if not len(antenna_list):
            continue
        print(f, antenna_list)

        # Iterate antennas
        for a in antenna_list:
            # Iterate other antennas
            for b in antenna_list:
                if b == a:
                    continue
                # Calculate antinode
                an = [a[0] + 2*(b[0] - a[0]), a[1] + 2*(b[1] - a[1])]
                if not on_grid(an, antenna_grid):
                    continue
                # Add antinode to grid
                print(a, b, an)
                antinode_grid[an[0]][an[1]] = "#"
    
    print_grid(antenna_grid, antinode_grid)
    an_count = count_an(antinode_grid)
    return an_count


def part2(input):
    # Setup grids
    antenna_grid = list(map(list, input.splitlines()))
    antinode_grid = [len(antenna_grid[0])*["."] for _ in range(len(antenna_grid))]
    print_grid(antenna_grid, antinode_grid)

    # Iterate posible antenna frequencies
    for f in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":

        # Get list of antennas
        antenna_list = []
        for r in range(len(antenna_grid)):
            for c in range(len(antenna_grid[r])):
                if antenna_grid[r][c] == f:
                    antenna_list += [[r, c]]
        if not len(antenna_list):
            continue
        print(f, antenna_list)

        # Iterate antennas
        for a in antenna_list:
            # Iterate other antennas
            for b in antenna_list:
                if b == a:
                    continue
                # Calculate antinodes
                an_dist = 1
                while True:
                    an = [a[0] + an_dist*(b[0] - a[0]), a[1] + an_dist*(b[1] - a[1])]
                    if not on_grid(an, antenna_grid):
                        break
                    # Add antinode to grid
                    print(a, b, an)
                    antinode_grid[an[0]][an[1]] = "#"
                    an_dist += 1
    
    print_grid(antenna_grid, antinode_grid)
    an_count = count_an(antinode_grid)
    return an_count


def count_an(grid):
    count = 0
    for r in grid:
        for i in r:
            if i == "#":
                count += 1
    return count


def on_grid(pos, grid):
    if pos[0] < 0 or pos[0] > len(grid)-1:
        return False
    if pos[1] < 0 or pos[1] > len(grid[0])-1:
        return False
    return True


def print_grid(gridA, gridB):
    for i in range(len(gridA)):
        print(" ".join(gridA[i]) + "   " + " ".join(gridB[i]))


main()
