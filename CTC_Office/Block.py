class Block:

    # constructor
    def __init__(self, blockInfo):
        self.blockName = blockInfo[0]
        self.length = blockInfo[1]
        self.grade = blockInfo[2]
        self.speedLimit = blockInfo[3]
        self.infrastructure = blockInfo[4]
        self.stationSide = blockInfo[5]
        self.elevation = blockInfo[6]
        self.cumElevation = blockInfo[7]

        self.occupied = False
        self.switchConnection = False
        self.maintenance = False

    # declare methods
    def setMaintenance(self, underMaintenance):
        maintenance = underMaintenance