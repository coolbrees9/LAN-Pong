
import pygame

class Scene:
	def __init__(self):
		self.size = self.width, self.height = pygame.display.get_surface().get_size()

	def render(self, screen):
		raise NotImplementedError

	def update(self):
		raise NotImplementedError

	def handle_events(self, events):
		raise NotImplementedError

