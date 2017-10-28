# import all scripts here
import courses
import gameplay
import environment
import graphics
import portfolio
import sys
from environment import *

courses = catalog.populate()
graphics.initialize()
control = Gameplay(courses)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
        if event.type == pygame.PICK:
            done = control.add_order()
            control.level_up()
        mouseOver(screen, text)
        mouseClicks()
    pygame.display.flip()
return done
