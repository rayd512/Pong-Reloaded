import pygame

class Paddle(pygame.sprite.Sprite):
	# Initializes the object as a sprite. Sets the
	# initial speed, size and location of paddle
	def __init__(self, x, y, speedY, speedX, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.speedY = speedY
		self.speedX = speedX
		self.width = width
		self.height = height
		self.rect = pygame.Rect(x, y, width, height)

	def handle_keys(self):
		key = pygame.key.get_pressed()
		dist = 1
		if key[pygame.K_LEFT]:
		   self.rect.move_ip(-1, 0)
		if key[pygame.K_RIGHT]:
		   self.rect.move_ip(1, 0)
		if key[pygame.K_UP]:
		   self.rect.move_ip(0, -1)
		if key[pygame.K_DOWN]:
		   self.rect.move_ip(0, 1)