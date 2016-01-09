"""
Today we're going to talk about pygame: http://pygame.org/wiki/about,
a set of python modules for creating games and multimedia applications.


Dana Hughes
02-Oct-2013

Rhonda Hoenigman
Spring, 2014

A simple bug / flower game using pygame.  

Images are from opengameart.org
"""


# Common modules to import
#import pygame
from pygame.locals import *

import random
import os, pygame.mixer, pygame.time

def main():
	# Some constants for use later 
	GAME_TITLE = "My Awesome Bug & Flower Game"
	DISPLAY_SIZE = (640,480)     # Size of the screen for the game (in pixels)
	DESIRED_FPS = 30             # We want our game to run at 30 Frames per second

	# Initialize pygame
	'''
	With the sound example, we also saw that pygame needed to be 
	initialized. There it was initializing the mixer.
	'''
	pygame.init()
	
	'''
	pygame mixer is the sound engine for playing sound. 
	'''
	pygame.mixer.init(22050,8,1,2048)
	
	# Create a display for the game (this creates a window)
	'''
	Use constants created earlier to set size and title of game window
	'''
	screen = pygame.display.set_mode(DISPLAY_SIZE)
	pygame.display.set_caption(GAME_TITLE)

	# Create a clock to try to keep the game running at however many FPS
	fps_clock = pygame.time.Clock()

	# Initial game variables
	'''
	This is important. We need a way of controlling how long the game
	runs, we want the user to have a way of saying they are ready to
	stop playing. The game_running variable serves that purpose.
	'''
	game_running = True          # Is the player still playing?

	'''
	This sets the bugs starting position. You can change these numbers,
	and as long as they are less than the total screen size, you will
	change the initial position of the bug on the screen. Try putting 
	the bug at 0,0 and see what happens.
	
	We can modify the x and y values to see where it puts the bug.
	
	The y position is the vertical position on the screen, and the x
	position is the horizontal position on the screen.
	'''
	bug_x = 300                  # The bug's starting position
	bug_y = 240

	'''
	Just like the bug, the flower has a starting position. You can move
	the flower around by putting the flower at different x,y values.
	'''
	flower_x = 100               # The flower's starting position
	flower_y = 100

	score = 0                    # How many flowers did the player get

	bug_color = "red"            # What color is the bug?

	# Load the images
	background = pygame.image.load("background.png")
	red_bug = pygame.image.load("red_bug.png")
	blue_bug = pygame.image.load("blue_bug.png")
	flower = pygame.image.load("flower.png")

	bug = red_bug                # The bug image is currently the red one

	# The main game loop
	'''
	Here's the game_running variable. It's currently set to True, so when
	this line executes, the program will go into the while loop
	'''
	while game_running:          # Keep going until the player quits

		'''We've talked about user input using input and using the 
		command line. Here, we're introducing another kind of input
		in the form of an event. The program can respond to keyboard
		and mouse clicks, and respond accordingly to which keys were
		pressed or where on the screen the mouse was clicked.
		
		Google pygame.event.get for more information. Events are added
		to a queue and processed in the order they were received.
		'''
		user_input = pygame.event.get()

		'''
		Pygame has built-in functionality for detecting keys pressed on
		the keyboard. The get_presed() event will capture the key that
		the user pressed and your program can respond accordingly. There
		is some code here that has been commented out. If you put it 
		back, you can see what key was pressed because it will print in
		the terminal.
		'''
		pressed_keys = pygame.key.get_pressed()    # Which keys are down?

		if pressed_keys[K_q]:
			print("The 'q' key is pressed.")

		# Does the user want to quit?
		
		if pressed_keys[K_q]:
			game_running = False

		# Should we move the bug?
		'''
		Here, we will update the bugs position by looking for keys 
		press and responding accordingly. If the UP key is pressed, we
		will change the bugs position to go up one, for example.
		'''

		#####################################
		### Redraw the game on the screen ###
		#####################################
		#we redraw the screen because the bug's position may have changed
		screen.blit(background, (0,0))             # Draw the background
		screen.blit(flower, (flower_x, flower_y))  # Then the flower
		screen.blit(bug, (bug_x, bug_y))       # And the bug

		pygame.display.flip()                      # All done drawing! 

		# Wait until this frame is finished (as per the FPS clock)
		fps_clock.tick(DESIRED_FPS)

	# Finished the game?  Need to clean up!

	pygame.quit()
	print "The final score is:", score

main()
