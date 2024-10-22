#GLOBAL VARIABLES

from headers import *

import board 
import paddle
import bricks
import paddle
import bricks
import ball
import powerUp

#DEFINE LIVES
LIVES = 5

#DEFINE LEVELS
LEVEL = 1

#CREATE BOARD
my_board = board.Board()


#CREATE PADDLE
PADDLE_LEN = 17
my_paddle = paddle.Paddle()
my_paddle.show()

#CREATE BALL
balls = [ball.Ball()]
balls[0].show()


#CREATE BRICKS

BREAKABLE_BRICKS = 0

def create_bricks(LAYOUT):
    my_bricks = []
    
    for coord in LAYOUT:
        my_brick = bricks.Brick(coord[0],coord[1])
        my_bricks.append(my_brick)

    for brick in my_bricks:
        brick.show()

    return my_bricks

my_bricks = create_bricks(LAYOUT1)




#DEFINE POWERUP
my_powerups = []

START_TIME = 0
CURR_TIME = 0
SCORE = 0