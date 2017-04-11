import pygame
import random
from GroupGame_Track import Track
from SwitchesRotation.switch_animation import switch_animation

pygame.init()

#The Required Set up for the loop
    #screen size needs to change depending of the graphics given
size = [800, 450]
screen = pygame.display.set_mode(size)

background = pygame.image.load("SwitchesRotation/game.jpg")

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
    screen.blit(background,(0,0))

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
                switches[0].rotSense = -switches[0].rotSense
                tracks[1].activate_switch() #First
            elif event.key == pygame.K_a:
                switches[1].rotSense = -switches[1].rotSense
                tracks[5].activate_switch() #First
            elif event.key == pygame.K_d:
                switches[2].rotSense = -switches[2].rotSense
                tracks[8].activate_switch() #Third
                '''
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
    #Actual generation of the circle
    pygame.draw.circle(screen,color,(int(xLocation), int(yLocation)),radius)

    #Calls the function for displaying score
    texts(score)

    for sw in switches:
        sw.update()

    #Signal to update the screen
    #Try to put all pygame.draw after this
    pygame.display.flip()

#This is the end of the program, no code after this point
pygame.quit()