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

    screen.blit(game.progressheat.image_2, game.progressheat.rect_2)
    screen.blit(game.progressheat.image, game.progressheat.rect)

    screen.blit(game.buttonwater.image, game.buttonwater.rect)

    pygame.display.flip()

    if game.progressheat.value >= 280:
        game.reactor.overheat()

    if game.progresswater.value >= 280:
        game.reactor.overheat()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                game.progresswater.add(10)
            if e.key == pygame.K_z:
                game.progressheat.add(10)
