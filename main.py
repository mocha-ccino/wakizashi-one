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
pygame.display.set_caption("Wakizashi One")
clock = pygame.time.Clock()

# Making some global colors to reference later.
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

player = Player(
    (WINDOW_WIDTH/2) - 10,
    (WINDOW_HEIGHT/2) - 5,
    20,
    10,
    RED)

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

    
    #player.update()
    clock.tick(FPS)




while not crashed:
    gameLoop()