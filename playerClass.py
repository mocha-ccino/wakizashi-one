import pygame

class Player():

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Vx = 0
        self.Vy = 0
        self.color = color

    #def gravity(self):
     #   if self.Vy > -10:
      #      self.Vy -= 1

    def update(self):
        #self.gravity()
        self.x += self.Vx
        self.y += self.Vy

    def draw(self, Surface):
        pygame.draw.rect(
            Surface,
            self.color,
            pygame.Rect(self.x,
            self.y,
            self.width,
            self.height)
            )
