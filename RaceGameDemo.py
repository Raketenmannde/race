#!/usr/bin/python3
import pgzrun
from random import randint  		# import the randint class from random module

WIDTH = 700         # width of the window
HEIGHT = 800        # height of the window
car = Actor("racecar")
car.pos = 350, 560
trackLeft = [] 		# list to store left barries
trackRight = [] 	# list to store right barries
trackCount = 0		# count the number of barries
trackPosition = 350
trackWidth = 150	# width between left and right barries
trackDirection = False
SPEED = 4				# sets the speed of the game


def draw():             # pygame zero draw function
    screen.fill((128, 128, 128))    # fill the screen with
    car.draw()
    b = 0
    while b < len(trackLeft):
    	trackLeft[b].draw()
    	trackRight[b].draw()
    	b +=1


pgzrun.go()
