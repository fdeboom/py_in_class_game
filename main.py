import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("The best game ever")  # game name

x_coordinate = 600
y_coordinate = 400

running = True
while running:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (x_coordinate, y_coordinate, 50, 50))

    button = pygame.key.get_pressed()

    if button[pygame.K_LEFT]:
        x_coordinate -= 1
    if button[pygame.K_RIGHT]:
        x_coordinate += 1
    if button[pygame.K_DOWN]:
        y_coordinate += 1
    if button[pygame.K_UP]:
        y_coordinate -= 1
    if x_coordinate < 0:
        x_coordinate = 0
    if y_coordinate > 1200:
        y_coordinate = 1200
    if y_coordinate > 800:
        y_coordinate = 800
    if y_coordinate < 0:
        y_coordinate = 0

    if button[pygame.K_ESCAPE]:
        running = False
    if event.type == pygame.QUIT:
        break
    pygame.time.Clock().tick(60)
    pygame.display.flip()  # updates your changes at the end of loop
