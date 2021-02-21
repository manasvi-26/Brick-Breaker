from getch import *
from headers import *
import config

#REPOSITION CURSOR TO (0,0)
def reposition_cursor(y,x):
    print("\033[%d;%dH" % (y, x), end="")


#TAKING INPUT
def take_input():
    
    getch = Get()
    ch = getChar(getch)

    if ch == 'q':
        Quit()
        os.system("stty echo")
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


def reset():
    
    #CREATE NEW BALL:
    for my_ball in config.balls:
        my_ball.clear()
        del my_ball
    
    

    #REMOVE POWERUPS:

    for powerup in config.my_powerups:
        if(powerup.show_mode == True):
            powerup.clear()

        if(powerup.activated == True):
            powerup.deactivate()

        del powerup

    config.my_powerups[:] = []

    config.balls[:] = []
    new_ball = config.ball.Ball()
    config.balls.append(new_ball)
    config.balls[0].show()




def print_headers():
    print(Fore.BLACK + Back.LIGHTCYAN_EX + Style.BRIGHT + "BRICK BREAKER".center(COL)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTCYAN_EX + Style.BRIGHT + "               ".center(COL)+Style.RESET_ALL)
    stats = str("LIVES: "+str(config.LIVES) + "  |  SCORE:" + str(config.SCORE)+"  |  TIME: " + str(config.CURR_TIME) + 's')
    print(Fore.BLACK + Back.LIGHTCYAN_EX + Style.BRIGHT + stats.center(COL)+Style.RESET_ALL)


def print_instructions():
    print(Fore.LIGHTCYAN_EX)
    BACK_COLORS.append(Back.RED)
    pos = 3

    reposition_cursor(pos,120)
    print('BRICKS : ')

    brick_types = ['BRICK STRENGTH = 1','BRICK STRENGTH = 2','BRICK STRENGTH = 3','UNBREAKABLE BRICK']
    pos -= 1
    for i in range(4):
        pos += 3
        reposition_cursor(pos,120)
        for r in range(BRICK_WIDTH):
            for c in range(BRICK_LENGTH):
                if(c== 0 or c == BRICK_LENGTH-1):
                    print(BACK_COLORS[i] + '|',end="" + Back.RESET) 
                else :
                    print(BACK_COLORS[i] + '-',end="" + Back.RESET) 
            if(r == 0):
                print(str('    ---   ') + brick_types[i])
            print()
            reposition_cursor(pos +1,120)
            

    BACK_COLORS.remove(Back.RED)

    pos += 4
    reposition_cursor(pos,120)
    print("CONTROLS : ")
    pos+=2
    reposition_cursor(pos,120)
    pos+=2
    print('Press \'a\' to move paddle LEFT')
    reposition_cursor(pos,120)
    pos+=2
    print('Press \'d\' to move paddle RIGHT')
    reposition_cursor(pos,120)
    pos+=2
    print('Press \'r\' to release ball from paddle')
    reposition_cursor(pos,120)
    pos+=2
    print('Press \'q\' to quit')
    reposition_cursor(pos,120)

    pos+= 1

    print("POWERUPS : ")
    
    for i in range(6):
        pos += 2
        reposition_cursor(pos,120)
        print(POWERUPS[i],end = "")
        print(Fore.LIGHTCYAN_EX + str('    ---   ') + powerup_names[i])

    print(Style.RESET_ALL)



def game_over():
    
    print(Fore.BLACK + Back.LIGHTCYAN_EX + Style.BRIGHT  +"GAME OVER :(".center(COL)+Style.RESET_ALL)                 
    print()

       

def win():
    print(Fore.BLACK + Back.LIGHTCYAN_EX + Style.BRIGHT +"YOU WON !!!GOOD JOB".center(COL)+Style.RESET_ALL)                 
    print()

def Quit():
    print(Fore.BLACK + Back.LIGHTCYAN_EX + Style.BRIGHT + "YOU QUIT :(".center(COL)+Style.RESET_ALL)                 
    print()