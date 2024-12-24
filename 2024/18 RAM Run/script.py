from time import sleep
from copy import deepcopy
from sys import getrecursionlimit, setrecursionlimit
setrecursionlimit(1000000)
print(getrecursionlimit())


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part1(input))


def part1(input):
    memory_space_size = 71
    drop_bytes = 1024
    mem_space = Room(memory_space_size, memory_space_size, "Memory space", ".")
    for i, xy in enumerate(input.splitlines()):
        if i == drop_bytes:
            break
        x, y = list(map(int, xy.split(",")))
        mem_space.grid[y][x] = "#"

    mem_space.display()

    start = Position(0, 0)
    end = Position(memory_space_size-1, memory_space_size-1)
    solver = Solver(mem_space, start, end)
    solver.move()

    return solver.found


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Position({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented
        return self.x == other.x and self.y == other.y


class Room:
    def __init__(self, width: int, height: int, name="Room", default=None):
        self.width = width
        self.height = height
        self.name = name
        self.grid = [[default]*width for i in range(height)]
        self.boxes = []
        self.robots = []

    def __str__(self):
        return f"Room({self.name})"

    def look(self, pos: Position):
        if pos.x < 0 or pos.x >= self.width:
            return False
        if pos.y < 0 or pos.y >= self.height:
            return False
        return self.grid[pos.y][pos.x]

    def display(self, title="", dwell=.05, redraw=False, add_space=True):
        if redraw:
            print("\033[F"*(len(self.grid)+2))
        print(title)
        box_char = "["
        for row in self.grid:
            for space in row:
                if add_space:
                    space += " "
                print(space, end="")
            print()
        sleep(dwell)


class Movement:
    def __init__(self, movement: str):
        if movement in ["^", "Up"]:
            self.x = 0
            self.y = -1
        elif movement in ["v", "Down"]:
            self.x = 0
            self.y = 1
        elif movement in ["<", "Left"]:
            self.x = -1
            self.y = 0
        elif movement in [">", "Right"]:
            self.x = 1
            self.y = 0
        else:
            raise Exception("Incorrect movement")


class Solver:
    def __init__(self, room: Room, start: Position, target: Position):
        self.room = room
        self.target = target
        self.pos = start
        self.found = None

    def move(self, from_pos=None, step=0, visits=[]):
        if not from_pos:
            from_pos = self.pos

        visits = deepcopy(visits)
        visits.append(from_pos)

        if from_pos == self.target:
            print(f"Finish in {step}!")
            if not self.found or step < self.found:
                self.found = step
            return True

        found = False

        move = Movement("Right")
        right = Position(from_pos.x+move.x, from_pos.y+move.y)
        if right not in visits and self.room.look(right) == ".":
            if self.move(right, step+1, visits):
                found = True

        move = Movement("Down")
        down = Position(from_pos.x+move.x, from_pos.y+move.y)
        if down not in visits and self.room.look(down) == ".":
            if self.move(down, step+1, visits):
                found = True

        move = Movement("Left")
        left = Position(from_pos.x+move.x, from_pos.y+move.y)
        if left not in visits and self.room.look(left) == ".":
            if self.move(left, step+1, visits):
                found = True

        move = Movement("Up")
        up = Position(from_pos.x+move.x, from_pos.y+move.y)
        if up not in visits and self.room.look(up) == ".":
            if self.move(up, step+1, visits):
                found = True

        return found


main()
