from headers import *
import config

class Ball:

    def __init__(self):
        self.row = PADDLE_HT - 1
        self.col = config.my_paddle.col + math.floor(config.PADDLE_LEN/2)

        self.vel_horz = 0
        self.vel_vert = 1

        self._reset = Back.BLACK + ' ' + Back.RESET

        self.on_paddle = True
        self.thru_ball = 0

        self.dead = False


    def show(self):
        config.my_board.grid[self.row][self.col] = BALL

    def clear(self):
        config.my_board.grid[self.row][self.col] = self._reset
    

    def set_position(self,new_row,new_col):
        self.clear()

        self.row = new_row
        self.col = new_col

        self.show()
        
    
    def set_velocity(self,new_velHor,new_velVert):

        self.vel_horz = new_velHor
        self.vel_vert = new_velVert
    
    def set_thruBall(self,val):
        self.thru_ball = val
        

    def release(self):
        self.on_paddle = not self.on_paddle
        
    
    def simulate_path(self):

        #SIMULATE A PATH FROM CURR POS TO NEXT JUMP
        row,col = self.row,self.col
        end_r,end_c = self.row + (-1*self.vel_vert),self.col + self.vel_horz
        

        h = abs(end_c - col)
        v = abs(end_r - row)

        dir_row,dir_col = 0,0
        
        if(self.vel_vert != 0):
            dir_row = -1*int(self.vel_vert/abs(self.vel_vert))
        if(self.vel_horz != 0):
            dir_col = int(self.vel_horz/abs(self.vel_horz))

       

        
        l= []

        if(h == 0):
            for i in range(v):
                row += dir_row
                l.append((row,col))
            return l
        
        q,r = floor(h/(v+1)) , h%(v+1)
        for i in range(v+1):
            if(r >0):
                for j in range(q+1):
                    col+= dir_col
                    l.append((row,col))
                r -= 1
            else:
                for j in range(q):
                    col += dir_col
                    l.append((row,col))
            if(i < v):
                row+= dir_row
                l.append((row,col))
        return l
    
    def collide_brick(self,row,col,direction):
        
        for brick in config.my_bricks:
            if(brick.show_mode == False):
                continue
            
            cond1 = brick.row <= row
            cond2 = row < brick.row + BRICK_WIDTH
            cond3 = brick.col <= col
            cond4 = col < brick.col + BRICK_LENGTH

            if(cond1 and cond2 and cond3 and cond4):
                if(self.thru_ball > 0):
                    brick.break_brick(1)
                    return
                if(brick.strength != -1):
                    brick.break_brick(0)
                if(direction == 'horz'):
                    self.set_velocity(-1* self.vel_horz, self.vel_vert)
                elif(direction == 'vert' ):
                    self.set_velocity(self.vel_horz,-1* self.vel_vert)
                
                return

            
    def collide_wall(self,row,col,dir):

        #Check if ball hits ground
        if row >= PADDLE_HT:
            self.dead = True
            self.clear()
            return

        if(dir == 'horz'):
            self.set_velocity(-1* self.vel_horz, self.vel_vert)
        elif(dir == 'vert' ):
            self.set_velocity(self.vel_horz,-1* self.vel_vert)
        return



    def collide_paddle(self,row,col):
        
        dist = config.my_paddle.col + int(config.my_paddle._len/2) -  col
        dist = floor(dist/4)
        self.set_velocity((-1*dist+ self.vel_horz), -1*(self.vel_vert))

        if(config.my_paddle.grab > 0):
            self.on_paddle = True
        
        return

    def check_collision(self,row,col,direction):

        #CHECK IF COLLIDED WITH BRICK
        if(config.my_board.hidden_grid[row][col] == 'B'):
            self.collide_brick(row,col,direction)
            if(self.thru_ball > 0):
                return False
            return True
        #CHECK IF COLLIDED WITH WALL
        elif (config.my_board.hidden_grid[row][col] == 'W'):
            self.collide_wall(row,col,direction)
            return True
        #CHECK IF COLLIDED WITH PADDLE
        elif (config.my_board.hidden_grid[row][col] == 'P'):
            self.collide_paddle(row,col)
            return True
        
        return False


    def move(self):

        path = self.simulate_path()
        
        dir_row,dir_col = 0,0
        if(self.vel_vert != 0):
            dir_row = -1*int(self.vel_vert/abs(self.vel_vert))
        if(self.vel_horz != 0):
            dir_col = int(self.vel_horz/abs(self.vel_horz))


        end_row = self.row - self.vel_vert
        end_col = self.col + self.vel_horz
        

        #CHECK COLLISION FOR EVERY PIXEL IN THE PATH
        for pixel in path:
            new_row,new_col = pixel[0],pixel[1]
            val = self.check_collision(new_row+dir_row,new_col,'vert')
            if val == True:
                self.set_position(new_row,new_col)
                
                return 
            val = self.check_collision(new_row,new_col + dir_col,'horz')
            if val == True:
                self.set_position(new_row,new_col)
                return

        
        self.set_position(end_row,end_col)





    
    




        



