import numpy as np


def print_frame(frame):
    string = ''

    for line in frame:
        string += '|'
        for pixel in line:
            if pixel:
                string += '#'
            else:
                string += '.'
        string += '|\n'
    print(string)


def next_pixel(frame, i, j, key):
    '''decide what the pixel should be in the next iteration'''
    key_number = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            y2 = i+y
            x2 = j+x
            if y2 < 0:
                y2 = 0
            elif y2 >= frame.shape[0]:
                y2 = frame.shape[0]-1
            if x2 < 0:
                x2 = 0
            elif x2 >= frame.shape[1]:
                x2 = frame.shape[1]-1
            bit = frame[y2, x2]
            exponent = 8 - (x+1) - (y+1)*3
            key_number += bit * 2**exponent
    return key[key_number]


iterations = 2
border_width = iterations + 1
with open('input.txt') as file:
    key = file.readline().strip()
    file.readline()
    initial_frame = file.readlines()
    height = len(initial_frame)
    width = len(initial_frame[0].strip())
    full_height = height + 2*(border_width)
    full_width = width + 2*(border_width)
    frame = np.zeros((full_height, full_width), dtype=bool)
    counter = 0
    for line in initial_frame:
        to_array = np.array([*line.strip()])
        frame[counter+border_width, border_width:border_width +
              width] = (to_array == '#')
        counter += 1

key_as_array = np.array([*key])
binary_key = key_as_array == '#'

print_frame([binary_key])
print_frame(frame)
for loop_count in range(iterations):
    new_frame = frame.copy()
    for i in range(0, full_height):
        for j in range(0, full_width):
            new_frame[i, j] = next_pixel(frame, i, j, binary_key)
    print_frame(new_frame)
    frame = new_frame
print(np.sum(frame))

# < 5613
