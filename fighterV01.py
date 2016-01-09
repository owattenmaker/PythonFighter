'''
Worst fighting game ever
By: Owen Wattenmaker, Max Lambek
'''
#TODO
############################################################################################
###	-add in frames for attacking, looks too choppy, need more pictures  				 ###
###	-fix yellow hit marker					                 							 ###
###	-fix framerate issues when loading background                                        ###
###	-add knockback				                      		   							 ###
### -														   							 ###
### -walking animation, possibly this: http://www.pygame.org/project-GIFImage-1039-.html ###
############################################################################################

import pygame, sys, time, random, os
from pygame.locals import *
#from GIFImage import GIFImage

#change this to false to disable the background and vastly improve performance
draw_background = False

def spriteMask(sprite, player, state):
	sprite.mask = pygame.mask.from_surface(player[state])
	return sprite
	
def dplayer1():
	if os.name == 'nt':
		#right stationary
		StationaryRight = pygame.transform.scale(pygame.image.load('character\player1\player1_right_stationary.png'), (350, 350))
		#left stationary
		StationaryLeft = pygame.transform.scale(pygame.image.load('character\player1\player1_left_stationary.png'), (350, 350))
		#right punch
		PunchRight = pygame.transform.scale(pygame.image.load('character\player1\player1_right_punch.png'), (350, 350))
		#left punch
		PunchLeft = pygame.transform.scale(pygame.image.load('character\player1\player1_left_punch.png'), (350, 350))
		#right kick
		KickRight = pygame.transform.scale(pygame.image.load('character\player1\player1_right_kick.png'), (350, 350))
		#left kick
		KickLeft = pygame.transform.scale(pygame.image.load('character\player1\player1_left_kick.png'), (350, 350))
		
	else:
		#right stationary
		StationaryRight = pygame.transform.scale(pygame.image.load('character/player1/player1_right_stationary.png'), (350, 350))
		#left stationary
		StationaryLeft = pygame.transform.scale(pygame.image.load('character/player1/player1_left_stationary.png'), (350, 350))
		#right punch
		PunchRight = pygame.transform.scale(pygame.image.load('character/player1/player1_right_punch.png'), (350, 350))
		#left punch
		PunchLeft = pygame.transform.scale(pygame.image.load('character/player1/player1_left_punch.png'), (350, 350))
		#right kick
		KickRight = pygame.transform.scale(pygame.image.load('character/player1/player1_right_kick.png'), (350, 350))
		#left kick
		KickLeft = pygame.transform.scale(pygame.image.load('character/player1/player1_left_kick.png'), (350, 350))
		
	player1 = {'right_stationary':StationaryRight, 'left_stationary':StationaryLeft, 'right_punch':PunchRight, 'left_punch':PunchLeft, 'right_kick':KickRight, 'left_kick':KickLeft}
	return player1

def dplayer2():	
	if os.name == 'nt':
		#right stationary
		StationaryRight = pygame.transform.scale(pygame.image.load('character\player2\player2_right_stationary.png'), (350, 350))
		#left stationary
		StationaryLeft = pygame.transform.scale(pygame.image.load('character\player2\player2_left_stationary.png'), (350, 350))
		#right punch
		PunchRight = pygame.transform.scale(pygame.image.load('character\player2\player2_right_punch.png'), (350, 350))
		#left punch
		PunchLeft = pygame.transform.scale(pygame.image.load('character\player2\player2_left_punch.png'), (350, 350))
		#right kick
		KickRight = pygame.transform.scale(pygame.image.load('character\player2\player2_right_kick.png'), (350, 350))
		#left kick
		KickLeft = pygame.transform.scale(pygame.image.load('character\player2\player2_left_kick.png'), (350, 350))

	else:
		StationaryRight = pygame.transform.scale(pygame.image.load('character/player2/player2_right_stationary.png'), (350, 350))
		#left stationary
		StationaryLeft = pygame.transform.scale(pygame.image.load('character/player2/player2_left_stationary.png'), (350, 350))
		#right punch
		PunchRight = pygame.transform.scale(pygame.image.load('character/player2/player2_right_punch.png'), (350, 350))
		#left punch
		PunchLeft = pygame.transform.scale(pygame.image.load('character/player2/player2_left_punch.png'), (350, 350))
		#right kick
		KickRight = pygame.transform.scale(pygame.image.load('character/player2/player2_right_kick.png'), (350, 350))
		#left kick
		KickLeft = pygame.transform.scale(pygame.image.load('character/player2/player2_left_kick.png'), (350, 350))
		
	player2 = {'right_stationary':StationaryRight, 'left_stationary':StationaryLeft, 'right_punch':PunchRight, 'left_punch':PunchLeft, 'right_kick':KickRight, 'left_kick':KickLeft}
	return player2
	
