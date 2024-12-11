import re


def main():
    # inputfile = "example1.txt"
    # inputfile = "example2.txt"
    inputfile = "input.txt"
    with open(inputfile) as f:
        input = f.read()

    print(part2(input))


def part1(input):
    games = []
    for line in input.splitlines():
        picks = []
        for pick in line.split(": ", 1)[1].split("; "):
            match = re.search(r'(\d+) red', pick)
            reds = int(match.group(1)) if match else 0
            match = re.search(r'(\d+) green', pick)
            greens = int(match.group(1)) if match else 0
            match = re.search(r'(\d+) blue', pick)
            blues = int(match.group(1)) if match else 0
            pick = [reds, greens, blues]
            picks.append(pick)
        games.append(picks)
        print(picks)

    possible = 0
    for i in range(len(games)):
        id = i + 1
        max_rgb = [0, 0, 0]
        for pick in games[i]:
            for c in range(3):
                if pick[c] > max_rgb[c]:
                    max_rgb[c] = pick[c]
        if max_rgb[0] <= 12 and max_rgb[1] <= 13 and max_rgb[2] <= 14:
            possible += id
        print(id, max_rgb, possible)
    return possible


def part2(input):
    games = []
    for line in input.splitlines():
        picks = []
        for pick in line.split(": ", 1)[1].split("; "):
            match = re.search(r'(\d+) red', pick)
            reds = int(match.group(1)) if match else 0
            match = re.search(r'(\d+) green', pick)
            greens = int(match.group(1)) if match else 0
            match = re.search(r'(\d+) blue', pick)
            blues = int(match.group(1)) if match else 0
            pick = [reds, greens, blues]
            picks.append(pick)
        games.append(picks)
        print(picks)

    total_power = 0
    for i in range(len(games)):
        id = i + 1
        max_rgb = [0, 0, 0]
        for pick in games[i]:
            for c in range(3):
                if pick[c] > max_rgb[c]:
                    max_rgb[c] = pick[c]
        game_power = max_rgb[0] * max_rgb[1] * max_rgb[2]
        total_power += game_power
        print(id, max_rgb, game_power, total_power)
    return total_power


main()
