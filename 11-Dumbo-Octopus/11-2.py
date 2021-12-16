import numpy as np
height = 12
width = 12
file = 'input.txt'
cave = np.zeros((height, width), dtype=int)
counter = 0
for line in open(file).readlines():
    cave[counter+1, 1:-1] = [int(x) for x in line.strip()]
    counter += 1
print(cave[1:height-1, 1:width-1])
flashed = np.zeros_like(cave, dtype=bool)


def flash(cave, i, j):
    for a in [i-1, i, i+1]:
        for b in [j-1, j, j+1]:
            cave[a, b] += 1


flashes = 0
simultaneous_flash = False
step = 0
while not simultaneous_flash:
    step += 1
    cave += 1
    flashed = np.zeros_like(cave, dtype=bool)
    check_again = True
    while check_again:
        check_again = False
        for i in range(1, height-1):
            for j in range(1, width-1):
                if cave[i, j] > 9 and not flashed[i, j]:
                    flash(cave, i, j)
                    flashed[i, j] = True
                    check_again = True
                    flashes += 1
    print(np.sum(flashed))
    if np.sum(flashed) == (width-2)*(height-2):
        simultaneous_flash = True
    for i in range(height):
        for j in range(width):
            if cave[i, j] > 9:
                cave[i, j] = 0
print(cave[1:height-1, 1:width-1])
print(flashes)
print(step)
