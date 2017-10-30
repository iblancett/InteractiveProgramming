# import all scripts here
import courses
from gameplay import Gameplay
import environment
import sys
import pygame
import ending
from environment import *

BUTTON = pygame.USEREVENT + 1
init_courses = courses.populate()
text_screen = environment.initialize()
screen = text_screen[0]
text = text_screen[1]
control = Gameplay(init_courses)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
        if event.type == BUTTON:
            done = control.add_order(event)
            control.level_up()
        mouseOver(text, screen)
        mouseClicks(control.order, BUTTON, screen)
    pygame.display.flip()
    pygame.event.pump()


victory = control.evaluate_portfolio()
if victory == 1:
    ending.determine(victory, ["%s: %s" % (control.courses[course].name, 'MAX') for course in control.courses])
else:
    ending.determine(victory, ["%s: %s" % (control.courses[course].name, control.courses[course].lvl) for course in control.courses])
