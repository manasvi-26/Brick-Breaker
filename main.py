from utility import *
from config import *

os.system('clear')
my_board.print_board()

os.system("stty -echo")

while True :
    
    take_input()
    reposition_cursor(0, 0)
    my_board.print_board()

    for my_ball in balls:
        if(my_ball.on_paddle == False):
            my_ball.move()

os.system("stty -echo")