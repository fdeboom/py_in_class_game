import pygame


pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("The best game ever")  # game name

running = True
while running:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (0, 0, 255), (600, 400, 300, 200))

    pygame.display.flip()  # updates your changes at the end of loop
