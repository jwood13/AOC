
board = ['.'] * 11
moves = []
board[2] = ['.'] * 4
board[4] = ['.'] * 4
board[6] = ['.'] * 4
board[8] = ['.'] * 4


def print_board(b):
    print('\n#0123456789A#')
    print(f'#{b[0]}{b[1]}.{b[3]}.{b[5]}.{b[7]}.{b[9]}{b[10]}#')
    print(f'###{b[2][0]}#{b[4][0]}#{b[6][0]}#{b[8][0]}###')
    print(f'  #{b[2][1]}#{b[4][1]}#{b[6][1]}#{b[8][1]}#')
    print(f'  #{b[2][2]}#{b[4][2]}#{b[6][2]}#{b[8][2]}#')
    print(f'  #{b[2][3]}#{b[4][3]}#{b[6][3]}#{b[8][3]}#')
    print('  #########')

# Load_input
with open('input.txt') as file:
    file.readline()
    file.readline()
    for i in range(4):
        line = file.readline()
        board[2][i] = line[3]
        board[4][i] = line[5]
        board[6][i] = line[7]
        board[8][i] = line[9]



def check_win(board):
    correct = {2: 'A', 4: 'B', 6: 'C', 8: 'D'}
    for i in [2, 4, 6, 8]:
        for j in board[i]:
            if j != correct[i]:
                return False
    return True


def get_alley(board, index):
    for i in range(4):
        if board[index][i] != '.':
            to_move = board[index][i]
            board[index][i] = '.'
            return to_move, i + 1
    return '.', 0


def get_piece(board, index):
    alleys = [2, 4, 6, 8]
    if index in alleys:
        return get_alley(board, index)
    else:
        piece = board[index]
        board[index] = '.'
        return piece, 0


def put_alley(board, index, put):
    for i in range(3, -1, -1):
        if board[index][i] == '.':
            board[index][i] = put
            return i + 1
    return '.'


def put_piece(board, index, put):
    alleys = [2, 4, 6, 8]
    if index in alleys:
        return put_alley(board, index, put)
    else:
        if board[index] == '.':
            board[index] = put
            return 0
        else:
            return '.'


def do_move(start, stop, board):
    alleys = [2, 4, 6, 7]
    energy_expense = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

    mover, out_cost = get_piece(board, start)
    if mover == '.':
        return 0
    else:
        in_cost = put_piece(board, stop, mover)
        if in_cost == '.':
            put_piece(board, start, mover)
            return 0
        else:
            move_cost = in_cost + out_cost + abs(start - stop)
            return move_cost * energy_expense[mover]
    return move_cost


moves = []
moves_cost = 0
while not check_win(board):
    print_board(board)
    print(moves_cost, ' '.join(moves))
    move = input('Input next move or "r" to reverse: ')
    if move != 'r':
        moves.append(move)
        try:
            start, stop = (int(x, 16) for x in move)
        except ValueError:
            start, stop = 0, 0
        if start > 10 or stop > 10:
            start, stop = 0, 0
        cost = do_move(start, stop, board)
        if cost == 0:
            print('Invalid Move, no changes made')
            moves.pop()
        moves_cost += cost
    else:
        if len(moves) > 0:
            move = moves.pop()
            print('reversed ' + move)
            stop, start = (int(x, 16) for x in move)
            cost = do_move(start, stop, board)
            moves_cost -= cost

print_board(board)
print(moves_cost, moves)

#< 50372
# < 50172