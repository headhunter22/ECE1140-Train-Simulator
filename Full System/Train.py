from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from TrainController import TrainController
from threading import Thread
import time
import math

class Train(QObject):
    trainCounter = 0

    def __init__(self, auth, speed, ID, line, power, actSpeed, trainController, track):
        super().__init__()

        self.trainController = trainController
        self.trainController.powerToTrain.connect(self.getPower)

        self.track = track

        # id
        self.ID = ID

        # location attributes
        self.line = line
        self.location = 63

        # authority and speeds
        self.authority = auth
        self.currentSpeed = 0
        self.suggSpeed = speed
        self.commandedSpeed = self.track.getLine(self.line).getBlock('63').speedLimit
        self.commandedPower = power
        self.actSpeed = actSpeed
        self.acc = 0.5
        self.numPassengers = 0

        # mass info
        self.baseMass = 81950 * .453 # kgs 

        trainThread = Thread(target=self.sendSpeeds)
        trainThread.start()
        trainThread.join()

    def sendSpeeds(self):
        while True:
            print('actual speed: ' + str(self.actSpeed) + ' commanded speed: ' + str(self.commandedSpeed))
            self.trainController.getSpeed(self.actSpeed, self.commandedSpeed)
            time.sleep(1)
        
    def getPower(self, power):
        self.commandedPower = power
        #print('got power: ' + str(power))

        # calculate mass -> each passenger weighs 150  + train weight in grams
        M = (self.numPassengers*150) + self.baseMass
        theta = math.degrees(math.atan(track.getLine('Green').getBlock(str(self.location)).elevation))

        # calculate force
        force = 0.5 * self.baseMass

        self.actualSpeed = self.commandedPower / force