import re
import json


def main():
    # inputfile = "example.txt"
    inputfile = "input.txt"
    with open(inputfile) as f:
        input = f.read()

    print(part2(input))


def part1(input):
    lines = input.splitlines()
    safe = 0
    for r in range(len(lines)):
        report = list(map(int, lines[r].split()))
        print(f"Report {r}", report)
        is_safe = True
        for i in range(len(report)):
            if i == 0:
                increasing = report[1] > report[0]
                continue
            if (report[i] > report[i-1]) != increasing:
                is_safe = False
            if abs(report[i]-report[i-1]) < 1:
                is_safe = False
            if abs(report[i]-report[i-1]) > 3:
                is_safe = False
        print(f"Report {r} is safe = {is_safe}")
        if is_safe:
            safe += 1
    return safe


def part2(input):
    lines = input.splitlines()
    safe_count = 0
    for r in range(len(lines)):
        report = list(map(int, lines[r].split()))
        safe = is_safe(report)
        print(f"{r} {safe} {report}")
        if safe:
            safe_count += 1
    return safe_count


def is_safe(report):
    for skip in range(len(report)):
        test_report = [x for i, x in enumerate(report) if i != skip]
        safe = True
        for i in range(len(test_report)):
            if i == 0:
                increasing = test_report[1] > test_report[0]
                continue
            if (test_report[i] > test_report[i-1]) != increasing:
                safe = False
            elif abs(test_report[i]-test_report[i-1]) < 1:
                safe = False
            elif abs(test_report[i]-test_report[i-1]) > 3:
                safe = False
        if safe:
            return True
    return False


main()
