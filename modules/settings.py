import pygame
from .path import find_path
class Settings:
    def __init__(self, width, high, x, y, image_name):
        self.WIDTH = width
        self.HIGH = high
        self.X = x 
        self.Y = y
        self.IMAGE_NAME = image_name
        self.load_image()
    def load_image(self, direction=False):
        self.IMAGE = pygame.image.load(find_path(f"{self.IMAGE_NAME}"))
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HIGH))
        self.IMAGE = pygame.transform.flip(self.IMAGE, flip_x=direction, flip_y=False)
    def blit_image(self, screen):
        screen.blit(self.IMAGE, (self.X, self.Y))
    #def collision(self, object):
        #if self.X + self.WIDTH >= object.X and self.Y + self.HIGH >= object.Y and object.X + object.WIDTH > self.X and object.Y + object.HIGH > self.Y:
            #print("collision")



