import pygame

def setUpE(screen):
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
    pygame.display.flip()

def mouseClicks():
    '''This function looks for the click of a mouse and creates an event based on where the mouse is'''
    pass

def mouseOver(screen, font):
    '''This function looks for the position of the mouse and will display text above the buttons if the mouse is hovering over the buttons'''
    #icon descriptions
    beeDesc = font.render("Bees?", 1, (255,255,0))
    ENMDesc = font.render("Magic", 1, (255,255,0))
    FOCSDesc = font.render("Hacker d00d", 1, (255,255,0))
    FunRoboDesc = font.render("beep boop", 1, (255,255,0))
    MatSciDesc = font.render("hm...", 1, (255,255,0))
    MechProtoDesc = font.render("Mechie Art", 1, (255,255,0))
    #if statements
    (x,y) = pygame.mouse.get_pos()
    if y >= 550 and y<= 655:
        if x >= 51 and x<= 159:
            screen.blit(beeDesc, (100, 490))
        if x >= 209 and x <= 317:
            screen.blit(ENMDesc, (100, 490))
        if x >= 367 and x <= 475:
            screen.blit(FOCSDesc, (100, 490))
        if x >= 525 and x <= 633:
            screen.blit(FunRoboDesc, (100, 490))
        if x >= 683 and x <= 791:
            screen.blit(MatSciDesc, (100, 490))
        if x >= 841 and x <= 950:
            screen.blit(MechProtoDesc, (100, 490))
