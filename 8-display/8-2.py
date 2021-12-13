# https://adventofcode.com/2021/day/8

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

# This could probably be done easier with binary operators

def sort_code(code):
    return "".join(sorted(code))

def in_a_not_in_b(a,b):
    ''' returns characters in string a not in string b
    '''
    output = ''
    for char in a:
        if not char in b:
            output += char
    return output

def make_key(all_strings):
    ''' Take the list of 10 unique display outputs and return a dictionary map to identify the character
    '''
    number_translation = {}
    length_5 = []
    length_6 = []
    # Separate by length
    for code in all_strings:
        sorted_code = sort_code(code)
        if len(sorted_code) == 2:
            number_translation[1] = sorted_code
        elif len(sorted_code) == 3:
            number_translation[7] = sorted_code
        elif len(sorted_code) == 4:
            number_translation[4] = sorted_code
        elif len(sorted_code) == 5:
            length_5.append(sorted_code)
        elif len(sorted_code) == 6:
            length_6.append(sorted_code)
        elif len(sorted_code) == 7:
            number_translation[8] = sorted_code
    # Find 6 by length 6, but doesn't cover 1
    for code in length_6:
        if in_a_not_in_b(number_translation[1],code) != '':
            number_translation[6] = code
            length_6.remove(code)
    # Find 3 by length 5 and does cover 1
    for code in length_5:
        if in_a_not_in_b(number_translation[1],code) == '':
            number_translation[3] = code
            length_5.remove(code)
    # separate 2 and 5 by whether they are covered by 6
    for code in length_5:
        if in_a_not_in_b(code,number_translation[6]) == '':
            number_translation[5] = code
        else:
            number_translation[2] = code
    # separate 0 and 9 by whether they cover 4
    for code in length_6:
        if in_a_not_in_b(number_translation[4],code) == '':
            number_translation[9] = code
        else:
            number_translation[0] = code
    # Invert dictionary
    code_translation = {key:value for value,key in number_translation.items()}
    return code_translation


def translate_number(code,key):
    '''Sorts the code for uniqueness, and looks in dictionary
    '''
    return key[sort_code(code)]


unique_digit_count = 0
unique_digit_lengths = [2,3,4,7]
with open('input.txt') as file:
    output = 0
    for line in file.readlines():
        all_strings, display_output = line.strip().split(' | ')
        key = make_key(all_strings.split(' '))
        codes = display_output.split(' ')
        for i in range(len(codes)):
            output += 10**(3-i)*translate_number(codes[i],key)

print(output)