import numpy as np
from collections import defaultdict

class Vent():

    def __init__(self,string):
        self.string = string.strip()
        s1, s2 = string.strip().split(' -> ')
        self.x1, self.y1 = (int(a) for a in s1.split(','))
        self.x2, self.y2 = (int(a) for a in s2.split(','))
        if self.x1 == self.x2 or self.y1 == self.y2:
            self.diag = False
        else:
            self.diag = True

    def __repr__(self):
        return self.string

    def coords(self):
        if self.x1 == self.x2:
            return [(self.x1,int(y)) for y in np.linspace(self.y1,self.y2,abs(self.y1-self.y2)+1)]
        elif self.y1 == self.y2:
            return [(int(x),self.y1) for x in np.linspace(self.x1,self.x2,abs(self.x1-self.x2)+1)]

vents = []
for line in open('input.txt').readlines():
    vents.append(Vent(line))

def zero():
    return 0

exposed_vents = defaultdict(zero)
count = 0
for vent in vents:
    if not vent.diag:
        for x,y in vent.coords():
            exposed_vents[str(x)+','+str(y)] += 1
            if exposed_vents[str(x)+','+str(y)] ==2:
                count += 1
print(exposed_vents)
print(vents)
print(count)