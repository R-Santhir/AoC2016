class taxiCab(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def right_turn(self):
        self.direction = self.direction + 90
        if self.direction == 360:
            self.direction = 0

    def left_turn(self):
        self.direction = self.direction - 90
        if self.direction == -90:
            self.direction = 270
        
    def move(self, paces):
        if self.direction == 0:
            self.y = self.y + paces
        elif self.direction == 90:
            self.x = self.x + paces
        elif self.direction == 180:
            self.y = self.y - paces
        else: #270
            self.x = self.x - paces
