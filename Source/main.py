# import all scripts here
import courses
import gameplay
import environment

def setup():

    courses = catalog.populate()

    portfolio = environment.Portfolio()

    return gameplay(courses, portfolio)

game = setup()

ended = False

while ended != True:
    selection = environment.prompt()
    ended = gameplay.add_order(selection)
    courses = gameplay.level_up()

gameplay.evaluate_portfolio()
