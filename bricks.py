from headers import *
import config
import utility


class Brick:

    def __init__(self,row,col):
        self.row = row
        self.col = col

        self.pick_brick()
        self.show_mode = True

        self._reset = Back.BLACK + ' ' + Back.RESET
    
    def pick_brick(self):

        choice = random.uniform(0,1)
        if(choice <= 0.2):
            self.color = Back.RED
            self.strength =  -1
        else:
            config.BREAKABLE_BRICKS += 1
            self.color = random.choice(BACK_COLORS)
            
            if self.color == Back.YELLOW:
                self.strength = 1
            if self.color == Back.GREEN:
                self.strength = 2
            if self.color == Back.BLUE:
                self.strength = 3    

    def show(self):

        for i in range(BRICK_WIDTH):
            for j in range(BRICK_LENGTH):
                config.my_board.hidden_grid[self.row + i][self.col+j] = 'B' 

                if(j== 0 or j == BRICK_LENGTH-1):
                    config.my_board.grid[self.row + i][self.col+j] = self.color + Fore.BLACK + '|' 
                else :
                    config.my_board.grid[self.row + i][self.col+j] = self.color + Fore.BLACK + '-' 
    
    def clear(self):

        for i in range(BRICK_WIDTH):
            for j in range(BRICK_LENGTH):
                
                config.my_board.grid[self.row + i][self.col+j] = self._reset       
                config.my_board.hidden_grid[self.row + i][self.col+j] = ' ' 


    def move(self):

        clear()
        self.col = self.col - 1
        show()




    def powerup_check(self):
       
        config.BREAKABLE_BRICKS -= 1

        val = random.uniform(0,1)
        if(val < 0.7):
            utility.create_powerup(self.row,self.col+int(BRICK_LENGTH/2))

    def break_brick(self,type):
        config.SCORE += 5
        if(type == 0):
            self.strength -= 1
            if self.strength == 0:
                self.clear()
                self.show_mode = False
                self.powerup_check()


            if self.strength == 1:
                self.color = Back.YELLOW
                self.show()
            if self.strength == 2:
                self.color = Back.GREEN
                self.show()
        
        if(type == 1):
        
            if(self.strength > 0):
                self.powerup_check()
            self.clear()
            self.strength = 0
            self.show_mode = False
            



        
            
        




        
