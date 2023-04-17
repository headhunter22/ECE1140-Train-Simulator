import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Track import Track
import time
from Clock import Clock
from signals import signals
from simple_pid import PID
from Train import Train

class TrainController(QObject):  

    def __init__(self):
        super().__init__()

        # connect signals
        signals.trainControllerUpdateCurrSpeed.connect(self.updateCurrSpeed)
        signals.trainControllerEmerBrake.connect(self.EmerBrake)
        signals.trainControllerUIKP.connect(self.updateKP)
        signals.trainControllerUIKI.connect(self.updateKI)
        signals.trainModelGUIcommandedSpeed.connect(self.sendPower)

        self.Ki = 10
        self.Kp = 1000

        self.UkPrev = 0
        self.EkPrev = 0
        self.T = 1
        self.commandedPower = 0
        self.currentSpeed = 0
        self.train = None
        
        signals.trainControllerKP.emit(self.Kp)
        signals.trainControllerKI.emit(self.Ki)

    def updateCurrSpeed(self, train, currSpeed):
        print('current speed updated')
        self.currentSpeed = currSpeed
        self.train = train

    def sendPower(self, train):
        #the train is moving and not stopped at a station
        self.commSpeed = float(train) * 0.621
        self.pid = PID(self.Kp, self.Ki, 0, self.commSpeed, 1)
        self.StopTime = self.train.actSpeed / 1.2
        self.StopDistance = self.StopTime * 0.5 * self.train.actSpeed
        signals.trainControllerAuthority.emit(self.train.authority)
        # print('authority: ' + str(self.train.commandedSpeed))
        # print('stopDistance: ' + str(self.train.actSpeed * 3.6))
    
        if self.train.authority < 0:
            self.train.authority = 10000

        if self.train.authority <= self.StopDistance:
            # print('authority = ' + str(self.train.authority))
            # print('distance = ' + str(self.StopDistance))
            # print("auth less than dist")
            self.commandedPower = 0
            signals.trainControllerServiceBrake.emit(True)

        if self.train.actSpeed == 0: #beginning state; train is not moving
            self.commandedPower = 120000
            signals.trainControllerSpeed.emit(self.train.actSpeed)
        else:
            # # velocity error calcuation
            # self.ek = (self.train.commandedSpeed * .2777) - self.train.actSpeed
            # print('commanded speed: ' + str(self.train.commandedSpeed))
            # print('actual speed: ' + str(self.train.actSpeed * 3.6))
            # print('ek: ' + str(self.ek))

            # # calculate uk
            # self.uk = self.UkPrev + ((self.T/2) * (self.ek + self.EkPrev))

            # self.commandedPower = (self.Kp * self.ek) + (self.Ki * self.uk)

            # self.UkPrev = self.uk
            # self.EkPrev = self.ek

            self.control = self.pid(self.currentSpeed)
            

            # send actual speed #
            x = self.train.actSpeed * 2.237
            txt = f"{x:.2f}"
            self.y = float(txt)
            signals.trainControllerSpeed.emit(self.y)

        if self.commandedPower > 120000:
            self.commandedPower = 120000

        signals.trainModelGetPower.emit(self.train, self.control)
        signals.trainControllerPower.emit(self.commandedPower)

    def EmerBrake(self):
        if signals.trainControllerEmerBrake == True:
            self.commandedPower = 0
            signals.trainModelGetPower.emit( self.train, self.commandedPower)
            print("Emergency Brake applied, power set to 0")

    def updateKP(self, kp):
        self.Kp = kp

    def updateKI(self, ki):
        self.Ki = ki