import pygame

class Background():
    def __init__(self):
        self.image = pygame.image.load('assets/bg.jpg')
        self.image = pygame.transform.scale(self.image, (1080, 720))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
