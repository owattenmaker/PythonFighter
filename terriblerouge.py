'''
The worst rouge like in existance
By: Owen Wattenmaker, Max Lambek

background taken from: http://legend-tony980.deviantart.com/art/Alternate-Kingdom-W1-Castle-Background-382965761
character model taken from: http://piq.codeus.net/picture/33378/chibi_knight
'''
#TODO
##################################################################
###	-Make the character not stop after finishing the attack    ###
###	-add in attack value                                       ###
###	-scrolling camera                                          ###
###	-Attacking enemys                                          ###
##################################################################

import pygame, sys, time, random
from pygame.locals import *

# set up pygame
pygame.init()

mainClock = pygame.time.Clock()
playerImage = pygame.image.load('character\player1\player1_right_stationary.png')
background = pygame.image.load('background.png')
computerimage = pygame.image.load('cherry.png')

# set up the window
WINDOWWIDTH = 1280
WINDOWHEIGHT = 570
r=0

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Worst Rouge Like')
playerStretchedImage = pygame.transform.scale(playerImage, (300, 300))
player = pygame.Rect(1, 300, 5, 5)
computer = pygame.Rect(750,400,10,10)

orientation = 'right'
airborn = False
moveLeft = False
moveRight = False
jump = False
MOVESPEED = 6

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			# change the keyboard variables
			if event.key == K_LEFT:
				moveRight = False
				moveLeft = True
				playerImage = pygame.image.load('knight_left.png')
				playerStretchedImage = pygame.transform.scale(playerImage, (300, 300))
				orientation = 'left'
				
			if event.key == K_RIGHT:
				moveLeft = False
				moveRight = True
				playerImage = pygame.image.load('knight_right.png')
				playerStretchedImage = pygame.transform.scale(playerImage, (300, 300))
				orientation = 'right'
				
			if event.key == K_UP and airborn == False:
				airborn = True
				verticalVelocity = 10
				player.top -= 1
				
			if event.key == ord('z'):
				moveLeft = False
				moveRight = False
				if orientation == 'right':
					playerImage = pygame.image.load('knight_right_attack.png')
					playerStretchedImage = pygame.transform.scale(playerImage, (300, 300))
				
				if orientation == 'left':
					playerImage = pygame.image.load('knight_left_attack.png')
					playerStretchedImage = pygame.transform.scale(playerImage, (300, 300))
				
		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == K_LEFT:
				moveLeft = False
			if event.key == K_RIGHT:
				moveRight = False			
			if event.key == ord('z'):
				if orientation == 'right':
					playerImage = pygame.image.load('knight_right.png')
					playerStretchedImage = pygame.transform.scale(playerImage, (300, 300))
				if orientation == 'left':
					playerImage = pygame.image.load('knight_left.png')
					playerStretchedImage = pygame.transform.scale(playerImage, (300, 300))

	computer.left -= MOVESPEED
	print player.top
	print player. left
	# move the player
	if moveLeft and player.left > 0:
		player.left -= MOVESPEED
	if moveRight and player.right < WINDOWWIDTH:
		player.right += MOVESPEED
	if airborn:
		print airborn
		verticalVelocity -= .56
		player.top -= verticalVelocity
		
		if player.top > 300:
			airborn = False
			
	print airborn 
	
	if player.top > 300:
		player.top = 300
		
		
	windowSurface.fill((r,0,0))
	windowSurface.blit(background,(0,0))
	#windowSurface.blit(player,(x - CameraX,y - CameraY))


	# draw the block onto the surface
	windowSurface.blit(playerStretchedImage, player)
	windowSurface.blit(computerimage, computer)
	
	# draw the window onto the screen
	pygame.display.update()
	mainClock.tick(60)

