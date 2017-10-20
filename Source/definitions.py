def make_courses():
    """Create course instances and distribute dependencies"""

    mech_reqs = [[3, 'Beekeeping', 1],
                 [4, 'FOCS', 3],
                 [4, 'EnM', 2],
                 [5, 'MatSci', 1]]

    bees_reqs = [[2, 'FOCS', 1],
                 ['Beekeeping', 3, 'MatSci', 2]]

    focs_reqs = [['FOCS', 3, 'EnM', 1]]

    robo_reqs = [['FunRobo', 2, 'MechProto', 5],
                 ['FunRobo', 2, 'Beekeeping', 3],
                 ['FunRobo', 2, 'FOCS', 3],
                 ['FunRobo', 2, 'EnM', 2],
                 ['FunRobo', 2, 'MatSci', 2]]

    mech = Course('Mechanical Prototyping', '', 5, mech_reqs)
    bees = Course('Sustainable Beekeeping', '', 4, bees_reqs)
    focs = Course('Fundamentals of Computer Science', '', 4, focs_reqs)
    elec = Course('Electricity & Magnetism', '', 3, 0)
    mats = Course('Material Science', '', 3, 0)
    robo = Course('Fundamentals of Robotics', '', 2, robo_reqs)

    print(robo.reqs)
    return [mech, bees, focs, elec, mats, robo]

class Course(object):
    """Course option
    Contains: description for graphics, max level, order, and current level"""
    def __init__(self, name, info, maxLvl, reqs):
        self.name = name
        self.info = info
        self.max = maxLvl
        self.reqs = reqs
        self.order = 0
        self.lvl = 0
    def __repr__(self):
        return '({}, {}, {})'.format(self.info, self.lvl, self.order)
    def addorder(self, roundNumber):
        self.order = roundNumber
        self.lvl = 1
    def levelup(self):
        self.lvl = self.lvl + 1

if __name__ == "__main__":
    make_courses()
