import re


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    #print(part1(input))
    print(part2(input))


def part1(input):
    # Parse ranges from input (remove newlines and split by comma)
    ranges_str = input.replace('\n', '').strip()
    ranges = ranges_str.split(',')
    
    invalid_ids = []
    
    for range_str in ranges:
        if not range_str:
            continue
        start, end = map(int, range_str.split('-'))
        
        # Check each ID in the range
        for id_num in range(start, end + 1):
            id_str = str(id_num)
            
            # Invalid ID must have even number of digits
            if len(id_str) % 2 != 0:
                continue
            
            # Split in half and check if both halves are equal
            half_len = len(id_str) // 2
            first_half = id_str[:half_len]
            second_half = id_str[half_len:]
            
            if first_half == second_half:
                invalid_ids.append(id_num)
    
    return sum(invalid_ids)


def part2(input):
    # Parse ranges from input (remove newlines and split by comma)
    ranges_str = input.replace('\n', '').strip()
    ranges = ranges_str.split(',')
    
    invalid_ids = []
    
    for range_str in ranges:
        if not range_str:
            continue
        start, end = map(int, range_str.split('-'))
        
        # Check each ID in the range
        for id_num in range(start, end + 1):
            id_str = str(id_num)
            n = len(id_str)
            
            # Try all possible ways to split the number into k equal parts (k >= 2)
            is_invalid = False
            for k in range(2, n + 1):
                # Check if n is divisible by k
                if n % k != 0:
                    continue
                
                # Split into k parts
                part_len = n // k
                first_part = id_str[:part_len]
                
                # Check if all parts are equal
                all_equal = True
                for i in range(1, k):
                    part = id_str[i * part_len:(i + 1) * part_len]
                    if part != first_part:
                        all_equal = False
                        break
                
                if all_equal:
                    is_invalid = True
                    break
            
            if is_invalid:
                invalid_ids.append(id_num)
    
    return sum(invalid_ids)


main()
