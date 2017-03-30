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

    def activate_switch(self):
        self.currentID = next(self.trackIDs)

    def get_current_id(self):
        return self.currentID
