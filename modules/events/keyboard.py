import pygame
def keyboard(key):
    event = pygame.key.get_pressed()
    if event[key]:
        return True  