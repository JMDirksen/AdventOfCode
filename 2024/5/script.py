import re


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part2(input))


def part1(input):
    rules, updates = input.split("\n\n")
    rules = rules.splitlines()
    updates = updates.splitlines()

    page_sum = 0
    for u in updates:
        u = u.split(",")
        if in_correct_order(u, rules):
            page_sum += middle_page(u)
    return page_sum


def part2(input):
    rules, updates = input.split("\n\n")
    rules = rules.splitlines()
    updates = updates.splitlines()

    page_sum = 0
    for u in updates:
        u = u.split(",")
        if not in_correct_order(u, rules):
            while not in_correct_order(u, rules):
                u = fix_order(u, rules)
            page_sum += middle_page(u)
    return page_sum


def fix_order(update, rules):
    for r in rules:
        x, y = r.split("|")
        if x in update and y in update:
            if update.index(x) > update.index(y):
                update.insert(update.index(y), update.pop(update.index(x)))
    return update

def middle_page(u):
    return int(u[int(len(u)/2)])


def in_correct_order(update, rules):
    for r in rules:
        x, y = r.split("|")
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


main()
