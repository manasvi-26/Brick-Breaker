from headers import *

class Board:

    def __init__(self):
        self.__rows = ROW
        self.__cols = COL
        self.grid = []
        self.hidden_grid= []
        self._color = Back.BLACK 
        self._wall = Back.WHITE
        self.create_board()
    
    def create_board(self):
        self.grid = [[self._color + " " for j in range(COL)] for i in range(ROW)]
        self.hidden_grid = [[" " for j in range(COL)] for i in range(ROW)]

        for j in range(COL):
            self.grid[0][j] = self._wall + ' '
            self.grid[ROW-1][j] = self._wall + ' '
            
            self.hidden_grid[0][j] = 'W'
            self.hidden_grid[ROW-1][j] =  'W'
        for i in range(ROW):
            self.grid[i][0] = self._wall + ' '
            self.grid[i][1] = self._wall + ' '
            
            self.hidden_grid[i][0] = 'W'
            self.hidden_grid[i][1] = 'W'

            self.grid[i][COL-1] = self._wall + ' '
            self.grid[i][COL-2] = self._wall + ' '
            
            self.hidden_grid[i][COL-1] = 'W'
            self.hidden_grid[i][COL-2] = 'W'



    def print_board(self):
        print()
        for i in range(ROW):
            for j in range(COL):
                print(self.grid[i][j],end='') 
                

            print()
        print(Style.RESET_ALL)
    

