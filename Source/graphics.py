import pygame
import os
from environment import *

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.font.init()
font = pygame.font.Font(None,30)
pygame.mouse.set_pos([500,350])
pygame.mouse.set_visible(True)
done = False
text = setUpE(screen, font)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                mouseOver(screen, text)
                if event.type == pygame.mouse.get_pressed:
                    location = pygame.mouse.get_pos()
                    pass
                    #if location >=
        pygame.display.flip()
