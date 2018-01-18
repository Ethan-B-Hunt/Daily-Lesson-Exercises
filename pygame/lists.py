#Code By: Ethan Hunt
import pygame, sys, random
from pygame.locals import *

BLACK = (0,   0,   0  )
BROWN = (153, 76,  0  )
GREEN = (0,   255, 0  )
BLUE  = (0,   0,   255)
LIGHTBLUE = (2, 2, 220)

DIRT  = 0
GRASS = 1
WATER = 2
COAL  = 3
DIAMOND = 4

textures = {
		DIRT    : pygame.image.load('images/dirt.jpg'),
		GRASS   : pygame.image.load('images/grass.jpg'),
		WATER   : pygame.image.load('images/water.jpg'),
		COAL    : pygame.image.load('images/coal.jpg'),
		DIAMOND : pygame.image.load('images/diamond.jpg')
		}

TILESIZE  = 20
MAPWIDTH  = 30
MAPHEIGHT = 20

resources = [DIRT,GRASS,WATER,COAL]

tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

for rw in range(MAPHEIGHT):
	for cl in range(MAPWIDTH):
		randomNumber = random.randint(0,120)
		if randomNumber >= 0 and randomNumber <= 18:
			tile = COAL
		elif randomNumber >= 19 and randomNumber <= 50:
			tile = WATER
		elif randomNumber >= 51 and randomNumber <= 100:
			tile = GRASS
		elif randomNumber == 120:
			tile = DIAMOND
		else:
			tile = DIRT
		tilemap[rw][cl] = tile

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))

	pygame.display.update()

	
	
	
	
	

	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
