# Author: Siena Okuno
# Project: Interactive Programming
# Date: 10.30.2017
# Description: Creates GUI for player and posts events when a button is clicked

import pygame
import os
import sys

def initialize(descriptions):
    """ Initializes graphic screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.font.init()
    font = pygame.font.Font(None,26)
    pygame.mouse.set_pos([500,350])
    pygame.mouse.set_visible(True)
    text = setUpE(screen, font, descriptions)
    return [screen, text]

def setUpE(screen, font, descriptions):
    '''This code is to load the basic backscreen for the program.
    setUpE is NOT to be run whenever the user clicks something, just at beginning.'''
    #loading/scaling images (loads as S___ for start, scaled as F___ for final)
    Sbee_Icon = pygame.image.load('Source/Course_Icons/bees.png')
    Fbee_Icon = pygame.transform.scale(Sbee_Icon, (108, 100))
    SENM_Icon = pygame.image.load('Source/Course_Icons/elec.png')
    FENM_Icon = pygame.transform.scale(SENM_Icon, (108, 100))
    SFOCS_Icon = pygame.image.load('Source/Course_Icons/focs.png')
    FFOCS_Icon = pygame.transform.scale(SFOCS_Icon, (108, 100))
    SFunRobo_Icon = pygame.image.load('Source/Course_Icons/robo.png')
    FFunRobo_Icon = pygame.transform.scale(SFunRobo_Icon, (108, 100))
    SMatSci_Icon = pygame.image.load('Source/Course_Icons/mats.png')
    FMatSci_Icon = pygame.transform.scale(SMatSci_Icon, (108, 100))
    SMechProto_Icon = pygame.image.load('Source/Course_Icons/mech.png')
    FMechProto_Icon = pygame.transform.scale(SMechProto_Icon, (108, 100))
    #basic background
    pygame.draw.rect(screen, (255, 255, 255), (0,10,1000,440))
    #icon buttons
    pygame.draw.rect(screen, (255, 255, 255), (51,550,108,100))
    pygame.draw.rect(screen, (255, 255, 255), (209,550,108,100))
    pygame.draw.rect(screen, (255, 255, 255), (367,550,108,100))
    pygame.draw.rect(screen, (255, 255, 255), (525,550,108,100))
    pygame.draw.rect(screen, (255, 255, 255), (683,550,108,100))
    pygame.draw.rect(screen, (255, 255, 255), (841,550,108,100))
    #icon display
    screen.blit(Fbee_Icon,(51,550))
    screen.blit(FENM_Icon,(209,550))
    screen.blit(FFOCS_Icon,(367,550))
    screen.blit(FFunRobo_Icon,(525,550))
    screen.blit(FMatSci_Icon,(683,550))
    screen.blit(FMechProto_Icon,(841,550))
    #render text
    text = []
    text.append(font.render("Sustainable Beekeeping: %s" % descriptions[0], 1, (255,255,255)))
    text.append(font.render("Electricity and Magnetism: %s" % descriptions[1], 1, (255,255,255)))
    text.append(font.render("Fundamentals of Computer Science: %s" % descriptions[2], 1, (255,255,255)))
    text.append(font.render("Fundamentals of Robotics: %s" % descriptions[3], 1, (255,255,255)))
    text.append(font.render("Material Science: %s" % descriptions[4], 1, (255,255,255)))
    text.append(font.render("Mechanical Prototyping: %s" % descriptions[5], 1, (255,255,255)))
    #Reload display / return font
    pygame.display.flip()
    return text

def mouseClicks(order, BUTTON, screen):
    '''This function looks for the click of a mouse and queues an event based on where the mouse is'''
    (x,y) = pygame.mouse.get_pos()
    clicked_path = 'Source/Course_Icons/%s_clicked.png'
    if y >= 550 and y<= 655 and any(pygame.mouse.get_pressed()):
        if x >= 51 and x<= 159 and 'bees' not in order:
            button1 = pygame.event.Event(BUTTON, pressed='bees')
            pygame.event.post(button1)
            updateImg(screen, clicked_path % 'bees', (51,550))
        elif x >= 209 and x <= 317 and 'elec' not in order:
            button2 = pygame.event.Event(BUTTON, pressed='elec')
            pygame.event.post(button2)
            updateImg(screen, clicked_path % 'elec', (209,550))
        elif x >= 367 and x <= 475 and 'focs' not in order:
            button3 = pygame.event.Event(BUTTON, pressed='focs')
            pygame.event.post(button3)
            updateImg(screen, clicked_path % 'focs', (367,550))
        elif x >= 525 and x <= 633 and 'robo' not in order:
            button4 = pygame.event.Event(BUTTON, pressed='robo')
            pygame.event.post(button4)
            updateImg(screen, clicked_path % 'robo', (525,550))
        elif x >= 683 and x <= 791 and 'mats' not in order:
            button5 = pygame.event.Event(BUTTON, pressed='mats')
            pygame.event.post(button5)
            updateImg(screen, clicked_path % 'mats', (683,550))
        elif x >= 841 and x <= 950 and 'mech' not in order:
            button6 = pygame.event.Event(BUTTON, pressed='mech')
            pygame.event.post(button6)
            updateImg(screen, clicked_path % 'mech', (841,550))

def mouseOver(text, screen):
    '''This function looks for the position of the mouse and will display text above the buttons if the mouse is hovering over the buttons'''
    #icon descriptions
    beeDesc = text[0]
    ENMDesc = text[1]
    FOCSDesc = text[2]
    FunRoboDesc = text[3]
    MatSciDesc = text[4]
    MechProtoDesc = text[5]
    #if statements
    (x,y) = pygame.mouse.get_pos()
    if y >= 550 and y<= 655:
        if x >= 51 and x<= 159:
            screen.blit(beeDesc, (100, 490))
        elif x >= 209 and x <= 317:
            screen.blit(ENMDesc, (100, 490))
        elif x >= 367 and x <= 475:
            screen.blit(FOCSDesc, (100, 490))
        elif x >= 525 and x <= 633:
            screen.blit(FunRoboDesc, (100, 490))
        elif x >= 683 and x <= 791:
            screen.blit(MatSciDesc, (100, 490))
        elif x >= 841 and x <= 950:
            screen.blit(MechProtoDesc, (100, 490))
        else:
            pygame.draw.rect(screen, (0,0,0), (0,480,1000,50))
    else:
        pygame.draw.rect(screen, (0,0,0), (0,480,1000,50))

def updateImg(screen, img, location):
    loaded = pygame.transform.scale(pygame.image.load(img), (108, 100))
    screen.blit(loaded, location)
    pygame.display.flip()

def update_portfolio(courses, screen):
    labels = list(courses)
    pygame.draw.rect(screen, (255,255,255), (0,10,1000,440))
    for label in labels:
        if courses[label].lvl:
            img = 'Source/Level_Icons/%s%s.png' % (label, courses[label].lvl)
            xmin = int(courses[label].range)
            updateImg(screen, img, (xmin, 150))
