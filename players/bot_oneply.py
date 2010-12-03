import random
from copy import copy

def bot_oneply(board, pieces, current_piece):
    from players import available_squares
    from quarto import is_win
    squares = available_squares(board)

    pos = None
    if current_piece:
        winning_squares = []
        for square in squares:
            test_board = copy(board)
            test_board[square] = current_piece
            if is_win(test_board):
                pos = square
                break
        else:
            pos = random.choice(squares)

    next_piece = None
    if pieces:
        next_piece = random.choice(pieces)

    return pos, next_piece
