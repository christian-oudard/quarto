import random

def bot_random(board, pieces, current_piece):
    from players import available_squares
    squares = available_squares(board)

    pos = None
    if current_piece:
        pos = random.choice(squares)

    next_piece = None
    if pieces:
        next_piece = random.choice(pieces)

    return pos, next_piece
