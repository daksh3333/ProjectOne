import pygame
import random

#initialize pygame
pygame.init()

#create screen (width, height)
screen = pygame.display.set_mode((800,600))

# Title/Icon
pygame.display.set_caption("Alien Armada")
icon = pygame.image.load('Alien dude.png')
pygame.display.set_icon(icon)

#Enemy
enemyimage = pygame.image.load('img.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

#Player 1
playerimage = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerimage, (x, y) )

def enemy(x,y):
    screen.blit(enemyimage, (x, y) )

# Keep the window open
running = True
while running:
    #RGB - Red, Green, Blue, goes up to 255
    screen.fill((0, 0, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check left/right when keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #Update position
    playerX +=  playerX_change
    enemyX += enemyX_change

    #Boundry
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change


    #Draw
    player(playerX, playerY)
    enemy(enemyX, enemyY)


    pygame.display.update()