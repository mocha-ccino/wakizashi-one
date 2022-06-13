import pygame
from playerClass import Player
from pygame import Rect
# Modules!!!!!!!!

pygame.init()

# Global variables for the window width and height.
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 30


# Initialising values and setting an FPS.
gameDisplay = pygame.display.set_mode(
    (WINDOW_WIDTH,
    WINDOW_HEIGHT)
    )
pygame.display.set_caption("WAKIZASHI-ONE")
icon = pygame.image.load("src/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Making some global variables to reference later, like common colors and also speeds.
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAX_SPEED = 20

player = Player(
    (WINDOW_WIDTH/2),
    (WINDOW_HEIGHT/2),
    20,
    40,
    RED)

def gravity(player, windowHeight):

    if player.y + player.height >= windowHeight:
        player.Vy = 0

    else:
        if player.Vy < 30:
            player.Vy += 2

def isGrounded(player):
    if player.y + player.height >= WINDOW_HEIGHT:
        isJumped = False

def movement(player, WINDOW_WIDTH):

    isJumped = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if player.x <= 0:
            player.x = 0

        if player.Vx > -MAX_SPEED:
            player.Vx -= 2

    if keys[pygame.K_RIGHT]:
        if player.x + player.width >= WINDOW_WIDTH:
            player.x = WINDOW_WIDTH - player.width
        if player.Vx < MAX_SPEED:
            player.Vx += 2

    if keys[pygame.K_SPACE]:
        if isJumped == False:
            isJumped = True
            player.Vy = -10

    if keys[pygame.K_DOWN]:
        pass

    if player.Vx > 0:
        player.Vx -= 1.5
    
    elif player.Vx < 0:
        player.Vx += 1.5

crashed = False

def gameLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            pygame.quit()
            quit()
    

    pygame.display.update()
    gameDisplay.fill(BLACK)
    player.draw(gameDisplay)

    gravity(player, WINDOW_HEIGHT)
    movement(player, WINDOW_WIDTH)
    player.update()

    if player.y >= WINDOW_HEIGHT:
        player.y = WINDOW_HEIGHT - player.height - 2
        player.Vy = 0

    
    clock.tick(FPS)




while not crashed:
    gameLoop()