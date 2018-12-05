
from ..Scene import *
from .GameScene import GameScene
from ..NetworkHandler import NetworkHandler
import pygame
from pygame import *

class JoinScene(Scene):

	def __init__(self):
		super().__init__()

		self.font = pygame.font.SysFont('Arial', 56)
		self.sfont = pygame.font.SysFont('Consolas', 24)
		pygame.mixer.music.load("resources/wii-shop.wav")
		pygame.mixer.music.play(-1)
		self.changesound = pygame.mixer.Sound("resources/menupress.wav")
		self.selectsound = pygame.mixer.Sound("resources/select.wav")

		# for same machine tests, set read and broadcast
		# to different sockets
		self.nethandle = NetworkHandler(42070, 42069)
		self.bcastFreq = 60

		self.selected = -1
		self.hosts = []

	def render(self, screen):
		screen.fill((0,0,0)) # clear screen
		heading = self.sfont.render("Available games", True, (255,255,255))
		screen.blit(heading, (50,30))
		if self.selected >= 0:
			screen.fill((0,128,0), Rect(75, 75+self.selected*30, 600, 30))
		offset = 80
		for h in self.hosts:
			entry = self.sfont.render(h[0].ljust(28, '.') + h[1], True, (255,255,255))
			screen.blit(entry, (100, offset))
			offset += 30

	def update(self):
		self.bcastFreq -= 1
		if self.bcastFreq == 0:
			self.nethandle.broadcast("SEARCH: Requesting to join")
			self.bcastFreq = 60
		msg, addr = self.nethandle.read()
		if msg and addr and "WAITING" in msg:
			print("CLIENT::", msg, "from", addr)
			msg = msg.split(None, 1)[1]
			self.hosts.append((msg,addr))
			self.hosts = list(sorted(set(self.hosts)))

	def handle_events(self, events):
		for e in events:
			if e.type == KEYDOWN and e.key == K_q:
				raise SystemExit
			if e.type == KEYDOWN and e.key == K_UP:
				self.changesound.play()
				self.selected -= 1
			if e.type == KEYDOWN and e.key == K_DOWN:
				self.changesound.play()
				self.selected += 1
			if e.type == KEYDOWN and e.key == K_RETURN:
				if len(self.hosts) == 0:
					return
				self.selectsound.play()
				msg, addr = self.hosts[self.selected]
				self.nethandle.send("JOIN: "+msg, addr)
				pygame.mixer.music.stop()
				self.manager.go_to(GameScene("right", addr))
		self.selected = self.selected%len(self.hosts) if self.hosts else -1
	

