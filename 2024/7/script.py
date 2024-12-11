import re


def main():
    inputfile = "example.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part1(input))


def part1(input):
    solve("6", ["2", "3", "1"])
    return

    for line in input.splitlines():
        answer, numbers = line.split(": ")
        numbers = numbers.split()

        solve(answer, numbers)

    return


def solve(answer, numbers):
    print(answer, numbers)
    operators = ["+", "*"]
    positions = len(numbers)-1
    posibilities = pow(len(operators), positions)
    print("Posibilities:", posibilities)
    for tries in range(posibilities):
        print("Try:", tries)
        oper_pos = tries % positions
        oper = tries % len(operators)

        for oper_pos in range(positions):
            print("Operant position:", oper_pos)
            oper = (tries+oper_pos) % len(operators)
            print("Operant:", operators[oper])            

    return


def get_oper(iter, positions, operators = ["+", "*"]):
    positions = positions*[0]
    for x in range(len(positions)):
        iter - 


    return



def part2(input):
    return


main()
