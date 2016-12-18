class advancedKeyPad(object):
    def __init__(self):
        self.digits = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]
        self.buttonsPressed = []
        self.x_indx = 0
        self.y_indx = 2

    def possibleMove(self, direction):
        if direction == 'U':
            self.y_indx = self.y_indx - 1        
            if self.y_indx == -1:
                self.y_indx = 0
        elif direction == 'D':
            self.y_indx = self.y_indx + 1        
            if self.y_indx == 5:
                self.y_indx = 4
        elif direction == 'L':
            self.x_indx = self.x_indx - 1        
            if self.x_indx == -1:
                self.x_indx = 0
        elif direction == 'R':
            self.x_indx = self.x_indx + 1        
            if self.x_indx == 5:
                self.x_indx = 4

    def isValidMove(self):
        if self.y_indx == 0:
            if (self.x_indx == 0 or self.x_indx == 1 or
                self.x_indx == 3 or self.x_indx == 4):
                    return False
        elif self.y_indx == 1:
            if (self.x_indx == 0 or self.x_indx == 4):
                    return False
        elif self.y_indx == 3:
            if (self.x_indx == 0 or self.x_indx == 4):
                    return False
        elif self.y_indx == 4:
            if (self.x_indx == 0 or self.x_indx == 1 or
                self.x_indx == 3 or self.x_indx == 4):
                    return False
        return True

    def oppositeMove(self, direction):
        if direction == 'U':
            return 'D'
        elif direction == 'D':
            return 'U'
        elif direction == 'R':
            return 'L'
        elif direction == 'L':
            return 'R'

    def move(self, direction):
        self.possibleMove(direction)
        if not self.isValidMove():
            self.possibleMove(self.oppositeMove(direction))

    def press_button(self):
       #print self.x_indx
       #print self.y_indx
       self.buttonsPressed.append(self.digits[self.y_indx][self.x_indx])
