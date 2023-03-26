class Train:

<<<<<<< HEAD
    trainCounter = 0

    def __init__(self, auth, speed, ID, Power):
=======
    def __init__(self, auth, speed, ID, line):
>>>>>>> 2bbdde8f835d8897a06d8fba955040a8e627fe75
        super().__init__()
        
        # id
        self.ID = ID

        # authority and speeds
        self.authority = auth
        self.currentSpeed = 0
        self.suggSpeed = speed
<<<<<<< HEAD
        self.ID = ID
        self.Power = Power
=======
        self.commandedSpeed = 0
        self.commandedPower = 120

        # location attributes
        self.line = line
        self.location = 63
>>>>>>> 2bbdde8f835d8897a06d8fba955040a8e627fe75
