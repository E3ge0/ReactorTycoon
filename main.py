import pygame
from game import Game
pygame.init()

pygame.display.set_caption('ReactorTycoon')
resolution = (1080, 720)
screen = pygame.display.set_mode(resolution)

game = Game()

running = True

while running:

    screen.blit(game.background.image, game.background.rect)
    screen.blit(game.reactor.image, game.reactor.rect)
    screen.blit(game.progresswater.image_2, game.progresswater.rect_2)
    screen.blit(game.progresswater.image, game.progresswater.rect)
    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            running = False
