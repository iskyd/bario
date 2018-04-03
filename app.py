#!/usr/bin/python

try:
    import os
    import sys
    import time
    import random
    import pygame
    from pygame.locals import *
    from objects.bario import Bario
except ImportError as err:
    print("Couldn't load module. {}".format(err))
    sys.exit(2)

def main():
    pygame.init()
    size_w, size_h = 800, 600
    if len(sys.argv) > 1:
        try:
            size_w = int(sys.argv[1])
        except ValueError:
            print("Value provided {} for size_w is not valid".format(size_w))
    if len(sys.argv) > 2:
        try:
            size_h = int(sys.argv[2])
        except ValueError:
            print("Value provided {} for size_h is not valid".format(size_h))
    
    screen = pygame.display.set_mode((size_w, size_h))
    pygame.display.set_caption('bario')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    bario = Bario()
    bariosprite = pygame.sprite.RenderPlain(bario)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    bario.jump()
                elif event.key == K_RIGHT:
                    bario.move("right")
                elif event.key == K_LEFT:
                    bario.move("left")
                elif event.key == K_DOWN:
                    bario.lower()
                elif event.key == K_LCTRL:
                    bario.batarang_attack()
                elif event.key == K_LSHIFT:
                    bario.shield_defence("enable")
            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    bario.stopMove("right")
                elif event.key == K_LEFT:
                    bario.stopMove("left")
                elif event.key == K_DOWN:
                    bario.up()
                elif event.key == K_LSHIFT:
                    bario.shield_defence("disable")
                
        bario.update()
        screen.blit(background, (0, 0))
        bariosprite.draw(screen)
        bario.batarangs.draw(screen)
        if bario.show_shield == True:
            bario.shieldsprite.draw(screen)
        pygame.display.flip()
        time.sleep(0.03)

if __name__ == "__main__":
    main()
