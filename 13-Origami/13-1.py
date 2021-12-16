import numpy as np

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
        if direction == "x":
            fold_index = 0
        else:
            fold_index = 1
        location = int(instructions[2:])
        folds.append((fold_index, location))
print(folds)
# print(dots)


def do_fold(dots, fold_index, fold_location):
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


def draw_dots(dots, x, y):
    board = np.full((x, y), ' ',)
    for dot in dots:
        coord = [int(a) for a in dot.split(',')]
        board[coord[0], coord[1]] = "X"
    np.transpose(board)
    for line in np.transpose(board):
        print(''.join(line))


print(len(dots))
closest_edge = [0, 0]
for fold in folds:
    dots = do_fold(dots, fold[0], fold[1])
    closest_edge[fold[0]] = fold[1]
    print(len(dots))
draw_dots(dots, closest_edge[0], closest_edge[1])
