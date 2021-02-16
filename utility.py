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
        on_paddle = config.my_ball.on_paddle

        #move ball if paddle has grabbed onto it
        if(can_move == True and on_paddle == True):
            config.my_ball.set_position(config.my_ball.row ,config.my_ball.col -config.my_paddle.delta)
            
            
    
    #MOVE PADDLE RIGHT
    if ch == 'd':
        can_move = config.my_paddle.move('right')
        on_paddle = config.my_ball.on_paddle

        #move ball if paddle has grabbed onto it
        if(can_move == True and on_paddle == True):
            config.my_ball.set_position(config.my_ball.row ,config.my_ball.col +config.my_paddle.delta)
            


    #ONLY WORKS IF PADDLE HAS GRABBED ONTO BALL
    if ch == 'r':

        if(config.my_ball.on_paddle == True):
            config.my_paddle.grab_func()
            config.my_ball.release()
            config.my_ball.move()






    

        

        