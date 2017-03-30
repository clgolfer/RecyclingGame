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

    def advance_object(self, coord):
        x, y = coord
        endX, endY = self.endPoint
        speed = 5
        distX = x - endX
        distY = y - endY
        totDist = math.sqrt(pow(distX,2) + pow(distY,2))

        distXPercentage = distX/totDist
        distYPercentage = distY/totDist

        return distXPercentage*speed, distYPercentage*speed