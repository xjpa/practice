# https://open.kattis.com/problems/skak

"""
for a rook, the distance doesnt matter cos
- same row means capture in 1 move
- else just gotta move to line with pawn to capture in 2moves

we only gotta align it with 1 coordinate to capture anything there
"""

rook_x, rook_y = map(int, input().split())
pawn_x, pawn_y = map(int, input().split())

if rook_x == pawn_x or rook_y == pawn_y:
    print("1")
else:
    print("2")