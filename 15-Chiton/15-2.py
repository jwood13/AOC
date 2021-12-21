import numpy as np


class point():
    coord = [0, 0]
    risk = 0

    def __init__(self, cave, coord=[0, 0], parent='', risk=0):
        self.parent = parent
        self.coord = coord
        self.risk = risk
        self.cave = cave
        self.bounds = cave.shape
        self.fitness = (self.bounds[0]-coord[0]) + \
            (self.bounds[1]-coord[1])

    def __repr__(self):
        return str(self.coord) + str(self.risk)

    def str(self):
        return str(self.coord)

    def generate_new_walkers(self):
        '''Generate new walkers in all 4 directions, covering for duplication, and revisitation'''
        directions = {'u': [self.coord[0], self.coord[1]-1], 'd': [self.coord[0], self.coord[1]+1],
                      'l': [self.coord[0]-1, self.coord[1]], 'r': [self.coord[0]+1, self.coord[1]]}
        new_walkers = []
        for coord in directions.values():
            if self.in_bounds(coord):
                # print('risk:', self.risk+self.cave[coord[0], coord[1]])
                new_walkers.append(
                    point(self.cave, coord, self.str(), self.risk+self.cave[coord[0], coord[1]]))
        return new_walkers

    def in_bounds(self, coord):
        '''Check if the coord would go out of bounds'''
        if coord[0] < 0 or coord[0] >= self.bounds[0] or coord[1] < 0 or coord[1] >= self.bounds[1]:
            return False
        else:
            return True

    def finished(self):
        coord = self.coord
        '''check to see if you've reached the end'''
        if coord == [self.cave.shape[0]-1, self.cave.shape[1]-1]:
            return True
        else:
            return False


def sort_key(x):
    '''sorting key function for the list'''
    return x.risk+x.fitness


def traceback(coordinate, closed):
    string = coordinate.str()
    while coordinate.str() != '[0, 0]':
        coordinate = closed[coordinate.parent]
        string = coordinate.str() + ", " + string
    return string


filename = 'input.txt'
with open(filename) as file:
    file_contents = file.readlines()
    height = len(file_contents)
    width = len(file_contents[0].strip())
    cave = np.ones((height, width), dtype=int)*10
    counter = 0
    for line in file_contents:
        cave[counter, :] = [int(x) for x in line.strip()]
        counter += 1
    goal = [width, height]

size_multiplier = 5
large_cave = np.ones(
    (height*size_multiplier, width*size_multiplier), dtype=int)
for row in range(size_multiplier):
    for column in range(size_multiplier):
        large_cave[column*width:(column+1)*width, row *
                   height:(row+1)*height] = (cave + (row+column))

full_height = size_multiplier * height
full_width = size_multiplier * width
for i in range(full_width):
    for j in range(full_height):
        if large_cave[i, j] > 9:
            large_cave[i, j] -= 9

reached = {}
start = point(large_cave)
to_check = {start.str(): start}
count = 0
finished = False
while not finished:
    # print(to_check.values())
    find_next = sorted(to_check.values(), key=sort_key)
    # print(find_next)
    next = find_next[0]
    if next.finished():
        finished = True
    to_check.pop(next.str())
    new_points = next.generate_new_walkers()
    reached[next.str()] = next
    for new in new_points:
        string_coord = new.str()
        if string_coord in reached.keys():
            if reached[string_coord].risk > new.risk:
                reached[string_coord] = new
        elif string_coord in to_check:
            if to_check[string_coord].risk > new.risk:
                to_check[string_coord] = new
        else:
            to_check[string_coord] = new
print(next, next.risk)
print(traceback(next, reached))
