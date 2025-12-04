from math import nan
import re


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part1(input))
    print(part2(input))


def part1(input):
    input = input.splitlines()

    total_joltage = 0
    for bank in input:
        bank = list(bank)

        highest_digit_index1 = 0
        for i in range(len(bank[:-1])):
            if bank[i] > bank[highest_digit_index1]:
                highest_digit_index1 = i
        print(bank, bank[highest_digit_index1])

        start_index = highest_digit_index1+1
        highest_digit_index2 = start_index
        for i in range(start_index, len(bank)):
            if bank[i] > bank[highest_digit_index2]:
                highest_digit_index2 = i
        print(bank[start_index:], bank[highest_digit_index2])

        bank_joltage = int(bank[highest_digit_index1]+bank[highest_digit_index2])
        total_joltage += bank_joltage
        print(bank_joltage, total_joltage)    
    
    return total_joltage


def part2(input):
    input = input.splitlines()
    
    total_joltage = 0
    for bank in input:
        bank = list(bank)
        n = len(bank)
        k = 12  # We need to select exactly 12 digits
        
        # If the bank has exactly 12 digits, use all of them
        if n == k:
            joltage = int(''.join(bank))
            total_joltage += joltage
            continue
        
        # We need to remove (n - k) digits to keep the largest number
        # Use a greedy stack approach: keep larger digits, remove smaller ones when possible
        stack = []
        to_remove = n - k
        
        for digit in bank:
            # While we can still remove digits and the current digit is larger than the top of stack
            while to_remove > 0 and stack and stack[-1] < digit:
                stack.pop()
                to_remove -= 1
            stack.append(digit)
        
        # If we still need to remove more digits, remove from the end
        while to_remove > 0:
            stack.pop()
            to_remove -= 1
        
        # Form the number from the selected digits
        joltage = int(''.join(stack))
        total_joltage += joltage
    
    return total_joltage


main()
