from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from TrainController import TrainController
import threading

class Train(QObject):
    trainCounter = 0

    def __init__(self, auth, speed, ID, line, power, actSpeed, trainController):
        super().__init__()

        self.trainController = trainController
        self.trainController.powerToTrain.connect(self.getPower)

        # id
        self.ID = ID

        # authority and speeds
        self.authority = auth
        self.currentSpeed = 0
        self.suggSpeed = speed
        self.commandedSpeed = 0
        self.commandedPower = power
        self.actSpeed = actSpeed
        self.acc = 0.5

        # location attributes
        self.line = line
        self.location = 3

        # mass info
        self.baseMass = 81950 * .453 # kgs 

        # train controller calculations thread
        #self.thread = threading.Thread(target=self.sendSpeeds)
        #self.thread.start()

    def sendSpeeds(self):
        # when the train enters a new block, track model should send signal with new commanded speed
        # and new authority, which triggers the train controller to get new speeds
        # and then this starts a recalculation
        while True:
            #print('actual speed: ' + str(self.actSpeed) + ' commanded speed: ' + str(self.commandedSpeed))
            self.trainController.getSpeed(self.actSpeed, self.commandedSpeed)

    def getPower(self, power):
        self.commandedPower = power
        #print('got power: ' + str(power))

        # calculate mass

        # calculate force
        force = 0.5 * self.baseMass

        self.actualSpeed = self.commandedPower / force