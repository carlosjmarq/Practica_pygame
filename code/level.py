import pygame
from settings import *
from player import Player
from tile import Tile
from debug import debug

class Level:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
	
		self.create_map()

	def run(self):
		#drawing and updating the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		

	def create_map(self):
		for i,row in enumerate(WORLD_MAP):
			for j,cell in enumerate(row):
				x = j * TILESIZE
				y = i * TILESIZE
				if cell == 'x':
					Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
				if cell == 'p':
					self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)


class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

	def custom_draw(self, player):

		#getting the offset
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

	