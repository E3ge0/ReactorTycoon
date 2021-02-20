import pygame

class Reactor():
    def __init__(self):
        self.image = pygame.image.load('./assets/reactor.png')
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 180
    def overheat(self):
        self.image = pygame.image.load('./assets/reactoroverheat.png')
