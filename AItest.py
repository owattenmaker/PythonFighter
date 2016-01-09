import pygame
import random
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,480))
clock=pygame.time.Clock()

px=35
py=35
prect=pygame.Rect(px-10,py-10,20,20)

class Enemy(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.rad=random.randint(5,10)
		self.rect=pygame.Rect(0,0,0,0)
		self.x_dir = random.choice(('left','right'))
		self.y_dir = random.choice(('up','down'))
	def move(self, mode='chase'):
		if mode=='chase':
			if self.x>px:
				self.x-=1
			elif self.x<px:
				self.x+=1
			if self.y<py:
				self.y+=1
			elif self.y>py:
				self.y-=1
		else: # roam around
			# Move for x direction
			if self.x_dir == 'left':
				if self.x > 1:
					self.x -= 1
				else:
					self.x_dir = 'right'
					self.x += 1
			else:
				if self.x < px - 1:
					self.x += 1
				else:
					self.x_dir = 'left'
					self.x -= 1
			# Now move for y direction
			if self.y_dir == 'up':
				if self.y > 1:
					self.y -= 1
				else:
					self.y_dir = 'down'
					self.y += 1
			else:
				if self.y < py - 1:
					self.y += 1
				else:
					self.y_dir = 'up'
					self.y -= 1


enemies=[Enemy(50,60),Enemy(200,100), Enemy(200,400), Enemy(200,200), Enemy(200,400), Enemy(200,200)]
roam = {} # Dict to track relative roam/chase
roam_count = {} # Dict to track time for which roaming
max_roam = {}
max_chasing = len(enemies) // 3
cur_chasing = 0
for i, enmy in enumerate(enemies):
	if cur_chasing < max_chasing:
		roam[i] = 'chase'
		cur_chasing += 1
	else:
		roam[i] = 'roam'
	roam_count[i] = 0
	max_roam[i] = random.randint(100, 500)

while True:
	screen.fill((200,230,200))
	key=pygame.key.get_pressed()

	if key[K_UP]:
		py-=2
	if key[K_DOWN]:
		py+=2
	if key[K_RIGHT]:
		px+=2
	if key[K_LEFT]:
		px-=2

	for e in pygame.event.get():
		if e.type==QUIT:
			exit()

	prect=pygame.Rect(px-20,py-20,20,20)

	for e_1, enmy in enumerate(enemies):
		pygame.draw.circle(screen, (255,0,0), (enmy.x-enmy.rad,enmy.y-enmy.rad), enmy.rad, 0)
		moved_once = False
		for e_2, enmy2 in enumerate(enemies):
			if enmy2 is not enmy:
				if enmy.rect.colliderect(enmy2.rect):
					if roam[e_2] == roam[e_1] == 'roam':
						if cur_chasing < max_chasing:
							roam[e_1] = 'chase'
					elif roam[e_2] == roam[e_1] == 'chase':
						roam[e_2] = 'roam'
						cur_chasing -= 1
					if roam[e_1] == 'roam':
						roam_count[e_1] += 1
						enmy.move('roam')
						if roam_count[e_1] > max_roam[e_1]:
							roam_count[e_1] = 0
							if cur_chasing < max_chasing:
								roam[e_1] = 'chase'
					else:
						enmy.move('chase')
				else:
					if not moved_once:
						if roam[e_1] == 'roam':
							roam_count[e_1] += 1
							enmy.move('roam')
							if roam_count[e_1] > max_roam[e_1]:
								roam_count[e_1] = 0
								if cur_chasing < max_chasing:
									roam[e_1] = 'chase'
						else:
							enmy.move('chase')
						moved_once = True


		enmy.rect=pygame.Rect(enmy.x-enmy.rad*2,enmy.y-enmy.rad*2,enmy.rad*2,enmy.rad*2)
		pygame.draw.rect(screen, (0,0,255), enmy.rect, 2)

	pygame.draw.circle(screen, (0,0,255), (px-10,py-10), 10, 0)
	pygame.draw.rect(screen, (255,0,0), prect, 2)
	clock.tick(80)
	pygame.display.flip()
