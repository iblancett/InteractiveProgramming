from definitions import *

def options():
    names = ['MechProto', 'Beekeeping', 'FOCS', 'EnM', 'MatSci', 'FunRobo']
    numCourses = len(names)
    descriptions = ['', '', '', '', '', '']
    numLvls = [5, 4, 3, 3, 3, 2]

    course1 = Course(names[0], descriptions[0], numLvls[0])
    course2 = Course(names[1], descriptions[1], numLvls[1])
    course3 = Course(names[2], descriptions[2], numLvls[2])
    course4 = Course(names[3], descriptions[3], numLvls[3])
    course5 = Course(names[4], descriptions[4], numLvls[4])
    course6 = Course(names[5], descriptions[5], numLvls[5])

    dependencies = [['MechProto', 3, 'Beekeeping', 1],
                    ['MechProto', 4, 'FOCS', 3],
                    ['MechProto', 4, 'EnM', 2],
                    ['MechProto', 5, 'MatSci', 1],
                    ['Beekeeping', 2, 'FOCS', 1],
                    ['Beekeeping', 3, 'MatSci', 2],
                    ['FOCS', 3, 'EnM', 1],
                    ['FunRobo', 2, 'MechProto', 5],
                    ['FunRobo', 2, 'Beekeeping', 3],
                    ['FunRobo', 2, 'FOCS', 3],
                    ['FunRobo', 2, 'EnM', 2],
                    ['FunRobo', 2, 'MatSci', 2]]

    for req in dependencies:
        names.index(req[0])
