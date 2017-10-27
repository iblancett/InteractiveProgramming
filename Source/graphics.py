import pygame
import os
from environment import *

def initialize():
    """ Initializes graphic screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.font.init()
    font = pygame.font.Font(None,30)
    pygame.mouse.set_pos([500,350])
    pygame.mouse.set_visible(True)
    setUpE(screen, font)

def rungraphics():
    """ Run game's graphics
    """
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            mouseOver(screen, text)
            mouseClicks()
        pygame.display.flip()
    return done
