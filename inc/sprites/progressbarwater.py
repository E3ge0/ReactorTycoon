import pygame

class ProgressWater():
    def __init__(self):
        self.image = pygame.image.load('./assets/ProgressWater.png')
        self.image = pygame.transform.rotate(self.image, 90)
        self.image_2 = pygame.image.load('./assets/ProgressWater_2.png')
        self.image_2 = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 500
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.x = 0
        self.rect_2.y = 0
