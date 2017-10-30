# Author: Isa Blancett
# Project: Interactive Programming
# Date: 10.30.2017
# Description: Class for current gameplay status, including course levels and
# round number
# Acknowledgements: Script structure is modeled after Transcriptase's Game
# repository on Git

from sys import exit
import courses
import doctest
import pygame

class Gameplay(object):
#Parses player commands and manipulates a map object

    def __init__ (self, courses):
        self.courses = courses # dictionary of course instances
        self.labels = list(courses) # list of four letter labels for each course
        self.order = [] # list of labels in order of the player's choosing
        self.round = 0 # round number of the current game

    def add_order(self, selection):
        """ adds the order to a course's class instance if picked

        returns: boolean (have all courses been picked?)

        Examples:
        >>> test_game = Gameplay(courses.populate(), 0)
        >>> test_game.add_order('mech')
        >>> print(test_game.courses['mech'].order)
        1
        """
        # increase round
        self.round = self.round + 1

        # add order and level up newest choice
        label = selection.pressed
        self.courses[label].order = self.round
        self.courses[label].lvl = 1
        self.order.append(label)

        # return whether all courses have been picked
        return len(self.order) == len(list(self.courses))

    def level_up(self):
        """ level up any courses that meet all requirements starting with the
        user's previous choice

        returns: None

        Examples:
        >>> test_game = Gameplay(courses.populate(), 0)
        >>> test_game.add_order('mech')
        >>> test_game.add_order('elec')
        >>> test_game.level_up()
        >>> print(test_game.courses['mech'].lvl)
        2
        """
        # No leveling up until 2 courses have been picked
        if len(self.order) > 1:
            # Start leveling with second most recent course selection
            for label in reversed(self.order[:-1]):
                # Check for maxed out and for dependencies
                if int(self.courses[label].lvl) < int(self.courses[label].max) and self.check_reqs(label):
                    self.courses[label].lvl = self.courses[label].lvl + 1
        return

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

        # Loop through reqs of given class
        for req in self.courses[label].reqs:
            # Parse req string for dependent level, needed course, and needed course level
            deplvl = int(req[0])
            neededcourse = req[1:5]
            neededlevel = int(req[-1])
            if deplvl == lvl:
                # Append list with True if req has been met
                reqs_met.append(neededlevel <= self.courses[neededcourse].lvl)
        # Return true if all reqs are met or no reqs are needed
        return all(reqs_met) or not len(reqs_met)

    def evaluate_portfolio(self):
        """ decides whether the user has picked the right order

        returns: None

        Examples:
        >>> test_game = Gameplay(courses.populate(), 0)
        >>> test_game.evaluate_portfolio()
        "Your portfolio could use a little more work. Try again?"
        """
        # Get list of current levels and max levels
        lvls = [int(self.courses[label].lvl) for label in list(self.courses)]
        maxlvls = [int(self.courses[label].max) for label in list(self.courses)]
        # 1 = perfect game, 2 = acceptable game, 0 = bad game (no job 4 u!!)
        if lvls == maxlvls:
            return 1
        elif (sum(lvls)) >= (sum(maxlvls)*3/4):
            return 2
        else:
            return 0

# Example docstring test
# doctest.run_docstring_examples(Gameplay.evaluate_portfolio, globals(), verbose=True)
