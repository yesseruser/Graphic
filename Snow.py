# coding = UTF-8

import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))

position: tuple[int, int] = (100, 20)
color: tuple[int, int, int] = (222, 254, 254)
radius: int = 20
background = (18, 20, 70)

clock = pygame.time.Clock()
positions = [
    (100, -10),
    (200, -10),
    (300, -10)
]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for index in range(len(positions)):
        x, y = positions[index]
        positions[index] = (x + 2, y + 2)

    screen.fill(background)
    for index in range(len(positions)):
        pygame.draw.circle(screen, color, positions[index], radius)
        pygame.display.flip()

    clock.tick(60)
