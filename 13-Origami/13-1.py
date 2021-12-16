
dots = {}
folds = []
before_split = True
for line in open('input.txt').readlines():
    if line == '\n':
        before_split = False
    elif before_split:
        coordinate = line.strip()
        dots[coordinate] = True
    else:
        instructions = line[11:]
        direction = instructions[0]
        location = int(instructions[2:])
        folds.append((direction, location))
print(folds)
print(dots)


def fold(dots, direction, fold_location):
    if direction == "x":
        fold_index = 0
    else:
        fold_index = 1
    to_remove = []
    to_add = []
    for dot in dots.keys():
        coord = [int(a) for a in dot.split(',')]
        if coord[fold_index] > fold_location:
            coord[fold_index] = fold_location - \
                (coord[fold_index] - fold_location)
            to_add.append(f'{coord[0]},{coord[1]}')
            to_remove.append(dot)
        elif coord[fold_index] > fold_location:
            del dots[dot]
    for dot in to_remove:
        del dots[dot]
    for dot in to_add:
        dots[dot] = True
    return dots


print(len(dots))
dots = fold(dots, folds[0][0], folds[0][1])
print(dots)
print(len(dots))
