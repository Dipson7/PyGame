import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('C:/Users/dipso/OneDrive/Pictures/Softwarica/pg.png')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((50, 0, 50))
        pygame.display.update()


