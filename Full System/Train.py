class Train:

    trainCounter = 0

    def __init__(self, auth, speed, ID, Power):
        super().__init__()
        self.authority = auth
        self.currentSpeed = 0
        self.suggSpeed = speed
        self.ID = ID
        self.Power = Power