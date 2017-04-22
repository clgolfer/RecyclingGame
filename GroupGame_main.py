import pygame
import random
from GroupGame_Track import Track
from SwitchesRotation.switch_animation import switch_animation

pygame.init()

#The Required Set up for the loop
    #screen size needs to change depending of the graphics given
size = [800, 450]
screen = pygame.display.set_mode(size)

#Various images used
background = pygame.image.load("SwitchesRotation/game.jpg")
bottle = pygame.image.load("bottle.png")
glassBottle = pygame.image.load("glass bottle.png")
paper = pygame.image.load("paper.png")
trashcan = pygame.image.load("trashcan.png")

#Color Pallet
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (175, 0, 175)

#Global Variable Grouping
radius = 20
score = 0
currTrack = 0
color = BLACK
nextColor = WHITE

#scale the recyclables to the correct size
bottle = pygame.transform.smoothscale(bottle, (radius, 2*radius))
glassBottle = pygame.transform.smoothscale(glassBottle, (radius, 2*radius))
paper = pygame.transform.smoothscale(paper, (2*radius, 2*radius))
trashcan = pygame.transform.smoothscale(trashcan, (2*radius, 2*radius))

#Look at me. These are the tracks now
mainPath0 =      Track(0, (361,30), (371,177), (1,1))
mainPathSplit0 =    Track(1, (371,177), (428,208), (5,2))
derivPath10 =       Track(2, (429,208),(429,262), (3,3))
derivPath11 =       Track(3, (249,208), (368,304), (4,4))
derivPath1End =     Track(4, (368,304),(367,369), (0,0)) #END NODE
mainPathSplit1 =    Track(5, (492, 208), (524,261), (7,6))
derivPath2End =       Track(6, (524,261), (523,374), (0,0)) #END NODE
mainPath1 =    Track(7, (524,261), (581,283), (8,8))
mainPathSplit2 =    Track(8, (581,283), (655,284), (10,9))
derivPath3End = Track(9, (655,284), (657, 370), (0,0)) #END NODE
mainPath3 =     Track(10, (655, 284), (796, 279), (0,0)) #END NODE


mainPathSplit0.activate_switch()
mainPathSplit1.activate_switch()
mainPathSplit2.activate_switch()

tracks = (mainPath0,mainPathSplit0,derivPath10,derivPath11,derivPath1End,mainPathSplit1,derivPath2End, mainPath1,
          mainPathSplit2,derivPath3End,mainPath3)

"""
Track layout based on the above.
 |
 |
0|
  \1
   \
    \
   2|\5
    | \
    /  \
  3/   |\7
  |    | \
  |    |  \____ ___10 trash
  |    |   8   |
 4|   6|      9|
bot gbot  paper
"""

left_switch = switch_animation(screen,1)
middle_switch = switch_animation(screen,2)
right_switch = switch_animation(screen,3)

switches = left_switch,middle_switch,right_switch

xLocation, yLocation = tracks[0].beginningPoint

pygame.display.set_caption("Recycle Till I Die")
done = False
clock = pygame.time.Clock()

#Paste text to the screen
def texts(score):
    font = pygame.font.Font("DIN Condensed.ttf", 36)
    scoreText = font.render(str(score),1, (0,0,0))
    directionsText = font.render("Tap Switch to Recycle",1, (0, 0, 0))
    screen.blit(scoreText, (103,100))
    screen.blit(directionsText, (550, 100))

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
# Associates a random color to the next object
value = random.random()
if value < .25:
    nextColor = RED
elif value < .5:
    nextColor = BLUE
elif value < .75:
    nextColor = GREEN
else:
    nextColor = PURPLE

