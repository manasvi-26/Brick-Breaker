import os
from colorama import Fore, Back, Style,init
import numpy as np
import sys
import termios
import tty
import signal
from time import sleep,time
from math import floor 
import random
import math
from copy import deepcopy
from layout import *

init()


#FOR BOARD
ROW = 40
COL = 100


#FOR PADDLE
PADDLE_HT = 35
PADDLE_WD = 2
PADDLE='.'

#FOR BALL
BALL = Back.BLACK + Fore.LIGHTCYAN_EX + 'O' + Fore.RESET + Back.RESET


#FOR BRICKS
BRICK_LENGTH = 9
BRICK_WIDTH = 2


#BRICK LAYOUT


#STARTING COORDS OF EVER BRICK (2D MATRIX) 
LAYOUT1 = create_layout1(BRICK_LENGTH,BRICK_WIDTH)
LAYOUT2 = create_layout2(BRICK_LENGTH,BRICK_WIDTH)


#COLORS
BACK_COLORS = [Back.YELLOW, Back.GREEN, Back.BLUE]


#POWERUP

EXPAND_PADDLE = Back.LIGHTMAGENTA_EX+ Fore.BLACK + 'E' + Fore.RESET +Back.RESET
SHRINK_PADDLE = Back.LIGHTCYAN_EX + Fore.BLACK + 'S' + Fore.RESET + Back.RESET
BALL_MULTIPLIER = Back.LIGHTRED_EX  + Fore.BLACK + 'B' + Fore.RESET + Back.RESET
FAST_BALL = Back.LIGHTYELLOW_EX + Fore.BLACK + 'F' + Fore.RESET + Back.RESET
THRU_BALL = Back.LIGHTBLUE_EX + Fore.BLACK + 'T' + Fore.RESET + Back.RESET
PADDLE_GRAB =Back.LIGHTGREEN_EX + Fore.BLACK + 'P' + Fore.RESET + Back.RESET

POWERUPS = [EXPAND_PADDLE,SHRINK_PADDLE,BALL_MULTIPLIER,FAST_BALL,THRU_BALL,PADDLE_GRAB]
powerup_names = ['Expand Paddle','Shrink Paddle', 'Ball Multiplier', 'Fast Ball', 'Thru-ball', 'Paddle Grab']


POWERUP_TIME = 10
BRICK_FALLING = 20
