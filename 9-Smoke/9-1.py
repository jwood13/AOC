import numpy as np
height = 102
width = 102
file = 'input.txt'
cave = np.ones((height,width),dtype=int)*9
counter = 0
for line in open(file).readlines():
    cave[counter+1,1:-1] = [int(x) for x in line.strip()]
    counter += 1
print(cave)

def is_minimum(cave,i,j):
    lowpoint = True
    coords = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    for coord in coords:
        if cave[i,j] >= cave[coord[0],coord[1]] :
            lowpoint = False
    return lowpoint

threat_level = 0
for i in range(1,height-1):
    for j in range(1,width-1):
        if is_minimum(cave,i,j):
            print(i,j,cave[i,j])
            threat_level += 1 + cave[i,j]

print(threat_level)

# wrong <1528 - bad calculation at flat spots
# wrong <1465
# wrong 451 - index -1 gives reverse lookup, not error