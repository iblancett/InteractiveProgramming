from sys import exit
class Gameplay(object):
#Parses player commands and manipulates a map object

    def __init__ (self, courses, portfolio):
        self.courses = courses
        self.labels = [x.label for x in courses]
        self.order = []
        self.portfolio = portfolio
        self.round = 0

    def add_order(self, selection, order):
        self.round = self.round + 1
        for i in len(self.courses):
            if self.course[i].label == selection:
                self.course[i].order = self.round
                self.course[i].lvl = 1
                self.order.append(i)
                return i

    def level_up(self):
        for i in self.order:
            if self.courses[i].lvl and check_reqs(i):
                self.courses[i].lvl = self.courses[i].lvl + 1

    def check_reqs(self, i):
        ready = 0
        lvl = self.course[i].lvl
        for req in self.course[i].reqs:
            deplvl = int(req[0])
            if deplvl == lvl:
                neededcourse = req[1:5]
                neededlevel = int(req[-1])
                ready = ready + (neededlevel == self.course[self.labels.index(neededcourse)].lvl)

        return ready



    def victory(self):
        print "Congratulations! You are a winner!"
        exit(1)
