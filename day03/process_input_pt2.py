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
for i in xrange(0,len(text)-2,3):
    sides1 = text[i].strip().split()
    sides2 = text[i+1].strip().split()
    sides3 = text[i+2].strip().split()
    for j in xrange(3):
        sides = []
        sides.append(sides1[j])
        sides.append(sides2[j])
        sides.append(sides3[j])
        #print "Triangle-----"
        #print sides[0]
        #print sides[1]
        #print sides[2]
        #print "-----"
        if isTriangle(sides):
            count = count + 1

print count
