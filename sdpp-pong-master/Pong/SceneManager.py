
from .scenes.TitleScene import *

class SceneManager:
	def __init__(self):
		# default behavior
		self.go_to(TitleScene())

	def go_to(self, scene):
		self.scene = scene
		self.scene.manager = self

