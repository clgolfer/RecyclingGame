import pygame
import random
pygame.init()

#Color Pallet
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (175, 0, 175)

#color = RED
trigger = 0
xLocation = 499
yLocation = 499
xTarget = 250
yTarget = 200
xRate = 0
yRate = 0
radius = 20
score = 0
mainTrashTrig = 0
leftTrashTrig = 0
rightTrashTrig = 0

mainPath = ((250,0),(250,200))
RightSide = ((250,200),(350,300))
LeftSide = ((250,200),(150,300))
RedPath = (150,300),(100,350),(100,500)
PurplePath = (150,300),(200,350),(200,500)
GreenPath = (350,300),(300,350),(300,500)
BluePath = (350,300),(400,350),(400,500)
MainTrash = ((250,200),(500,200))
LeftTrash = ((350,300),(500,300))
RightTrash = ((150,300),(0,300))

#The Required Set up for the loop
size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Recycle Till I Die")
done = False
clock = pygame.time.Clock()

def texts(score):
    font = pygame.font.Font(None, 36)
    scoreText = font.render("W, A, D for trash                      Score: " + str(score),1, (0, 0, 0))
    screen.blit(scoreText, (10,10))

#Loops till quit is called
#This is where you put code
while not done:
    if(yLocation > 470 or xLocation > 470 or xLocation < 30):
        if(xLocation > 60 and xLocation < 140 and color == RED):
            score = score + 10
        elif(xLocation > 160 and xLocation < 240 and color == PURPLE):
            score = score + 10
        elif(xLocation > 260 and xLocation < 340 and color == GREEN):
            score = score + 10
        elif(xLocation > 360 and xLocation < 440 and color == BLUE):
            score = score + 10
        yLocation = 100
        xLocation = 250
        xTarget,yTarget = mainPath[1]
        xRate = abs(xTarget-xLocation)/50
        yRate = abs(yTarget-yLocation)/50
    if(yLocation == 100):
        value = random.random()
        if value < .25:
            color = RED
        elif value < .5:
            color = BLUE
        elif value < .75:
            color = GREEN
        else:
            color = PURPLE
    #Limiter on loop time
    clock.tick(60)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (alpha, omega) = pygame.mouse.get_pos()
            if (xLocation + radius > alpha and xLocation - radius < alpha):
                if(yLocation + radius > omega and yLocation - radius < omega):
                    trigger = 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mainTrashTrig = 1
            elif event.key == pygame.K_a:
                leftTrashTrig = 1
            elif event.key == pygame.K_d:
                rightTrashTrig = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                mainTrashTrig = 0
            elif event.key == pygame.K_a:
                leftTrashTrig = 0
            elif event.key == pygame.K_d:
                rightTrashTrig = 0
        #elif event.type == pygame.key.
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

    pygame.draw.lines(screen, BLACK,0,mainPath,1)
    pygame.draw.lines(screen, BLACK,0,RightSide,1)
    pygame.draw.lines(screen, BLACK,0,LeftSide,1)
    pygame.draw.lines(screen, BLACK,0,RedPath,1)
    pygame.draw.lines(screen, BLACK,0,PurplePath,1)
    pygame.draw.lines(screen, BLACK,0,GreenPath,1)
    pygame.draw.lines(screen, BLACK,0,BluePath,1)
    pygame.draw.lines(screen, BLACK,0,MainTrash,1)
    pygame.draw.lines(screen, BLACK,0,RightTrash,1)
    pygame.draw.lines(screen, BLACK,0,LeftTrash,1)

    if (trigger == 1):
        (xLocation, yLocation) = pygame.mouse.get_pos()

    pygame.draw.circle(screen,color,(xLocation, yLocation),radius)

    texts(score)

    #Signal to update the screen
    #All Drawing must be done prior to this command
    pygame.display.flip()

    if yLocation == 200 and xTarget != 500:
        if mainTrashTrig == 1:
            xTarget,yTarget = MainTrash[1]
        elif color[0] == RED[0] and color[1] == RED[1] and color[2] == RED[2]:
            xTarget,yTarget = LeftSide[1]
        elif color[0] == PURPLE[0] and color[1] == PURPLE[1] and color[2] == PURPLE[2]:
            xTarget,yTarget = LeftSide[1]
        elif color[0] == GREEN[0] and color[1] == GREEN[1] and color[2] == GREEN[2]:
            xTarget,yTarget = RightSide[1]
        else:
            xTarget,yTarget = RightSide[1]
        xRate = (xTarget-xLocation)/50
        yRate = (yTarget-yLocation)/50
    if yLocation == 300 and xTarget != 500 and xTarget != 0:
        if leftTrashTrig == 1 and xLocation == 150:
            xTarget,yTarget = RightTrash[1]
        elif rightTrashTrig == 1 and xLocation == 350:
            xTarget,yTarget = LeftTrash[1]
        elif color[0] == RED[0] and color[1] == RED[1] and color[2] == RED[2]:
            xTarget,yTarget = RedPath[1]
        elif color[0] == PURPLE[0] and color[1] == PURPLE[1] and color[2] == PURPLE[2]:
            xTarget,yTarget = PurplePath[1]
        elif color[0] == GREEN[0] and color[1] == GREEN[1] and color[2] == GREEN[2]:
            xTarget,yTarget = GreenPath[1]
        else:
            xTarget,yTarget = BluePath[1]
        xRate = (xTarget-xLocation)/50
        yRate = (yTarget-yLocation)/50
    if yLocation == 350:
        if color[0] == RED[0] and color[1] == RED[1] and color[2] == RED[2]:
            xTarget,yTarget = RedPath[2]
        elif color[0] == PURPLE[0] and color[1] == PURPLE[1] and color[2] == PURPLE[2]:
            xTarget,yTarget = PurplePath[2]
        elif color[0] == GREEN[0] and color[1] == GREEN[1] and color[2] == GREEN[2]:
            xTarget,yTarget = GreenPath[2]
        else:
            xTarget,yTarget = BluePath[2]
        xRate = (xTarget-xLocation)/50
        yRate = (yTarget-yLocation)/50
    if xTarget == 500:
        xRate = 3
        yRate = 0
    elif xTarget == 0:
        xRate = -3
        yRate = 0
    yLocation = yLocation + yRate
    xLocation = xLocation + xRate
    #if xTarget < xLocation:
    #    xLocation = xLocation - xRate
    #elif xTarget > xLocation:
    #    xLocation = xLocation + xRate
pygame.quit()