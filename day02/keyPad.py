class keyPad(object):
    def __init__(self):
        self.digits = [[1,2,3],[4,5,6],[7,8,9]]
        self.buttonsPressed = []
        self.x_indx = 1
        self.y_indx = 1

    def move(self, direction):
        if direction == 'U':
            self.y_indx = self.y_indx - 1        
            if self.y_indx == -1:
                self.y_indx = 0
        elif direction == 'D':
            self.y_indx = self.y_indx + 1        
            if self.y_indx == 3:
                self.y_indx = 2
        elif direction == 'L':
            self.x_indx = self.x_indx + 1        
            if self.x_indx == 3:
                self.x_indx = 2
        elif direction == 'R':
            self.x_indx = self.x_indx + 1        
            if self.x_indx == 3:
                self.x_indx = 2

    def press_button(self):
       self.buttonsPressed.append(self.digits[self.y_indx][self.x_indx])
