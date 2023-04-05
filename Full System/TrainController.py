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

        # connect signals
        signals.trainControllerUpdateCurrSpeed.connect(self.updateCurrSpeed)
        signals.trainControllerEmerBrake.connect(self.EmerBrake)

        self.Ki = 1000
        self.Kp = 1000

        self.UkPrev = 0
        self.EkPrev = 0
        self.T = 1
        self.commandedPower = 0
        self.currentSpeed = 0
        self.train = None

    def updateCurrSpeed(self, train, currSpeed):
        print('current speed updated')
        self.currentSpeed = currSpeed
        self.train = train

    def sendPower(self):
        if self.train.actSpeed == 0:
            self.commandedPower = 120000
            signals.trainControllerSpeed.emit(self.train.actSpeed)
        else:
            # velocity error calcuation
            self.ek = self.train.commandedSpeed - self.train.actSpeed

            # calculate uk
            self.uk = self.UkPrev + ((self.T/2) * (self.ek + self.EkPrev))

            self.commandedPower = (self.Kp * self.ek) + (self.Ki * self.uk)

            self.UkPrev = self.uk
            self.EkPrev = self.ek

            # send actual speed #
            x = self.train.actSpeed * 2.237
            txt = f"{x:.2f}"
            self.y = float(txt)
            signals.trainControllerSpeed.emit(self.y)

        if self.commandedPower > 120000:
            self.commandedPower = 120000

        signals.trainModelGetPower.emit(self.train, self.commandedPower)
        signals.trainControllerPower.emit(self.commandedPower)

    def EmerBrake(self):
        if signals.trainControllerEmerBrake == True:
            self.commandedPower = 0
            signals.trainModelGetPower.emit( self.train, self.commandedPower)
            print("Emergency Brake applied, power set to 0")