class Course(object):
    """Course option
    Contains: description for graphics, max level, order, and current level"""
    def __init__(self, info, maxLvl):
        self.info = info
        self.max = maxLvl
        self.order = 0
        self.lvl = 0
    def __repr__(self):
        return '({}, {}, {})'.format(self.info, self.lvl, self.order)

class Reqs(object):
    """Requirements for course to level
    Contains: all dependencies"""
    def __init__(self, name):
        self.name = name
        self.reqlist = []
    def addreqs(self, reqlist):
        self.reqlist = reqlist
