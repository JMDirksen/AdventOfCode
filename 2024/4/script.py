import re


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part2(input))


def part1(input):
    rows = input.splitlines()
    count = 0
    for r in range(len(rows)):
        row = rows[r]
        for c in range(len(row)):
            count += count_xmas(r, c, rows)
    return count


def part2(input):
    rows = input.splitlines()
    count = 0
    for r in range(1, len(rows)-1):
        row = rows[r]
        for c in range(1, len(row)-1):
            count += is_xmas(r, c, rows)
    return count


def is_xmas(r, c, grid):
    """ Is there a X-MAS here? """

    if grid[r][c] != "A": return False

    # Check diagonal /
    d1 = True if grid[r+1][c-1] == "M" and grid[r-1][c+1] == "S" or grid[r+1][c-1] == "S" and grid[r-1][c+1] == "M" else False

    # Check diagonal \
    d2 = True if grid[r-1][c-1] == "M" and grid[r+1][c+1] == "S" or grid[r-1][c-1] == "S" and grid[r+1][c+1] == "M" else False

    return d1 and d2




def count_xmas(r, c, grid):
    """ Return how many XMAS-es it can find from this start position """

    count = 0
    if grid[r][c] != "X":
        return count

    # Search all 8 directions

    # To top
    if r >= 3 \
            and grid[r-1][c] == "M" \
            and grid[r-2][c] == "A" \
            and grid[r-3][c] == "S":
        count += 1

    # To botom
    if r <= len(grid)-4 \
            and grid[r+1][c] == "M" \
            and grid[r+2][c] == "A" \
            and grid[r+3][c] == "S":
        count += 1

    # To left
    if c >= 3 \
            and grid[r][c-1] == "M" \
            and grid[r][c-2] == "A" \
            and grid[r][c-3] == "S":
        count += 1

    # To right
    if c <= len(grid[r])-4 \
            and grid[r][c+1] == "M" \
            and grid[r][c+2] == "A" \
            and grid[r][c+3] == "S":
        count += 1

    # To top left
    if r >= 3 and c >= 3 \
            and grid[r-1][c-1] == "M" \
            and grid[r-2][c-2] == "A" \
            and grid[r-3][c-3] == "S":
        count += 1

    # To bottom left
    if r <= len(grid)-4 and c >= 3 \
            and grid[r+1][c-1] == "M" \
            and grid[r+2][c-2] == "A" \
            and grid[r+3][c-3] == "S":
        count += 1

    # To top right
    if r >= 3 and c <= len(grid[r])-4 \
            and grid[r-1][c+1] == "M" \
            and grid[r-2][c+2] == "A" \
            and grid[r-3][c+3] == "S":
        count += 1

    # To bottom right
    if r <= len(grid)-4 and c <= len(grid[r])-4 \
            and grid[r+1][c+1] == "M" \
            and grid[r+2][c+2] == "A" \
            and grid[r+3][c+3] == "S":
        count += 1

    return count


main()
