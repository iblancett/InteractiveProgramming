# Author: Siena Okuno
# Project: Interactive Programming
# Date: 10.30.2017
# Description: Determines endings

import pygame
import sys

def screenScroll(screen, color):
    '''Turns screen a color by filling in with rectangles.'''
    for i in range(700):
        pygame.draw.rect(screen, color, (0,i,1000,i+1))
        i+=1
        pygame.display.flip()


def ending(victory, levels, screen):
    '''Creates basic, text-only ending'''
    font50 = pygame.font.Font(None, 50)
    font20 = pygame.font.Font(None, 20)
    if victory == 0 or victory == 2:
        screenScroll(screen, (0,0,0))
        screen.blit(font50.render("Looks like your profolio", 1, (255,255,255)), (150, 250))
        screen.blit(font50.render("could use some improvement", 1, (255,255,255)), (170, 350))
        for i in range(len(levels)):
            screen.blit(font20.render(levels[i], 1, (255,255,255)), (100+(i*20), 500))
        pygame.display.flip()
    if victory == 1:
        screenScroll(screen, (255,255,255))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(1)
            screen.blit(font50.render("Good job!", 1, (0,0,0)), (400, 250))
            screen.blit(font50.render("You're the ultimate Oliner!'", 1, (0,0,0)), (150, 250))
            screen.blit(font20.render('All course levels maxed. :)', 1, (0,0,0)), (450, 500))
            pygame.display.flip()
            pygame.event.pump()


#not implemented yet
def graduation():
    '''Shows graphics for graduating. Used in all endings'''
    screenScroll(screen, (255,255,255))
    font100 = pygame.font.Font(None, 100)
    screen.blit(font100.render("Congratulations,", 1, (0,0,0)), (200, 175))
    screen.blit(font100.render("Olin Grad!", 1, (0,0,0)), (325, 325))
    grad_hat = pygame.transform.scale(pygame.image.load('Ending_pics/grad_hat.png'), (250, 200))
    screen.blit(grad_hat,(350,400))
    pygame.display.flip()
    pygame.time.delay(2000)
    screenScroll(screen, (255,255,255))
    font50 = pygame.font.Font(None, 50)
    screen.blit(font100.render("You got your degree...", 1, (0,0,0)), (150, 300))
    pygame.display.flip()
    pygame.time.delay(2000)
    screenScroll(screen, (0,0,0))
    screen.blit(font100.render("But how will you fair", 1, (255,255,255)), (150, 300))
    screen.blit(font100.render("in the real world?", 1, (255,255,255)), (170, 400))
    pygame.display.flip()
    pygame.time.delay(2000)


def badEnding():
    '''Shows graphics for bad ending. Called when average is below ___.
    You tried? Desk jobs are all the rage these days.'''



def middleEnding():
    '''Shows graphics for middle ending. Called when average is above ___ but levels are not maxed.
    You are a leading engineer at your own startup'''



def goodEnding():
    '''Shows graphics for good ending. Called when levels are all maxed.
    You are the next Steve Jobs.'''


def determine(victory, levels):
    '''Determines ending.
    Victory is value 0, 1, or 2. 0 is bad, 2 is perfect.
    Levels is a list of strings. Print out with for loop'''
    graduation()
    if victory == 0:
        badEnding()
    if victory == 2:
        middleEnding()
    if victory == 1:
        goodEnding
