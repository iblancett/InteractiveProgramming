class Course(object):
    """Course option
    Contains: description for graphics, max level, order, and current level"""
    def __init__(self, name, info, maxLvl):
        self.name = name
        self.info = info
        self.max = maxLvl
        self.reqs = [0]*maxLvl
        self.order = 0
        self.lvl = 0
    def __repr__(self):
        return '({}, {}, {})'.format(self.info, self.lvl, self.order)
    def addreqs(self, effectLvl, cause, causeLvl):
        print(self.reqs)
        if self.reqs[effectLvl-1]:
            self.reqs[effectLvl-1].extend([cause, causeLvl])
        else:
            self.reqs[effectLvl-1] = [cause, causeLvl]
    def addorder(self, roundNumber):
        self.order = roundNumber
        self.lvl = 1
    def levelup(self):
        self.lvl = self.lvl + 1
