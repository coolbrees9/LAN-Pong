
from pygame import Rect

class Ball:

	base_speed = 5

	def __init__(self):
		self.speed = Ball.base_speed
		self.width, self.height = 5, 5
		self.x, self.y = 100, 100

	def getRect(self):
		return Rect(self.x,self.y,self.width,self.height)

