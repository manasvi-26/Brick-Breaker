from headers import *

class Paddle:

    def __init__(self,PADDLE_LEN):
        self._len = PADDLE_LEN
        self.row = PADDLE_HT
        self.col = int((COL - 1 - self._len)/2)
        self._color = Back.RED
        self._reset = Back.BLACK
        self.grab = True


    def show(self,my_board):

        for i in range(self._len):
            my_board.grid[self.row][self.col + i] = self._color + PADDLE
            my_board.hidden_grid[self.row][self.col + i] = 'P'


            
    def clear(self,my_board):

        for i in range(self._len):
            my_board.grid[self.row][self.col + i] =  self._reset  + ' '
            my_board.hidden_grid[self.row][self.col + i] =  ' '

            
    
    def change_position(self,direction):
        if(direction == 'left'):
            if(self.col > 2):
                self.col = self.col - 1
            else:
                return False
        if(direction == 'right'):
            if(self.col + self._len < COL - 2):
                self.col = self.col + 1
            else:
                return False
        
        return True

    def grab_func(self):
        self.grab = not self.grab

    def move(self,direction,my_board):

        #Clear the Paddle
        self.clear(my_board)

        #Change Position
        val = self.change_position(direction)

        #Show the Paddle
        self.show(my_board)
        
        return val





    
    



