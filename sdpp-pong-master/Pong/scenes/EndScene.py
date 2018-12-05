
from ..Scene import *
import pygame
from pygame import *

class EndScene(Scene):

	def __init__(self, index):
		super().__init__()
		self.word = "Congrats, You Win" if index == 1 else "Loser!"
		self.font = pygame.font.SysFont('Arial', 56)
		self.sfont = pygame.font.SysFont('Consolas', 24)
		pygame.mixer.music.load("resources/wii-shop.wav")
		pygame.mixer.music.play(-1)
		self.sdppsound = pygame.mixer.Sound("resources/sdpp.wav")
		self.sdppsound.play()

	def update(self):
		pass


	def render(self, screen):
		screen.fill((0, 0, 0))  # clear screen
		heading = self.sfont.render(self.word, True, (255, 255, 255))
		screen.blit(heading, (100, 72))

	def handle_events(self, events):
		for e in events:
			if e.type == KEYDOWN and e.key == K_SPACE:
				pygame.mixer.music.stop()
				raise SystemExit
			if e.type == KEYDOWN and e.key == K_q:
				raise SystemExit

