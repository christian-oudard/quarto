from copy import copy

from quarto import SIZE, is_win

from players.bot_random import bot_random
from players.bot_oneply import bot_oneply
from players.bot_twoply import bot_twoply

def available_squares(board):
    """
    >>> from quarto import parse_board
    >>> available_squares(parse_board('''
    ...     da90
    ...     31-b
    ...     e46-
    ...     8cf7
    ... '''))
    [(2, 1), (3, 2)]
    """
    squares = []
    for x in range(SIZE):
        for y in range(SIZE):
            pos = x, y
            if board.get(pos) is None:
                squares.append(pos)
    return squares

def winning_moves(board, piece):
    """
    >>> from quarto import parse_board, parse_piece
    >>> board = parse_board('''
    ...     -086
    ...     cd-3
    ...     -a49
    ...     1b7-
    ... ''')
    >>> winning_moves(board, parse_piece('2'))
    [(0, 0)]
    >>> winning_moves(board, parse_piece('5'))
    [(3, 3)]
    >>> winning_moves(board, parse_piece('e'))
    [(0, 0)]
    >>> winning_moves(board, parse_piece('f'))
    [(3, 3)]
    """
    winning_squares = []
    for square in available_squares(board):
        test_board = copy(board)
        test_board[square] = piece
        if is_win(test_board):
            winning_squares.append(square)
    return winning_squares
