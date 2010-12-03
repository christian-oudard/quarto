import random

def bot_twoply(board, pieces, current_piece):
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
        losing_pieces = set()
        for piece in pieces:
            winning_squares = winning_moves(board, piece)
            if winning_squares:
                losing_pieces.add(piece)
        not_losing_pieces = [p for p in pieces if p not in losing_pieces]
        if not_losing_pieces:
            next_piece = random.choice(not_losing_pieces)
        else:
            next_piece = random.choice(pieces)

    return pos, next_piece

