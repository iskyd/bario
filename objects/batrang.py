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

    def __init__(self, rect, direction):
        """ Parameters
        rect: current position of bario """

        pygame.sprite.Sprite.__init__(self)

        self.width, __ = pygame.display.get_surface().get_size()

        self.image_loader = ImageLoader()
        self.image, self.rect = self.image_loader.load('batrang.png')

        w, h = rect.size

        self.rect = rect.move(w, (h / 2))

        self.speed = 15
        self.direction = direction

    def update(self):
        if self.direction == "left":
            self.rect = self.rect.move(-(self.speed), 0)
        elif self.direction == "right":
            self.rect = self.rect.move(self.speed, 0)
    
        if self.rect.left < 0:
            print("killed")
            self.kill()
        elif self.rect.right > self.width:
            print("killed")
            self.kill()