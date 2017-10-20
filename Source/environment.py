import pygame

def setUpE(screen):
    #basic background
    pygame.draw.rect(screen, (255, 255, 255), (0,10,1000,490))
    #icon buttons
    pygame.draw.rect(screen, (255, 255, 255), (51,550,108,100))
    #pygame.image.load('BeeKeeping.png')    not working yet
    pygame.draw.rect(screen, (255, 255, 255), (209,550,108,100))
    pygame.draw.rect(screen, (255, 255, 255), (367,550,108,100))
    pygame.draw.rect(screen, (255, 255, 255), (525,550,108,100))
    pygame.draw.rect(screen, (255, 255, 255), (683,550,108,100))
    pygame.draw.rect(screen, (255, 255, 255), (841,550,108,100))
