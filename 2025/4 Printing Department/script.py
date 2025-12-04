import re


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def part1(input):
    grid = [list(line) for line in input.strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    accessible_count = 0
    
    # Directions for 8 neighbors (up, down, left, right, and 4 diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                # Count neighbors that are '@'
                neighbor_count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == '@':
                            neighbor_count += 1
                
                # Accessible if fewer than 4 neighbors are '@'
                if neighbor_count < 4:
                    accessible_count += 1
    
    return accessible_count


def part2(input):
    grid = [list(line) for line in input.strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Directions for 8 neighbors (up, down, left, right, and 4 diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    total_removed = 0
    
    while True:
        # Find all accessible rolls in this iteration
        to_remove = []
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    # Count neighbors that are '@'
                    neighbor_count = 0
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols:
                            if grid[ni][nj] == '@':
                                neighbor_count += 1
                    
                    # Accessible if fewer than 4 neighbors are '@'
                    if neighbor_count < 4:
                        to_remove.append((i, j))
        
        # If no rolls can be removed, we're done
        if len(to_remove) == 0:
            break
        
        # Remove the accessible rolls
        for i, j in to_remove:
            grid[i][j] = '.'
        
        total_removed += len(to_remove)
    
    return total_removed


main()
