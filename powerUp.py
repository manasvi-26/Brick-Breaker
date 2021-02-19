from headers import *
import config

class PowerUp:
    
    def __init__(self,row,col):

        self.vel_vert = -1
        self.row = row
        self.col = col
        self._reset = Back.BLACK + ' ' + Back.RESET
        self.delete = False
        self.show_mode = True
        self.activated = False


    def clear(self):
        config.my_board.grid[self.row][self.col] = self._reset 


    def show(self):
        config.my_board.grid[self.row][self.col] = self.shape 
    
    def activate(self):
        pass

    def deactivate(self):
        pass

    def set_position(self,new_row,new_col):

        self.row = new_row
        self.col = new_col
    
    def check_time(self):
        activated_time = round(time() - self.start_time)
        if(activated_time >  POWERUP_TIME):
            self.deactivate()
            return True
        return False
    
    def move(self):

        #CHECK IF IT CROSSED PADDLE
        if(config.my_paddle.row <= self.row):
            self.clear()
            self.delete = True
            return
        
        #CHECK IF COLLIDED WITH PADDLE
        if(config.my_board.hidden_grid[self.row+1][self.col] == 'P'):
            self.activate()
            self.clear()
            return
        
        #CHECK COLLISION AND MOVE

        if(self.show_mode == True):
            self.clear()

        if(config.my_board.hidden_grid[self.row + 1][self.col] == ' '):
            self.show_mode = True
        else:
            self.show_mode = False
        
        self.set_position(self.row+1,self.col)
        if(self.show_mode == True):
            self.show()



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


class Paddle_Grab(PowerUp):

    def __init__(self,row,col):
        super().__init__(row,col)
        self.shape = PADDLE_GRAB
    
    def activate(self):
        self.start_time = time()
        self.activated = True
        self.show_mode = False
        config.my_paddle.grab_func(config.my_paddle.grab + 1)
    
    def deactivate(self):
        config.my_paddle.grab_func(config.my_paddle.grab - 1)
        if(config.my_paddle.grab == 0):
            for my_ball in config.balls:
                my_ball.on_paddle = False
        self.activated = False
        