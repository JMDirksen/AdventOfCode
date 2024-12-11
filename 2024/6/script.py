import re


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part2(input))


def part1(input):
    # Get map
    lab = list(map(list, input.splitlines()))
    # Get position/direction
    pos = get_position(lab)
    dir = 0
    lab[pos[0]][pos[1]] = "X"

    target = get_target(pos, dir, lab)
    while target:
        # show_lab(lab)
        # Look
        in_front = lab[target[0]][target[1]]
        # Turn?
        if in_front == "#":
            dir = turn(dir)
            target = get_target(pos, dir, lab)
        # Move
        pos = target
        lab[pos[0]][pos[1]] = "X"
        # Get new target
        target = get_target(pos, dir, lab)

    show_lab(lab)
    return count_visits(lab)


def part2(input):
    # Get map
    lab = list(map(list, input.splitlines()))
    # Get position/direction
    pos = get_position(lab)
    dir = 0
    arrow = ["^", ">", "v", "<"]

    count_obstructs = 0
    target = get_target(pos, dir, lab)
    while target:
        # Look
        in_front = lab[target[0]][target[1]]
        # Turn?
        if in_front == "#":
            dir = turn(dir)
            target = get_target(pos, dir, lab)
            continue
        # Possible obstruction place ahead?
        if obstruct_causes_loop(pos, dir, lab):
            obstruct = get_target(pos, dir, lab)
            if obstruct and lab[obstruct[0]][obstruct[1]] == ".":
                print(obstruct)
                #show_lab(lab)
                count_obstructs += 1
        lab[pos[0]][pos[1]] += arrow[dir]
        # Move
        pos = target
        # Get new target
        target = get_target(pos, dir, lab)
        print("New pos/dir/target:", pos, dir, target)
    lab[pos[0]][pos[1]] = arrow[dir]

    return count_obstructs


def obstruct_causes_loop(pos, dir, grid):
    arrow = ["^", ">", "v", "<"]
    right_dir = turn(dir)
    next = get_target(pos, right_dir, grid)
    while next:
        if "#" in grid[next[0]][next[1]]:
            right_dir = turn(right_dir)
            next = get_target(pos, right_dir, grid)
            continue
        if arrow[right_dir] in grid[next[0]][next[1]]: return True
        pos = next
        next = get_target(pos, right_dir, grid)
        print(".", next, end="")
    return False


def count_visits(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "X":
                count += 1
    return count


def show_lab(lab):
    for r in lab:
        print(" ".join(r))
    print()


def turn(dir):
    return 0 if dir >= 3 else dir + 1


def get_target(pos, dir, grid, step = 1):
    target = []
    match dir:
        case 0: target = pos[0]-step, pos[1]
        case 1: target = pos[0], pos[1]+step
        case 2: target = pos[0]+step, pos[1]
        case 3: target = pos[0], pos[1]-step
    if is_on_grid(target, grid):
        return target
    else:
        return False


def is_on_grid(pos, grid):
    rows = len(grid)
    cols = len(grid[0])
    if pos[0] < 0 or pos[0] >= rows:
        return False
    if pos[1] < 0 or pos[1] >= cols:
        return False
    return True


def get_position(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "^":
                return r, c


main()
