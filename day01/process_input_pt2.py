import sys
from taxiCab import taxiCab
from router import router

beck = taxiCab(0, 0, 0)
beck_router = router(beck)

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
    
    if beck_router.check_and_update_intersection(beck): #if 1 an intersection has occurred
        break 
    else:
        beck_router.add_trip(beck)

#beck_router.print_trips()
print (abs(beck_router.intersect_point.x) + abs(beck_router.intersect_point.y))
