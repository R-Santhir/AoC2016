import sys
from taxiCab import taxiCab

beck = taxiCab(0, 0, 0)

input_file = sys.argv[1]
with open(input_file,  'r') as f:
    text = f.read()

directions = text.split(',')
for move in directions:
    move = move.strip()
    if move[0] == 'R':
        beck.right_turn()
    else: #'L'
        beck.left_turn()

    beck.move(int(move[1:]))

print (abs(beck.x) + abs(beck.y))
