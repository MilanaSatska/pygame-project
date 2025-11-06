import pytmx
import pygame
from .path import find_path
class Map:
    def __init__(self, file_name):
        self.TILEMAP = pytmx.load_pygame(find_path(f"tilemap/{file_name}"))
        self.WIDTH = self.TILEMAP.tilewidth
        self.HIGH = self.TILEMAP.tileheight
        self.MAP_MOVE = 0
        self.camera_x = 0
    def blit_map(self, screen):
        self.LAYERS = self.TILEMAP.visible_tile_layers
        for layer_id in self.LAYERS:
            #print(layer_id)
            layer = self.TILEMAP.layers[layer_id]
            for x, y, cell in layer:
                if cell:
                    #self.MAP_MOVE = map_move
                    cell_image = self.TILEMAP.get_tile_image_by_gid(cell)
                    screen.blit(cell_image, (x*self.WIDTH - self.camera_x, y*self.HIGH))

    def update_camera(self, player):
        self.camera_x = player.X - 400  # 400 — половина ширины окна (центр камеры)
        if self.camera_x < 0:
            self.camera_x = 0


    def blit_collision(self, screen):
        self.COLLISION_LAYER = self.TILEMAP.get_layer_by_name("ground_2")
        for collision_object in self.COLLISION_LAYER:
            block_rect = pygame.Rect(collision_object.x - self.MAP_MOVE, collision_object.y, collision_object.width, collision_object.height)
            pygame.draw.rect(screen, (230, 150, 240), block_rect, 4)
    def create_collision(self):
        self.COLLISION_LAYER= self.TILEMAP.get_layer_by_name("ground_2")
        map_collision = []
        for collision_object in self.COLLISION_LAYER:
            block_rect = pygame.Rect(collision_object.x -self.MAP_MOVE, collision_object.y, collision_object.width, collision_object.height)
            map_collision.append(block_rect)
        return map_collision
    def create_object_collision(self):
        self.COLLISION_LAYER= self.TILEMAP.get_layer_by_name("object")
        thing_collision = []
        for collision_object in self.COLLISION_LAYER:
            thing_rect = pygame.Rect(collision_object.x- self.MAP_MOVE, collision_object.y, collision_object.width, collision_object.height)
            thing_collision.append(thing_rect)
        return thing_collision
    def blit_object_collision(self, screen):
        self.COLLISION_LAYER = self.TILEMAP.get_layer_by_name("object")
        for collision_object in self.COLLISION_LAYER:
            block_rect = pygame.Rect(collision_object.x - self.MAP_MOVE, collision_object.y, collision_object.width, collision_object.height)
            pygame.draw.rect(screen, (230, 150, 240), block_rect, 4)
    def delete_tile(self, x: int, y: int):
        self.LAYER = self.TILEMAP.get_layer_by_name("things")
        self.BOTTLE_LAYER = self.TILEMAP.get_layer_by_name("object")
        x_for_things = x + self.MAP_MOVE
        column = x_for_things // self.WIDTH
        row = y // self.HIGH
        #self.LAYER.data[row][column]=0
        for count in range(5):
            self.LAYER.data[row+count][column+count] = 0
            self.LAYER.data[row-count][column-count] = 0
            self.LAYER.data[row+count][column]=0
            self.LAYER.data[row-count][column]=0
            self.LAYER.data[row][column+count]=0
            self.LAYER.data[row][column-count]=0
            

        print(column, row)

        #self.BOTTLE_LAYER[row][column] = 0
        for bottle in self.BOTTLE_LAYER:
            bottle_rect = pygame.Rect(bottle.x- self.MAP_MOVE, bottle.y, bottle.width, bottle.height)
            if bottle_rect.collidepoint(x,y):
                self.BOTTLE_LAYER.remove(bottle)
                break
# self. BOTTLE_LAYER

tile_map = Map(file_name="map.tmx")