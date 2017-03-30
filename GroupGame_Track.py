from GroupGame_Switch import Switch
import math

class Track:

    """
    nid = the track's ID. Related to track_ids
    beginning = tuple containing the x and y coordinates of the beginning of the track
    end = tuple containing the x and y coordinates of the end of the track
    track_ids = list containing IDs of track which the switch can cycle through
        For instance, a list of [0, 5, 6] means that when the object reaches the end of the track,
        the object will change to track 0, track 5, or track 6, depending on where the switch is point at that time.
    """
    def __init__(self, nid, beginning, end, track_ids):
        self.beginningPoint = beginning
        self.endPoint = end
        self.ID = nid
        self.switch = Switch(end, track_ids)

    """
    Get the current ID of the track
    """
    def get_id(self):
        return self.ID

    """
    Determines if the object is at the end of the track. If it is, then it gives the ID of the track to start on next.
    If not, this function will return -1.
    
    What happens if we're at the end of the track, but said track is the end? This should connect to the main track
    then, which is whatever you set it to be. Add a check to tell if this connects to the main track. If it does, then
    clearly you're at the end.
    """
    def object_is_at_end(self, coords):
        if self.endPoint[0] == coords[0] and self.endPoint[1] == coords[1]:
            return self.switch.get_current_id()
        else:
            return -1

    """
    Gets the tuple of the style ( (beginningX, beginningY), (endX, endY) )
    Used mainly for drawing in pygame.
    """
    def get_tuple(self):
        return self.beginningPoint, self.endPoint

    """
    coord = tuple of the form of x,y
    
    Wait, what?
    This is a bit confusing so hold tight. You want the object to advance at a steady, solid rate for the
    entirety of its journey throughout the track toward the end. but how do we do this in such a way that it gets 
    to the target?
        The answer is percentages.
        
    This function will take in the current coordinate, and advance at a length of 5.
    If the difference in X is much bigger than the difference in Y, then it will advance more in the X direction
    Vice versa for Y. Thus we advance at a length of 5 every time this function is called.
    
    This function will return a tuple (x,y) that contains the next set of coordinates
    """
    def advance_object(self, coord):
        x, y = coord
        endX, endY = self.endPoint
        speed = 1
        distX = endX - x
        distY = endY - y
        totDist = math.sqrt(pow(distX,2) + pow(distY,2))

        distXPercentage = distX/totDist
        distYPercentage = distY/totDist

        return round(distXPercentage*speed + x), round(distYPercentage*speed + y)

    """
    Activate the switch so we connect to the next track instead of the current one
    """
    def activate_switch(self):
        self.switch.activate_switch()