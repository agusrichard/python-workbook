import sys
import pygame

pygame.init()

WIDTH = 1920
HEIGHT = 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    # As the halting condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (25,25,112), [(1920/2) - 50, (1080/2) - 50, 100, 150])
    pygame.display.update()

    