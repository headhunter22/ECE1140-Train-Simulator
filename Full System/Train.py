from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from TrainController import TrainController
from threading import Thread
import time
import math

class Train(QObject):
    trainCounter = 0

    def __init__(self, id, line, destBlock):
        super().__init__()

        self.trainController = trainController
        self.trainController.powerToTrain.connect(self.getPower)

        self.track = track

        #self.clock = clock
        #self.clock.clock.timeout.connect(self.sendSpeeds)

        # id
        self.ID = ID

        # location attributes
        self.line = line
        self.block = 63

        # authority and speeds
        self.authority = auth
        self.currentSpeed = 0
        self.suggSpeed = speed
        self.commandedSpeed = self.track.getLine(self.line).getBlock('63').speedLimit
        self.commandedPower = power
        self.actSpeed = actSpeed
        self.numPassengers = 0

        #power calculation vars
        self.An_1 = .5
        self.An = 0
        self.actSpeed_1 = track.getLine(self.line).getBlock(str(self.location)).speedLimit

        # mass info
        self.baseMass = 81950 * .453 # kgs

    def sendSpeeds(self):
        print('actual speed: ' + str(self.actSpeed) + ' commanded speed: ' + str(self.commandedSpeed))
        self.trainController.getSpeed(self.actSpeed, self.commandedSpeed)
        
    def getPower(self, power):
        self.commandedPower = power
        #print('got power: ' + str(power))

        # calculate mass -> each passenger weighs 150  + train weight in grams
        M = (self.numPassengers*150) + self.baseMass
        theta = math.degrees(math.atan(self.track.getLine('Green').getBlock(str(self.location)).elevation))
        g = 9.8 #  m/s^2
        friction = .006
        self.An = ((M*g*math.cos(theta)*friction) + (M*g*math.cos(theta)) + F_b + (self.commandedPower/self.actSpeed_1) )/M

        # calculate force
        force = 0.5 * self.baseMass

        self.actualSpeed = self.commandedPower / force