from getch import *
from headers import *
import config

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
        can_move = config.my_paddle.move('left')

        for my_ball in config.balls:
            on_paddle = my_ball.on_paddle

            #move ball if paddle has grabbed onto it
            if(can_move == True and on_paddle == True):
                my_ball.set_position(my_ball.row ,my_ball.col -config.my_paddle.delta)
            
            
    
    #MOVE PADDLE RIGHT
    if ch == 'd':
        can_move = config.my_paddle.move('right')
        
        for my_ball in config.balls:
            on_paddle = my_ball.on_paddle
            #move ball if paddle has grabbed onto it
            if(can_move == True and on_paddle == True):
                my_ball.set_position(my_ball.row ,my_ball.col +config.my_paddle.delta)
            


    #ONLY WORKS IF PADDLE HAS GRABBED ONTO BALL
    if ch == 'r':
        for my_ball in config.balls:
            if(my_ball.on_paddle == True):
                my_ball.release()



def create_powerup(row,col):

    val = random.choice([0,1,2,3,4,5])
    val = 3
    if val == 0:
        powerup = config.powerUp.Ball_Multiplier(row,col)
    
    if val == 1:
        powerup = config.powerUp.Thru_Ball(row,col)

    if val == 2:
        powerup = config.powerUp.Expand_Paddle(row,col)
    
    if val == 3:
        powerup = config.powerUp.Shrink_Paddle(row,col)
    
    if val == 4: 
        powerup = config.powerUp.Fast_Ball(row,col)
    
    if val == 5:
        powerup = config.powerUp.Paddle_Grab(row,col)

    

    config.my_powerups.append(powerup)


    

        

        