import pygame

#initialize pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('C:/Users/dipso/OneDrive/Pictures/Softwarica/pg.png')
pygame.display.set_icon(icon)

#Adding player
playerImg = pygame.image.load('C:/Users/dipso/OneDrive/Pictures/Softwarica/ship.png')
playerX = 370
playerY = 480
playerX_change = 0

#x and y coordinate passed
def player(x,y):
    #blit --> draw
    screen.blit(playerImg, (x,y))

#Game loop
running = True
while running:

    #RGB COLOR TO RGB for background color
    screen.fill((58, 0, 28))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed whether its right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                # Increase to 0.3 if u want to increase the speed
                playerX_change = -0.3
            if event.key == pygame.K_d:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
    playerX += playerX_change

    player(playerX, playerY)

    pygame.display.update()