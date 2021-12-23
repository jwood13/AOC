import numpy as np


class Cube():
    def __init__(self, state, xs, ys, zs):
        self.state = True
        self.xs = xs
        self.x_min = min(xs)
        self.x_max = max(xs)
        self.ys = ys
        self.y_min = min(ys)
        self.y_max = max(ys)
        self.zs = zs
        self.z_min = min(zs)
        self.z_max = max(zs)
        self.init_volume = int(abs(np.diff(xs))+1) * int(abs(np.diff(ys))+1) * int(abs(np.diff(zs))+1)
        self.override_cubes = []
    
    def __repr__(self):
        return f"[{self.xs},{self.ys},{self.zs}] {self.get_active_volume()}"

    def add_over(self, nega_cube):
        vacancy = self.overlap_cube(nega_cube)
        if vacancy:
            for cube in self.override_cubes:
                cube.add_over(vacancy)
            self.override_cubes.append(vacancy)

    def overlap_cube(self, nega_cube):
        if self.x_min <= nega_cube.x_max:
            if self.x_max >= nega_cube.x_min:
                if self.y_min <= nega_cube.y_max:
                    if self.y_max >= nega_cube.y_min:
                        if self.z_min <= nega_cube.z_max:
                            if self.z_max >= nega_cube.z_min:
                                x_bounds = [max(self.x_min, nega_cube.x_min), min(
                                    self.x_max, nega_cube.x_max)]
                                y_bounds = [max(self.y_min, nega_cube.y_min), min(
                                    self.y_max, nega_cube.y_max)]
                                z_bounds = [max(self.z_min, nega_cube.z_min), min(
                                    self.z_max, nega_cube.z_max)]
                                overlap = Cube(False, x_bounds,
                                               y_bounds, z_bounds)
                                return overlap
        return None

    def get_active_volume(self):
        volume = self.init_volume
        for cut in self.override_cubes:
            volume -= cut.get_active_volume()
        return volume


on_cubes = []
for line in open('input.txt').readlines():
    command, coordinates = line.strip().split(' ')
    command = command == 'on'
    bounds = coordinates.split(',')
    xs = [int(x) for x in bounds[0][2:].split('..')]
    ys = [int(x) for x in bounds[1][2:].split('..')]
    zs = [int(x) for x in bounds[2][2:].split('..')]
    if command:
        on_cube = Cube(command, xs, ys, zs)
        for cube in on_cubes:
            cube.add_over(on_cube)
        on_cubes.append(on_cube)
    else:
        off_cube = Cube(command, xs, ys, zs)
        for cube in on_cubes:
            cube.add_over(off_cube)
print('-----')
on_volume = 0
for cube in on_cubes:
    print(cube)
    on_volume += cube.get_active_volume()
print(on_volume)
