def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part1(input))


def part1(input):
    # Setup garden
    garden = []
    for r, row in enumerate(input.splitlines()):
        for c, plant in enumerate(list(row)):
            garden.append(Plot(garden, Pos(r, c), plant))

    # Identify regions
    id = 0
    regions = []
    for plot in garden:
        if plot.region == None:
            ident_region(id, plot)
            regions.append(Region(garden, id))
            id += 1

    # Iterate regions
    price = 0
    for region in regions:
        price += region.price()

    return price


class Pos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


    def __eq__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return self.x == other.x and self.y == other.y


class Plot:
    def __init__(self, garden: list, pos: Pos, plant: str):
        self.garden = garden
        self.pos = pos
        self.plant = plant
        self.region = None


    def neighbours(self):
        north = Pos(self.pos.x-1, self.pos.y)
        south = Pos(self.pos.x+1, self.pos.y)
        west = Pos(self.pos.x, self.pos.y-1)
        east = Pos(self.pos.x, self.pos.y+1)
        neighbours = []
        for plot in self.garden:
            if plot.pos in [north, south, west, east]:
                neighbours.append(plot)
        return neighbours


    def perimeter(self):
        count = 4
        for nb in self.neighbours():
            if nb.plant == self.plant:
                count -= 1
        return count


class Region:
    def __init__(self, garden:list, id: int):
        self.garden = garden
        self.id = id


    def plots(self):
        plots = []
        for plot in self.garden:
            if plot.region == self.id:
                plots.append(plot)
        return plots


    def area(self):
        count = 0
        for plot in self.garden:
            if plot.region == self.id:
                count += 1
        return count
    

    def perimeter(self):
        count = 0
        for plot in self.plots():
            count += plot.perimeter()
        return count
    

    def price(self):
        return self.area()*self.perimeter()


def part2(input):
    return


def ident_region(id: int, plot: Plot):
    if plot.region != None:
        return

    # Set region id
    plot.region = id

    # Check neighbouring plots
    for nb in plot.neighbours():
        if nb.region == None and nb.plant == plot.plant:
            ident_region(id, nb)


main()
