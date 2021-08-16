import pygame

#initialize pygame
pygame.init()

#cresting screen
screen = pygame.display.set_mode((800, 600))

#adding title and icon
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('C:/Users/dipso/OneDrive/Pictures/Softwarica/pg.png')
pygame.display.set_icon(icon)

#adding player
playerImg = pygame.image.load('C:/Users/dipso/OneDrive/Pictures/Softwarica/ship.png')

#X and Y to position spaceship
playerX = 370
playerY = 480
def player():
    screen.blit(playerImg, (playerX, playerY)) #blit --> draw

#looping game
running = True
while running:

    screen.fill((100, 0, 50)) #RGB background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player()

        pygame.display.update()