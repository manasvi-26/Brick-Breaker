from headers import *


class Ball:

    def __init__(self,PADDLE_LEN):
        self.row = PADDLE_HT - 1
        self.col = int((COL - 1 - PADDLE_LEN)/2 + math.floor(PADDLE_LEN/2))

        self.vel_horz = 0
        self.vel_vert = 1

        self._color = Fore.CYAN
        self._reset = Back.BLACK + ' ' + Back.RESET

        self.on_paddle = True

    def show(self,my_board):
        my_board.grid[self.row][self.col] = self._color + BALL

    def clear(self,my_board):
        my_board.grid[self.row][self.col] = self._reset
    

    def set_position(self,new_row,new_col,my_board):
        self.clear(my_board)

        self.row = new_row
        self.col = new_col

        self.show(my_board)
        
    
    def set_velocity(self,new_velHor,new_velVert):

        self.vel_horz = new_velHor
        self.vel_vert = new_velVert
        
        

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
    
    def collide_brick(self,row,col,my_bricks,my_board,direction):
        
        for brick in my_bricks:
            if(brick.show_mode == False):
                continue
            
            cond1 = brick.row <= row
            cond2 = row < brick.row + BRICK_WIDTH
            cond3 = brick.col <= col
            cond4 = col < brick.col + BRICK_LENGTH

            if(cond1 and cond2 and cond3 and cond4):
                if(brick.strength != -1):
                    brick.break_brick(my_board)
                if(direction == 'horz'):
                    self.set_velocity(-1* self.vel_horz, self.vel_vert)
                elif(direction == 'vert' ):
                    self.set_velocity(self.vel_horz,-1* self.vel_vert)
                
                return

            
    def collide_wall(self,row,col,my_board,dir):

        #Check if ball hits ground
        if row == ROW - 1:
            print('lol loser')
            exit()
        
        if(dir == 'horz'):
            self.set_velocity(-1* self.vel_horz, self.vel_vert)
        elif(dir == 'vert' ):
            self.set_velocity(self.vel_horz,-1* self.vel_vert)
        return



    def collide_paddle(self,row,col,my_paddle,my_board):
        
        dist = my_paddle.col + int(my_paddle._len/2) -  col
        dist = floor(dist/4)
        self.set_velocity((-1*dist+ self.vel_horz), -1*(self.vel_vert))
        
        return

    def check_collision(self,row,col,my_board,my_paddle,my_bricks,direction):

        #CHECK IF COLLIDED WITH BRICK
        if(my_board.hidden_grid[row][col] == 'B'):
            self.collide_brick(row,col,my_bricks,my_board,direction)
            return True
        #CHECK IF COLLIDED WITH WALL
        elif (my_board.hidden_grid[row][col] == 'W'):
            self.collide_wall(row,col,my_board,direction)
            return True
        #CHECK IF COLLIDED WITH PADDLE
        elif (my_board.hidden_grid[row][col] == 'P'):
            self.collide_paddle(row,col,my_paddle,my_board)
            return True
        
        return False


    def move(self,my_board,my_paddle,my_bricks):

        print(self.vel_horz,self.vel_vert)
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
            val = self.check_collision(new_row+dir_row,new_col,my_board,my_paddle,my_bricks,'vert')
            if val == True:
                self.set_position(new_row,new_col,my_board)
                
                return 
            val = self.check_collision(new_row,new_col + dir_col,my_board,my_paddle,my_bricks,'horz')
            if val == True:
                self.set_position(new_row,new_col,my_board)
                return

        
        self.set_position(end_row,end_col,my_board)





    
    




        



