class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.moves = moves
        self.goal = goal

    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)

    def expand(self, moves):
        result = []
        i = self.board.index(0)
        if not i in [0, 1, 2] :
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0, 3, 6] :
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2, 5, 8] :
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8] :
            result.append(self.get_new_board(i, i+3, moves))
        return result

    def __str__(self):
        return str(self.board[:3]) + "\n" + \
            str(self.board[3:6]) + "\n" + \
            str(self.board[6:]) + "\n" + \
            "----------------"

###
# 스택으로 동작
###

puzzle = [1, 2, 3,
          0, 4, 6,
          7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

open_stack = []
open_stack.insert(0, State(puzzle, goal))
closed_stack = []
moves = 0
i = 0

while len(open_stack) != 0:
    # print("START OF OPENQ")
    # for elem in open_queue:
    #     print(elem)
    # print("END OF OPENQ")

    print(i)
    i = i + 1
    current = open_stack.pop(0)
    print(current)
    if current.board == goal:
        print("탐색 성공")
        break
    moves = current.moves + 1
    closed_stack.insert(0, current)
    open_stack_board = []
    closed_stack_board = []
    for open in open_stack:
        open_stack_board.append(open.board)
    for close in closed_stack:
        closed_stack_board.append(close.board)

    for state in current.expand(moves):
        if (state.board in open_stack_board) or (state.board in closed_stack_board):
            continue
        else:
            open_stack.insert(0, state)

