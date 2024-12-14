import re


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part2(input))


def part1(input):
    # Setup machines
    machines = []
    for line in input.splitlines():
        if line.startswith("Button A"):
            bax, bay = re.search(r'X\+(\d+), Y\+(\d+)', line).groups()
        elif line.startswith("Button B"):
            bbx, bby = re.search(r'X\+(\d+), Y\+(\d+)', line).groups()
        elif line.startswith("Prize"):
            px, py = re.search(r'X=(\d+), Y=(\d+)', line).groups()
            machines.append(Machine(Pos(bax, bay), Pos(bbx, bby), Pos(px, py)))

    cost = 0
    for m, machine in enumerate(machines):
        wins = machine.wins()
        for win in wins:
            print(m, win[0], win[1], win[2])
            cost += win[2]

    return cost


def part2(input):
    # Setup machines
    machines = []
    for line in input.splitlines():
        if line.startswith("Button A"):
            bax, bay = re.search(r'X\+(\d+), Y\+(\d+)', line).groups()
        elif line.startswith("Button B"):
            bbx, bby = re.search(r'X\+(\d+), Y\+(\d+)', line).groups()
        elif line.startswith("Prize"):
            px, py = re.search(r'X=(\d+), Y=(\d+)', line).groups()
            px = int(px) + 10000000000000
            py = int(py) + 10000000000000
            name = str(len(machines)+1)
            machines.append(Machine(Pos(bax, bay), Pos(bbx, bby), Pos(px, py), name))

    cost = 0
    for machine in machines:
        win_cost = machine.win_cost()
        if win_cost:
            cost += win_cost

    return cost


class Pos:
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def __eq__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return self.x == other.x and self.y == other.y


class Machine:
    def __init__(self, button_a: Pos, button_b: Pos, prize: Pos, name=None):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize
        self.name = name

    def win_cost(self):
        wins = self.wins()
        wins.sort(key=lambda wins: wins[2])
        if not wins:
            return None
        return wins[0][2]

    def wins(self):
        wins = []

        a = 0
        while True:
            a += 1
            if a * self.button_a.x > self.prize.x:
                break
            if a * self.button_a.y > self.prize.y:
                break
            b = 0
            while True:
                b += 1
                if b * self.button_b.x > self.prize.x:
                    break
                if b * self.button_b.y > self.prize.y:
                    break
                pos = Pos(a * self.button_a.x + b * self.button_b.x,
                          a * self.button_a.y + b * self.button_b.y)
                if pos == self.prize:
                    cost = a*3 + b*1
                    wins.append([a, b, cost])
                    print(f"Machine {self.name} wins {len(wins)}")
        return wins


main()
