import src.assets as assets
from src.utilities import constants
import pygame

class GameBoard:
	def __init__(self, _display_surf, clock):
		self._running = True
		self._display_surf = _display_surf
		self.clock = clock
		self.HEIGHT = constants.HEIGHT
 
	def on_init(self):
		pygame.display.set_caption('Pong Reloaded')
		self.paddle1 = assets.Paddle(10, 0, 8, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT)
		paddle2_x_position = constants.WIDTH - constants.PADDLE_WIDTH - 10
		self.paddle2 = assets.Paddle(paddle2_x_position, 0, 8, 10, 50)
		self._running = True
 
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
	
	def on_loop(self):
		self._display_surf.fill(constants.WHITE)
		self.paddle1.handle_keys(1)
		self.paddle2.handle_keys(2)
		self.clock.tick(60)

	def on_render(self):

		self.paddle1.draw(self._display_surf)
		self.paddle2.draw(self._display_surf)
		pygame.display.update()
 
	def on_execute(self):
		if self.on_init() == False:
			self._running = False

		while self._running:
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()