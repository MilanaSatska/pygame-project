import pygame
from .path import find_path 
class Music:
    def __init__(self, repeat:int, volume:float, name:str):
        self.REPEAT = repeat
        self.VOLUME = volume
        self.NAME = name
    def load_music(self):
        pygame.mixer.music.load (self.NAME)
        pygame.mixer.music.set_volume(self.VOLUME)
    def unload_music(self):
        pygame.mixer.music.unload()
    def play(self):
        pygame.mixer.music.play(loops=self.REPEAT)
    def stop(self):
        pygame.mixer.music.stop()

main_music = Music(name=find_path("music/ТомиДжерри.mp3"), repeat=-1, volume=0.1)