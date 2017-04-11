import pygame

class switch_animation(object):

    width_Img,height_Img = 560,560   #Dimensions of every switch image

    def __init__(self,pygame_display,switch_type):
        if switch_type == 1:    #Left Switch
            self.image = pygame.image.load("door1centered.png") #Switch image
            self.maxAngle = 115                                 #Max rotation angle
            self.center = 445,238                               #Position of switch center
        elif switch_type == 2:  #Middle Switch
            self.image = pygame.image.load("door2centered.png")
            self.maxAngle = 115
            self.center = 540,290
        elif switch_type == 3:  #Right Switch
            self.image = pygame.image.load("door3centered.png")
            self.maxAngle = 90
            self.center = 672,305

        self.display = pygame_display                           #Pygame display object
        scaleRatio = 1/5.3
        self.image = pygame.transform.smoothscale(self.image,(int(self.width_Img*scaleRatio),int(self.height_Img*scaleRatio)))    #Scaling down the image
        self.rotAngle = 0                                       #Initial rotation angle (degrees)
        self.rotSense = -1                                      #Initial rotation sense (up)
        self.minAngle = 0                                       #Min rotation angle
        self.rotRate = 2.5                                      #Rotation rate (degrees)


    #Rotating the image and blitting it to the pygame display.
    def update(self):
        if self.rotAngle + self.rotRate*self.rotSense < self.minAngle:          #Checking for angle between bounds
            self.rotAngle = self.minAngle
        elif self.rotAngle + self.rotRate*self.rotSense > self.maxAngle:
            self.rotAngle = self.maxAngle
        else:
            self.rotAngle += self.rotRate*self.rotSense

        #We get the bound rectangle from the rotated image to
        # re-center the rotated image to the original center
        rotImage = pygame.transform.rotate(self.image, self.rotAngle)
        rect = rotImage.get_rect()
        x,y = rect.width,rect.height
        self.display.blit(rotImage,(self.center[0] - x/2,self.center[1] - y/2))
        #self.display.blit(rotImage,(self.center[0],self.center[1]))



