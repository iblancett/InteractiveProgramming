# Author: Leo Liu, Siena Okuno, & Isa Blancett
# Project: Interactive Programming
# Date: 10.30.2017
# Description: Game setup, loop through game graphics and control, & ending call

import courses
from gameplay import Gameplay
import sys
import pygame
#import ending
from environment import *

# INITIALIZE GAME
BUTTON = pygame.USEREVENT + 1
init_courses = courses.populate()
text_screen = initialize([init_courses[label].description for label in list(init_courses)])
screen = text_screen[0]
text = text_screen[1]
control = Gameplay(init_courses)

# LOOP THROUGH GRAPHICS AND CONTROLS, CHECKING FOR PASSING OF EVENTS
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
        if event.type == BUTTON:
            done = control.add_order(event)
            courses = control.level_up()
            update_portfolio(courses, screen)
        mouseOver(text, screen)
        mouseClicks(control.order, BUTTON, screen)
    pygame.display.flip()
    pygame.event.pump()

# EVALUATE ENDING AND SEND TO VICTORY SCREEN
#victory = control.evaluate_portfolio()
#if victory == 1:
#    ending.determine(victory, ["%s: %s" % (control.courses[course].name, 'MAX') for course in control.courses])
#else:
#    ending.determine(victory, ["%s: %s" % (control.courses[course].name, control.courses[course].lvl) for course in control.courses])
