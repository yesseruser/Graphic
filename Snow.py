# coding = UTF-8

import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
position: tuple[int, int] = (100, 20)
color: tuple[int, int, int] = (222, 254, 254)
radius: int = 20

pygame.draw.circle(screen, color, position, radius)
pygame.display.flip()



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
