import time
import pygame
from resources.image_loader import ImageLoader
from resources.sound_player import SoundPlayer

class Bario(pygame.sprite.Sprite):
    """ It's me! Bario! 
    Returns: Bario
    Functions: update
    Attributes: image, area, vector """

    MAX_JUMP = 2

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.v = 4
        self.m = 10
        self.speed = 10

        self.width, self.height = pygame.display.get_surface().get_size()

        image_loader = ImageLoader()
        self.image, self.rect = image_loader.load('bario.png')

        self.sound_player = SoundPlayer()

        self.is_jump = False
        self.move_right = False
        self.move_left = False

        self.rect = self.rect.move(self.width * .45, self.height * .8)

        self.max_bottom = self.rect.bottom
    
    def jump(self):
        self.is_jump = True
        self.sound_player.load("jump.wav")
        self.sound_player.play(0)
    
    def move(self, pos):
        if pos == "right":
            self.move_right = True
            self.move_left = False
        elif pos == "left":
            self.move_right = False
            self.move_left = True

    def stopMove(self, pos):
        if pos == "right":
            self.move_right = False
        elif pos == "left":
            self.move_left = False

    def update(self):
        x, y = 0, 0

        if self.is_jump:
            f = (.5 * self.m * (self.v*self.v))
            if self.v <= 0:
                f = -f
            
            self.v = self.v - 1

            if self.rect.bottom >= self.max_bottom and self.v < 0:
                self.is_jump = False
                self.v = 4
                f = 0

            y -= f
        if self.move_right and self.rect.right < self.width:
            x += self.speed
        if self.move_left and self.rect.left > 0:
            x -= self.speed
    
        self.rect = self.rect.move(x, y)
