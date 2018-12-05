
from pygame import Rect

class Paddle:

	def __init__(self):
		self.speed = 5
		self.width, self.height = 5, 50
		self.x, self.y = 10, 10

	def getRect(self):
		return Rect(self.x,self.y,self.width,self.height)

