import pygame

class ProgressWater():
    def __init__(self):
        self.image = pygame.image.load('./assets/ProgressWater.png')
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (10, self.value))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 267

        self.image_2 = pygame.image.load('./assets/ProgressWater_2.png')
        self.image_2 = pygame.transform.rotate(self.image_2, 90)
        self.image_2 = pygame.transform.scale(self.image_2, (23, 300))
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.x = 95
        self.rect_2.y = 255
        
        self.value = 10

    def add(self, value):
        self.value += value
        self.image = pygame.transform.scale(self.image, (10, self.value))
