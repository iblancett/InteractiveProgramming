# import all scripts here
import courses
import gameplay
import environment
import graphics
import portfolio

def setup():

    courses = catalog.populate()
    environment = graphics()
    portfolio = portfolio.Portfolio(courses)

    return gameplay(courses)

game = setup()
ended = False
while ended != True:
    selection = environment.prompt()
    ended = gameplay.add_order(selection)
    courses = gameplay.level_up()

gameplay.evaluate_portfolio()
