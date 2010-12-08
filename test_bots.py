from quarto import parse_board, parse_piece
from players.bot_oneply import bot_oneply
from players.bot_twoply import bot_twoply

def test_winning_move():
    # Should take a winning move if it has one.
    board = parse_board('''
        50-4
        --cb
        --6a
        f2--
    ''')
    for bot in [bot_oneply, bot_twoply]:
        pos, piece = bot(board, pieces=[], current_piece=parse_piece('e'))
        assert pos == (1, 2)

def test_no_lose():
    # Should avoid giving the opponent a piece that they can win with.
    board = parse_board('''
        14--
        -7--
        6-58
        -e--

    ''')
    available_pieces = [parse_piece(c) for c in '239abcdf']
    for bot in [bot_twoply]:
        pos, piece = bot(board, pieces=available_pieces, current_piece=None)
        assert piece == parse_piece('a')
