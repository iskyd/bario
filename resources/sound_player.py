import os
import pygame
from resources.resource_loader import ResourceLoader

class SoundPlayer(ResourceLoader):
    """Sound resource"""
    def __init__(self):
        self.lastSoundLoadedName = False

    def load(self, name):
        fullname = os.path.join('sounds', name)
        if self.lastSoundLoadedName == fullname:
            return True
        
        self.lastSoundLoadedName = fullname
        try:
            pygame.mixer.music.load(fullname)
        except pygame.error as message:
            raise SystemExit(message)
        return True
    
    def play(self, t):
        pygame.mixer.music.play(t)