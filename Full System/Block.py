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
        self.section = section

        # boolean attributes
        self.occupied = False
        self.maintenance = False

        # switch logic
        # if the block does not have a switch, the connection is blank
        if 'SWITCH' not in self.infrastructure:
            self.switchConnection = ''
        else:
            # if the block has a connection, default to first option
            # parse out the options
            start = self.infrastructure.find('(')
            middle = self.infrastructure.find(';') 

            opt1 = self.infrastructure[start+1:middle]
            self.switchConnection = opt1

        # placeholder until train model and track model communicate
        self.passengers = 0

        # underground logic
        if 'UNDERGROUND' in self.infrastructure:
            self.underground = True
        else:
            self.underground = False

    # declare methods
    def setMaintenance(self, underMaintenance):
        maintenance = underMaintenance