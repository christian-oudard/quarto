from textwrap import dedent

SIZE = 4

# Lines that can create a win.
winning_lines = []
# Horizontal.
for y in range(SIZE):
    winning_lines.append([(x, y) for x in range(SIZE)])
# Vertical.
for x in range(SIZE):
    winning_lines.append([(x, y) for y in range(SIZE)])
# Diagonal.
winning_lines.append([(i, i) for i in range(SIZE)])
winning_lines.append([(i, SIZE - 1 - i) for i in range(SIZE)])

winning_lines = [tuple(line) for line in winning_lines]


def piece_number(n):
    """
    Use the bits in the number n to construct a piece.

    >>> piece_number(0)
    (False, False, False, False)
    >>> piece_number(5)
    (True, False, True, False)
    """
    return tuple(bool(n >> i & 1) for i in range(SIZE))

def number_piece(piece):
    """
    Construct a number representing the piece with its bits.

    >>> number_piece((False, False, False, False))
    0
    >>> number_piece((True, False, True, False))
    5
    """
    return sum((2**i) * b for i, b in enumerate(piece))

def parse_board(board_string):
    """
    >>> parse_board('''
    ...     ----
    ...     --0-
    ...     ----
    ...     -f--
    ... ''') == {(2, 1): (False, False, False, False), (1, 3): (True, True, True, True)}
    True
    """
    board_string = dedent(board_string).strip()
    board = {}
    for y, line in enumerate(board_string.splitlines()):
        for x, c in enumerate(line):
            if c == '-':
                continue
            board[(x, y)] = piece_number(int(c, 16))
    return board

def board_string(board):
    """
    >>> board = parse_board('''
    ...     ----
    ...     --0-
    ...     ----
    ...     -f--
    ... ''')
    >>> board[(0, 0)] = None # Ignore None values.
    >>> print(board_string(board))
    ----
    --0-
    ----
    -f--
    """
    grid = [['-' for x in range(SIZE)] for y in range(SIZE)]
    for (x, y), c in board.items():
        if c is None:
            continue
        grid[y][x] = hex(number_piece(c))[2:]
    return '\n'.join(''.join(line) for line in grid)

def is_win(board):
    """
    >>> is_win(parse_board('''
    ...     0---
    ...     -2--
    ...     --4-
    ...     -f--
    ... '''))
    False
    >>> is_win(parse_board('''
    ...     0---
    ...     -2--
    ...     --4-
    ...     -f-6
    ... '''))
    True
    """
    for line in winning_lines:
        pieces = [board.get(pos) for pos in line]
        if not all(pieces):
            continue
        for a, b, c, d in zip(*pieces):
            if a == b == c == d:
                return True
    return False
