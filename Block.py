class Block:

    # constructor
    def __init__(self, blockName, occupied, length, elevation, grade, speedLimit, stationSide, underground, switchConnection, passengers, maintenance):
        self.blockName = blockName
        self.occupied = occupied
        self.length = length
        self.elevation = elevation
        self.grade = grade
        self.speedLimit = speedLimit
        self.stationSide = stationSide
        self.underground = underground
        self.switchConnection = switchConnection
        self.passengers = passengers
        self.maintenance = maintenance

    # declare methods
    def setMaintenance(self, underMaintenance):
        maintenance = underMaintenance