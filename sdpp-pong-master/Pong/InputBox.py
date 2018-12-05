
import pygame as pg

COLOR_INACTIVE = (64, 64, 64)
COLOR_ACTIVE = (255, 255, 255)

class InputBox:

	def __init__(self, x, y, w, h, font, text=''):
		self.rect = pg.Rect(x, y, w, h)
		self.color = COLOR_INACTIVE
		self.text = text
		self.font = font
		self.txt_surface = self.font.render(text+"|", True, self.color)
		self.active = False

	def handle_event(self, event):
		if event.type == pg.MOUSEBUTTONDOWN:
			# If the user clicked on the input_box rect.
			if self.rect.collidepoint(event.pos):
				# Toggle the active variable.
				self.active = not self.active
			else:
				self.active = False
			# Change the current color of the input box.
		self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
		if event.type == pg.KEYDOWN:
			if self.active:
				if event.key == pg.K_RETURN:
					self.text = ''
				elif event.key == pg.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					self.text += event.unicode
				# Re-render the text.
				self.txt_surface = self.font.render(self.text+"|", True, self.color)

	def update(self):
		pass

	def draw(self, screen):
		# draw the text
		screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
		# draw the border
		pg.draw.rect(screen, self.color, self.rect, 2)

