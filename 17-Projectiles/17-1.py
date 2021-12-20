import math

test_cases = [(20, 30, -10, -5, 7, 2, True), (20, 30, -10, -5,
                                              6, 3, True), (20, 30, -10, -5,
                                              6, 9, True), (20, 30, -10, -5, 17, 4, False)]


class projectile():

    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.x = 0
        self.y = 0
    max_height = 0

    def __repr__(self):
        return f'probe: ({self.x},{self.y}) vel: ({self.dx},{self.dy}) {self.max_height}'

    def step(self, steps=1):
        '''Move the projectile'''
        for i in range(steps):
            self.x += self.dx
            self.y += self.dy
            self.dy -= 1
            if self.dx > 0:
                self.dx -= 1
            if self.y > self.max_height:
                self.max_height = self.y


def check_hit(projectile, limits):
    if projectile.x >= min(limits[:2]) and projectile.x <= max(limits[:2]) and projectile.y <= max(limits[2:]) and projectile.y >= min(limits[2:]):
        return True
    else:
        return False


def check_if_possible(projectile, limits):
    if projectile.x > max(limits[:2]) or (projectile.x < min(limits[:2]) and projectile.dx == 0):
        return False
    elif projectile.y < min(limits[2:]):
        return False
    else:
        return True


def max_dist(dy):
    return (dy*dy+dy)/2


def ydist(dy, step):
    return dy*step-step*step/2


def xdist(dx, step):
    if step > dx:
        return (dx*dx+dx)/2
    else:
        return dx*step-step*step/2


def run_trajectory(probe, limits):
    possible = True
    while possible:
        probe.step()
        if check_hit(probe, limits):
            return True
        elif not check_if_possible(probe, limits):
            return False


for i in test_cases:
    limits = i[:4]
    probe = projectile(i[4], i[5])
    result = run_trajectory(probe, limits)
    print(probe,result)
    assert(result == i[6])


input = open('input.txt').readline().strip().split(' ')
xlims = input[2]
x1, x2 = [int(x) for x in xlims[2:-1].split('..')]
ylims = input[3]
y1, y2 = [int(y) for y in ylims[2:].split('..')]
limits = [x1, x2, y1, y2]

dy = -min(limits[2:])-1
print(limits)
dx_min = int(math.sqrt(min(x1, x2)))
while dy > 0:
    dx_max = int(max(x1, x2)/dy+dy/2)
    max_height = max_dist(dy)
    for dx in range(dx_min, dx_max):
        probe = projectile(dx, dy)
        probe.step(2*dy)
        if probe.x < max(x1, x2):
            if run_trajectory(probe, limits):
                print('hit', max_height, probe.x, probe.y)
                dy = 0
                break
            else:
                print('loss', probe)
        else:
            break
    dy -= 1
print(probe, max_height)
