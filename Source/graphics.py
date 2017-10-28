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
    text = setUpE(screen, font)
    return [screen, text]
