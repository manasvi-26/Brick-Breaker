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

init()

#FOR BOARD
ROW = 40
COL = 100


#FOR PADDLE
PADDLE_HT = 35
PADDLE_WD = 2
PADDLE='.'

#FOR BALL
BALL = 'O'


#FOR BRICKS
BRICK_LENGTH = 9
BRICK_WIDTH = 2


#BRICK LAYOUT

def create_layout():

    list = []
    row = 5
    start_col = 5
    end_col = 86

    col = 5
    for r in range(5):
        
        for i in range(10):
            list.append((row,col))
            col+= BRICK_LENGTH
       
        row+= BRICK_WIDTH
        col = start_col

    for r in [4,3,2,1]:
        
        col = start_col
        for i in range(r):
            list.append((row,col))   
            col +=  BRICK_LENGTH
     
        col = end_col
        for i in range(r):
            list.append((row,col))
            col -= BRICK_LENGTH
        
        row += BRICK_WIDTH
    return list

#STARTING COORDS OF EVER BRICK (2D MATRIX) 
LAYOUT = create_layout()


#COLORS
BACK_COLORS = [Back.YELLOW, Back.GREEN, Back.BLUE]


#POWERUP

EXPAND_PADDLE = Fore.LIGHTCYAN_EX + 'E' + Fore.RESET
SHRINK_PADDLE = Fore.LIGHTCYAN_EX + 'S' + Fore.RESET
BALL_MULTIPLIER = Fore.LIGHTCYAN_EX  + 'B' + Fore.RESET
FAST_BALL = Fore.LIGHTCYAN_EX + 'F' + Fore.RESET
THRU_BALL = Fore.LIGHTCYAN_EX + 'T' + Fore.RESET
PADDLE_GRAB =Fore.LIGHTCYAN_EX + 'P' + Fore.RESET


POWERUP_CNT = 20
POWERUP_TIME = 5

