import time
import pygame
from resources.image_loader import ImageLoader

class Bario(pygame.sprite.Sprite):
    """ It's me! Mario! 
    Returns: Mario
    Functions: update
    Attributes: image, area, vector """

    JUMP_MOVE_DY = 1
    JUMP_MOVE_DX = 0
    MOVE_X = 1
    MOVE_Y = 0
    MAX_JUMP = 2

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image_loader = ImageLoader()
        self.image, self.rect = image_loader.load('bario.png')
        self.rect = self.rect.move(50, 600)

        self.isMarioJump = False
        self.isMarioJumpBack = False
        self.stopJumpTime = False
        self.moveRight = False
        self.moveLeft = False
        self.maxBottom = self.rect.bottom
        self.numberOfJump = 0
    
    def jump(self, pos):
        if pos == "up" and self.numberOfJump < self.MAX_JUMP:
            self.isMarioJump = True
            self.isMarioJumpBack = False
            self.numberOfJump += 1
            self.stopJumpTime = time.time() + 0.2
        elif pos == "up" and self.isMarioJumpBack:
            if self.numberOfJump < self.MAX_JUMP:
                self.jump("up")
        elif pos == "down" and self.isMarioJump:
            self.stopJumpTime = False
            self.isMarioJumpBack = True
    
    def move(self, pos):
        if pos == "right":
            self.moveRight = True
            self.moveLeft = False
        elif pos == "left":
            self.moveRight = False
            self.moveLeft = True

    def stopMove(self, pos):
        if pos == "right":
            self.moveRight = False
        elif pos == "left":
            self.moveLeft = False

    def update(self):
        if self.stopJumpTime and time.time() > self.stopJumpTime:
            self.jump("down")

        if self.isMarioJump and self.isMarioJumpBack == False:
            self.rect = self.rect.move(self.JUMP_MOVE_DX, -self.JUMP_MOVE_DY)
        elif self.isMarioJumpBack:
            self.rect = self.rect.move(self.JUMP_MOVE_DX, self.JUMP_MOVE_DY)
            if self.rect.bottom >= self.maxBottom:
                self.isMarioJumpBack = False
                self.isMarioJump = False
                self.numberOfJump = 0

        if self.moveRight:
            self.rect = self.rect.move(self.MOVE_X, self.MOVE_Y)
        elif self.moveLeft:
            self.rect = self.rect.move(-self.MOVE_X, self.MOVE_Y)
