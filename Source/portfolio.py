import courses
import pygame
import os

class Portfolio(object):

    def __init__(self, courses, screen):
        self.labels = list(courses)
        self.screen = screen


    # def get_imgs(self, courses):
    #     imgs = []
    #     for label in self.labels:
    #         if courses[labels].lvl:
    #             imgs = 'Source/Level_Icons/%s%s.png' % (label, str(courses[labels].lvl)
    #     return imgs

    def update_imgs(self, courses):
        imgs = []
        # imgs = 'Source/Level_Icons/%s%s.png' % (label, str(courses[labels].lvl)
        for label in self.labels:
            for level in self.courses[labels].lvl:
                img = 'Source/Level_Icons/%s%s.png' % (label, int(courses[labels].lvl))
        return img

    def portfolio_image(screen, img, location):
        imgs = []
        for label in self.labels:
            for level in self.courses[labels].lvl:
                img = 'Source/Level_Icons/%s%s.png' % (label, int(courses[labels].lvl))
                pygame.draw.rect(screen, (255,255,255), (30,100,400,800))
                loaded = pygame.transform.scale(pygame.image.load(img),(108,100))
                screen.blit(img,(30,100,400,800))
                pygame.display.flip()

    def portfolio_image(screen, img, location):
        loaded = pygame.transform.scale(pygame.image.load(img),(108,100))
        while True:
            pygame.image.loaded
            screen.blit(loaded, (30,100,400,800))
        screen.blit(loaded, (30,100,400,800))
        pygame.display.flip()
        # if pygame.draw.rect(screen, (255,255,255), (30,100,400,800))
