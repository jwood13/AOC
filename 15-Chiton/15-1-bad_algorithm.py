import numpy as np


class walker():
    history = 's'
    coordinate = [0, 0]
    risk = 0

    def __init__(self, cave, coordinate=[0, 0], history=[], risk=0):
        self.history = history
        self.history.append(coordinate)
        self.coordinate = coordinate
        self.risk = risk
        self.cave = cave
        self.bounds = cave.shape
        self.fitness = (self.bounds[0]-coordinate[0]) + \
            (self.bounds[1]-coordinate[1])

    def __repr__(self):
        return str(self.history)+str(self.risk)

    def generate_new_walkers(self):
        '''Generate new walkers in all 4 directions, covering for duplication, and revisitation'''
        directions = {'u': [self.coordinate[0], self.coordinate[1]-1], 'd': [self.coordinate[0], self.coordinate[1]+1],
                      'l': [self.coordinate[0]-1, self.coordinate[1]], 'r': [self.coordinate[0]+1, self.coordinate[1]]}
        opposites = {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}
        new_walkers = []
        for dir, coordinate in directions.items():
            if coordinate not in self.history:
                if self.in_bounds(coordinate):
                    new_walkers.append(
                        walker(self.cave, coordinate, self.history.copy(), self.risk+cave[coordinate[0], coordinate[1]]))
        return new_walkers

    def in_bounds(self, coord):
        '''Check if the coordinate would go out of bounds'''
        if coord[0] < 0 or coord[0] >= self.bounds[0] or coord[1] < 0 or coord[1] >= self.bounds[1]:
            return False
        else:
            return True

    def finished(self):
        coord = self.coordinate
        '''check to see if you've reached the end'''
        if coord == [self.cave.shape[0]-1, self.cave.shape[1]-1]:
            return True
        else:
            return False


def sort_key(x):
    '''sorting key function for the list'''
    return x.risk+x.fitness


filename = 'sinput.txt'
with open(filename) as file:
    file_contents = file.readlines()
    height = len(file_contents)
    width = len(file_contents[0].strip())
    cave = np.ones((height, width), dtype=int)*10
    for line in file_contents:
        counter = 0
        cave[counter, :] = [int(x) for x in line.strip()]
        counter += 1
    goal = [width, height]

walkers = [walker(cave)]
count = 0
while not walkers[0].finished():
    expanding = walkers.pop(0)
    new_walkers = expanding.generate_new_walkers()
    for new in new_walkers:
        walkers.append(new)
    # print(walkers)
    walkers.sort(key=sort_key)
    # for w in walkers:
    #     (print(sort_key(w)))
    count += 1
    print(count)

print(walkers[0], walkers[0].risk)
