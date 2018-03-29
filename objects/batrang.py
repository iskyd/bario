try:
    import sys
    import pygame
    from resources.image_loader import ImageLoader
    from resources.sound_player import SoundPlayer
except ImportError as err:
    print("Couldn't load module. {}".format(err))
    sys.exit(2)

class Batrang(pygame.sprite.Sprite):
    """ Batrang
    Returns: Batrang
    Functions: update
    Attributes: image, rect """

    def __init__(self, rect):
        """ Parameters
        rect: current position of bario """

        pygame.sprite.Sprite.__init__(self)

        self.image_loader = ImageLoader()
        self.image, self.rect = self.image_loader.load('batrang.png')

        w, h = rect.size

        self.rect = rect.move(w, (h / 2))

    def update(self):
        self.rect = self.rect.move(100, 0)