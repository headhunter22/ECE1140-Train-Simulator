class Block:

    # constructor
    def __init__(self, blockInfo, section):
        # info attributes
        self.blockName = blockInfo[0]
        self.length = round(float(blockInfo[1]) * 3.28084)
        self.grade = blockInfo[2]
        self.speedLimit = round(float(blockInfo[3]) * 0.621371)
        self.infrastructure = blockInfo[4]
        self.stationSide = blockInfo[5]
        self.elevation = round(float(blockInfo[6]) * 3.28084)
        self.cumElevation = round(float(blockInfo[7]) * 3.28084)
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