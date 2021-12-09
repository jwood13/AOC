horizontal = 0
depth = 0
aim = 0
for line in open("input.txt").readlines():
    change = line.split(' ')
    change[0]
    if change[0] == 'forward':
        horizontal += int(change[1])
        depth += aim * int(change[1])
    elif change[0] == 'up':
        aim -= int(change[1])
    elif change[0] == 'down':
        aim += int(change[1])

print(horizontal,depth,horizontal*depth)