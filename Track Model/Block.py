class Block:

    # constructor
    def __init__(self, blockInfo, section):
        # info attributes
        self.blockName = blockInfo[0]
        self.length = blockInfo[1]
        self.grade = blockInfo[2]
        self.speedLimit = blockInfo[3]
        self.infrastructure = blockInfo[4]
        self.stationSide = blockInfo[5]
        self.elevation = blockInfo[6]
        self.cumElevation = blockInfo[7]
        self.section = section

        # boolean attributes
        self.occupied = False
        self.maintenance = False

        # need actual logic
        self.switchConnection = False
        self.passengers = 0

        # underground logic
        if 'UNDERGROUND' in self.infrastructure:
            self.underground = True
        else:
            self.underground = False

    # declare methods
    def setMaintenance(self, underMaintenance):
        maintenance = underMaintenance