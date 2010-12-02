from quarto import SIZE

import random

def bot_random(board, pieces, current_piece):
    available_squares = []
    for x in range(SIZE):
        for y in range(SIZE):
            pos = x, y
            if board.get(pos) is None:
                available_squares.append(pos)
    pos = None
    if current_piece:
        pos = random.choice(available_squares)

    next_piece = None
    if pieces:
        next_piece = random.choice(pieces)

    return pos, next_piece


