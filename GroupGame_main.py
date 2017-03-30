import pygame
import random
from GroupGame_Track import Track

pygame.init()

#Color Pallet
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (175, 0, 175)

#Global Variable Grouping
trigger = 0
xLocation, yLocation = (250,0)
xTarget = 250
yTarget = 200
xRate = 0
yRate = 0
radius = 20
score = 0
mainTrashTrig = 0
leftTrashTrig = 0
rightTrashTrig = 0
currTrack = 0
color = BLACK


#Look at me. These are the tracks now
mainPath =      Track(0, (250,0), (250,200), (1,2,7))
RightSide =     Track(1, (250,200),(350,300), (5,6,9)) #Connects green & blue & right trash
LeftSide =      Track(2, (250,200),(150,300), (3,4,8)) #Connects red & purple & left trash
RedPath =       Track(3, (150,300),(100,350), (0,0)) #END NODE
PurplePath =    Track(4, (150,300),(200,350), (0,0)) #END NODE
GreenPath =     Track(5, (350,300),(300,350), (0,0)) #END NODE
BluePath =      Track(6, (350,300),(400,350), (0,0)) #END NODE
MainTrash =     Track(7, (250,200),(500,200), (0,0)) #END NODE
LeftTrash =     Track(8, (350,300),(500,300), (0,0)) #END NODE
RightTrash =    Track(9, (150,300),(0,300), (0,0)) #END NODE

tracks = (mainPath, RightSide, LeftSide, RedPath, PurplePath, GreenPath, BluePath, MainTrash, LeftTrash, RightTrash)


#The Required Set up for the loop
    #screen size needs to change depending of the graphics given
size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Recycle Till I Die")
done = False
clock = pygame.time.Clock()

#Paste text to the screen
def texts(score):
    font = pygame.font.Font(None, 36)
    scoreText = font.render("W, A, D for trash                      Score: " + str(score),1, (0, 0, 0))
    screen.blit(scoreText, (10,10))

#Loops till quit is called

# Associates a random color to the object
value = random.random()
if value < .25:
    color = RED
elif value < .5:
    color = BLUE
elif value < .75:
    color = GREEN
else:
    color = PURPLE

while not done:
    #Checks if an object has reached the boundaries and gives score
    track = tracks[currTrack].object_is_at_end((xLocation,yLocation))
    if(track != -1): #We have reached the end of a certain track
        if(track == 0): #Said track we have reached the end of is an end node
            if currTrack == 3: #If it's red
                if color == RED: #You did good
                    score = score + 10
                else: #You didn't
                    score = score - 10
            elif currTrack == 4: #Purple!
                if color == PURPLE:
                    score = score + 10
                else:
                    score = score - 10
            elif currTrack == 5: #Green!
                if color == GREEN:
                    score = score + 10
                else:
                    score = score - 10
            elif currTrack == 6: #Blue!
                if color == BLUE:
                    score = score + 10
                else:
                    score = score - 10
            elif currTrack == 7: #Main trash!
                score = score - 10
            elif currTrack == 8: #Left trash
                score = score - 10
            elif currTrack == 9: #Aaaaand right trash
                score = score - 10
            xLocation, yLocation = tracks[0].beginningPoint

            # Associates a random color to the object
            value = random.random()
            if value < .25:
                color = RED
            elif value < .5:
                color = BLUE
            elif value < .75:
                color = GREEN
            else:
                color = PURPLE
        currTrack = track

    #Establishes the starting path that every object takes
    xLocation,yLocation = tracks[currTrack].advance_object((xLocation,yLocation))

    #Limiter on loop time
    clock.tick(60)
    screen.fill(WHITE)

    #This for loop handles all events: IE input from mouse and keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #Mouse control, left it in incase it helps with the touchscreen later
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (alpha, omega) = pygame.mouse.get_pos()
            if (xLocation + radius > alpha and xLocation - radius < alpha):
                if(yLocation + radius > omega and yLocation - radius < omega):
                    trigger = 1

        #Keydown and Keyup are the pressing and releasing a keyboard input
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

    #These are the trashcans at the bottom of the screen, Just for visual representation
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

    pygame.draw.lines(screen, BLACK,0,mainPath.get_tuple(),1)
    pygame.draw.lines(screen, BLACK,0,RightSide.get_tuple(),1)
    pygame.draw.lines(screen, BLACK,0,LeftSide.get_tuple(),1)
    pygame.draw.lines(screen, BLACK,0,RedPath.get_tuple(),1)
    pygame.draw.lines(screen, BLACK,0,PurplePath.get_tuple(),1)
    pygame.draw.lines(screen, BLACK,0,GreenPath.get_tuple(),1)
    pygame.draw.lines(screen, BLACK,0,BluePath.get_tuple(),1)
    pygame.draw.lines(screen, BLACK,0,MainTrash.get_tuple(),1)
    pygame.draw.lines(screen, BLACK,0,RightTrash.get_tuple(),1)
    pygame.draw.lines(screen, BLACK,0,LeftTrash.get_tuple(),1)

    #Part of the mouse input so that if you click on the ball you grab it
    if (trigger == 1):
        (xLocation, yLocation) = pygame.mouse.get_pos()

    #Actual generation of the circle
    pygame.draw.circle(screen,color,(int(xLocation), int(yLocation)),radius)

    #Calls the function for displaying score
    texts(score)

    #Signal to update the screen
    #Try to put all pygame.draw after this
    pygame.display.flip()

#This is the end of the program, no code after this point
pygame.quit()