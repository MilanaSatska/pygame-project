import pygame
from .app import screen , clock, FSP
from .events import quit_game 
from .enemy import enemy
from .player import jery
from .map import tile_map
from .music import main_music
from .fonts import thing_font
pygame.init()

def run():
    main_music.load_music()
    main_music.play()
    game = True
    while game:
        game_events = pygame.event.get()
        for event in game_events:
            if quit_game(event=event) == True:
                game = False
        screen.fill((170,216,240))

        tile_map.blit_map(screen, jery.move_map())

        #tile_map.blit_collision(screen)
        #tile_map.blit_object_collision(screen)
        #tom.blit_image(screen)

        

        jery.blit_image(screen)
        jery.move()
        jery.can_move_down(tile_map.create_collision())
        jery.can_move_left(tile_map.create_collision())
        jery.can_move_right(tile_map.create_collision())
        jery.can_move_up(tile_map.create_collision())
        #jery.blit_rect(screen)
        jery.direction()
        jery.object_collision(tile_map.create_object_collision())
        #tile_map.blit_object_collision(screen)

        enemy.blit_image(screen)
        enemy.move()
        enemy.can_move_right(tile_map.create_collision())
        enemy.can_move_down(tile_map.create_collision())
        enemy.can_move_left(tile_map.create_collision())
        enemy.can_move_up(tile_map.create_collision())

        
        thing_text = thing_font.render(str(jery.COUNT_THINGS), True, (140, 125, 100), (255, 255, 255))
        screen.blit(thing_text, (100,100))
        #tom.move()
        #tom.collision(jery)
        #print(jery.CAN_MOVE_DOWN)
        pygame.display.flip()
        clock.tick(FSP)
