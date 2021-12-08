increases = 0
previous = [0, 0, 0]
counter = 0
for line in open("input.txt").readlines():
    index = counter % 3
    dropped_digit = previous[index]
    new_digit = int(line)
    previous[index] = new_digit
    if new_digit > dropped_digit and counter > 2:
        increases += 1
    counter += 1
print(increases)
