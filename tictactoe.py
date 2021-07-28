"""
Tic Tac Toe Player
"""

import copy
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
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x += 1
            if board[i][j] == O:
                o += 1
    if x > o:
        return O
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    i, j = action
    new_board = copy.deepcopy(board)
    if not terminal(board):
        new_board[i][j] = player(board)
        return new_board
    raise Exception

def check(board, symbol):
    """
    Checks if a player denoted by the symbol has won
    """
    row = [0 for i in range(3)]
    col = [0 for i in range(3)]
    dia = [0 for i in range(2)]
    for i in range(3):
        for j in range(3):
            if board[i][j] == symbol:
                row[i] += 1
                col[j] += 1
        if board[i][i] == symbol:
            dia[0] += 1
        if board[i][2 - i] == symbol:
            dia[1] += 1
    win = False
    for i in range(3):
        if row[i] == 3 or col[i] == 3:
            win = True
    if dia[0] == 3 or dia[1] == 3:
        win = True
    return win

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    if check(board, X):
        return X
    if check(board, O):
        return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x += 1
            if board[i][j] == O:
                o += 1
    if x + o == 9 or winner(board) != None:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError
    results = winner(board)
    if results == X:
        return 1
    if results == O:
        return -1
    return 0

def min_value(board):
    if terminal(board):
        return (utility(board), None)
    val = 2
    actions_list = actions(board)
    action_taken = None
    for action in actions_list:
        result_val = max_value(result(board, action))
        if result_val[0] < val:
            val = result_val[0]
            action_taken = action
        if val == -1:
            return (val, action_taken)
    return (val, action_taken)

def max_value(board):
    if terminal(board):
        return (utility(board), None)
    val = -2
    actions_list = actions(board)
    action_taken = None
    for action in actions_list:
        result_val = min_value(result(board, action))
        if result_val[0] > val:
            val = result_val[0]
            action_taken = action
        if val == 1:
            return (val, action_taken)
    return (val, action_taken)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #raise NotImplementedError
    if terminal(board):
        return None
    if player(board) == X:
        return max_value(board)[1]
    return min_value(board)[1]
