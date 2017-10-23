from sys import exit
import courses
import doctest

class Gameplay(object):
#Parses player commands and manipulates a map object

    def __init__ (self, courses, portfolio):
        self.courses = courses
        self.labels = list(courses)
        self.order = []
        self.portfolio = portfolio
        self.round = 0

    def add_order(self, selection):
        """ adds the order to a course's class instance if picked

        Examples:
        >>> test_game = Gameplay(courses.populate(), 0)
        >>> test_game.add_order('mech')
        >>> print(test_game.courses['mech'].order)
        1
        """
        self.round = self.round + 1
        for label in self.labels:
            if label == selection:
                self.courses[label].order = self.round
                self.courses[label].lvl = 1
                self.order.append(label)

    def level_up(self):
        """ level up any courses that meet all requirements
        Examples:
        >>> test_game = Gameplay(courses.populate(), 0)
        >>> test_game.add_order('mech')
        >>> test_game.level_up()
        >>> print(test_game.courses['mech'].lvl)
        2
        """

        for label in self.order:
            if self.courses[label].lvl and self.check_reqs(label):
                self.courses[label].lvl = self.courses[label].lvl + 1

    def check_reqs(self, label):
        reqs_met = []
        lvl = self.courses[label].lvl
        for req in self.courses[label].reqs:
            deplvl = int(req[0])
            if deplvl == lvl:
                neededcourse = req[1:5]
                neededlevel = int(req[-1])
                reqs_met.append(neededlevel == self.courses[neededcourse].lvl)

        return any(reqs_met) or not reqs_met



    def victory(self):
        print("Congratulations! You are a winner!")
        exit(1)

doctest.run_docstring_examples(Gameplay.level_up, globals())
