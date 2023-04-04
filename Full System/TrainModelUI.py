import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track
from Train import Train
from TrainController import TrainController
from signals import signals

class TrainModelUI(QObject):
    def __init__(self):
        super().__init__()

        signals.SIGNALNAME.connect(self.displayPower)
        signals.SIGNALNAME.connect(self.displaySpeed)
        
    def displayPower(self):
        self.powLabel.setText("Power Input: {0} Watts".format(SIGNALNAME))

    def displaySpeed(self):
        self.actSpeed.setText("Power Input: {0} Watts".format(SIGNALNAME))
        