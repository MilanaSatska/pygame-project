import pygame
from .sprite import Sprite 
from .events import keyboard
from .map import tile_map
class Player(Sprite):
    def __init__(self,speed, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.SPEED = speed
        self.NUMBER_IMAGE = 0
        self.SPEED_ANIMATION = 0
        self.CURRENT_ANIMATION = ""
        self.COUNT_THINGS = 0
        self.COUNT_LIFES = 5
        self.MAP_MOVE_COUNT = 0
        self.ENEMY_COUNT = 0
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HIGH)
    def move(self):
        if keyboard(pygame.K_RIGHT):
            if self.CAN_MOVE_RIGHT == True:
                self.X += self.SPEED 
                self.RECT.x += self.SPEED 
                self.DIRECTION = "Right"
                if self.CURRENT_ANIMATION != "run":
                    self.NUMBER_IMAGE = 0
                    self.CURRENT_ANIMATION = "run"
                self.animation(animation_name="player/run", last_image=7, count_image=8)
        elif keyboard(pygame.K_LEFT):
            if self.CAN_MOVE_LEFT == True:
                self.X -= self. SPEED 
                self.RECT.x -= self.SPEED 
                self.DIRECTION = "Left"
                if self.CURRENT_ANIMATION != "run":
                    self.NUMBER_IMAGE = 0
                    self.CURRENT_ANIMATION = "run"
                self.animation(animation_name="player/run", last_image=7, count_image=8)
        elif keyboard(pygame.K_UP):
            if self.CAN_MOVE_UP== True:
                self.Y -= self.SPEED 
                self.RECT.y -= self.SPEED 
                if self.CURRENT_ANIMATION != "run":
                    self.NUMBER_IMAGE = 0
                    self.CURRENT_ANIMATION = "run"
                self.animation(animation_name="player/run", last_image=7, count_image=8)
        elif keyboard(pygame.K_DOWN):
            if self.CAN_MOVE_DOWN== True:
                self.Y += self.SPEED 
                self.RECT.y += self.SPEED
                if self.CURRENT_ANIMATION != "run":
                    self.NUMBER_IMAGE = 0
                    self.CURRENT_ANIMATION = "run"
                self.animation(animation_name="player/run", last_image=7, count_image=8)
        else:
            self.CURRENT_ANIMATION = "idle"
            self.animation(animation_name="player/idle", last_image=9, count_image=10)

    def animation(self, animation_name, last_image, count_image):
        self.SPEED_ANIMATION += 2
        if self.SPEED_ANIMATION % count_image == 0:
            if self.NUMBER_IMAGE == last_image:
                self.NUMBER_IMAGE = 0
            self.IMAGE_NAME = f"{animation_name}/{self.NUMBER_IMAGE}.png"
            self.direction()
            if count_image > 1:
                self.NUMBER_IMAGE += 1

    def blit_rect(self, screen):
        pygame.draw.rect(screen, (230, 150, 240), self.RECT, 4)
    def object_collision(self, thing_collision):
        for thing in thing_collision:
            thing_rect = pygame.Rect(thing.x, thing.y, thing.width, thing.height)
            if self.RECT.colliderect(thing_rect):
                tile_map.delete_tile(x=thing_rect.x, y=thing_rect.y)
                self.COUNT_THINGS += 1
                break
    def enemy_collision(self, enemy, hearts):
        self.ENEMY_COUNT += 0.5 
        if self.ENEMY_COUNT > 25:
            if self.RECT.colliderect(enemy.RECT):
                del hearts[-1]
                self.COUNT_LIFES -= 1
                self.ENEMY_COUNT = 0

    def end_game(self):
        if self.COUNT_LIFES == 0:
            return True
            
    def map_exit(self, screen: pygame.Surface):
        if self.RECT.y > screen.get_height():
            self.X =500
            self.RECT.x = 500
            self.Y =100
            self.RECT.y =100

    def move_map(self):
        if self.CAN_MOVE_RIGHT == True and keyboard(pygame.K_RIGHT):
            self.MAP_MOVE_COUNT += 3
        elif self.CAN_MOVE_LEFT == True and keyboard(pygame.K_LEFT) :
            self.MAP_MOVE_COUNT -= 3
        return self.MAP_MOVE_COUNT
    
jery = Player(image_name= "player/idle/0.png", width=65, high= 45, x= 255, y= 410, speed= 2)
