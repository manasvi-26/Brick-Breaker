from headers import *
import config

class PowerUp:
    
    def __init__(self):

        self.vel_vert = -1
        self.row = row
        self.col = col
        self._reset = Back.BLACK + ' ' + Back.RESET

    def clear(self):
        config.my_board.grid[self.row][self.col] = self._reset 


    def show(self):
        config.my_board.grid[self.row][self.col] = self.shape 


class Ball_Multiplier(PowerUp):

    def __init__(self):
        super().__init__()
        self.shape = BALL_MULTIPLIER

class Thru_Ball(PowerUp):
    
    def __init__(self):
        super().__init__()
        self.shape = THRU_BALL
        
    
        
class Expand_Paddle(PowerUp):
    
    def __init__(self):
        super().__init__()
        self.shape = EXPAND_PADDLE
        

class Shrink_Paddle(PowerUp):
    def __init__(self):
        super().__init__()
        self.shape = SHRINK_PADDLE
        

class Fast_Ball(PowerUp):
    
    def __init__(self):
        super().__init__()
        self.shape = FAST_BALL


