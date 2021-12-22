import numpy as np

reactor = np.zeros((101,101,101), dtype=bool)
print(np.sum(reactor))

for line in open('input.txt').readlines():
    command, coordinates = line.strip().split(' ')
    command = command == 'on'
    bounds = coordinates.split(',')
    x1, x2 = (int(x)+50 for x in bounds[0][2:].split('..'))
    y1, y2 = (int(x)+50 for x in bounds[1][2:].split('..'))
    z1, z2 = (int(x)+50 for x in bounds[2][2:].split('..'))
    reactor[x1:x2+1, y1:y2+1, z1:z2+1] = command
    # print(reactor[x1:x2, y1:y2, z1:z2] )
    # print(x1,x2,y1,y2,z1,z2+1,command)
# print(reactor)
print(np.sum(reactor))