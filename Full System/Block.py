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
        self.beacon = Beacon()

        # travel direction 0 means going from lower block # to higher block #
        # travel diretion 1 means going from higher block # to lower block # 
        self.travelDirection = 0
            
        self.section = section

        # boolean attributes
        self.occupied = False
        self.maintenance = False

        # switch logic
        # if the block does not have a switch, the connection is blank
        if 'SWITCH' not in self.infrastructure:
            self.switchConnection = ''
            
            if 'UNDERGROUND' in self.infrastructure:
                self.station = self.infrastructure.replace('; UNDERGROUND', '')
            else:
                self.station = self.infrastructure

            # add beacon if needed
            if blockInfo[9]:
                self.beacon.stationName = self.station
                
                # set beacon to be the station side as listed
                self.beacon.stationSide = self.stationSide

                print(self.beacon.stationName, self.beacon.stationSide)
        else:
            # if the block has a connection, default to first option
            # parse out the options
            start = self.infrastructure.find('(')
            middle = self.infrastructure.find(';') 

            opt1 = self.infrastructure[start+1:middle]
            self.switchConnection = opt1

            self.beacon.swFrom = self.blockName
            self.beacon.swTo = self.blockName

        # underground logic
        if 'UNDERGROUND' in self.infrastructure:
            self.underground = True
        else:
            self.underground = False

    # declare methods
    def setMaintenance(self, underMaintenance):
        maintenance = underMaintenance

    def addBeacon(self, beacon):
        self.beacon = beacon