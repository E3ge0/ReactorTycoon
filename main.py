import pygame
pygame.init()

pygame.display.set_caption('ReactorTycoon')
resolution = (1080, 720)
screen = pygame.display.set_mode(resolution)

running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            running = False
