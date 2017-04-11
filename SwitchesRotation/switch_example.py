import pygame
from pygame.locals import *
from switch_animation import switch_animation

pygame.init()

background = pygame.image.load("game.jpg")

window = pygame.display.set_mode((800,450))

left_switch = switch_animation(window,1)
middle_switch = switch_animation(window,2)
right_switch = switch_animation(window,3)

switches = left_switch,middle_switch,right_switch

running = True
while running:

    window.blit(background,(0,0))

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                switches[0].rotSense = 1
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                switches[1].rotSense = 1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                switches[2].rotSense = 1
        if event.type == KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
               switches[0].rotSense = -1
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                switches[1].rotSense = -1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                switches[2].rotSense = -1

    for sw in switches:
        sw.update()

    pygame.display.update()
