import random

from quarto import make_move

def bot_wholeply(board, pieces, current_piece):
    from players import available_squares, winning_moves
    squares = available_squares(board)

    # Play a winning move if one exists.
    if current_piece:
        for pos in winning_moves(board, current_piece):
            return pos, None

    # Try to find a combination of a move and piece that doesn't lose on the
    # opponent's next turn.
    for pos in squares:
        test_board = make_move(board, current_piece, pos)
        losing_pieces = set()
        for next_piece in pieces:
            if list(winning_moves(test_board, next_piece)):
                losing_pieces.add(next_piece)
        not_losing_pieces = list(set(pieces) - losing_pieces)
        if not_losing_pieces:
            return pos, random.choice(not_losing_pieces)

    # Nothing intelligent left to do, give up and play randomly.
    pos = None
    if squares:
        pos = random.choice(squares)

    next_piece = None
    if pieces:
        next_piece = random.choice(pieces)

    return pos, next_piece

