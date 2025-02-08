
"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    num_x = 0
    num_o = 0
    for i in board:
        num_x += i.count(X)
        num_o += i.count(O)
    if num_x <= num_o:
        return X
    else:
        return O 
    
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    len_board = len(board)
    for i in range(len_board):
        for j in range(len_board):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = board.copy()
    
    if action in actions(board):
        new_board[action[0]][action[1]] = player(board)
        return new_board
    else:
        raise NameError('No valid action')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        if i[0] == i[1] and i[1] == i[2] and i[0] != None:
            return i[0]
    for j in range(len(board)):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j]  and board[0][j] != None:
            return board[0][j]
    if board[1][1] != None:
        if board[1][1] == board[0][0] and board[1][1] == board[2][2]:
            return board[1][1]
        elif board[1][1] == board[0][2] and board[1][1] == board[2][0]:
            return board[1][1]
    
    return None


def terminal(board):
    if winner(board):
        print(winner(board))
        return True
    for i in board:
        if EMPTY in i:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    util = {X : 1, O : -1}
    winner_simbol = winner(board)
    if winner_simbol:
        return util[winner_simbol]
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    raise NotImplementedError