def collision(sprite1, sprite2):
	a = pygame.sprite.collide_mask(sprite1, sprite2)
	return a
	
def movement(moveLeft, moveRight, player_left, player_right, MOVESPEED, WINDOWWIDTH):
	# move the player
	if moveLeft and player_left > -100:
		player_right -= MOVESPEED
	if moveRight and player_right < WINDOWWIDTH - 300:
		player_right += MOVESPEED
	
	return player_left, player_right

def jumping1(player_top, airborn, verticalVelocity):
	if airborn:
		verticalVelocity += .7
		player_top += verticalVelocity
	
	if player_top >= 360:
		airborn = False
	
	return player_top, airborn, verticalVelocity
	
def jumping2(player_top, airborn, verticalVelocity):
	if airborn:
		verticalVelocity += .7
		player_top += verticalVelocity
	
	if player_top >= 360:
		airborn = False
	
	return player_top, airborn, verticalVelocity
	
def score(hpplayer1, hpplayer2, punch1, kick1, punch2, kick2, hit):
	if punch1:
		hpplayer2 -= random.randint(23, 33)
		hit = True
	if kick1:
		hpplayer2 -= random.randint(38, 45)
		hit = True
	if punch2:
		hpplayer1 -= random.randint(23, 33)
		hit = True
	if kick2:
		hpplayer1 -= random.randint(38, 45)
		hit = True
	
	return hpplayer1, hpplayer2, hit
	
