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

mainPath = ((250,0),(250,200))
RightSide = ((250,200),(350,300))
LeftSide = ((250,200),(150,300))
RedPath = (150,300),(100,350),(100,500)
PurplePath = (150,300),(200,350),(200,500)
GreenPath = (350,300),(300,350),(300,500)
BluePath = (350,300),(400,350),(400,500)

#The Required Set up for the loop
size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Recycle Till I Die")
done = False
clock = pygame.time.Clock()

def texts(score):
    font = pygame.font.Font(None, 36)
    scoreText = font.render("Score: " + str(score),1, (0, 0, 0))
    screen.blit(scoreText, (10,10))

def bounds(x,y):
    print("Fail")

#Loops till quit is called
#This is where you put code
while not done:
    if(yLocation > 470):
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
        elif event.type == pygame.MOUSEBUTTONUP:
            trigger = 0
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

    #Example Code for creating a path.  The big grouping of numbers is a set of points and its draws a polygon through that point by point
    #pygame.draw.polygon(screen, (110, 110, 110),((200, 0), (150, 0), (150,200), (200,300), (275, 400), (300,500) ,(350,500) ,(325, 400) ,(250,300) , (200,200)))

    pygame.draw.lines(screen, BLACK,0,mainPath,1)
    pygame.draw.lines(screen, BLACK,0,RightSide,1)
    pygame.draw.lines(screen, BLACK,0,LeftSide,1)
    pygame.draw.lines(screen, BLACK,0,RedPath,1)
    pygame.draw.lines(screen, BLACK,0,PurplePath,1)
    pygame.draw.lines(screen, BLACK,0,GreenPath,1)
    pygame.draw.lines(screen, BLACK,0,BluePath,1)

    if (trigger == 1):
        (xLocation, yLocation) = pygame.mouse.get_pos()

    pygame.draw.circle(screen,color,(xLocation, yLocation),radius)

    texts(score)

    #Signal to update the screen
    #All Drawing must be done prior to this command
    pygame.display.flip()
    if yLocation == 200:
        if cmp(color,RED) == 1| cmp(color,PURPLE)==1:
            print "RED/Prupl"
            xTarget,yTarget = LeftSide[1]
        else:
            xTarget,yTarget = RightSide[1]
        xRate = abs(xTarget-xLocation)/50
        yRate = abs(yTarget-yLocation)/50
    if yLocation == 300:
        if cmp(color,RED) == 1:
            xTarget,yTarget = RedPath[1]
        elif cmp(color,PURPLE) == 1:
            xTarget,yTarget = PurplePath[1]
        elif cmp(color,GREEN) == 1:
            xTarget,yTarget = GreenPath[1]
        else:
            xTarget,yTarget = BluePath[1]
        xRate = abs(xTarget-xLocation)/50
        yRate = abs(yTarget-yLocation)/50
    if yLocation == 350:
        if cmp(color,RED) == 1:
            xTarget,yTarget = RedPath[2]
        elif cmp(color,PURPLE) == 1:
            xTarget,yTarget = PurplePath[2]
        elif cmp(color,GREEN) == 1:
            xTarget,yTarget = GreenPath[2]
        else:
            xTarget,yTarget = BluePath[2]
        xRate = abs(xTarget-xLocation)/50
        yRate = abs(yTarget-yLocation)/50

    #print xRate,yRate

    yLocation = yLocation + yRate
    xLocation = xLocation + xRate



pygame.quit()