from math import sqrt, atan, pi
import pygame

class Player():

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Vx = 0
        self.Vy = 0
        self.color = color

    def rad_to_deg(self, rad):
        return rad * (180/pi)

    def calc_mouse_angle(self):
        angle = 0
        try:
            mousePos = list(pygame.mouse.get_pos())
            abs_x = mousePos[0]
            abs_y = mousePos[1]
            x = self.x - abs_x
            y = self.y - abs_y
            return abs(self.rad_to_deg(atan(y/x)))
        
        except:
            print("One of the values is zero, this won't work")

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
    
    def swing(self, attack_image):
        pass
