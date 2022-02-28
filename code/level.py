import pygame

class Level:
	def __init__(self) -> None:
		self.display_surface = pygame.display.get_surface()
		self.visible_sprites = pygame.sprite.Group()
		self.obstacle_sprites = pygame.sprite.Group()
	
	def run(self):
		#drawing and updating the game
		pass