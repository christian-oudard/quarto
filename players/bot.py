# How big is the state space?
# There are 16! completed boards.
# Each board is invariant under rotation and reflection, reducing the space by a factor of 8
# We can also reduce on symmetry of piece attributes, by "column swapping" one attribute for another across the entire set of pieces. This reduces the state space by a factor of (4!)

# import math
#
# def product(iterable):
#     prod = 1
#     for n in iterable:
#         prod *= n
#     return prod
#
# def npr(n, r):
#     """
#     Calculate the number of ordered permutations of r items taken from a
#     population of size n.
#
#     >>> npr(3, 2)
#     6
#     >>> npr(100, 20)
#     1303995018204712451095685346159820800000
#     """
#     assert 0 <= r <= n
#     return product(range(n - r + 1, n + 1))
#
# def ncr(n, r):
#     """
#     Calculate the number of unordered combinations of r items taken from a
#     population of size n.
#
#     >>> ncr(3, 2)
#     3
#     >>> ncr(100, 20)
#     535983370403809682970
#     >>> ncr(10000, 1000) == ncr(10000, 9000)
#     True
#     """
#     assert 0 <= r <= n
#     if r > n // 2:
#         r = n - r
#     return npr(n, r) // math.factorial(r)
#
# #pieces on board: number of possibilities
# #0: 1
# #1: 16 * 16
# #2: ncr(16, 2) * 16 * 15
# #3: ncr(16, 3) * 16 * 15 * 14
# #4: ncr(16, 4) * npr(16, 4)
# total = 1
# for i in range(1, 16 + 1):
#     total += ncr(16, i) * npr(16, i)
# print(total // 8 // 24) # About 32 trillion


# Branching factor per ply, accounting for symmetry
# pieces on board : factor
# -1: 1 move (no move)* 1 piece, symmetrically = 1
# 0: 3 moves (center, edge, corner) * 4 pieces (share 3 attributes, share 2 attributes, share 1 attribute, share no attributes) = 12
# 1: up to 15 moves, 14 pieces = 210
# corner, 9 moves
# X***
# -***
# --**
# ---*
#
# edge, 15 moves
# *X**
# ****
# ****
# ****
#
# center, 9 moves
# ****
# -X**
# --**
# ---*
#
# Symmetry doesn't matter beyond the first couple moves.

# Branching factor per ply, not taking into account symmetry
# pieces on board : factor
# -1: 1 move (no move) * 16 pieces = 16
# 0: 16 moves * 15 pieces = 240
# 1: 15 moves * 14 pieces = 210
# 2: 14 moves * 13 pieces = 182
# ...
# 9: 7 moves * 6 pieces = 42
# 10: 6 moves * 5 pieces = 30
# 11: 5 moves * 4 pieces = 20
# 12: 2 moves * 3 pieces = 12
# 13: 3 moves * 2 pieces = 6
# 14: 2 moves * 1 piece = 2
# 15: 1 move * 1 piece (no piece) = 1

# Remaining game tree size per ply:
# 16: 0
# 15: 1
# 14: 2
# 13: 12
# 12: 144
# 11: 2880
# 10: 86400
#  9: 3628800 (too many to exhaustively search?)

# Strategy:
# Play perfectly from ply 10 onward.
# Before ply 10, use the heuristic of maximizing the number of ways for the opponent to lose?
