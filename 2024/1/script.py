import re
import json


def main():
    # inputfile = "example1.txt"
    inputfile = "example2.txt"
    inputfile = "input.txt"
    with open(inputfile) as f:
        input = f.read()

    print(part2(input))


def part1(input):
    lines = input.splitlines()
    list1 = []
    list2 = []
    diff = []
    for line in lines:
        list1_item, list2_item = line.split()
        list1 += [int(list1_item)]
        list2 += [int(list2_item)]
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        diff += [abs(list1[i]-list2[i])]
    print(list1, list2, diff)
    return sum(diff)


def part2(input):
    lines = input.splitlines()
    list1 = []
    list2 = []
    for line in lines:
        list1_item, list2_item = line.split()
        list1 += [int(list1_item)]
        list2 += [int(list2_item)]
    
    similarity_score = 0
    for i in range(len(list1)):
        count = list2.count(list1[i])
        similarity_score += list1[i] * count
        print(list1[i], count, similarity_score)
    return similarity_score


main()
