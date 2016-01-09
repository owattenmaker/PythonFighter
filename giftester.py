import pygame
from pygame.locals import *
from GIFImage import GIFImage
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

shittingdog = GIFImage('supergif.gif')

while True:
	screen.fill((0,0,0))
	shittingdog.render(screen, (0,0))
	pygame.display.update()
	