while not done:
    screen.blit(background,(0,0))
    pygame.mouse.set_visible(False)
    #Checks if an object has reached the boundaries and gives score
    track = tracks[currTrack].object_is_at_end((xLocation,yLocation))
    if(track != -1): #We have reached the end of a certain track
        if(track == 0): #Said track we have reached the end of is an end node
            if currTrack == 4: #Purple! Bottle!
                if color == PURPLE: #You did good
                    score = score + 10
                else: #You didn't
                    score = score - 10
                color = nextColor #update to the next thing
            elif currTrack == 6: #Blue! Glass bottle!
                if color == BLUE:
                    score = score + 10
                else:
                    score = score - 10
                color = nextColor #update to the next thing
            elif currTrack == 9: #Green! Paper!
                if color == GREEN:
                    score = score + 10
                else:
                    score = score - 10
                color = nextColor #update to the next thing
            elif currTrack == 10: #If it's red. Trash!
                if color == RED: 
                    score = score + 10
                else: 
                    score = score - 10
                color = nextColor #update to the next thing
            xLocation, yLocation = tracks[0].beginningPoint

            # Associates a random color to the next object
            value = random.random()
            if value < .25:
                nextColor = RED
            elif value < .5:
                nextColor = BLUE
            elif value < .75:
                nextColor = GREEN
            else:
                nextColor = PURPLE
        currTrack = track

    #Establishes the starting path that every object takes
    xLocation,yLocation = tracks[currTrack].advance_object((xLocation,yLocation))

    #Limiter on loop time
    clock.tick(60)

    #This for loop handles all events: IE input from mouse and keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #Mouse control, left it in incase it helps with the touchscreen later
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (alpha, omega) = pygame.mouse.get_pos()
            if 373 > omega and 340 < omega:
                if 439 > alpha and 409 < alpha:
                    trigger = 1
                    switches[0].rotSense = -switches[0].rotSense
                    tracks[1].activate_switch()  # First
                elif 597 > alpha and 563 < alpha:
                    trigger = 1
                    switches[1].rotSense = -switches[1].rotSense
                    tracks[5].activate_switch() #Second
                elif 731 > alpha and 700 < alpha:
                    trigger = 1
                    switches[2].rotSense = -switches[2].rotSense
                    tracks[8].activate_switch()  # Third

        elif event.type == pygame.MOUSEBUTTONUP:
            trigger = 0

        '''
        #Keydown and Keyup are the pressing and releasing a keyboard input
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xy = pygame.mouse.get_pos();
            if xy[1] > 340 or xy[1] < 373:
                if xy[0]>409 or xy[0]<439:
                    switches[0].rotSense = -switches[0].rotSense
                    tracks[1].activate_switch() #First
                elif xy[0]>563 or xy[0]<597:
                    switches[1].rotSense = -switches[1].rotSense
                    tracks[5].activate_switch() #Second
                elif xy[0]>700 or xy[0]<731:
                    switches[2].rotSense = -switches[2].rotSense
                    tracks[8].activate_switch() #Third

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                x = 1
                #switches[0].rotSense = -1
                #tracks[1].activate_switch() #First
            elif event.key == pygame.K_a:
                switches[1].rotSense = -1
                tracks[5].activate_switch() #Second
            elif event.key == pygame.K_d:
                switches[2].rotSense = -1
                tracks[8].activate_switch() #Third
                '''

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

    '''
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
    '''
    
    #blit the recyclable to the screen
    if color == RED:
        screen.blit(trashcan, (int(xLocation)-radius, int(yLocation)-radius))
    elif color == PURPLE:
        screen.blit(bottle, (int(xLocation)-radius/2, int(yLocation)-radius))
    elif color == GREEN:
        screen.blit(paper, (int(xLocation)-radius, int(yLocation)-radius))
    elif color == BLUE:
        screen.blit(glassBottle, (int(xLocation)-radius/2, int(yLocation)-radius))

    #blit the next recyclable in the "Coming up" spot
    if nextColor == RED:
        screen.blit(trashcan, (77, 268))
    elif nextColor == PURPLE:
        screen.blit(bottle, (85,268))
    elif nextColor == GREEN:
        screen.blit(paper, (77,268))
    elif nextColor == BLUE:
        screen.blit(glassBottle, (85,268))
        
    #Calls the function for displaying score
    texts(score)

    for sw in switches:
        sw.update()

    #Signal to update the screen
    #Try to put all pygame.draw after this
    pygame.display.flip()

#This is the end of the program, no code after this point
pygame.quit()
