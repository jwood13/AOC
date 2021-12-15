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

def get_basin_points(cave,point):
    i=point[0]
    j=point[1]
    basin_points = []
    coords = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    for coord in coords:
        if cave[coord[0],coord[1]] != 9:
            basin_points.append((coord[0],coord[1]))
    return basin_points

low_points = []
for i in range(1,height-1):
    for j in range(1,width-1):
        if is_minimum(cave,i,j):
            low_points.append((i,j))

basin_sizes = []
for minimum in low_points:
    size = 1
    basin_points=[minimum]
    for point in basin_points:
        new_points = get_basin_points(cave,point)
        for a in new_points:
            if a not in basin_points:
                basin_points.append(a)
    basin_sizes.append(len(basin_points))
basin_sizes.sort()
print(basin_sizes)
print(basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3])