def main():
	i = 0
	# set up pygame
	pygame.init()
	
	font = pygame.font.SysFont("monospace", 72)
	mainClock = pygame.time.Clock()
	background = pygame.transform.scale(pygame.image.load('background.jpg'), (1300, 1300))
	hit_background = pygame.transform.scale(pygame.image.load('flash_back.png'), (1300, 1300))
	
	# set up the window
	WINDOWWIDTH = 1280
	WINDOWHEIGHT = 760
	r=0
	
	windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
	pygame.display.set_caption('Terrible Fighting Game')
	rectplayer1 = pygame.Rect(1, 360, 5, 5)
	rectplayer2 = pygame.Rect(600, 360, 5, 5)
	splayer1 = pygame.sprite.Sprite()
	splayer1.image = pygame.transform.scale(pygame.image.load('character/player1/player1_right_stationary.png'), (350, 350))
	splayer1.rect = splayer1.image.get_rect()
	splayer1.rect.topleft = [0, 350]
	
	splayer2 = pygame.sprite.Sprite()
	splayer2.image = pygame.transform.scale(pygame.image.load('character/player1/player1_right_stationary.png'), (350, 350))
	splayer2.rect = splayer2.image.get_rect()
	splayer2.rect.topleft = [450, 350]
	
	#hit_effect = pygame.transform.scale(pygame.image.load('hit_effect.png'), (100, 100))
	
	hit = False
	collide = False
	airborn1 = False
	airborn2 = False
	moveLeft1 = False
	moveLeft2 = False
	moveRight1 = False
	moveRight2 = False
	MOVESPEED = 6
	
	orientation1 = 'right'
	orientation2 = 'left'
	state1 = 'right_stationary'
	state2 = 'left_stationary'
	
	verticalVelocity1 = 0
	verticalVelocity2 = 0
	
	hpplayer1 = 500
	hpplayer2 = 500
	
	player1 = dplayer1()
	player2 = dplayer2()
	gameStart = False
	while not gameStart:
		windowSurface.blit(background,(0,-450))
		windowSurface.blit(hit_background, [0,0])
		pressenter = font.render('<Press enter to start>', 1, (255, 255, 0))
		windowSurface.blit(pressenter, [150, 400])
		
		for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				pressed_keys = pygame.key.get_pressed()
				if pressed_keys[K_KP_ENTER] or pressed_keys[K_RETURN]:
					gameStart = True
		
		pygame.display.update()
		
	while True:
		while hpplayer1 > 0 and hpplayer2 > 0:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
					
				pressed_keys = pygame.key.get_pressed()
				
				#player1
				if pressed_keys[K_a]:
					moveLeft1 = True
					moveRight1 = False
					orientation1 = 'left'
					state1 = 'left_stationary'
				if pressed_keys[K_d]:
					moveLeft1 = False
					moveRight1 = True
					orientation1 = 'right'
					state1 = 'right_stationary'
				
				if pressed_keys[K_w]:
					if not airborn1:
						airborn1 = True
						verticalVelocity1 = -20
				
				#player2
				if pressed_keys[K_LEFT]:
					moveLeft2 = True
					moveRight2 = False
					orientation2 = 'left'
					state2 = 'left_stationary'
				if pressed_keys[K_RIGHT]:
					moveLeft2 = False
					moveRight2 = True
					orientation2 = 'right'
					state2 = 'right_stationary'
				
				if pressed_keys[K_UP]:
					if not airborn2:
						airborn2 = True
						verticalVelocity2 = -20
				
				#player1
				if not pressed_keys[K_a]:
					moveLeft1 = False
				if not pressed_keys[K_d]:
					moveRight1 = False
				#player2	
				if not pressed_keys[K_LEFT]:
					moveLeft2 = False
				if not pressed_keys[K_RIGHT]:
					moveRight2 = False
				
				if event.type == KEYDOWN:
					# change the keyboard variables
					#player1
					if event.key == ord('t'):
						kick1 = True
						if not airborn1:
							moveLeft1 = False
							moveRight1 = False
							if orientation1 == 'right':
								state1 = 'right_kick'
							if orientation1 == 'left':
								state1 = 'left_kick'
						if airborn1:
							if orientation1 == 'right':
								state1 = 'right_kick'
							if orientation1 == 'left':
								state1 = 'left_kick'
								
					if event.key == ord('y'):
						punch1 = True
						if not airborn1:	
							moveLeft = False
							moveRight = False
							if orientation1 == 'right':
								state1 = 'right_punch'
							if orientation1 == 'left':
								state1 = 'left_punch'
						if airborn1:
							if orientation1 == 'right':
								state1 = 'right_punch'
							if orientation1 == 'left':
								state1 = 'left_punch'	
								
					#player2
					if event.key == ord('.'):
						kick2 = True
						if not airborn2:
							moveLeft2 = False
							moveRight2 = False
							if orientation2 == 'right':
								state2 = 'right_kick'
							if orientation2 == 'left':
								state2 = 'left_kick'
						if airborn2:
							if orientation2 == 'right':
								state2 = 'right_kick'
							if orientation2 == 'left':
								state2 = 'left_kick'
								
					if event.key == ord('/'):
						punch2 = True
						if not airborn2:	
							moveLeft2 = False
							moveRight2 = False
							if orientation2 == 'right':
								state2 = 'right_punch'
							if orientation2 == 'left':
								state2 = 'left_punch'
						if airborn2:
							if orientation2 == 'right':
								state2 = 'right_punch'
							if orientation2 == 'left':
								state2 = 'left_punch'	
				
				if event.type == KEYUP:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
					
					#player1
					if event.key == ord('t') and orientation1 == 'right':
						state1 = 'right_stationary'
					
					if event.key == ord('t') and orientation1 == 'left':
						state1 = 'left_stationary'
					
					if event.key == ord('y') and orientation1 == 'right':
						state1 = 'right_stationary'
					
					if event.key == ord('y') and orientation1 == 'left':
						state1 = 'left_stationary'
					
					#player2
					if event.key == ord('.') and orientation2 == 'right':
						state2 = 'right_stationary'
					
					if event.key == ord('.') and orientation2 == 'left':
						state2 = 'left_stationary'
					
					if event.key == ord('/') and orientation2 == 'right':
						state2 = 'right_stationary'
					
					if event.key == ord('/') and orientation2 == 'left':
						state2 = 'left_stationary'
			
			#sprite.mask = pygame.mask.from_surface(sprite.image)
			#moveplayer
			rectplayer1.left, rectplayer1.right = movement(moveLeft1, moveRight1, rectplayer1.left, rectplayer1.right, MOVESPEED, WINDOWWIDTH)
			rectplayer2.left, rectplayer2.right = movement(moveLeft2, moveRight2, rectplayer2.left, rectplayer2.right, MOVESPEED, WINDOWWIDTH)
			
			#jump player
			rectplayer1.top, airborn1, verticalVelocity1 = jumping1(rectplayer1.top, airborn1, verticalVelocity1)
			rectplayer2.top, airborn2, verticalVelocity2 = jumping2(rectplayer2.top, airborn2, verticalVelocity2)
			
			if draw_background:
				windowSurface.blit(background,(0,-450))
			else:
				windowSurface.fill((50,50,50))
			
			#assign the image state to the sprite
			splayer1.image = player1[state1]
			splayer2.image = player2[state2]
			
			#do the mask, do the monster mask, it was a 2 player smash
			splayer1.mask = pygame.mask.from_surface(splayer1.image)
			splayer2.mask = pygame.mask.from_surface(splayer2.image)
			
			#assign the player rectangle to the sprite
			splayer1.rect.topleft = [rectplayer1.left, rectplayer1.top]
			splayer2.rect.topleft = [rectplayer2.left, rectplayer2.top]
			
			hitcoordinates = collision(splayer1, splayer2)
			#hitcoordinates = pygame.sprite.collide_mask(splayer1, splayer2)
			
			if hitcoordinates != None:
				hpplayer1, hpplayer2, hit = score(hpplayer1, hpplayer2, punch1, kick1, punch2, kick2, hit)
			
			if hit:
				windowSurface.blit(hit_background, [0,0])
			
			pygame.draw.rect(windowSurface, (216,0,0), (620,30,-500,30), 0)
			pygame.draw.rect(windowSurface, (216,0,0), (660,30, 500,30), 0)
			
			if hpplayer1 > 0:
				pygame.draw.rect(windowSurface, (19,193,0), (620,30,-hpplayer1,30), 0)
			
			if hpplayer2 > 0:
				pygame.draw.rect(windowSurface, (19,193,0), (660,30, hpplayer2,30), 0)
			
			#draw players	
			windowSurface.blit(splayer1.image, splayer1.rect)
			windowSurface.blit(splayer2.image, splayer2.rect)
			
			#if hit:
			#	windowSurface.blit(hit_effect, [hitcoordinates[0] - 40 , hitcoordinates[1] + 324])
			
			#draw the window onto the screen
			pygame.display.update()
			
			#pause for dramatic effect
			if hit:
				pygame.time.delay(350)
				hit = False
			
			mainClock.tick(60)
			
			punch1 = False
			punch2 = False
			kick1 = False
			kick2 = False
		
		if hpplayer1 > 0:
			print 'Player 1 wins!'
			return 0
		if hpplayer2 > 0:
			print 'Player 2 wins!'
			return 0	

main()
