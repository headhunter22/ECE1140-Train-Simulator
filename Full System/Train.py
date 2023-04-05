from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from threading import Thread
import time
import math

class Train(QObject):
    trainCounter = 0

    def __init__(self, id, line, destBlock):
        super().__init__()

        self.route = []

        # id
        self.ID = id

        # location attributes
        self.line = line
        self.block = 63
        self.position = 0.0

        # authority and speeds
        self.authority = 3
        self.currentSpeed = 0
        self.suggSpeed = 70
        self.commandedSpeed = 0
        self.commandedPower = 0
        self.actSpeed = 0
        self.numPassengers = 0
        self.serviceBrake = 0
        self.emBrake = 0

        #power calculation vars
        self.An_1 = 0
        self.An = 0
        self.actSpeed_1 = 0
        self.T = 1

        # mass info
        self.baseMass = 81950 # kgs

    # def sendSpeeds(self):
    #     print('actual speed: ' + str(self.actSpeed) + ' commanded speed: ' + str(self.commandedSpeed))
    #     self.trainController.getSpeed(self.actSpeed, self.commandedSpeed)
        
    # def getPower(self, power):
    #     self.commandedPower = power
    #     #print('got power: ' + str(power))

    #     # calculate mass -> each passenger weighs 150  + train weight in grams
    #     M = (self.numPassengers*150) + self.baseMass
    #     theta = math.degrees(math.atan(self.track.getLine('Green').getBlock(str(self.location)).elevation))
    #     g = 9.8 #  m/s^2
    #     friction = .006
    #     #calculating the braking force
    #     if self.emBrake == 1:
    #         F_b = -2.73
    #     elif self.serviceBrake == 1:
    #         F_b = -1.2
    #     else:
    #         F_b = 0

    #     self.An = ((M*g*math.cos(theta)*friction) + (M*g*math.cos(theta)) + F_b + (self.commandedPower/self.actSpeed_1) )/M
    #     self.actSpeed = self.actSpeed_1 + self.T/2 *(self.An - self.An_1)
    #     self.An_1 = self.An
    #     self.actSpeed_1 = self.actSpeed

    #     # calculate force
    #     force = 0.5 * self.baseMass

    #     self.actualSpeed = self.commandedPower / force