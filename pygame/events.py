#Code By: Ethan Hunt
import pygame, sys
import random
from pygame.locals import *

DIRT  = 0
GRASS = 1
WATER = 2
COAL  = 3
DIAMOND = 4

TILESIZE  = 20
MAPWIDTH  = 30
MAPHEIGHT = 20

resources = [DIRT, GRASS, WATER, COAL, DIAMOND]

tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

textures = {
		DIRT    : pygame.image.load('images/dirt.jpg'),
		GRASS   : pygame.image.load('images/grass.jpg'),
		WATER   : pygame.image.load('images/water.jpg'),
		COAL    : pygame.image.load('images/coal.jpg'),
		DIAMOND : pygame.image.load('images/diamond.jpg')}

pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
pygame.display.set_caption('Events: Ethan Hunt')

PLAYER = pygame.image.load('images/player.jpg').convert_alpha()
playerPos = [0,0]
size = 20,20

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
		elif event.type == KEYDOWN:
			if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH - 1:
				playerPos[0] += 1
			if (event.key == K_LEFT) and playerPos[0] > 0:
				playerPos[0] -= 1
			if (event.key == K_UP) and playerPos[1] > 0:
				playerPos[1] -= 1
			if (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT - 1:
				playerPos[1] += 1


	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row* TILESIZE))
	DISPLAYSURF.blit(PLAYER, (playerPos[0]*TILESIZE,playerPos[1] * TILESIZE))
	pygame.display.update()






	

















