import pygame
from settings import *
from player import Player
from tile import Tile
from debug import debug

class Level:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.visible_sprites = pygame.sprite.Group()
		self.obstacle_sprites = pygame.sprite.Group()
	
		self.create_map()

	def run(self):
		#drawing and updating the game
		self.visible_sprites.draw(self.display_surface)
		self.visible_sprites.update()
		debug(self.player.direction)
		

	def create_map(self):
		for i,row in enumerate(WORLD_MAP):
			for j,cell in enumerate(row):
				x = j * TILESIZE
				y = i * TILESIZE
				if cell == 'x':
					Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
				if cell == 'p':
					self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
