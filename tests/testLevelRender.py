import pygame
from testLevel import level

GREY = (175, 175, 175)

class Block(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.width / 2, self.rect.height / 2)

pygame.init()

# Global variables for the window width and height.
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CENTER_X = WINDOW_WIDTH/2
CENTER_Y = WINDOW_HEIGHT/2
FPS = 30
BLOCK_SIZE_X = WINDOW_WIDTH / 16
BLOCK_SIZE_Y = WINDOW_HEIGHT / 12

gameDisplay = pygame.display.set_mode(
    (WINDOW_WIDTH,
    WINDOW_HEIGHT)
    )
pygame.display.set_caption("level rendery")

all_blocks = pygame.sprite.Group()
block = Block()
all_blocks.add(block)

def gameLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            pygame.quit()
            quit()
    
    for y in range(len(level)):
        for x in range(len(level[0])):
            if level[y][x] == 1:
                pass

    pygame.display.update()

while True:
    gameLoop()

