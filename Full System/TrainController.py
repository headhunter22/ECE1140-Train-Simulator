import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Track import Track
import time

class TrainController(QObject):

    powerToTrain = pyqtSignal(float)

    def __init__(self): 
        super().__init__()
        self.authority = 0

        self.Ki = 0.4
        self.Kp = 0.14

        self.UkPrev = 120
        self.EkPrev = 50 # change to actual speed limit
        self.T = 1e-8

    def getSpeed(self, actualSpeed, commandedSpeed):
        self.actualSpeed = actualSpeed
        self.commandedSpeed = commandedSpeed
        self.sendPower()
        print('actual speed: ' + str(self.actualSpeed))
        
    """ def sendPower(self):  
        ek = self.commandedSpeed - self.actualSpeed
        uk = self.UkPrev + ((self.T/2) * (ek + self.EkPrev))

        powerOut = (self.Kp * ek) + (self.Ki * uk)

        self.powerToTrain.emit(powerOut)

        self.UkPrev = uk
        self.EkPrev = ek """

    def sendPower(self):
        if self.actualSpeed < self.commandedSpeed:
            powerOut = 120000
        else:
            powerOut = 0
            
        self.powerToTrain.emit(powerOut)