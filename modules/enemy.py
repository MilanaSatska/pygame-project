import pygame
from .events import keyboard
from .sprite import Sprite 
class Enemy(Sprite):
    def __init__ (self, speed, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.CAN_MOVE_RIGHT_ENEMY = True
        self.CAN_MOVE_LEFT_ENEMY = False
        self.CAN_MOVE_DOWN_ENEMY = True
        self.CAN_MOVE_UP_ENEMY = True
        self.SPEED = 2
        self.SPEED = speed
        self.NUMBER_IMAGE = 0
        self.SPEED_ANIMATION = 0
        self.CURRENT_ANIMATION = ""
        self.COUNT_THINGS = 0
        self.MAP_MOVE_COUNT = 0
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HIGH)
    def move(self):
        if keyboard(pygame.K_d):
            if self.CAN_MOVE_RIGHT_ENEMY == True:
                self.X += self.SPEED 
                self.RECT.x += self.SPEED 
                self.DIRECTION = "Right"
                if self.CURRENT_ANIMATION != "run":
                    self.NUMBER_IMAGE = 0
                    self.CURRENT_ANIMATION = "run"
                self.animation(animation_name="enemy/run", last_image=7, count_image=8)
        elif keyboard(pygame.K_a):
            if self.CAN_MOVE_LEFT_ENEMY == True:
                self.X -= self. SPEED 
                self.RECT.x -= self.SPEED 
                self.DIRECTION = "Left"
                if self.CURRENT_ANIMATION != "run":
                    self.NUMBER_IMAGE = 0
                    self.CURRENT_ANIMATION = "run"
                self.animation(animation_name="enemy/run", last_image=7, count_image=8)
        elif keyboard(pygame.K_w):
            if self.CAN_MOVE_UP== True:
                self.Y -= self.SPEED 
                self.RECT.y -= self.SPEED 
                if self.CURRENT_ANIMATION != "run":
                    self.NUMBER_IMAGE = 0
                    self.CURRENT_ANIMATION = "run"
                self.animation(animation_name="enemy/run", last_image=7, count_image=8)
        elif keyboard(pygame.K_s):
            if self.CAN_MOVE_DOWN== True:
                self.Y += self.SPEED 
                self.RECT.y += self.SPEED
                if self.CURRENT_ANIMATION != "run":
                    self.NUMBER_IMAGE = 0
                    self.CURRENT_ANIMATION = "run"
                self.animation(animation_name="enemy/run", last_image=7, count_image=8)

    def animation(self, animation_name, last_image, count_image):
        self.SPEED_ANIMATION += 2
        if self.SPEED_ANIMATION % count_image == 0:
            if self.NUMBER_IMAGE == last_image:
                self.NUMBER_IMAGE = 0
            self.IMAGE_NAME = f"{animation_name}/{self.NUMBER_IMAGE}.png"
            self.direction()
            if count_image > 1:
                self.NUMBER_IMAGE += 1

enemy = Enemy(image_name= "enemy/run/0.png", width=65, high= 45, x= 280, y= 410, speed= 2)
