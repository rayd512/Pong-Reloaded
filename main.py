import pygame
from pygame.locals import *
import src.assets as assets
import src.boards as boards
from src.utilities import constants

class App:
	def __init__(self):
		self._running = True
		self._display_surf = None
		self.clock = None
		self.size = self.width, self.height = constants.WIDTH, constants.HEIGHT
 
	def on_init(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		pygame.display.set_caption('Pong Reloaded')
		self.clock = pygame.time.Clock()
		self.game = boards.GameBoard(self._display_surf, self.clock)
		self._running = True
 
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False

	def on_loop(self):
		self.game.on_execute()
		self._running = False

	def on_render(self):
		pass

	def on_cleanup(self):
		pygame.quit()
 
	def on_execute(self):
		if self.on_init() == False:
			self._running = False
 
		while self._running:
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()
 
if __name__ == "__main__" :
	pong = App()
	pong.on_execute()