import pygame


pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("The best game ever")  # game name

x_coordinate = 600
y_coordinate = 400

running = True
while running:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (0, 0, 255), (x_coordinate, y_coordinate, 300, 200))

    button = pygame.key.get_pressed()

    if button[pygame.K_LEFT]:
        x_coordinate -= 1
    if button[pygame.K_RIGHT]:
        x_coordinate += 1
    if button[pygame.K_DOWN]:
        y_coordinate += 1
    if button[pygame.K_UP]:
        y_coordinate -= 1

    if button[pygame.K_ESCAPE]:
        running = False


    pygame.display.flip()  # updates your changes at the end of loop
