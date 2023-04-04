import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Track import Track
import time
from Clock import Clock
from signals import signals

class TrainController(QObject):  

    def __init__(self):
        super().__init__()
        print('train controller created')

        # connect signals
        signals.trainControllerUpdateCurrSpeed.connect(self.updateCurrSpeed)

        self.Ki = 0.4
        self.Kp = 0.14

        self.UkPrev = 120
        self.EkPrev = 50 # change to actual speed limit
        self.T = 0.2
        self.commandedPower = 0
        self.currentSpeed = 0
        self.train = None

    def updateCurrSpeed(self, train, currSpeed):
        print('current speed updated')
        self.currentSpeed = currSpeed
        self.train = train

    def sendPower(self, power):
        print('sending power')
        # velocity error calcuation
        self.ek = self.train.commandedSpeed - self.train.actualSpeed

        # calculate uk
        self.uk = self.UkPrev + ((self.T/2) * (ek + self.EkPrev))

        self.commandedPower = (self.Kp * ek) + (self.Ki * uk)

        self.UkPrev = uk
        self.EkPrev = ek

        signals.trainModelGetPower.emit(self.commandedPower)