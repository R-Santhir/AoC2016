import sys

def isTriangle(sides):
    if (int(sides[0]) + int(sides[1])) <= int(sides[2]):
        return False 
    elif (int(sides[1]) + int(sides[2])) <= int(sides[0]):
        return False 
    elif (int(sides[2]) + int(sides[0])) <= int(sides[1]):
        return False
    else:
        return True

input_file = sys.argv[1]
with open(input_file,  'r') as f:
    text = f.readlines()

count = 0
for line in text:
    sides = line.strip().split()
    if isTriangle(sides):
        count = count + 1

print count
