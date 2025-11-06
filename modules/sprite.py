import pygame
from .settings import Settings 
class Sprite(Settings):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HIGH)
        self.Y_VELOCITY = 0 
        self.CAN_MOVE_LEFT = True
        self.CAN_MOVE_RIGHT = True
        self.CAN_MOVE_UP = True
        self.CAN_MOVE_DOWN = True
        self.DIRECTION = ""


    
    def can_move_down(self, map_collision):
        for block in map_collision:
            block_rect = pygame.Rect(block.x, block.y, block.width, block.height)
            if self.RECT.y + self.RECT.height >= block_rect.y and self.RECT.y  < block_rect.y:
                if self.RECT.x <= block_rect.x + block_rect.width and self.RECT.x + self.RECT.width >= block_rect.x:
                    self.CAN_MOVE_DOWN = False
                    break
                else:
                    self.CAN_MOVE_DOWN = True
            else:
                self.CAN_MOVE_DOWN = True
    def can_move_up(self, map_collision):
        for block in map_collision:
            block_rect = pygame.Rect(block.x, block.y, block.width, block.height)
            if self.RECT.y <= block_rect.y + block_rect.height and self.RECT.y + self.RECT.height > block_rect.y + block_rect.height:
                if self.RECT.x <= block_rect.x + block_rect.width and self.RECT.x + self.RECT.width >= block_rect.x:
                    self.CAN_MOVE_UP = False
                    break
                else:
                    self.CAN_MOVE_UP = True
            else:
                self.CAN_MOVE_UP = True

    def can_move_left(self, map_collision):
        for block in map_collision:
            block_rect = pygame.Rect(block.x, block.y, block.width, block.height)
            if self.RECT.y + self.RECT.height - 10 < block_rect.y + block_rect.height and self.RECT.y + self.RECT.height - 10 > block_rect.y:
                if self.RECT.x <= block_rect.x + block_rect.width and self.RECT.x + self.RECT.width >= block_rect.x + block_rect.width:
                    self.CAN_MOVE_LEFT = False
                    break
                else:
                    self.CAN_MOVE_LEFT = True
            else:
                self.CAN_MOVE_LEFT = True

    def can_move_right(self, map_collision):
        for block in map_collision:
            block_rect = pygame.Rect(block.x, block.y, block.width, block.height)
            if self.RECT.colliderect(block_rect):
            #if self.RECT.y + self.RECT.height > block_rect.y and self.RECT.y < block_rect.y + block_rect.height:
                if self.RECT.x + self.RECT.width + self.SPEED > block_rect.x and self.RECT.x < block_rect.x:
                    # self.RECT.x -= 2
                    # self.X -= 2
                    self.CAN_MOVE_RIGHT = False
                    break
            else:
                self.CAN_MOVE_RIGHT = True
        else:
            self.CAN_MOVE_RIGHT = True

    def direction(self):
        if self.DIRECTION == "Right":
            self.load_image()
        elif self.DIRECTION == "Left":
            self.load_image(direction=True)