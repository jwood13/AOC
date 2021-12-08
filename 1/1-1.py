increases = -1
previous = -1
for line in open("input.txt").readlines():
    if int(line) > previous:
        increases += 1
    previous = int(line)
print(increases)
