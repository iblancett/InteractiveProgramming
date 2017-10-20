import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.mouse.set_pos([200,150])
pygame.mouse.set_visible(True)
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.mouse.get_pressed:
                    pass


        pygame.display.flip()
