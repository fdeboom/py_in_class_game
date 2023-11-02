import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The best game ever")  # game name

running = True
while running:
    for event in pygame.event.get():
        pass

    pygame.display.flip()  #updates your changes