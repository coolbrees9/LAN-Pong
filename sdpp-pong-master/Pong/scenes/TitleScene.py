
from ..Scene import *
from .SinglePlayerGameScene import *
from .JoinScene import *
from .HostScene import *
import pygame
from pygame import *

class TitleScene(Scene):

	def __init__(self):
		super().__init__()

		self.font = pygame.font.SysFont('Arial', 56)
		self.sfont = pygame.font.SysFont('Arial', 32)
		pygame.mixer.music.load("resources/mii-plaza.wav")
		pygame.mixer.music.play(-1)

	def render(self, screen):
		screen.fill((0,0,0)) # clear screen
		title = self.font.render("LAN Pong", True, (255,255,255))
		subtitle = self.sfont.render("J to join, H to host", True, (255,255,255))
		screen.blit(title, (self.width/2 - title.get_width()/2, self.height/2 - title.get_height()/2))
		screen.blit(subtitle, (self.width/2 - subtitle.get_width()/2, self.height/2 + 2*subtitle.get_height()))

	def update(self):
		#TODO
		pass

	def handle_events(self, events):
		for e in events:
			if e.type == KEYDOWN and e.key == K_SPACE:
				pygame.mixer.music.stop()
				self.manager.go_to(SinglePlayerGameScene())
			if e.type == KEYDOWN and e.key == K_j:
				pygame.mixer.music.stop()
				self.manager.go_to(JoinScene())
			if e.type == KEYDOWN and e.key == K_h:
				pygame.mixer.music.stop()
				self.manager.go_to(HostScene())
			if e.type == KEYDOWN and e.key == K_q:
				raise SystemExit

