
from ..Scene import Scene
from ..NetworkHandler import NetworkHandler
from .SinglePlayerGameScene import SinglePlayerGameScene
from .GameScene import GameScene
import pygame
from pygame import *

class WaitScene(Scene):

	def __init__(self, roomname):
		super().__init__()

		self.roomname = roomname

		self.font = pygame.font.SysFont('Arial', 56)
		self.sfont = pygame.font.SysFont('Consolas', 24)
		pygame.mixer.music.load("resources/wii-shop.wav")
		pygame.mixer.music.play(-1)
		self.selectsound = pygame.mixer.Sound("resources/select.wav")

		# for same machine tests, set read and broadcast
		# to different sockets
		self.nethandle = NetworkHandler(42069, 42070)

	def render(self, screen):
		screen.fill((0,0,0)) # clear screen
		roomname = self.font.render(self.roomname, True, (255,255,255))
		screen.blit(roomname, (self.width/2 - roomname.get_width()/2, self.height/3 - roomname.get_height()/2))
		heading = self.sfont.render("Waiting for a player...", True, (255,255,255))
		screen.blit(heading, (self.width/2 - heading.get_width()/2, self.height/2 - heading.get_height()/2))

	def update(self):
		msg, addr = self.nethandle.read()
		if msg and addr and "SEARCH" in msg:
			print("HOST::", msg, "from", addr)
			self.nethandle.send("WAITING: "+self.roomname, addr)
		if msg and addr and "JOIN" in msg:
			print("HOST::", msg, "from", addr)
			pygame.mixer.music.stop()
			self.manager.go_to(GameScene("left", addr))

	def handle_events(self, events):
		for e in events:
			if e.type == KEYDOWN and e.key == K_q:
				raise SystemExit
			if e.type == KEYDOWN and e.key == K_RETURN:
				self.selectsound.play()
				pygame.mixer.music.stop()
				self.manager.go_to(SinglePlayerGameScene())
	

