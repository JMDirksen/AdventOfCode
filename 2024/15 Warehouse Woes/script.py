from time import sleep


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part2(input))


def part1(input):
    # Room
    grid = []
    for line in input.splitlines():
        if not line.startswith("#"):
            break
        grid.append(list(line))
    room = Room(len(grid[0]), len(grid), "Warehouse")

    # Fill room
    for r, row in enumerate(grid):
        for c, column in enumerate(row):
            if column == "#":
                room.grid[r][c] = "#"
            elif column == "O":
                box = Box(room, Position(c, r))
                room.boxes.append(box)
                room.grid[r][c] = box
            elif column == "@":
                robot = Robot(room, Position(c, r))
                room.robots.append(robot)
                room.grid[r][c] = robot

    # Movements
    movements = ""
    for line in input.splitlines():
        if line.startswith("#"):
            continue
        movements += line
    movements = list(map(Movement, list(movements)))

    # Iterate movements
    room.display("0%")
    for m, move in enumerate(movements):
        robot.move(move)
        if m % 100 == 0:
            percent = int((m+1)/len(movements)*100)
            title = f"{percent}%"
            room.display(title, redraw=True, dwell=0)

    # GPS sum
    gps_sum = 0
    for box in room.boxes:
        gps_sum += box.pos.gps()

    return gps_sum


def part2(input):
    # Room
    grid = []
    for line in input.splitlines():
        if not line.startswith("#"):
            break
        grid_line = []
        for c in list(line):
            if c == "#":
                grid_line.extend(["#", "#"])
            elif c == "O":
                grid_line.extend(["[", "]"])
            elif c == ".":
                grid_line.extend([".", "."])
            elif c == "@":
                grid_line.extend(["@", "."])
        grid.append(grid_line)
    room = Room(len(grid[0]), len(grid), "Warehouse2")

    # Fill room
    for r, row in enumerate(grid):
        for c, column in enumerate(row):
            if column == "#":
                room.grid[r][c] = "#"
            elif column == "[":
                box = Box(room, Position(c, r), 2)
                room.boxes.append(box)
                room.grid[r][c] = box
            elif column == "]":
                room.grid[r][c] = box
            elif column == "@":
                robot = Robot(room, Position(c, r))
                room.robots.append(robot)
                room.grid[r][c] = robot

    # Movements
    movements = ""
    for line in input.splitlines():
        if line.startswith("#"):
            continue
        movements += line
    movements = list(map(Movement, list(movements)))

    # Iterate movements
    room.display("0%")
    for m, move in enumerate(movements):
        robot.move(move)
        if m % 100 == 0:
            percent = int((m+1)/len(movements)*100)
            title = f"{percent}%"
            room.display(title, redraw=True, dwell=0)

    # GPS sum
    gps_sum = 0
    for box in room.boxes:
        gps_sum += box.pos.gps()

    return gps_sum


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

    def gps(self) -> int:
        return 100 * self.y + self.x


class Room:
    def __init__(self, width: int, height: int, name="room"):
        self.width = width
        self.height = height
        self.name = name
        self.grid = [[None]*width for i in range(height)]
        self.boxes = []
        self.robots = []

    def __str__(self):
        return f"Room({self.name})"

    def look(self, pos: Position):
        return self.grid[pos.y][pos.x]

    def display(self, title="", dwell=.05, redraw=False):
        if redraw:
            print("\033[F"*(len(self.grid)+2))
        print(title)
        box_char = "["
        for row in self.grid:
            for space in row:
                if isinstance(space, Robot):
                    char = "@"
                elif isinstance(space, Box):
                    char = box_char
                    if box_char == "[":
                        box_char = "]"
                    else:
                        box_char = "["
                elif space == "#":
                    char = "#"
                else:
                    char = "."
                print(char, end="")
            print()
        sleep(dwell)


class Movement:
    def __init__(self, movement: str):
        if movement == "^":
            self.x = 0
            self.y = -1
        elif movement == "v":
            self.x = 0
            self.y = 1
        elif movement == "<":
            self.x = -1
            self.y = 0
        elif movement == ">":
            self.x = 1
            self.y = 0
        else:
            raise Exception("Incorrect movement")


class Robot:
    def __init__(self, room: Room, pos: Position):
        self.room = room
        self.pos = pos

    def move(self, move: Movement) -> bool:
        new_pos = Position(self.pos.x + move.x, self.pos.y + move.y)
        at_pos = self.room.look(new_pos)
        if at_pos == None:
            self.move_to(new_pos)
            return True
        elif isinstance(at_pos, Box):
            if at_pos.push(move):
                self.move_to(new_pos)
                return True
            else:
                return False
        else:
            return False

    def move_to(self, new_pos: Position):
        old_pos = self.pos
        self.pos = new_pos
        self.room.grid[old_pos.y][old_pos.x] = None
        self.room.grid[new_pos.y][new_pos.x] = self


class Box:
    def __init__(self, room: Room, pos: Position, width=1):
        self.room = room
        self.pos = pos
        self.width = width

    def __str__(self):
        return f"Box({self.room}, {self.pos})"

    def push(self, move: Movement) -> bool:
        new_pos_list = []
        at_pos_list = []
        for w in range(self.width):
            new_pos_list.append(
                Position(self.pos.x + move.x + w, self.pos.y + move.y))
            at_pos_list.append(self.room.look(new_pos_list[w]))

        if all(at_pos == None for at_pos in at_pos_list):
            self.move_to(new_pos_list[0])
            return True
        elif any(at_pos == "#" for at_pos in at_pos_list):
            return False

        can_move = True
        for at_pos in at_pos_list:
            if isinstance(at_pos, Box) and at_pos != self and not at_pos.can_push(move):
                can_move = False
                break
        if can_move:
            for pos in new_pos_list:
                if isinstance(self.room.look(pos), Box) and self.room.look(pos) != self:
                    self.room.look(pos).push(move)
            self.move_to(new_pos_list[0])
            return True
        else:
            return False

    def can_push(self, move: Movement) -> bool:
        new_pos_list = []
        at_pos_list = []
        for w in range(self.width):
            new_pos_list.append(
                Position(self.pos.x + move.x + w, self.pos.y + move.y))
            at_pos_list.append(self.room.look(new_pos_list[w]))

        if all(at_pos == None for at_pos in at_pos_list):
            return True

        if any(at_pos == "#" for at_pos in at_pos_list):
            return False

        for at_pos in at_pos_list:
            if isinstance(at_pos, Box) and at_pos != self and not at_pos.can_push(move):
                return False

        return True

    def move_to(self, new_pos: Position):
        old_pos = self.pos
        self.pos = new_pos
        for w in range(self.width):
            self.room.grid[old_pos.y][old_pos.x + w] = None
        for w in range(self.width):
            self.room.grid[new_pos.y][new_pos.x + w] = self


main()
