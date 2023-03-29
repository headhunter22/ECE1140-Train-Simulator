import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Track import Track
import time

class TrainController(QObject):

    powerToTrain = pyqtSignal(int)

    def __init__(self): 
        super().__init__()

    def getSpeed(self, actualSpeed, commandedSpeed):
        self.actualSpeed = actualSpeed
        print('actual speed: ' + str(self.actualSpeed))
        print('power: power')
        self.powerToTrain.emit(120)