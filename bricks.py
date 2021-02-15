from headers import *

class Brick:

    def __init__(self,row,col):
        self.row = row
        self.col = col

        self.pick_brick()
        self.show_mode = True

        self._reset = Back.BLACK
    
    def pick_brick(self):

        choice = random.uniform(0,1)
        if(choice <= 0.2):
            self.color = Back.RED
            self.strength =  -1
        else:
            self.color = random.choice(BACK_COLORS)
            
            if self.color == Back.YELLOW:
                self.strength = 1
            if self.color == Back.GREEN:
                self.strength = 2
            if self.color == Back.BLUE:
                self.strength = 3    

    def show(self,my_board):

        for i in range(BRICK_WIDTH):
            for j in range(BRICK_LENGTH):
                my_board.hidden_grid[self.row + i][self.col+j] = 'B' 

                if(j== 0 or j == BRICK_LENGTH-1):
                    my_board.grid[self.row + i][self.col+j] = self.color + Fore.BLACK + '|' 
                else :
                    my_board.grid[self.row + i][self.col+j] = self.color + Fore.BLACK + '-' 
    
    def clear(self,my_board):

        for i in range(BRICK_WIDTH):
            for j in range(BRICK_LENGTH):
                
                my_board.grid[self.row + i][self.col+j] = self._reset + ' ' 
                
                my_board.hidden_grid[self.row + i][self.col+j] = ' ' 

       

    def break_brick(self,my_board):

        self.strength -= 1
        if self.strength == 0:
            self.clear(my_board)
            self.show_mode = False
        if self.strength == 1:
            self.color = Back.YELLOW
            self.show(my_board)
        if self.strength == 2:
            self.color = Back.GREEN
            self.show(my_board)
        
            
        




        
