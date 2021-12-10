import numpy as np
from Bingo_Board import Board

boards = []
with open("input.txt") as file:
    random_sequence = [int(x) for x in file.readline().strip().split(',')]
    # try:
    while file.readline(): # Blank
        board = np.zeros((5,5),dtype=int)
        for i in range(5):
            
            line = file.readline().strip().replace('  ',' ').split(' ',)
            print(line)
            board[i,:] = line 

        boards.append(Board(board))
    # except:
print(boards)

for bingo_call in random_sequence:
    print(bingo_call)
    for board in boards:
        i, j = board.mark_number(bingo_call)
        if i >= 0:
            if board.check_win(i,j):
                print(np.sum(board.board))
                print(bingo_call,board,board.sum_unmarked(),bingo_call*board.sum_unmarked())
                break
    else:
        continue
    break

# < 4038200
#   1071734