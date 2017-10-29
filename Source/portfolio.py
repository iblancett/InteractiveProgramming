class Portfolio(object):

    def __init__(self, courses, screen):
        self.labels = list(courses)
        self.screen = screen

    def get_imgs(self, courses):
        imgs = []
        for label in self.labels:
            if courses[labels].lvl:
                imgs = 'Source/Level_Icons/%s%s.png' % (label, str(courses[labels].lvl)
        return imgs

    def update_imgs(self, courses):
        imgs = self.get_imgs(courses)
        pass
