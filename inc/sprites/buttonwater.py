import pygame

class ButtonWater:

    def __init__(self):
        self.image = pygame.image.load('./assets/buttonwater.png')
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.x = 65
        self.rect.y = 175
