from copy import copy

from quarto import SIZE, is_win

from players.bot_random import bot_random
from players.bot_oneply import bot_oneply
from players.bot_twoply import bot_twoply

def available_squares(board):
    squares = []
    for x in range(SIZE):
        for y in range(SIZE):
            pos = x, y
            if board.get(pos) is None:
                squares.append(pos)
    return squares

def winning_moves(board, piece):
    winning_squares = []
    for square in available_squares(board):
        test_board = copy(board)
        test_board[square] = piece
        if is_win(test_board):
            winning_squares.append(square)
    return winning_squares
