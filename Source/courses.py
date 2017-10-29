import csv

class Courses(object):
    """ class for the different course options the user can choose from

    contains:
    label - 4 letter id
    course - full title
    description - in-depth summary of course
    max - total number of levels
    reqs - dependencies, '%s%s%s' % (effected level, needed course, needed level)
    lvl - current level
    order - order picked by user
    """

    def setup(self, config):

        self.config = config
        self.label = config['label']
        self.course = config['course']
        self.description = config['description']
        self.max = config['max']
        self.reqs = config['dependencies']
        self.lvl = 0
        self.order = 0



def create_course(config):
    """ creates a single instance of a course given a config dictionary

    returns: single course instance
    """

    new_course = Courses()
    new_course.setup(config)
    return(new_course)

def populate():
    """ sets up item objects by creating a config dictionary for each one

    Sample config dictionary (can be copied for each new item):
    config = {
        'label':'LABEL'
        'course':'COURSE TITLE',
        'description':'DESCRIPTION',
        'max': NUMBER OF LEVELS,
        'dependencies': 'LVL' + 'NEEDEDCOURSE' + 'NEEDEDLEVEL',
    }

    returns: dictionary of all course instances
    """
    all_courses = {}

    f = open('Source\courses.csv', 'r')
    reader = csv.DictReader(f)

    for row in reader:
        if row != '0':
            row['dependencies'] = row['dependencies'].split()
        else:
            row['dependencies'] = []
        new_course = (create_course(row))
        all_courses[new_course.label] = new_course
    return all_courses

populate()
