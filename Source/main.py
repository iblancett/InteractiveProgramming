# import all scripts here
import courses
import gameplay
import environment
import graphics
import portfolio
import sys
import pygame
from environment import *

BUTTON = USEREVENT + 1
courses = catalog.populate()
text = graphics.initialize()
control = Gameplay(courses)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
        if event.type == pygame.BUTTON:
            done = control.add_order()
            control.level_up()
            for course in list(gameplay.courses):
                print course, gameplay.courses[course].lvl
        mouseOver(screen, text)
        mouseClicks(control.order, BUTTON)
    pygame.display.flip()
return done
