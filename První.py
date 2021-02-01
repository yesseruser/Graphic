# coding = UTF-8
import pygame

pygame.init()

velikost: tuple[int, int] = (800, 600)
screen = pygame.display.set_mode(velikost)

pygame.draw.rect(screen, 'white', (100, 100, 50, 50))
pygame.draw.circle(screen, "green", (200, 150), 50)
pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
