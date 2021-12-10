import numpy as np
class Board():
    def __init__(self, board):
        self.board = board
        self.marks = np.zeros_like(board,dtype=int)
        self.won = False

    def __repr__(self):
        return self.board.__repr__()+'\n' + self.marks.__repr__()

    def mark_number(self,number):
        marked = (-1,-1)
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i,j] == number:
                    self.marks[i,j] = 1
                    marked = (i,j)
                    break
            else:
                continue
            break
        return marked

    def check_win(self,i,j):
        row_sum = np.sum(self.marks[i,:])
        col_sum = np.sum(self.marks[:,j])
        if row_sum == 5 or col_sum == 5:
            self.won = True
            return True
        else:
            return False

    def sum_unmarked(self):
        sum = 0
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                sum += self.board[i,j] * -(self.marks[i,j]-1)
        return sum