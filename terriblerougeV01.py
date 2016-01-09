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
playerImage = pygame.image.load('knight_right.png')
background = pygame.image.load('background.png')
computerimage = pygame.image.load('cherry.png')


# set up the window
WINDOWWIDTH = 1280
WINDOWHEIGHT = 570
r=0

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Worst Rouge Like')
playerStretchedImage = pygame.transform.scale(playerImage, (150, 150))
player = pygame.Rect(1, 400, 5, 5)
computer = pygame.Rect(750,400,10,10)

orientation = 'right'
airborn = False
moveLeft = False
moveRight = False
MOVESPEED = 6
	
def movement(moveLeft, moveRight, player_left, player_right, MOVESPEED, WINDOWWIDTH):
	# move the player
	if moveLeft and player_left > 0:
		player_right -= MOVESPEED
	if moveRight and player_right < WINDOWWIDTH:
		player_right += MOVESPEED
	
	return player_left, player_right

def jumping(player_top, airborn, verticalVelocity):
	if airborn:
		print verticalVelocity
		verticalVelocity -= .56
		print verticalVelocity, 'new'
		player_top += verticalVelocity
	
	if player_top >= 400:
		airborn = False
	
	return player_top, airborn, verticalVelocity
	
def main(orientation, airborn, moveLeft, moveRight, MOVESPEED):
	mainClock = pygame.time.Clock()
	playerImage = pygame.image.load('knight_right.png')
	background = pygame.image.load('background.png')
	computerimage = pygame.image.load('cherry.png')

	# set up the window
	WINDOWWIDTH = 1280
	WINDOWHEIGHT = 570
	r=0

	#set display surface and the player and computer hitbox and position
	windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
	pygame.display.set_caption('Worst Rouge Like')
	playerStretchedImage = pygame.transform.scale(playerImage, (150, 150))
	player = pygame.Rect(1, 400, 5, 5)
	computer = pygame.Rect(750,400,10,10)
	verticalVelocity = 0
	
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
					playerStretchedImage = pygame.transform.scale(playerImage, (150, 150))
					orientation = 'left'
					
				if event.key == K_RIGHT:
					moveLeft = False
					moveRight = True
					playerImage = pygame.image.load('knight_right.png')
					playerStretchedImage = pygame.transform.scale(playerImage, (150, 150))
					orientation = 'right'
					
				if event.key == K_UP and airborn == False:
					print 'here'
					airborn = True
					verticalVelocity = 10
					player.top -= 1
					
				if event.key == ord('z'):
					moveLeft = False
					moveRight = False
					if orientation == 'right':
						playerImage = pygame.image.load('knight_right_attack.png')
						playerStretchedImage = pygame.transform.scale(playerImage, (150, 150))
					
					if orientation == 'left':
						playerImage = pygame.image.load('knight_left_attack.png')
						playerStretchedImage = pygame.transform.scale(playerImage, (150, 150))
					
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
						playerStretchedImage = pygame.transform.scale(playerImage, (150, 150))
					if orientation == 'left':
						playerImage = pygame.image.load('knight_left.png')
						playerStretchedImage = pygame.transform.scale(playerImage, (150, 150))

		computer.left -= MOVESPEED
		#moveplayer
		player.left, player.right = movement(moveLeft, moveRight, player.left, player.right, MOVESPEED, WINDOWWIDTH)
		
		#jump player
		player.top, airborn, verticalVelocity = jumping(player.top, airborn, verticalVelocity)
		
		#if player.top > 400:
		#	player.top = 400
			
			
		windowSurface.fill((r,0,0))
		windowSurface.blit(background,(0,0))
		#windowSurface.blit(player,(x - CameraX,y - CameraY))


		# draw the block onto the surface
		windowSurface.blit(playerStretchedImage, player)
		windowSurface.blit(computerimage, computer)
		
		# draw the window onto the screen
		pygame.display.update()
		mainClock.tick(60)

main(orientation, airborn, moveLeft, moveRight, MOVESPEED)
