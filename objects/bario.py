try:
    import sys
    import pygame
    from resources.image_loader import ImageLoader
    from resources.sound_player import SoundPlayer
    from objects.batarang import Batarang
    from objects.shield import Shield
except ImportError as err:
    print("Couldn't load module. {}".format(err))
    sys.exit(2)

class Bario(pygame.sprite.Sprite):
    """ It's me! Bario! 
    Returns: Bario
    Functions: update, jump, move, stopMove, lower, batarang_attack
    Attributes: image, rect, batarangs"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.v = 4
        self.m = 10
        self.speed = 10

        self.width, self.height = pygame.display.get_surface().get_size()

        self.image_loader = ImageLoader()
        self.image, self.rect = self.image_loader.load('bario.png')

        self.sound_player = SoundPlayer()

        self.is_jump = False
        self.is_lower = False
        self.move_right = False
        self.move_left = False
        self.direction = "right"
        self.show_shield = False
        
        self.rect = self.rect.move(self.width * .45, self.height * .7)
        
        self.shield = Shield(self.rect)
        self.shieldsprite = pygame.sprite.RenderPlain(self.shield)
        
        self.max_bottom = self.rect.bottom

        self.batarangs = pygame.sprite.Group()
        
    def jump(self):
        if self.is_lower == False:
            self.is_jump = True
            self.sound_player.load("jump.wav")
            self.sound_player.play(0)
    
    def move(self, pos):
        if pos == "right":
            self.move_right = True
            self.move_left = False
            self.direction = "right"
        elif pos == "left":
            self.move_right = False
            self.move_left = True
            self.direction = "left"

    def stopMove(self, pos):
        if pos == "right":
            self.move_right = False
        elif pos == "left":
            self.move_left = False

    def lower(self):
        if self.is_jump == False:
            __, h = self.rect.size
            image, __ = self.image_loader.load('bario_lower.png')
            self.is_lower = True
            self.image = image
            self.rect = self.rect.move(0, h / 2)
            self.sound_player.load("lower.wav")
            self.sound_player.play(0)

    def up(self):
        if self.is_lower == True:
            __, h = self.rect.size
            image, __ = self.image_loader.load('bario.png')
            self.is_lower = False
            self.rect = self.rect.move(0, -(h / 2))
            self.image = image

    def batarang_attack(self):
        if self.is_lower == False and self.show_shield == False:
            self.sound_player.load("batarang.wav")
            self.sound_player.play(0)
            batarang = Batarang(self.rect, self.direction)
            batarangsprite = pygame.sprite.RenderPlain(batarang)
            self.batarangs.add(batarangsprite)

    def shield_defence(self, status):
        if status == "enable":
            self.sound_player.load("shield.wav")
            self.sound_player.play(0)
            self.shield.load_shield(self.rect, self.direction)
            self.show_shield = True
        else:
            self.show_shield = False

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
        
        self.batarangs.update()
    
        self.rect = self.rect.move(x, y)

        if self.show_shield:
            self.shieldsprite.update(self.rect)
