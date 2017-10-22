import csv

class Courses(object):
    #properties of all items

    def setup(self, config):
        # Takes in a dictionary and assigns item properties according to labels
        self.config = config

        self.label = config['label']
        #one word, serves as key in dictionary and shortest name

        self.course = config['course']
        #full course title

        self.description = config['description']
        #full detailed descriptive text

        self.levels = config['levels']
        #number of levels in course

        self.dependencies = config['dependencies']
        #string matching label of starting room


# Sets up item objects by creating a config dictionary for each one
#
# Sample config dictionary (can be copied for each new item):
#config = {
#   'label':'LABEL'
#   'course':'COURSE TITLE',
#   'description':'DESCRIPTION',
#   'levels': NUMBER OF LEVELS,
#   'dependent levels': [[LVL, 'COURSE', COURSELVL],
#}

#'label' : a single word string used as an internal id
#'course': full course title
#'decription': the full verbose description
#'dependencies': nested list of levels effected by other courses



def create_course(config):
    course = Course()
    new_item.setup(config)
    return(new_item)

def populate():
    #runs each of the item creation functions
    #and returns a dictionary of all the items
    all_items = {}

    f = open('data/courses.csv', 'rb')
    reader = csv.DictReader(f)

    for row in reader:
        if row != '0':
            row['dependencies'] = row['dependencies'].split()
        else:
            row['dependencies'] = []
        new_course = (create_course(row))
        all_courses[new_course.label] = new_course

    return(all_courses)
