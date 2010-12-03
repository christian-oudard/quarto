from quarto import SIZE

from players.bot_random import bot_random

def available_squares(board):
    squares = []
    for x in range(SIZE):
        for y in range(SIZE):
            pos = x, y
            if board.get(pos) is None:
                squares.append(pos)
    return squares
