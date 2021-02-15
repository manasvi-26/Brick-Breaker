from getch import *
from headers import *

from board import *
from paddle import *
from bricks import *
from ball import *

#CREATE BOARD
my_board = Board()


#CREATE PADDLE
PADDLE_LEN = 17
my_paddle = Paddle(PADDLE_LEN)
my_paddle.show(my_board)

#CREATE BALL
my_ball = Ball(PADDLE_LEN)
my_ball.show(my_board)


#CREATE BRICKS
my_bricks = []
for coord in LAYOUT:
    my_brick = Brick(coord[0],coord[1])
    my_bricks.append(my_brick)

for brick in my_bricks:
    brick.show(my_board)


#REPOSITION CURSOR TO (0,0)
def reposition_cursor(x,y):
    print("\033[%d;%dH" % (x, y))


#TAKING INPUT
def take_input():
    
    getch = Get()
    ch = getChar(getch)

    if ch == 'q':
        print("AW you quit:(")
        exit()

    #MOVE PADDLE LEFT
    if ch == 'a':
        can_move = my_paddle.move('left',my_board)
        on_paddle = my_ball.on_paddle

        #move ball if paddle has grabbed onto it
        if(can_move == True and on_paddle == True):
            my_ball.set_position(my_ball.row ,my_ball.col -1,my_board)
            
            
    
    #MOVE PADDLE RIGHT
    if ch == 'd':
        can_move = my_paddle.move('right',my_board)
        on_paddle = my_ball.on_paddle

        #move ball if paddle has grabbed onto it
        if(can_move == True and on_paddle == True):
            my_ball.set_position(my_ball.row ,my_ball.col +1,my_board)
            


    #ONLY WORKS IF PADDLE HAS GRABBED ONTO BALL
    if ch == 'r':

        if(my_ball.on_paddle == True):
            my_paddle.grab_func()
            my_ball.release()
            my_ball.move(my_board,my_paddle,my_bricks)







    

        

        