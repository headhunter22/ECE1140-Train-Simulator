class Train:

    trainCounter = 0

    def __init__(self, auth, speed, ID):
    def __init__(self, auth, speed, ID, line):
        super().__init__()
        
        # id
        self.ID = ID

        # authority and speeds
        self.authority = auth
        self.currentSpeed = 0
        self.suggSpeed = speed
        self.ID = ID
        self.commandedSpeed = 0
        self.commandedPower = 120

        # location attributes
        self.line = line
        self.location = 63
