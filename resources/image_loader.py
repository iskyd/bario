import os
import pygame
from resources.resource_loader import ResourceLoader

class ImageLoader(ResourceLoader):
    """Image resource"""
    def load(self, name):
        fullname = os.path.join('images', name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except pygame.error as message:
            raise SystemExit(message)
        return image, image.get_rect()