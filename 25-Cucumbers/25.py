import numpy as np

lines =  open('input.txt').readlines()
height = len(lines)
width = len(lines[0].strip())
floor = np.full((height,width),'.')
moved = np.zeros_like(floor,dtype=bool)
count = 0
for line in lines:
    floor[count,:] = np.array([*line.strip()])

    count += 1
step_count = 0
move_count = 1
print(floor)
while move_count > 0:
    move_count = 0
    step_count += 1
    moved[:,:] = False
    for i in range(height):
        for j in range(width):
            if floor[i, j] == '>' and not moved[i,j]:
                if j+1 == width:
                    move_index = 0
                else:
                    move_index = j + 1
                if floor[i, move_index] == '.' and not moved[i, move_index]:
                    move_count += 1
                    floor[i, j] = '.'
                    floor[i, move_index] = '>'
                    moved[i, move_index] = True
                    moved[i,j] = True
    moved[:,:] = False
    for i in range(height):
        for j in range(width):
            if floor[i, j] == 'v' and not moved[i,j]:
                if i+1 == height:
                    move_index = 0
                else:
                    move_index = i + 1
                if floor[move_index, j] == '.'and not moved[move_index, j]:
                    move_count += 1
                    floor[i, j] = '.'
                    floor[move_index,j] = 'v'
                    moved[move_index,j] = True
                    moved[i,j] = True
    print(step_count)
    # print(floor)

print(floor)
print(step_count)
