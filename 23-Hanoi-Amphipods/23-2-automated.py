
rooms = [2, 4, 6, 8]
corridors = [0, 1, 3, 5, 7, 9, 10]
correct = {2: 'A', 4: 'B', 6: 'C', 8: 'D'}
homes = {v: k for k, v in correct.items()}
move_cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def put_room(board, index, put):
    for i in range(3, -1, -1):
        if board[index][i] == '.':
            board[index][i] = put
            return i + 1
    return '.'


def get_room(board, index):
    for i in range(4):
        if board[index][i] != '.':
            to_move = board[index][i]
            board[index][i] = '.'
            return to_move, i + 1
    return '.', 0


def available_room(board, room_number):
    target = correct[room_number]
    for i in board[room_number]:
        if i != target and i != '.':
            return False
    return True


def clear_corridor(board, start, stop):
    if start < stop:
        for i in range(start+1, stop):
            if board[i] != '.' and type(board[i]) is not list:
                return False
    else:
        for i in range(stop+1, start):
            if board[i] != '.' and type(board[i]) is not list:
                return False
    return True


class Board_State():
    cost = 0

    def __init__(self, board, parent='', cost=0):
        self.parent = parent
        self.board = board.copy()
        self.cost = cost
        self.fitness = self.get_fitness()

    def __repr__(self):
        return self.state_string() + str(self.cost+self.fitness)

    def state_string(self):
        return str(self.board).replace(', ', '').replace("'", "")


    def get_base_fitness(self):
        minimum_cost = 0
        for i in corridors:
            if self.board[i] == 'A':
                minimum_cost += abs(i-2)
            elif self.board[i] == 'B':
                minimum_cost += abs(i-4) * 10
            elif self.board[i] == 'C':
                minimum_cost += abs(i-6) * 100
            elif self.board[i] == 'D':
                minimum_cost += abs(i-8) * 1000
        for i in rooms:
            if not available_room(self.board, i):
                to_empty = False
                # add emptying and corridor costs
                for k in range(3, -1, -1):
                    j = self.board[int(i)][k]
                    if to_empty or j != correct[i]:
                        to_empty = True
                        if j == 'A':
                            minimum_cost += abs(i-2)
                            minimum_cost += k+1
                        elif j == 'B':
                            minimum_cost += (abs(i-4)) * 10
                            minimum_cost += (k+1) * 10
                        elif j == 'C':
                            minimum_cost += abs(i-6) * 100
                            minimum_cost += (k+1) * 100
                        elif j == 'D':
                            minimum_cost += abs(i-8) * 1000
                            minimum_cost += (k+1) * 1000
                        # add filling cost
                        minimum_cost += (k+1) * move_cost[correct[i]]
            else:
                for j in range(4):
                    if self.board[i][j] == '.':
                        minimum_cost += (j+1) * move_cost[correct[i]]

        return minimum_cost

    def get_fitness(self):
        minimum_cost = self.get_base_fitness()
        return minimum_cost

    def str(self):
        return self.state_string()

    def check_move(self, start, stop):
        # only valid moves are from corridor to room or reverse
        move_board = self.board.copy()
        for i in rooms:
            move_board[i] = move_board[i].copy()
        if start in corridors:
            mover = move_board[start]
            if stop in corridors or mover == '.':
                return False, 0
            else:
                move_to = homes[mover]
                if available_room(move_board, move_to) and clear_corridor(move_board, start, stop):
                    room_cost = put_room(move_board, stop, mover)
                    move_board[start] = '.'
                else:
                    return False, 0
        else:
            mover, room_cost = get_room(move_board, start)
            if stop in rooms or mover == '.':
                return False, 0
            else:
                if board[stop] == '.' and clear_corridor(move_board, start, stop):
                    move_board[stop] = mover
                else:
                    return False, 0
        cost = (room_cost + abs(stop - start)) * move_cost[mover]
        return move_board, cost

    def generate_new_states(self):
        '''Generate new walkers in all 4 directions, covering for duplication, and revisitation'''
        new_walkers = []
        for i in corridors:
            if self.board[i] != '.':
                move, cost = self.check_move(i, homes[self.board[i]])
                if move:
                    # print('cost:', self.cost+self.cave[coord[0], coord[1]])
                    new_walkers.append(
                        Board_State(move, self.state_string(), self.cost + cost))
            else:
                for j in rooms:
                    if not available_room(self.board, j):
                        move, cost = self.check_move(j, i)
                        if move:
                            # print('cost:', self.cost+self.cave[coord[0], coord[1]])
                            new_walkers.append(
                                Board_State(move, self.state_string(), self.cost + cost))
        return new_walkers

    def finished(self):
        for r in rooms:
            if not available_room(self.board,r):
                return False
        for c in corridors:
            if self.board[c] != '.':
                return False
        return True


def sort_key(x):
    '''sorting key function for the list'''
    return x.cost+x.fitness


def traceback(coordinate, closed):
    string = coordinate.str()
    while coordinate.parent != '':
        coordinate = closed[coordinate.parent]
        string = coordinate.str()+str(coordinate.cost) + ", " + string
    return string


filename = 'input.txt'
board = ['.'] * 11
board[2] = ['.'] * 4
board[4] = ['.'] * 4
board[6] = ['.'] * 4
board[8] = ['.'] * 4
print(board)
with open('input.txt') as file:
    file.readline()
    file.readline()
    for i in range(4):
        line = file.readline()
        board[2][i] = line[3]
        board[4][i] = line[5]
        board[6][i] = line[7]
        board[8][i] = line[9]
part1 = False
if part1:
    board[2][2] = 'A'
    board[4][2] = 'B'
    board[6][2] = 'C'
    board[8][2] = 'D'
    board[2][1] = board[2][3]
    board[4][1] = board[4][3]
    board[6][1] = board[6][3]
    board[8][1] = board[8][3]
    board[2][3] = 'A'
    board[4][3] = 'B'
    board[6][3] = 'C'
    board[8][3] = 'D'

print(board)
start_state = Board_State(board)
print(start_state.fitness)
reached = {}
start = start_state
to_check = {start.str(): start}
count = 0
finished = False
while not finished:
    #     # print(to_check.values())
    find_next = sorted(to_check.values(), key=sort_key)
    # print(find_next)
    next = find_next[0]
    if next.finished():
        finished = True
    to_check.pop(next.str())
    new_points = next.generate_new_states()
    reached[next.str()] = next
    for new in new_points:
        string_coord = new.str()
        if string_coord in reached.keys():
            if reached[string_coord].cost > new.cost:
                reached[string_coord] = new
        elif string_coord in to_check:
            if to_check[string_coord].cost > new.cost:
                to_check[string_coord] = new
        else:
            to_check[string_coord] = new
    count += 1
    # print(next.fitness)
print(next, next.cost, next.fitness)
print(traceback(next, reached))
