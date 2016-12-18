from taxiCab import taxiCab

class router(object):
    def __init__(self, taxi_cab):
        self.taxi_cab = taxi_cab 
        self.endpoints = []
        temp_cab = taxiCab(taxi_cab.x, taxi_cab.y, 0)
        self.endpoints.append(temp_cab)
        self.intersect_point = taxiCab(0, 0, 0)

    def print_trips(self):
        print "There are " + str(len(self.endpoints)) + " trips"
        for point in self.endpoints:
            print "(" + str(point.x) + "," + str(point.y) + ")"
    
    def check_and_update_intersection(self, taxi_cab):
        if len(self.endpoints) >= 4:
            for i in xrange(len(self.endpoints) - 2):
                if self.intersects(self.endpoints[i], self.endpoints[i+1], self.endpoints[-1], taxi_cab):
                    self.update_intersection(self.endpoints[i], self.endpoints[i+1], self.endpoints[-1], taxi_cab)
                    return 1
            return 0
        else:
            return 0
            
        
    def add_trip(self, taxi_cab):
        temp_cab = taxiCab(taxi_cab.x, taxi_cab.y, 0)
        self.endpoints.append(temp_cab)

    def intersects(self, a_start, a_end, b_start, b_end):
        if b_start.x == b_end.x:
            #b is a vertical line
            b_vert = True
            b_horiz = False
        else:
            #b is a horizontal line
            b_vert = False
            b_horiz = True
        if a_start.x == a_end.x:
            #a is a vertical line 
            a_vert = True
            a_horiz = False
        else:
            #a is a horizontal line
            a_vert = False
            a_horiz = True

        if a_vert and b_vert:
            if a_start.x == b_start.x:
                if b_start.y <= a_start.y and b_start.y >= a_end.y:
                    return True
                elif b_end.y <= a_start.y and b_end.y >= a_end.y:
                    return True
                elif b_end.y >= a_start.y and b_end.y <= a_end.y:
                    return True
                elif b_end.y >= a_start.y and b_end.y <= a_end.y:
                    return True
                else:
                    return False
            else:# paralell lines
                return False
        elif a_vert and b_horiz:
            if (a_start.x <= b_start.x and a_start.x >= b_end.x or
                a_start.x >= b_start.x and a_start.x <= b_end.x):
                if (b_start.y <= a_start.y and b_start.y >= a_end.y or
                    b_start.y >= a_start.y and b_start.y <= a_end.y):
                    return True
                else:
                    return False
            else:
                return False
        elif a_horiz and b_vert:
            if (b_start.x <= a_start.x and b_start.x >= a_end.x or
                b_start.x >= a_start.x and b_start.x <= a_end.x):
                if (a_start.y <= b_start.y and a_start.y >= b_end.y or
                    a_start.y >= b_start.y and a_start.y <= b_end.y):
                    return True
                else:
                    return False
            else:
                return False
        elif a_horiz and b_horiz:
            if a_start.y == b_start.y:
                if b_start.x <= a_start.x and b_start.x >= a_end.x:
                    return True
                elif b_end.x <= a_start.x and b_end.x >= a_end.x:
                    return True
                elif b_end.x >= a_start.x and b_end.x <= a_end.x:
                    return True
                elif b_end.x >= a_start.x and b_end.x <= a_end.x:
                    return True
                else:
                    return False
            else:# paralell lines
                return False

    def update_intersection(self, a_start, a_end, b_start, b_end):
        #print "in update_intersection"
        #print b_start.x, b_end.x
        if b_start.x == b_end.x:
            #print "b is a vertical line"
            b_vert = True
            b_horiz = False
        else:
            #print "b is a horizontal line"
            b_vert = False
            b_horiz = True
        if a_start.x == a_end.x:
            #print "a is a vertical line" 
            a_vert = True
            a_horiz = False
        else:
            #print "a is a horizontal line"
            a_vert = False
            a_horiz = True
        if a_vert and b_vert:
            self.intersect_point.x = b_start.x
            cursor = b_start.y
            while cursor != b_end.y:
                if cursor == a_start.y or cursor == a_end.y:
                    self.intersect_point.y = cursor
                    break
                if cursor <= b_end.y:
                    cursor = cursor + 1
                else: # cursor >= b_end.y
                    cursor = cursor - 1
        elif a_vert and b_horiz:
            #print "CASE 2"
            self.intersect_point.x = a_start.x
            self.intersect_point.y = b_start.y
        elif a_horiz and b_vert:
            #print "CASE 3"
            self.intersect_point.x = b_start.x 
            self.intersect_point.y = a_start.y
        elif a_horiz and b_horiz:
            self.intersect_point.y = b_start.y
            cursor = b_start.x
            while cursor != b_end.x:
                if cursor == a_start.x or cursor == a_end.x:
                    self.intersect_point.x = cursor
                    break
                if cursor <= b_end.x:
                    cursor = cursor + 1
                else: # cursor >= b_end.x
                    cursor = cursor - 1
        
