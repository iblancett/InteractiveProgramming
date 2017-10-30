# import all scripts here
import courses
from gameplay import Gameplay
import environment
import graphics
import sys
import pygame
from environment import *

BUTTON = pygame.USEREVENT + 1
init_courses = courses.populate()
text_screen = graphics.initialize()
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
            for course in list(control.courses):
                print(course, control.courses[course].lvl)
        mouseOver(text, screen)
        mouseClicks(control.order, BUTTON)
    pygame.display.flip()
    pygame.event.pump()

victory = control.evaluate_portfolio()
print("Final Levels:")
if victory:
    for course in list(control.courses):
        print("%s: %s" % (control.courses[course].name, 'MAX'))
else:
    for course in list(control.courses):
        print("%s: %s" % (control.courses[course].name, control.courses[course].lvl))
