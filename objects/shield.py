try:
    import sys
    import pygame
    from resources.image_loader import ImageLoader
    from resources.sound_player import SoundPlayer
except ImportError as err:
    print("Couldn't load module. {}".format(err))
    sys.exit(2)

class Shield(pygame.sprite.Sprite):
    """ Bario Shield 
    Returns: Shield
    Functions: update, load_shield
    Attributes: image, rect, direction"""
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image_loader = ImageLoader()
        self.image, self.rect = self.image_loader.load('shield.png')

        self.direction = "right"

    def load_shield(self, rect, direction):
        w, h = rect.size
        self.direction = direction
        
        if self.direction == "right":
            self.image, self.rect = self.image_loader.load('shield.png')
        elif self.direction == "left":
            self.image, self.rect = self.image_loader.load('shield_left.png')

        

    def update(self, rect):
        w, h = rect.size
        if self.direction == "right":
            self.rect = rect.move(w, (h / 2) - (h / 2))
        elif self.direction == "left":
            self.rect = rect.move(-(w / 2) / 4,(h / 2) - (h / 2))
