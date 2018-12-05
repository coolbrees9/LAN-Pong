
from ..Scene import *
from ..InputBox import InputBox
from .WaitScene import WaitScene
import pygame
from pygame import *

class HostScene(Scene):
	def __init__(self):
		super().__init__()

		self.font = pygame.font.SysFont('Arial', 56)
		self.sfont = pygame.font.SysFont('Consolas', 24)
		pygame.mixer.music.load("resources/wii-shop.wav")
		pygame.mixer.music.play(-1)
		self.selectsound = pygame.mixer.Sound("resources/select.wav")
		self.inputbox = InputBox(100,100,400,32,self.sfont)
		self.inputbox.active = True

	def render(self, screen):
		screen.fill((0,0,0)) # clear screen
		heading = self.sfont.render("Choose a name for your game:", True, (255,255,255))
		screen.blit(heading, (100,72))
		self.inputbox.draw(screen)

	def update(self):
		pass

	def handle_events(self, events):
		for e in events:
			if e.type == KEYDOWN and e.key == K_RETURN:
				self.selectsound.play()
				pygame.mixer.music.stop()
				self.manager.go_to(WaitScene(self.inputbox.text))
			self.inputbox.handle_event(e)
	

