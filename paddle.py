from headers import *
import config

class Paddle:

    def __init__(self):

        self._len = config.PADDLE_LEN
        self.row = PADDLE_HT
        self.col = int((COL - 1 - self._len)/2)
        self._color = Back.RED
        self._reset = Back.BLACK + ' ' + Back.RESET
        self.grab = 0
        self.delta = 2


    def show(self):

        for i in range(self._len):
            config.my_board.grid[self.row][self.col + i] = self._color + PADDLE
            config.my_board.hidden_grid[self.row][self.col + i] = 'P'


            
    def clear(self):

        for i in range(self._len):
            config.my_board.grid[self.row][self.col + i] =  self._reset
            config.my_board.hidden_grid[self.row][self.col + i] =  ' '

            
    
    def change_position(self,direction):
        if(direction == 'left'):
            if(self.col - self.delta>1 ):
                self.col = self.col - self.delta
            else:
                return False
        if(direction == 'right'):
            if(self.col + self._len < COL - 2):
                self.col = self.col + self.delta
            else:
                return False
        
        return True

    def grab_func(self,val):
        self.grab = val
    
    def expand_paddle(self):
        self.clear()
        self._len = self._len + 4
        self.show()
    
    def shrink_paddle(self):
        
        if(self._len > 7):
            self.clear()
            self._len = self._len - 4
            self.show()

    def move(self,direction):

        #Clear the Paddle
        self.clear()

        #Change Position
        val = self.change_position(direction)

        #Show the Paddle
        self.show()
        
        return val





    
    



