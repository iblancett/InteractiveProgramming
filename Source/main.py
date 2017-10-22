# import all scripts here
import courses

def setup():

    courses = catalog.populate()

    portfolio = portfolio.Portfolio()

    gameplay = gameplay.Play(courses, portfolio)

    return gameplay

gameplay = setup()

while gameplay.victory != True:
    action = gameplay.prompt()
    gameplay.parse(action)

gameplay.victory()
