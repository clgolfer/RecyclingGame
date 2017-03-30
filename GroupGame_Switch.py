from itertools import cycle


class Switch:

    """
    loc = the location of the switch, a tuple of x,y
    IDs = the IDs of the tracks which the switch connects to. A list
    """
    def __init__(self, loc, IDs):
        self.location = loc
        self.trackIDs = cycle(IDs)
        self.currentID = IDs[0]

    """
    Advances once in the loop to find the next track ID
    """
    def activate_switch(self):
        self.currentID = next(self.trackIDs)

    """
    Returns the current ID
    """
    def get_current_id(self):
        return self.currentID
