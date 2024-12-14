import re
from os import system
from time import sleep


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part1(input))


def part1(input):
    # Room
    bathroom = Room(101, 103)

    # Add robots
    for line in input.splitlines():
        r = "p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
        posX, posY, velX, velY = re.search(r, line).groups()
        pos = Position(int(posX), int(posY))
        vel = Velocity(int(velX), int(velY))
        robot = Robot(bathroom, pos, vel)
        bathroom.robots.append(robot)

    # Move
    f = open("output.txt", "w")
    for sec in range(10000):
        for robot in bathroom.robots:
            robot.move()
        print(sec+1)
        f.write(bathroom.get_image(sec+1))
        # if sec+1 > 580:
        # bathroom.display(sec+1, 0.1)

        # if sec == 45: sleep(5)

    return  # bathroom.safety_factor()


def part2(input):
    return


class Room:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.robots = []
        self.grid = [[0]*width for i in range(height)]

    def safety_factor(self):
        # Count robots in quadrants
        qA = qB = qC = qD = 0
        for robot in self.robots:
            if robot.pos.x < self.width//2:
                if robot.pos.y < self.height//2:
                    qA += 1
                elif robot.pos.y > self.height//2:
                    qC += 1
            elif robot.pos.x > self.width//2:
                if robot.pos.y < self.height//2:
                    qB += 1
                elif robot.pos.y > self.height//2:
                    qD += 1

        return qA * qB * qC * qD

    def display(self, title: str, dwell=.25):
        self.count()
        # system('cls')
        print()
        print()
        print()
        print(title)
        print()
        for y in range(self.height):
            for x in range(self.width):
                char = "  "
                if self.grid[y][x] > 0:
                    char = "# "
                print(char, end="")
            print()
        print()
        sleep(dwell)

    def get_image(self, title: str):
        self.count()
        lines = [f"\n{title}\n\n"]
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                char = "  "
                if self.grid[y][x] > 0:
                    char = "# "
                line += char
            lines.append(line)
        return "\n".join(lines)

    def count(self):
        self.grid = [[0]*self.width for i in range(self.height)]
        for robot in self.robots:
            self.grid[robot.pos.y][robot.pos.x] += 1


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented
        return self.x == other.x and self.y == other.y


class Velocity:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Velocity):
            return NotImplemented
        return self.x == other.x and self.y == other.y


class Robot:
    def __init__(self, room: Room, pos: Position, vel: Velocity):
        self.room = room
        self.pos = pos
        self.vel = vel

    def move(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        if self.pos.x >= self.room.width:
            self.pos.x -= self.room.width
        if self.pos.y >= self.room.height:
            self.pos.y -= self.room.height
        if self.pos.x < 0:
            self.pos.x += self.room.width
        if self.pos.y < 0:
            self.pos.y += self.room.height


main()
