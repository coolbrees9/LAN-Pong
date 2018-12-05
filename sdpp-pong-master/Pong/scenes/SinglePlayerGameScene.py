
from ..Scene import *
from ..entities.Paddle import *
from ..entities.Ball import *
from .EndScene import *
import pygame
import random
from pygame import *

class SinglePlayerGameScene(Scene):

	def __init__(self):
		super().__init__()

		self.font = pygame.font.SysFont('Consolas', 32)

		# setup SFX
		self.popsound = pygame.mixer.Sound("resources/pop.wav")
		self.boomsound = pygame.mixer.Sound("resources/boom.wav")
		self.airhornsound = pygame.mixer.Sound("resources/airhorn.wav")
		self.sdppsound = pygame.mixer.Sound("resources/sdpp.wav")

		# setup paddles
		self.p1, self.p2 = Paddle(), Paddle()
		self.p1.x = 10
		self.p1.y = self.height/2 - self.p1.height/2
		self.p2.x = self.width - 10 - self.p2.width
		self.p2.y = self.height/2 - self.p2.height/2

		# setup ball
		self.ball = Ball()
		self.ball.x, self.ball.y = self.width/2, self.height/2

		# setup walls
		self.wall1 = Rect(0,0,10,self.height)
		self.wall2 = Rect(self.width-10,0,10,self.height)
		self.net = Rect(self.width/2 - 5, 0, 10, self.height)

		self.score1, self.score2 = 0, 0
		self.score = self.font.render("%2d  %2d "%(self.score1,self.score2), False, (255,255,255))

		self.newVelocity()


	def render(self, screen):
		screen.fill((0,0,0)) # clear screen

		# draw goals and net
		screen.fill((255,0,0), self.wall1)
		screen.fill((0,0,255), self.wall2)
		screen.fill((0,32,0), self.net)
	
		# paddles and ball
		screen.fill((255,255,255), self.p1.getRect())
		screen.fill((255,255,255), self.p2.getRect())
		screen.fill((255,255,255), self.ball.getRect())

		screen.blit(self.score, (self.width/2 - self.score.get_width()/2,0))

		pygame.display.flip()

	def update(self):
		self.score = self.font.render("%2d  %2d "%(self.score1,self.score2), False, (255,255,255))
		self.resolveCollision()

		# update ball position
		self.ball.x += self.dx*self.ball.speed
		self.ball.y += self.dy*self.ball.speed


	def handle_events(self, events):
		for e in events:
			if e.type == KEYDOWN and e.key == K_q:
				raise SystemExit
		keys = key.get_pressed()

		# paddle movement
		if(keys[K_w]): self.p1.y += -self.p1.speed if self.p1.y>0 else 0
		if(keys[K_s]): self.p1.y += self.p1.speed if self.p1.y+self.p1.height<self.height else 0

		# right paddle movement
		if(keys[K_UP]): self.p2.y += -self.p2.speed if self.p2.y>0 else 0
		if(keys[K_DOWN]): self.p2.y += self.p2.speed if self.p2.y+self.p2.height<self.height else 0

	def resolveCollision(self):
		if self.ball.x+self.ball.width > self.width-10-self.p2.width:
			self.newVelocity(True)
			if self.ball.y < self.p2.y or self.ball.y > self.p2.y+self.p2.height:
				self.score1 += 1
				self.ball.x, self.ball.y = self.width/2, self.height/2
				self.ball.speed = self.ball.base_speed
				self.airhornsound.play()
				return
			self.ball.speed *= 1.10
			self.popsound.play()
		if self.ball.x < 10+self.p1.width:
			self.newVelocity()
			if self.ball.y < self.p1.y or self.ball.y > self.p1.y+self.p1.height:
				self.score2 += 1
				self.ball.x, self.ball.y = self.width/2, self.height/2
				self.ball.speed = self.ball.base_speed
				self.airhornsound.play()
				return
			self.ball.speed *= 1.10
			self.boomsound.play()
		if self.ball.y > self.height or self.ball.y < 0:
			self.dy *= -1
	
		if self.score1 == 11:
			self.manager.go_to(EndScene(1))
		elif self.score2 == 11:
				self.manager.go_to(EndScene(0))

	def newVelocity(self, left=False):
		self.dx, self.dy = random.random()/2 + 0.5, (random.random()*2-1)/2
		self.dx /= (self.dx**2 + self.dy**2)**0.5
		self.dy /= (self.dx**2 + self.dy**2)**0.5
		if left: self.dx *= -1

