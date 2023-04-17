# data needed:
# station name
# station side
# something about switches

class Beacon:
    def __init__(self, station=None, stationSide=None, swFrom=0, swTo=0):
        # for station beacons
        self.stationName = station
        self.stataionSide = stationSide

        # for switch beacons
        self.switchFrom = swFrom
        self.switchTo = swTo
        