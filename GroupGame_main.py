import pygame
from math import pi


pygame.init()

#Color Pallet
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (175, 0, 175)

#The Required Set up for the loop
size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Recycle Till I Die")
done = False
clock = pygame.time.Clock()

#Loops till quit is called
#This is where you put code
while not done:

    #Limiter on loop time
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    #Circles to represent the targets
    pygame.draw.rect(screen, RED, [50, 465, 90, 50], 0)
    pygame.draw.ellipse(screen, BLACK, [50, 450, 90, 30], 0)
    pygame.draw.ellipse(screen, RED, [50, 450, 90, 30], 2)

    pygame.draw.rect(screen, PURPLE, [150, 465, 90, 50], 0)
    pygame.draw.ellipse(screen, BLACK, [150, 450, 90, 30], 0)
    pygame.draw.ellipse(screen, PURPLE, [150, 450, 90, 30], 2)

    pygame.draw.rect(screen, GREEN, [250, 465, 90, 50], 0)
    pygame.draw.ellipse(screen, BLACK, [250, 450, 90, 30], 0)
    pygame.draw.ellipse(screen, GREEN, [250, 450, 90, 30], 2)

    pygame.draw.rect(screen, BLUE, [350, 465, 90, 50], 0)
    pygame.draw.ellipse(screen, BLACK, [350, 450, 90, 30], 0)
    pygame.draw.ellipse(screen, BLUE, [350, 450, 90, 30], 2)

    #Signal to update the screen
    #All Drawing must be done prior to this command
    pygame.display.flip()

pygame.quit()