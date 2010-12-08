import itertools
from copy import copy
from quarto import SIZE, is_win, board_string, make_move

# Description of pieces, a 4-dimensional binary space.
piece_descriptions = {}
for a, size in enumerate(['short', 'tall']):
    for b, color in enumerate(['dark', 'light']):
        for c, shape in enumerate(['round', 'square']):
            for d, density in enumerate(['hollow', 'solid']):
                piece = (bool(a), bool(b), bool(c), bool(d))
                piece_descriptions[piece] = (size, color, shape, density)

def game(player_a, player_b):
    """
    Play a game between two player functions.
    """
    pieces = list(piece_descriptions.keys())

    # Board mapping positions to pieces currently occupying that position.
    board = {}
    for x in range(SIZE):
        for y in range(SIZE):
            board[(x, y)] = None

    current_piece = None
    for score, current_player in itertools.cycle([(+1, player_a), (-1, player_b)]):
        # Remove the current piece from available pieces, and give it to the current player.
        if current_piece:
            pieces.remove(current_piece)
        # Current player places the piece at `pos`, and chooses a piece for the opponent.
        pos, next_piece = current_player(copy(board), copy(pieces), current_piece)
        #print('player moved at %s, and chose %s' % (pos, next_piece))
        if pos:
            assert board[pos] is None # Don't allow playing on occupied positions.
            board = make_move(board, current_piece, pos)
        current_piece = next_piece

        #print(board_string(board))

        if is_win(board):
            #print('%s wins!' % current_player.__name__)
            return score

        if not pieces:
            # Game over, draw.
            #print('draw')
            return 0

def match(player_a, player_b, num_games, verbose=False):
    a_score = 0
    b_score = 0
    ties = 0
    for i in range(num_games):
        if i % 2 == 0:
            result = game(player_a, player_b)
        else:
            result = -game(player_b, player_a)

        if result == +1:
            a_score += 1
        elif result == -1:
            b_score += 1
        elif result == 0:
            ties += 1

    if verbose:
        print(player_a.__name__, a_score)
        print(player_b.__name__, b_score)
        print('ties', ties)

    return (a_score, b_score, ties)

if __name__ == '__main__':
    from players import bot_random, bot_oneply, bot_twoply
    a, b, t = match(bot_random, bot_oneply, 100, verbose=True)
    a, b, t = match(bot_twoply, bot_oneply, 100, verbose=True)
