import pygame
from src.utilities import constants

class Paddle(pygame.sprite.Sprite):
	# Initializes the object as a sprite. Sets the
	# initial speed, size and location of paddle
	def __init__(self, x, y, speedY, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.speedY = speedY
		# self.speedX = speedX
		self.width = width
		self.height = height
		self.rect = pygame.Rect(x, y, width, height)

	def handle_keys(self, paddle):
		key = pygame.key.get_pressed()

		if paddle == 1:
			if key[pygame.K_w]:
				self.rect.move_ip(0, -self.speedY)
			if key[pygame.K_s]:
				self.rect.move_ip(0, self.speedY)
			if self.rect.bottom > constants.HEIGHT:
				self.rect.bottom = constants.HEIGHT
			if self.rect.top < 0:
				self.rect.top = 0
		elif paddle == 2:
			if key[pygame.K_UP]:
				self.rect.move_ip(0, -self.speedY)
			if key[pygame.K_DOWN]:
				self.rect.move_ip(0, self.speedY)
			if self.rect.bottom > constants.HEIGHT:
				self.rect.bottom = constants.HEIGHT
			if self.rect.top < 0:
				self.rect.top = 0

	def draw(self, screen):
		pygame.draw.rect(screen, (0, 0, 128), self.rect)