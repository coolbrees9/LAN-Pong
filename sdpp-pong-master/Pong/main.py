
from .SceneManager import *
from .scenes import TitleScene, GameScene
import pygame

def main():
	pygame.init()
	SIZE = width, height = 800, 400
	FLAGS = 0
	DEPTH = 0
	screen = pygame.display.set_mode(SIZE, FLAGS, DEPTH)
	pygame.display.set_caption("Scooby-Doo Pang Pang")
	timer = pygame.time.Clock()
	running = True

	manager = SceneManager()

	while running:
		timer.tick(30) # fps

		if pygame.event.get(QUIT):
			running = False
			return
		manager.scene.handle_events(pygame.event.get())
		manager.scene.update()
		manager.scene.render(screen)
		pygame.display.flip()

