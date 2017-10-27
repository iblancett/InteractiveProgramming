# import all scripts here
import courses
import gameplay
import environment
import graphics
import portfolio
import sys

courses = catalog.populate()
graphics.initialize()
portfolio.Portfolio(courses)
gameplay.evaluate_portfolio()
