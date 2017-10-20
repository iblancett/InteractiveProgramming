import pygame
import os
from environment import *

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.mouse.set_pos([500,350])
pygame.mouse.set_visible(True)
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                setUpE(screen)
                if event.type == pygame.mouse.get_pressed:
                    location = pygame.mouse.get_pos()
                    pass
                    #if location >=


        pygame.display.flip()
