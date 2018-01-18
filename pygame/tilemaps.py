#Code By: Ethan Hunt
import pygame, sys
from pygame.locals import * 

BLACK = (0,   0,   0   )
BROWN = (153, 76,  0   )
GREEN = (0,   255, 0   )
BLUE  = (0,   0,   255 )
GRAY  = (131, 139, 139 )
RED   = (220, 20,  60  )

DIRT  = 0
GRASS = 1
WATER = 2
COAL  = 3
ROCK  = 4
LAVA  = 5

colours = {
			DIRT  : BROWN,
			GRASS : GREEN,
			WATER : BLUE,
			COAL  : BLACK,
			ROCK  : GRAY,
			LAVA  : RED
			}

tilemap = [
			[GRASS, COAL,  ROCK,  LAVA,  ROCK],
			[ROCK,  WATER, GRASS, GRASS, COAL],
			[COAL,  ROCK,  WATER, WATER, LAVA],
			[DIRT,  LAVA,  COAL,  DIRT,  ROCK],
			[GRASS, WATER, DIRT,  DIRT,  COAL]
			]
			
TILESIZE  = 40
MAPWIDTH  = 5
MAPHEIGHT = 5

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
		pygame.display.update()





