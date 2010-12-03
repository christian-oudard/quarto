import random

def bot_oneply(board, pieces, current_piece):
    from players import available_squares, winning_moves
    squares = available_squares(board)

    pos = None
    if current_piece:
        winning_squares = winning_moves(board, current_piece)
        if winning_squares:
            pos = random.choice(winning_squares)
        else:
            pos = random.choice(squares)

    next_piece = None
    if pieces:
        next_piece = random.choice(pieces)

    return pos, next_piece
