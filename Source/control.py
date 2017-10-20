from definitions import *

mech_reqs = [[3, 'Beekeeping', 1],
             [4, 'FOCS', 3],
             [4, 'EnM', 2],
             [5, 'MatSci', 1]]

bees_reqs = [[2, 'FOCS', 1],
             [3, 'MatSci', 2]]

focs_reqs = [[3, 'EnM', 1]]

robo_reqs = [[2, 'MechProto', 5],
             [2, 'Beekeeping', 3],
             [2, 'FOCS', 3],
             [2, 'EnM', 2],
             [2, 'MatSci', 2]]

mech = Course('Mechanical Prototyping', '', 5, mech_reqs)
bees = Course('Sustainable Beekeeping', '', 4, bees_reqs)
focs = Course('Fundamentals of Computer Science', '', 4, focs_reqs)
elec = Course('Electricity & Magnetism', '', 3, 0)
mats = Course('Material Science', '', 3, 0)
robo = Course('Fundamentals of Robotics', '', 2, robo_reqs)


def give_order(selection, order):
    if selection == mech.name:
        mech.addorder(order)
    if selection == bees.name:
        bees.addorder(order)
    if selection == focs.name:
        focs.addorder(order)
    if selection == elec.name:
        elec.addorder(order)
    if selection == mats.name:
        mats.addorder(order)
    if selection == robo.name:
        robo.addorder(order)

if __name__ == "__main__":
    make_courses()
    give_order('Mechanical Prototyping', 1)
    print(mech.lvl)
