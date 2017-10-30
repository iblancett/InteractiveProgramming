import courses


class Portfolio(object):

    def __init__(self, courses, screen):
        self.labels = list(courses)
        self.screen = screen

"""could be incorprated into update_imgs
    def get_imgs(self, courses):
        imgs = []
        for label in self.labels:
            if courses[labels].lvl:
                imgs = 'Source/Level_Icons/%s%s.png' % (label, str(courses[labels].lvl)
        return imgs
"""

    def update_imgs(self, courses):
        imgs = []
        # imgs = 'Source/Level_Icons/%s%s.png' % (label, str(courses[labels].lvl)
        for label in self.labels:
            for level in self.courses[labels].lvl
                imgs = 'Source/Level_Icons/%s%s.png' % (label, int(courses[labels].lvl)
        return imgs
