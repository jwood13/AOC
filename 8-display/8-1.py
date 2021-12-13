# https://adventofcode.com/2021/day/8

unique_digit_count = 0
unique_digit_lengths = [2,3,4,7]
with open('input.txt') as file:
    for line in file.readlines():
        all_strings, display_output = line.strip().split(' | ')
        print(display_output)
        for string in display_output.split(' '):
            print(string)
            if len(string) in unique_digit_lengths:
                unique_digit_count += 1

print(unique_digit_count)