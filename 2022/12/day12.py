import copy
from datetime import datetime

shortestPath = 500
end = [0, 0]
tries = 0


def main():
    global end
    print(datetime.now())

    # Read file lines
    lines = open('input.txt', 'r').readlines()

    # Build map array
    map = []
    for line in lines:
        map.append(list(line.strip('\n')))

    # Find start position
    for r, val in enumerate(map):
        if 'S' in val:
            c = val.index('S')
            break
    start = [r, c]
    map[start[0]][start[1]] = 'a'

    # Find end position
    for r, val in enumerate(map):
        if 'E' in val:
            c = val.index('E')
            break
    end = [r, c]

    # Solve
    solve(map, start, 0)


def solve(map, pos, steps):
    global shortestPath, tries
    tries += 1
    if tries % 1000 == 0:
        print('try:', tries)
        printMap(map, steps)

    # Limit search to shortest path already found
    if steps >= shortestPath:
        return

    #printMap(map, steps)
    hight = map[pos[0]][pos[1]]

    # Check solved
    if hight == 'E':
        print('Solved in:', steps, datetime.now())
        if steps < shortestPath:
            shortestPath = steps
        return

    # Best direction
    dY = end[0] - pos[0]
    dX = end[1] - pos[1]
    if abs(dX) >= abs(dY):
        if dX >= 0 and dY >= 0:
            #direction = ['>', 'V', '^', '<']
            direction = ['>', 'V', '^']
        elif dX >= 0 and dY <= 0:
            #direction = ['>', '^', 'V', '<']
            direction = ['>', '^', 'V']
        elif dX <= 0 and dY >= 0:
            #direction = ['<', 'V', '^', '>']
            direction = ['<', 'V', '^']
        else:
            #direction = ['<', '^', 'V', '>']
            direction = ['<', '^', 'V']
    else:
        if dY >= 0 and dX >= 0:
            #direction = ['V', '>', '<', '^']
            direction = ['V', '>', '<']
        elif dY >= 0 and dX <= 0:
            #direction = ['V', '<', '>', '^']
            direction = ['V', '<', '>']
        elif dY <= 0 and dX >= 0:
            #direction = ['^', '>', '<', 'V']
            direction = ['^', '>', '<']
        else:
            #direction = ['^', '<', '>', 'V']
            direction = ['^', '<', '>']

    for d in direction:
        # Check direction
        if d == '^':
            targetPos = [pos[0]-1, pos[1]]
        elif d == '>':
            targetPos = [pos[0], pos[1]+1]
        elif d == 'V':
            targetPos = [pos[0]+1, pos[1]]
        elif d == '<':
            targetPos = [pos[0], pos[1]-1]
        # Check negative grid pos
        if targetPos[0] < 0 or targetPos[1] < 0:
            continue
        # Get target hight / check grid out of bound
        try:
            targetHight = map[targetPos[0]][targetPos[1]]
        except IndexError:
            continue
        # Check if valid target
        validChar = targetHight.replace('E', 'z').islower()
        if not validChar:
            continue
        climb = (ord(targetHight.replace('E', 'z')) - ord(hight))
        if not 0 <= climb <= 1:
            continue
        newMap = copy.deepcopy(map)
        newMap[pos[0]][pos[1]] = d
        solve(newMap, targetPos, steps+1)


def printMap(map, step):
    print(step, '/', shortestPath)
    for row in map:
        print(''.join(row))
    print()


if __name__ == "__main__":
    main()
