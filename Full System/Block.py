from Beacon import Beacon

class Block:

    # constructor
    def __init__(self, blockInfo, section):
        # info attributes
        self.blockName = blockInfo[0]
        self.length = blockInfo[1]
        self.grade = blockInfo[2]
        self.speedLimit = int(blockInfo[3])
        self.infrastructure = blockInfo[4]
        self.stationSide = blockInfo[5]
        self.elevation = blockInfo[6]
        self.cumElevation = blockInfo[7]
        self.secsToTraverse = blockInfo[8]
        self.beaconBool = bool(blockInfo[9])
        self.lastStation = blockInfo[10]
        self.stationBool = blockInfo[11]
        self.switchBool = blockInfo[12]
        self.underground = blockInfo[15]

        self.beacon = Beacon()

        # travel direction 0 means going from lower block # to higher block #
        # travel diretion 1 means going from higher block # to lower block # 
        self.travelDirection = 0
            
        self.section = section

        # boolean attributes
        self.occupied = False
        self.maintenance = False

        # switch logic
        if self.switchBool:
            self.swOpt1 = blockInfo[13]
            self.swOpt2 = blockInfo[14]
        else:
            self.swOpt1 = None
            self.swOpt2 = None

        # add beacon if needed
        if self.beaconBool:
            # if there's a station at this beacon, add that info
            if self.stationBool:
                self.beacon.stationName = self.infrastructure
                self.beacon.stationSide = self.stationSide
            if self.switchBool:
                self.beacon.switchFrom = self.blockName
                self.beacon.switchTo = self.swOpt1

    # declare methods
    def setMaintenance(self, underMaintenance):
        maintenance = underMaintenance

    def addBeacon(self, beacon):
        self.beacon = beacon