from utility import *
import config
from config import *

os.system('clear')

config.START_TIME = time()

os.system("stty -echo")
reposition_cursor(0, 0)
print_instructions()

while True :
    
    take_input()
    reposition_cursor(0, 0)

    if(BREAKABLE_BRICKS == 0):
        yay()
        break

    config.CURR_TIME = round(time() - config.START_TIME)

    print_headers()
    my_board.print_board()

    #CHECK LIVES REMAINING
    val = False
    if(len(balls) == 0):
        val = True

    if(val == True):
        config.LIVES -= 1

    if(val == True and config.LIVES >= 0):
        reset()
    if (val == True and config.LIVES < 0):
        game_over()
        break

    #MOVE BALL
    for my_ball in balls:
        if(my_ball.dead == True):
            my_ball.clear()
            balls.remove(my_ball)
            del my_ball

        elif(my_ball.on_paddle == False and my_ball.dead == False):
            my_ball.move()
    
    #CHECK POWERUPS
    for powerup in my_powerups:

        if powerup.delete == True:
            my_powerups.remove(powerup)
        
        elif powerup.activated == True:
            val = powerup.check_time()
            if(val == True):
                my_powerups.remove(powerup)
                del powerup
        else:
            powerup.move()
            



os.system("stty echo")