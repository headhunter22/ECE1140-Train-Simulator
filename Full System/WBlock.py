class WBlock:
    def __init__(self):
        super().__init__()
        self.ID = ""
        self.section = ""
        self.blockNumber = 0
        self.nextBlock = 0
        self.previousBlock = 0
        self.line = 0
        self.station = 0
        self.crossing = 0
        self.crossingState = 0
        self.crossingLights = 0
        self.occupancy = 0
        self.authority = 0
        self.switch = 0
        self.switch0 = ''
        self.switch1 = ''
        self.switchstate = 0
        self.switchLights = 0
        self.fault = 0