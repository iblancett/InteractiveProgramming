from sys import exit
import courses
import doctest
import pygame

class Gameplay(object):
#Parses player commands and manipulates a map object

    def __init__ (self, courses):
        self.courses = courses
        self.labels = list(courses)
        self.order = []
        self.round = 0

    def add_order(self, selection):
        """ adds the order to a course's class instance if picked

        returns: boolean (have all courses been picked?)

        Examples:
        >>> test_game = Gameplay(courses.populate(), 0)
        >>> test_game.add_order('mech')
        >>> print(test_game.courses['mech'].order)
        1
        """
        self.round = self.round + 1
        for label in self.labels:
            if label == selection.pressed:
                self.courses[label].order = self.round
                self.courses[label].lvl = 1
                self.order.append(label)

        return len(self.order) == len(list(self.courses))

    def level_up(self):
        """ level up any courses that meet all requirements starting with the
        user's previous choice

        returns: dictionary of courses

        Examples:
        >>> test_game = Gameplay(courses.populate(), 0)
        >>> test_game.add_order('mech')
        >>> test_game.add_order('elec')
        >>> test_game.level_up()
        >>> print(test_game.courses['mech'].lvl)
        2
        """

        if len(self.order) > 1:
            for label in reversed(self.order):
                if 0 < int(self.courses[label].lvl) < int(self.courses[label].max) and self.check_reqs(label):
                    self.courses[label].lvl = self.courses[label].lvl + 1

    def check_reqs(self, label):
        """ given a course label, checks whether all dependencies are met

        returns: boolean

        Examples:
        >>> test_game = Gameplay(courses.populate(), 0)
        >>> test_game.courses['mech'].lvl = 4
        >>> test_game.courses['focs'].lvl = 3
        >>> test_game.courses['elec'].lvl = 2
        >>> test_game.check_reqs('mech')
        True
        >>> test_game = Gameplay(courses.populate(), 0)
        >>> test_game.courses['mech'].lvl = 4
        >>> test_game.courses['focs'].lvl = 3
        >>> test_game.check_reqs('mech')
        False
        """
        reqs_met = []
        lvl = self.courses[label].lvl
        for req in self.courses[label].reqs:
            deplvl = int(req[0])
            if deplvl == lvl:
                neededcourse = req[1:5]
                neededlevel = int(req[-1])
                reqs_met.append(neededlevel == self.courses[neededcourse].lvl)
        return all(reqs_met) or not len(reqs_met)

    def evaluate_portfolio(self):
        """ decides whether the user has picked the right order

        returns: None

        Examples:
        >>> test_game = Gameplay(courses.populate(), 0)
        >>> test_game.evaluate_portfolio()
        "Your portfolio could use a little more work. Try again?"
        """
        maxedlvls = [self.courses[label].lvl == self.courses[label].max for label in list(self.courses)]

        if all(maxedlvls):
            return "Congratulations! You created the coolest portfolio!"
        else:
            return "Your portfolio could use a little more work. Try again?"

# doctest.run_docstring_examples(Gameplay.evaluate_portfolio, globals(), verbose=True)
